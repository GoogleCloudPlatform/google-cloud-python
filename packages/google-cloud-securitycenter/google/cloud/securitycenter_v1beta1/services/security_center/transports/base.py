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

from google.cloud.securitycenter_v1beta1 import gapic_version as package_version
from google.cloud.securitycenter_v1beta1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.securitycenter_v1beta1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.securitycenter_v1beta1.types import (
    finding,
    organization_settings,
    securitycenter_service,
    source,
)
from google.cloud.securitycenter_v1beta1.types import finding as gcs_finding
from google.cloud.securitycenter_v1beta1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1beta1.types import (
    security_marks as gcs_security_marks,
)
from google.cloud.securitycenter_v1beta1.types import source as gcs_source

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class SecurityCenterTransport(abc.ABC):
    """Abstract transport class for SecurityCenter."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "securitycenter.googleapis.com"

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
                 The hostname to connect to (default: 'securitycenter.googleapis.com').
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
            self.create_source: self._wrap_method(
                self.create_source,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/CreateSource",
            ),
            self.create_finding: self._wrap_method(
                self.create_finding,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/CreateFinding",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
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
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/GetIamPolicy",
            ),
            self.get_organization_settings: self._wrap_method(
                self.get_organization_settings,
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
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/GetOrganizationSettings",
            ),
            self.get_source: self._wrap_method(
                self.get_source,
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
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/GetSource",
            ),
            self.group_assets: self._wrap_method(
                self.group_assets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/GroupAssets",
            ),
            self.group_findings: self._wrap_method(
                self.group_findings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/GroupFindings",
            ),
            self.list_assets: self._wrap_method(
                self.list_assets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/ListAssets",
            ),
            self.list_findings: self._wrap_method(
                self.list_findings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=480.0,
                ),
                default_timeout=480.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/ListFindings",
            ),
            self.list_sources: self._wrap_method(
                self.list_sources,
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
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/ListSources",
            ),
            self.run_asset_discovery: self._wrap_method(
                self.run_asset_discovery,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/RunAssetDiscovery",
            ),
            self.set_finding_state: self._wrap_method(
                self.set_finding_state,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/SetFindingState",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/SetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
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
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/TestIamPermissions",
            ),
            self.update_finding: self._wrap_method(
                self.update_finding,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateFinding",
            ),
            self.update_organization_settings: self._wrap_method(
                self.update_organization_settings,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateOrganizationSettings",
            ),
            self.update_source: self._wrap_method(
                self.update_source,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateSource",
            ),
            self.update_security_marks: self._wrap_method(
                self.update_security_marks,
                default_timeout=480.0,
                client_info=client_info,
                method_name="google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateSecurityMarks",
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
    def create_source(
        self,
    ) -> Callable[
        [securitycenter_service.CreateSourceRequest],
        Union[gcs_source.Source, Awaitable[gcs_source.Source]],
    ]:
        raise NotImplementedError()

    @property
    def create_finding(
        self,
    ) -> Callable[
        [securitycenter_service.CreateFindingRequest],
        Union[gcs_finding.Finding, Awaitable[gcs_finding.Finding]],
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
    def get_organization_settings(
        self,
    ) -> Callable[
        [securitycenter_service.GetOrganizationSettingsRequest],
        Union[
            organization_settings.OrganizationSettings,
            Awaitable[organization_settings.OrganizationSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_source(
        self,
    ) -> Callable[
        [securitycenter_service.GetSourceRequest],
        Union[source.Source, Awaitable[source.Source]],
    ]:
        raise NotImplementedError()

    @property
    def group_assets(
        self,
    ) -> Callable[
        [securitycenter_service.GroupAssetsRequest],
        Union[
            securitycenter_service.GroupAssetsResponse,
            Awaitable[securitycenter_service.GroupAssetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def group_findings(
        self,
    ) -> Callable[
        [securitycenter_service.GroupFindingsRequest],
        Union[
            securitycenter_service.GroupFindingsResponse,
            Awaitable[securitycenter_service.GroupFindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_assets(
        self,
    ) -> Callable[
        [securitycenter_service.ListAssetsRequest],
        Union[
            securitycenter_service.ListAssetsResponse,
            Awaitable[securitycenter_service.ListAssetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_findings(
        self,
    ) -> Callable[
        [securitycenter_service.ListFindingsRequest],
        Union[
            securitycenter_service.ListFindingsResponse,
            Awaitable[securitycenter_service.ListFindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_sources(
        self,
    ) -> Callable[
        [securitycenter_service.ListSourcesRequest],
        Union[
            securitycenter_service.ListSourcesResponse,
            Awaitable[securitycenter_service.ListSourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def run_asset_discovery(
        self,
    ) -> Callable[
        [securitycenter_service.RunAssetDiscoveryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_finding_state(
        self,
    ) -> Callable[
        [securitycenter_service.SetFindingStateRequest],
        Union[finding.Finding, Awaitable[finding.Finding]],
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
    def update_finding(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateFindingRequest],
        Union[gcs_finding.Finding, Awaitable[gcs_finding.Finding]],
    ]:
        raise NotImplementedError()

    @property
    def update_organization_settings(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateOrganizationSettingsRequest],
        Union[
            gcs_organization_settings.OrganizationSettings,
            Awaitable[gcs_organization_settings.OrganizationSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_source(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSourceRequest],
        Union[gcs_source.Source, Awaitable[gcs_source.Source]],
    ]:
        raise NotImplementedError()

    @property
    def update_security_marks(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSecurityMarksRequest],
        Union[
            gcs_security_marks.SecurityMarks,
            Awaitable[gcs_security_marks.SecurityMarks],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("SecurityCenterTransport",)
