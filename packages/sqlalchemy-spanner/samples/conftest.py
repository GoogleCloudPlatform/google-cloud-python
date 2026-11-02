# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import configparser
import datetime
import os
import uuid

import pytest
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)


@pytest.fixture
def db_url():
    project = os.getenv(
        "GOOGLE_CLOUD_PROJECT",
        os.getenv("PROJECT_ID", "emulator-test-project"),
    )
    db_url = (
        f"spanner:///projects/{project}/instances/"
        "sqlalchemy-dialect-test/databases/compliance-test"
    )

    config = configparser.ConfigParser()
    if os.path.exists("test.cfg"):
        config.read("test.cfg")
    else:
        config.read("setup.cfg")
    return config.get("db", "default", fallback=db_url)


@pytest.fixture
def table_id():
    now = datetime.datetime.now()
    table_id = "example_table_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    return table_id


@pytest.fixture
def table(db_url, table_id):
    engine = create_engine(db_url)
    metadata = MetaData(bind=engine)

    table = Table(
        table_id,
        metadata,
        Column("user_id", Integer, primary_key=True),
        Column("user_name", String(16), nullable=False),
    )
    table.create()
    yield table
    table.drop()


@pytest.fixture
def table_w_foreign_key(db_url, table):
    engine = create_engine(db_url)
    metadata = MetaData(bind=engine)

    table_fk = Table(
        "table_fk",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(16), nullable=False),
        Column(
            table.name + "_user_id",
            Integer,
            ForeignKey(table.c.user_id, name=table.name + "user_id"),
        ),
    )
    table_fk.create()
    yield table_fk
    table_fk.drop()


@pytest.fixture
def connection(db_url):
    engine = create_engine(db_url)
    return engine.connect()


def insert_data(conn, table, data):
    conn.execute(table.insert(), data)
