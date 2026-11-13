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

import os
import uuid
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from google.api_core.exceptions import NotFound

from google.cloud import bigtable_admin_v2
from google.cloud.bigtable.data import BigtableDataClientAsync, SetCell

from ...utils import create_table_cm
from . import authorized_views_snippets_async

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_INSTANCE = os.environ["BIGTABLE_INSTANCE"]
TABLE_ID = f"authorized-views-async-{str(uuid.uuid4())[:16]}"
AUTHORIZED_VIEW_ID = f"view-{str(uuid.uuid4())[:16]}"


@pytest.fixture(scope="module")
def event_loop():
    import asyncio

    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="module")
async def table_id() -> AsyncGenerator[str, None]:
    with create_table_cm(
        PROJECT,
        BIGTABLE_INSTANCE,
        TABLE_ID,
        {"cf": None},
        verbose=False,
    ):
        yield TABLE_ID


@pytest_asyncio.fixture(scope="module")
async def authorized_view_id(table_id: str) -> AsyncGenerator[str, None]:
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        table_path = admin_client.table_path(PROJECT, BIGTABLE_INSTANCE, table_id)
        subset_view = bigtable_admin_v2.AuthorizedView.SubsetView(
            row_prefixes=[b""],
            family_subsets={
                "cf": bigtable_admin_v2.AuthorizedView.FamilySubsets(
                    qualifier_prefixes=[b""]
                )
            },
        )
        operation = await admin_client.create_authorized_view(
            parent=table_path,
            authorized_view_id=AUTHORIZED_VIEW_ID,
            authorized_view=bigtable_admin_v2.AuthorizedView(subset_view=subset_view),
        )
        await operation.result()

    async with BigtableDataClientAsync(project=PROJECT) as client:
        async with client.get_table(BIGTABLE_INSTANCE, table_id) as table:
            for i, name in enumerate(["World", "Bigtable", "Python"]):
                await table.mutate_row(
                    f"rowKey{i}",
                    [
                        SetCell("cf", "name", name),
                        SetCell("cf", "greeting", f"Hello {name}!"),
                    ],
                )

    yield AUTHORIZED_VIEW_ID


@pytest.mark.asyncio
async def test_create_authorized_view(capsys, table_id):
    view_id = f"view-create-{str(uuid.uuid4())[:12]}"
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        try:
            await authorized_views_snippets_async.create_authorized_view(
                PROJECT, BIGTABLE_INSTANCE, table_id, view_id
            )
            out, _ = capsys.readouterr()
            assert f"authorizedViews/{view_id} created successfully" in out
        finally:
            try:
                await admin_client.delete_authorized_view(
                    name=admin_client.authorized_view_path(
                        PROJECT, BIGTABLE_INSTANCE, table_id, view_id
                    )
                )
            except NotFound:
                pass


@pytest.mark.asyncio
async def test_update_authorized_view(capsys, table_id, authorized_view_id):
    await authorized_views_snippets_async.update_authorized_view(
        PROJECT, BIGTABLE_INSTANCE, table_id, authorized_view_id
    )
    out, _ = capsys.readouterr()
    assert f"authorizedViews/{authorized_view_id} updated successfully" in out


@pytest.mark.asyncio
async def test_get_authorized_view(capsys, table_id, authorized_view_id):
    await authorized_views_snippets_async.get_authorized_view(
        PROJECT, BIGTABLE_INSTANCE, table_id, authorized_view_id
    )
    out, _ = capsys.readouterr()
    assert "Row Prefix: " in out
    assert "Column Family: cf, Qualifier Prefix: " in out


@pytest.mark.asyncio
async def test_list_authorized_views(capsys, table_id, authorized_view_id):
    await authorized_views_snippets_async.list_authorized_views(
        PROJECT, BIGTABLE_INSTANCE, table_id
    )
    out, _ = capsys.readouterr()
    assert authorized_view_id in out.splitlines()


@pytest.mark.asyncio
async def test_delete_authorized_view(capsys, table_id):
    view_id = f"view-delete-{str(uuid.uuid4())[:12]}"
    async with bigtable_admin_v2.BigtableTableAdminAsyncClient() as admin_client:
        table_path = admin_client.table_path(PROJECT, BIGTABLE_INSTANCE, table_id)
        subset_view = bigtable_admin_v2.AuthorizedView.SubsetView(row_prefixes=[b""])
        operation = await admin_client.create_authorized_view(
            parent=table_path,
            authorized_view_id=view_id,
            authorized_view=bigtable_admin_v2.AuthorizedView(subset_view=subset_view),
        )
        await operation.result()

    await authorized_views_snippets_async.delete_authorized_view(
        PROJECT, BIGTABLE_INSTANCE, table_id, view_id
    )
    out, _ = capsys.readouterr()
    assert f"AuthorizedView: {view_id} deleted successfully" in out


@pytest.mark.asyncio
async def test_write_to_authorized_view(capsys, table_id, authorized_view_id):
    await authorized_views_snippets_async.write_to_authorized_view(
        PROJECT, BIGTABLE_INSTANCE, table_id, authorized_view_id
    )
    out, _ = capsys.readouterr()
    assert "Hello World!" in out
    assert "Hello Bigtable!" in out
    assert "Hello Python!" in out


@pytest.mark.asyncio
async def test_read_single_row_from_authorized_view(
    capsys, table_id, authorized_view_id
):
    await authorized_views_snippets_async.read_single_row_from_authorized_view(
        PROJECT, BIGTABLE_INSTANCE, table_id, authorized_view_id
    )
    out, _ = capsys.readouterr()
    assert "Row: rowKey0" in out
    assert "Family: cf    Qualifier: greeting    Value: Hello World!" in out


@pytest.mark.asyncio
async def test_read_rows_with_filter_from_authorized_view(
    capsys, table_id, authorized_view_id
):
    await authorized_views_snippets_async.read_rows_with_filter_from_authorized_view(
        PROJECT, BIGTABLE_INSTANCE, table_id, authorized_view_id
    )
    out, _ = capsys.readouterr()
    assert "Row Key: rowKey0" in out
    assert "Row Key: rowKey2" in out
