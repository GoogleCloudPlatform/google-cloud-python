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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.servicedirectory_v1 import gapic_version as package_version
from google.cloud.servicedirectory_v1.types import (
    endpoint,
    namespace,
    registration_service,
    service,
)
from google.cloud.servicedirectory_v1.types import endpoint as gcs_endpoint
from google.cloud.servicedirectory_v1.types import namespace as gcs_namespace
from google.cloud.servicedirectory_v1.types import service as gcs_service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class RegistrationServiceTransport(abc.ABC):
    """Abstract transport class for RegistrationService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "servicedirectory.googleapis.com"

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
                 The hostname to connect to (default: 'servicedirectory.googleapis.com').
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
            self.create_namespace: gapic_v1.method.wrap_method(
                self.create_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_namespaces: gapic_v1.method.wrap_method(
                self.list_namespaces,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_namespace: gapic_v1.method.wrap_method(
                self.get_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_namespace: gapic_v1.method.wrap_method(
                self.update_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_namespace: gapic_v1.method.wrap_method(
                self.delete_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_service: gapic_v1.method.wrap_method(
                self.create_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_services: gapic_v1.method.wrap_method(
                self.list_services,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_service: gapic_v1.method.wrap_method(
                self.get_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_service: gapic_v1.method.wrap_method(
                self.update_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_service: gapic_v1.method.wrap_method(
                self.delete_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_endpoint: gapic_v1.method.wrap_method(
                self.create_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_endpoints: gapic_v1.method.wrap_method(
                self.list_endpoints,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_endpoint: gapic_v1.method.wrap_method(
                self.get_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_endpoint: gapic_v1.method.wrap_method(
                self.update_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_endpoint: gapic_v1.method.wrap_method(
                self.delete_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
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
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def create_namespace(
        self,
    ) -> Callable[
        [registration_service.CreateNamespaceRequest],
        Union[gcs_namespace.Namespace, Awaitable[gcs_namespace.Namespace]],
    ]:
        raise NotImplementedError()

    @property
    def list_namespaces(
        self,
    ) -> Callable[
        [registration_service.ListNamespacesRequest],
        Union[
            registration_service.ListNamespacesResponse,
            Awaitable[registration_service.ListNamespacesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_namespace(
        self,
    ) -> Callable[
        [registration_service.GetNamespaceRequest],
        Union[namespace.Namespace, Awaitable[namespace.Namespace]],
    ]:
        raise NotImplementedError()

    @property
    def update_namespace(
        self,
    ) -> Callable[
        [registration_service.UpdateNamespaceRequest],
        Union[gcs_namespace.Namespace, Awaitable[gcs_namespace.Namespace]],
    ]:
        raise NotImplementedError()

    @property
    def delete_namespace(
        self,
    ) -> Callable[
        [registration_service.DeleteNamespaceRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_service(
        self,
    ) -> Callable[
        [registration_service.CreateServiceRequest],
        Union[gcs_service.Service, Awaitable[gcs_service.Service]],
    ]:
        raise NotImplementedError()

    @property
    def list_services(
        self,
    ) -> Callable[
        [registration_service.ListServicesRequest],
        Union[
            registration_service.ListServicesResponse,
            Awaitable[registration_service.ListServicesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service(
        self,
    ) -> Callable[
        [registration_service.GetServiceRequest],
        Union[service.Service, Awaitable[service.Service]],
    ]:
        raise NotImplementedError()

    @property
    def update_service(
        self,
    ) -> Callable[
        [registration_service.UpdateServiceRequest],
        Union[gcs_service.Service, Awaitable[gcs_service.Service]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service(
        self,
    ) -> Callable[
        [registration_service.DeleteServiceRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_endpoint(
        self,
    ) -> Callable[
        [registration_service.CreateEndpointRequest],
        Union[gcs_endpoint.Endpoint, Awaitable[gcs_endpoint.Endpoint]],
    ]:
        raise NotImplementedError()

    @property
    def list_endpoints(
        self,
    ) -> Callable[
        [registration_service.ListEndpointsRequest],
        Union[
            registration_service.ListEndpointsResponse,
            Awaitable[registration_service.ListEndpointsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_endpoint(
        self,
    ) -> Callable[
        [registration_service.GetEndpointRequest],
        Union[endpoint.Endpoint, Awaitable[endpoint.Endpoint]],
    ]:
        raise NotImplementedError()

    @property
    def update_endpoint(
        self,
    ) -> Callable[
        [registration_service.UpdateEndpointRequest],
        Union[gcs_endpoint.Endpoint, Awaitable[gcs_endpoint.Endpoint]],
    ]:
        raise NotImplementedError()

    @property
    def delete_endpoint(
        self,
    ) -> Callable[
        [registration_service.DeleteEndpointRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
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


__all__ = ("RegistrationServiceTransport",)
