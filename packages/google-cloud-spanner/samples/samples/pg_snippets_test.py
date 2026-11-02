# Copyright 2022 Google, Inc.
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

import time
import uuid

from google.api_core import exceptions
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect
import pytest
from test_utils.retry import RetryErrors

import pg_snippets as snippets

CREATE_TABLE_SINGERS = """\
CREATE TABLE Singers (
    SingerId     BIGINT NOT NULL,
    FirstName    CHARACTER VARYING(1024),
    LastName     CHARACTER VARYING(1024),
    SingerInfo   BYTEA,
    FullName     CHARACTER VARYING(2048)
        GENERATED ALWAYS AS (FirstName || ' ' || LastName) STORED,
    PRIMARY KEY (SingerId)
)
"""

CREATE_TABLE_ALBUMS = """\
CREATE TABLE Albums (
    SingerId     BIGINT NOT NULL,
    AlbumId      BIGINT NOT NULL,
    AlbumTitle   CHARACTER VARYING(1024),
    PRIMARY KEY (SingerId, AlbumId)
    ) INTERLEAVE IN PARENT Singers ON DELETE CASCADE
"""

retry_429 = RetryErrors(exceptions.ResourceExhausted, delay=15)


@pytest.fixture(scope="module")
def database_dialect():
    """Spanner dialect to be used for this sample.

    The dialect is used to initialize the dialect for the database.
    It can either be GoogleStandardSql or PostgreSql.
    """
    return DatabaseDialect.POSTGRESQL


@pytest.fixture(scope="module")
def create_instance_id():
    """Id for the low-cost instance."""
    return f"create-instance-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def lci_instance_id():
    """Id for the low-cost instance."""
    return f"lci-instance-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def database_id():
    return f"test-db-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def create_database_id():
    return f"create-db-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def cmek_database_id():
    return f"cmek-db-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def default_leader_database_id():
    return f"leader_db_{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def database_ddl():
    """Sequence of DDL statements used to set up the database.

    Sample testcase modules can override as needed.
    """
    return [CREATE_TABLE_SINGERS, CREATE_TABLE_ALBUMS]


@pytest.fixture(scope="module")
def default_leader():
    """Default leader for multi-region instances."""
    return "us-east4"


def test_create_instance_explicit(spanner_client, create_instance_id):
    # Rather than re-use 'sample_isntance', we create a new instance, to
    # ensure that the 'create_instance' snippet is tested.
    retry_429(snippets.create_instance)(create_instance_id)
    instance = spanner_client.instance(create_instance_id)
    retry_429(instance.delete)()


def test_create_database_explicit(sample_instance, create_database_id):
    # Rather than re-use 'sample_database', we create a new database, to
    # ensure that the 'create_database' snippet is tested.
    snippets.create_database(sample_instance.instance_id, create_database_id)
    database = sample_instance.database(create_database_id)
    database.drop()


@pytest.mark.dependency(name="insert_data")
def test_insert_data(capsys, instance_id, sample_database):
    snippets.insert_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Inserted data" in out


@pytest.mark.dependency(depends=["insert_data"])
def test_delete_data(capsys, instance_id, sample_database):
    snippets.delete_data(instance_id, sample_database.database_id)
    # put it back for other tests
    snippets.insert_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Deleted data" in out


@pytest.mark.dependency(depends=["insert_data"])
def test_query_data(capsys, instance_id, sample_database):
    snippets.query_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk" in out


@pytest.mark.dependency(name="add_column", depends=["insert_data"])
def test_add_column(capsys, instance_id, sample_database):
    snippets.add_column(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Added the MarketingBudget column." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_read_data(capsys, instance_id, sample_database):
    snippets.read_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk" in out


@pytest.mark.dependency(name="update_data", depends=["add_column"])
def test_update_data(capsys, instance_id, sample_database):
    # Sleep for 15 seconds to ensure previous inserts will be
    # 'stale' by the time test_read_stale_data is run.
    time.sleep(15)

    snippets.update_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated data." in out


@pytest.mark.dependency(depends=["update_data"])
def test_read_stale_data(capsys, instance_id, sample_database):
    # This snippet relies on test_update_data inserting data
    # at least 15 seconds after the previous insert
    snippets.read_stale_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, MarketingBudget: None" in out


@pytest.mark.dependency(depends=["add_column"])
def test_read_write_transaction(capsys, instance_id, sample_database):
    snippets.read_write_transaction(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Transaction complete" in out


@pytest.mark.dependency(depends=["add_column"])
def test_query_data_with_new_column(capsys, instance_id, sample_database):
    snippets.query_data_with_new_column(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, MarketingBudget: 300000" in out
    assert "SingerId: 2, AlbumId: 2, MarketingBudget: 300000" in out


@pytest.mark.dependency(name="add_index", depends=["insert_data"])
def test_add_index(capsys, instance_id, sample_database):
    snippets.add_index(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Added the AlbumsByAlbumTitle index" in out


@pytest.mark.dependency(depends=["add_index"])
def test_read_data_with_index(capsys, instance_id, sample_database):
    snippets.read_data_with_index(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Go, Go, Go" in out
    assert "Forever Hold Your Peace" in out
    assert "Green" in out


@pytest.mark.dependency(name="add_storing_index", depends=["insert_data"])
def test_add_storing_index(capsys, instance_id, sample_database):
    snippets.add_storing_index(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Added the AlbumsByAlbumTitle2 index." in out


@pytest.mark.dependency(depends=["add_storing_index"])
def test_read_data_with_storing_index(capsys, instance_id, sample_database):
    snippets.read_data_with_storing_index(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "300000" in out


@pytest.mark.dependency(depends=["insert_data"])
def test_read_only_transaction(capsys, instance_id, sample_database):
    snippets.read_only_transaction(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    # Snippet does two reads, so entry should be listed twice
    assert out.count("SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk") == 2


@pytest.mark.dependency(name="add_timestamp_column", depends=["insert_data"])
def test_add_timestamp_column(capsys, instance_id, sample_database):
    snippets.add_timestamp_column(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert 'Altered table "Albums" on database ' in out


@pytest.mark.dependency(depends=["add_timestamp_column"])
def test_update_data_with_timestamp(capsys, instance_id, sample_database):
    snippets.update_data_with_timestamp(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated data" in out


@pytest.mark.dependency(depends=["add_timestamp_column"])
def test_query_data_with_timestamp(capsys, instance_id, sample_database):
    snippets.query_data_with_timestamp(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, MarketingBudget: 1000000" in out
    assert "SingerId: 2, AlbumId: 2, MarketingBudget: 750000" in out


@pytest.mark.dependency(name="create_table_with_timestamp")
def test_create_table_with_timestamp(capsys, instance_id, sample_database):
    snippets.create_table_with_timestamp(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Created Performances table on database" in out


@pytest.mark.dependency(depends=["create_table_with_timestamp"])
def test_insert_data_with_timestamp(capsys, instance_id, sample_database):
    snippets.insert_data_with_timestamp(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Inserted data." in out


@pytest.mark.dependency(name="insert_data_with_dml")
def test_insert_data_with_dml(capsys, instance_id, sample_database):
    snippets.insert_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_update_data_with_dml(capsys, instance_id, sample_database):
    snippets.update_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) updated." in out


@pytest.mark.dependency(depends=["add_column"])
def test_update_data_with_dml_returning(capsys, instance_id, sample_database):
    snippets.update_data_with_dml_returning(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) updated." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_delete_data_with_dml(capsys, instance_id, sample_database):
    snippets.delete_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) deleted." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_delete_data_with_dml_returning(capsys, instance_id, sample_database):
    snippets.delete_data_with_dml_returning(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) deleted." in out


@pytest.mark.dependency(name="dml_write_read_transaction")
def test_dml_write_read_transaction(capsys, instance_id, sample_database):
    snippets.dml_write_read_transaction(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out
    assert "FirstName: Timothy, LastName: Campbell" in out


@pytest.mark.dependency(name="insert_with_dml")
def test_insert_with_dml(capsys, instance_id, sample_database):
    snippets.insert_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "4 record(s) inserted" in out


@pytest.mark.dependency(name="insert_with_dml_returning")
def test_insert_with_dml_returning(capsys, instance_id, sample_database):
    snippets.insert_with_dml_returning(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "4 record(s) inserted" in out


@pytest.mark.dependency(depends=["insert_with_dml"])
def test_query_data_with_parameter(capsys, instance_id, sample_database):
    snippets.query_data_with_parameter(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 12, FirstName: Melissa, LastName: Garcia" in out


@pytest.mark.dependency(depends=["add_column"])
def test_write_with_dml_transaction(capsys, instance_id, sample_database):
    snippets.write_with_dml_transaction(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Transferred 200000 from Album2's budget to Album1's" in out


@pytest.mark.dependency(depends=["add_column"])
def update_data_with_partitioned_dml(capsys, instance_id, sample_database):
    snippets.update_data_with_partitioned_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "3 record(s) updated" in out


@pytest.mark.dependency(depends=["insert_with_dml", "insert_with_dml_returning"])
def test_delete_data_with_partitioned_dml(capsys, instance_id, sample_database):
    snippets.delete_data_with_partitioned_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "9 record(s) deleted" in out


@pytest.mark.dependency(depends=["add_column"])
def test_update_with_batch_dml(capsys, instance_id, sample_database):
    snippets.update_with_batch_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Executed 2 SQL statements using Batch DML." in out


def test_dml_last_statement_option(capsys, instance_id, sample_database):
    snippets.dml_last_statement_option(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out
    assert "1 record(s) updated." in out


@pytest.mark.dependency(name="create_table_with_datatypes")
def test_create_table_with_datatypes(capsys, instance_id, sample_database):
    snippets.create_table_with_datatypes(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Created Venues table on database" in out


@pytest.mark.dependency(
    name="insert_datatypes_data",
    depends=["create_table_with_datatypes"],
)
def test_insert_datatypes_data(capsys, instance_id, sample_database):
    snippets.insert_datatypes_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Inserted data." in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_bool(capsys, instance_id, sample_database):
    snippets.query_data_with_bool(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 19, VenueName: Venue 19, OutdoorVenue: True" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_bytes(capsys, instance_id, sample_database):
    snippets.query_data_with_bytes(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, VenueName: Venue 4" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_float(capsys, instance_id, sample_database):
    snippets.query_data_with_float(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, VenueName: Venue 4, PopularityScore: 0.8" in out
    assert "VenueId: 19, VenueName: Venue 19, PopularityScore: 0.9" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_int(capsys, instance_id, sample_database):
    snippets.query_data_with_int(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 19, VenueName: Venue 19, Capacity: 6300" in out
    assert "VenueId: 42, VenueName: Venue 42, Capacity: 3000" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_string(capsys, instance_id, sample_database):
    snippets.query_data_with_string(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 42, VenueName: Venue 42" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_update_data_with_numeric(capsys, instance_id, sample_database):
    snippets.update_data_with_numeric(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated data" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_numeric_parameter(capsys, instance_id, sample_database):
    snippets.query_data_with_numeric_parameter(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, Revenue: 35000" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_timestamp_parameter(capsys, instance_id, sample_database):
    snippets.query_data_with_timestamp_parameter(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "VenueId: 4, VenueName: Venue 4, LastUpdateTime:" in out
    assert "VenueId: 19, VenueName: Venue 19, LastUpdateTime:" in out
    assert "VenueId: 42, VenueName: Venue 42, LastUpdateTime:" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_query_data_with_query_options(capsys, instance_id, sample_database):
    snippets.query_data_with_query_options(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, VenueName: Venue 4, LastUpdateTime:" in out
    assert "VenueId: 19, VenueName: Venue 19, LastUpdateTime:" in out
    assert "VenueId: 42, VenueName: Venue 42, LastUpdateTime:" in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_create_client_with_query_options(capsys, instance_id, sample_database):
    snippets.create_client_with_query_options(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, VenueName: Venue 4, LastUpdateTime:" in out
    assert "VenueId: 19, VenueName: Venue 19, LastUpdateTime:" in out
    assert "VenueId: 42, VenueName: Venue 42, LastUpdateTime:" in out


@pytest.mark.dependency(name="add_jsonb_column", depends=["insert_datatypes_data"])
def test_add_jsonb_column(capsys, instance_id, sample_database):
    snippets.add_jsonb_column(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Waiting for operation to complete..." in out
    assert 'Altered table "Venues" on database ' in out


@pytest.mark.dependency(name="update_data_with_jsonb", depends=["add_jsonb_column"])
def test_update_data_with_jsonb(capsys, instance_id, sample_database):
    snippets.update_data_with_jsonb(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated data." in out


@pytest.mark.dependency(depends=["update_data_with_jsonb"])
def test_query_data_with_jsonb_parameter(capsys, instance_id, sample_database):
    snippets.query_data_with_jsonb_parameter(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 19, VenueDetails: {'open': True, 'rating': 9}" in out


def test_create_sequence(capsys, instance_id, bit_reverse_sequence_database):
    snippets.create_sequence(instance_id, bit_reverse_sequence_database.database_id)
    out, _ = capsys.readouterr()
    assert (
        "Created Seq sequence and Customers table, where the key column CustomerId uses the sequence as a default value on database"
        in out
    )
    assert "Number of customer records inserted is 3" in out
    assert "Inserted customer record with Customer Id:" in out


@pytest.mark.dependency(depends=["create_sequence"])
def test_alter_sequence(capsys, instance_id, bit_reverse_sequence_database):
    snippets.alter_sequence(instance_id, bit_reverse_sequence_database.database_id)
    out, _ = capsys.readouterr()
    assert (
        "Altered Seq sequence to skip an inclusive range between 1000 and 5000000 on database"
        in out
    )
    assert "Number of customer records inserted is 3" in out
    assert "Inserted customer record with Customer Id:" in out


@pytest.mark.dependency(depends=["alter_sequence"])
def test_drop_sequence(capsys, instance_id, bit_reverse_sequence_database):
    snippets.drop_sequence(instance_id, bit_reverse_sequence_database.database_id)
    out, _ = capsys.readouterr()
    assert (
        "Altered Customers table to drop DEFAULT from CustomerId column and dropped the Seq sequence on database"
        in out
    )
