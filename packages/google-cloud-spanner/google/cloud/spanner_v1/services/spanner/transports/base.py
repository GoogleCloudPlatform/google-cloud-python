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

from google.cloud.spanner_v1 import gapic_version as package_version
from google.cloud.spanner_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.spanner_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)
from google.cloud.spanner_v1.metrics.metrics_interceptor import MetricsInterceptor

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.spanner_v1.types import (
    commit_response,
    location,
    result_set,
    spanner,
    transaction,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class SpannerTransport(abc.ABC):
    """Abstract transport class for Spanner."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/spanner.data",
    )

    DEFAULT_HOST: str = "spanner.googleapis.com"

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
        metrics_interceptor: Optional[MetricsInterceptor] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'spanner.googleapis.com').
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
            self.create_session: self._wrap_method(
                self.create_session,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/CreateSession",
            ),
            self.batch_create_sessions: self._wrap_method(
                self.batch_create_sessions,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/BatchCreateSessions",
            ),
            self.get_session: self._wrap_method(
                self.get_session,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/GetSession",
            ),
            self.list_sessions: self._wrap_method(
                self.list_sessions,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/ListSessions",
            ),
            self.delete_session: self._wrap_method(
                self.delete_session,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/DeleteSession",
            ),
            self.execute_sql: self._wrap_method(
                self.execute_sql,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/ExecuteSql",
            ),
            self.execute_streaming_sql: self._wrap_method(
                self.execute_streaming_sql,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/ExecuteStreamingSql",
                is_streaming=True,
            ),
            self.execute_batch_dml: self._wrap_method(
                self.execute_batch_dml,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/ExecuteBatchDml",
            ),
            self.read: self._wrap_method(
                self.read,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/Read",
            ),
            self.streaming_read: self._wrap_method(
                self.streaming_read,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/StreamingRead",
                is_streaming=True,
            ),
            self.begin_transaction: self._wrap_method(
                self.begin_transaction,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/BeginTransaction",
            ),
            self.commit: self._wrap_method(
                self.commit,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=3600.0,
                ),
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/Commit",
            ),
            self.rollback: self._wrap_method(
                self.rollback,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/Rollback",
            ),
            self.partition_query: self._wrap_method(
                self.partition_query,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/PartitionQuery",
            ),
            self.partition_read: self._wrap_method(
                self.partition_read,
                default_retry=retries.Retry(
                    initial=0.25,
                    maximum=32.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/PartitionRead",
            ),
            self.batch_write: self._wrap_method(
                self.batch_write,
                default_timeout=3600.0,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/BatchWrite",
                is_streaming=True,
            ),
            self.fetch_cache_update: self._wrap_method(
                self.fetch_cache_update,
                default_timeout=None,
                client_info=client_info,
                method_name="google.spanner.v1.Spanner/FetchCacheUpdate",
                is_streaming=True,
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
    def create_session(
        self,
    ) -> Callable[
        [spanner.CreateSessionRequest],
        Union[spanner.Session, Awaitable[spanner.Session]],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_sessions(
        self,
    ) -> Callable[
        [spanner.BatchCreateSessionsRequest],
        Union[
            spanner.BatchCreateSessionsResponse,
            Awaitable[spanner.BatchCreateSessionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_session(
        self,
    ) -> Callable[
        [spanner.GetSessionRequest], Union[spanner.Session, Awaitable[spanner.Session]]
    ]:
        raise NotImplementedError()

    @property
    def list_sessions(
        self,
    ) -> Callable[
        [spanner.ListSessionsRequest],
        Union[spanner.ListSessionsResponse, Awaitable[spanner.ListSessionsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_session(
        self,
    ) -> Callable[
        [spanner.DeleteSessionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def execute_sql(
        self,
    ) -> Callable[
        [spanner.ExecuteSqlRequest],
        Union[result_set.ResultSet, Awaitable[result_set.ResultSet]],
    ]:
        raise NotImplementedError()

    @property
    def execute_streaming_sql(
        self,
    ) -> Callable[
        [spanner.ExecuteSqlRequest],
        Union[result_set.PartialResultSet, Awaitable[result_set.PartialResultSet]],
    ]:
        raise NotImplementedError()

    @property
    def execute_batch_dml(
        self,
    ) -> Callable[
        [spanner.ExecuteBatchDmlRequest],
        Union[
            spanner.ExecuteBatchDmlResponse, Awaitable[spanner.ExecuteBatchDmlResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def read(
        self,
    ) -> Callable[
        [spanner.ReadRequest],
        Union[result_set.ResultSet, Awaitable[result_set.ResultSet]],
    ]:
        raise NotImplementedError()

    @property
    def streaming_read(
        self,
    ) -> Callable[
        [spanner.ReadRequest],
        Union[result_set.PartialResultSet, Awaitable[result_set.PartialResultSet]],
    ]:
        raise NotImplementedError()

    @property
    def begin_transaction(
        self,
    ) -> Callable[
        [spanner.BeginTransactionRequest],
        Union[transaction.Transaction, Awaitable[transaction.Transaction]],
    ]:
        raise NotImplementedError()

    @property
    def commit(
        self,
    ) -> Callable[
        [spanner.CommitRequest],
        Union[
            commit_response.CommitResponse, Awaitable[commit_response.CommitResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def rollback(
        self,
    ) -> Callable[
        [spanner.RollbackRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def partition_query(
        self,
    ) -> Callable[
        [spanner.PartitionQueryRequest],
        Union[spanner.PartitionResponse, Awaitable[spanner.PartitionResponse]],
    ]:
        raise NotImplementedError()

    @property
    def partition_read(
        self,
    ) -> Callable[
        [spanner.PartitionReadRequest],
        Union[spanner.PartitionResponse, Awaitable[spanner.PartitionResponse]],
    ]:
        raise NotImplementedError()

    @property
    def batch_write(
        self,
    ) -> Callable[
        [spanner.BatchWriteRequest],
        Union[spanner.BatchWriteResponse, Awaitable[spanner.BatchWriteResponse]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_cache_update(
        self,
    ) -> Callable[
        [spanner.FetchCacheUpdateRequest],
        Union[location.CacheUpdate, Awaitable[location.CacheUpdate]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("SpannerTransport",)
