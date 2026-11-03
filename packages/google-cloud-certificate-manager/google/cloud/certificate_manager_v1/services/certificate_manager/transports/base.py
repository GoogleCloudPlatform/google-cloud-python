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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.certificate_manager_v1 import gapic_version as package_version
from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config,
    certificate_manager,
    trust_config,
)
from google.cloud.certificate_manager_v1.types import (
    certificate_issuance_config as gcc_certificate_issuance_config,
)
from google.cloud.certificate_manager_v1.types import trust_config as gcc_trust_config

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class CertificateManagerTransport(abc.ABC):
    """Abstract transport class for CertificateManager."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "certificatemanager.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'certificatemanager.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_certificates: gapic_v1.method.wrap_method(
                self.list_certificates,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_certificate: gapic_v1.method.wrap_method(
                self.get_certificate,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_certificate: gapic_v1.method.wrap_method(
                self.create_certificate,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_certificate: gapic_v1.method.wrap_method(
                self.update_certificate,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_certificate: gapic_v1.method.wrap_method(
                self.delete_certificate,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_certificate_maps: gapic_v1.method.wrap_method(
                self.list_certificate_maps,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_certificate_map: gapic_v1.method.wrap_method(
                self.get_certificate_map,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_certificate_map: gapic_v1.method.wrap_method(
                self.create_certificate_map,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_certificate_map: gapic_v1.method.wrap_method(
                self.update_certificate_map,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_certificate_map: gapic_v1.method.wrap_method(
                self.delete_certificate_map,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_certificate_map_entries: gapic_v1.method.wrap_method(
                self.list_certificate_map_entries,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_certificate_map_entry: gapic_v1.method.wrap_method(
                self.get_certificate_map_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_certificate_map_entry: gapic_v1.method.wrap_method(
                self.create_certificate_map_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_certificate_map_entry: gapic_v1.method.wrap_method(
                self.update_certificate_map_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_certificate_map_entry: gapic_v1.method.wrap_method(
                self.delete_certificate_map_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_dns_authorizations: gapic_v1.method.wrap_method(
                self.list_dns_authorizations,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_dns_authorization: gapic_v1.method.wrap_method(
                self.get_dns_authorization,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_dns_authorization: gapic_v1.method.wrap_method(
                self.create_dns_authorization,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_dns_authorization: gapic_v1.method.wrap_method(
                self.update_dns_authorization,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_dns_authorization: gapic_v1.method.wrap_method(
                self.delete_dns_authorization,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_certificate_issuance_configs: gapic_v1.method.wrap_method(
                self.list_certificate_issuance_configs,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_certificate_issuance_config: gapic_v1.method.wrap_method(
                self.get_certificate_issuance_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_certificate_issuance_config: gapic_v1.method.wrap_method(
                self.create_certificate_issuance_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_certificate_issuance_config: gapic_v1.method.wrap_method(
                self.update_certificate_issuance_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_certificate_issuance_config: gapic_v1.method.wrap_method(
                self.delete_certificate_issuance_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_trust_configs: gapic_v1.method.wrap_method(
                self.list_trust_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_trust_config: gapic_v1.method.wrap_method(
                self.get_trust_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_trust_config: gapic_v1.method.wrap_method(
                self.create_trust_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_trust_config: gapic_v1.method.wrap_method(
                self.update_trust_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_trust_config: gapic_v1.method.wrap_method(
                self.delete_trust_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_certificates(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificatesRequest],
        Union[
            certificate_manager.ListCertificatesResponse,
            Awaitable[certificate_manager.ListCertificatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateRequest],
        Union[
            certificate_manager.Certificate, Awaitable[certificate_manager.Certificate]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_certificate(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_certificate(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_certificate_maps(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificateMapsRequest],
        Union[
            certificate_manager.ListCertificateMapsResponse,
            Awaitable[certificate_manager.ListCertificateMapsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateMapRequest],
        Union[
            certificate_manager.CertificateMap,
            Awaitable[certificate_manager.CertificateMap],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateMapRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateMapRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_certificate_map(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateMapRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_certificate_map_entries(
        self,
    ) -> Callable[
        [certificate_manager.ListCertificateMapEntriesRequest],
        Union[
            certificate_manager.ListCertificateMapEntriesResponse,
            Awaitable[certificate_manager.ListCertificateMapEntriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.GetCertificateMapEntryRequest],
        Union[
            certificate_manager.CertificateMapEntry,
            Awaitable[certificate_manager.CertificateMapEntry],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.CreateCertificateMapEntryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.UpdateCertificateMapEntryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_certificate_map_entry(
        self,
    ) -> Callable[
        [certificate_manager.DeleteCertificateMapEntryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_dns_authorizations(
        self,
    ) -> Callable[
        [certificate_manager.ListDnsAuthorizationsRequest],
        Union[
            certificate_manager.ListDnsAuthorizationsResponse,
            Awaitable[certificate_manager.ListDnsAuthorizationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.GetDnsAuthorizationRequest],
        Union[
            certificate_manager.DnsAuthorization,
            Awaitable[certificate_manager.DnsAuthorization],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.CreateDnsAuthorizationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.UpdateDnsAuthorizationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_dns_authorization(
        self,
    ) -> Callable[
        [certificate_manager.DeleteDnsAuthorizationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_certificate_issuance_configs(
        self,
    ) -> Callable[
        [certificate_issuance_config.ListCertificateIssuanceConfigsRequest],
        Union[
            certificate_issuance_config.ListCertificateIssuanceConfigsResponse,
            Awaitable[
                certificate_issuance_config.ListCertificateIssuanceConfigsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_certificate_issuance_config(
        self,
    ) -> Callable[
        [certificate_issuance_config.GetCertificateIssuanceConfigRequest],
        Union[
            certificate_issuance_config.CertificateIssuanceConfig,
            Awaitable[certificate_issuance_config.CertificateIssuanceConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_certificate_issuance_config(
        self,
    ) -> Callable[
        [gcc_certificate_issuance_config.CreateCertificateIssuanceConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_certificate_issuance_config(
        self,
    ) -> Callable[
        [gcc_certificate_issuance_config.UpdateCertificateIssuanceConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_certificate_issuance_config(
        self,
    ) -> Callable[
        [certificate_issuance_config.DeleteCertificateIssuanceConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_trust_configs(
        self,
    ) -> Callable[
        [trust_config.ListTrustConfigsRequest],
        Union[
            trust_config.ListTrustConfigsResponse,
            Awaitable[trust_config.ListTrustConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_trust_config(
        self,
    ) -> Callable[
        [trust_config.GetTrustConfigRequest],
        Union[trust_config.TrustConfig, Awaitable[trust_config.TrustConfig]],
    ]:
        raise NotImplementedError()

    @property
    def create_trust_config(
        self,
    ) -> Callable[
        [gcc_trust_config.CreateTrustConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_trust_config(
        self,
    ) -> Callable[
        [gcc_trust_config.UpdateTrustConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_trust_config(
        self,
    ) -> Callable[
        [trust_config.DeleteTrustConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("CertificateManagerTransport",)
