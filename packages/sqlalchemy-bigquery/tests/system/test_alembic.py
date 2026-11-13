# Copyright (c) 2021 The sqlalchemy-bigquery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import contextlib

import google.api_core.exceptions
import pytest
from google.cloud.bigquery import SchemaField, TimePartitioning
from sqlalchemy import Column, DateTime, Integer, Numeric, String

alembic = pytest.importorskip("alembic")


@pytest.fixture
def alembic_table(bigquery_dataset, bigquery_client):
    import alembic.migration
    import alembic.operations
    import sqlalchemy

    def get_table(table_name, data="table"):
        try:
            table_id = f"{bigquery_dataset}.{table_name}"
            if data == "rows":
                return [dict(r) for r in bigquery_client.list_rows(table_id)]
            else:
                table = bigquery_client.get_table(table_id)
                if data == "table":
                    return table
                elif data == "schema":
                    return table.schema
                else:
                    raise ValueError(data)
        except google.api_core.exceptions.NotFound:
            return None

    engine = sqlalchemy.create_engine(f"bigquery:///{bigquery_dataset}")
    with contextlib.closing(engine.connect()) as conn:
        migration_context = alembic.migration.MigrationContext.configure(conn, {})
        with alembic.operations.Operations.context(migration_context):
            yield get_table


def test_alembic_scenario(alembic_table):
    """
    Exercise all of the operations we support.

    It's a little awkward because we have to avoid doing too many
    operations on the same table to avoid tripping over limits on
    table mods within a short time.
    """
    from alembic import op

    from sqlalchemy_bigquery.base import SqlalchemyBigqueryImpl

    # Register the BigQuery Implementation to test the customized methods.
    op.implementation_for(SqlalchemyBigqueryImpl)

    assert alembic_table("account") is None

    account = op.create_table(
        "account",
        Column("id", Integer, nullable=False),
        Column("name", String(50), nullable=False, comment="The name"),
        Column("description", String(200)),
    )
    assert alembic_table("account", "schema") == [
        SchemaField("id", "INTEGER", "REQUIRED"),
        SchemaField("name", "STRING(50)", "REQUIRED", description="The name"),
        SchemaField("description", "STRING(200)"),
    ]

    op.bulk_insert(
        account,
        [
            dict(id=1, name="home", description="the home account"),
            dict(id=2, name="operations", description="the ops account"),
            dict(id=3, name="savings", description=None),
        ],
    )

    assert alembic_table("account", "rows") == [
        {"description": "the home account", "id": 1, "name": "home"},
        {"description": "the ops account", "id": 2, "name": "operations"},
        {"description": None, "id": 3, "name": "savings"},
    ]

    op.add_column(
        "account", Column("last_transaction_date", DateTime, comment="when updated")
    )

    # Tests customized visit_column_name()
    op.alter_column("account", "name", new_column_name="friendly_name")
    assert alembic_table("account", "schema") == [
        SchemaField("id", "INTEGER", "REQUIRED"),
        SchemaField("friendly_name", "STRING(50)", "REQUIRED", description="The name"),
        SchemaField("description", "STRING(200)"),
        SchemaField("last_transaction_date", "DATETIME", description="when updated"),
    ]

    op.create_table(
        "account_w_comment",
        Column("id", Integer, nullable=False),
        Column("name", String(50), nullable=False, comment="The name"),
        Column("description", String(200)),
        comment="This table has comments",
    )
    assert alembic_table("account_w_comment").description == "This table has comments"
    op.drop_table_comment("account_w_comment")
    assert alembic_table("account_w_comment").description is None

    op.drop_column("account_w_comment", "description")
    assert alembic_table("account_w_comment", "schema") == [
        SchemaField("id", "INTEGER", "REQUIRED"),
        SchemaField("name", "STRING(50)", "REQUIRED", description="The name"),
    ]

    op.drop_table("account_w_comment")
    assert alembic_table("account_w_comment") is None

    op.rename_table("account", "accounts")
    assert alembic_table("account") is None
    assert alembic_table("accounts", "schema") == [
        SchemaField("id", "INTEGER", "REQUIRED"),
        SchemaField("friendly_name", "STRING(50)", "REQUIRED", description="The name"),
        SchemaField("description", "STRING(200)"),
        SchemaField("last_transaction_date", "DATETIME", description="when updated"),
    ]
    op.drop_table("accounts")
    assert alembic_table("accounts") is None

    op.create_table(
        "transactions",
        Column("account", Integer, nullable=False),
        Column("transaction_time", DateTime(), nullable=False),
        Column("amount", Numeric(11, 2), nullable=False),
        bigquery_time_partitioning=TimePartitioning(field="transaction_time"),
    )

    op.alter_column("transactions", "amount", nullable=True)
    assert alembic_table("transactions", "schema") == [
        SchemaField("account", "INTEGER", "REQUIRED"),
        SchemaField("transaction_time", "DATETIME", "REQUIRED"),
        SchemaField("amount", "NUMERIC(11, 2)"),
    ]

    op.create_table_comment("transactions", "Transaction log")
    assert alembic_table("transactions").description == "Transaction log"

    op.drop_table("transactions")

    # Another thing we can do is alter the datatype of a nullable column,
    # if allowed by BigQuery's type coercion rules
    op.create_table("identifiers", Column("id", Integer))

    # Tests customized visit_column_type()
    op.alter_column("identifiers", "id", type_=Numeric)
    assert alembic_table("identifiers", "schema") == [SchemaField("id", "NUMERIC")]

    op.drop_table("identifiers")
