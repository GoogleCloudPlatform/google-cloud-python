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

from google.cloud.servicemanagement_v1 import gapic_version as package_version
from google.cloud.servicemanagement_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.servicemanagement_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api.service_pb2 as service_pb2  # type: ignore
import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.servicemanagement_v1.types import resources, servicemanager

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ServiceManagerTransport(abc.ABC):
    """Abstract transport class for ServiceManager."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
        "https://www.googleapis.com/auth/service.management",
        "https://www.googleapis.com/auth/service.management.readonly",
    )

    DEFAULT_HOST: str = "servicemanagement.googleapis.com"

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
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'servicemanagement.googleapis.com').
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
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
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

        self._client_options = client_options
        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _wrap_method(self, func, *args, **kwargs):
        """Wrap an RPC method with common client-level features.

        Applies retry, timeout, metadata, and tracing wrappers to the
        underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method.wrap_method(func, *args, **kwargs)

    def _wrap_async_method(self, func, *args, **kwargs):
        """Wrap an async RPC method with common client-level features.

        Applies asynchronous retry, timeout, metadata, and tracing wrappers
        to the underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _ASYNC_WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method_async.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _ASYNC_WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for RPC dispatch."""
        self._wrapped_methods = {
            self.list_services: self._wrap_method(
                self.list_services,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/ListServices",
            ),
            self.get_service: self._wrap_method(
                self.get_service,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/GetService",
            ),
            self.create_service: self._wrap_method(
                self.create_service,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/CreateService",
            ),
            self.delete_service: self._wrap_method(
                self.delete_service,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/DeleteService",
            ),
            self.undelete_service: self._wrap_method(
                self.undelete_service,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/UndeleteService",
            ),
            self.list_service_configs: self._wrap_method(
                self.list_service_configs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/ListServiceConfigs",
            ),
            self.get_service_config: self._wrap_method(
                self.get_service_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/GetServiceConfig",
            ),
            self.create_service_config: self._wrap_method(
                self.create_service_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/CreateServiceConfig",
            ),
            self.submit_config_source: self._wrap_method(
                self.submit_config_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/SubmitConfigSource",
            ),
            self.list_service_rollouts: self._wrap_method(
                self.list_service_rollouts,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/ListServiceRollouts",
            ),
            self.get_service_rollout: self._wrap_method(
                self.get_service_rollout,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/GetServiceRollout",
            ),
            self.create_service_rollout: self._wrap_method(
                self.create_service_rollout,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/CreateServiceRollout",
            ),
            self.generate_config_report: self._wrap_method(
                self.generate_config_report,
                default_timeout=None,
                client_info=client_info,
                method_name="google.api.servicemanagement.v1.ServiceManager/GenerateConfigReport",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/GetIamPolicy",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/SetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/TestIamPermissions",
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
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
    def list_services(
        self,
    ) -> Callable[
        [servicemanager.ListServicesRequest],
        Union[
            servicemanager.ListServicesResponse,
            Awaitable[servicemanager.ListServicesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service(
        self,
    ) -> Callable[
        [servicemanager.GetServiceRequest],
        Union[resources.ManagedService, Awaitable[resources.ManagedService]],
    ]:
        raise NotImplementedError()

    @property
    def create_service(
        self,
    ) -> Callable[
        [servicemanager.CreateServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service(
        self,
    ) -> Callable[
        [servicemanager.DeleteServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def undelete_service(
        self,
    ) -> Callable[
        [servicemanager.UndeleteServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_service_configs(
        self,
    ) -> Callable[
        [servicemanager.ListServiceConfigsRequest],
        Union[
            servicemanager.ListServiceConfigsResponse,
            Awaitable[servicemanager.ListServiceConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service_config(
        self,
    ) -> Callable[
        [servicemanager.GetServiceConfigRequest],
        Union[service_pb2.Service, Awaitable[service_pb2.Service]],
    ]:
        raise NotImplementedError()

    @property
    def create_service_config(
        self,
    ) -> Callable[
        [servicemanager.CreateServiceConfigRequest],
        Union[service_pb2.Service, Awaitable[service_pb2.Service]],
    ]:
        raise NotImplementedError()

    @property
    def submit_config_source(
        self,
    ) -> Callable[
        [servicemanager.SubmitConfigSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_service_rollouts(
        self,
    ) -> Callable[
        [servicemanager.ListServiceRolloutsRequest],
        Union[
            servicemanager.ListServiceRolloutsResponse,
            Awaitable[servicemanager.ListServiceRolloutsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service_rollout(
        self,
    ) -> Callable[
        [servicemanager.GetServiceRolloutRequest],
        Union[resources.Rollout, Awaitable[resources.Rollout]],
    ]:
        raise NotImplementedError()

    @property
    def create_service_rollout(
        self,
    ) -> Callable[
        [servicemanager.CreateServiceRolloutRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_config_report(
        self,
    ) -> Callable[
        [servicemanager.GenerateConfigReportRequest],
        Union[
            servicemanager.GenerateConfigReportResponse,
            Awaitable[servicemanager.GenerateConfigReportResponse],
        ],
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
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ServiceManagerTransport",)
