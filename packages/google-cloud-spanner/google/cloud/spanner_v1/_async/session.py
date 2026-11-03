# Copyright 2016 Google LLC All rights reserved.
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

"""Wrapper for Cloud Spanner Session objects."""

__CROSS_SYNC_OUTPUT__ = "google.cloud.spanner_v1.session"
import time
from datetime import datetime, timezone
from functools import total_ordering
from typing import MutableMapping, Optional

from google.api_core.exceptions import Aborted, GoogleAPICallError, NotFound
from google.api_core.gapic_v1 import method

from google.cloud.aio._cross_sync import CrossSync
from google.cloud.spanner_v1._async._helpers import _delay_until_retry
from google.cloud.spanner_v1._async.batch import Batch
from google.cloud.spanner_v1._async.snapshot import Snapshot
from google.cloud.spanner_v1._async.transaction import Transaction
from google.cloud.spanner_v1._helpers import (
    _get_retry_delay,
    _metadata_with_leader_aware_routing,
    _metadata_with_prefix,
    _resource_info_from_database,
)
from google.cloud.spanner_v1._opentelemetry_tracing import (
    add_span_event,
    get_current_span,
    trace_call,
)
from google.cloud.spanner_v1.metrics.metrics_capture import MetricsCapture
from google.cloud.spanner_v1.types.spanner import (
    CreateSessionRequest,
    ExecuteSqlRequest,
)

DEFAULT_RETRY_TIMEOUT_SECS = 30
"""Default timeout used by :meth:`Session.run_in_transaction`."""


@total_ordering
@CrossSync.convert_class(
    docstring_format_vars={
        "experimental_api": (
            "\n\n    .. warning::\n        The Spanner AsyncIO API is experimental and may be subject to breaking changes.\n",
            "",
        )
    }
)
class Session(object):
    """{experimental_api}Representation of a Cloud Spanner Session.

    We can use a :class:`Session` to:

    * :meth:`create` the session
    * Use :meth:`exists` to check for the existence of the session
    * :meth:`drop` the session

    :type database: :class:`~google.cloud.spanner_v1.database.Database`
    :param database: The database to which the session is bound.

    :type labels: dict (str -> str)
    :param labels: (Optional) User-assigned labels for the session.

    :type database_role: str
    :param database_role: (Optional) user-assigned database_role for the session.

    :type is_multiplexed: bool
    :param is_multiplexed: (Optional) whether this session is a multiplexed session.
    """

    def __init__(self, database, labels=None, database_role=None, is_multiplexed=False):
        self._database = database
        self._session_id: Optional[str] = None

        if labels is None:
            labels = {}

        self._labels: MutableMapping[str, str] = labels
        self._database_role: Optional[str] = database_role
        self._is_multiplexed: bool = is_multiplexed
        self._last_use_time: datetime = datetime.now(timezone.utc)

    @property
    def _resource_info(self):
        """Resource information for metrics labels."""
        return _resource_info_from_database(self._database)

    def __lt__(self, other):
        return self._session_id < other._session_id

    @property
    def session_id(self):
        """Read-only ID, set by the back-end during :meth:`create`."""
        return self._session_id

    @property
    def is_multiplexed(self):
        """Whether this session is a multiplexed session.

        :rtype: bool
        :returns: True if this is a multiplexed session, False otherwise.
        """
        return self._is_multiplexed

    @property
    def last_use_time(self):
        """Approximate last use time of this session

        :rtype: datetime
        :returns: the approximate last use time of this session"""
        return self._last_use_time

    @property
    def database_role(self):
        """User-assigned database-role for the session.

        :rtype: str
        :returns: the database role str (None if no database role were assigned)."""
        return self._database_role

    @property
    def labels(self):
        """User-assigned labels for the session.

        :rtype: dict (str -> str)
        :returns: the labels dict (empty if no labels were assigned.
        """
        return self._labels

    @property
    def name(self):
        """Session name used in requests.

        .. note::

          This property will not change if ``session_id`` does not, but the
          return value is not cached.

        The session name is of the form

            ``"projects/../instances/../databases/../sessions/{session_id}"``

        :rtype: str
        :returns: The session name.
        :raises ValueError: if session is not yet created
        """
        if self._session_id is None:
            raise ValueError("No session ID set by back-end")
        return self._database.name + "/sessions/" + self._session_id

    @CrossSync.convert
    async def create(self):
        """Create this session, bound to its database.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.CreateSession

        :raises ValueError: if :attr:`session_id` is already set.
        """
        current_span = get_current_span()
        add_span_event(current_span, "Creating Session")

        if self._session_id is not None:
            raise ValueError("Session ID already set by back-end")

        database = self._database
        api = database.spanner_api

        metadata = _metadata_with_prefix(database.name)
        if database._route_to_leader_enabled:
            metadata.append(
                _metadata_with_leader_aware_routing(database._route_to_leader_enabled)
            )

        create_session_request = CreateSessionRequest(database=database.name)
        if database.database_role is not None:
            create_session_request.session.creator_role = database.database_role

        if self._labels:
            create_session_request.session.labels = self._labels

        # Set the multiplexed field for multiplexed sessions
        if self._is_multiplexed:
            create_session_request.session.multiplexed = True

        observability_options = getattr(database, "observability_options", None)
        span_name = (
            "CloudSpanner.CreateMultiplexedSession"
            if self._is_multiplexed
            else "CloudSpanner.CreateSession"
        )
        nth_request = database._next_nth_request
        with (
            trace_call(
                span_name,
                self,
                self._labels,
                observability_options=observability_options,
                metadata=metadata,
            ) as span,
            MetricsCapture(self._resource_info),
        ):
            call_metadata, error_augmenter = database.with_error_augmentation(
                nth_request, 1, metadata, span
            )
            with error_augmenter:
                session_pb = await api.create_session(
                    request=create_session_request,
                    metadata=call_metadata,
                )
        self._session_id = session_pb.name.split("/")[-1]

    @CrossSync.convert
    async def exists(self):
        """Test for the existence of this session.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.GetSession

        :rtype: bool
        :returns: True if the session exists on the back-end, else False.
        """
        current_span = get_current_span()
        if self._session_id is None:
            add_span_event(
                current_span,
                "Checking session existence: Session does not exist as it has not been created yet",
            )
            return False

        add_span_event(
            current_span, "Checking if Session exists", {"session.id": self._session_id}
        )

        database = self._database
        api = database.spanner_api
        metadata = _metadata_with_prefix(self._database.name)
        if self._database._route_to_leader_enabled:
            metadata.append(
                _metadata_with_leader_aware_routing(
                    self._database._route_to_leader_enabled
                )
            )

        observability_options = getattr(self._database, "observability_options", None)
        nth_request = database._next_nth_request
        with (
            trace_call(
                "CloudSpanner.GetSession",
                self,
                observability_options=observability_options,
                metadata=metadata,
            ) as span,
            MetricsCapture(self._resource_info),
        ):
            call_metadata, error_augmenter = database.with_error_augmentation(
                nth_request, 1, metadata, span
            )
            with error_augmenter:
                try:
                    await api.get_session(
                        name=self.name,
                        metadata=call_metadata,
                    )
                    span.set_attribute("session_found", True)
                except NotFound:
                    span.set_attribute("session_found", False)
                    return False

        return True

    @CrossSync.convert
    async def delete(self):
        """Delete this session.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.GetSession

        :raises ValueError: if :attr:`session_id` is not already set.
        :raises NotFound: if the session does not exist
        """
        current_span = get_current_span()
        if self._session_id is None:
            add_span_event(
                current_span, "Deleting Session failed due to unset session_id"
            )
            raise ValueError("Session ID not set by back-end")
        if self._is_multiplexed:
            add_span_event(
                current_span,
                "Skipped deleting Multiplexed Session",
                {"session.id": self._session_id},
            )
            return
        add_span_event(
            current_span, "Deleting Session", {"session.id": self._session_id}
        )

        database = self._database
        api = database.spanner_api
        metadata = _metadata_with_prefix(database.name)
        observability_options = getattr(self._database, "observability_options", None)
        nth_request = database._next_nth_request
        with (
            trace_call(
                "CloudSpanner.DeleteSession",
                self,
                extra_attributes={
                    "session.id": self._session_id,
                    "session.name": self.name,
                },
                observability_options=observability_options,
                metadata=metadata,
            ) as span,
            MetricsCapture(self._resource_info),
        ):
            call_metadata, error_augmenter = database.with_error_augmentation(
                nth_request, 1, metadata, span
            )
            with error_augmenter:
                await api.delete_session(
                    name=self.name,
                    metadata=call_metadata,
                )

    @CrossSync.convert
    async def ping(self):
        """Ping the session to keep it alive by executing "SELECT 1".

        :raises ValueError: if :attr:`session_id` is not already set.
        """
        if self._session_id is None:
            raise ValueError("Session ID not set by back-end")

        database = self._database
        api = database.spanner_api
        metadata = _metadata_with_prefix(database.name)
        nth_request = database._next_nth_request

        with (
            trace_call("CloudSpanner.Session.ping", self) as span,
            MetricsCapture(self._resource_info),
        ):
            call_metadata, error_augmenter = database.with_error_augmentation(
                nth_request, 1, metadata, span
            )
            with error_augmenter:
                request = ExecuteSqlRequest(session=self.name, sql="SELECT 1")
                await api.execute_sql(
                    request=request,
                    metadata=call_metadata,
                )

    def snapshot(self, **kw):
        """Create a snapshot to perform a set of reads with shared staleness.

        See
        https://cloud.google.com/spanner/reference/rpc/google.spanner.v1#google.spanner.v1.TransactionOptions.ReadOnly

        :type kw: dict
        :param kw: Passed through to
                   :class:`~google.cloud.spanner_v1.snapshot.Snapshot` ctor.

        :rtype: :class:`~google.cloud.spanner_v1.snapshot.Snapshot`
        :returns: a snapshot bound to this session
        :raises ValueError: if the session has not yet been created.
        """
        if self._session_id is None:
            raise ValueError("Session has not been created.")

        return Snapshot(self, **kw)

    @CrossSync.convert
    async def read(self, table, columns, keyset, index="", limit=0, column_info=None):
        """Perform a ``StreamingRead`` API request for rows in a table.

        :type table: str
        :param table: name of the table from which to fetch data

        :type columns: list of str
        :param columns: names of columns to be retrieved

        :type keyset: :class:`~google.cloud.spanner_v1.keyset.KeySet`
        :param keyset: keys / ranges identifying rows to be retrieved

        :type index: str
        :param index: (Optional) name of index to use, rather than the
                      table's primary key

        :type limit: int
        :param limit: (Optional) maximum number of rows to return

        :type column_info: dict
        :param column_info: (Optional) dict of mapping between column names and additional column information.
            An object where column names as keys and custom objects as corresponding
            values for deserialization. It's specifically useful for data types like
            protobuf where deserialization logic is on user-specific code. When provided,
            the custom object enables deserialization of backend-received column data.
            If not provided, data remains serialized as bytes for Proto Messages and
            integer for Proto Enums.

        :rtype: :class:`~google.cloud.spanner_v1.streamed.StreamedResultSet`
        :returns: a result set instance which can be used to consume rows.
        """
        return await self.snapshot().read(
            table, columns, keyset, index, limit, column_info=column_info
        )

    @CrossSync.convert
    async def execute_sql(
        self,
        sql,
        params=None,
        param_types=None,
        query_mode=None,
        query_options=None,
        request_options=None,
        retry=method.DEFAULT,
        timeout=method.DEFAULT,
        column_info=None,
    ):
        """Perform an ``ExecuteStreamingSql`` API request.

        :type sql: str
        :param sql: SQL query statement

        :type params: dict, {str -> column value}
        :param params: values for parameter replacement.  Keys must match
                       the names used in ``sql``.

        :type param_types:
            dict, {str -> :class:`~google.spanner.v1.types.TypeCode`}
        :param param_types: (Optional) explicit types for one or more param
                            values;  overrides default type detection on the
                            back-end.

        :type query_mode:
            :class:`~google.spanner.v1.types.ExecuteSqlRequest.QueryMode`
        :param query_mode: Mode governing return of results / query plan. See:
            `QueryMode <https://cloud.google.com/spanner/reference/rpc/google.spanner.v1#google.spanner.v1.ExecuteSqlRequest.QueryMode>`_.

        :type query_options:
            :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions`
            or :class:`dict`
        :param query_options: (Optional) Options that are provided for query plan stability.

        :type request_options:
            :class:`google.cloud.spanner_v1.types.RequestOptions`
        :param request_options:
                (Optional) Common options for this request.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.spanner_v1.types.RequestOptions`.

        :type retry: :class:`~google.api_core.retry.Retry`
        :param retry: (Optional) The retry settings for this request.

        :type timeout: float
        :param timeout: (Optional) The timeout for this request.

        :type column_info: dict
        :param column_info: (Optional) dict of mapping between column names and additional column information.
            An object where column names as keys and custom objects as corresponding
            values for deserialization. It's specifically useful for data types like
            protobuf where deserialization logic is on user-specific code. When provided,
            the custom object enables deserialization of backend-received column data.
            If not provided, data remains serialized as bytes for Proto Messages and
            integer for Proto Enums.

        :rtype: :class:`~google.cloud.spanner_v1.streamed.StreamedResultSet`
        :returns: a result set instance which can be used to consume rows.
        """
        return await self.snapshot().execute_sql(
            sql,
            params,
            param_types,
            query_mode,
            query_options=query_options,
            request_options=request_options,
            retry=retry,
            timeout=timeout,
            column_info=column_info,
        )

    def batch(self):
        """Factory to create a batch for this session.

        :rtype: :class:`~google.cloud.spanner_v1.batch.Batch`
        :returns: a batch bound to this session
        :raises ValueError: if the session has not yet been created.
        """
        if self._session_id is None:
            raise ValueError("Session has not been created.")

        return Batch(self)

    def transaction(self, client_context=None) -> Transaction:
        """Create a transaction to perform a set of reads with shared staleness.

        :rtype: :class:`~google.cloud.spanner_v1.transaction.Transaction`
        :returns: a transaction bound to this session

        :raises ValueError: if the session has not yet been created.
        """
        if self._session_id is None:
            raise ValueError("Session has not been created.")

        return Transaction(self, client_context=client_context)

    def _create_transaction_for_attempt(
        self,
        client_context=None,
        transaction_tag=None,
        exclude_txn_from_change_streams=None,
        isolation_level=None,
        read_lock_mode=None,
        previous_transaction_id=None,
    ) -> Transaction:
        """Create and configure a transaction instance for a single attempt.

        :type client_context: :class:`~google.cloud.spanner_v1.client_context.ClientContext`
        :param client_context: (Optional) client context to use for the transaction.

        :type transaction_tag: str
        :param transaction_tag: (Optional) transaction tag.

        :type exclude_txn_from_change_streams: bool
        :param exclude_txn_from_change_streams: (Optional) whether to exclude from change streams.

        :type isolation_level: int
        :param isolation_level: (Optional) isolation level.

        :type read_lock_mode: int
        :param read_lock_mode: (Optional) read lock mode.

        :type previous_transaction_id: bytes
        :param previous_transaction_id: (Optional) previous transaction id for multiplexed sessions.

        :rtype: :class:`~google.cloud.spanner_v1.transaction.Transaction`
        :returns: A configured Transaction instance.
        """
        transaction = self.transaction(client_context=client_context)
        transaction.transaction_tag = transaction_tag
        transaction.exclude_txn_from_change_streams = exclude_txn_from_change_streams
        transaction.isolation_level = isolation_level
        transaction.read_lock_mode = read_lock_mode

        if self.is_multiplexed:
            transaction._multiplexed_session_previous_transaction_id = (
                previous_transaction_id
            )
        return transaction

    @CrossSync.convert
    async def _handle_aborted(
        self,
        exception,
        span,
        event_name,
        attempts,
        deadline,
        default_retry_delay,
        include_cause=False,
    ):
        """Handle an Aborted error: record trace event and delay until next retry attempt.

        :type exception: :class:`google.api_core.exceptions.Aborted`
        :param exception: The aborted exception.

        :type span: :class:`opentelemetry.trace.Span`
        :param span: The current active span.

        :type event_name: str
        :param event_name: The span event name to record.

        :type attempts: int
        :param attempts: The retry attempt number.

        :type deadline: float
        :param deadline: Timestamp deadline for retrying.

        :type default_retry_delay: float
        :param default_retry_delay: Default delay between retries.

        :type include_cause: bool
        :param include_cause: (Optional) Whether to include the exception string as cause.
        """
        if span and span.is_recording():
            errors = getattr(exception, "errors", None)
            cause = errors[0] if errors else exception
            delay_seconds = _get_retry_delay(
                cause,
                attempts,
                default_retry_delay=default_retry_delay,
            )
            attributes = {
                "attempt": attempts,
                "delay_seconds": delay_seconds,
            }
            if include_cause:
                attributes["cause"] = str(exception)
            add_span_event(span, event_name, attributes)
        await _delay_until_retry(
            exception,
            deadline,
            attempts,
            default_retry_delay=default_retry_delay,
        )

    @CrossSync.convert
    async def run_in_transaction(self, func, *args, **kw):
        """Perform a unit of work in a transaction, retrying on abort.

        :type func: callable
        :param func: takes a required positional argument, the transaction,
                     and additional positional / keyword arguments as supplied
                     by the caller.

        :type args: tuple
        :param args: additional positional arguments to be passed to ``func``.

        :type kw: dict
        :param kw: (Optional) keyword arguments to be passed to ``func``.
                   If passed:
                   "timeout_secs" will be removed and used to
                   override the default retry timeout which defines maximum timestamp
                   to continue retrying the transaction.
                   "commit_request_options" will be removed and used to set the
                   request options for the commit request.
                   "max_commit_delay" will be removed and used to set the max commit delay for the request.
                   "transaction_tag" will be removed and used to set the transaction tag for the request.
                   "exclude_txn_from_change_streams" if true, instructs the transaction to be excluded
                   from being recorded in change streams with the DDL option `allow_txn_exclusion=true`.
                   This does not exclude the transaction from being recorded in the change streams with
                   the DDL option `allow_txn_exclusion` being false or unset.
                   "isolation_level" sets the isolation level for the transaction.
                   "read_lock_mode" sets the read lock mode for the transaction.

        :rtype: Any
        :returns: The return value of ``func``.

        :raises Exception:
            reraises any non-ABORT exceptions raised by ``func``.
        """
        deadline = time.time() + kw.pop("timeout_secs", DEFAULT_RETRY_TIMEOUT_SECS)
        default_retry_delay = kw.pop("default_retry_delay", None)
        commit_request_options = kw.pop("commit_request_options", None)
        max_commit_delay = kw.pop("max_commit_delay", None)
        transaction_tag = kw.pop("transaction_tag", None)
        exclude_txn_from_change_streams = kw.pop(
            "exclude_txn_from_change_streams", None
        )
        isolation_level = kw.pop("isolation_level", None)
        read_lock_mode = kw.pop("read_lock_mode", None)
        client_context = kw.pop("client_context", None)

        database = self._database
        log_commit_stats = database.log_commit_stats

        span = get_current_span()
        attempts: int = 0

        # If a transaction using a multiplexed session is retried after an aborted
        # user operation, it should include the previous transaction ID in the
        # transaction options used to begin the transaction. This allows the backend
        # to recognize the transaction and increase the lock order for the new
        # transaction that is created.
        # See :attr:`~google.cloud.spanner_v1.types.TransactionOptions.ReadWrite.multiplexed_session_previous_transaction_id`
        previous_transaction_id: Optional[bytes] = None

        while True:
            transaction = self._create_transaction_for_attempt(
                client_context=client_context,
                transaction_tag=transaction_tag,
                exclude_txn_from_change_streams=exclude_txn_from_change_streams,
                isolation_level=isolation_level,
                read_lock_mode=read_lock_mode,
                previous_transaction_id=previous_transaction_id,
            )
            attempts += 1

            try:
                return_value = await CrossSync.run_if_async(
                    func, transaction, *args, **kw
                )

            except Aborted as exc:
                previous_transaction_id = transaction._transaction_id
                await self._handle_aborted(
                    exc,
                    span,
                    "Transaction was aborted in user operation, retrying",
                    attempts,
                    deadline,
                    default_retry_delay,
                    include_cause=True,
                )
                continue

            except GoogleAPICallError:
                add_span_event(
                    span,
                    "User operation failed due to GoogleAPICallError, not retrying",
                    {"attempt": attempts},
                )
                raise

            except Exception:
                add_span_event(
                    span,
                    "User operation failed. Invoking Transaction.rollback(), not retrying",
                    {"attempt": attempts},
                )
                await transaction.rollback()
                raise

            try:
                await transaction.commit(
                    return_commit_stats=log_commit_stats,
                    request_options=commit_request_options,
                    max_commit_delay=max_commit_delay,
                )

            except Aborted as exc:
                previous_transaction_id = transaction._transaction_id
                await self._handle_aborted(
                    exc,
                    span,
                    "Transaction was aborted during commit, retrying",
                    attempts,
                    deadline,
                    default_retry_delay,
                )
                continue

            except GoogleAPICallError:
                add_span_event(
                    span,
                    "Transaction.commit failed due to GoogleAPICallError, not retrying",
                    {"attempt": attempts},
                )
                raise

            else:
                if log_commit_stats and transaction.commit_stats:
                    database.logger.info(
                        "CommitStats: {}".format(transaction.commit_stats),
                        extra={"commit_stats": transaction.commit_stats},
                    )
                return return_value
