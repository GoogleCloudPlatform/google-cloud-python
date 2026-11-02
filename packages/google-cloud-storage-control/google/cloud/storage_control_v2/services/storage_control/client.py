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
import uuid
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

from google.cloud.storage_control_v2 import gapic_version as package_version
from google.cloud.storage_control_v2._compat import (
    get_api_endpoint,
    get_default_mtls_endpoint,
    get_universe_domain,
    read_environment_variables,
    setup_request_id,
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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.storage_control_v2.services.storage_control import pagers
from google.cloud.storage_control_v2.types import storage_control

from .transports.base import DEFAULT_CLIENT_INFO, StorageControlTransport
from .transports.grpc import StorageControlGrpcTransport
from .transports.grpc_asyncio import StorageControlGrpcAsyncIOTransport
from .transports.rest import StorageControlRestTransport


class StorageControlClientMeta(type):
    """Metaclass for the StorageControl client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[StorageControlTransport]]
    _transport_registry["grpc"] = StorageControlGrpcTransport
    _transport_registry["grpc_asyncio"] = StorageControlGrpcAsyncIOTransport
    _transport_registry["rest"] = StorageControlRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[StorageControlTransport]:
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


class StorageControlClient(metaclass=StorageControlClientMeta):
    """StorageControl service includes selected control plane
    operations.
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "storage.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "storage.{UNIVERSE_DOMAIN}"
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
            StorageControlClient: The constructed client.
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
            StorageControlClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> StorageControlTransport:
        """Returns the transport used by the client instance.

        Returns:
            StorageControlTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def anywhere_cache_path(
        project: str,
        bucket: str,
        anywhere_cache: str,
    ) -> str:
        """Returns a fully-qualified anywhere_cache string."""
        return "projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}".format(
            project=project,
            bucket=bucket,
            anywhere_cache=anywhere_cache,
        )

    @staticmethod
    def parse_anywhere_cache_path(path: str) -> Dict[str, str]:
        """Parses a anywhere_cache path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)/anywhereCaches/(?P<anywhere_cache>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def bucket_path(
        project: str,
        bucket: str,
    ) -> str:
        """Returns a fully-qualified bucket string."""
        return "projects/{project}/buckets/{bucket}".format(
            project=project,
            bucket=bucket,
        )

    @staticmethod
    def parse_bucket_path(path: str) -> Dict[str, str]:
        """Parses a bucket path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def folder_path(
        project: str,
        bucket: str,
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "projects/{project}/buckets/{bucket}/folders/{folder}".format(
            project=project,
            bucket=bucket,
            folder=folder,
        )

    @staticmethod
    def parse_folder_path(path: str) -> Dict[str, str]:
        """Parses a folder path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)/folders/(?P<folder>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def intelligence_config_path(
        folder: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified intelligence_config string."""
        return "folders/{folder}/locations/{location}/intelligenceConfig".format(
            folder=folder,
            location=location,
        )

    @staticmethod
    def parse_intelligence_config_path(path: str) -> Dict[str, str]:
        """Parses a intelligence_config path into its component segments."""
        m = re.match(
            r"^folders/(?P<folder>.+?)/locations/(?P<location>.+?)/intelligenceConfig$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def intelligence_finding_path(
        project: str,
        location: str,
        intelligence_finding: str,
    ) -> str:
        """Returns a fully-qualified intelligence_finding string."""
        return "projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}".format(
            project=project,
            location=location,
            intelligence_finding=intelligence_finding,
        )

    @staticmethod
    def parse_intelligence_finding_path(path: str) -> Dict[str, str]:
        """Parses a intelligence_finding path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/intelligenceFindings/(?P<intelligence_finding>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def intelligence_finding_revision_path(
        project: str,
        location: str,
        intelligence_finding: str,
        revision: str,
    ) -> str:
        """Returns a fully-qualified intelligence_finding_revision string."""
        return "projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}".format(
            project=project,
            location=location,
            intelligence_finding=intelligence_finding,
            revision=revision,
        )

    @staticmethod
    def parse_intelligence_finding_revision_path(path: str) -> Dict[str, str]:
        """Parses a intelligence_finding_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/intelligenceFindings/(?P<intelligence_finding>.+?)/revisions/(?P<revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def managed_folder_path(
        project: str,
        bucket: str,
        managed_folder: str,
    ) -> str:
        """Returns a fully-qualified managed_folder string."""
        return "projects/{project}/buckets/{bucket}/managedFolders/{managed_folder}".format(
            project=project,
            bucket=bucket,
            managed_folder=managed_folder,
        )

    @staticmethod
    def parse_managed_folder_path(path: str) -> Dict[str, str]:
        """Parses a managed_folder path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)/managedFolders/(?P<managed_folder>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def object_path(
        project: str,
        bucket: str,
        object: str,
    ) -> str:
        """Returns a fully-qualified object string."""
        return "projects/{project}/buckets/{bucket}/objects/{object}".format(
            project=project,
            bucket=bucket,
            object=object,
        )

    @staticmethod
    def parse_object_path(path: str) -> Dict[str, str]:
        """Parses a object path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)/objects/(?P<object>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def rapid_cache_path(
        project: str,
        bucket: str,
        rapid_cache: str,
    ) -> str:
        """Returns a fully-qualified rapid_cache string."""
        return "projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}".format(
            project=project,
            bucket=bucket,
            rapid_cache=rapid_cache,
        )

    @staticmethod
    def parse_rapid_cache_path(path: str) -> Dict[str, str]:
        """Parses a rapid_cache path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)/rapidCaches/(?P<rapid_cache>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def storage_layout_path(
        project: str,
        bucket: str,
    ) -> str:
        """Returns a fully-qualified storage_layout string."""
        return "projects/{project}/buckets/{bucket}/storageLayout".format(
            project=project,
            bucket=bucket,
        )

    @staticmethod
    def parse_storage_layout_path(path: str) -> Dict[str, str]:
        """Parses a storage_layout path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/buckets/(?P<bucket>.+?)/storageLayout$", path
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
            Union[str, StorageControlTransport, Callable[..., StorageControlTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the storage control client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,StorageControlTransport,Callable[..., StorageControlTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the StorageControlTransport constructor.
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
        self._client_cert_source = StorageControlClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=StorageControlClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, StorageControlTransport)
        if transport_provided:
            # transport is a StorageControlTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(StorageControlTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=StorageControlClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=StorageControlClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=StorageControlClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[StorageControlTransport], Callable[..., StorageControlTransport]
            ] = (
                StorageControlClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., StorageControlTransport], transport)
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
                    "Created client `google.storage.control_v2.StorageControlClient`.",
                    extra={
                        "serviceName": "google.storage.control.v2.StorageControl",
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
                        "serviceName": "google.storage.control.v2.StorageControl",
                        "credentialsType": None,
                    },
                )

    def create_folder(
        self,
        request: Optional[Union[storage_control.CreateFolderRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        folder: Optional[storage_control.Folder] = None,
        folder_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.Folder:
        r"""Creates a new folder. This operation is only
        applicable to a hierarchical namespace enabled bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_create_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.CreateFolderRequest(
                    parent="parent_value",
                    folder_id="folder_id_value",
                )

                # Make the request
                response = client.create_folder(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.CreateFolderRequest, dict]):
                The request object. Request message for CreateFolder.
                This operation is only applicable to a
                hierarchical namespace enabled bucket.
            parent (str):
                Required. Name of the bucket in which
                the folder will reside. The bucket must
                be a hierarchical namespace enabled
                bucket.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            folder (google.cloud.storage_control_v2.types.Folder):
                Required. Properties of the new folder being created.
                The bucket and name of the folder are specified in the
                parent and folder_id fields, respectively. Populating
                those fields in ``folder`` will result in an error.

                This corresponds to the ``folder`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            folder_id (str):
                Required. The full name of a folder, including all its
                parent folders. Folders use single '/' characters as a
                delimiter. The folder_id must end with a slash. For
                example, the folder_id of "books/biographies/" would
                create a new "biographies/" folder under the "books/"
                folder.

                This corresponds to the ``folder_id`` field
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
            google.cloud.storage_control_v2.types.Folder:
                A folder resource. This resource can
                only exist in a hierarchical namespace
                enabled bucket.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, folder, folder_id]
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
        if not isinstance(request, storage_control.CreateFolderRequest):
            request = storage_control.CreateFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if folder is not None:
                request.folder = folder
            if folder_id is not None:
                request.folder_id = folder_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def delete_folder(
        self,
        request: Optional[Union[storage_control.DeleteFolderRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Permanently deletes an empty folder. This operation
        is only applicable to a hierarchical namespace enabled
        bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_delete_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.DeleteFolderRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_folder(request=request)

        Args:
            request (Union[google.cloud.storage_control_v2.types.DeleteFolderRequest, dict]):
                The request object. Request message for DeleteFolder.
                This operation is only applicable to a
                hierarchical namespace enabled bucket.
            name (str):
                Required. Name of the folder. Format:
                ``projects/{project}/buckets/{bucket}/folders/{folder}``

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
        if not isinstance(request, storage_control.DeleteFolderRequest):
            request = storage_control.DeleteFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def get_folder(
        self,
        request: Optional[Union[storage_control.GetFolderRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.Folder:
        r"""Returns metadata for the specified folder. This
        operation is only applicable to a hierarchical namespace
        enabled bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetFolderRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_folder(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetFolderRequest, dict]):
                The request object. Request message for GetFolder. This
                operation is only applicable to a
                hierarchical namespace enabled bucket.
            name (str):
                Required. Name of the folder. Format:
                ``projects/{project}/buckets/{bucket}/folders/{folder}``

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
            google.cloud.storage_control_v2.types.Folder:
                A folder resource. This resource can
                only exist in a hierarchical namespace
                enabled bucket.

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
        if not isinstance(request, storage_control.GetFolderRequest):
            request = storage_control.GetFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def list_folders(
        self,
        request: Optional[Union[storage_control.ListFoldersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListFoldersPager:
        r"""Retrieves a list of folders. This operation is only
        applicable to a hierarchical namespace enabled bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_list_folders():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ListFoldersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_folders(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ListFoldersRequest, dict]):
                The request object. Request message for ListFolders. This
                operation is only applicable to a
                hierarchical namespace enabled bucket.
            parent (str):
                Required. Name of the bucket in which
                to look for folders. The bucket must be
                a hierarchical namespace enabled bucket.

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
            google.cloud.storage_control_v2.services.storage_control.pagers.ListFoldersPager:
                Response message for ListFolders.

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
        if not isinstance(request, storage_control.ListFoldersRequest):
            request = storage_control.ListFoldersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_folders]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
        response = pagers.ListFoldersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def rename_folder(
        self,
        request: Optional[Union[storage_control.RenameFolderRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        destination_folder_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Renames a source folder to a destination folder. This
        operation is only applicable to a hierarchical namespace
        enabled bucket. During a rename, the source and
        destination folders are locked until the long running
        operation completes.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_rename_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.RenameFolderRequest(
                    name="name_value",
                    destination_folder_id="destination_folder_id_value",
                )

                # Make the request
                operation = client.rename_folder(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.RenameFolderRequest, dict]):
                The request object. Request message for RenameFolder.
                This operation is only applicable to a
                hierarchical namespace enabled bucket.
            name (str):
                Required. Name of the source folder being renamed.
                Format:
                ``projects/{project}/buckets/{bucket}/folders/{folder}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            destination_folder_id (str):
                Required. The destination folder ID, e.g. ``foo/bar/``.
                This corresponds to the ``destination_folder_id`` field
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

                The result type for the operation will be :class:`google.cloud.storage_control_v2.types.Folder` A folder resource. This resource can only exist in a hierarchical namespace
                   enabled bucket.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, destination_folder_id]
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
        if not isinstance(request, storage_control.RenameFolderRequest):
            request = storage_control.RenameFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if destination_folder_id is not None:
                request.destination_folder_id = destination_folder_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.rename_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            storage_control.Folder,
            metadata_type=storage_control.RenameFolderMetadata,
        )

        # Done; return the response.
        return response

    def delete_folder_recursive(
        self,
        request: Optional[
            Union[storage_control.DeleteFolderRecursiveRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a folder recursively. This operation is only
        applicable to a hierarchical namespace enabled bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_delete_folder_recursive():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.DeleteFolderRecursiveRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_folder_recursive(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.DeleteFolderRecursiveRequest, dict]):
                The request object. Request message for
                DeleteFolderRecursive.
            name (str):
                Required. Name of the folder being deleted, however all
                of its contents will be deleted too. Format:
                ``projects/{project}/buckets/{bucket}/folders/{folder}``

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
        if not isinstance(request, storage_control.DeleteFolderRecursiveRequest):
            request = storage_control.DeleteFolderRecursiveRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_folder_recursive]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            metadata_type=storage_control.DeleteFolderRecursiveMetadata,
        )

        # Done; return the response.
        return response

    def get_storage_layout(
        self,
        request: Optional[Union[storage_control.GetStorageLayoutRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.StorageLayout:
        r"""Returns the storage layout configuration for a given
        bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_storage_layout():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetStorageLayoutRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_storage_layout(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetStorageLayoutRequest, dict]):
                The request object. Request message for GetStorageLayout.
            name (str):
                Required. The name of the StorageLayout resource.
                Format:
                ``projects/{project}/buckets/{bucket}/storageLayout``

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
            google.cloud.storage_control_v2.types.StorageLayout:
                The storage layout configuration of a
                bucket.

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
        if not isinstance(request, storage_control.GetStorageLayoutRequest):
            request = storage_control.GetStorageLayoutRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_storage_layout]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def create_managed_folder(
        self,
        request: Optional[
            Union[storage_control.CreateManagedFolderRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        managed_folder: Optional[storage_control.ManagedFolder] = None,
        managed_folder_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.ManagedFolder:
        r"""Creates a new managed folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_create_managed_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.CreateManagedFolderRequest(
                    parent="parent_value",
                    managed_folder_id="managed_folder_id_value",
                )

                # Make the request
                response = client.create_managed_folder(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.CreateManagedFolderRequest, dict]):
                The request object. Request message for
                CreateManagedFolder.
            parent (str):
                Required. Name of the bucket this
                managed folder belongs to.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            managed_folder (google.cloud.storage_control_v2.types.ManagedFolder):
                Required. Properties of the managed folder being
                created. The bucket and managed folder names are
                specified in the ``parent`` and ``managed_folder_id``
                fields. Populating these fields in ``managed_folder``
                will result in an error.

                This corresponds to the ``managed_folder`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            managed_folder_id (str):
                Required. The name of the managed folder. It uses a
                single ``/`` as delimiter and leading and trailing ``/``
                are allowed.

                This corresponds to the ``managed_folder_id`` field
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
            google.cloud.storage_control_v2.types.ManagedFolder:
                A managed folder.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, managed_folder, managed_folder_id]
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
        if not isinstance(request, storage_control.CreateManagedFolderRequest):
            request = storage_control.CreateManagedFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if managed_folder is not None:
                request.managed_folder = managed_folder
            if managed_folder_id is not None:
                request.managed_folder_id = managed_folder_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_managed_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def delete_managed_folder(
        self,
        request: Optional[
            Union[storage_control.DeleteManagedFolderRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Permanently deletes an empty managed folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_delete_managed_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.DeleteManagedFolderRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_managed_folder(request=request)

        Args:
            request (Union[google.cloud.storage_control_v2.types.DeleteManagedFolderRequest, dict]):
                The request object. DeleteManagedFolder RPC request
                message.
            name (str):
                Required. Name of the managed folder. Format:
                ``projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}``

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
        if not isinstance(request, storage_control.DeleteManagedFolderRequest):
            request = storage_control.DeleteManagedFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_managed_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def get_managed_folder(
        self,
        request: Optional[Union[storage_control.GetManagedFolderRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.ManagedFolder:
        r"""Returns metadata for the specified managed folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_managed_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetManagedFolderRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_managed_folder(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetManagedFolderRequest, dict]):
                The request object. Request message for GetManagedFolder.
            name (str):
                Required. Name of the managed folder. Format:
                ``projects/{project}/buckets/{bucket}/managedFolders/{managedFolder}``

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
            google.cloud.storage_control_v2.types.ManagedFolder:
                A managed folder.
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
        if not isinstance(request, storage_control.GetManagedFolderRequest):
            request = storage_control.GetManagedFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_managed_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def list_managed_folders(
        self,
        request: Optional[
            Union[storage_control.ListManagedFoldersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListManagedFoldersPager:
        r"""Retrieves a list of managed folders for a given
        bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_list_managed_folders():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ListManagedFoldersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_managed_folders(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ListManagedFoldersRequest, dict]):
                The request object. Request message for
                ListManagedFolders.
            parent (str):
                Required. Name of the bucket this
                managed folder belongs to.

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
            google.cloud.storage_control_v2.services.storage_control.pagers.ListManagedFoldersPager:
                Response message for
                ListManagedFolders.
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
        if not isinstance(request, storage_control.ListManagedFoldersRequest):
            request = storage_control.ListManagedFoldersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_managed_folders]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
        response = pagers.ListManagedFoldersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_managed_folder(
        self,
        request: Optional[
            Union[storage_control.UpdateManagedFolderRequest, dict]
        ] = None,
        *,
        managed_folder: Optional[storage_control.ManagedFolder] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.ManagedFolder:
        r"""Updates a managed folder. Currently, this RPC only supports
        updating the ``rapid_cache_config`` field.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_update_managed_folder():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.UpdateManagedFolderRequest(
                )

                # Make the request
                response = client.update_managed_folder(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.UpdateManagedFolderRequest, dict]):
                The request object. Request message for
                UpdateManagedFolder.
            managed_folder (google.cloud.storage_control_v2.types.ManagedFolder):
                Required. Properties of the managed folder being
                updated. Currently, this RPC only supports updating the
                ``rapid_cache_config`` field in ``managed_folder``.

                This corresponds to the ``managed_folder`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Update mask for managed_folder. Currently,
                this RPC only supports updating the
                ``rapid_cache_config`` field in ``managed_folder``. This
                field also supports update mask for the subfields in the
                map of ``rapid_cache_config``. The user can specify the
                update mask for ``rapid_cache_config.policies`` and
                ``rapid_cache_config.policies.<key>``, but patching is
                not supported for a field within
                ``RapidCachePolicy.policies.<key>``, like
                rapid_cache_config.policies.[key].ingest_on_write.

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
            google.cloud.storage_control_v2.types.ManagedFolder:
                A managed folder.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [managed_folder, update_mask]
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
        if not isinstance(request, storage_control.UpdateManagedFolderRequest):
            request = storage_control.UpdateManagedFolderRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if managed_folder is not None:
                request.managed_folder = managed_folder
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_managed_folder]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.managed_folder.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def create_anywhere_cache(
        self,
        request: Optional[
            Union[storage_control.CreateAnywhereCacheRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        anywhere_cache: Optional[storage_control.AnywhereCache] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates an Anywhere Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_create_anywhere_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.CreateAnywhereCacheRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_anywhere_cache(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.CreateAnywhereCacheRequest, dict]):
                The request object. Request message for
                CreateAnywhereCache.
            parent (str):
                Required. The bucket to which this cache belongs.
                Format: ``projects/{project}/buckets/{bucket}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            anywhere_cache (google.cloud.storage_control_v2.types.AnywhereCache):
                Required. Properties of the Anywhere Cache instance
                being created. The parent bucket name is specified in
                the ``parent`` field. Server uses the default value of
                ``ttl`` or ``admission_policy`` if not specified in
                request.

                This corresponds to the ``anywhere_cache`` field
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
                :class:`google.cloud.storage_control_v2.types.AnywhereCache`
                An Anywhere Cache Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, anywhere_cache]
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
        if not isinstance(request, storage_control.CreateAnywhereCacheRequest):
            request = storage_control.CreateAnywhereCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if anywhere_cache is not None:
                request.anywhere_cache = anywhere_cache

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_anywhere_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            storage_control.AnywhereCache,
            metadata_type=storage_control.CreateAnywhereCacheMetadata,
        )

        # Done; return the response.
        return response

    def update_anywhere_cache(
        self,
        request: Optional[
            Union[storage_control.UpdateAnywhereCacheRequest, dict]
        ] = None,
        *,
        anywhere_cache: Optional[storage_control.AnywhereCache] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates an Anywhere Cache instance. Mutable fields include
        ``ttl`` and ``admission_policy``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_update_anywhere_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.UpdateAnywhereCacheRequest(
                )

                # Make the request
                operation = client.update_anywhere_cache(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.UpdateAnywhereCacheRequest, dict]):
                The request object. Request message for
                UpdateAnywhereCache.
            anywhere_cache (google.cloud.storage_control_v2.types.AnywhereCache):
                Required. The Anywhere Cache instance
                to be updated.

                This corresponds to the ``anywhere_cache`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. List of fields to be updated. Mutable fields
                of AnywhereCache include ``ttl`` and
                ``admission_policy``.

                To specify ALL fields, specify a single field with the
                value ``*``. Note: We recommend against doing this. If a
                new field is introduced at a later time, an older client
                updating with the ``*`` may accidentally reset the new
                field's value.

                Not specifying any fields is an error.

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
                :class:`google.cloud.storage_control_v2.types.AnywhereCache`
                An Anywhere Cache Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [anywhere_cache, update_mask]
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
        if not isinstance(request, storage_control.UpdateAnywhereCacheRequest):
            request = storage_control.UpdateAnywhereCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if anywhere_cache is not None:
                request.anywhere_cache = anywhere_cache
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_anywhere_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.anywhere_cache.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            storage_control.AnywhereCache,
            metadata_type=storage_control.UpdateAnywhereCacheMetadata,
        )

        # Done; return the response.
        return response

    def disable_anywhere_cache(
        self,
        request: Optional[
            Union[storage_control.DisableAnywhereCacheRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.AnywhereCache:
        r"""Disables an Anywhere Cache instance. A disabled
        instance is read-only. The disablement could be revoked
        by calling ResumeAnywhereCache. The cache instance will
        be deleted automatically if it remains in the disabled
        state for at least one hour.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_disable_anywhere_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.DisableAnywhereCacheRequest(
                    name="name_value",
                )

                # Make the request
                response = client.disable_anywhere_cache(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.DisableAnywhereCacheRequest, dict]):
                The request object. Request message for
                DisableAnywhereCache.
            name (str):
                Required. The name field in the request should be:
                ``projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}``

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
            google.cloud.storage_control_v2.types.AnywhereCache:
                An Anywhere Cache Instance.
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
        if not isinstance(request, storage_control.DisableAnywhereCacheRequest):
            request = storage_control.DisableAnywhereCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.disable_anywhere_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def pause_anywhere_cache(
        self,
        request: Optional[
            Union[storage_control.PauseAnywhereCacheRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.AnywhereCache:
        r"""Pauses an Anywhere Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_pause_anywhere_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.PauseAnywhereCacheRequest(
                    name="name_value",
                )

                # Make the request
                response = client.pause_anywhere_cache(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.PauseAnywhereCacheRequest, dict]):
                The request object. Request message for
                PauseAnywhereCache.
            name (str):
                Required. The name field in the request should be:
                ``projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}``

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
            google.cloud.storage_control_v2.types.AnywhereCache:
                An Anywhere Cache Instance.
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
        if not isinstance(request, storage_control.PauseAnywhereCacheRequest):
            request = storage_control.PauseAnywhereCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.pause_anywhere_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def resume_anywhere_cache(
        self,
        request: Optional[
            Union[storage_control.ResumeAnywhereCacheRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.AnywhereCache:
        r"""Resumes a disabled or paused Anywhere Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_resume_anywhere_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ResumeAnywhereCacheRequest(
                    name="name_value",
                )

                # Make the request
                response = client.resume_anywhere_cache(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ResumeAnywhereCacheRequest, dict]):
                The request object. Request message for
                ResumeAnywhereCache.
            name (str):
                Required. The name field in the request should be:
                ``projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}``

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
            google.cloud.storage_control_v2.types.AnywhereCache:
                An Anywhere Cache Instance.
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
        if not isinstance(request, storage_control.ResumeAnywhereCacheRequest):
            request = storage_control.ResumeAnywhereCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.resume_anywhere_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def get_anywhere_cache(
        self,
        request: Optional[Union[storage_control.GetAnywhereCacheRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.AnywhereCache:
        r"""Gets an Anywhere Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_anywhere_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetAnywhereCacheRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_anywhere_cache(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetAnywhereCacheRequest, dict]):
                The request object. Request message for GetAnywhereCache.
            name (str):
                Required. The name field in the request should be:
                ``projects/{project}/buckets/{bucket}/anywhereCaches/{anywhere_cache}``

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
            google.cloud.storage_control_v2.types.AnywhereCache:
                An Anywhere Cache Instance.
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
        if not isinstance(request, storage_control.GetAnywhereCacheRequest):
            request = storage_control.GetAnywhereCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_anywhere_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def list_anywhere_caches(
        self,
        request: Optional[
            Union[storage_control.ListAnywhereCachesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAnywhereCachesPager:
        r"""Lists Anywhere Cache instances for a given bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_list_anywhere_caches():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ListAnywhereCachesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_anywhere_caches(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ListAnywhereCachesRequest, dict]):
                The request object. Request message for
                ListAnywhereCaches.
            parent (str):
                Required. The bucket to which this
                cache belongs.

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
            google.cloud.storage_control_v2.services.storage_control.pagers.ListAnywhereCachesPager:
                Response message for
                ListAnywhereCaches.
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
        if not isinstance(request, storage_control.ListAnywhereCachesRequest):
            request = storage_control.ListAnywhereCachesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_anywhere_caches]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
        response = pagers.ListAnywhereCachesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_rapid_cache(
        self,
        request: Optional[Union[storage_control.CreateRapidCacheRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        rapid_cache: Optional[storage_control.RapidCache] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a Rapid Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_create_rapid_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.CreateRapidCacheRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_rapid_cache(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.CreateRapidCacheRequest, dict]):
                The request object. Request message for CreateRapidCache.
            parent (str):
                Required. The bucket to which this cache belongs.
                Format: ``projects/{project}/buckets/{bucket}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            rapid_cache (google.cloud.storage_control_v2.types.RapidCache):
                Required. The RapidCache to create. Default values for
                ingest_on_write, ttl and admission_policy will be
                applied if not specified in the request.

                This corresponds to the ``rapid_cache`` field
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
                :class:`google.cloud.storage_control_v2.types.RapidCache`
                A Rapid Cache Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, rapid_cache]
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
        if not isinstance(request, storage_control.CreateRapidCacheRequest):
            request = storage_control.CreateRapidCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if rapid_cache is not None:
                request.rapid_cache = rapid_cache

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_rapid_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            storage_control.RapidCache,
            metadata_type=storage_control.CreateRapidCacheMetadata,
        )

        # Done; return the response.
        return response

    def update_rapid_cache(
        self,
        request: Optional[Union[storage_control.UpdateRapidCacheRequest, dict]] = None,
        *,
        rapid_cache: Optional[storage_control.RapidCache] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates a Rapid Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_update_rapid_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.UpdateRapidCacheRequest(
                )

                # Make the request
                operation = client.update_rapid_cache(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.UpdateRapidCacheRequest, dict]):
                The request object. Request message for UpdateRapidCache.
            rapid_cache (google.cloud.storage_control_v2.types.RapidCache):
                Required. The RapidCache to update.
                This corresponds to the ``rapid_cache`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. List of fields to be updated. Mutable fields
                of RapidCache include ``ttl``, ``admission_policy`` and
                ``ingest_on_write``.

                To specify ALL fields, specify a single field with the
                value ``*``. Note: We recommend against doing this. If a
                new field is introduced at a later time, an older client
                updating with the ``*`` may accidentally reset the new
                field's value.

                Not specifying any fields is an error.

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
                :class:`google.cloud.storage_control_v2.types.RapidCache`
                A Rapid Cache Instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [rapid_cache, update_mask]
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
        if not isinstance(request, storage_control.UpdateRapidCacheRequest):
            request = storage_control.UpdateRapidCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if rapid_cache is not None:
                request.rapid_cache = rapid_cache
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_rapid_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.rapid_cache.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            storage_control.RapidCache,
            metadata_type=storage_control.UpdateRapidCacheMetadata,
        )

        # Done; return the response.
        return response

    def disable_rapid_cache(
        self,
        request: Optional[Union[storage_control.DisableRapidCacheRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Disables a Rapid Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_disable_rapid_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.DisableRapidCacheRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.disable_rapid_cache(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.DisableRapidCacheRequest, dict]):
                The request object. Request message for
                DisableRapidCache.
            name (str):
                Required. The name field in the request should be:
                ``projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}``

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
                :class:`google.cloud.storage_control_v2.types.RapidCache`
                A Rapid Cache Instance.

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
        if not isinstance(request, storage_control.DisableRapidCacheRequest):
            request = storage_control.DisableRapidCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.disable_rapid_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
            storage_control.RapidCache,
            metadata_type=storage_control.DisableRapidCacheMetadata,
        )

        # Done; return the response.
        return response

    def get_rapid_cache(
        self,
        request: Optional[Union[storage_control.GetRapidCacheRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.RapidCache:
        r"""Gets a Rapid Cache instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_rapid_cache():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetRapidCacheRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_rapid_cache(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetRapidCacheRequest, dict]):
                The request object. Request message for GetRapidCache.
            name (str):
                Required. The name field in the request should be:
                ``projects/{project}/buckets/{bucket}/rapidCaches/{rapid_cache}``

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
            google.cloud.storage_control_v2.types.RapidCache:
                A Rapid Cache Instance.
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
        if not isinstance(request, storage_control.GetRapidCacheRequest):
            request = storage_control.GetRapidCacheRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_rapid_cache]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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

    def list_rapid_caches(
        self,
        request: Optional[Union[storage_control.ListRapidCachesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListRapidCachesPager:
        r"""Lists Rapid Cache instances for a given bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_list_rapid_caches():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ListRapidCachesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_rapid_caches(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ListRapidCachesRequest, dict]):
                The request object. Request message for ListRapidCaches.
            parent (str):
                Required. The bucket to which this
                cache belongs.

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
            google.cloud.storage_control_v2.services.storage_control.pagers.ListRapidCachesPager:
                Response message for ListRapidCaches.

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
        if not isinstance(request, storage_control.ListRapidCachesRequest):
            request = storage_control.ListRapidCachesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_rapid_caches]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        setup_request_id(request, "request_id", False)

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
        response = pagers.ListRapidCachesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_project_intelligence_config(
        self,
        request: Optional[
            Union[storage_control.GetProjectIntelligenceConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceConfig:
        r"""Returns the Project scoped singleton
        IntelligenceConfig resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_project_intelligence_config():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetProjectIntelligenceConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_project_intelligence_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetProjectIntelligenceConfigRequest, dict]):
                The request object. Request message to get the ``IntelligenceConfig``
                resource associated with your project.
            name (str):
                Required. The name of the ``IntelligenceConfig``
                resource associated with your project.

                Format:
                ``projects/{id}/locations/global/intelligenceConfig``

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
            google.cloud.storage_control_v2.types.IntelligenceConfig:
                The IntelligenceConfig resource associated with your organization, folder,
                   or project.

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
        if not isinstance(request, storage_control.GetProjectIntelligenceConfigRequest):
            request = storage_control.GetProjectIntelligenceConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_project_intelligence_config
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

    def update_project_intelligence_config(
        self,
        request: Optional[
            Union[storage_control.UpdateProjectIntelligenceConfigRequest, dict]
        ] = None,
        *,
        intelligence_config: Optional[storage_control.IntelligenceConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceConfig:
        r"""Updates the Project scoped singleton
        IntelligenceConfig resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_update_project_intelligence_config():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.UpdateProjectIntelligenceConfigRequest(
                )

                # Make the request
                response = client.update_project_intelligence_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.UpdateProjectIntelligenceConfigRequest, dict]):
                The request object. Request message to update the ``IntelligenceConfig``
                resource associated with your project.
            intelligence_config (google.cloud.storage_control_v2.types.IntelligenceConfig):
                Required. The ``IntelligenceConfig`` resource to be
                updated.

                This corresponds to the ``intelligence_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The ``update_mask`` that specifies the fields
                within the ``IntelligenceConfig`` resource that should
                be modified by this update. Only the listed fields are
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
            google.cloud.storage_control_v2.types.IntelligenceConfig:
                The IntelligenceConfig resource associated with your organization, folder,
                   or project.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [intelligence_config, update_mask]
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
            request, storage_control.UpdateProjectIntelligenceConfigRequest
        ):
            request = storage_control.UpdateProjectIntelligenceConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if intelligence_config is not None:
                request.intelligence_config = intelligence_config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_project_intelligence_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("intelligence_config.name", request.intelligence_config.name),)
            ),
        )

        setup_request_id(request, "request_id", False)

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

    def get_folder_intelligence_config(
        self,
        request: Optional[
            Union[storage_control.GetFolderIntelligenceConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceConfig:
        r"""Returns the Folder scoped singleton
        IntelligenceConfig resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_folder_intelligence_config():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetFolderIntelligenceConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_folder_intelligence_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetFolderIntelligenceConfigRequest, dict]):
                The request object. Request message to get the ``IntelligenceConfig``
                resource associated with your folder.
            name (str):
                Required. The name of the ``IntelligenceConfig``
                resource associated with your folder.

                Format:
                ``folders/{id}/locations/global/intelligenceConfig``

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
            google.cloud.storage_control_v2.types.IntelligenceConfig:
                The IntelligenceConfig resource associated with your organization, folder,
                   or project.

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
        if not isinstance(request, storage_control.GetFolderIntelligenceConfigRequest):
            request = storage_control.GetFolderIntelligenceConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_folder_intelligence_config
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

    def update_folder_intelligence_config(
        self,
        request: Optional[
            Union[storage_control.UpdateFolderIntelligenceConfigRequest, dict]
        ] = None,
        *,
        intelligence_config: Optional[storage_control.IntelligenceConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceConfig:
        r"""Updates the Folder scoped singleton
        IntelligenceConfig resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_update_folder_intelligence_config():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.UpdateFolderIntelligenceConfigRequest(
                )

                # Make the request
                response = client.update_folder_intelligence_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.UpdateFolderIntelligenceConfigRequest, dict]):
                The request object. Request message to update the ``IntelligenceConfig``
                resource associated with your folder.
            intelligence_config (google.cloud.storage_control_v2.types.IntelligenceConfig):
                Required. The ``IntelligenceConfig`` resource to be
                updated.

                This corresponds to the ``intelligence_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The ``update_mask`` that specifies the fields
                within the ``IntelligenceConfig`` resource that should
                be modified by this update. Only the listed fields are
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
            google.cloud.storage_control_v2.types.IntelligenceConfig:
                The IntelligenceConfig resource associated with your organization, folder,
                   or project.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [intelligence_config, update_mask]
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
            request, storage_control.UpdateFolderIntelligenceConfigRequest
        ):
            request = storage_control.UpdateFolderIntelligenceConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if intelligence_config is not None:
                request.intelligence_config = intelligence_config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_folder_intelligence_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("intelligence_config.name", request.intelligence_config.name),)
            ),
        )

        setup_request_id(request, "request_id", False)

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

    def get_organization_intelligence_config(
        self,
        request: Optional[
            Union[storage_control.GetOrganizationIntelligenceConfigRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceConfig:
        r"""Returns the Organization scoped singleton
        IntelligenceConfig resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_organization_intelligence_config():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetOrganizationIntelligenceConfigRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_organization_intelligence_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetOrganizationIntelligenceConfigRequest, dict]):
                The request object. Request message to get the ``IntelligenceConfig``
                resource associated with your organization.
            name (str):
                Required. The name of the ``IntelligenceConfig``
                resource associated with your organization.

                Format:
                ``organizations/{org_id}/locations/global/intelligenceConfig``

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
            google.cloud.storage_control_v2.types.IntelligenceConfig:
                The IntelligenceConfig resource associated with your organization, folder,
                   or project.

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
            request, storage_control.GetOrganizationIntelligenceConfigRequest
        ):
            request = storage_control.GetOrganizationIntelligenceConfigRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_organization_intelligence_config
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

    def update_organization_intelligence_config(
        self,
        request: Optional[
            Union[storage_control.UpdateOrganizationIntelligenceConfigRequest, dict]
        ] = None,
        *,
        intelligence_config: Optional[storage_control.IntelligenceConfig] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceConfig:
        r"""Updates the Organization scoped singleton
        IntelligenceConfig resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_update_organization_intelligence_config():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.UpdateOrganizationIntelligenceConfigRequest(
                )

                # Make the request
                response = client.update_organization_intelligence_config(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.UpdateOrganizationIntelligenceConfigRequest, dict]):
                The request object. Request message to update the ``IntelligenceConfig``
                resource associated with your organization.
            intelligence_config (google.cloud.storage_control_v2.types.IntelligenceConfig):
                Required. The ``IntelligenceConfig`` resource to be
                updated.

                This corresponds to the ``intelligence_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The ``update_mask`` that specifies the fields
                within the ``IntelligenceConfig`` resource that should
                be modified by this update. Only the listed fields are
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
            google.cloud.storage_control_v2.types.IntelligenceConfig:
                The IntelligenceConfig resource associated with your organization, folder,
                   or project.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [intelligence_config, update_mask]
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
            request, storage_control.UpdateOrganizationIntelligenceConfigRequest
        ):
            request = storage_control.UpdateOrganizationIntelligenceConfigRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if intelligence_config is not None:
                request.intelligence_config = intelligence_config
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_organization_intelligence_config
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("intelligence_config.name", request.intelligence_config.name),)
            ),
        )

        setup_request_id(request, "request_id", False)

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
        request: Optional[Union[iam_policy_pb2.GetIamPolicyRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the IAM policy for a specified bucket. The ``resource``
        field in the request should be ``projects/_/buckets/{bucket}``
        for a bucket, or
        ``projects/_/buckets/{bucket}/managedFolders/{managedFolder}``
        for a managed folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            def sample_get_iam_policy():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.GetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]):
                The request object. Request message for ``GetIamPolicy`` method.
            resource (str):
                REQUIRED: The resource for which the
                policy is being requested. See the
                operation documentation for the
                appropriate value for this field.

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
            google.iam.v1.policy_pb2.Policy:
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

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time <             timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

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

        if isinstance(request, dict):
            # - The request isn't a proto-plus wrapped type,
            #   so it must be constructed via keyword expansion.
            request = iam_policy_pb2.GetIamPolicyRequest(**request)
        elif not request:
            # Null request, just make one.
            request = iam_policy_pb2.GetIamPolicyRequest()
            if resource is not None:
                request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_iam_policy]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

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

    def set_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.SetIamPolicyRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Updates an IAM policy for the specified bucket. The ``resource``
        field in the request should be ``projects/_/buckets/{bucket}``
        for a bucket, or
        ``projects/_/buckets/{bucket}/managedFolders/{managedFolder}``
        for a managed folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            def sample_set_iam_policy():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.SetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]):
                The request object. Request message for ``SetIamPolicy`` method.
            resource (str):
                REQUIRED: The resource for which the
                policy is being specified. See the
                operation documentation for the
                appropriate value for this field.

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
            google.iam.v1.policy_pb2.Policy:
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

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time <             timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

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

        if isinstance(request, dict):
            # - The request isn't a proto-plus wrapped type,
            #   so it must be constructed via keyword expansion.
            request = iam_policy_pb2.SetIamPolicyRequest(**request)
        elif not request:
            # Null request, just make one.
            request = iam_policy_pb2.SetIamPolicyRequest()
            if resource is not None:
                request.resource = resource

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_iam_policy]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

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

    def test_iam_permissions(
        self,
        request: Optional[Union[iam_policy_pb2.TestIamPermissionsRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        permissions: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Tests a set of permissions on the given bucket, object, or
        managed folder to see which, if any, are held by the caller. The
        ``resource`` field in the request should be
        ``projects/_/buckets/{bucket}`` for a bucket,
        ``projects/_/buckets/{bucket}/objects/{object}`` for an object,
        or
        ``projects/_/buckets/{bucket}/managedFolders/{managedFolder}``
        for a managed folder.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            def sample_test_iam_permissions():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.TestIamPermissionsRequest(
                    resource="resource_value",
                    permissions=['permissions_value1', 'permissions_value2'],
                )

                # Make the request
                response = client.test_iam_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]):
                The request object. Request message for ``TestIamPermissions`` method.
            resource (str):
                REQUIRED: The resource for which the
                policy detail is being requested. See
                the operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            permissions (MutableSequence[str]):
                The set of permissions to check for the ``resource``.
                Permissions with wildcards (such as '*' or 'storage.*')
                are not allowed. For more information see `IAM
                Overview <https://cloud.google.com/iam/docs/overview#permissions>`__.

                This corresponds to the ``permissions`` field
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
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for TestIamPermissions method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource, permissions]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        if isinstance(request, dict):
            # - The request isn't a proto-plus wrapped type,
            #   so it must be constructed via keyword expansion.
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)
        elif not request:
            # Null request, just make one.
            request = iam_policy_pb2.TestIamPermissionsRequest()
            if resource is not None:
                request.resource = resource
            if permissions:
                request.permissions.extend(permissions)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.test_iam_permissions]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile("^(?P<bucket>.*)$")
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)/objects(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)/managedFolders(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.resource)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

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

    def get_intelligence_finding(
        self,
        request: Optional[
            Union[storage_control.GetIntelligenceFindingRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceFinding:
        r"""Gets the ``IntelligenceFinding`` for a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_intelligence_finding():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetIntelligenceFindingRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_intelligence_finding(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetIntelligenceFindingRequest, dict]):
                The request object. Request message to get the ``IntelligenceFinding``
                resource associated with a project.
            name (str):
                Required. The name of the ``IntelligenceFinding``
                resource.

                Format:
                ``projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}``

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
            google.cloud.storage_control_v2.types.IntelligenceFinding:
                The IntelligenceFinding resource that represents a security, performance,
                   or cost-related finding about a project or bucket.

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
        if not isinstance(request, storage_control.GetIntelligenceFindingRequest):
            request = storage_control.GetIntelligenceFindingRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_intelligence_finding]

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

    def list_intelligence_findings(
        self,
        request: Optional[
            Union[storage_control.ListIntelligenceFindingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListIntelligenceFindingsPager:
        r"""Lists the ``IntelligenceFinding`` resources for the specified
        the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_list_intelligence_findings():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ListIntelligenceFindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_intelligence_findings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ListIntelligenceFindingsRequest, dict]):
                The request object. Request message to list ``IntelligenceFinding``
                resources associated with a project.
            parent (str):
                Required. The parent of the ``IntelligenceFinding``
                resource.

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
            google.cloud.storage_control_v2.services.storage_control.pagers.ListIntelligenceFindingsPager:
                Response message to list the IntelligenceFinding resources associated with
                   a project.

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
        if not isinstance(request, storage_control.ListIntelligenceFindingsRequest):
            request = storage_control.ListIntelligenceFindingsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_intelligence_findings
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
        response = pagers.ListIntelligenceFindingsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def summarize_intelligence_findings(
        self,
        request: Optional[
            Union[storage_control.SummarizeIntelligenceFindingsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SummarizeIntelligenceFindingsPager:
        r"""Summarizes the intelligence findings for the
        specified scope (organization, folder or project).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_summarize_intelligence_findings():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.SummarizeIntelligenceFindingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.summarize_intelligence_findings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.SummarizeIntelligenceFindingsRequest, dict]):
                The request object. Request message to summarize the
                intelligence findings for the specified
                scope (organization, folder or project).
            parent (str):
                Required. The scope to summarize the findings for.
                Format:

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
            google.cloud.storage_control_v2.services.storage_control.pagers.SummarizeIntelligenceFindingsPager:
                Response message to summarize the
                intelligence findings for a specified
                scope (organization, folder or project).

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
            request, storage_control.SummarizeIntelligenceFindingsRequest
        ):
            request = storage_control.SummarizeIntelligenceFindingsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.summarize_intelligence_findings
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
        response = pagers.SummarizeIntelligenceFindingsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_intelligence_finding_revision(
        self,
        request: Optional[
            Union[storage_control.GetIntelligenceFindingRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.IntelligenceFindingRevision:
        r"""Gets the ``IntelligenceFindingRevision`` resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_get_intelligence_finding_revision():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.GetIntelligenceFindingRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_intelligence_finding_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.GetIntelligenceFindingRevisionRequest, dict]):
                The request object. Request message to get the
                ``IntelligenceFindingRevision`` resource associated with
                a project.
            name (str):
                Required. The name of the
                ``IntelligenceFindingRevision`` resource.

                Format:
                -------

                ``projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}/revisions/{revision}``

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
            google.cloud.storage_control_v2.types.IntelligenceFindingRevision:
                An IntelligenceFindingRevision represents a specific revision of an
                   IntelligenceFinding resource.

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
            request, storage_control.GetIntelligenceFindingRevisionRequest
        ):
            request = storage_control.GetIntelligenceFindingRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_intelligence_finding_revision
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

    def list_intelligence_finding_revisions(
        self,
        request: Optional[
            Union[storage_control.ListIntelligenceFindingRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListIntelligenceFindingRevisionsPager:
        r"""Lists all the revisions of an ``IntelligenceFinding`` resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_list_intelligence_finding_revisions():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ListIntelligenceFindingRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_intelligence_finding_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ListIntelligenceFindingRevisionsRequest, dict]):
                The request object. Request message to list ``IntelligenceFindingRevision``
                resources associated with a project.
            parent (str):
                Required. The parent of the
                ``IntelligenceFindingRevision`` resource.

                Format:
                -------

                ``projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}``

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
            google.cloud.storage_control_v2.services.storage_control.pagers.ListIntelligenceFindingRevisionsPager:
                Response message to list IntelligenceFindingRevision resources associated
                   with a project.

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
            request, storage_control.ListIntelligenceFindingRevisionsRequest
        ):
            request = storage_control.ListIntelligenceFindingRevisionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_intelligence_finding_revisions
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
        response = pagers.ListIntelligenceFindingRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def view_object_full_context(
        self,
        request: Optional[
            Union[storage_control.ViewObjectFullContextRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        context_key: Optional[str] = None,
        generation: Optional[int] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> storage_control.ObjectFullContext:
        r"""Retrieves the full content of an object context, including its
        key, value, and any associated extended data for a given context
        key.

        Object contexts can optionally contain extended data. If an
        object context contains extended data, the metadata payload
        structure will contain only its type URL. To retrieve the full
        extended data, call this method.

        Returns the complete representation of the context as an
        [``ObjectFullContext``][google.storage.control.v2.ObjectFullContext].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import storage_control_v2

            def sample_view_object_full_context():
                # Create a client
                client = storage_control_v2.StorageControlClient()

                # Initialize request argument(s)
                request = storage_control_v2.ViewObjectFullContextRequest(
                    context_key="context_key_value",
                    name="name_value",
                )

                # Make the request
                response = client.view_object_full_context(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.storage_control_v2.types.ViewObjectFullContextRequest, dict]):
                The request object. Request message for
                ViewObjectFullContext.
            name (str):
                Required. The name of the object. Format:
                ``projects/{project}/buckets/{bucket}/objects/{object}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            context_key (str):
                Required. The key of the object
                context to retrieve.

                This corresponds to the ``context_key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            generation (int):
                Optional. If present, selects a
                specific revision of this object (as
                opposed to the latest version, the
                default).

                This corresponds to the ``generation`` field
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
            google.cloud.storage_control_v2.types.ObjectFullContext:
                A full representation of an object
                context.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, context_key, generation]
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
        if not isinstance(request, storage_control.ViewObjectFullContextRequest):
            request = storage_control.ViewObjectFullContextRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if context_key is not None:
                request.context_key = context_key
            if generation is not None:
                request.generation = generation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.view_object_full_context]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^(?P<bucket>projects/[^/]+/buckets/[^/]+)(?:/.*)?$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("bucket"):
            header_params["bucket"] = regex_match.group("bucket")

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

    def __enter__(self) -> "StorageControlClient":
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

__all__ = ("StorageControlClient",)
