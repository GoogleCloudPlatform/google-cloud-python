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
    Iterable,
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

from google.cloud.biglake_hive_v1beta import gapic_version as package_version
from google.cloud.biglake_hive_v1beta._compat import (
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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.biglake_hive_v1beta.services.hive_metastore_service import pagers
from google.cloud.biglake_hive_v1beta.types import hive_metastore

from .transports.base import DEFAULT_CLIENT_INFO, HiveMetastoreServiceTransport
from .transports.grpc import HiveMetastoreServiceGrpcTransport
from .transports.grpc_asyncio import HiveMetastoreServiceGrpcAsyncIOTransport
from .transports.rest import HiveMetastoreServiceRestTransport


class HiveMetastoreServiceClientMeta(type):
    """Metaclass for the HiveMetastoreService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[HiveMetastoreServiceTransport]]
    _transport_registry["grpc"] = HiveMetastoreServiceGrpcTransport
    _transport_registry["grpc_asyncio"] = HiveMetastoreServiceGrpcAsyncIOTransport
    _transport_registry["rest"] = HiveMetastoreServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[HiveMetastoreServiceTransport]:
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


class HiveMetastoreServiceClient(metaclass=HiveMetastoreServiceClientMeta):
    """Hive Metastore Service is a biglake service that allows users to
    manage their external Hive catalogs. Full API compatibility with OSS
    Hive Metastore APIs is not supported. The methods match the Hive
    Metastore API spec mostly except for a few exceptions. These include
    listing resources with pattern, environment context which are
    combined in a single List API, return of ListResponse object instead
    of a list of resources, transactions, locks, etc.

    The BigLake Hive Metastore API defines the following resources:

    - A collection of Google Cloud projects: ``/projects/*``
    - Each project has a collection of catalogs: ``/catalogs/*``
    - Each catalog has a collection of databases: ``/databases/*``
    - Each database has a collection of tables: ``/tables/*``
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "biglake.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "biglake.{UNIVERSE_DOMAIN}"
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
            HiveMetastoreServiceClient: The constructed client.
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
            HiveMetastoreServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> HiveMetastoreServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            HiveMetastoreServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def catalog_path(
        project: str,
        catalog: str,
    ) -> str:
        """Returns a fully-qualified catalog string."""
        return "projects/{project}/catalogs/{catalog}".format(
            project=project,
            catalog=catalog,
        )

    @staticmethod
    def parse_catalog_path(path: str) -> Dict[str, str]:
        """Parses a catalog path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/catalogs/(?P<catalog>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def namespace_path(
        project: str,
        catalog: str,
        database: str,
    ) -> str:
        """Returns a fully-qualified namespace string."""
        return "projects/{project}/catalogs/{catalog}/databases/{database}".format(
            project=project,
            catalog=catalog,
            database=database,
        )

    @staticmethod
    def parse_namespace_path(path: str) -> Dict[str, str]:
        """Parses a namespace path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/catalogs/(?P<catalog>.+?)/databases/(?P<database>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def table_path(
        project: str,
        catalog: str,
        database: str,
        table: str,
    ) -> str:
        """Returns a fully-qualified table string."""
        return "projects/{project}/catalogs/{catalog}/databases/{database}/tables/{table}".format(
            project=project,
            catalog=catalog,
            database=database,
            table=table,
        )

    @staticmethod
    def parse_table_path(path: str) -> Dict[str, str]:
        """Parses a table path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/catalogs/(?P<catalog>.+?)/databases/(?P<database>.+?)/tables/(?P<table>.+?)$",
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
                HiveMetastoreServiceTransport,
                Callable[..., HiveMetastoreServiceTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the hive metastore service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,HiveMetastoreServiceTransport,Callable[..., HiveMetastoreServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the HiveMetastoreServiceTransport constructor.
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
        self._client_cert_source = HiveMetastoreServiceClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=HiveMetastoreServiceClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, HiveMetastoreServiceTransport)
        if transport_provided:
            # transport is a HiveMetastoreServiceTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(HiveMetastoreServiceTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=HiveMetastoreServiceClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=HiveMetastoreServiceClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=HiveMetastoreServiceClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[HiveMetastoreServiceTransport],
                Callable[..., HiveMetastoreServiceTransport],
            ] = (
                HiveMetastoreServiceClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., HiveMetastoreServiceTransport], transport)
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
                    "Created client `google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient`.",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
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
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "credentialsType": None,
                    },
                )

    def create_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.CreateHiveCatalogRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        hive_catalog: Optional[hive_metastore.HiveCatalog] = None,
        hive_catalog_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveCatalog:
        r"""Creates a new hive catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_create_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                hive_catalog = biglake_hive_v1beta.HiveCatalog()
                hive_catalog.location_uri = "location_uri_value"

                request = biglake_hive_v1beta.CreateHiveCatalogRequest(
                    parent="parent_value",
                    hive_catalog=hive_catalog,
                    hive_catalog_id="hive_catalog_id_value",
                    primary_location="primary_location_value",
                )

                # Make the request
                response = client.create_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.CreateHiveCatalogRequest, dict]):
                The request object. Request message for the
                CreateHiveCatalog method.
            parent (str):
                Required. The parent resource where this catalog will be
                created. Format: projects/{project_id_or_number}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_catalog (google.cloud.biglake_hive_v1beta.types.HiveCatalog):
                Required. The catalog to create. The ``name`` field does
                not need to be provided. Gets copied over from
                catalog_id.

                This corresponds to the ``hive_catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_catalog_id (str):
                Required. The Hive Catalog ID to use
                for the catalog that will become the
                final component of the catalog's
                resource name. The maximum length is 256
                characters.

                This corresponds to the ``hive_catalog_id`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveCatalog:
                The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hive_catalog, hive_catalog_id]
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
        if not isinstance(request, hive_metastore.CreateHiveCatalogRequest):
            request = hive_metastore.CreateHiveCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if hive_catalog is not None:
                request.hive_catalog = hive_catalog
            if hive_catalog_id is not None:
                request.hive_catalog_id = hive_catalog_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_hive_catalog]

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

    def get_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.GetHiveCatalogRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveCatalog:
        r"""Gets the catalog specified by the resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_get_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.GetHiveCatalogRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.GetHiveCatalogRequest, dict]):
                The request object. Request message for the
                GetHiveCatalog method.
            name (str):
                Required. The name of the catalog to retrieve. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

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
            google.cloud.biglake_hive_v1beta.types.HiveCatalog:
                The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

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
        if not isinstance(request, hive_metastore.GetHiveCatalogRequest):
            request = hive_metastore.GetHiveCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_hive_catalog]

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

    def list_hive_catalogs(
        self,
        request: Optional[Union[hive_metastore.ListHiveCatalogsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHiveCatalogsPager:
        r"""List all catalogs in a specified project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_list_hive_catalogs():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListHiveCatalogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hive_catalogs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.ListHiveCatalogsRequest, dict]):
                The request object. Request message for the
                ListHiveCatalogs method.
            parent (str):
                Required. The project to list catalogs from. Format:
                projects/{project_id_or_number}

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
            google.cloud.biglake_hive_v1beta.services.hive_metastore_service.pagers.ListHiveCatalogsPager:
                Response message for the
                ListHiveCatalogs method.
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
        if not isinstance(request, hive_metastore.ListHiveCatalogsRequest):
            request = hive_metastore.ListHiveCatalogsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_hive_catalogs]

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
        response = pagers.ListHiveCatalogsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.UpdateHiveCatalogRequest, dict]] = None,
        *,
        hive_catalog: Optional[hive_metastore.HiveCatalog] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveCatalog:
        r"""Updates an existing catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_update_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                hive_catalog = biglake_hive_v1beta.HiveCatalog()
                hive_catalog.location_uri = "location_uri_value"

                request = biglake_hive_v1beta.UpdateHiveCatalogRequest(
                    hive_catalog=hive_catalog,
                )

                # Make the request
                response = client.update_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.UpdateHiveCatalogRequest, dict]):
                The request object. Request message for the
                UpdateHiveCatalog method.
            hive_catalog (google.cloud.biglake_hive_v1beta.types.HiveCatalog):
                Required. The hive catalog to update. The name under the
                catalog is used to identify the catalog. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

                This corresponds to the ``hive_catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The list of fields to update.

                For the ``FieldMask`` definition, see
                https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
                If not set, defaults to all of the fields that are
                allowed to update.

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
            google.cloud.biglake_hive_v1beta.types.HiveCatalog:
                The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hive_catalog, update_mask]
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
        if not isinstance(request, hive_metastore.UpdateHiveCatalogRequest):
            request = hive_metastore.UpdateHiveCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if hive_catalog is not None:
                request.hive_catalog = hive_catalog
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_hive_catalog]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("hive_catalog.name", request.hive_catalog.name),)
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

    def delete_hive_catalog(
        self,
        request: Optional[Union[hive_metastore.DeleteHiveCatalogRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing catalog specified by the catalog
        ID. Delete will fail if the catalog is not empty.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_delete_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.DeleteHiveCatalogRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_hive_catalog(request=request)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.DeleteHiveCatalogRequest, dict]):
                The request object. Request message for the
                DeleteHiveCatalog method.
            name (str):
                Required. The name of the catalog to delete. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

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
        if not isinstance(request, hive_metastore.DeleteHiveCatalogRequest):
            request = hive_metastore.DeleteHiveCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_hive_catalog]

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

    def create_hive_database(
        self,
        request: Optional[Union[hive_metastore.CreateHiveDatabaseRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        hive_database: Optional[hive_metastore.HiveDatabase] = None,
        hive_database_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveDatabase:
        r"""Creates a new database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_create_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.CreateHiveDatabaseRequest(
                    parent="parent_value",
                    hive_database_id="hive_database_id_value",
                )

                # Make the request
                response = client.create_hive_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.CreateHiveDatabaseRequest, dict]):
                The request object. Request message for the
                CreateHiveDatabase method.
            parent (str):
                Required. The parent resource where this database will
                be created. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_database (google.cloud.biglake_hive_v1beta.types.HiveDatabase):
                Required. The database to create. The ``name`` field
                does not need to be provided.

                This corresponds to the ``hive_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_database_id (str):
                Required. The ID to use for the Hive
                Database. The maximum length is 128
                characters.

                This corresponds to the ``hive_database_id`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveDatabase:
                Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hive_database, hive_database_id]
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
        if not isinstance(request, hive_metastore.CreateHiveDatabaseRequest):
            request = hive_metastore.CreateHiveDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if hive_database is not None:
                request.hive_database = hive_database
            if hive_database_id is not None:
                request.hive_database_id = hive_database_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_hive_database]

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

    def get_hive_database(
        self,
        request: Optional[Union[hive_metastore.GetHiveDatabaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveDatabase:
        r"""Gets the database specified by the resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_get_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.GetHiveDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_hive_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.GetHiveDatabaseRequest, dict]):
                The request object. Request message for the
                GetHiveDatabase method.
            name (str):
                Required. The name of the database to retrieve. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

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
            google.cloud.biglake_hive_v1beta.types.HiveDatabase:
                Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

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
        if not isinstance(request, hive_metastore.GetHiveDatabaseRequest):
            request = hive_metastore.GetHiveDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_hive_database]

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

    def list_hive_databases(
        self,
        request: Optional[Union[hive_metastore.ListHiveDatabasesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHiveDatabasesPager:
        r"""List all databases in a specified catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_list_hive_databases():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListHiveDatabasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hive_databases(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.ListHiveDatabasesRequest, dict]):
                The request object. Request message for the
                ListHiveDatabases method.
            parent (str):
                Required. The hive catalog to list databases from.
                Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}

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
            google.cloud.biglake_hive_v1beta.services.hive_metastore_service.pagers.ListHiveDatabasesPager:
                Response message for the
                ListHiveDatabases method.
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
        if not isinstance(request, hive_metastore.ListHiveDatabasesRequest):
            request = hive_metastore.ListHiveDatabasesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_hive_databases]

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
        response = pagers.ListHiveDatabasesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_hive_database(
        self,
        request: Optional[Union[hive_metastore.UpdateHiveDatabaseRequest, dict]] = None,
        *,
        hive_database: Optional[hive_metastore.HiveDatabase] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveDatabase:
        r"""Updates an existing database specified by the
        database name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_update_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.UpdateHiveDatabaseRequest(
                )

                # Make the request
                response = client.update_hive_database(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.UpdateHiveDatabaseRequest, dict]):
                The request object. Request message for the
                UpdateHiveDatabase method.
            hive_database (google.cloud.biglake_hive_v1beta.types.HiveDatabase):
                Required. The database to update.

                The database's ``name`` field is used to identify the
                database to update. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

                This corresponds to the ``hive_database`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The list of fields to
                update.

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
            google.cloud.biglake_hive_v1beta.types.HiveDatabase:
                Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hive_database, update_mask]
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
        if not isinstance(request, hive_metastore.UpdateHiveDatabaseRequest):
            request = hive_metastore.UpdateHiveDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if hive_database is not None:
                request.hive_database = hive_database
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_hive_database]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("hive_database.name", request.hive_database.name),)
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

    def delete_hive_database(
        self,
        request: Optional[Union[hive_metastore.DeleteHiveDatabaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing database specified by the
        database name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_delete_hive_database():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.DeleteHiveDatabaseRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_hive_database(request=request)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.DeleteHiveDatabaseRequest, dict]):
                The request object. Request message for the
                DeleteHiveDatabase method.
            name (str):
                Required. The name of the database to delete. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

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
        if not isinstance(request, hive_metastore.DeleteHiveDatabaseRequest):
            request = hive_metastore.DeleteHiveDatabaseRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_hive_database]

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

    def create_hive_table(
        self,
        request: Optional[Union[hive_metastore.CreateHiveTableRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        hive_table: Optional[hive_metastore.HiveTable] = None,
        hive_table_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveTable:
        r"""Creates a new hive table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_create_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                hive_table = biglake_hive_v1beta.HiveTable()
                hive_table.storage_descriptor.columns.name = "name_value"
                hive_table.storage_descriptor.columns.type_ = "type__value"

                request = biglake_hive_v1beta.CreateHiveTableRequest(
                    parent="parent_value",
                    hive_table=hive_table,
                    hive_table_id="hive_table_id_value",
                )

                # Make the request
                response = client.create_hive_table(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.CreateHiveTableRequest, dict]):
                The request object. Request message for the
                CreateHiveTable method.
            parent (str):
                Required. The parent resource for the table to be
                created. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_table (google.cloud.biglake_hive_v1beta.types.HiveTable):
                Required. The Hive Table to create. The ``name`` field
                does not need to be provided.

                This corresponds to the ``hive_table`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            hive_table_id (str):
                Required. The Hive Table ID to use
                for the table that will become the final
                component of the table's resource name.
                The maximum length is 256 characters.

                This corresponds to the ``hive_table_id`` field
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
            google.cloud.biglake_hive_v1beta.types.HiveTable:
                Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, hive_table, hive_table_id]
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
        if not isinstance(request, hive_metastore.CreateHiveTableRequest):
            request = hive_metastore.CreateHiveTableRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if hive_table is not None:
                request.hive_table = hive_table
            if hive_table_id is not None:
                request.hive_table_id = hive_table_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_hive_table]

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

    def get_hive_table(
        self,
        request: Optional[Union[hive_metastore.GetHiveTableRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveTable:
        r"""Gets the table specified by the resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_get_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.GetHiveTableRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_hive_table(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.GetHiveTableRequest, dict]):
                The request object. Request message for the GetHiveTable
                method.
            name (str):
                Required. The name of the table to retrieve. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

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
            google.cloud.biglake_hive_v1beta.types.HiveTable:
                Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

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
        if not isinstance(request, hive_metastore.GetHiveTableRequest):
            request = hive_metastore.GetHiveTableRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_hive_table]

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

    def list_hive_tables(
        self,
        request: Optional[Union[hive_metastore.ListHiveTablesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListHiveTablesPager:
        r"""List all hive tables in a specified project under the
        hive catalog and database.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_list_hive_tables():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListHiveTablesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_hive_tables(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.ListHiveTablesRequest, dict]):
                The request object. Request message for the
                ListHiveTables method.
            parent (str):
                Required. The database to list tables from. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}

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
            google.cloud.biglake_hive_v1beta.services.hive_metastore_service.pagers.ListHiveTablesPager:
                Response message for the
                ListHiveTables method.
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
        if not isinstance(request, hive_metastore.ListHiveTablesRequest):
            request = hive_metastore.ListHiveTablesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_hive_tables]

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
        response = pagers.ListHiveTablesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_hive_table(
        self,
        request: Optional[Union[hive_metastore.UpdateHiveTableRequest, dict]] = None,
        *,
        hive_table: Optional[hive_metastore.HiveTable] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.HiveTable:
        r"""Updates an existing table specified by the table
        name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_update_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                hive_table = biglake_hive_v1beta.HiveTable()
                hive_table.storage_descriptor.columns.name = "name_value"
                hive_table.storage_descriptor.columns.type_ = "type__value"

                request = biglake_hive_v1beta.UpdateHiveTableRequest(
                    hive_table=hive_table,
                )

                # Make the request
                response = client.update_hive_table(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.UpdateHiveTableRequest, dict]):
                The request object. Request message for the
                UpdateHiveTable method.
            hive_table (google.cloud.biglake_hive_v1beta.types.HiveTable):
                Required. The table to update.

                The table's ``name`` field is used to identify the table
                to update. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

                This corresponds to the ``hive_table`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The list of fields to
                update.

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
            google.cloud.biglake_hive_v1beta.types.HiveTable:
                Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [hive_table, update_mask]
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
        if not isinstance(request, hive_metastore.UpdateHiveTableRequest):
            request = hive_metastore.UpdateHiveTableRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if hive_table is not None:
                request.hive_table = hive_table
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_hive_table]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("hive_table.name", request.hive_table.name),)
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

    def delete_hive_table(
        self,
        request: Optional[Union[hive_metastore.DeleteHiveTableRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing table specified by the table
        name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_delete_hive_table():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.DeleteHiveTableRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_hive_table(request=request)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.DeleteHiveTableRequest, dict]):
                The request object. Request message for the
                DeleteHiveTable method.
            name (str):
                Required. The name of the database to delete. Format:
                projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}

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
        if not isinstance(request, hive_metastore.DeleteHiveTableRequest):
            request = hive_metastore.DeleteHiveTableRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_hive_table]

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

    def batch_create_partitions(
        self,
        request: Optional[
            Union[hive_metastore.BatchCreatePartitionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.BatchCreatePartitionsResponse:
        r"""Adds partitions to a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_batch_create_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                requests = biglake_hive_v1beta.CreatePartitionRequest()
                requests.parent = "parent_value"
                requests.partition.values = ['values_value1', 'values_value2']

                request = biglake_hive_v1beta.BatchCreatePartitionsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_create_partitions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.BatchCreatePartitionsRequest, dict]):
                The request object. Request message for the
                BatchCreatePartitions method.
            parent (str):
                Required. Reference to the table to
                where the partitions to be added, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
            google.cloud.biglake_hive_v1beta.types.BatchCreatePartitionsResponse:
                Response message for
                BatchCreatePartitions.

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
        if not isinstance(request, hive_metastore.BatchCreatePartitionsRequest):
            request = hive_metastore.BatchCreatePartitionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_create_partitions]

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

    def batch_delete_partitions(
        self,
        request: Optional[
            Union[hive_metastore.BatchDeletePartitionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes partitions from a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_batch_delete_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                partition_values = biglake_hive_v1beta.PartitionValues()
                partition_values.values = ['values_value1', 'values_value2']

                request = biglake_hive_v1beta.BatchDeletePartitionsRequest(
                    parent="parent_value",
                    partition_values=partition_values,
                )

                # Make the request
                client.batch_delete_partitions(request=request)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.BatchDeletePartitionsRequest, dict]):
                The request object. Request message for
                BatchDeletePartitions. The Partition is
                uniquely identified by values, which is
                an ordered list. Hence, there is no
                separate name or partition id field.
            parent (str):
                Required. Reference to the table to
                which these partitions belong, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
        if not isinstance(request, hive_metastore.BatchDeletePartitionsRequest):
            request = hive_metastore.BatchDeletePartitionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_delete_partitions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
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

    def batch_update_partitions(
        self,
        request: Optional[
            Union[hive_metastore.BatchUpdatePartitionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.BatchUpdatePartitionsResponse:
        r"""Updates partitions in a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_batch_update_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                requests = biglake_hive_v1beta.UpdatePartitionRequest()
                requests.partition.values = ['values_value1', 'values_value2']

                request = biglake_hive_v1beta.BatchUpdatePartitionsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_update_partitions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.BatchUpdatePartitionsRequest, dict]):
                The request object. Request message for
                BatchUpdatePartitions.
            parent (str):
                Required. Reference to the table to
                which these partitions belong, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
            google.cloud.biglake_hive_v1beta.types.BatchUpdatePartitionsResponse:
                Response message for
                BatchUpdatePartitions.

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
        if not isinstance(request, hive_metastore.BatchUpdatePartitionsRequest):
            request = hive_metastore.BatchUpdatePartitionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_update_partitions]

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

    def list_partitions(
        self,
        request: Optional[Union[hive_metastore.ListPartitionsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Iterable[hive_metastore.ListPartitionsResponse]:
        r"""Streams list of partitions from a table.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_list_partitions():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.ListPartitionsRequest(
                    parent="parent_value",
                )

                # Make the request
                stream = client.list_partitions(request=request)

                # Handle the response
                for response in stream:
                    print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.ListPartitionsRequest, dict]):
                The request object. Request message for ListPartitions.
            parent (str):
                Required. Reference to the table to
                which these partitions belong, in the
                format of
                projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.

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
            Iterable[google.cloud.biglake_hive_v1beta.types.ListPartitionsResponse]:
                Response message for ListPartitions.
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
        if not isinstance(request, hive_metastore.ListPartitionsRequest):
            request = hive_metastore.ListPartitionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_partitions]

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

    def failover_hive_catalog(
        self,
        request: Optional[
            Union[hive_metastore.FailoverHiveCatalogRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        primary_replica: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> hive_metastore.FailoverHiveCatalogResponse:
        r"""Failover the catalog to a new primary replica region.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import biglake_hive_v1beta

            def sample_failover_hive_catalog():
                # Create a client
                client = biglake_hive_v1beta.HiveMetastoreServiceClient()

                # Initialize request argument(s)
                request = biglake_hive_v1beta.FailoverHiveCatalogRequest(
                    name="name_value",
                    primary_replica="primary_replica_value",
                )

                # Make the request
                response = client.failover_hive_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.biglake_hive_v1beta.types.FailoverHiveCatalogRequest, dict]):
                The request object. Request message for
                FailoverHiveCatalog.
            name (str):
                Required. The name of the catalog in the form
                "projects/{project_id}/catalogs/{catalog_id}"

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            primary_replica (str):
                Required. The region being assigned
                as the new primary replica region. For
                example "us-east1". This must be one of
                the replica regions in the catalog's
                list of replicas marked as a
                "secondary".

                This corresponds to the ``primary_replica`` field
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
            google.cloud.biglake_hive_v1beta.types.FailoverHiveCatalogResponse:
                Response message for
                FailoverHiveCatalog.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, primary_replica]
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
        if not isinstance(request, hive_metastore.FailoverHiveCatalogRequest):
            request = hive_metastore.FailoverHiveCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if primary_replica is not None:
                request.primary_replica = primary_replica

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.failover_hive_catalog]

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

    def __enter__(self) -> "HiveMetastoreServiceClient":
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

__all__ = ("HiveMetastoreServiceClient",)
