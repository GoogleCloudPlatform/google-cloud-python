# Copyright 2024 Google LLC All rights reserved.
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

"""Manage sessions for a database."""

__CROSS_SYNC_OUTPUT__ = "google.cloud.spanner_v1.database_sessions_manager"

import asyncio
import threading
import time
from datetime import timedelta
from enum import Enum
from os import getenv
from threading import Thread
from typing import Optional
from weakref import ref

from google.cloud.aio._cross_sync import CrossSync
from google.cloud.spanner_v1._async.session import Session
from google.cloud.spanner_v1._opentelemetry_tracing import (
    add_span_event,
    get_current_span,
)


class TransactionType(Enum):
    """Transaction types for session options."""

    READ_ONLY = "read-only"
    PARTITIONED = "partitioned"
    READ_WRITE = "read/write"


@CrossSync.convert_class
class DatabaseSessionsManager(object):
    """Manages sessions for a Cloud Spanner database.

    Sessions can be checked out from the database session manager for a specific
    transaction type using :meth:`get_session`, and returned to the session manager
    using :meth:`put_session`.

    The sessions returned by the session manager depend on the configured environment variables
    and the provided session pool (see :class:`~google.cloud.spanner_v1.pool.AbstractSessionPool`).

    :type database: :class:`~google.cloud.spanner_v1.database.Database`
    :param database: The database to manage sessions for.

    :type pool: :class:`~google.cloud.spanner_v1.pool.AbstractSessionPool`
    :param pool: The pool to get non-multiplexed sessions from.
    """

    _ENV_VAR_MULTIPLEXED = "GOOGLE_CLOUD_SPANNER_MULTIPLEXED_SESSIONS"
    _ENV_VAR_MULTIPLEXED_PARTITIONED = (
        "GOOGLE_CLOUD_SPANNER_MULTIPLEXED_SESSIONS_PARTITIONED_OPS"
    )
    _ENV_VAR_MULTIPLEXED_READ_WRITE = "GOOGLE_CLOUD_SPANNER_MULTIPLEXED_SESSIONS_FOR_RW"
    _MAINTENANCE_THREAD_POLLING_INTERVAL = timedelta(minutes=10)
    _MAINTENANCE_THREAD_REFRESH_INTERVAL = timedelta(days=7)

    def __init__(self, database, pool):
        self._database = database
        self._pool = pool
        self._multiplexed_session: Optional[Session] = None
        self._multiplexed_session_thread: Optional[CrossSync.Task] = None
        self._init_lock = threading.Lock()
        self._multiplexed_session_lock: Optional[CrossSync.Lock] = None
        self._multiplexed_session_terminate_event: Optional[CrossSync.Event] = None

    @CrossSync.convert
    async def get_session(self, transaction_type: TransactionType) -> Session:
        """Returns a session for the given transaction type from the database session manager.

        :rtype: :class:`~google.cloud.spanner_v1.session.Session`
        :returns: a session for the given transaction type."""
        session = (
            await self._get_multiplexed_session()
            if self._use_multiplexed(transaction_type)
            or (
                self._database._instance
                and getattr(
                    getattr(self._database._instance, "_client", None),
                    "instance_type",
                    None,
                )
                == "omni"
            )
            else await CrossSync.run_if_async(self._pool.get)
        )
        add_span_event(
            get_current_span(),
            "Using session",
            {"id": session.session_id, "multiplexed": session.is_multiplexed},
        )
        return session

    @CrossSync.convert
    async def put_session(self, session: Session) -> None:
        """Returns the session to the database session manager.

        :type session: :class:`~google.cloud.spanner_v1.session.Session`
        :param session: The session to return to the database session manager."""
        add_span_event(
            get_current_span(),
            "Returning session",
            {"id": session.session_id, "multiplexed": session.is_multiplexed},
        )
        if not session.is_multiplexed:
            await CrossSync.run_if_async(self._pool.put, session)

    @CrossSync.convert
    async def _get_multiplexed_session(self) -> Session:
        """Returns a multiplexed session from the database session manager.

        If the multiplexed session is not defined, creates a new multiplexed
        session and starts a maintenance thread to periodically rotate
        it so that it remains valid. Otherwise, simply returns the
        current multiplexed session.

        :rtype: :class:`~google.cloud.spanner_v1.session.Session`
        :returns: a multiplexed session."""
        session = self._multiplexed_session
        if session is not None:
            return session

        with self._init_lock:
            if self._multiplexed_session_lock is None:
                self._multiplexed_session_lock = CrossSync.Lock()
            if self._multiplexed_session_terminate_event is None:
                self._multiplexed_session_terminate_event = CrossSync.Event()

        async with self._multiplexed_session_lock:
            if self._multiplexed_session is None:
                session = await self._build_multiplexed_session()
                maintenance_thread = self._build_maintenance_thread(session)
                if not CrossSync.is_async:
                    maintenance_thread.start()
                self._multiplexed_session_thread = maintenance_thread
                self._multiplexed_session = session
            return self._multiplexed_session

    @CrossSync.convert
    async def _build_multiplexed_session(self) -> Session:
        """Builds and returns a new multiplexed session for the database session manager.

        :rtype: :class:`~google.cloud.spanner_v1.session.Session`
        :returns: a new multiplexed session."""
        session = Session(
            database=self._database,
            database_role=self._database.database_role,
            is_multiplexed=True,
        )
        await session.create()
        return session

    def _build_maintenance_thread(
        self, session: Optional[Session] = None
    ) -> CrossSync.Task:
        """Builds and returns a multiplexed session maintenance thread for
        the database session manager. This thread will periodically rotate
        the multiplexed session to ensure that it is always valid.

        :type session: :class:`~google.cloud.spanner_v1.session.Session`
        :param session: (Optional) The multiplexed session to maintain.

        :rtype: :class:`CrossSync.Task`
        :returns: a multiplexed session maintenance thread."""
        session_to_maintain = (
            session if session is not None else self._multiplexed_session
        )
        session_manager_ref = ref(self)
        if CrossSync.is_async:
            return CrossSync.create_task(
                self._maintain_multiplexed_session, session_manager_ref
            )
        else:
            session_id = (
                session_to_maintain.session_id
                if session_to_maintain is not None
                else ""
            )
            return Thread(
                target=self._maintain_multiplexed_session,
                name=f"maintenance-multiplexed-session-{session_id}",
                args=[session_manager_ref],
                daemon=True,
            )

    @CrossSync.convert
    async def _rotate_multiplexed_session(self) -> bool:
        """Rotates the multiplexed session by building and swapping in a new session.

        :rtype: bool
        :returns: True if the session was successfully refreshed, False otherwise.
        """
        try:
            new_session = await self._build_multiplexed_session()
        except Exception:
            return False

        async with self._multiplexed_session_lock:
            self._multiplexed_session = new_session

        return True

    @staticmethod
    @CrossSync.convert
    async def _maintain_multiplexed_session(session_manager_ref) -> None:
        """Maintains the multiplexed session for the database session manager.

        This method will periodically rotate the referenced database session manager's
        multiplexed session to ensure that it is always valid. The method will run until
        the database session manager is garbage collected or the session manager is closed.

        :type session_manager_ref: :class:`_weakref.ReferenceType`
        :param session_manager_ref: A weak reference to the database session manager."""
        manager = session_manager_ref()
        if manager is None:
            return
        polling_interval_seconds = (
            manager._MAINTENANCE_THREAD_POLLING_INTERVAL.total_seconds()
        )
        refresh_interval_seconds = (
            manager._MAINTENANCE_THREAD_REFRESH_INTERVAL.total_seconds()
        )
        session_created_time = time.monotonic()
        while True:
            manager = session_manager_ref()
            if manager is None:
                return
            terminate_event = manager._multiplexed_session_terminate_event
            if terminate_event.is_set():
                return

            if time.monotonic() - session_created_time >= refresh_interval_seconds:
                if await manager._rotate_multiplexed_session():
                    session_created_time = time.monotonic()
                    manager = None
                    continue

            manager = None
            await CrossSync.event_wait(
                terminate_event,
                timeout=polling_interval_seconds,
            )

    @classmethod
    def _use_multiplexed(cls, transaction_type: TransactionType) -> bool:
        """Returns whether to use multiplexed sessions for the given transaction type."""
        if transaction_type is TransactionType.READ_ONLY:
            return cls._getenv(cls._ENV_VAR_MULTIPLEXED)
        elif transaction_type is TransactionType.PARTITIONED:
            return cls._getenv(cls._ENV_VAR_MULTIPLEXED_PARTITIONED)
        elif transaction_type is TransactionType.READ_WRITE:
            return cls._getenv(cls._ENV_VAR_MULTIPLEXED_READ_WRITE)
        raise ValueError(f"Transaction type {transaction_type} is not supported.")

    @classmethod
    def _getenv(cls, env_var_name: str) -> bool:
        """Returns the value of the given environment variable as a boolean."""
        env_var_value = getenv(env_var_name, "true").lower().strip()
        return env_var_value != "false"

    @CrossSync.convert
    async def close(self) -> None:
        """Closes the database session manager and stops all background tasks."""
        if self._multiplexed_session_terminate_event is not None:
            self._multiplexed_session_terminate_event.set()
        if self._multiplexed_session_thread is not None:
            if CrossSync.is_async:
                self._multiplexed_session_thread.cancel()
                try:
                    await self._multiplexed_session_thread
                except CrossSync.rm_aio(asyncio.CancelledError):
                    pass
            else:
                self._multiplexed_session_thread.join()
        self._multiplexed_session = None
