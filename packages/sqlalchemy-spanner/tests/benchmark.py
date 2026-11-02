# Copyright 2021 Google LLC
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

"""
A test suite to check Spanner dialect for SQLAlchemy performance
in comparison with the original Spanner client.
"""

import base64
import datetime
import random
import statistics
import time

from google.api_core.exceptions import Aborted, NotFound
from google.cloud.spanner_v1 import Client, KeySet
from scipy.stats import sem
from sqlalchemy import (
    MetaData,
    Table,
    create_engine,
    insert,
    select,
    text,
)

from google.cloud import spanner, spanner_dbapi

PROJECT = "project-id"
INSTANCE = "instance-id"
DATABASE = "database-id"


def measure_execution_time(function):
    """Decorator to measure a wrapped method execution time."""

    def wrapper(self, measures):
        """Execute the wrapped method and measure its execution time.

        Args:
            measures (dict): Test cases and their execution time.
        """
        t_start = time.time()
        try:
            function(self)
            measures[function.__name__] = round(time.time() - t_start, 2)
        except Aborted:
            measures[function.__name__] = 0

    return wrapper


class BenchmarkTestBase:
    """Base class for performance testing.

    Organizes testing data preparation and cleanup.
    """

    _many_rows_ids = []
    _many_rows2_ids = []

    def __init__(self):
        self._cleanup()
        self._create_table()

        self._one_row = {
            "id": 1,
            "first_name": "Pete",
            "last_name": "Allison",
            "birth_date": datetime.date(1998, 10, 6),
            "picture": b"123",
        }
        self.keys = set([1])
        if not self._many_rows_ids:
            for i in range(99):
                self._many_rows_ids.append(self._generate_id())
                self._many_rows2_ids.append(self._generate_id())

    def _cleanup(self):
        """Drop the test table."""
        conn = spanner_dbapi.connect(INSTANCE, DATABASE)
        try:
            conn.database.update_ddl(["DROP TABLE Singers"])
        except NotFound:
            pass
        conn.close()

    def _create_table(self):
        """Create a table for performace testing."""
        conn = spanner_dbapi.connect(INSTANCE, DATABASE)
        try:
            conn.database.update_ddl(["DROP TABLE Singers"])
        except NotFound:
            pass
        conn.database.update_ddl(
            [
                """
CREATE TABLE Singers (
    id INT64,
    first_name STRING(1024),
    last_name STRING(1024),
    birth_date DATE,
    picture BYTES(1024),
) PRIMARY KEY (id)
        """
            ]
        ).result()

        conn.close()

    def _generate_id(self):
        num = 1
        while num in self.keys:
            num = round(random.random() * 1000000)
        self.keys.add(num)
        return num

    def run(self):
        """Execute every test case."""
        measures = {}
        for method in (
            self.insert_one_row_with_fetch_after,
            self.read_one_row,
            self.insert_many_rows,
            self.select_many_rows,
            self.insert_many_rows_with_mutations,
        ):
            method(measures)

        self._cleanup()
        return measures


class SpannerBenchmarkTest(BenchmarkTestBase):
    """The original Spanner performance testing class."""

    def __init__(self):
        super().__init__()
        self._client = Client()
        self._instance = self._client.instance(INSTANCE)
        self._database = self._instance.database(DATABASE)

        self._many_rows = []
        self._many_rows2 = []
        birth_date = datetime.date(1998, 10, 6)
        picture = base64.b64encode("123".encode())
        for num in self._many_rows_ids:
            self._many_rows.append(
                {
                    "id": num,
                    "first_name": "Pete",
                    "last_name": "Allison",
                    "birth_date": birth_date,
                    "picture": picture,
                }
            )
        for num in self._many_rows2_ids:
            self._many_rows2.append((num, "Pete", "Allison", birth_date, picture))

        # initiate a session
        with self._database.snapshot():
            pass

    @measure_execution_time
    def insert_one_row_with_fetch_after(self):
        self._database.run_in_transaction(insert_one_row, self._one_row)

    @measure_execution_time
    def insert_many_rows(self):
        self._database.run_in_transaction(insert_many_rows, self._many_rows)

    @measure_execution_time
    def insert_many_rows_with_mutations(self):
        with self._database.batch() as batch:
            batch.insert(
                table="Singers",
                columns=("id", "first_name", "last_name", "birth_date", "picture"),
                values=self._many_rows2,
            )

    @measure_execution_time
    def read_one_row(self):
        with self._database.snapshot() as snapshot:
            keyset = KeySet(all_=True)
            snapshot.read(
                table="Singers",
                columns=("id", "first_name", "last_name", "birth_date", "picture"),
                keyset=keyset,
            ).one()

    @measure_execution_time
    def select_many_rows(self):
        with self._database.snapshot() as snapshot:
            rows = list(
                snapshot.execute_sql("SELECT * FROM Singers ORDER BY last_name")
            )
            if len(rows) != 100:
                raise ValueError("Wrong number of rows read")


class SQLAlchemyBenchmarkTest(BenchmarkTestBase):
    """Spanner dialect for SQLAlchemy performance testing class."""

    def __init__(self):
        super().__init__()
        self._engine = create_engine(
            "spanner:///projects/{project}/instances/{instance}/databases/{db}".format(
                project=PROJECT,
                instance=INSTANCE,
                db=DATABASE,
            )
        )
        metadata = MetaData(bind=self._engine)
        self._table = Table("Singers", metadata, autoload=True)

        self._conn = self._engine.connect()

        self._many_rows = []
        self._many_rows2 = []
        birth_date = datetime.date(1998, 10, 6)
        for num in self._many_rows_ids:
            self._many_rows.append(
                {
                    "id": num,
                    "first_name": "Pete",
                    "last_name": "Allison",
                    "birth_date": birth_date,
                    "picture": b"123",
                }
            )
        for num in self._many_rows2_ids:
            self._many_rows2.append(
                {
                    "id": num,
                    "first_name": "Pete",
                    "last_name": "Allison",
                    "birth_date": birth_date,
                    "picture": b"123",
                }
            )

    @measure_execution_time
    def insert_one_row_with_fetch_after(self):
        self._conn.execute(insert(self._table).values(self._one_row))
        last_name = self._conn.execute(
            select([text("last_name")], from_obj=self._table)
        ).fetchone()[0]
        if last_name != "Allison":
            raise ValueError("Received invalid last name: " + last_name)

    @measure_execution_time
    def insert_many_rows(self):
        self._conn.execute(
            self._table.insert(),
            self._many_rows,
        )

    @measure_execution_time
    def insert_many_rows_with_mutations(self):
        self._conn.execute(
            self._table.insert(),
            self._many_rows2,
        )

    @measure_execution_time
    def read_one_row(self):
        row = self._conn.execute(select(["*"], from_obj=self._table)).fetchone()
        if not row:
            raise ValueError("No rows read")

    @measure_execution_time
    def select_many_rows(self):
        rows = self._conn.execute(select(["*"], from_obj=self._table)).fetchall()
        if len(rows) != 100:
            raise ValueError("Wrong number of rows read")


def insert_one_row(transaction, one_row):
    """A transaction-function for the original Spanner client.

    Inserts a single row into a database and then fetches it back.
    """
    transaction.execute_update(
        "INSERT INTO `Singers` (id, first_name, last_name, birth_date, picture)"
        " VALUES (@id, @first_name, @last_name, @birth_date, @picture)",
        params=one_row,
        param_types={
            "id": spanner.param_types.INT64,
            "first_name": spanner.param_types.STRING,
            "last_name": spanner.param_types.STRING,
            "birth_date": spanner.param_types.DATE,
            "picture": spanner.param_types.BYTES,
        },
    )
    last_name = transaction.execute_sql(
        "SELECT last_name FROM Singers WHERE id=1"
    ).one()[0]
    if last_name != "Allison":
        raise ValueError("Received invalid last name: " + last_name)


def insert_many_rows(transaction, many_rows):
    """A transaction-function for the original Spanner client.

    Insert 100 rows into a database.
    """
    statements = []
    for row in many_rows:
        statements.append(
            (
                "INSERT INTO `Singers` (id, first_name, last_name, birth_date, picture)"
                " VALUES (@id, @first_name, @last_name, @birth_date, @picture)",
                row,
                {
                    "id": spanner.param_types.INT64,
                    "first_name": spanner.param_types.STRING,
                    "last_name": spanner.param_types.STRING,
                    "birth_date": spanner.param_types.DATE,
                    "picture": spanner.param_types.BYTES,
                },
            )
        )
    _, count = transaction.batch_update(statements)
    if sum(count) != 99:
        raise ValueError("Wrong number of inserts: " + str(sum(count)))


def compare_measurements(spanner, alchemy):
    """
    Compare the original Spanner client performance measures
    with Spanner dialect for SQLAlchemy ones.
    """
    comparison = {}
    for key in spanner.keys():
        comparison[key] = {
            "Spanner, sec": spanner[key],
            "SQLAlchemy, sec": alchemy[key],
            "SQLAlchemy deviation": round(alchemy[key] - spanner[key], 2),
            "SQLAlchemy to Spanner, %": round(alchemy[key] / spanner[key] * 100),
        }
    return comparison


measures = []
for _ in range(50):
    spanner_measures = SpannerBenchmarkTest().run()
    alchemy_measures = SQLAlchemyBenchmarkTest().run()
    measures.append((spanner_measures, alchemy_measures))

agg = {"spanner": {}, "alchemy": {}}

for span, alch in measures:
    for key, value in span.items():
        agg["spanner"].setdefault(key, []).append(value)
        agg["alchemy"].setdefault(key, []).append(alch[key])

spanner_stats = {}
for key, value in agg["spanner"].items():
    while 0 in value:
        value.remove(0)
    spanner_stats[key + "_aver"] = round(statistics.mean(value), 2)
    spanner_stats[key + "_error"] = round(sem(value), 2)
    spanner_stats[key + "_std_dev"] = round(statistics.pstdev(value), 2)

alchemy_stats = {}
for key, value in agg["alchemy"].items():
    while 0 in value:
        value.remove(0)
    alchemy_stats[key + "_aver"] = round(statistics.mean(value), 2)
    alchemy_stats[key + "_error"] = round(sem(value), 2)
    alchemy_stats[key + "_std_dev"] = round(statistics.pstdev(value), 2)

for key in spanner_stats:
    print(key + ":")
    print("spanner: ", spanner_stats[key])
    print("alchemy: ", alchemy_stats[key])
