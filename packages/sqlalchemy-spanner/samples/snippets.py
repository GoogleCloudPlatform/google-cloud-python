# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bs

"""
This application demonstrates how to do basic operations with Cloud
Spanner database.
For more information, see the README.md under /python-spanner-sqlalchemy.
"""

from sqlalchemy import (
    Column,
    Index,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    inspect,
)


# [START spanner_sqlalchemy_autocommit_on]
def enable_autocommit_mode(connection, url):
    """Enable AUTOCOMMIT mode."""
    level = connection.get_isolation_level()
    print("Connection default mode is {}.".format(level))

    connection.execution_options(isolation_level="AUTOCOMMIT")
    level = connection.get_isolation_level()
    print("Connection mode is now {}.".format(level))


# [END spanner_sqlalchemy_autocommit_on]


# [START spanner_sqlalchemy_create_table]
def create_table(url, table_id):
    """Create a table."""
    engine = create_engine(url)
    metadata = MetaData(bind=engine)

    table = Table(
        table_id,
        metadata,
        Column("user_id", Integer, primary_key=True),
        Column("user_name", String(16), nullable=False),
    )
    table.create()

    print("Table {} successfully created.".format(table.name))


# [END spanner_sqlalchemy_create_table]


# [START spanner_sqlalchemy_drop_table]
def drop_table(table):
    """Drop the table."""
    table.drop()

    print("Table {} successfully dropped.".format(table.name))


# [END spanner_sqlalchemy_drop_table]


# [START spanner_sqlalchemy_get_table_names]
def get_table_names(url):
    """Retrieve the list of the table names in the database.

    The table must already exist and can be created using
    `create_table.`
    """
    engine = create_engine(url)
    insp = inspect(engine)
    names = insp.get_table_names()

    print("Retrieved table names:")
    for name in names:
        print(name)


# [END spanner_sqlalchemy_get_table_names]


# [START spanner_sqlalchemy_create_unique_index]
def create_unique_index(table):
    """Create unique index.

    The table must already exist and can be created using
    `create_table.`
    """
    index = Index("some_index", table.c.user_name, unique=True)
    index.create()
    print("Index created.")


# [END spanner_sqlalchemy_create_unique_index]


# [START spanner_sqlalchemy_delete_all_rows]
def delete_all_rows(connection, table):
    """Delete all rows from the table.

    The table must already exist and can be created using
    `create_table.`
    """
    rows = connection.execute(table.select()).fetchall()
    print("Row count:", len(rows))

    connection.execute(table.delete())

    rows = connection.execute(table.select()).fetchall()
    print("Row count after deletion:", len(rows))


# [END spanner_sqlalchemy_delete_all_rows]


# [START spanner_sqlalchemy_delete_row]
def delete_row_with_where_clause(connection, table):
    """Delete a row.

    The table must already exist and can be created using
    `create_table.`
    """
    rows = connection.execute(table.select()).fetchall()
    print("Row count:", len(rows))

    connection.execute(table.delete().where(table.c.user_id == 1))

    rows = connection.execute(table.select()).fetchall()
    print("Row count after deletion:", len(rows))


# [END spanner_sqlalchemy_delete_row]


# [START spanner_sqlalchemy_table_exists]
def table_exists(table):
    """Check the table exists.

    The table must already exist and can be created using
    `create_table.`
    """
    result = table.exists()
    if result is True:
        print("Table exists.")


# [END spanner_sqlalchemy_table_exists]


# [START spanner_sqlalchemy_fetch_rows]
def fetch_rows(connection, table):
    """Fetch all rows from the table.

    The table must already exist and can be created using
    `create_table.`
    """
    rows = connection.execute(table.select()).fetchall()

    print("Fetched rows: ", rows)


# [END spanner_sqlalchemy_fetch_rows]


# [START spanner_sqlalchemy_fetch_row]
def fetch_row_with_where_clause(connection, table):
    """Fetch row with a WHERE clause.

    The table must already exist and can be created using
    `create_table.`
    """
    row = list(connection.execute(table.select().where(table.c.user_id == 1)))

    print("Fetched row: ", row)


# [END spanner_sqlalchemy_fetch_row]


# [START spanner_sqlalchemy_fetch_rows_with_limit_offset]
def fetch_rows_with_limit_offset(connection, table):
    """Fetch rows from the table with LIMIT and OFFSET clauses.

    The table must already exist and can be created using
    `create_table.`
    """
    rows = list(connection.execute(table.select().limit(2).offset(1)))

    print("Fetched rows: ", rows)


# [END spanner_sqlalchemy_fetch_rows_with_limit_offset]


# [START spanner_sqlalchemy_fetch_rows_with_order_by]
def fetch_rows_with_order_by(connection, table):
    """Fetch all rows ordered.

    The table must already exist and can be created using
    `create_table.`
    """
    rows = list(
        connection.execute(table.select().order_by(table.c.user_name)).fetchall()
    )
    print("Ordered rows: ", rows)


# [END spanner_sqlalchemy_fetch_rows_with_order_by]


# [START spanner_sqlalchemy_filter_data_startswith]
def filter_data_startswith(connection, table):
    """Filter data with STARTSWITH clause.

    The table must already exist and can be created using
    `create_table.`
    """
    rows = list(
        connection.execute(table.select().where(table.c.user_name.startswith("abcd%")))
    )
    print("Fetched rows: ", rows)


# [END spanner_sqlalchemy_filter_data_startswith]


# [START spanner_sqlalchemy_get_table_columns]
def get_table_columns(url, table):
    """Retrieve the list of columns of the table.

    The table must already exist and can be created using
    `create_table.`
    """
    engine = create_engine(url)
    insp = inspect(engine)
    columns = insp.get_columns(table.name)

    print("Fetched columns: ", columns)


# [END spanner_sqlalchemy_get_table_columns]


# [START spanner_sqlalchemy_get_foreign_key]
def get_table_foreign_key(url, table):
    """Retrieve a Foreign Key.

    The table must already exist and can be created using
    `create_table.`
    """
    engine = create_engine(url)
    insp = inspect(engine)
    f_keys = insp.get_foreign_keys(table.name)

    if f_keys:
        print("Fetched foreign keys: ", f_keys)


# [END spanner_sqlalchemy_get_foreign_key]


# [START spanner_sqlalchemy_get_indexes]
def get_table_indexes(url, table):
    """Retrieve the table indexes.

    The table must already exist and can be created using
    `create_table.`
    """
    engine = create_engine(url)
    insp = inspect(engine)
    indexes = insp.get_indexes(table.name)

    if indexes:
        print("Fetched indexes: ", indexes)


# [END spanner_sqlalchemy_get_indexes]


# [START spanner_sqlalchemy_get_primary_key]
def get_table_primary_key(url, table):
    """Retrieve the table Primary Key.

    The table must already exist and can be created using
    `create_table.`
    """
    engine = create_engine(url)
    insp = inspect(engine)
    p_key = insp.get_pk_constraint(table.name)

    if p_key:
        print("Fetched primary key: ", p_key)


# [END spanner_sqlalchemy_get_primary_key]


# [START spanner_sqlalchemy_insert_row]
def insert_row(connection, table):
    """Insert row into the table.

    The table must already exist and can be created using
    `create_table.`
    """
    connection.execute(table.insert(), {"user_id": 1, "user_name": "ABC"})

    row = list(connection.execute(table.select()))

    print("Inserted row: ", row)


# [END spanner_sqlalchemy_insert_row]


# [START spanner_sqlalchemy_update_row]
def update_row(connection, table):
    """Update a row in the table.

    The table must already exist and can be created using
    `create_table.`
    """
    connection.execute(
        table.update().where(table.c.user_id == 2).values(user_name="GEH")
    )
    row = list(connection.execute(table.select().where(table.c.user_id == 2)))

    print("Updated row: ", row)


# [END spanner_sqlalchemy_update_row]
