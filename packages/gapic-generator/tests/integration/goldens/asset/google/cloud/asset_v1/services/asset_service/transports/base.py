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

from google.cloud.asset_v1 import gapic_version as package_version
from google.cloud.asset_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)
_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.auth  # type: ignore
import google.api_core
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore
import google.protobuf

from google.cloud.asset_v1.types import asset_service
from google.longrunning import operations_pb2 # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AssetServiceTransport(abc.ABC):
    """Abstract transport class for AssetService."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    DEFAULT_HOST: str = 'cloudasset.googleapis.com'

    def __init__(
            self, *,
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
                 The hostname to connect to (default: 'cloudasset.googleapis.com').
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
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                scopes=scopes,
                                quota_project_id=quota_project_id,
                                default_scopes=self.AUTH_SCOPES,
                            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(scopes=scopes, quota_project_id=quota_project_id, default_scopes=self.AUTH_SCOPES)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
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
            self.export_assets: self._wrap_method(
                self.export_assets,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/ExportAssets",
            ),
            self.list_assets: self._wrap_method(
                self.list_assets,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/ListAssets",
            ),
            self.batch_get_assets_history: self._wrap_method(
                self.batch_get_assets_history,
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
                method_name="google.cloud.asset.v1.AssetService/BatchGetAssetsHistory",
            ),
            self.create_feed: self._wrap_method(
                self.create_feed,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/CreateFeed",
            ),
            self.get_feed: self._wrap_method(
                self.get_feed,
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
                method_name="google.cloud.asset.v1.AssetService/GetFeed",
            ),
            self.list_feeds: self._wrap_method(
                self.list_feeds,
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
                method_name="google.cloud.asset.v1.AssetService/ListFeeds",
            ),
            self.update_feed: self._wrap_method(
                self.update_feed,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/UpdateFeed",
            ),
            self.delete_feed: self._wrap_method(
                self.delete_feed,
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
                method_name="google.cloud.asset.v1.AssetService/DeleteFeed",
            ),
            self.search_all_resources: self._wrap_method(
                self.search_all_resources,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=15.0,
                ),
                default_timeout=15.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/SearchAllResources",
            ),
            self.search_all_iam_policies: self._wrap_method(
                self.search_all_iam_policies,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=15.0,
                ),
                default_timeout=15.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/SearchAllIamPolicies",
            ),
            self.analyze_iam_policy: self._wrap_method(
                self.analyze_iam_policy,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/AnalyzeIamPolicy",
            ),
            self.analyze_iam_policy_longrunning: self._wrap_method(
                self.analyze_iam_policy_longrunning,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/AnalyzeIamPolicyLongrunning",
            ),
            self.analyze_move: self._wrap_method(
                self.analyze_move,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/AnalyzeMove",
            ),
            self.query_assets: self._wrap_method(
                self.query_assets,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/QueryAssets",
            ),
            self.create_saved_query: self._wrap_method(
                self.create_saved_query,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/CreateSavedQuery",
            ),
            self.get_saved_query: self._wrap_method(
                self.get_saved_query,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/GetSavedQuery",
            ),
            self.list_saved_queries: self._wrap_method(
                self.list_saved_queries,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/ListSavedQueries",
            ),
            self.update_saved_query: self._wrap_method(
                self.update_saved_query,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/UpdateSavedQuery",
            ),
            self.delete_saved_query: self._wrap_method(
                self.delete_saved_query,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/DeleteSavedQuery",
            ),
            self.batch_get_effective_iam_policies: self._wrap_method(
                self.batch_get_effective_iam_policies,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/BatchGetEffectiveIamPolicies",
            ),
            self.analyze_org_policies: self._wrap_method(
                self.analyze_org_policies,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/AnalyzeOrgPolicies",
            ),
            self.analyze_org_policy_governed_containers: self._wrap_method(
                self.analyze_org_policy_governed_containers,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/AnalyzeOrgPolicyGovernedContainers",
            ),
            self.analyze_org_policy_governed_assets: self._wrap_method(
                self.analyze_org_policy_governed_assets,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.asset.v1.AssetService/AnalyzeOrgPolicyGovernedAssets",
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
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
    def export_assets(self) -> Callable[
            [asset_service.ExportAssetsRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_assets(self) -> Callable[
            [asset_service.ListAssetsRequest],
            Union[
                asset_service.ListAssetsResponse,
                Awaitable[asset_service.ListAssetsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def batch_get_assets_history(self) -> Callable[
            [asset_service.BatchGetAssetsHistoryRequest],
            Union[
                asset_service.BatchGetAssetsHistoryResponse,
                Awaitable[asset_service.BatchGetAssetsHistoryResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_feed(self) -> Callable[
            [asset_service.CreateFeedRequest],
            Union[
                asset_service.Feed,
                Awaitable[asset_service.Feed]
            ]]:
        raise NotImplementedError()

    @property
    def get_feed(self) -> Callable[
            [asset_service.GetFeedRequest],
            Union[
                asset_service.Feed,
                Awaitable[asset_service.Feed]
            ]]:
        raise NotImplementedError()

    @property
    def list_feeds(self) -> Callable[
            [asset_service.ListFeedsRequest],
            Union[
                asset_service.ListFeedsResponse,
                Awaitable[asset_service.ListFeedsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def update_feed(self) -> Callable[
            [asset_service.UpdateFeedRequest],
            Union[
                asset_service.Feed,
                Awaitable[asset_service.Feed]
            ]]:
        raise NotImplementedError()

    @property
    def delete_feed(self) -> Callable[
            [asset_service.DeleteFeedRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def search_all_resources(self) -> Callable[
            [asset_service.SearchAllResourcesRequest],
            Union[
                asset_service.SearchAllResourcesResponse,
                Awaitable[asset_service.SearchAllResourcesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def search_all_iam_policies(self) -> Callable[
            [asset_service.SearchAllIamPoliciesRequest],
            Union[
                asset_service.SearchAllIamPoliciesResponse,
                Awaitable[asset_service.SearchAllIamPoliciesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_iam_policy(self) -> Callable[
            [asset_service.AnalyzeIamPolicyRequest],
            Union[
                asset_service.AnalyzeIamPolicyResponse,
                Awaitable[asset_service.AnalyzeIamPolicyResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_iam_policy_longrunning(self) -> Callable[
            [asset_service.AnalyzeIamPolicyLongrunningRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_move(self) -> Callable[
            [asset_service.AnalyzeMoveRequest],
            Union[
                asset_service.AnalyzeMoveResponse,
                Awaitable[asset_service.AnalyzeMoveResponse]
            ]]:
        raise NotImplementedError()

    @property
    def query_assets(self) -> Callable[
            [asset_service.QueryAssetsRequest],
            Union[
                asset_service.QueryAssetsResponse,
                Awaitable[asset_service.QueryAssetsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_saved_query(self) -> Callable[
            [asset_service.CreateSavedQueryRequest],
            Union[
                asset_service.SavedQuery,
                Awaitable[asset_service.SavedQuery]
            ]]:
        raise NotImplementedError()

    @property
    def get_saved_query(self) -> Callable[
            [asset_service.GetSavedQueryRequest],
            Union[
                asset_service.SavedQuery,
                Awaitable[asset_service.SavedQuery]
            ]]:
        raise NotImplementedError()

    @property
    def list_saved_queries(self) -> Callable[
            [asset_service.ListSavedQueriesRequest],
            Union[
                asset_service.ListSavedQueriesResponse,
                Awaitable[asset_service.ListSavedQueriesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def update_saved_query(self) -> Callable[
            [asset_service.UpdateSavedQueryRequest],
            Union[
                asset_service.SavedQuery,
                Awaitable[asset_service.SavedQuery]
            ]]:
        raise NotImplementedError()

    @property
    def delete_saved_query(self) -> Callable[
            [asset_service.DeleteSavedQueryRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def batch_get_effective_iam_policies(self) -> Callable[
            [asset_service.BatchGetEffectiveIamPoliciesRequest],
            Union[
                asset_service.BatchGetEffectiveIamPoliciesResponse,
                Awaitable[asset_service.BatchGetEffectiveIamPoliciesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_org_policies(self) -> Callable[
            [asset_service.AnalyzeOrgPoliciesRequest],
            Union[
                asset_service.AnalyzeOrgPoliciesResponse,
                Awaitable[asset_service.AnalyzeOrgPoliciesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_org_policy_governed_containers(self) -> Callable[
            [asset_service.AnalyzeOrgPolicyGovernedContainersRequest],
            Union[
                asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
                Awaitable[asset_service.AnalyzeOrgPolicyGovernedContainersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def analyze_org_policy_governed_assets(self) -> Callable[
            [asset_service.AnalyzeOrgPolicyGovernedAssetsRequest],
            Union[
                asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
                Awaitable[asset_service.AnalyzeOrgPolicyGovernedAssetsResponse]
            ]]:
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'AssetServiceTransport',
)
