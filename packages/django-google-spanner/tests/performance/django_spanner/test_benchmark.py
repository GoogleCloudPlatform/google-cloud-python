# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import random
import time
import unittest

import pandas as pd
import pytest
from django.db import connection
from google.api_core.exceptions import Aborted
from google.cloud import spanner_dbapi
from google.cloud.spanner_v1 import Client, KeySet

from tests.performance.django_spanner.models import Author
from tests.settings import DATABASE_NAME, INSTANCE_ID
from tests.system.django_spanner.utils import setup_database, setup_instance


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
            measures[function.__name__] = round(time.time() - t_start, 4)
        except Aborted:
            measures[function.__name__] = 0

    return wrapper


def insert_one_row(transaction, one_row):
    """A transaction-function for the original Spanner client.
    Inserts a single row into a database and then fetches it back.
    """
    transaction.execute_update(
        "INSERT Author (id, first_name, last_name, rating)  VALUES {}".format(
            str(one_row)
        )
    )
    last_name = transaction.execute_sql(
        "SELECT last_name FROM Author WHERE id=1"
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
            "INSERT Author (id, first_name, last_name, rating)  VALUES {}".format(
                str(row)
            )
        )
    _, count = transaction.batch_update(statements)
    if sum(count) != 99:
        raise ValueError("Wrong number of inserts: " + str(sum(count)))


class DjangoBenchmarkTest:
    """The Django performace testing class."""

    def __init__(self):
        with connection.schema_editor() as editor:
            # Create the tables
            editor.create_model(Author)

        self._many_rows = []
        self._many_rows2 = []
        for i in range(99):
            num = round(random.randint(0, 100000000))
            self._many_rows.append(Author(num, "Pete", "Allison", "2.1"))
            num2 = round(random.randint(0, 100000000))
            self._many_rows2.append(Author(num2, "Pete", "Allison", "2.1"))

    @measure_execution_time
    def insert_one_row_with_fetch_after(self):
        author_kent = Author(
            id=2,
            first_name="Pete",
            last_name="Allison",
            rating="2.1",
        )
        author_kent.save()
        last_name = Author.objects.get(pk=author_kent.id).last_name
        if last_name != "Allison":
            raise ValueError("Received invalid last name: " + last_name)

    @measure_execution_time
    def insert_many_rows(self):
        for row in self._many_rows:
            row.save()

    @measure_execution_time
    def insert_many_rows_with_mutations(self):
        Author.objects.bulk_create(self._many_rows2)

    @measure_execution_time
    def read_one_row(self):
        row = Author.objects.all().first()
        if row is None:
            raise ValueError("No rows read")

    @measure_execution_time
    def select_many_rows(self):
        rows = Author.objects.all()
        if len(rows) != 100:
            raise ValueError("Wrong number of rows read")

    def _cleanup(self):
        """Drop the test table."""
        with connection.schema_editor() as editor:
            # delete the table
            editor.delete_model(Author)

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


class SpannerBenchmarkTest:
    """The Spanner performace testing class."""

    def __init__(self):
        self._create_table()
        self._one_row = (
            1,
            "Pete",
            "Allison",
            "2.1",
        )
        self._client = Client()
        self._instance = self._client.instance(INSTANCE_ID)
        self._database = self._instance.database(DATABASE_NAME)

        self._many_rows = []
        self._many_rows2 = []
        for i in range(99):
            num = round(random.randint(0, 100000000))
            self._many_rows.append((num, "Pete", "Allison", "2.1"))
            num2 = round(random.randint(0, 100000000))
            self._many_rows2.append((num2, "Pete", "Allison", "2.1"))

        # initiate a session
        with self._database.snapshot():
            pass

    def _create_table(self):
        """Create a table for performace testing."""
        conn = spanner_dbapi.connect(INSTANCE_ID, DATABASE_NAME)
        conn.database.update_ddl(
            [
                """
CREATE TABLE Author (
    id INT64,
    first_name STRING(20),
    last_name STRING(20),
    rating STRING(50),
) PRIMARY KEY (id)
        """
            ]
        ).result(120)

        conn.close()

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
                table="Author",
                columns=("id", "first_name", "last_name", "rating"),
                values=self._many_rows2,
            )

    @measure_execution_time
    def read_one_row(self):
        with self._database.snapshot() as snapshot:
            keyset = KeySet(all_=True)
            snapshot.read(
                table="Author",
                columns=("id", "first_name", "last_name", "rating"),
                keyset=keyset,
            ).one()

    @measure_execution_time
    def select_many_rows(self):
        with self._database.snapshot() as snapshot:
            rows = list(snapshot.execute_sql("SELECT * FROM Author ORDER BY last_name"))
            if len(rows) != 100:
                raise ValueError("Wrong number of rows read")

    def _cleanup(self):
        """Drop the test table."""
        conn = spanner_dbapi.connect(INSTANCE_ID, DATABASE_NAME)
        conn.database.update_ddl(["DROP TABLE Author"])
        conn.close()

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


@pytest.mark.django_db()
class BenchmarkTest(unittest.TestCase):
    def setUp(self):
        setup_instance()
        setup_database()

    def test_run(self):
        django_obj = pd.DataFrame(
            columns=[
                "insert_one_row_with_fetch_after",
                "read_one_row",
                "insert_many_rows",
                "select_many_rows",
                "insert_many_rows_with_mutations",
            ]
        )
        spanner_obj = pd.DataFrame(
            columns=[
                "insert_one_row_with_fetch_after",
                "read_one_row",
                "insert_many_rows",
                "select_many_rows",
                "insert_many_rows_with_mutations",
            ]
        )

        for _ in range(50):
            django_obj = django_obj.append(
                DjangoBenchmarkTest().run(), ignore_index=True
            )
            spanner_obj = spanner_obj.append(
                SpannerBenchmarkTest().run(), ignore_index=True
            )

        avg = pd.concat([django_obj.mean(axis=0), spanner_obj.mean(axis=0)], axis=1)
        avg.columns = ["Django", "Spanner"]
        std = pd.concat([django_obj.std(axis=0), spanner_obj.std(axis=0)], axis=1)
        std.columns = ["Django", "Spanner"]
        err = pd.concat([django_obj.sem(axis=0), spanner_obj.sem(axis=0)], axis=1)
        err.columns = ["Django", "Spanner"]

        print(
            "Average: ",
            avg,
            "Standard Deviation: ",
            std,
            "Error:",
            err,
            sep="\n",
        )
