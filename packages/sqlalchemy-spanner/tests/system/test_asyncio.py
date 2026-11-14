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

from google.cloud import spanner_dbapi
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    insert,
    select,
    text,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.testing import config, eq_, is_true
from sqlalchemy.testing.plugin.plugin_base import fixtures

metadata = MetaData()
users = Table(
    "async_users",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(32), nullable=False),
)

reflected_metadata = MetaData()
Table(
    "async_reflected",
    reflected_metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(16), nullable=False),
)


class TestAsyncio(fixtures.TestBase):
    """End-to-end tests for the ``spanner+spanner_asyncio`` dialect.

    Each test drives the event loop with ``asyncio.run()`` rather than using
    ``pytest.mark.asyncio``, so the tests do not depend on the asyncio mode
    that the session happens to be configured with.
    """

    def setup_test(self):
        metadata.drop_all(config.db, checkfirst=True)
        metadata.create_all(config.db)

    def teardown_test(self):
        metadata.drop_all(config.db, checkfirst=True)
        reflected_metadata.drop_all(config.db, checkfirst=True)

    def _engine(self):
        return create_async_engine(
            config.db.url.set(drivername="spanner+spanner_asyncio")
        )

    def _run(self, main):
        async def wrapper():
            engine = self._engine()
            try:
                return await main(engine)
            finally:
                await engine.dispose()

        return asyncio.run(wrapper())

    def _insert_users(self):
        with config.db.begin() as connection:
            connection.execute(
                insert(users),
                [
                    {"user_id": 1, "user_name": "alice"},
                    {"user_id": 2, "user_name": "bob"},
                ],
            )

    def test_dialect_is_async(self):
        async def main(engine):
            is_true(engine.dialect.is_async)
            is_true(engine.dialect.has_terminate)
            eq_(engine.dialect.driver, "spanner_asyncio")

        self._run(main)

    def test_select(self):
        async def main(engine):
            async with engine.connect() as connection:
                result = await connection.execute(text("SELECT 1"))
                eq_(result.fetchone()[0], 1)

        self._run(main)

    def test_insert_commit_select(self):
        async def main(engine):
            async with engine.begin() as connection:
                await connection.execute(
                    insert(users),
                    [
                        {"user_id": 1, "user_name": "alice"},
                        {"user_id": 2, "user_name": "bob"},
                    ],
                )
            async with engine.connect() as connection:
                result = await connection.execute(
                    select(users).order_by(users.c.user_id)
                )
                eq_([row.user_name for row in result.fetchall()], ["alice", "bob"])

        self._run(main)

    def test_rollback(self):
        self._insert_users()

        async def main(engine):
            async with engine.connect() as connection:
                await connection.execute(
                    insert(users), {"user_id": 3, "user_name": "carol"}
                )
                await connection.rollback()
            async with engine.connect() as connection:
                result = await connection.execute(
                    text("SELECT COUNT(*) FROM async_users")
                )
                eq_(result.scalar(), 2)

        self._run(main)

    def test_create_all_and_reflection(self):
        async def main(engine):
            # Spanner batches DDL and applies it on commit, so the drop and the
            # create have to happen in separate transactions.
            async with engine.begin() as connection:
                await connection.run_sync(reflected_metadata.drop_all, checkfirst=True)
            async with engine.begin() as connection:
                await connection.run_sync(reflected_metadata.create_all)

            async with engine.connect() as connection:
                names = await connection.run_sync(
                    lambda sync_connection: sync_connection.dialect.get_table_names(
                        sync_connection
                    )
                )
                is_true("async_reflected" in names)

                columns = await connection.run_sync(
                    lambda sync_connection: sync_connection.dialect.get_columns(
                        sync_connection, "async_reflected"
                    )
                )
                eq_([column["name"] for column in columns], ["id", "name"])

        self._run(main)

    def test_read_only_execution_option(self):
        """``read_only`` has to reach the Spanner connection itself.

        SQLAlchemy hands the execution context the async adapter rather than the
        Spanner connection, so the adapter must forward the assignment.
        """
        self._insert_users()

        async def main(engine):
            async with engine.connect() as connection:
                connection = await connection.execution_options(read_only=True)
                result = await connection.execute(select(users))
                eq_(len(result.fetchall()), 2)

                raw_connection = await connection.get_raw_connection()
                is_true(raw_connection.driver_connection.read_only)
                is_true(
                    isinstance(
                        raw_connection.driver_connection, spanner_dbapi.Connection
                    )
                )

        self._run(main)

    def _database_timestamp(self):
        """Read the current timestamp from Spanner.

        The local clock cannot be used for a stale read, because any skew
        against Spanner's clock makes the read timestamp unusable.
        """
        with config.db.connect() as connection:
            connection = connection.execution_options(isolation_level="AUTOCOMMIT")
            return connection.execute(select(text("current_timestamp"))).one()[0]

    def test_stale_read(self):
        before_insert = self._database_timestamp()
        self._insert_users()
        after_insert = self._database_timestamp()

        async def main(engine):
            async def stale_row_count(read_timestamp):
                async with engine.connect() as connection:
                    connection = await connection.execution_options(
                        read_only=True, staleness={"read_timestamp": read_timestamp}
                    )
                    result = await connection.execute(select(users))
                    return len(result.fetchall())

            eq_(await stale_row_count(after_insert), 2)
            eq_(await stale_row_count(before_insert), 0)

        self._run(main)

    def test_request_and_transaction_tags(self):
        async def main(engine):
            async with engine.begin() as connection:
                connection = await connection.execution_options(
                    request_tag="async-request-tag",
                    transaction_tag="async-transaction-tag",
                )
                await connection.execute(
                    insert(users), {"user_id": 1, "user_name": "alice"}
                )
            async with engine.connect() as connection:
                result = await connection.execute(
                    text("SELECT COUNT(*) FROM async_users")
                )
                eq_(result.scalar(), 1)

        self._run(main)

    def test_concurrent_connections(self):
        self._insert_users()

        async def main(engine):
            async def count():
                async with engine.connect() as connection:
                    result = await connection.execute(
                        text("SELECT COUNT(*) FROM async_users")
                    )
                    return result.scalar()

            eq_(await asyncio.gather(*(count() for _ in range(8))), [2] * 8)

        self._run(main)
