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

from google.cloud.redis_cluster_v1beta1 import gapic_version as package_version
from google.cloud.redis_cluster_v1beta1._compat import (
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
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster import pagers
from google.cloud.redis_cluster_v1beta1.types import cloud_redis_cluster

from .transports.base import DEFAULT_CLIENT_INFO, CloudRedisClusterTransport
from .transports.grpc import CloudRedisClusterGrpcTransport
from .transports.grpc_asyncio import CloudRedisClusterGrpcAsyncIOTransport
from .transports.rest import CloudRedisClusterRestTransport


class CloudRedisClusterClientMeta(type):
    """Metaclass for the CloudRedisCluster client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[CloudRedisClusterTransport]]
    _transport_registry["grpc"] = CloudRedisClusterGrpcTransport
    _transport_registry["grpc_asyncio"] = CloudRedisClusterGrpcAsyncIOTransport
    _transport_registry["rest"] = CloudRedisClusterRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[CloudRedisClusterTransport]:
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


class CloudRedisClusterClient(metaclass=CloudRedisClusterClientMeta):
    """Configures and manages Cloud Memorystore for Redis clusters

    Google Cloud Memorystore for Redis Cluster

    The ``redis.googleapis.com`` service implements the Google Cloud
    Memorystore for Redis API and defines the following resource model
    for managing Redis clusters:

    - The service works with a collection of cloud projects, named:
      ``/projects/*``
    - Each project has a collection of available locations, named:
      ``/locations/*``
    - Each location has a collection of Redis clusters, named:
      ``/clusters/*``
    - As such, Redis clusters are resources of the form:
      ``/projects/{project_id}/locations/{location_id}/clusters/{instance_id}``

    Note that location_id must be a GCP ``region``; for example:

    - ``projects/redpepper-1290/locations/us-central1/clusters/my-redis``
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "redis.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "redis.{UNIVERSE_DOMAIN}"
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
            CloudRedisClusterClient: The constructed client.
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
            CloudRedisClusterClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> CloudRedisClusterTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudRedisClusterTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def acl_policy_path(
        project: str,
        location: str,
        acl_policy: str,
    ) -> str:
        """Returns a fully-qualified acl_policy string."""
        return (
            "projects/{project}/locations/{location}/aclPolicies/{acl_policy}".format(
                project=project,
                location=location,
                acl_policy=acl_policy,
            )
        )

    @staticmethod
    def parse_acl_policy_path(path: str) -> Dict[str, str]:
        """Parses a acl_policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/aclPolicies/(?P<acl_policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def acl_policy_revision_path(
        project: str,
        location: str,
        acl_policy: str,
        revision: str,
    ) -> str:
        """Returns a fully-qualified acl_policy_revision string."""
        return "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}".format(
            project=project,
            location=location,
            acl_policy=acl_policy,
            revision=revision,
        )

    @staticmethod
    def parse_acl_policy_revision_path(path: str) -> Dict[str, str]:
        """Parses a acl_policy_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/aclPolicies/(?P<acl_policy>.+?)/revisions/(?P<revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def auth_token_path(
        project: str,
        location: str,
        cluster: str,
        token_auth_user: str,
        auth_token: str,
    ) -> str:
        """Returns a fully-qualified auth_token string."""
        return "projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}".format(
            project=project,
            location=location,
            cluster=cluster,
            token_auth_user=token_auth_user,
            auth_token=auth_token,
        )

    @staticmethod
    def parse_auth_token_path(path: str) -> Dict[str, str]:
        """Parses a auth_token path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/clusters/(?P<cluster>.+?)/tokenAuthUsers/(?P<token_auth_user>.+?)/authTokens/(?P<auth_token>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def backup_path(
        project: str,
        location: str,
        backup_collection: str,
        backup: str,
    ) -> str:
        """Returns a fully-qualified backup string."""
        return "projects/{project}/locations/{location}/backupCollections/{backup_collection}/backups/{backup}".format(
            project=project,
            location=location,
            backup_collection=backup_collection,
            backup=backup,
        )

    @staticmethod
    def parse_backup_path(path: str) -> Dict[str, str]:
        """Parses a backup path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/backupCollections/(?P<backup_collection>.+?)/backups/(?P<backup>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def backup_collection_path(
        project: str,
        location: str,
        backup_collection: str,
    ) -> str:
        """Returns a fully-qualified backup_collection string."""
        return "projects/{project}/locations/{location}/backupCollections/{backup_collection}".format(
            project=project,
            location=location,
            backup_collection=backup_collection,
        )

    @staticmethod
    def parse_backup_collection_path(path: str) -> Dict[str, str]:
        """Parses a backup_collection path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/backupCollections/(?P<backup_collection>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ca_pool_path(
        project: str,
        location: str,
        ca_pool: str,
    ) -> str:
        """Returns a fully-qualified ca_pool string."""
        return "projects/{project}/locations/{location}/caPools/{ca_pool}".format(
            project=project,
            location=location,
            ca_pool=ca_pool,
        )

    @staticmethod
    def parse_ca_pool_path(path: str) -> Dict[str, str]:
        """Parses a ca_pool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/caPools/(?P<ca_pool>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def certificate_authority_path(
        project: str,
        location: str,
        cluster: str,
    ) -> str:
        """Returns a fully-qualified certificate_authority string."""
        return "projects/{project}/locations/{location}/clusters/{cluster}/certificateAuthority".format(
            project=project,
            location=location,
            cluster=cluster,
        )

    @staticmethod
    def parse_certificate_authority_path(path: str) -> Dict[str, str]:
        """Parses a certificate_authority path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/clusters/(?P<cluster>.+?)/certificateAuthority$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def cluster_path(
        project: str,
        location: str,
        cluster: str,
    ) -> str:
        """Returns a fully-qualified cluster string."""
        return "projects/{project}/locations/{location}/clusters/{cluster}".format(
            project=project,
            location=location,
            cluster=cluster,
        )

    @staticmethod
    def parse_cluster_path(path: str) -> Dict[str, str]:
        """Parses a cluster path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/clusters/(?P<cluster>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def crypto_key_path(
        project: str,
        location: str,
        key_ring: str,
        crypto_key: str,
    ) -> str:
        """Returns a fully-qualified crypto_key string."""
        return "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}".format(
            project=project,
            location=location,
            key_ring=key_ring,
            crypto_key=crypto_key,
        )

    @staticmethod
    def parse_crypto_key_path(path: str) -> Dict[str, str]:
        """Parses a crypto_key path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/keyRings/(?P<key_ring>.+?)/cryptoKeys/(?P<crypto_key>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def crypto_key_version_path(
        project: str,
        location: str,
        key_ring: str,
        crypto_key: str,
        crypto_key_version: str,
    ) -> str:
        """Returns a fully-qualified crypto_key_version string."""
        return "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}".format(
            project=project,
            location=location,
            key_ring=key_ring,
            crypto_key=crypto_key,
            crypto_key_version=crypto_key_version,
        )

    @staticmethod
    def parse_crypto_key_version_path(path: str) -> Dict[str, str]:
        """Parses a crypto_key_version path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/keyRings/(?P<key_ring>.+?)/cryptoKeys/(?P<crypto_key>.+?)/cryptoKeyVersions/(?P<crypto_key_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def forwarding_rule_path(
        project: str,
        region: str,
        forwarding_rule: str,
    ) -> str:
        """Returns a fully-qualified forwarding_rule string."""
        return "projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}".format(
            project=project,
            region=region,
            forwarding_rule=forwarding_rule,
        )

    @staticmethod
    def parse_forwarding_rule_path(path: str) -> Dict[str, str]:
        """Parses a forwarding_rule path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/regions/(?P<region>.+?)/forwardingRules/(?P<forwarding_rule>.+?)$",
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
    def service_attachment_path(
        project: str,
        region: str,
        service_attachment: str,
    ) -> str:
        """Returns a fully-qualified service_attachment string."""
        return "projects/{project}/regions/{region}/serviceAttachments/{service_attachment}".format(
            project=project,
            region=region,
            service_attachment=service_attachment,
        )

    @staticmethod
    def parse_service_attachment_path(path: str) -> Dict[str, str]:
        """Parses a service_attachment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/regions/(?P<region>.+?)/serviceAttachments/(?P<service_attachment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def shared_regional_certificate_authority_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified shared_regional_certificate_authority string."""
        return "projects/{project}/locations/{location}/sharedRegionalCertificateAuthority".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_shared_regional_certificate_authority_path(path: str) -> Dict[str, str]:
        """Parses a shared_regional_certificate_authority path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/sharedRegionalCertificateAuthority$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def token_auth_user_path(
        project: str,
        location: str,
        cluster: str,
        token_auth_user: str,
    ) -> str:
        """Returns a fully-qualified token_auth_user string."""
        return "projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}".format(
            project=project,
            location=location,
            cluster=cluster,
            token_auth_user=token_auth_user,
        )

    @staticmethod
    def parse_token_auth_user_path(path: str) -> Dict[str, str]:
        """Parses a token_auth_user path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/clusters/(?P<cluster>.+?)/tokenAuthUsers/(?P<token_auth_user>.+?)$",
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
                CloudRedisClusterTransport,
                Callable[..., CloudRedisClusterTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud redis cluster client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CloudRedisClusterTransport,Callable[..., CloudRedisClusterTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CloudRedisClusterTransport constructor.
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
        self._client_cert_source = CloudRedisClusterClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=CloudRedisClusterClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, CloudRedisClusterTransport)
        if transport_provided:
            # transport is a CloudRedisClusterTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(CloudRedisClusterTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=CloudRedisClusterClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=CloudRedisClusterClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=CloudRedisClusterClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[CloudRedisClusterTransport],
                Callable[..., CloudRedisClusterTransport],
            ] = (
                CloudRedisClusterClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., CloudRedisClusterTransport], transport)
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
                    "Created client `google.cloud.redis.cluster_v1beta1.CloudRedisClusterClient`.",
                    extra={
                        "serviceName": "google.cloud.redis.cluster.v1beta1.CloudRedisCluster",
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
                        "serviceName": "google.cloud.redis.cluster.v1beta1.CloudRedisCluster",
                        "credentialsType": None,
                    },
                )

    def list_clusters(
        self,
        request: Optional[Union[cloud_redis_cluster.ListClustersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListClustersPager:
        r"""Lists all Redis clusters owned by a project in either the
        specified location (region) or all locations.

        The location should have the following format:

        - ``projects/{project_id}/locations/{location_id}``

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_clusters():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListClustersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_clusters(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListClustersRequest, dict]):
                The request object. Request for [ListClusters][CloudRedis.ListClusters].
            parent (str):
                Required. The resource name of the cluster location
                using the form:
                ``projects/{project_id}/locations/{location_id}`` where
                ``location_id`` refers to a GCP region.

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersPager:
                Response for [ListClusters][CloudRedis.ListClusters].

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
        if not isinstance(request, cloud_redis_cluster.ListClustersRequest):
            request = cloud_redis_cluster.ListClustersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_clusters]

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
        response = pagers.ListClustersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_acl_policies(
        self,
        request: Optional[
            Union[cloud_redis_cluster.ListAclPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAclPoliciesPager:
        r"""Lists all ACL policies owned by a project in either the
        specified location (region) or all locations.

        The location should have the following format:

        - ``projects/{project_id}/locations/{location_id}``

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_acl_policies():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListAclPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_acl_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListAclPoliciesRequest, dict]):
                The request object. Request for ``ListAclPolicies``.
            parent (str):
                Required. The resource name of the ACL policy location
                using the form:
                ``projects/{project_id}/locations/{location_id}`` where
                ``location_id`` refers to a Google Cloud region.

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListAclPoliciesPager:
                Response for ListAclPolicies.

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
        if not isinstance(request, cloud_redis_cluster.ListAclPoliciesRequest):
            request = cloud_redis_cluster.ListAclPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_acl_policies]

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
        response = pagers.ListAclPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_cluster(
        self,
        request: Optional[Union[cloud_redis_cluster.GetClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.Cluster:
        r"""Gets the details of a specific Redis cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_cluster():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetClusterRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_cluster(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetClusterRequest, dict]):
                The request object. Request for [GetCluster][CloudRedis.GetCluster].
            name (str):
                Required. Redis cluster resource name using the form:
                ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
                where ``location_id`` refers to a GCP region.

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
            google.cloud.redis_cluster_v1beta1.types.Cluster:
                A cluster instance.
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
        if not isinstance(request, cloud_redis_cluster.GetClusterRequest):
            request = cloud_redis_cluster.GetClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_cluster]

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

    def get_acl_policy(
        self,
        request: Optional[Union[cloud_redis_cluster.GetAclPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.AclPolicy:
        r"""Gets the details of a specific Redis Cluster ACL
        policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_acl_policy():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetAclPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_acl_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetAclPolicyRequest, dict]):
                The request object. Request for ``GetAclPolicy``.
            name (str):
                Required. Redis ACL policy resource name using the form:
                ``projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}``
                where ``location_id`` refers to a Google Cloud region.

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
            google.cloud.redis_cluster_v1beta1.types.AclPolicy:
                The ACL policy resource.
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
        if not isinstance(request, cloud_redis_cluster.GetAclPolicyRequest):
            request = cloud_redis_cluster.GetAclPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_acl_policy]

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

    def update_cluster(
        self,
        request: Optional[Union[cloud_redis_cluster.UpdateClusterRequest, dict]] = None,
        *,
        cluster: Optional[cloud_redis_cluster.Cluster] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the metadata and configuration of a specific
        Redis cluster.
        Completed longrunning.Operation will contain the new
        cluster object in the response field. The returned
        operation is automatically deleted after a few hours, so
        there is no need to call DeleteOperation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_update_cluster():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                cluster = redis_cluster_v1beta1.Cluster()
                cluster.name = "name_value"

                request = redis_cluster_v1beta1.UpdateClusterRequest(
                    cluster=cluster,
                )

                # Make the request
                operation = client.update_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.UpdateClusterRequest, dict]):
                The request object. Request for [UpdateCluster][CloudRedis.UpdateCluster].
            cluster (google.cloud.redis_cluster_v1beta1.types.Cluster):
                Required. Update description. Only fields specified in
                update_mask are updated.

                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. Mask of fields to update. At least one path
                must be supplied in this field. The elements of the
                repeated paths field may only include these fields from
                [Cluster][google.cloud.redis.cluster.v1beta1.Cluster]:

                - ``size_gb``
                - ``replica_count``

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
                :class:`google.cloud.redis_cluster_v1beta1.types.Cluster`
                A cluster instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [cluster, update_mask]
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
        if not isinstance(request, cloud_redis_cluster.UpdateClusterRequest):
            request = cloud_redis_cluster.UpdateClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if cluster is not None:
                request.cluster = cluster
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_cluster]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("cluster.name", request.cluster.name),)
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
            cloud_redis_cluster.Cluster,
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def update_acl_policy(
        self,
        request: Optional[
            Union[cloud_redis_cluster.UpdateAclPolicyRequest, dict]
        ] = None,
        *,
        acl_policy: Optional[cloud_redis_cluster.AclPolicy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Updates the ACL policy.

        The operation applies the updated ACL policy to all of
        the linked clusters. If Memorystore can apply the policy
        to all clusters, then the operation returns a SUCCESS
        status. If Memorystore can't apply the policy to all
        clusters, then to ensure eventual consistency,
        Memorystore uses reconciliation to apply the policy to
        the failed clusters.

        Completed longrunning.Operation will contain the new ACL
        policy object in the response field.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_update_acl_policy():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                acl_policy = redis_cluster_v1beta1.AclPolicy()
                acl_policy.rules.username = "username_value"
                acl_policy.rules.rule = "rule_value"

                request = redis_cluster_v1beta1.UpdateAclPolicyRequest(
                    acl_policy=acl_policy,
                )

                # Make the request
                operation = client.update_acl_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.UpdateAclPolicyRequest, dict]):
                The request object. Request for ``UpdateAclPolicy``.
            acl_policy (google.cloud.redis_cluster_v1beta1.types.AclPolicy):
                Required. The ACL policy to be
                updated.

                This corresponds to the ``acl_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Mask of fields to be updated. At least one
                path must be supplied in this field. The elements of the
                repeated paths field may only include these fields from
                ``AclPolicy``:

                - ``rules``

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
                :class:`google.cloud.redis_cluster_v1beta1.types.AclPolicy`
                The ACL policy resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [acl_policy, update_mask]
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
        if not isinstance(request, cloud_redis_cluster.UpdateAclPolicyRequest):
            request = cloud_redis_cluster.UpdateAclPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if acl_policy is not None:
                request.acl_policy = acl_policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_acl_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("acl_policy.name", request.acl_policy.name),)
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
            cloud_redis_cluster.AclPolicy,
            metadata_type=cloud_redis_cluster.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_cluster(
        self,
        request: Optional[Union[cloud_redis_cluster.DeleteClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a specific Redis cluster. Cluster stops
        serving and data is deleted.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_delete_cluster():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.DeleteClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.DeleteClusterRequest, dict]):
                The request object. Request for [DeleteCluster][CloudRedis.DeleteCluster].
            name (str):
                Required. Redis cluster resource name using the form:
                ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
                where ``location_id`` refers to a GCP region.

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
        if not isinstance(request, cloud_redis_cluster.DeleteClusterRequest):
            request = cloud_redis_cluster.DeleteClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_cluster]

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
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def delete_acl_policy(
        self,
        request: Optional[
            Union[cloud_redis_cluster.DeleteAclPolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a specific ACL policy. This action will
        delete the ACL policy and all the rules associated with
        it. An ACL policy cannot be deleted if it is attached to
        a cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_delete_acl_policy():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.DeleteAclPolicyRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_acl_policy(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.DeleteAclPolicyRequest, dict]):
                The request object. Request for ``DeleteAclPolicy``.
            name (str):
                Required. Redis ACL policy resource name using the form:
                ``projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}``
                where ``location_id`` refers to a Google Cloud region.

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
        if not isinstance(request, cloud_redis_cluster.DeleteAclPolicyRequest):
            request = cloud_redis_cluster.DeleteAclPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_acl_policy]

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
            metadata_type=cloud_redis_cluster.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_acl_policy_revision(
        self,
        request: Optional[
            Union[cloud_redis_cluster.GetAclPolicyRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.AclPolicyRevision:
        r"""Gets details of a specific ACL policy revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_acl_policy_revision():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetAclPolicyRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_acl_policy_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetAclPolicyRevisionRequest, dict]):
                The request object. Request for ``GetAclPolicyRevision``.
            name (str):
                Required. Redis ACL policy revision resource name using
                the form:
                ``projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}/revisions/{revision_id}``
                where ``location_id`` refers to a Google Cloud region.

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
            google.cloud.redis_cluster_v1beta1.types.AclPolicyRevision:
                The ACL policy revision resource.
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
        if not isinstance(request, cloud_redis_cluster.GetAclPolicyRevisionRequest):
            request = cloud_redis_cluster.GetAclPolicyRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_acl_policy_revision]

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

    def list_acl_policy_revisions(
        self,
        request: Optional[
            Union[cloud_redis_cluster.ListAclPolicyRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAclPolicyRevisionsPager:
        r"""Lists all ACL policy revisions in a given ACL policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_acl_policy_revisions():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListAclPolicyRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_acl_policy_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListAclPolicyRevisionsRequest, dict]):
                The request object. Request for ``ListAclPolicyRevisions``.
            parent (str):
                Required. The name of the ACL policy to list revisions
                for. Format:
                "projects/{project_id}/locations/{location_id}/aclPolicies/{acl_policy_id}"

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListAclPolicyRevisionsPager:
                Response for ListAclPolicyRevisions.

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
        if not isinstance(request, cloud_redis_cluster.ListAclPolicyRevisionsRequest):
            request = cloud_redis_cluster.ListAclPolicyRevisionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_acl_policy_revisions
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
        response = pagers.ListAclPolicyRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_cluster(
        self,
        request: Optional[Union[cloud_redis_cluster.CreateClusterRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        cluster: Optional[cloud_redis_cluster.Cluster] = None,
        cluster_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a Redis cluster based on the specified
        properties. The creation is executed asynchronously and
        callers may check the returned operation to track its
        progress. Once the operation is completed the Redis
        cluster will be fully functional. The completed
        longrunning.Operation will contain the new cluster
        object in the response field.

        The returned operation is automatically deleted after a
        few hours, so there is no need to call DeleteOperation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_create_cluster():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                cluster = redis_cluster_v1beta1.Cluster()
                cluster.name = "name_value"

                request = redis_cluster_v1beta1.CreateClusterRequest(
                    parent="parent_value",
                    cluster_id="cluster_id_value",
                    cluster=cluster,
                )

                # Make the request
                operation = client.create_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.CreateClusterRequest, dict]):
                The request object. Request for [CreateCluster][CloudRedis.CreateCluster].
            parent (str):
                Required. The resource name of the cluster location
                using the form:
                ``projects/{project_id}/locations/{location_id}`` where
                ``location_id`` refers to a GCP region.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster (google.cloud.redis_cluster_v1beta1.types.Cluster):
                Required. The cluster that is to be
                created.

                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            cluster_id (str):
                Required. The logical name of the Redis cluster in the
                customer project with the following restrictions:

                - Must contain only lowercase letters, numbers, and
                  hyphens.
                - Must start with a letter.
                - Must be between 1-63 characters.
                - Must end with a number or a letter.
                - Must be unique within the customer project / location

                This corresponds to the ``cluster_id`` field
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
                :class:`google.cloud.redis_cluster_v1beta1.types.Cluster`
                A cluster instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, cluster, cluster_id]
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
        if not isinstance(request, cloud_redis_cluster.CreateClusterRequest):
            request = cloud_redis_cluster.CreateClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if cluster is not None:
                request.cluster = cluster
            if cluster_id is not None:
                request.cluster_id = cluster_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_cluster]

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
            cloud_redis_cluster.Cluster,
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def create_acl_policy(
        self,
        request: Optional[
            Union[cloud_redis_cluster.CreateAclPolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        acl_policy: Optional[cloud_redis_cluster.AclPolicy] = None,
        acl_policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.AclPolicy:
        r"""Creates an ACL policy.
        The creation is executed synchronously and the policy is
        available for use immediately after the RPC returns.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_create_acl_policy():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                acl_policy = redis_cluster_v1beta1.AclPolicy()
                acl_policy.rules.username = "username_value"
                acl_policy.rules.rule = "rule_value"

                request = redis_cluster_v1beta1.CreateAclPolicyRequest(
                    parent="parent_value",
                    acl_policy_id="acl_policy_id_value",
                    acl_policy=acl_policy,
                )

                # Make the request
                response = client.create_acl_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.CreateAclPolicyRequest, dict]):
                The request object. Request for ``CreateAclPolicy``.
            parent (str):
                Required. The resource name of the cluster location
                using the form:
                ``projects/{project_id}/locations/{location_id}`` where
                ``location_id`` refers to a Google Cloud region.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            acl_policy (google.cloud.redis_cluster_v1beta1.types.AclPolicy):
                Required. The ACL policy that is to
                be created.

                This corresponds to the ``acl_policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            acl_policy_id (str):
                Required. The logical name of the ACL policy in the
                customer project with the following restrictions:

                - Must contain only lowercase letters, numbers, and
                  hyphens.
                - Must start with a letter.
                - Must be between 1-63 characters.
                - Must end with a number or a letter.
                - Must be unique within the customer project / location

                This corresponds to the ``acl_policy_id`` field
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
            google.cloud.redis_cluster_v1beta1.types.AclPolicy:
                The ACL policy resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, acl_policy, acl_policy_id]
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
        if not isinstance(request, cloud_redis_cluster.CreateAclPolicyRequest):
            request = cloud_redis_cluster.CreateAclPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if acl_policy is not None:
                request.acl_policy = acl_policy
            if acl_policy_id is not None:
                request.acl_policy_id = acl_policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_acl_policy]

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

    def get_cluster_certificate_authority(
        self,
        request: Optional[
            Union[cloud_redis_cluster.GetClusterCertificateAuthorityRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.CertificateAuthority:
        r"""Gets the details of certificate authority information
        for Redis cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_cluster_certificate_authority():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetClusterCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_cluster_certificate_authority(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetClusterCertificateAuthorityRequest, dict]):
                The request object. Request for
                [GetClusterCertificateAuthorityRequest][CloudRedis.GetClusterCertificateAuthorityRequest].
            name (str):
                Required. Redis cluster certificate authority resource
                name using the form:
                ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}/certificateAuthority``
                where ``location_id`` refers to a GCP region.

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
            google.cloud.redis_cluster_v1beta1.types.CertificateAuthority:
                Redis cluster certificate authority
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
            request, cloud_redis_cluster.GetClusterCertificateAuthorityRequest
        ):
            request = cloud_redis_cluster.GetClusterCertificateAuthorityRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_cluster_certificate_authority
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

    def get_shared_regional_certificate_authority(
        self,
        request: Optional[
            Union[
                cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.SharedRegionalCertificateAuthority:
        r"""Gets the details of regional certificate authority
        information for Redis cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_shared_regional_certificate_authority():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetSharedRegionalCertificateAuthorityRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_shared_regional_certificate_authority(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetSharedRegionalCertificateAuthorityRequest, dict]):
                The request object. Request for
                [GetSharedRegionalCertificateAuthority][CloudRedis.GetSharedRegionalCertificateAuthority].
            name (str):
                Required. Regional certificate authority resource name
                using the form:
                ``projects/{project_id}/locations/{location_id}/sharedRegionalCertificateAuthority``
                where ``location_id`` refers to a Google Cloud region.

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
            google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority:
                Shared regional certificate authority
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
            request, cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest
        ):
            request = cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_shared_regional_certificate_authority
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

    def reschedule_cluster_maintenance(
        self,
        request: Optional[
            Union[cloud_redis_cluster.RescheduleClusterMaintenanceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        reschedule_type: Optional[
            cloud_redis_cluster.RescheduleClusterMaintenanceRequest.RescheduleType
        ] = None,
        schedule_time: Optional[timestamp_pb2.Timestamp] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Reschedules upcoming maintenance event.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_reschedule_cluster_maintenance():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.RescheduleClusterMaintenanceRequest(
                    name="name_value",
                    reschedule_type="SPECIFIC_TIME",
                )

                # Make the request
                operation = client.reschedule_cluster_maintenance(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest, dict]):
                The request object. Request for rescheduling a cluster
                maintenance.
            name (str):
                Required. Redis Cluster instance resource name using the
                form:
                ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
                where ``location_id`` refers to a GCP region.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            reschedule_type (google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest.RescheduleType):
                Required. If reschedule type is SPECIFIC_TIME, must set
                up schedule_time as well.

                This corresponds to the ``reschedule_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            schedule_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. Timestamp when the maintenance shall be
                rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC
                3339 format, for example ``2012-11-15T16:19:00.094Z``.

                This corresponds to the ``schedule_time`` field
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
                :class:`google.cloud.redis_cluster_v1beta1.types.Cluster`
                A cluster instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, reschedule_type, schedule_time]
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
            request, cloud_redis_cluster.RescheduleClusterMaintenanceRequest
        ):
            request = cloud_redis_cluster.RescheduleClusterMaintenanceRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if reschedule_type is not None:
                request.reschedule_type = reschedule_type
            if schedule_time is not None:
                request.schedule_time = schedule_time

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.reschedule_cluster_maintenance
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
            cloud_redis_cluster.Cluster,
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def list_backup_collections(
        self,
        request: Optional[
            Union[cloud_redis_cluster.ListBackupCollectionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupCollectionsPager:
        r"""Lists all backup collections owned by a consumer project in
        either the specified location (region) or all locations.

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_backup_collections():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListBackupCollectionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backup_collections(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest, dict]):
                The request object. Request for [ListBackupCollections]
            parent (str):
                Required. The resource name of the backupCollection
                location using the form:
                ``projects/{project_id}/locations/{location_id}`` where
                ``location_id`` refers to a GCP region.

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsPager:
                Response for [ListBackupCollections].

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
        if not isinstance(request, cloud_redis_cluster.ListBackupCollectionsRequest):
            request = cloud_redis_cluster.ListBackupCollectionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_backup_collections]

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
        response = pagers.ListBackupCollectionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_backup_collection(
        self,
        request: Optional[
            Union[cloud_redis_cluster.GetBackupCollectionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.BackupCollection:
        r"""Get a backup collection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_backup_collection():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetBackupCollectionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_backup_collection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetBackupCollectionRequest, dict]):
                The request object. Request for [GetBackupCollection].
            name (str):
                Required. Redis backupCollection resource name using the
                form:
                ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}``
                where ``location_id`` refers to a GCP region.

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
            google.cloud.redis_cluster_v1beta1.types.BackupCollection:
                BackupCollection of a cluster.
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
        if not isinstance(request, cloud_redis_cluster.GetBackupCollectionRequest):
            request = cloud_redis_cluster.GetBackupCollectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_backup_collection]

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

    def list_backups(
        self,
        request: Optional[Union[cloud_redis_cluster.ListBackupsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBackupsPager:
        r"""Lists all backups owned by a backup collection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_backups():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListBackupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_backups(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest, dict]):
                The request object. Request for [ListBackups].
            parent (str):
                Required. The resource name of the backupCollection
                using the form:
                ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}``

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsPager:
                Response for [ListBackups].

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
        if not isinstance(request, cloud_redis_cluster.ListBackupsRequest):
            request = cloud_redis_cluster.ListBackupsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_backups]

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
        response = pagers.ListBackupsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_backup(
        self,
        request: Optional[Union[cloud_redis_cluster.GetBackupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.Backup:
        r"""Gets the details of a specific backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_backup():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetBackupRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_backup(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetBackupRequest, dict]):
                The request object. Request for [GetBackup].
            name (str):
                Required. Redis backup resource name using the form:
                ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``

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
            google.cloud.redis_cluster_v1beta1.types.Backup:
                Backup of a cluster.
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
        if not isinstance(request, cloud_redis_cluster.GetBackupRequest):
            request = cloud_redis_cluster.GetBackupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_backup]

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

    def delete_backup(
        self,
        request: Optional[Union[cloud_redis_cluster.DeleteBackupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a specific backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_delete_backup():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.DeleteBackupRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_backup(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.DeleteBackupRequest, dict]):
                The request object. Request for [DeleteBackup].
            name (str):
                Required. Redis backup resource name using the form:
                ``projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}``

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
        if not isinstance(request, cloud_redis_cluster.DeleteBackupRequest):
            request = cloud_redis_cluster.DeleteBackupRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_backup]

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
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def export_backup(
        self,
        request: Optional[Union[cloud_redis_cluster.ExportBackupRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Exports a specific backup to a customer target Cloud
        Storage URI.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_export_backup():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ExportBackupRequest(
                    gcs_bucket="gcs_bucket_value",
                    name="name_value",
                )

                # Make the request
                operation = client.export_backup(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ExportBackupRequest, dict]):
                The request object. Request for [ExportBackup].
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
                :class:`google.cloud.redis_cluster_v1beta1.types.Backup`
                Backup of a cluster.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloud_redis_cluster.ExportBackupRequest):
            request = cloud_redis_cluster.ExportBackupRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.export_backup]

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
            cloud_redis_cluster.Backup,
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def backup_cluster(
        self,
        request: Optional[Union[cloud_redis_cluster.BackupClusterRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Backup Redis Cluster.
        If this is the first time a backup is being created, a
        backup collection will be created at the backend, and
        this backup belongs to this collection. Both collection
        and backup will have a resource name. Backup will be
        executed for each shard. A replica (primary if nonHA)
        will be selected to perform the execution. Backup call
        will be rejected if there is an ongoing backup or update
        operation. Be aware that during preview, if the
        cluster's internal software version is too old, critical
        update will be performed before actual backup. Once the
        internal software version is updated to the minimum
        version required by the backup feature, subsequent
        backups will not require critical update. After preview,
        there will be no critical update needed for backup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_backup_cluster():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.BackupClusterRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.backup_cluster(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.BackupClusterRequest, dict]):
                The request object. Request for [BackupCluster].
            name (str):
                Required. Redis cluster resource name using the form:
                ``projects/{project_id}/locations/{location_id}/clusters/{cluster_id}``
                where ``location_id`` refers to a GCP region.

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
                :class:`google.cloud.redis_cluster_v1beta1.types.Cluster`
                A cluster instance.

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
        if not isinstance(request, cloud_redis_cluster.BackupClusterRequest):
            request = cloud_redis_cluster.BackupClusterRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.backup_cluster]

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
            cloud_redis_cluster.Cluster,
            metadata_type=any_pb2.Any,
        )

        # Done; return the response.
        return response

    def list_token_auth_users(
        self,
        request: Optional[
            Union[cloud_redis_cluster.ListTokenAuthUsersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTokenAuthUsersPager:
        r"""Lists all the token auth users for a token based auth
        enabled cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_token_auth_users():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListTokenAuthUsersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_token_auth_users(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListTokenAuthUsersRequest, dict]):
                The request object. Request message for [ListTokenAuthUsers][].
            parent (str):
                Required. The parent resource that
                this token based auth user will be
                listed for. Format:

                projects/{project}/locations/{location}/clusters/{cluster}

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListTokenAuthUsersPager:
                Response message for [ListTokenAuthUsers][].

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
        if not isinstance(request, cloud_redis_cluster.ListTokenAuthUsersRequest):
            request = cloud_redis_cluster.ListTokenAuthUsersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_token_auth_users]

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
        response = pagers.ListTokenAuthUsersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_token_auth_user(
        self,
        request: Optional[
            Union[cloud_redis_cluster.GetTokenAuthUserRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.TokenAuthUser:
        r"""Gets a specific token auth user for a basic auth
        enabled cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_token_auth_user():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetTokenAuthUserRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_token_auth_user(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetTokenAuthUserRequest, dict]):
                The request object. Request message for [GetTokenAuthUser][].
            name (str):
                Required. The name of token auth user for a token based
                auth enabled cluster. Format:
                projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}

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
            google.cloud.redis_cluster_v1beta1.types.TokenAuthUser:
                Represents a token based auth user
                for the cluster.

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
        if not isinstance(request, cloud_redis_cluster.GetTokenAuthUserRequest):
            request = cloud_redis_cluster.GetTokenAuthUserRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_token_auth_user]

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

    def list_auth_tokens(
        self,
        request: Optional[
            Union[cloud_redis_cluster.ListAuthTokensRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuthTokensPager:
        r"""Lists all the auth tokens for a specific token auth
        user.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_list_auth_tokens():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.ListAuthTokensRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_auth_tokens(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.ListAuthTokensRequest, dict]):
                The request object. Request message for [ListAuthTokens][].
            parent (str):
                Required. The parent resource that this auth token will
                be listed for. Format:
                projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}

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
            google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListAuthTokensPager:
                Response message for [ListAuthTokens][].

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
        if not isinstance(request, cloud_redis_cluster.ListAuthTokensRequest):
            request = cloud_redis_cluster.ListAuthTokensRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_auth_tokens]

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
        response = pagers.ListAuthTokensPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_auth_token(
        self,
        request: Optional[Union[cloud_redis_cluster.GetAuthTokenRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloud_redis_cluster.AuthToken:
        r"""Gets a specific auth token for a specific token auth
        user.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_get_auth_token():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.GetAuthTokenRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_auth_token(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.GetAuthTokenRequest, dict]):
                The request object. Request message for [GetAuthToken][].
            name (str):
                Required. The name of auth token for a token based auth
                enabled cluster. Format:
                projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}

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
            google.cloud.redis_cluster_v1beta1.types.AuthToken:
                Auth token for the cluster.
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
        if not isinstance(request, cloud_redis_cluster.GetAuthTokenRequest):
            request = cloud_redis_cluster.GetAuthTokenRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_auth_token]

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

    def add_token_auth_user(
        self,
        request: Optional[
            Union[cloud_redis_cluster.AddTokenAuthUserRequest, dict]
        ] = None,
        *,
        cluster: Optional[str] = None,
        token_auth_user: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Adds a token auth user for a token based auth enabled
        cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_add_token_auth_user():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.AddTokenAuthUserRequest(
                    cluster="cluster_value",
                    token_auth_user="token_auth_user_value",
                )

                # Make the request
                operation = client.add_token_auth_user(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.AddTokenAuthUserRequest, dict]):
                The request object. Request message for [AddTokenAuthUser][].
            cluster (str):
                Required. The cluster resource that
                this token auth user will be added for.
                Format:
                projects/{project}/locations/{location}/clusters/{cluster}

                This corresponds to the ``cluster`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            token_auth_user (str):
                Required. The id of the token auth
                user to add.

                This corresponds to the ``token_auth_user`` field
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
                :class:`google.cloud.redis_cluster_v1beta1.types.Cluster`
                A cluster instance.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [cluster, token_auth_user]
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
        if not isinstance(request, cloud_redis_cluster.AddTokenAuthUserRequest):
            request = cloud_redis_cluster.AddTokenAuthUserRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if cluster is not None:
                request.cluster = cluster
            if token_auth_user is not None:
                request.token_auth_user = token_auth_user

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_token_auth_user]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("cluster", request.cluster),)),
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
            cloud_redis_cluster.Cluster,
            metadata_type=cloud_redis_cluster.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_token_auth_user(
        self,
        request: Optional[
            Union[cloud_redis_cluster.DeleteTokenAuthUserRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a token auth user for a token based auth
        enabled cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_delete_token_auth_user():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.DeleteTokenAuthUserRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_token_auth_user(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.DeleteTokenAuthUserRequest, dict]):
                The request object. Request message for [DeleteTokenAuthUser][].
            name (str):
                Required. The name of the token auth user to delete.
                Format:
                projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}

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
        if not isinstance(request, cloud_redis_cluster.DeleteTokenAuthUserRequest):
            request = cloud_redis_cluster.DeleteTokenAuthUserRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_token_auth_user]

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
            metadata_type=cloud_redis_cluster.OperationMetadata,
        )

        # Done; return the response.
        return response

    def add_auth_token(
        self,
        request: Optional[Union[cloud_redis_cluster.AddAuthTokenRequest, dict]] = None,
        *,
        token_auth_user: Optional[str] = None,
        auth_token: Optional[cloud_redis_cluster.AuthToken] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Adds a auth token for a user of a token based auth
        enabled cluster.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_add_auth_token():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.AddAuthTokenRequest(
                    token_auth_user="token_auth_user_value",
                )

                # Make the request
                operation = client.add_auth_token(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.AddAuthTokenRequest, dict]):
                The request object. Request message for [AddAuthToken][].
            token_auth_user (str):
                Required. The name of the token auth user resource that
                this auth token will be added for. Format:
                projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}

                This corresponds to the ``token_auth_user`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            auth_token (google.cloud.redis_cluster_v1beta1.types.AuthToken):
                Required. The auth token to add.
                This corresponds to the ``auth_token`` field
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
                :class:`google.cloud.redis_cluster_v1beta1.types.TokenAuthUser`
                Represents a token based auth user for the cluster.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [token_auth_user, auth_token]
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
        if not isinstance(request, cloud_redis_cluster.AddAuthTokenRequest):
            request = cloud_redis_cluster.AddAuthTokenRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if token_auth_user is not None:
                request.token_auth_user = token_auth_user
            if auth_token is not None:
                request.auth_token = auth_token

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.add_auth_token]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("token_auth_user", request.token_auth_user),)
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
            cloud_redis_cluster.TokenAuthUser,
            metadata_type=cloud_redis_cluster.OperationMetadata,
        )

        # Done; return the response.
        return response

    def delete_auth_token(
        self,
        request: Optional[
            Union[cloud_redis_cluster.DeleteAuthTokenRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Removes a auth token for a user of a token based auth
        enabled instance.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import redis_cluster_v1beta1

            def sample_delete_auth_token():
                # Create a client
                client = redis_cluster_v1beta1.CloudRedisClusterClient()

                # Initialize request argument(s)
                request = redis_cluster_v1beta1.DeleteAuthTokenRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_auth_token(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.redis_cluster_v1beta1.types.DeleteAuthTokenRequest, dict]):
                The request object. Request message for [DeleteAuthToken][].
            name (str):
                Required. The name of the token auth user resource that
                this auth token will be deleted from. Format:
                projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}

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
        if not isinstance(request, cloud_redis_cluster.DeleteAuthTokenRequest):
            request = cloud_redis_cluster.DeleteAuthTokenRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_auth_token]

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
            metadata_type=cloud_redis_cluster.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "CloudRedisClusterClient":
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

__all__ = ("CloudRedisClusterClient",)
