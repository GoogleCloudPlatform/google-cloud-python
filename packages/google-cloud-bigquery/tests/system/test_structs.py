import datetime

import pytest

from google.cloud.bigquery.dbapi import connect

person_type = "struct<name string," " children array<struct<name string, bdate date>>>"
person_type_sized = (
    "struct<name string(22)," " children array<struct<name string(22), bdate date>>>"
)


@pytest.mark.parametrize("person_type_decl", [person_type, person_type_sized])
def test_structs(bigquery_client, dataset_id, person_type_decl, table_id):
    conn = connect(bigquery_client)
    cursor = conn.cursor()
    cursor.execute(f"create table {table_id} (person {person_type_decl})")
    data = dict(
        name="par",
        children=[
            dict(name="ch1", bdate=datetime.date(2021, 1, 1)),
            dict(name="ch2", bdate=datetime.date(2021, 1, 2)),
        ],
    )
    cursor.execute(
        f"insert into {table_id} (person) values (%(v:{person_type})s)",
        dict(v=data),
    )

    cursor.execute(f"select * from {table_id}")
    [[result]] = list(cursor)
    assert result == data
