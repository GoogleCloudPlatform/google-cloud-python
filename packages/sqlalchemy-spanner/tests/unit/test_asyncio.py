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

import asyncio
from unittest.mock import MagicMock, patch

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.testing import eq_, is_true
from sqlalchemy.testing.plugin.plugin_base import fixtures
from sqlalchemy.util import greenlet_spawn

from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner_asyncio import (
    AsyncAdapt_spanner_connection,
    AsyncAdapt_spanner_dbapi,
    AsyncIODBAPISpannerConnection,
    SpannerDialect_asyncio,
)

URL = "spanner+spanner_asyncio:///projects/p/instances/i/databases/d"


def _adapted_connection(sync_conn):
    """Build an adapter around ``sync_conn`` without going through a pool."""
    return AsyncAdapt_spanner_connection(
        MagicMock(), AsyncIODBAPISpannerConnection(sync_conn)
    )


class TestSpannerAsyncioDialect(fixtures.TestBase):
    """Unit tests for the ``spanner+spanner_asyncio`` dialect.

    These tests drive the event loop with ``asyncio.run()`` rather than using
    ``pytest.mark.asyncio``, so that they do not depend on ``pytest-asyncio``
    which the ``unit`` nox session does not install.
    """

    def _engine(self):
        return create_async_engine(URL, poolclass=NullPool)

    def test_dialect_is_registered_as_async(self):
        engine = self._engine()

        is_true(engine.dialect.is_async)
        is_true(isinstance(engine.dialect, SpannerDialect_asyncio))
        eq_(engine.dialect.driver, "spanner_asyncio")
        # Required so that SQLAlchemy can drop a connection that was garbage
        # collected without being closed, instead of leaking a Spanner session.
        is_true(engine.dialect.has_terminate)

    def test_execute_is_delegated_to_the_sync_cursor(self):
        with patch("google.cloud.spanner_dbapi.connect") as connect:
            sync_conn = connect.return_value
            sync_cursor = sync_conn.cursor.return_value

            async def go():
                engine = self._engine()
                async with engine.connect() as conn:
                    await conn.execute(text("SELECT 1"))
                await engine.dispose()

            asyncio.run(go())

            connect.assert_called_once()
            sync_cursor.execute.assert_called_once()
            eq_(sync_cursor.execute.call_args[0][0], "SELECT 1")
            sync_conn.close.assert_called_once()

    def test_execution_options_reach_the_spanner_connection(self):
        """Execution options are set on the DB API connection by ``pre_exec``.

        The pool hands ``pre_exec`` the async adapter rather than the Spanner
        connection, so the adapter has to forward the writes; otherwise the
        options are silently dropped.
        """
        staleness = {"max_staleness": {"seconds": 5}}
        observed = {}

        with patch("google.cloud.spanner_dbapi.connect") as connect:
            sync_conn = connect.return_value
            sync_cursor = sync_conn.cursor.return_value

            async def go():
                engine = self._engine()
                async with engine.connect() as conn:
                    conn = await conn.execution_options(
                        read_only=True,
                        staleness=staleness,
                        request_priority=3,
                        transaction_tag="transaction-tag",
                        request_tag="request-tag",
                    )
                    await conn.execute(text("SELECT 1"))
                    observed["read_only"] = sync_conn.read_only
                    observed["staleness"] = sync_conn.staleness
                    observed["request_priority"] = sync_conn.request_priority
                    observed["transaction_tag"] = sync_conn.transaction_tag
                    observed["request_tag"] = sync_cursor.request_tag
                await engine.dispose()

            asyncio.run(go())

        eq_(observed["read_only"], True)
        eq_(observed["staleness"], staleness)
        eq_(observed["request_priority"], 3)
        eq_(observed["transaction_tag"], "transaction-tag")
        eq_(observed["request_tag"], "request-tag")

    def test_get_driver_connection_returns_the_spanner_connection(self):
        sync_conn = MagicMock()

        eq_(
            SpannerDialect_asyncio().get_driver_connection(
                _adapted_connection(sync_conn)
            ),
            sync_conn,
        )

    def test_terminate_closes_the_spanner_connection(self):
        sync_conn = MagicMock()

        # Outside a greenlet ``terminate()`` cannot await, so it has to close
        # the underlying connection directly.
        _adapted_connection(sync_conn).terminate()

        sync_conn.close.assert_called_once()

    def test_connection_attribute_reads_are_forwarded(self):
        sync_conn = MagicMock()
        sync_conn.autocommit = False

        eq_(_adapted_connection(sync_conn).autocommit, False)

    def test_sync_creator_fn_is_used_as_is(self):
        sync_conn = MagicMock()
        dbapi = AsyncAdapt_spanner_dbapi(MagicMock())

        adapted = dbapi.connect(async_creator_fn=lambda: sync_conn)

        eq_(adapted.connection, sync_conn)

    def test_async_creator_fn_is_awaited(self):
        sync_conn = MagicMock()
        dbapi = AsyncAdapt_spanner_dbapi(MagicMock())

        async def creator():
            return sync_conn

        async def go():
            return await greenlet_spawn(dbapi.connect, async_creator_fn=creator)

        eq_(asyncio.run(go()).connection, sync_conn)

    def test_sync_dbapi_module_attributes_are_exposed(self):
        from google.cloud import spanner_dbapi

        dbapi = SpannerDialect_asyncio.import_dbapi()

        eq_(dbapi.paramstyle, spanner_dbapi.paramstyle)
        eq_(dbapi.Error, spanner_dbapi.Error)
