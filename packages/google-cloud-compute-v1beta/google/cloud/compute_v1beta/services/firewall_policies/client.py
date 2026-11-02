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

from google.cloud.compute_v1beta.services.firewall_policies import pagers
from google.cloud.compute_v1beta.types import compute

from .transports.base import DEFAULT_CLIENT_INFO, FirewallPoliciesTransport
from .transports.rest import FirewallPoliciesRestTransport


class FirewallPoliciesClientMeta(type):
    """Metaclass for the FirewallPolicies client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[FirewallPoliciesTransport]]
    _transport_registry["rest"] = FirewallPoliciesRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[FirewallPoliciesTransport]:
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


class FirewallPoliciesClient(metaclass=FirewallPoliciesClientMeta):
    """The FirewallPolicies API."""

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
            FirewallPoliciesClient: The constructed client.
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
            FirewallPoliciesClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> FirewallPoliciesTransport:
        """Returns the transport used by the client instance.

        Returns:
            FirewallPoliciesTransport: The transport used by the client
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
                str, FirewallPoliciesTransport, Callable[..., FirewallPoliciesTransport]
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the firewall policies client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,FirewallPoliciesTransport,Callable[..., FirewallPoliciesTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the FirewallPoliciesTransport constructor.
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
        self._client_cert_source = FirewallPoliciesClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=FirewallPoliciesClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, FirewallPoliciesTransport)
        if transport_provided:
            # transport is a FirewallPoliciesTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(FirewallPoliciesTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=FirewallPoliciesClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=FirewallPoliciesClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=FirewallPoliciesClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[FirewallPoliciesTransport],
                Callable[..., FirewallPoliciesTransport],
            ] = (
                FirewallPoliciesClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., FirewallPoliciesTransport], transport)
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
                    "Created client `google.cloud.compute_v1beta.FirewallPoliciesClient`.",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.FirewallPolicies",
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
                        "serviceName": "google.cloud.compute.v1beta.FirewallPolicies",
                        "credentialsType": None,
                    },
                )

    def add_association_unary(
        self,
        request: Optional[
            Union[compute.AddAssociationFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_association_resource: Optional[
            compute.FirewallPolicyAssociation
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Inserts an association for the specified firewall
        policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddAssociationFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.add_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddAssociationFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.AddAssociation. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_association_resource (google.cloud.compute_v1beta.types.FirewallPolicyAssociation):
                The body resource for this request
                This corresponds to the ``firewall_policy_association_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_association_resource]
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
        if not isinstance(request, compute.AddAssociationFirewallPolicyRequest):
            request = compute.AddAssociationFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_association_resource is not None:
                request.firewall_policy_association_resource = (
                    firewall_policy_association_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
            Union[compute.AddAssociationFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_association_resource: Optional[
            compute.FirewallPolicyAssociation
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Inserts an association for the specified firewall
        policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddAssociationFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.add_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddAssociationFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.AddAssociation. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_association_resource (google.cloud.compute_v1beta.types.FirewallPolicyAssociation):
                The body resource for this request
                This corresponds to the ``firewall_policy_association_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_association_resource]
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
        if not isinstance(request, compute.AddAssociationFirewallPolicyRequest):
            request = compute.AddAssociationFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_association_resource is not None:
                request.firewall_policy_association_resource = (
                    firewall_policy_association_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def add_packet_mirroring_rule_unary(
        self,
        request: Optional[
            Union[compute.AddPacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Inserts a packet mirroring rule into a firewall
        policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_add_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddPacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.add_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddPacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.AddPacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
        if not isinstance(request, compute.AddPacketMirroringRuleFirewallPolicyRequest):
            request = compute.AddPacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.add_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def add_packet_mirroring_rule(
        self,
        request: Optional[
            Union[compute.AddPacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Inserts a packet mirroring rule into a firewall
        policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_add_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddPacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.add_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddPacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.AddPacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
        if not isinstance(request, compute.AddPacketMirroringRuleFirewallPolicyRequest):
            request = compute.AddPacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.add_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.AddRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Inserts a rule into a firewall policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.add_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.AddRule. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
        if not isinstance(request, compute.AddRuleFirewallPolicyRequest):
            request = compute.AddRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.AddRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Inserts a rule into a firewall policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.AddRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.add_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.AddRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.AddRule. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
        if not isinstance(request, compute.AddRuleFirewallPolicyRequest):
            request = compute.AddRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def clone_rules_unary(
        self,
        request: Optional[Union[compute.CloneRulesFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Copies rules to the specified firewall policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_clone_rules():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.CloneRulesFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.clone_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.CloneRulesFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.CloneRules. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.CloneRulesFirewallPolicyRequest):
            request = compute.CloneRulesFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.clone_rules]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def clone_rules(
        self,
        request: Optional[Union[compute.CloneRulesFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Copies rules to the specified firewall policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_clone_rules():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.CloneRulesFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.clone_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.CloneRulesFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.CloneRules. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.CloneRulesFirewallPolicyRequest):
            request = compute.CloneRulesFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.clone_rules]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.DeleteFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Deletes the specified policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.DeleteFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.DeleteFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Delete. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                delete.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.DeleteFirewallPolicyRequest):
            request = compute.DeleteFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.DeleteFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes the specified policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.DeleteFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.delete(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.DeleteFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Delete. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                delete.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.DeleteFirewallPolicyRequest):
            request = compute.DeleteFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.GetFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.FirewallPolicy:
        r"""Returns the specified firewall policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.get(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Get. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to get.
                This corresponds to the ``firewall_policy`` field
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
            google.cloud.compute_v1beta.types.FirewallPolicy:
                Represents a Firewall Policy
                resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.GetFirewallPolicyRequest):
            request = compute.GetFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
            Union[compute.GetAssociationFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.FirewallPolicyAssociation:
        r"""Gets an association with the specified name.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetAssociationFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.get_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetAssociationFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.GetAssociation. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to which
                the queried rule belongs.

                This corresponds to the ``firewall_policy`` field
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
            google.cloud.compute_v1beta.types.FirewallPolicyAssociation:

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.GetAssociationFirewallPolicyRequest):
            request = compute.GetAssociationFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def get_iam_policy(
        self,
        request: Optional[
            Union[compute.GetIamPolicyFirewallPolicyRequest, dict]
        ] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Policy:
        r"""Gets the access control policy for a resource. May be
        empty if no such policy or resource exists.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_get_iam_policy():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetIamPolicyFirewallPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetIamPolicyFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.GetIamPolicy. See the
                method description for details.
            resource (str):
                Name or id of the resource for this
                request.

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
            google.cloud.compute_v1beta.types.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

                   **YAML example:**

                   :literal:``     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\ \`

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource]
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
        if not isinstance(request, compute.GetIamPolicyFirewallPolicyRequest):
            request = compute.GetIamPolicyFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if resource is not None:
                request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

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

    def get_packet_mirroring_rule(
        self,
        request: Optional[
            Union[compute.GetPacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.FirewallPolicyRule:
        r"""Gets a packet mirroring rule of the specified
        priority.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_get_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetPacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.get_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetPacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.GetPacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to which
                the queried rule belongs.

                This corresponds to the ``firewall_policy`` field
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
            google.cloud.compute_v1beta.types.FirewallPolicyRule:
                Represents a rule that describes one
                or more match conditions along with the
                action to be taken when traffic matches
                this condition (allow or deny).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.GetPacketMirroringRuleFirewallPolicyRequest):
            request = compute.GetPacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.GetRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.FirewallPolicyRule:
        r"""Gets a rule of the specified priority.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.GetRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.get_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.GetRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.GetRule. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to which
                the queried rule belongs.

                This corresponds to the ``firewall_policy`` field
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
            google.cloud.compute_v1beta.types.FirewallPolicyRule:
                Represents a rule that describes one
                or more match conditions along with the
                action to be taken when traffic matches
                this condition (allow or deny).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.GetRuleFirewallPolicyRequest):
            request = compute.GetRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.InsertFirewallPolicyRequest, dict]] = None,
        *,
        parent_id: Optional[str] = None,
        firewall_policy_resource: Optional[compute.FirewallPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Creates a new policy in the specified project using
        the data included in the request.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.InsertFirewallPolicyRequest(
                    parent_id="parent_id_value",
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.InsertFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Insert. See the method
                description for details.
            parent_id (str):
                Parent ID for this request. The ID can be either be
                "folders/[FOLDER_ID]" if the parent is a folder or
                "organizations/[ORGANIZATION_ID]" if the parent is an
                organization.

                This corresponds to the ``parent_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_resource (google.cloud.compute_v1beta.types.FirewallPolicy):
                The body resource for this request
                This corresponds to the ``firewall_policy_resource`` field
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
        flattened_params = [parent_id, firewall_policy_resource]
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
        if not isinstance(request, compute.InsertFirewallPolicyRequest):
            request = compute.InsertFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent_id is not None:
                request.parent_id = parent_id
            if firewall_policy_resource is not None:
                request.firewall_policy_resource = firewall_policy_resource

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
        request: Optional[Union[compute.InsertFirewallPolicyRequest, dict]] = None,
        *,
        parent_id: Optional[str] = None,
        firewall_policy_resource: Optional[compute.FirewallPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Creates a new policy in the specified project using
        the data included in the request.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.InsertFirewallPolicyRequest(
                    parent_id="parent_id_value",
                )

                # Make the request
                response = client.insert(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.InsertFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Insert. See the method
                description for details.
            parent_id (str):
                Parent ID for this request. The ID can be either be
                "folders/[FOLDER_ID]" if the parent is a folder or
                "organizations/[ORGANIZATION_ID]" if the parent is an
                organization.

                This corresponds to the ``parent_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_resource (google.cloud.compute_v1beta.types.FirewallPolicy):
                The body resource for this request
                This corresponds to the ``firewall_policy_resource`` field
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
        flattened_params = [parent_id, firewall_policy_resource]
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
        if not isinstance(request, compute.InsertFirewallPolicyRequest):
            request = compute.InsertFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent_id is not None:
                request.parent_id = parent_id
            if firewall_policy_resource is not None:
                request.firewall_policy_resource = firewall_policy_resource

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
        request: Optional[Union[compute.ListFirewallPoliciesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPager:
        r"""Lists all the policies that have been configured for
        the specified folder or organization.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.ListFirewallPoliciesRequest(
                )

                # Make the request
                page_result = client.list(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.ListFirewallPoliciesRequest, dict]):
                The request object. A request message for
                FirewallPolicies.List. See the method
                description for details.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.services.firewall_policies.pagers.ListPager:
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.ListFirewallPoliciesRequest):
            request = compute.ListFirewallPoliciesRequest(request)

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
            Union[compute.ListAssociationsFirewallPolicyRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.FirewallPoliciesListAssociationsResponse:
        r"""Lists associations of a specified target, i.e.,
        organization or folder.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.ListAssociationsFirewallPolicyRequest(
                )

                # Make the request
                response = client.list_associations(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.ListAssociationsFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.ListAssociations. See
                the method description for details.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.compute_v1beta.types.FirewallPoliciesListAssociationsResponse:

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, compute.ListAssociationsFirewallPolicyRequest):
            request = compute.ListAssociationsFirewallPolicyRequest(request)

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

    def move_unary(
        self,
        request: Optional[Union[compute.MoveFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        parent_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Moves the specified firewall policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.MoveFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                    parent_id="parent_id_value",
                )

                # Make the request
                response = client.move(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.MoveFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Move. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            parent_id (str):
                The new parent of the firewall policy. The ID can be
                either be "folders/[FOLDER_ID]" if the parent is a
                folder or "organizations/[ORGANIZATION_ID]" if the
                parent is an organization.

                This corresponds to the ``parent_id`` field
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
        flattened_params = [firewall_policy, parent_id]
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
        if not isinstance(request, compute.MoveFirewallPolicyRequest):
            request = compute.MoveFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if parent_id is not None:
                request.parent_id = parent_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.move]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.MoveFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        parent_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Moves the specified firewall policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.MoveFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                    parent_id="parent_id_value",
                )

                # Make the request
                response = client.move(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.MoveFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Move. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            parent_id (str):
                The new parent of the firewall policy. The ID can be
                either be "folders/[FOLDER_ID]" if the parent is a
                folder or "organizations/[ORGANIZATION_ID]" if the
                parent is an organization.

                This corresponds to the ``parent_id`` field
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
        flattened_params = [firewall_policy, parent_id]
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
        if not isinstance(request, compute.MoveFirewallPolicyRequest):
            request = compute.MoveFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if parent_id is not None:
                request.parent_id = parent_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.move]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.PatchFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_resource: Optional[compute.FirewallPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Patches the specified policy with the data included
        in the request.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.patch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Patch. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_resource (google.cloud.compute_v1beta.types.FirewallPolicy):
                The body resource for this request
                This corresponds to the ``firewall_policy_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_resource]
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
        if not isinstance(request, compute.PatchFirewallPolicyRequest):
            request = compute.PatchFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_resource is not None:
                request.firewall_policy_resource = firewall_policy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.PatchFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_resource: Optional[compute.FirewallPolicy] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Patches the specified policy with the data included
        in the request.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.patch(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.Patch. See the method
                description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_resource (google.cloud.compute_v1beta.types.FirewallPolicy):
                The body resource for this request
                This corresponds to the ``firewall_policy_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_resource]
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
        if not isinstance(request, compute.PatchFirewallPolicyRequest):
            request = compute.PatchFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_resource is not None:
                request.firewall_policy_resource = firewall_policy_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def patch_packet_mirroring_rule_unary(
        self,
        request: Optional[
            Union[compute.PatchPacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Patches a packet mirroring rule of the specified
        priority.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_patch_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchPacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.patch_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchPacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.PatchPacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
            request, compute.PatchPacketMirroringRuleFirewallPolicyRequest
        ):
            request = compute.PatchPacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.patch_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def patch_packet_mirroring_rule(
        self,
        request: Optional[
            Union[compute.PatchPacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Patches a packet mirroring rule of the specified
        priority.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_patch_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchPacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.patch_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchPacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.PatchPacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
            request, compute.PatchPacketMirroringRuleFirewallPolicyRequest
        ):
            request = compute.PatchPacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.patch_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.PatchRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Patches a rule of the specified priority.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.patch_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.PatchRule. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
        if not isinstance(request, compute.PatchRuleFirewallPolicyRequest):
            request = compute.PatchRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.PatchRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        firewall_policy_rule_resource: Optional[compute.FirewallPolicyRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Patches a rule of the specified priority.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.PatchRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.patch_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.PatchRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.PatchRule. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            firewall_policy_rule_resource (google.cloud.compute_v1beta.types.FirewallPolicyRule):
                The body resource for this request
                This corresponds to the ``firewall_policy_rule_resource`` field
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
        flattened_params = [firewall_policy, firewall_policy_rule_resource]
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
        if not isinstance(request, compute.PatchRuleFirewallPolicyRequest):
            request = compute.PatchRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy
            if firewall_policy_rule_resource is not None:
                request.firewall_policy_rule_resource = firewall_policy_rule_resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.patch_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
            Union[compute.RemoveAssociationFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Removes an association for the specified firewall
        policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveAssociationFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.remove_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveAssociationFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.RemoveAssociation. See
                the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.RemoveAssociationFirewallPolicyRequest):
            request = compute.RemoveAssociationFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
            Union[compute.RemoveAssociationFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Removes an association for the specified firewall
        policy.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveAssociationFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.remove_association(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveAssociationFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.RemoveAssociation. See
                the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.RemoveAssociationFirewallPolicyRequest):
            request = compute.RemoveAssociationFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_association]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def remove_packet_mirroring_rule_unary(
        self,
        request: Optional[
            Union[compute.RemovePacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Deletes a packet mirroring rule of the specified
        priority.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_remove_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemovePacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.remove_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemovePacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.RemovePacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
            request, compute.RemovePacketMirroringRuleFirewallPolicyRequest
        ):
            request = compute.RemovePacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.remove_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def remove_packet_mirroring_rule(
        self,
        request: Optional[
            Union[compute.RemovePacketMirroringRuleFirewallPolicyRequest, dict]
        ] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes a packet mirroring rule of the specified
        priority.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_remove_packet_mirroring_rule():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemovePacketMirroringRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.remove_packet_mirroring_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemovePacketMirroringRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.RemovePacketMirroringRule.
                See the method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
            request, compute.RemovePacketMirroringRuleFirewallPolicyRequest
        ):
            request = compute.RemovePacketMirroringRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.remove_packet_mirroring_rule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.RemoveRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Operation:
        r"""Deletes a rule of the specified priority.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.remove_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.RemoveRule. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.RemoveRuleFirewallPolicyRequest):
            request = compute.RemoveRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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
        request: Optional[Union[compute.RemoveRuleFirewallPolicyRequest, dict]] = None,
        *,
        firewall_policy: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> extended_operation.ExtendedOperation:
        r"""Deletes a rule of the specified priority.

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
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.RemoveRuleFirewallPolicyRequest(
                    firewall_policy="firewall_policy_value",
                )

                # Make the request
                response = client.remove_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.RemoveRuleFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.RemoveRule. See the
                method description for details.
            firewall_policy (str):
                Name of the firewall policy to
                update.

                This corresponds to the ``firewall_policy`` field
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
        flattened_params = [firewall_policy]
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
        if not isinstance(request, compute.RemoveRuleFirewallPolicyRequest):
            request = compute.RemoveRuleFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if firewall_policy is not None:
                request.firewall_policy = firewall_policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.remove_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("firewall_policy", request.firewall_policy),)
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

    def set_iam_policy(
        self,
        request: Optional[
            Union[compute.SetIamPolicyFirewallPolicyRequest, dict]
        ] = None,
        *,
        resource: Optional[str] = None,
        global_organization_set_policy_request_resource: Optional[
            compute.GlobalOrganizationSetPolicyRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.Policy:
        r"""Sets the access control policy on the specified
        resource. Replaces any existing policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_set_iam_policy():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.SetIamPolicyFirewallPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.SetIamPolicyFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.SetIamPolicy. See the
                method description for details.
            resource (str):
                Name or id of the resource for this
                request.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            global_organization_set_policy_request_resource (google.cloud.compute_v1beta.types.GlobalOrganizationSetPolicyRequest):
                The body resource for this request
                This corresponds to the ``global_organization_set_policy_request_resource`` field
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
            google.cloud.compute_v1beta.types.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

                   **YAML example:**

                   :literal:``     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\ \`

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource, global_organization_set_policy_request_resource]
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
        if not isinstance(request, compute.SetIamPolicyFirewallPolicyRequest):
            request = compute.SetIamPolicyFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if resource is not None:
                request.resource = resource
            if global_organization_set_policy_request_resource is not None:
                request.global_organization_set_policy_request_resource = (
                    global_organization_set_policy_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

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

    def test_iam_permissions(
        self,
        request: Optional[
            Union[compute.TestIamPermissionsFirewallPolicyRequest, dict]
        ] = None,
        *,
        resource: Optional[str] = None,
        test_permissions_request_resource: Optional[
            compute.TestPermissionsRequest
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> compute.TestPermissionsResponse:
        r"""Returns permissions that a caller has on the
        specified resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import compute_v1beta

            def sample_test_iam_permissions():
                # Create a client
                client = compute_v1beta.FirewallPoliciesClient()

                # Initialize request argument(s)
                request = compute_v1beta.TestIamPermissionsFirewallPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.test_iam_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.compute_v1beta.types.TestIamPermissionsFirewallPolicyRequest, dict]):
                The request object. A request message for
                FirewallPolicies.TestIamPermissions. See
                the method description for details.
            resource (str):
                Name or id of the resource for this
                request.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            test_permissions_request_resource (google.cloud.compute_v1beta.types.TestPermissionsRequest):
                The body resource for this request
                This corresponds to the ``test_permissions_request_resource`` field
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
            google.cloud.compute_v1beta.types.TestPermissionsResponse:

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource, test_permissions_request_resource]
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
        if not isinstance(request, compute.TestIamPermissionsFirewallPolicyRequest):
            request = compute.TestIamPermissionsFirewallPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if resource is not None:
                request.resource = resource
            if test_permissions_request_resource is not None:
                request.test_permissions_request_resource = (
                    test_permissions_request_resource
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.test_iam_permissions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

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

    def __enter__(self) -> "FirewallPoliciesClient":
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

__all__ = ("FirewallPoliciesClient",)
