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
import functools
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
from google.api_core import extended_operation, gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.compute_v1beta import gapic_version as package_version
from google.cloud.compute_v1beta._compat import (
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

import google.api_core.extended_operation as extended_operation  # type: ignore

from google.cloud.compute_v1beta.services.organization_security_policies import pagers
from google.cloud.compute_v1beta.types import compute

from .transports.base import DEFAULT_CLIENT_INFO, OrganizationSecurityPoliciesTransport
from .transports.rest import OrganizationSecurityPoliciesRestTransport


class OrganizationSecurityPoliciesClientMeta(type):
    """Metaclass for the OrganizationSecurityPolicies client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[OrganizationSecurityPoliciesTransport]]
    _transport_registry["rest"] = OrganizationSecurityPoliciesRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[OrganizationSecurityPoliciesTransport]:
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


class OrganizationSecurityPoliciesClient(
    metaclass=OrganizationSecurityPoliciesClientMeta
):
    """The OrganizationSecurityPolicies API."""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "compute.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "compute.{UNIVERSE_DOMAIN}"
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
            OrganizationSecurityPoliciesClient: The constructed client.
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
            OrganizationSecurityPoliciesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> OrganizationSecurityPoliciesTransport:
        """Returns the transport used by the client instance.

        Returns:
            OrganizationSecurityPoliciesTransport: The transport used by the client
                instance.
        """
        return self._transport

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
                OrganizationSecurityPoliciesTransport,
                Callable[..., OrganizationSecurityPoliciesTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the organization security policies client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,OrganizationSecurityPoliciesTransport,Callable[..., OrganizationSecurityPoliciesTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the OrganizationSecurityPoliciesTransport constructor.
                If set to None, a transport is chosen automatically.
                NOTE: "rest" transport functionality is currently in a
                beta state (preview). We welcome your feedback via an
                issue in this library's source repository.
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
            OrganizationSecurityPoliciesClient._get_client_cert_source(
                self._client_options.client_cert_source, self._use_client_cert
            )
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=OrganizationSecurityPoliciesClient._DEFAULT_UNIVERSE,
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
            transport, OrganizationSecurityPoliciesTransport
        )
        if transport_provided:
            # transport is a OrganizationSecurityPoliciesTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(OrganizationSecurityPoliciesTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=OrganizationSecurityPoliciesClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=OrganizationSecurityPoliciesClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=OrganizationSecurityPoliciesClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[OrganizationSecurityPoliciesTransport],
                Callable[..., OrganizationSecurityPoliciesTransport],
            ] = (
                OrganizationSecurityPoliciesClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(
                    Callable[..., OrganizationSecurityPoliciesTransport], transport
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
                    "Created client `google.cloud.compute_v1beta.OrganizationSecurityPoliciesClient`.",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.OrganizationSecurityPolicies",
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
                        "serviceName": "google.cloud.compute.v1beta.OrganizationSecurityPolicies",
                        "credentialsType": None,
                    },
                )

    def add_association_unary(
        self,
        request: Optional[
            Union[compute.AddAssociationOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_association_resource: Optional[
            compute.SecurityPolicyAssociation
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Inserts an association for the specified security
        policy.
        This has billing implications.  Projects in the
        hierarchy with effective hierarchical security policies
        will be automatically enrolled into Cloud Armor
        Enterprise if not already enrolled.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.addAssociation
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_add_association():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddAssociationOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.add_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddAssociationOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.AddAssociation.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_association_resource (google.cloud.compute_v1beta.types.SecurityPolicyAssociation):
                The body resource for this request
                This corresponds to the ``security_policy_association_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_association_resource]
        has_flattened_params = (
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
            request, compute.AddAssociationOrganizationSecurityPolicyRequest
        ):
            request = compute.AddAssociationOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_association_resource is not None:
                request.security_policy_association_resource = (
                    security_policy_association_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def add_association(
        self,
        request: Optional[
            Union[compute.AddAssociationOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_association_resource: Optional[
            compute.SecurityPolicyAssociation
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Inserts an association for the specified security
        policy.
        This has billing implications.  Projects in the
        hierarchy with effective hierarchical security policies
        will be automatically enrolled into Cloud Armor
        Enterprise if not already enrolled.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.addAssociation
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_add_association():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddAssociationOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.add_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddAssociationOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.AddAssociation.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_association_resource (google.cloud.compute_v1beta.types.SecurityPolicyAssociation):
                The body resource for this request
                This corresponds to the ``security_policy_association_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_association_resource]
        has_flattened_params = (
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
            request, compute.AddAssociationOrganizationSecurityPolicyRequest
        ):
            request = compute.AddAssociationOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_association_resource is not None:
                request.security_policy_association_resource = (
                    security_policy_association_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def add_rule_unary(
        self,
        request: Optional[
            Union[compute.AddRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_rule_resource: Optional[compute.SecurityPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Inserts a rule into a security policy.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.addRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_add_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.add_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.AddRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_rule_resource (google.cloud.compute_v1beta.types.SecurityPolicyRule):
                The body resource for this request
                This corresponds to the ``security_policy_rule_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_rule_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.AddRuleOrganizationSecurityPolicyRequest):
            request = compute.AddRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_rule_resource is not None:
                request.security_policy_rule_resource = security_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def add_rule(
        self,
        request: Optional[
            Union[compute.AddRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_rule_resource: Optional[compute.SecurityPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Inserts a rule into a security policy.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.addRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_add_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.add_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.AddRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_rule_resource (google.cloud.compute_v1beta.types.SecurityPolicyRule):
                The body resource for this request
                This corresponds to the ``security_policy_rule_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_rule_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.AddRuleOrganizationSecurityPolicyRequest):
            request = compute.AddRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_rule_resource is not None:
                request.security_policy_rule_resource = security_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def copy_rules_unary(
        self,
        request: Optional[
            Union[compute.CopyRulesOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Copies rules to the specified security policy.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.cloneRules instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_copy_rules():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.CopyRulesOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.copy_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.CopyRulesOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.CopyRules.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.CopyRulesOrganizationSecurityPolicyRequest):
            request = compute.CopyRulesOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.copy_rules]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def copy_rules(
        self,
        request: Optional[
            Union[compute.CopyRulesOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Copies rules to the specified security policy.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.cloneRules instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_copy_rules():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.CopyRulesOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.copy_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.CopyRulesOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.CopyRules.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.CopyRulesOrganizationSecurityPolicyRequest):
            request = compute.CopyRulesOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.copy_rules]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def delete_unary(
        self,
        request: Optional[
            Union[compute.DeleteOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Deletes the specified policy.

        Use this API to remove Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to remove
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.delete instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_delete():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.DeleteOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.DeleteOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Delete. See
                the method description for details.
            security_policy (str):
                Name of the security policy to
                delete.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.DeleteOrganizationSecurityPolicyRequest):
            request = compute.DeleteOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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
            Union[compute.DeleteOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes the specified policy.

        Use this API to remove Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to remove
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.delete instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_delete():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.DeleteOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.DeleteOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Delete. See
                the method description for details.
            security_policy (str):
                Name of the security policy to
                delete.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.DeleteOrganizationSecurityPolicyRequest):
            request = compute.DeleteOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def get(
        self,
        request: Optional[
            Union[compute.GetOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.SecurityPolicy:
        r"""List all of the ordered rules present in a single
        specified policy.
        Use this API to read Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to read
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.get instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_get():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.get(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Get. See
                the method description for details.
            security_policy (str):
                Name of the security policy to get.
                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.types.SecurityPolicy:
                Represents a Google Cloud Armor
                security policy resource.
                Only external backend services that use
                load balancers can reference a security
                policy. For more information, see Google
                Cloud Armor security policy overview.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.GetOrganizationSecurityPolicyRequest):
            request = compute.GetOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def get_association(
        self,
        request: Optional[
            Union[compute.GetAssociationOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.SecurityPolicyAssociation:
        r"""Gets an association with the specified name.

        Use this API to read Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to read
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.getAssociation
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_get_association():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetAssociationOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.get_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetAssociationOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.GetAssociation.
                See the method description for details.
            security_policy (str):
                Name of the security policy to which
                the queried rule belongs.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.types.SecurityPolicyAssociation:

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
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
            request, compute.GetAssociationOrganizationSecurityPolicyRequest
        ):
            request = compute.GetAssociationOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def get_rule(
        self,
        request: Optional[
            Union[compute.GetRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.SecurityPolicyRule:
        r"""Gets a rule at the specified priority.

        Use this API to read Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to read
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.getRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_get_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.get_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.GetRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to which
                the queried rule belongs.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.types.SecurityPolicyRule:
                Represents a rule that describes one
                or more match conditions along with the
                action to be taken when traffic matches
                this condition (allow or deny).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.GetRuleOrganizationSecurityPolicyRequest):
            request = compute.GetRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def insert_unary(
        self,
        request: Optional[
            Union[compute.InsertOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy_resource: Optional[compute.SecurityPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Creates a new policy in the specified organization
        using the data included in the request.

        Use this API to add Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to add
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.insert instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_insert():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.InsertOrganizationSecurityPolicyRequest(
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.InsertOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Insert. See
                the method description for details.
            security_policy_resource (google.cloud.compute_v1beta.types.SecurityPolicy):
                The body resource for this request
                This corresponds to the ``security_policy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.InsertOrganizationSecurityPolicyRequest):
            request = compute.InsertOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy_resource is not None:
                request.security_policy_resource = security_policy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

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
            Union[compute.InsertOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy_resource: Optional[compute.SecurityPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Creates a new policy in the specified organization
        using the data included in the request.

        Use this API to add Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to add
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.insert instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_insert():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.InsertOrganizationSecurityPolicyRequest(
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.InsertOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Insert. See
                the method description for details.
            security_policy_resource (google.cloud.compute_v1beta.types.SecurityPolicy):
                The body resource for this request
                This corresponds to the ``security_policy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.InsertOrganizationSecurityPolicyRequest):
            request = compute.InsertOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy_resource is not None:
                request.security_policy_resource = security_policy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.insert]

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.parent_id = request.parent_id
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def list(
        self,
        request: Optional[
            Union[compute.ListOrganizationSecurityPoliciesRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPager:
        r"""List all the policies that have been configured for
        the specified organization.

        Use this API to read Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to read
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.list instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_list():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.ListOrganizationSecurityPoliciesRequest(
                )

                # Make the request
                page_result = client.list(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.ListOrganizationSecurityPoliciesRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.List. See
                the method description for details.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.services.organization_security_policies.pagers.ListPager:
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.ListOrganizationSecurityPoliciesRequest):
            request = compute.ListOrganizationSecurityPoliciesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list]

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

    def list_associations(
        self,
        request: Optional[
            Union[compute.ListAssociationsOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.OrganizationSecurityPoliciesListAssociationsResponse:
        r"""Lists associations of a specified target, i.e.,
        organization or folder.
        Use this API to read Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to read
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.listAssociations
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_list_associations():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.ListAssociationsOrganizationSecurityPolicyRequest(
                )

                # Make the request
                response = client.list_associations(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.ListAssociationsOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.ListAssociations.
                See the method description for details.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.types.OrganizationSecurityPoliciesListAssociationsResponse:

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, compute.ListAssociationsOrganizationSecurityPolicyRequest
        ):
            request = compute.ListAssociationsOrganizationSecurityPolicyRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_associations]

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

    def list_preconfigured_expression_sets(
        self,
        request: Optional[
            Union[
                compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,
                dict,
            ]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.SecurityPoliciesListPreconfiguredExpressionSetsResponse:
        r"""Gets the current list of preconfigured Web
        Application Firewall (WAF) expressions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_list_preconfigured_expression_sets():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest(
                )

                # Make the request
                response = client.list_preconfigured_expression_sets(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.ListPreconfiguredExpressionSets.
                See the method description for details.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.types.SecurityPoliciesListPreconfiguredExpressionSetsResponse:

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request,
            compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,
        ):
            request = compute.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_preconfigured_expression_sets
        ]

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

    def move_unary(
        self,
        request: Optional[
            Union[compute.MoveOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Moves the specified security policy.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.move instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_move():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.MoveOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.move(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.MoveOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Move. See
                the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.MoveOrganizationSecurityPolicyRequest):
            request = compute.MoveOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.move]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def move(
        self,
        request: Optional[
            Union[compute.MoveOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Moves the specified security policy.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.move instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_move():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.MoveOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.move(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.MoveOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Move. See
                the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.MoveOrganizationSecurityPolicyRequest):
            request = compute.MoveOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.move]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.parent_id = request.parent_id
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def patch_unary(
        self,
        request: Optional[
            Union[compute.PatchOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_resource: Optional[compute.SecurityPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Patches the specified policy with the data included
        in the request.
        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.patch instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_patch():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.patch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Patch. See
                the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_resource (google.cloud.compute_v1beta.types.SecurityPolicy):
                The body resource for this request
                This corresponds to the ``security_policy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.PatchOrganizationSecurityPolicyRequest):
            request = compute.PatchOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_resource is not None:
                request.security_policy_resource = security_policy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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
            Union[compute.PatchOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_resource: Optional[compute.SecurityPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Patches the specified policy with the data included
        in the request.
        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.patch instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_patch():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.patch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.Patch. See
                the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_resource (google.cloud.compute_v1beta.types.SecurityPolicy):
                The body resource for this request
                This corresponds to the ``security_policy_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.PatchOrganizationSecurityPolicyRequest):
            request = compute.PatchOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_resource is not None:
                request.security_policy_resource = security_policy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def patch_rule_unary(
        self,
        request: Optional[
            Union[compute.PatchRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_rule_resource: Optional[compute.SecurityPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Patches a rule at the specified priority.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.patchRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_patch_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.patch_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.PatchRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_rule_resource (google.cloud.compute_v1beta.types.SecurityPolicyRule):
                The body resource for this request
                This corresponds to the ``security_policy_rule_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_rule_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.PatchRuleOrganizationSecurityPolicyRequest):
            request = compute.PatchRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_rule_resource is not None:
                request.security_policy_rule_resource = security_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def patch_rule(
        self,
        request: Optional[
            Union[compute.PatchRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        security_policy_rule_resource: Optional[compute.SecurityPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Patches a rule at the specified priority.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.patchRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_patch_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.patch_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.PatchRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            security_policy_rule_resource (google.cloud.compute_v1beta.types.SecurityPolicyRule):
                The body resource for this request
                This corresponds to the ``security_policy_rule_resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy, security_policy_rule_resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.PatchRuleOrganizationSecurityPolicyRequest):
            request = compute.PatchRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy
            if security_policy_rule_resource is not None:
                request.security_policy_rule_resource = security_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def remove_association_unary(
        self,
        request: Optional[
            Union[compute.RemoveAssociationOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Removes an association for the specified security
        policy.
        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.removeAssociation
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_remove_association():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveAssociationOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.remove_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveAssociationOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.RemoveAssociation.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
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
            request, compute.RemoveAssociationOrganizationSecurityPolicyRequest
        ):
            request = compute.RemoveAssociationOrganizationSecurityPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def remove_association(
        self,
        request: Optional[
            Union[compute.RemoveAssociationOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Removes an association for the specified security
        policy.
        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.removeAssociation
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_remove_association():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveAssociationOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.remove_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveAssociationOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.RemoveAssociation.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
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
            request, compute.RemoveAssociationOrganizationSecurityPolicyRequest
        ):
            request = compute.RemoveAssociationOrganizationSecurityPolicyRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def remove_rule_unary(
        self,
        request: Optional[
            Union[compute.RemoveRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Deletes a rule at the specified priority.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.removeRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_remove_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.remove_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.RemoveRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.RemoveRuleOrganizationSecurityPolicyRequest):
            request = compute.RemoveRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

    def remove_rule(
        self,
        request: Optional[
            Union[compute.RemoveRuleOrganizationSecurityPolicyRequest, dict]
        ] = None,
        *,
        security_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes a rule at the specified priority.

        Use this API to modify Cloud Armor policies. Previously,
        alpha and beta versions of this API were used to modify
        firewall policies. This usage is now disabled for most
        organizations. Use firewallPolicies.removeRule instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_remove_rule():
                # Create a client
                client = compute_v1beta.OrganizationSecurityPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveRuleOrganizationSecurityPolicyRequest(
                    security_policy="security_policy_value",
                )

                # Make the request
                response = client.remove_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveRuleOrganizationSecurityPolicyRequest, dict]):
                The request object. A request message for
                OrganizationSecurityPolicies.RemoveRule.
                See the method description for details.
            security_policy (str):
                Name of the security policy to
                update.

                This corresponds to the ``security_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.extended_operation.ExtendedOperation:
                An object representing a extended
                long-running operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [security_policy]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.RemoveRuleOrganizationSecurityPolicyRequest):
            request = compute.RemoveRuleOrganizationSecurityPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if security_policy is not None:
                request.security_policy = security_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("security_policy", request.security_policy),)
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

        operation_service = self._transport._global_organization_operations_client
        operation_request = compute.GetGlobalOrganizationOperationRequest()
        operation_request.operation = response.name

        get_operation = functools.partial(operation_service.get, operation_request)
        # Cancel is not part of extended operations yet.
        cancel_operation = lambda: None

        # Note: this class is an implementation detail to provide a uniform
        # set of names for certain fields in the extended operation proto message.
        # See google.api_core.extended_operation.ExtendedOperation for details
        # on these properties and the  expected interface.
        class _CustomOperation(extended_operation.ExtendedOperation):
            @property
            def error_message(self):
                return self._extended_operation.http_error_message

            @property
            def error_code(self):
                return self._extended_operation.http_error_status_code

        response = _CustomOperation.make(get_operation, cancel_operation, response)

        # Done; return the response.
        return response

    def __enter__(self) -> "OrganizationSecurityPoliciesClient":
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

__all__ = ("OrganizationSecurityPoliciesClient",)
