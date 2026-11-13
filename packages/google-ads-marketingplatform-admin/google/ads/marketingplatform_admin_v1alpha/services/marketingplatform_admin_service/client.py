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

from google.ads.marketingplatform_admin_v1alpha import gapic_version as package_version
from google.ads.marketingplatform_admin_v1alpha._compat import (
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

from google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service import (
    pagers,
)
from google.ads.marketingplatform_admin_v1alpha.types import (
    marketingplatform_admin,
    resources,
)

from .transports.base import DEFAULT_CLIENT_INFO, MarketingplatformAdminServiceTransport
from .transports.grpc import MarketingplatformAdminServiceGrpcTransport
from .transports.grpc_asyncio import MarketingplatformAdminServiceGrpcAsyncIOTransport
from .transports.rest import MarketingplatformAdminServiceRestTransport


class MarketingplatformAdminServiceClientMeta(type):
    """Metaclass for the MarketingplatformAdminService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[MarketingplatformAdminServiceTransport]]
    _transport_registry["grpc"] = MarketingplatformAdminServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = (
        MarketingplatformAdminServiceGrpcAsyncIOTransport
    )
    _transport_registry["rest"] = MarketingplatformAdminServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[MarketingplatformAdminServiceTransport]:
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


class MarketingplatformAdminServiceClient(
    metaclass=MarketingplatformAdminServiceClientMeta
):
    """Service Interface for the Google Marketing Platform Admin
    API.
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "marketingplatformadmin.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "marketingplatformadmin.{UNIVERSE_DOMAIN}"
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
            MarketingplatformAdminServiceClient: The constructed client.
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
            MarketingplatformAdminServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> MarketingplatformAdminServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            MarketingplatformAdminServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def account_path(
        account: str,
    ) -> str:
        """Returns a fully-qualified account string."""
        return "accounts/{account}".format(
            account=account,
        )

    @staticmethod
    def parse_account_path(path: str) -> Dict[str, str]:
        """Parses a account path into its component segments."""
        m = re.match(r"^accounts/(?P<account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def admin_access_binding_path(
        organization: str,
        admin_access_binding: str,
    ) -> str:
        """Returns a fully-qualified admin_access_binding string."""
        return "organizations/{organization}/adminAccessBindings/{admin_access_binding}".format(
            organization=organization,
            admin_access_binding=admin_access_binding,
        )

    @staticmethod
    def parse_admin_access_binding_path(path: str) -> Dict[str, str]:
        """Parses a admin_access_binding path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/adminAccessBindings/(?P<admin_access_binding>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def analytics_account_link_path(
        organization: str,
        analytics_account_link: str,
    ) -> str:
        """Returns a fully-qualified analytics_account_link string."""
        return "organizations/{organization}/analyticsAccountLinks/{analytics_account_link}".format(
            organization=organization,
            analytics_account_link=analytics_account_link,
        )

    @staticmethod
    def parse_analytics_account_link_path(path: str) -> Dict[str, str]:
        """Parses a analytics_account_link path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/analyticsAccountLinks/(?P<analytics_account_link>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_organization_path(path: str) -> Dict[str, str]:
        """Parses a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def property_path(
        property: str,
    ) -> str:
        """Returns a fully-qualified property string."""
        return "properties/{property}".format(
            property=property,
        )

    @staticmethod
    def parse_property_path(path: str) -> Dict[str, str]:
        """Parses a property path into its component segments."""
        m = re.match(r"^properties/(?P<property>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def user_group_path(
        organization: str,
        user_group: str,
    ) -> str:
        """Returns a fully-qualified user_group string."""
        return "organizations/{organization}/userGroups/{user_group}".format(
            organization=organization,
            user_group=user_group,
        )

    @staticmethod
    def parse_user_group_path(path: str) -> Dict[str, str]:
        """Parses a user_group path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/userGroups/(?P<user_group>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def user_group_member_path(
        organization: str,
        user_group: str,
        member: str,
    ) -> str:
        """Returns a fully-qualified user_group_member string."""
        return "organizations/{organization}/userGroups/{user_group}/members/{member}".format(
            organization=organization,
            user_group=user_group,
            member=member,
        )

    @staticmethod
    def parse_user_group_member_path(path: str) -> Dict[str, str]:
        """Parses a user_group_member path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/userGroups/(?P<user_group>.+?)/members/(?P<member>.+?)$",
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
                MarketingplatformAdminServiceTransport,
                Callable[..., MarketingplatformAdminServiceTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the marketingplatform admin service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,MarketingplatformAdminServiceTransport,Callable[..., MarketingplatformAdminServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the MarketingplatformAdminServiceTransport constructor.
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
            MarketingplatformAdminServiceClient._get_client_cert_source(
                self._client_options.client_cert_source, self._use_client_cert
            )
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=MarketingplatformAdminServiceClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(
            transport, MarketingplatformAdminServiceTransport
        )
        if transport_provided:
            # transport is a MarketingplatformAdminServiceTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(MarketingplatformAdminServiceTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=MarketingplatformAdminServiceClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=MarketingplatformAdminServiceClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=MarketingplatformAdminServiceClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[MarketingplatformAdminServiceTransport],
                Callable[..., MarketingplatformAdminServiceTransport],
            ] = (
                MarketingplatformAdminServiceClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(
                    Callable[..., MarketingplatformAdminServiceTransport], transport
                )
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
                    "Created client `google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient`.",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
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
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "credentialsType": None,
                    },
                )

    def get_organization(
        self,
        request: Optional[
            Union[marketingplatform_admin.GetOrganizationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Organization:
        r"""Looks up a single organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_get_organization():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.GetOrganizationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_organization(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.GetOrganizationRequest, dict]):
                The request object. Request message for GetOrganization
                RPC.
            name (str):
                Required. The name of the Organization to retrieve.
                Format: organizations/{org_id}

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
            google.ads.marketingplatform_admin_v1alpha.types.Organization:
                A resource message representing a
                Google Marketing Platform organization.

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
        if not isinstance(request, marketingplatform_admin.GetOrganizationRequest):
            request = marketingplatform_admin.GetOrganizationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_organization]

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

    def list_organizations(
        self,
        request: Optional[
            Union[marketingplatform_admin.ListOrganizationsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListOrganizationsPager:
        r"""Returns a list of organizations that the user has
        access to.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_list_organizations():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.ListOrganizationsRequest(
                )

                # Make the request
                page_result = client.list_organizations(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.ListOrganizationsRequest, dict]):
                The request object. Request message for ListOrganizations
                RPC.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.pagers.ListOrganizationsPager:
                Response message for
                ListOrganizations RPC.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, marketingplatform_admin.ListOrganizationsRequest):
            request = marketingplatform_admin.ListOrganizationsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_organizations]

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
        response = pagers.ListOrganizationsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def find_sales_partner_managed_clients(
        self,
        request: Optional[
            Union[marketingplatform_admin.FindSalesPartnerManagedClientsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> marketingplatform_admin.FindSalesPartnerManagedClientsResponse:
        r"""Returns a list of clients managed by the sales
        partner organization.
        User needs to be an OrgAdmin/BillingAdmin on the sales
        partner organization in order to view the end clients.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_find_sales_partner_managed_clients():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.FindSalesPartnerManagedClientsRequest(
                    organization="organization_value",
                )

                # Make the request
                response = client.find_sales_partner_managed_clients(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.FindSalesPartnerManagedClientsRequest, dict]):
                The request object. Request message for
                FindSalesPartnerManagedClients RPC.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.FindSalesPartnerManagedClientsResponse:
                Response message for
                FindSalesPartnerManagedClients RPC.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, marketingplatform_admin.FindSalesPartnerManagedClientsRequest
        ):
            request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.find_sales_partner_managed_clients
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("organization", request.organization),)
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

    def list_analytics_account_links(
        self,
        request: Optional[
            Union[marketingplatform_admin.ListAnalyticsAccountLinksRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAnalyticsAccountLinksPager:
        r"""Lists the Google Analytics accounts link to the
        specified Google Marketing Platform organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_list_analytics_account_links():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.ListAnalyticsAccountLinksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_analytics_account_links(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.ListAnalyticsAccountLinksRequest, dict]):
                The request object. Request message for
                ListAnalyticsAccountLinks RPC.
            parent (str):
                Required. The parent organization, which owns this
                collection of Analytics account links. Format:
                organizations/{org_id}

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
            google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.pagers.ListAnalyticsAccountLinksPager:
                Response message for
                ListAnalyticsAccountLinks RPC.
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
            request, marketingplatform_admin.ListAnalyticsAccountLinksRequest
        ):
            request = marketingplatform_admin.ListAnalyticsAccountLinksRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_analytics_account_links
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
        response = pagers.ListAnalyticsAccountLinksPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_analytics_account_link(
        self,
        request: Optional[
            Union[marketingplatform_admin.CreateAnalyticsAccountLinkRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        analytics_account_link: Optional[resources.AnalyticsAccountLink] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AnalyticsAccountLink:
        r"""Creates the link between the Analytics account and
        the Google Marketing Platform organization.

        User needs to be an org user, and admin on the Analytics
        account to create the link. If the account is already
        linked to an organization, user needs to unlink the
        account from the current organization, then try link
        again.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_create_analytics_account_link():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                analytics_account_link = marketingplatform_admin_v1alpha.AnalyticsAccountLink()
                analytics_account_link.analytics_account = "analytics_account_value"

                request = marketingplatform_admin_v1alpha.CreateAnalyticsAccountLinkRequest(
                    parent="parent_value",
                    analytics_account_link=analytics_account_link,
                )

                # Make the request
                response = client.create_analytics_account_link(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.CreateAnalyticsAccountLinkRequest, dict]):
                The request object. Request message for
                CreateAnalyticsAccountLink RPC.
            parent (str):
                Required. The parent resource where this Analytics
                account link will be created. Format:
                organizations/{org_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            analytics_account_link (google.ads.marketingplatform_admin_v1alpha.types.AnalyticsAccountLink):
                Required. The Analytics account link
                to create.

                This corresponds to the ``analytics_account_link`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.AnalyticsAccountLink:
                A resource message representing the
                link between a Google Analytics account
                and a Google Marketing Platform
                organization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, analytics_account_link]
        has_flattened_params = (
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
            request, marketingplatform_admin.CreateAnalyticsAccountLinkRequest
        ):
            request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if analytics_account_link is not None:
                request.analytics_account_link = analytics_account_link

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_analytics_account_link
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

    def delete_analytics_account_link(
        self,
        request: Optional[
            Union[marketingplatform_admin.DeleteAnalyticsAccountLinkRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the AnalyticsAccountLink, which detaches the
        Analytics account from the Google Marketing Platform
        organization.

        User needs to be an org user, and admin on the Analytics
        account in order to delete the link.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_delete_analytics_account_link():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.DeleteAnalyticsAccountLinkRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_analytics_account_link(request=request)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.DeleteAnalyticsAccountLinkRequest, dict]):
                The request object. Request message for
                DeleteAnalyticsAccountLink RPC.
            name (str):
                Required. The name of the Analytics account link to
                delete. Format:
                organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}

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
            request, marketingplatform_admin.DeleteAnalyticsAccountLinkRequest
        ):
            request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_analytics_account_link
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

    def set_property_service_level(
        self,
        request: Optional[
            Union[marketingplatform_admin.SetPropertyServiceLevelRequest, dict]
        ] = None,
        *,
        analytics_account_link: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> marketingplatform_admin.SetPropertyServiceLevelResponse:
        r"""Updates the service level for an Analytics property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_set_property_service_level():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.SetPropertyServiceLevelRequest(
                    analytics_account_link="analytics_account_link_value",
                    analytics_property="analytics_property_value",
                    service_level="ANALYTICS_SERVICE_LEVEL_360",
                )

                # Make the request
                response = client.set_property_service_level(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.SetPropertyServiceLevelRequest, dict]):
                The request object. Request message for
                SetPropertyServiceLevel RPC.
            analytics_account_link (str):
                Required. The parent AnalyticsAccountLink scope where
                this property is in. Format:
                organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}

                This corresponds to the ``analytics_account_link`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.SetPropertyServiceLevelResponse:
                Response message for
                SetPropertyServiceLevel RPC.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [analytics_account_link]
        has_flattened_params = (
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
            request, marketingplatform_admin.SetPropertyServiceLevelRequest
        ):
            request = marketingplatform_admin.SetPropertyServiceLevelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if analytics_account_link is not None:
                request.analytics_account_link = analytics_account_link

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.set_property_service_level
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("analytics_account_link", request.analytics_account_link),)
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

    def report_property_usage(
        self,
        request: Optional[
            Union[marketingplatform_admin.ReportPropertyUsageRequest, dict]
        ] = None,
        *,
        organization: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> marketingplatform_admin.ReportPropertyUsageResponse:
        r"""Gets the usage and billing data for properties within
        the organization for the specified month.

        Per direct client org, user needs to be
        OrgAdmin/BillingAdmin on the organization in order to
        view the billing and usage data.

        Per sales partner client org, user needs to be
        OrgAdmin/BillingAdmin on the sales partner org in order
        to view the billing and usage data, or
        OrgAdmin/BillingAdmin on the sales partner client org in
        order to view the usage data only.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_report_property_usage():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.ReportPropertyUsageRequest(
                    organization="organization_value",
                    month="month_value",
                )

                # Make the request
                response = client.report_property_usage(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.ReportPropertyUsageRequest, dict]):
                The request object. Request message for
                ReportPropertyUsage RPC.
            organization (str):
                Required. Specifies the organization whose property
                usage will be listed.

                Format: organizations/{org_id}

                This corresponds to the ``organization`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.ReportPropertyUsageResponse:
                Response message for
                ReportPropertyUsage RPC.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [organization]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, marketingplatform_admin.ReportPropertyUsageRequest):
            request = marketingplatform_admin.ReportPropertyUsageRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if organization is not None:
                request.organization = organization

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.report_property_usage]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("organization", request.organization),)
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

    def get_user_group(
        self,
        request: Optional[
            Union[marketingplatform_admin.GetUserGroupRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.UserGroup:
        r"""Looks up a single user group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_get_user_group():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.GetUserGroupRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_user_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.GetUserGroupRequest, dict]):
                The request object. Request message for GetUserGroup RPC.
            name (str):
                Required. The name of the UserGroup to retrieve. Format:
                organizations/{org_id}/userGroups/{user_group_id}

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
            google.ads.marketingplatform_admin_v1alpha.types.UserGroup:
                A resource message representing a
                user group in a GMP organization.

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
        if not isinstance(request, marketingplatform_admin.GetUserGroupRequest):
            request = marketingplatform_admin.GetUserGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_user_group]

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

    def list_user_groups(
        self,
        request: Optional[
            Union[marketingplatform_admin.ListUserGroupsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserGroupsPager:
        r"""Returns a list of user groups in the specified GMP
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_list_user_groups():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.ListUserGroupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_groups(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupsRequest, dict]):
                The request object. Request message for ListUserGroups
                RPC.
            parent (str):
                Required. The parent org where this UserGroup will be
                listed. Format: organizations/{org_id}

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
            google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.pagers.ListUserGroupsPager:
                Response message for ListUserGroups
                RPC.
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
        if not isinstance(request, marketingplatform_admin.ListUserGroupsRequest):
            request = marketingplatform_admin.ListUserGroupsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_user_groups]

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
        response = pagers.ListUserGroupsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_user_group(
        self,
        request: Optional[
            Union[marketingplatform_admin.CreateUserGroupRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        user_group: Optional[resources.UserGroup] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.UserGroup:
        r"""Creates a user group in the specified GMP
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_create_user_group():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.CreateUserGroupRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_user_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.CreateUserGroupRequest, dict]):
                The request object. Request message for CreateUserGroup
                RPC.
            parent (str):
                Required. The parent resource where this UserGroup will
                be created. Format: organizations/{org_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_group (google.ads.marketingplatform_admin_v1alpha.types.UserGroup):
                Required. The user group to create.
                This corresponds to the ``user_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.UserGroup:
                A resource message representing a
                user group in a GMP organization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_group]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, marketingplatform_admin.CreateUserGroupRequest):
            request = marketingplatform_admin.CreateUserGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if user_group is not None:
                request.user_group = user_group

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_user_group]

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

    def update_user_group(
        self,
        request: Optional[
            Union[marketingplatform_admin.UpdateUserGroupRequest, dict]
        ] = None,
        *,
        user_group: Optional[resources.UserGroup] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.UserGroup:
        r"""Updates a user group in the specified GMP
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_update_user_group():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.UpdateUserGroupRequest(
                )

                # Make the request
                response = client.update_user_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.UpdateUserGroupRequest, dict]):
                The request object. Request message for UpdateUserGroup
                RPC.
            user_group (google.ads.marketingplatform_admin_v1alpha.types.UserGroup):
                Required. The user group to update.
                This corresponds to the ``user_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Field names must
                be in snake case (for example, "field_to_update").
                Omitted fields will not be updated. To replace the
                entire entity, use one path with the string "\*" to
                match all fields.

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
            google.ads.marketingplatform_admin_v1alpha.types.UserGroup:
                A resource message representing a
                user group in a GMP organization.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [user_group, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, marketingplatform_admin.UpdateUserGroupRequest):
            request = marketingplatform_admin.UpdateUserGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if user_group is not None:
                request.user_group = user_group
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_user_group]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("user_group.name", request.user_group.name),)
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

    def delete_user_group(
        self,
        request: Optional[
            Union[marketingplatform_admin.DeleteUserGroupRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a user group in the specified GMP
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_delete_user_group():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.DeleteUserGroupRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_user_group(request=request)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.DeleteUserGroupRequest, dict]):
                The request object. Request message for DeleteUserGroup
                RPC.
            name (str):
                Required. The name of the user group to delete. Format:
                organizations/{org_id}/userGroups/{user_group_id}

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
        if not isinstance(request, marketingplatform_admin.DeleteUserGroupRequest):
            request = marketingplatform_admin.DeleteUserGroupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_user_group]

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

    def get_user_group_member(
        self,
        request: Optional[
            Union[marketingplatform_admin.GetUserGroupMemberRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.UserGroupMember:
        r"""Looks up a single user group member.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_get_user_group_member():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.GetUserGroupMemberRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_user_group_member(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.GetUserGroupMemberRequest, dict]):
                The request object. Request message for
                GetUserGroupMember RPC.
            name (str):
                Required. The name of the user group member to retrieve.
                Format:
                organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}

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
            google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember:
                A resource message representing a
                member of a user group.

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
        if not isinstance(request, marketingplatform_admin.GetUserGroupMemberRequest):
            request = marketingplatform_admin.GetUserGroupMemberRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_user_group_member]

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

    def list_user_group_members(
        self,
        request: Optional[
            Union[marketingplatform_admin.ListUserGroupMembersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserGroupMembersPager:
        r"""Returns a list of members in the specified user
        group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_list_user_group_members():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.ListUserGroupMembersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_group_members(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.ListUserGroupMembersRequest, dict]):
                The request object. Request message for
                ListUserGroupMembers RPC.
            parent (str):
                Required. The parent user group where this
                UserGroupMember will be listed. Format:
                organizations/{org_id}/userGroups/{user_group_id}

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
            google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.pagers.ListUserGroupMembersPager:
                Response message for
                ListUserGroupMembers RPC.
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
        if not isinstance(request, marketingplatform_admin.ListUserGroupMembersRequest):
            request = marketingplatform_admin.ListUserGroupMembersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_user_group_members]

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
        response = pagers.ListUserGroupMembersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_user_group_member(
        self,
        request: Optional[
            Union[marketingplatform_admin.CreateUserGroupMemberRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        user_group_member: Optional[resources.UserGroupMember] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.UserGroupMember:
        r"""Adds a member to the specified GMP user group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_create_user_group_member():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                user_group_member = marketingplatform_admin_v1alpha.UserGroupMember()
                user_group_member.user_email = "user_email_value"

                request = marketingplatform_admin_v1alpha.CreateUserGroupMemberRequest(
                    parent="parent_value",
                    user_group_member=user_group_member,
                )

                # Make the request
                response = client.create_user_group_member(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.CreateUserGroupMemberRequest, dict]):
                The request object. Request message for
                CreateUserGroupMember RPC.
            parent (str):
                Required. The parent resource where this UserGroupMember
                will be created. Format:
                organizations/{org_id}/userGroups/{user_group_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_group_member (google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember):
                Required. The user group member to
                create.

                This corresponds to the ``user_group_member`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember:
                A resource message representing a
                member of a user group.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_group_member]
        has_flattened_params = (
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
            request, marketingplatform_admin.CreateUserGroupMemberRequest
        ):
            request = marketingplatform_admin.CreateUserGroupMemberRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if user_group_member is not None:
                request.user_group_member = user_group_member

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_user_group_member]

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

    def update_user_group_member(
        self,
        request: Optional[
            Union[marketingplatform_admin.UpdateUserGroupMemberRequest, dict]
        ] = None,
        *,
        user_group_member: Optional[resources.UserGroupMember] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.UserGroupMember:
        r"""Updates a member in the specified GMP user group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_update_user_group_member():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                user_group_member = marketingplatform_admin_v1alpha.UserGroupMember()
                user_group_member.user_email = "user_email_value"

                request = marketingplatform_admin_v1alpha.UpdateUserGroupMemberRequest(
                    user_group_member=user_group_member,
                )

                # Make the request
                response = client.update_user_group_member(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.UpdateUserGroupMemberRequest, dict]):
                The request object. Request message for
                UpdateUserGroupMember RPC.
            user_group_member (google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember):
                Required. The user group member to
                update.

                This corresponds to the ``user_group_member`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Field names must
                be in snake case (for example, "field_to_update").
                Omitted fields will not be updated. To replace the
                entire entity, use one path with the string "\*" to
                match all fields.

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
            google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember:
                A resource message representing a
                member of a user group.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [user_group_member, update_mask]
        has_flattened_params = (
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
            request, marketingplatform_admin.UpdateUserGroupMemberRequest
        ):
            request = marketingplatform_admin.UpdateUserGroupMemberRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if user_group_member is not None:
                request.user_group_member = user_group_member
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_user_group_member]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("user_group_member.name", request.user_group_member.name),)
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

    def delete_user_group_member(
        self,
        request: Optional[
            Union[marketingplatform_admin.DeleteUserGroupMemberRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a member in the specified GMP user group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_delete_user_group_member():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.DeleteUserGroupMemberRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_user_group_member(request=request)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.DeleteUserGroupMemberRequest, dict]):
                The request object. Request message for
                DeleteUserGroupMember RPC.
            name (str):
                Required. The name of the user group member to delete.
                Format:
                organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}

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
            request, marketingplatform_admin.DeleteUserGroupMemberRequest
        ):
            request = marketingplatform_admin.DeleteUserGroupMemberRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_user_group_member]

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

    def get_admin_access_binding(
        self,
        request: Optional[
            Union[marketingplatform_admin.GetAdminAccessBindingRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AdminAccessBinding:
        r"""Looks up a single admin access binding.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_get_admin_access_binding():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.GetAdminAccessBindingRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_admin_access_binding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.GetAdminAccessBindingRequest, dict]):
                The request object. Response message for
                GetAdminAccessBinding RPC.
            name (str):
                Required. The name of the AdminAccessBinding to
                retrieve. Format:
                organizations/{org_id}/adminAccessBindings/{admin_access_binding_id}

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
            google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding:
                A resource message representing a
                binding to a set of roles.

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
            request, marketingplatform_admin.GetAdminAccessBindingRequest
        ):
            request = marketingplatform_admin.GetAdminAccessBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_admin_access_binding]

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

    def list_admin_access_bindings(
        self,
        request: Optional[
            Union[marketingplatform_admin.ListAdminAccessBindingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAdminAccessBindingsPager:
        r"""Returns a list of admin access bindings in the
        specified GMP organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_list_admin_access_bindings():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                request = marketingplatform_admin_v1alpha.ListAdminAccessBindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_admin_access_bindings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.ListAdminAccessBindingsRequest, dict]):
                The request object. Request message for
                ListAdminAccessBindings RPC.
            parent (str):
                Required. The parent organization, which owns this
                collection of Admin Access Bindings. Format:
                organizations/{org_id}

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
            google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.pagers.ListAdminAccessBindingsPager:
                Response message for
                ListAdminAccessBindings RPC.
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
            request, marketingplatform_admin.ListAdminAccessBindingsRequest
        ):
            request = marketingplatform_admin.ListAdminAccessBindingsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_admin_access_bindings
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
        response = pagers.ListAdminAccessBindingsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_admin_access_binding(
        self,
        request: Optional[
            Union[marketingplatform_admin.CreateAdminAccessBindingRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        admin_access_binding: Optional[resources.AdminAccessBinding] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AdminAccessBinding:
        r"""Creates an admin access binding in the specified GMP
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_create_admin_access_binding():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                admin_access_binding = marketingplatform_admin_v1alpha.AdminAccessBinding()
                admin_access_binding.user_email = "user_email_value"

                request = marketingplatform_admin_v1alpha.CreateAdminAccessBindingRequest(
                    parent="parent_value",
                    admin_access_binding=admin_access_binding,
                )

                # Make the request
                response = client.create_admin_access_binding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.CreateAdminAccessBindingRequest, dict]):
                The request object. Request message for
                CreateAdminAccessBinding RPC.
            parent (str):
                Required. The parent organization, which owns this Admin
                Access Binding. Format: organizations/{org_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            admin_access_binding (google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding):
                Required. The Admin Access Binding to create.

                Only 'user_email' input is allowed.

                This corresponds to the ``admin_access_binding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding:
                A resource message representing a
                binding to a set of roles.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, admin_access_binding]
        has_flattened_params = (
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
            request, marketingplatform_admin.CreateAdminAccessBindingRequest
        ):
            request = marketingplatform_admin.CreateAdminAccessBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if admin_access_binding is not None:
                request.admin_access_binding = admin_access_binding

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_admin_access_binding
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

    def update_admin_access_binding(
        self,
        request: Optional[
            Union[marketingplatform_admin.UpdateAdminAccessBindingRequest, dict]
        ] = None,
        *,
        admin_access_binding: Optional[resources.AdminAccessBinding] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AdminAccessBinding:
        r"""Updates an admin access binding in the specified GMP
        organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import marketingplatform_admin_v1alpha

            def sample_update_admin_access_binding():
                # Create a client
                client = marketingplatform_admin_v1alpha.MarketingplatformAdminServiceClient()

                # Initialize request argument(s)
                admin_access_binding = marketingplatform_admin_v1alpha.AdminAccessBinding()
                admin_access_binding.user_email = "user_email_value"

                request = marketingplatform_admin_v1alpha.UpdateAdminAccessBindingRequest(
                    admin_access_binding=admin_access_binding,
                )

                # Make the request
                response = client.update_admin_access_binding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.marketingplatform_admin_v1alpha.types.UpdateAdminAccessBindingRequest, dict]):
                The request object. Request message for
                UpdateAdminAccessBinding RPC.
            admin_access_binding (google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding):
                Required. The AdminAccessBinding to
                update.

                This corresponds to the ``admin_access_binding`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Field names must
                be in snake case (for example, "field_to_update").
                Omitted fields will not be updated. To replace the
                entire entity, use one path with the string "\*" to
                match all fields.

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
            google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding:
                A resource message representing a
                binding to a set of roles.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [admin_access_binding, update_mask]
        has_flattened_params = (
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
            request, marketingplatform_admin.UpdateAdminAccessBindingRequest
        ):
            request = marketingplatform_admin.UpdateAdminAccessBindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if admin_access_binding is not None:
                request.admin_access_binding = admin_access_binding
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_admin_access_binding
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("admin_access_binding.name", request.admin_access_binding.name),)
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

    def __enter__(self) -> "MarketingplatformAdminServiceClient":
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

__all__ = ("MarketingplatformAdminServiceClient",)
