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

"""Asyncio support for the Cloud Spanner SQLAlchemy dialect.

The Spanner DB API is synchronous, so this dialect adapts it for asyncio by
running every blocking DB API call in a worker thread and exposing the result
through SQLAlchemy's standard ``AsyncAdapt_dbapi_*`` facades.

Known limitations, both of which run blocking gRPC calls on the event loop
thread rather than in a worker thread:

* Schema reflection and DDL (``metadata.create_all``, ``autoload_with``,
  Alembic) use ``connection.connection.database.snapshot()`` directly in the
  synchronous dialect, bypassing this adapter.
* Returning a connection with an open transaction to the pool triggers the
  ``Pool.reset`` handler in the synchronous dialect, which rolls back inline.
"""

import asyncio
import inspect

from .sqlalchemy_spanner import SpannerDialect

try:
    from sqlalchemy.connectors.asyncio import (
        AsyncAdapt_dbapi_connection,
        AsyncAdapt_dbapi_cursor,
        AsyncAdapt_dbapi_module,
    )
except ImportError as exc:  # pragma: NO COVER
    raise ImportError(
        "The asyncio Spanner dialect (spanner+spanner_asyncio) requires "
        "SQLAlchemy 2.0 or later."
    ) from exc

from sqlalchemy.util.concurrency import await_only, in_greenlet


def _forward_to(instance, own_attr_name):
    """Return the object attribute access should be delegated to.

    Raises ``AttributeError`` instead of recursing when the delegate has not
    been assigned yet, which happens if ``__init__`` fails part way through or
    the object is copied/unpickled.
    """
    try:
        return object.__getattribute__(instance, own_attr_name)
    except AttributeError:
        raise AttributeError(own_attr_name) from None


def _is_own_attribute(instance, name):
    """Whether ``name`` belongs to the adapter itself rather than the driver.

    Private names and anything declared on the adapter class -- including
    ``__slots__`` descriptors such as ``dbapi`` and ``await_`` -- are set on
    the adapter; every other name is forwarded to the wrapped driver object so
    that assignments made by the synchronous dialect actually reach Spanner.
    """
    return name.startswith("_") or hasattr(type(instance), name)


class AsyncIODBAPISpannerCursor:
    """An asyncio facade over a synchronous ``spanner_dbapi`` cursor."""

    def __init__(self, sync_cursor):
        self._sync_cursor = sync_cursor

    @property
    def description(self):
        return self._sync_cursor.description

    @property
    def rowcount(self):
        return self._sync_cursor.rowcount

    @property
    def lastrowid(self):
        return self._sync_cursor.lastrowid

    @property
    def arraysize(self):
        return self._sync_cursor.arraysize

    @arraysize.setter
    def arraysize(self, value):
        self._sync_cursor.arraysize = value

    async def close(self):
        await asyncio.to_thread(self._sync_cursor.close)

    async def execute(self, operation, parameters=None):
        return await asyncio.to_thread(self._sync_cursor.execute, operation, parameters)

    async def executemany(self, operation, seq_of_parameters):
        return await asyncio.to_thread(
            self._sync_cursor.executemany, operation, seq_of_parameters
        )

    async def fetchone(self):
        return await asyncio.to_thread(self._sync_cursor.fetchone)

    async def fetchmany(self, size=None):
        return await asyncio.to_thread(self._sync_cursor.fetchmany, size)

    async def fetchall(self):
        return await asyncio.to_thread(self._sync_cursor.fetchall)

    async def nextset(self):
        if hasattr(self._sync_cursor, "nextset"):
            return await asyncio.to_thread(self._sync_cursor.nextset)

    def __getattr__(self, name):
        return getattr(_forward_to(self, "_sync_cursor"), name)

    def __setattr__(self, name, value):
        if _is_own_attribute(self, name):
            object.__setattr__(self, name, value)
        else:
            setattr(_forward_to(self, "_sync_cursor"), name, value)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class AsyncIODBAPISpannerConnection:
    """An asyncio facade over a synchronous ``spanner_dbapi`` connection."""

    def __init__(self, sync_conn):
        self._sync_conn = sync_conn

    async def commit(self):
        await asyncio.to_thread(self._sync_conn.commit)

    async def rollback(self):
        await asyncio.to_thread(self._sync_conn.rollback)

    async def close(self):
        await asyncio.to_thread(self._sync_conn.close)

    def cursor(self):
        return AsyncIODBAPISpannerCursor(self._sync_conn.cursor())

    def __getattr__(self, name):
        return getattr(_forward_to(self, "_sync_conn"), name)

    def __setattr__(self, name, value):
        if _is_own_attribute(self, name):
            object.__setattr__(self, name, value)
        else:
            setattr(_forward_to(self, "_sync_conn"), name, value)


class AsyncAdapt_spanner_cursor(AsyncAdapt_dbapi_cursor):
    @property
    def connection(self):
        return self._adapt_connection

    def __getattr__(self, name):
        return getattr(_forward_to(self, "_cursor"), name)

    def __setattr__(self, name, value):
        # ``SpannerExecutionContext.pre_exec`` sets ``request_tag`` on the
        # cursor; without this the value would be stored on the adapter and
        # never reach Spanner.
        if _is_own_attribute(self, name):
            object.__setattr__(self, name, value)
        else:
            setattr(_forward_to(self, "_cursor"), name, value)


class AsyncAdapt_spanner_connection(AsyncAdapt_dbapi_connection):
    _cursor_cls = AsyncAdapt_spanner_cursor

    @property
    def connection(self):
        return self._connection._sync_conn

    def terminate(self):
        """Close the connection without waiting on the event loop."""
        if in_greenlet():
            self.await_(self._connection.close())
        else:
            # Garbage-collection path: there is no greenlet to await in, so
            # the blocking close has to be called directly.
            self._connection._sync_conn.close()

    def __getattr__(self, name):
        return getattr(_forward_to(self, "_connection"), name)

    def __setattr__(self, name, value):
        # ``SpannerExecutionContext.pre_exec`` sets ``read_only``, ``staleness``,
        # ``request_priority`` and ``transaction_tag`` on the connection it gets
        # from the pool, which is this adapter. Forward those writes so the
        # execution options are applied to the real Spanner connection.
        if _is_own_attribute(self, name):
            object.__setattr__(self, name, value)
        else:
            setattr(_forward_to(self, "_connection"), name, value)


class AsyncAdapt_spanner_dbapi(AsyncAdapt_dbapi_module):
    await_ = staticmethod(await_only)

    def __init__(self, spanner_dbapi):
        self.spanner_dbapi = spanner_dbapi

    def __getattr__(self, name):
        # Expose the synchronous DB API module's attributes (exception classes,
        # ``paramstyle``, type constructors, ...) unchanged.
        return getattr(_forward_to(self, "spanner_dbapi"), name)

    def connect(self, *arg, **kw):
        async_creator_fn = kw.pop("async_creator_fn", None)
        if async_creator_fn:
            connection = async_creator_fn(*arg, **kw)
            if inspect.isawaitable(connection):
                connection = self.await_(connection)
        else:
            connection = self.spanner_dbapi.connect(*arg, **kw)

        return AsyncAdapt_spanner_connection(
            self, AsyncIODBAPISpannerConnection(connection)
        )


class SpannerDialect_asyncio(SpannerDialect):
    driver = "spanner_asyncio"
    is_async = True
    has_terminate = True
    supports_statement_cache = True

    @classmethod
    def import_dbapi(cls):
        from google.cloud import spanner_dbapi

        return AsyncAdapt_spanner_dbapi(spanner_dbapi)

    @classmethod
    def dbapi(cls):
        return cls.import_dbapi()

    @classmethod
    def get_pool_class(cls, url):
        from sqlalchemy.pool import AsyncAdaptedQueuePool

        return AsyncAdaptedQueuePool

    def do_terminate(self, dbapi_connection):
        dbapi_connection.terminate()

    def get_driver_connection(self, connection):
        return connection._connection._sync_conn
