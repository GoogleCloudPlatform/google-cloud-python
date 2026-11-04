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

from google.cloud.iam_admin_v1 import gapic_version as package_version
from google.cloud.iam_admin_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.iam_admin_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.iam_admin_v1.types import iam

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class IAMTransport(abc.ABC):
    """Abstract transport class for IAM."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "iam.googleapis.com"

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
                 The hostname to connect to (default: 'iam.googleapis.com').
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
            self.list_service_accounts: self._wrap_method(
                self.list_service_accounts,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/ListServiceAccounts",
            ),
            self.get_service_account: self._wrap_method(
                self.get_service_account,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/GetServiceAccount",
            ),
            self.create_service_account: self._wrap_method(
                self.create_service_account,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/CreateServiceAccount",
            ),
            self.update_service_account: self._wrap_method(
                self.update_service_account,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/UpdateServiceAccount",
            ),
            self.patch_service_account: self._wrap_method(
                self.patch_service_account,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/PatchServiceAccount",
            ),
            self.delete_service_account: self._wrap_method(
                self.delete_service_account,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/DeleteServiceAccount",
            ),
            self.undelete_service_account: self._wrap_method(
                self.undelete_service_account,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/UndeleteServiceAccount",
            ),
            self.enable_service_account: self._wrap_method(
                self.enable_service_account,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/EnableServiceAccount",
            ),
            self.disable_service_account: self._wrap_method(
                self.disable_service_account,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/DisableServiceAccount",
            ),
            self.list_service_account_keys: self._wrap_method(
                self.list_service_account_keys,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/ListServiceAccountKeys",
            ),
            self.get_service_account_key: self._wrap_method(
                self.get_service_account_key,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/GetServiceAccountKey",
            ),
            self.create_service_account_key: self._wrap_method(
                self.create_service_account_key,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/CreateServiceAccountKey",
            ),
            self.upload_service_account_key: self._wrap_method(
                self.upload_service_account_key,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/UploadServiceAccountKey",
            ),
            self.delete_service_account_key: self._wrap_method(
                self.delete_service_account_key,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/DeleteServiceAccountKey",
            ),
            self.disable_service_account_key: self._wrap_method(
                self.disable_service_account_key,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/DisableServiceAccountKey",
            ),
            self.enable_service_account_key: self._wrap_method(
                self.enable_service_account_key,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/EnableServiceAccountKey",
            ),
            self.sign_blob: self._wrap_method(
                self.sign_blob,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/SignBlob",
            ),
            self.sign_jwt: self._wrap_method(
                self.sign_jwt,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/SignJwt",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/GetIamPolicy",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/SetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/TestIamPermissions",
            ),
            self.query_grantable_roles: self._wrap_method(
                self.query_grantable_roles,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/QueryGrantableRoles",
            ),
            self.list_roles: self._wrap_method(
                self.list_roles,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/ListRoles",
            ),
            self.get_role: self._wrap_method(
                self.get_role,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/GetRole",
            ),
            self.create_role: self._wrap_method(
                self.create_role,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/CreateRole",
            ),
            self.update_role: self._wrap_method(
                self.update_role,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/UpdateRole",
            ),
            self.delete_role: self._wrap_method(
                self.delete_role,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/DeleteRole",
            ),
            self.undelete_role: self._wrap_method(
                self.undelete_role,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/UndeleteRole",
            ),
            self.query_testable_permissions: self._wrap_method(
                self.query_testable_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/QueryTestablePermissions",
            ),
            self.query_auditable_services: self._wrap_method(
                self.query_auditable_services,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/QueryAuditableServices",
            ),
            self.lint_policy: self._wrap_method(
                self.lint_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.admin.v1.IAM/LintPolicy",
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
    def list_service_accounts(
        self,
    ) -> Callable[
        [iam.ListServiceAccountsRequest],
        Union[
            iam.ListServiceAccountsResponse, Awaitable[iam.ListServiceAccountsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service_account(
        self,
    ) -> Callable[
        [iam.GetServiceAccountRequest],
        Union[iam.ServiceAccount, Awaitable[iam.ServiceAccount]],
    ]:
        raise NotImplementedError()

    @property
    def create_service_account(
        self,
    ) -> Callable[
        [iam.CreateServiceAccountRequest],
        Union[iam.ServiceAccount, Awaitable[iam.ServiceAccount]],
    ]:
        raise NotImplementedError()

    @property
    def update_service_account(
        self,
    ) -> Callable[
        [iam.ServiceAccount], Union[iam.ServiceAccount, Awaitable[iam.ServiceAccount]]
    ]:
        raise NotImplementedError()

    @property
    def patch_service_account(
        self,
    ) -> Callable[
        [iam.PatchServiceAccountRequest],
        Union[iam.ServiceAccount, Awaitable[iam.ServiceAccount]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service_account(
        self,
    ) -> Callable[
        [iam.DeleteServiceAccountRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def undelete_service_account(
        self,
    ) -> Callable[
        [iam.UndeleteServiceAccountRequest],
        Union[
            iam.UndeleteServiceAccountResponse,
            Awaitable[iam.UndeleteServiceAccountResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def enable_service_account(
        self,
    ) -> Callable[
        [iam.EnableServiceAccountRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def disable_service_account(
        self,
    ) -> Callable[
        [iam.DisableServiceAccountRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_service_account_keys(
        self,
    ) -> Callable[
        [iam.ListServiceAccountKeysRequest],
        Union[
            iam.ListServiceAccountKeysResponse,
            Awaitable[iam.ListServiceAccountKeysResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service_account_key(
        self,
    ) -> Callable[
        [iam.GetServiceAccountKeyRequest],
        Union[iam.ServiceAccountKey, Awaitable[iam.ServiceAccountKey]],
    ]:
        raise NotImplementedError()

    @property
    def create_service_account_key(
        self,
    ) -> Callable[
        [iam.CreateServiceAccountKeyRequest],
        Union[iam.ServiceAccountKey, Awaitable[iam.ServiceAccountKey]],
    ]:
        raise NotImplementedError()

    @property
    def upload_service_account_key(
        self,
    ) -> Callable[
        [iam.UploadServiceAccountKeyRequest],
        Union[iam.ServiceAccountKey, Awaitable[iam.ServiceAccountKey]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service_account_key(
        self,
    ) -> Callable[
        [iam.DeleteServiceAccountKeyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def disable_service_account_key(
        self,
    ) -> Callable[
        [iam.DisableServiceAccountKeyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def enable_service_account_key(
        self,
    ) -> Callable[
        [iam.EnableServiceAccountKeyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def sign_blob(
        self,
    ) -> Callable[
        [iam.SignBlobRequest],
        Union[iam.SignBlobResponse, Awaitable[iam.SignBlobResponse]],
    ]:
        raise NotImplementedError()

    @property
    def sign_jwt(
        self,
    ) -> Callable[
        [iam.SignJwtRequest], Union[iam.SignJwtResponse, Awaitable[iam.SignJwtResponse]]
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
    def query_grantable_roles(
        self,
    ) -> Callable[
        [iam.QueryGrantableRolesRequest],
        Union[
            iam.QueryGrantableRolesResponse, Awaitable[iam.QueryGrantableRolesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_roles(
        self,
    ) -> Callable[
        [iam.ListRolesRequest],
        Union[iam.ListRolesResponse, Awaitable[iam.ListRolesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_role(
        self,
    ) -> Callable[[iam.GetRoleRequest], Union[iam.Role, Awaitable[iam.Role]]]:
        raise NotImplementedError()

    @property
    def create_role(
        self,
    ) -> Callable[[iam.CreateRoleRequest], Union[iam.Role, Awaitable[iam.Role]]]:
        raise NotImplementedError()

    @property
    def update_role(
        self,
    ) -> Callable[[iam.UpdateRoleRequest], Union[iam.Role, Awaitable[iam.Role]]]:
        raise NotImplementedError()

    @property
    def delete_role(
        self,
    ) -> Callable[[iam.DeleteRoleRequest], Union[iam.Role, Awaitable[iam.Role]]]:
        raise NotImplementedError()

    @property
    def undelete_role(
        self,
    ) -> Callable[[iam.UndeleteRoleRequest], Union[iam.Role, Awaitable[iam.Role]]]:
        raise NotImplementedError()

    @property
    def query_testable_permissions(
        self,
    ) -> Callable[
        [iam.QueryTestablePermissionsRequest],
        Union[
            iam.QueryTestablePermissionsResponse,
            Awaitable[iam.QueryTestablePermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def query_auditable_services(
        self,
    ) -> Callable[
        [iam.QueryAuditableServicesRequest],
        Union[
            iam.QueryAuditableServicesResponse,
            Awaitable[iam.QueryAuditableServicesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def lint_policy(
        self,
    ) -> Callable[
        [iam.LintPolicyRequest],
        Union[iam.LintPolicyResponse, Awaitable[iam.LintPolicyResponse]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("IAMTransport",)
