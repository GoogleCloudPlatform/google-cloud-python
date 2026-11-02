# Copyright 2026 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import async_snippets


@pytest.fixture(scope="module")
def database_ddl():
    """DDL statements to set up the database for testing async snippets."""
    return [
        """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)""",
        """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
    ]


@pytest.mark.asyncio
async def test_async_snippets_flow(capsys, instance_id, sample_database):
    # 1. Test Async Spanner Client Creation
    db = await async_snippets.async_create_client(
        instance_id, sample_database.database_id
    )
    assert db is not None
    out, _ = capsys.readouterr()
    assert "Async Spanner client instantiated successfully." in out

    # 2. Test Async DML Insert
    await async_snippets.async_insert_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Async DML Insert transaction complete." in out

    # 3. Seed additional albums data via sync batch write for query testing
    with sample_database.batch() as batch:
        batch.insert(
            table="Albums",
            columns=("SingerId", "AlbumId", "AlbumTitle"),
            values=[
                (12, 1, "Total Junk"),
                (13, 2, "Go, Go, Go"),
            ],
        )

    # 4. Test Async Query Data
    await async_snippets.async_query_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 12, AlbumId: 1, AlbumTitle: Total Junk" in out
    assert "SingerId: 13, AlbumId: 2, AlbumTitle: Go, Go, Go" in out

    # 5. Test Async Read-Write Transaction
    await async_snippets.async_read_write_transaction(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "Before Update - SingerId: 12, FirstName: Melissa, LastName: Garcia" in out
    assert "Async read-write transaction complete." in out

    # 6. Test Async Read-Only Transaction
    await async_snippets.async_read_only_transaction(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "Read Row - SingerId: 12, FirstName: Melissa, LastName: Jackson" in out
    assert "Read Row - SingerId: 13, FirstName: Russell, LastName: Morales" in out
