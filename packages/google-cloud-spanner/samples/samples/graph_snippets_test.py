# Copyright 2024 Google, Inc.
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

# import time
import uuid

from google.api_core import exceptions
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect
import pytest
from test_utils.retry import RetryErrors

import graph_snippets

retry_429 = RetryErrors(exceptions.ResourceExhausted, delay=15)

CREATE_TABLE_PERSON = """\
CREATE TABLE Person (
    id               INT64 NOT NULL,
    name             STRING(MAX),
    birthday         TIMESTAMP,
    country          STRING(MAX),
    city             STRING(MAX),
) PRIMARY KEY (id)
"""

CREATE_TABLE_ACCOUNT = """\
            CREATE TABLE Account (
            id               INT64 NOT NULL,
            create_time      TIMESTAMP,
            is_blocked       BOOL,
            nick_name        STRING(MAX),
        ) PRIMARY KEY (id)
"""

CREATE_TABLE_PERSON_OWN_ACCOUNT = """\
CREATE TABLE PersonOwnAccount (
            id               INT64 NOT NULL,
            account_id       INT64 NOT NULL,
            create_time      TIMESTAMP,
            FOREIGN KEY (account_id)
                REFERENCES Account (id)
        ) PRIMARY KEY (id, account_id),
        INTERLEAVE IN PARENT Person ON DELETE CASCADE
"""

CREATE_TABLE_ACCOUNT_TRANSFER_ACCOUNT = """\
CREATE TABLE AccountTransferAccount (
            id               INT64 NOT NULL,
            to_id            INT64 NOT NULL,
            amount           FLOAT64,
            create_time      TIMESTAMP NOT NULL,
            order_number     STRING(MAX),
            FOREIGN KEY (to_id) REFERENCES Account (id)
        ) PRIMARY KEY (id, to_id, create_time),
        INTERLEAVE IN PARENT Account ON DELETE CASCADE
"""

CREATE_PROPERTY_GRAPH = """
CREATE OR REPLACE PROPERTY GRAPH FinGraph
            NODE TABLES (Account, Person)
            EDGE TABLES (
                PersonOwnAccount
                    SOURCE KEY(id) REFERENCES Person(id)
                    DESTINATION KEY(account_id) REFERENCES Account(id)
                    LABEL Owns,
                AccountTransferAccount
                    SOURCE KEY(id) REFERENCES Account(id)
                    DESTINATION KEY(to_id) REFERENCES Account(id)
                    LABEL Transfers)
"""


@pytest.fixture(scope="module")
def database_dialect():
    """Spanner dialect to be used for this sample.

    The dialect is used to initialize the dialect for the database.
    It can either be GoogleStandardSql or PostgreSql.
    """
    return DatabaseDialect.GOOGLE_STANDARD_SQL


@pytest.fixture(scope="module")
def database_id():
    return f"test-db-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def create_database_id():
    return f"create-db-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def database_ddl():
    """Sequence of DDL statements used to set up the database.

    Sample testcase modules can override as needed.
    """
    return [
        CREATE_TABLE_PERSON,
        CREATE_TABLE_ACCOUNT,
        CREATE_TABLE_PERSON_OWN_ACCOUNT,
        CREATE_TABLE_ACCOUNT_TRANSFER_ACCOUNT,
        CREATE_PROPERTY_GRAPH,
    ]


def test_create_database_explicit(sample_instance, create_database_id):
    graph_snippets.create_database_with_property_graph(
        sample_instance.instance_id, create_database_id
    )
    database = sample_instance.database(create_database_id)
    database.drop()


@pytest.mark.dependency(name="insert_data")
def test_insert_data(capsys, instance_id, sample_database):
    graph_snippets.insert_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Inserted data" in out


@pytest.mark.dependency(depends=["insert_data"])
def test_query_data(capsys, instance_id, sample_database):
    graph_snippets.query_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert (
        "sender: Dana, receiver: Alex, amount: 500.0, transfer_at: 2020-10-04 16:55:05.120000+00:00"
        in out
    )
    assert (
        "sender: Lee, receiver: Dana, amount: 300.0, transfer_at: 2020-09-25 02:36:14.120000+00:00"
        in out
    )
    assert (
        "sender: Alex, receiver: Lee, amount: 300.0, transfer_at: 2020-08-29 15:28:58.120000+00:00"
        in out
    )
    assert (
        "sender: Alex, receiver: Lee, amount: 100.0, transfer_at: 2020-10-04 16:55:05.120000+00:00"
        in out
    )
    assert (
        "sender: Dana, receiver: Lee, amount: 200.0, transfer_at: 2020-10-17 03:59:40.120000+00:00"
        in out
    )


@pytest.mark.dependency(depends=["insert_data"])
def test_query_data_with_parameter(capsys, instance_id, sample_database):
    graph_snippets.query_data_with_parameter(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert (
        "sender: Dana, receiver: Alex, amount: 500.0, transfer_at: 2020-10-04 16:55:05.120000+00:00"
        in out
    )


@pytest.mark.dependency(name="insert_data_with_dml", depends=["insert_data"])
def test_insert_data_with_dml(capsys, instance_id, sample_database):
    graph_snippets.insert_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "2 record(s) inserted into Account." in out
    assert "2 record(s) inserted into AccountTransferAccount." in out


@pytest.mark.dependency(name="update_data_with_dml", depends=["insert_data_with_dml"])
def test_update_data_with_dml(capsys, instance_id, sample_database):
    graph_snippets.update_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 Account record(s) updated." in out
    assert "1 AccountTransferAccount record(s) updated." in out


@pytest.mark.dependency(depends=["update_data_with_dml"])
def test_update_data_with_graph_query_in_dml(capsys, instance_id, sample_database):
    graph_snippets.update_data_with_graph_query_in_dml(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "2 Account record(s) updated." in out


@pytest.mark.dependency(depends=["update_data_with_dml"])
def test_delete_data_with_graph_query_in_dml(capsys, instance_id, sample_database):
    graph_snippets.delete_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 AccountTransferAccount record(s) deleted." in out
    assert "1 Account record(s) deleted." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_delete_data(capsys, instance_id, sample_database):
    graph_snippets.delete_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Deleted data." in out
