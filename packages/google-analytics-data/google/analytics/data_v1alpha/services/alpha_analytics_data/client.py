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

from google.analytics.data_v1alpha import gapic_version as package_version
from google.analytics.data_v1alpha._compat import (
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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.analytics.data_v1alpha.services.alpha_analytics_data import pagers
from google.analytics.data_v1alpha.types import analytics_data_api, data

from .transports.base import DEFAULT_CLIENT_INFO, AlphaAnalyticsDataTransport
from .transports.grpc import AlphaAnalyticsDataGrpcTransport
from .transports.grpc_asyncio import AlphaAnalyticsDataGrpcAsyncIOTransport
from .transports.rest import AlphaAnalyticsDataRestTransport


class AlphaAnalyticsDataClientMeta(type):
    """Metaclass for the AlphaAnalyticsData client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[AlphaAnalyticsDataTransport]]
    _transport_registry["grpc"] = AlphaAnalyticsDataGrpcTransport
    _transport_registry["grpc_asyncio"] = AlphaAnalyticsDataGrpcAsyncIOTransport
    _transport_registry["rest"] = AlphaAnalyticsDataRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[AlphaAnalyticsDataTransport]:
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


class AlphaAnalyticsDataClient(metaclass=AlphaAnalyticsDataClientMeta):
    """Google Analytics reporting data service."""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "analyticsdata.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "analyticsdata.{UNIVERSE_DOMAIN}"
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
            AlphaAnalyticsDataClient: The constructed client.
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
            AlphaAnalyticsDataClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> AlphaAnalyticsDataTransport:
        """Returns the transport used by the client instance.

        Returns:
            AlphaAnalyticsDataTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def audience_list_path(
        property: str,
        audience_list: str,
    ) -> str:
        """Returns a fully-qualified audience_list string."""
        return "properties/{property}/audienceLists/{audience_list}".format(
            property=property,
            audience_list=audience_list,
        )

    @staticmethod
    def parse_audience_list_path(path: str) -> Dict[str, str]:
        """Parses a audience_list path into its component segments."""
        m = re.match(
            r"^properties/(?P<property>.+?)/audienceLists/(?P<audience_list>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def metadata_path(
        property: str,
    ) -> str:
        """Returns a fully-qualified metadata string."""
        return "properties/{property}/metadata".format(
            property=property,
        )

    @staticmethod
    def parse_metadata_path(path: str) -> Dict[str, str]:
        """Parses a metadata path into its component segments."""
        m = re.match(r"^properties/(?P<property>.+?)/metadata$", path)
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
    def property_quotas_snapshot_path(
        property: str,
    ) -> str:
        """Returns a fully-qualified property_quotas_snapshot string."""
        return "properties/{property}/propertyQuotasSnapshot".format(
            property=property,
        )

    @staticmethod
    def parse_property_quotas_snapshot_path(path: str) -> Dict[str, str]:
        """Parses a property_quotas_snapshot path into its component segments."""
        m = re.match(r"^properties/(?P<property>.+?)/propertyQuotasSnapshot$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def recurring_audience_list_path(
        property: str,
        recurring_audience_list: str,
    ) -> str:
        """Returns a fully-qualified recurring_audience_list string."""
        return "properties/{property}/recurringAudienceLists/{recurring_audience_list}".format(
            property=property,
            recurring_audience_list=recurring_audience_list,
        )

    @staticmethod
    def parse_recurring_audience_list_path(path: str) -> Dict[str, str]:
        """Parses a recurring_audience_list path into its component segments."""
        m = re.match(
            r"^properties/(?P<property>.+?)/recurringAudienceLists/(?P<recurring_audience_list>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def report_task_path(
        property: str,
        report_task: str,
    ) -> str:
        """Returns a fully-qualified report_task string."""
        return "properties/{property}/reportTasks/{report_task}".format(
            property=property,
            report_task=report_task,
        )

    @staticmethod
    def parse_report_task_path(path: str) -> Dict[str, str]:
        """Parses a report_task path into its component segments."""
        m = re.match(
            r"^properties/(?P<property>.+?)/reportTasks/(?P<report_task>.+?)$", path
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
                AlphaAnalyticsDataTransport,
                Callable[..., AlphaAnalyticsDataTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the alpha analytics data client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AlphaAnalyticsDataTransport,Callable[..., AlphaAnalyticsDataTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AlphaAnalyticsDataTransport constructor.
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
        self._client_cert_source = AlphaAnalyticsDataClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=AlphaAnalyticsDataClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, AlphaAnalyticsDataTransport)
        if transport_provided:
            # transport is a AlphaAnalyticsDataTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(AlphaAnalyticsDataTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=AlphaAnalyticsDataClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=AlphaAnalyticsDataClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=AlphaAnalyticsDataClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[AlphaAnalyticsDataTransport],
                Callable[..., AlphaAnalyticsDataTransport],
            ] = (
                AlphaAnalyticsDataClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., AlphaAnalyticsDataTransport], transport)
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
                    "Created client `google.analytics.data_v1alpha.AlphaAnalyticsDataClient`.",
                    extra={
                        "serviceName": "google.analytics.data.v1alpha.AlphaAnalyticsData",
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
                        "serviceName": "google.analytics.data.v1alpha.AlphaAnalyticsData",
                        "credentialsType": None,
                    },
                )

    def run_funnel_report(
        self,
        request: Optional[
            Union[analytics_data_api.RunFunnelReportRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunFunnelReportResponse:
        r"""Returns a customized funnel report of your Google Analytics
        event data. The data returned from the API is as a table with
        columns for the requested dimensions and metrics.

        Funnel exploration lets you visualize the steps your users take
        to complete a task and quickly see how well they are succeeding
        or failing at each step. For example, how do prospects become
        shoppers and then become buyers? How do one time buyers become
        repeat buyers? With this information, you can improve
        inefficient or abandoned customer journeys. To learn more, see
        `GA4 Funnel
        Explorations <https://support.google.com/analytics/answer/9327974>`__.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Data API Funnel Reporting
        Feedback <https://docs.google.com/forms/d/e/1FAIpQLSdwOlQDJAUoBiIgUZZ3S_Lwi8gr7Bb0k1jhvc-DEg7Rol3UjA/viewform>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_run_funnel_report():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.RunFunnelReportRequest(
                )

                # Make the request
                response = client.run_funnel_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.RunFunnelReportRequest, dict]):
                The request object. The request for a funnel report.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1alpha.types.RunFunnelReportResponse:
                The funnel report response contains
                two sub reports. The two sub reports are
                different combinations of dimensions and
                metrics.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.RunFunnelReportRequest):
            request = analytics_data_api.RunFunnelReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.run_funnel_report]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

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

    def create_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.CreateAudienceListRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        audience_list: Optional[analytics_data_api.AudienceList] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates an audience list for later retrieval. This method
        quickly returns the audience list's resource name and initiates
        a long running asynchronous request to form an audience list. To
        list the users in an audience list, first create the audience
        list through this method and then send the audience resource
        name to the ``QueryAudienceList`` method.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        An audience list is a snapshot of the users currently in the
        audience at the time of audience list creation. Creating
        audience lists for one audience on different days will return
        different results as users enter and exit the audience.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.
        Audience lists contain the users in each audience.

        This method is available at beta stability at
        `audienceExports.create <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/create>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_create_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                audience_list = data_v1alpha.AudienceList()
                audience_list.audience = "audience_value"

                request = data_v1alpha.CreateAudienceListRequest(
                    parent="parent_value",
                    audience_list=audience_list,
                )

                # Make the request
                operation = client.create_audience_list(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.CreateAudienceListRequest, dict]):
                The request object. A request to create a new audience
                list.
            parent (str):
                Required. The parent resource where this audience list
                will be created. Format: ``properties/{property}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audience_list (google.analytics.data_v1alpha.types.AudienceList):
                Required. The audience list to
                create.

                This corresponds to the ``audience_list`` field
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

                The result type for the operation will be :class:`google.analytics.data_v1alpha.types.AudienceList` An audience list is a list of users in an audience at the time of the list's
                   creation. One audience may have multiple audience
                   lists created for different days.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, audience_list]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.CreateAudienceListRequest):
            request = analytics_data_api.CreateAudienceListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if audience_list is not None:
                request.audience_list = audience_list

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_audience_list]

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
            analytics_data_api.AudienceList,
            metadata_type=analytics_data_api.AudienceListMetadata,
        )

        # Done; return the response.
        return response

    def query_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.QueryAudienceListRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.QueryAudienceListResponse:
        r"""Retrieves an audience list of users. After creating an audience,
        the users are not immediately available for listing. First, a
        request to ``CreateAudienceList`` is necessary to create an
        audience list of users, and then second, this method is used to
        retrieve the users in the audience list.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        Audiences in Google Analytics 4 allow you to segment your users
        in the ways that are important to your business. To learn more,
        see https://support.google.com/analytics/answer/9267572.

        This method is available at beta stability at
        `audienceExports.query <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/query>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_query_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.QueryAudienceListRequest(
                    name="name_value",
                )

                # Make the request
                response = client.query_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.QueryAudienceListRequest, dict]):
                The request object. A request to list users in an
                audience list.
            name (str):
                Required. The name of the audience list to retrieve
                users from. Format:
                ``properties/{property}/audienceLists/{audience_list}``

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
            google.analytics.data_v1alpha.types.QueryAudienceListResponse:
                A list of users in an audience list.
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
        if not isinstance(request, analytics_data_api.QueryAudienceListRequest):
            request = analytics_data_api.QueryAudienceListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.query_audience_list]

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

    def get_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.GetAudienceListRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.AudienceList:
        r"""Gets configuration metadata about a specific audience list. This
        method can be used to understand an audience list after it has
        been created.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        This method is available at beta stability at
        `audienceExports.get <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/get>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_get_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetAudienceListRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.GetAudienceListRequest, dict]):
                The request object. A request to retrieve configuration
                metadata about a specific audience list.
            name (str):
                Required. The audience list resource name. Format:
                ``properties/{property}/audienceLists/{audience_list}``

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
            google.analytics.data_v1alpha.types.AudienceList:
                An audience list is a list of users
                in an audience at the time of the list's
                creation. One audience may have multiple
                audience lists created for different
                days.

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
        if not isinstance(request, analytics_data_api.GetAudienceListRequest):
            request = analytics_data_api.GetAudienceListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_audience_list]

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

    def list_audience_lists(
        self,
        request: Optional[
            Union[analytics_data_api.ListAudienceListsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAudienceListsPager:
        r"""Lists all audience lists for a property. This method can be used
        for you to find and reuse existing audience lists rather than
        creating unnecessary new audience lists. The same audience can
        have multiple audience lists that represent the list of users
        that were in an audience on different days.

        See `Creating an Audience
        List <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>`__
        for an introduction to Audience Lists with examples.

        This method is available at beta stability at
        `audienceExports.list <https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/list>`__.
        To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_list_audience_lists():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.ListAudienceListsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audience_lists(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.ListAudienceListsRequest, dict]):
                The request object. A request to list all audience lists
                for a property.
            parent (str):
                Required. All audience lists for this property will be
                listed in the response. Format:
                ``properties/{property}``

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
            google.analytics.data_v1alpha.services.alpha_analytics_data.pagers.ListAudienceListsPager:
                A list of all audience lists for a
                property.
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
        if not isinstance(request, analytics_data_api.ListAudienceListsRequest):
            request = analytics_data_api.ListAudienceListsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_audience_lists]

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
        response = pagers.ListAudienceListsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_recurring_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.CreateRecurringAudienceListRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        recurring_audience_list: Optional[
            analytics_data_api.RecurringAudienceList
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RecurringAudienceList:
        r"""Creates a recurring audience list. Recurring audience lists
        produces new audience lists each day. Audience lists are users
        in an audience at the time of the list's creation.

        A recurring audience list ensures that you have audience list
        based on the most recent data available for use each day. If you
        manually create audience list, you don't know when an audience
        list based on an additional day's data is available. This
        recurring audience list automates the creation of an audience
        list when an additional day's data is available. You will
        consume fewer quota tokens by using recurring audience list
        versus manually creating audience list at various times of day
        trying to guess when an additional day's data is ready.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_create_recurring_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                recurring_audience_list = data_v1alpha.RecurringAudienceList()
                recurring_audience_list.audience = "audience_value"

                request = data_v1alpha.CreateRecurringAudienceListRequest(
                    parent="parent_value",
                    recurring_audience_list=recurring_audience_list,
                )

                # Make the request
                response = client.create_recurring_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.CreateRecurringAudienceListRequest, dict]):
                The request object. A request to create a new recurring
                audience list.
            parent (str):
                Required. The parent resource where this recurring
                audience list will be created. Format:
                ``properties/{property}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            recurring_audience_list (google.analytics.data_v1alpha.types.RecurringAudienceList):
                Required. The recurring audience list
                to create.

                This corresponds to the ``recurring_audience_list`` field
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
            google.analytics.data_v1alpha.types.RecurringAudienceList:
                A recurring audience list produces
                new audience lists each day. Audience
                lists are users in an audience at the
                time of the list's creation. A recurring
                audience list ensures that you have
                audience list based on the most recent
                data available for use each day.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, recurring_audience_list]
        has_flattened_params = (
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
            request, analytics_data_api.CreateRecurringAudienceListRequest
        ):
            request = analytics_data_api.CreateRecurringAudienceListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if recurring_audience_list is not None:
                request.recurring_audience_list = recurring_audience_list

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_recurring_audience_list
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

    def get_recurring_audience_list(
        self,
        request: Optional[
            Union[analytics_data_api.GetRecurringAudienceListRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RecurringAudienceList:
        r"""Gets configuration metadata about a specific recurring audience
        list. This method can be used to understand a recurring audience
        list's state after it has been created. For example, a recurring
        audience list resource will generate audience list instances for
        each day, and this method can be used to get the resource name
        of the most recent audience list instance.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_get_recurring_audience_list():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetRecurringAudienceListRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_recurring_audience_list(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.GetRecurringAudienceListRequest, dict]):
                The request object. A request to retrieve configuration
                metadata about a specific recurring
                audience list.
            name (str):
                Required. The recurring audience list resource name.
                Format:
                ``properties/{property}/recurringAudienceLists/{recurring_audience_list}``

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
            google.analytics.data_v1alpha.types.RecurringAudienceList:
                A recurring audience list produces
                new audience lists each day. Audience
                lists are users in an audience at the
                time of the list's creation. A recurring
                audience list ensures that you have
                audience list based on the most recent
                data available for use each day.

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
        if not isinstance(request, analytics_data_api.GetRecurringAudienceListRequest):
            request = analytics_data_api.GetRecurringAudienceListRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_recurring_audience_list
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

    def list_recurring_audience_lists(
        self,
        request: Optional[
            Union[analytics_data_api.ListRecurringAudienceListsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRecurringAudienceListsPager:
        r"""Lists all recurring audience lists for a property. This method
        can be used for you to find and reuse existing recurring
        audience lists rather than creating unnecessary new recurring
        audience lists. The same audience can have multiple recurring
        audience lists that represent different dimension combinations;
        for example, just the dimension ``deviceId`` or both the
        dimensions ``deviceId`` and ``userId``.

        This method is introduced at alpha stability with the intention
        of gathering feedback on syntax and capabilities before entering
        beta. To give your feedback on this API, complete the `Google
        Analytics Audience Export API
        Feedback <https://forms.gle/EeA5u5LW6PEggtCEA>`__ form.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_list_recurring_audience_lists():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.ListRecurringAudienceListsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_recurring_audience_lists(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.ListRecurringAudienceListsRequest, dict]):
                The request object. A request to list all recurring
                audience lists for a property.
            parent (str):
                Required. All recurring audience lists for this property
                will be listed in the response. Format:
                ``properties/{property}``

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
            google.analytics.data_v1alpha.services.alpha_analytics_data.pagers.ListRecurringAudienceListsPager:
                A list of all recurring audience
                lists for a property.
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
            request, analytics_data_api.ListRecurringAudienceListsRequest
        ):
            request = analytics_data_api.ListRecurringAudienceListsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_recurring_audience_lists
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
        response = pagers.ListRecurringAudienceListsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_property_quotas_snapshot(
        self,
        request: Optional[
            Union[analytics_data_api.GetPropertyQuotasSnapshotRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.PropertyQuotasSnapshot:
        r"""Get all property quotas organized by quota category
        for a given property. This will charge 1 property quota
        from the category with the most quota.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_get_property_quotas_snapshot():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetPropertyQuotasSnapshotRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_property_quotas_snapshot(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.GetPropertyQuotasSnapshotRequest, dict]):
                The request object. A request to return the
                PropertyQuotasSnapshot for a given
                category.
            name (str):
                Required. Quotas from this property will be listed in
                the response. Format:
                ``properties/{property}/propertyQuotasSnapshot``

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
            google.analytics.data_v1alpha.types.PropertyQuotasSnapshot:
                Current state of all Property Quotas
                organized by quota category.

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
        if not isinstance(request, analytics_data_api.GetPropertyQuotasSnapshotRequest):
            request = analytics_data_api.GetPropertyQuotasSnapshotRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_property_quotas_snapshot
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

    def create_report_task(
        self,
        request: Optional[
            Union[analytics_data_api.CreateReportTaskRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        report_task: Optional[analytics_data_api.ReportTask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Initiates the creation of a report task. This method
        quickly returns a report task and initiates a long
        running asynchronous request to form a customized report
        of your Google Analytics event data.

        A report task will be retained and available for
        querying for 72 hours after it has been created.

        A report task created by one user can be listed and
        queried by all users who have access to the property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_create_report_task():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.CreateReportTaskRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_report_task(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.CreateReportTaskRequest, dict]):
                The request object. A request to create a report task.
            parent (str):
                Required. The parent resource where this report task
                will be created. Format: ``properties/{propertyId}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            report_task (google.analytics.data_v1alpha.types.ReportTask):
                Required. The report task
                configuration to create.

                This corresponds to the ``report_task`` field
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
                :class:`google.analytics.data_v1alpha.types.ReportTask`
                A specific report task configuration.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, report_task]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.CreateReportTaskRequest):
            request = analytics_data_api.CreateReportTaskRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if report_task is not None:
                request.report_task = report_task

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_report_task]

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
            analytics_data_api.ReportTask,
            metadata_type=analytics_data_api.ReportTaskMetadata,
        )

        # Done; return the response.
        return response

    def query_report_task(
        self,
        request: Optional[
            Union[analytics_data_api.QueryReportTaskRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.QueryReportTaskResponse:
        r"""Retrieves a report task's content. After requesting the
        ``CreateReportTask``, you are able to retrieve the report
        content once the report is ACTIVE. This method will return an
        error if the report task's state is not ``ACTIVE``. A query
        response will return the tabular row & column values of the
        report.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_query_report_task():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.QueryReportTaskRequest(
                    name="name_value",
                )

                # Make the request
                response = client.query_report_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.QueryReportTaskRequest, dict]):
                The request object. A request to fetch the report content
                for a report task.
            name (str):
                Required. The report source name. Format:
                ``properties/{property}/reportTasks/{report}``

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
            google.analytics.data_v1alpha.types.QueryReportTaskResponse:
                The report content corresponding to a
                report task.

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
        if not isinstance(request, analytics_data_api.QueryReportTaskRequest):
            request = analytics_data_api.QueryReportTaskRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.query_report_task]

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

    def get_report_task(
        self,
        request: Optional[Union[analytics_data_api.GetReportTaskRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.ReportTask:
        r"""Gets report metadata about a specific report task.
        After creating a report task, use this method to check
        its processing state or inspect its report definition.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_get_report_task():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetReportTaskRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_report_task(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.GetReportTaskRequest, dict]):
                The request object. A request to retrieve configuration
                metadata about a specific report task.
            name (str):
                Required. The report task resource name. Format:
                ``properties/{property}/reportTasks/{report_task}``

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
            google.analytics.data_v1alpha.types.ReportTask:
                A specific report task configuration.
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
        if not isinstance(request, analytics_data_api.GetReportTaskRequest):
            request = analytics_data_api.GetReportTaskRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_report_task]

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

    def list_report_tasks(
        self,
        request: Optional[
            Union[analytics_data_api.ListReportTasksRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListReportTasksPager:
        r"""Lists all report tasks for a property.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_list_report_tasks():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.ListReportTasksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_report_tasks(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.ListReportTasksRequest, dict]):
                The request object. A request to list all report tasks
                for a property.
            parent (str):
                Required. All report tasks for this property will be
                listed in the response. Format:
                ``properties/{property}``

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
            google.analytics.data_v1alpha.services.alpha_analytics_data.pagers.ListReportTasksPager:
                A list of all report tasks for a
                property.
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
        if not isinstance(request, analytics_data_api.ListReportTasksRequest):
            request = analytics_data_api.ListReportTasksRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_report_tasks]

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
        response = pagers.ListReportTasksPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def chat(
        self,
        request: Optional[Union[analytics_data_api.ChatRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.ChatResponse:
        r"""Provides a chat interface for interacting with Google Analytics
        data through the API.

        This product uses AI and may display inaccurate info. Your chat
        activity may be used to improve the product and your use is
        subject to Google's
        `Terms <https://policies.google.com/terms>`__, `AI Use
        Policy <https://policies.google.com/terms/generative-ai/use-policy>`__,
        and `Privacy Policy <https://policies.google.com/privacy>`__.
        `Learn more about Chat AI
        Privacy <https://support.google.com/helpguide/answer/14185196>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_chat():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.ChatRequest(
                    property="property_value",
                    user_query="user_query_value",
                )

                # Make the request
                response = client.chat(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.ChatRequest, dict]):
                The request object. Request message for the Chat method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1alpha.types.ChatResponse:
                Response message for the Chat method.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.ChatRequest):
            request = analytics_data_api.ChatRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.chat]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

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

    def run_report(
        self,
        request: Optional[Union[analytics_data_api.RunReportRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.RunReportResponse:
        r"""Returns a customized report of your Google Analytics
        event data. Reports contain statistics derived from data
        collected by the Google Analytics tracking code. The
        data returned from the API is as a table with columns
        for the requested dimensions and metrics. Metrics are
        individual measurements of user activity on your
        property, such as active users or event count.
        Dimensions break down metrics across some common
        criteria, such as country or event name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_run_report():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.RunReportRequest(
                    property="property_value",
                )

                # Make the request
                response = client.run_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.RunReportRequest, dict]):
                The request object. The request to generate a report.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.analytics.data_v1alpha.types.RunReportResponse:
                The response report table
                corresponding to a request.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, analytics_data_api.RunReportRequest):
            request = analytics_data_api.RunReportRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.run_report]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("property", request.property),)),
        )

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

    def get_metadata(
        self,
        request: Optional[Union[analytics_data_api.GetMetadataRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> analytics_data_api.Metadata:
        r"""Returns metadata for dimensions and metrics available in
        reporting methods. Used to explore the dimensions and metrics.
        In this method, a Google Analytics property identifier is
        specified in the request, and the metadata response includes
        Custom dimensions and metrics as well as Universal metadata.

        For example if a custom metric with parameter name
        ``levels_unlocked`` is registered to a property, the Metadata
        response will contain ``customEvent:levels_unlocked``. Universal
        metadata are dimensions and metrics applicable to any property
        such as ``country`` and ``totalUsers``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.analytics import data_v1alpha

            def sample_get_metadata():
                # Create a client
                client = data_v1alpha.AlphaAnalyticsDataClient()

                # Initialize request argument(s)
                request = data_v1alpha.GetMetadataRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_metadata(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.analytics.data_v1alpha.types.GetMetadataRequest, dict]):
                The request object. Request for a property's dimension
                and metric metadata.
            name (str):
                Required. The resource name of the metadata to retrieve.
                This name field is specified in the URL path and not URL
                parameters. Property is a numeric Google Analytics
                property identifier. To learn more, see `where to find
                your Property
                ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.

                Example: properties/1234/metadata

                Set the Property ID to 0 for dimensions and metrics
                common to all properties. In this special mode, this
                method will not return custom dimensions and metrics.

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
            google.analytics.data_v1alpha.types.Metadata:
                The dimensions, metrics and
                comparisons currently accepted in
                reporting methods.

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
        if not isinstance(request, analytics_data_api.GetMetadataRequest):
            request = analytics_data_api.GetMetadataRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_metadata]

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

    def __enter__(self) -> "AlphaAnalyticsDataClient":
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

__all__ = ("AlphaAnalyticsDataClient",)
