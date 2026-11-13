# Copyright 2016 Google, Inc.
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
from google.cloud import spanner
from google.cloud.spanner_admin_database_v1.types.common import DatabaseDialect
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
import pytest
from test_utils.retry import RetryErrors

import snippets

CREATE_TABLE_SINGERS = """\
CREATE TABLE Singers (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX),
    FullName     STRING(2048) AS (
        ARRAY_TO_STRING([FirstName, LastName], " ")
    ) STORED
) PRIMARY KEY (SingerId)
"""

CREATE_TABLE_ALBUMS = """\
CREATE TABLE Albums (
    SingerId     INT64 NOT NULL,
    AlbumId      INT64 NOT NULL,
    AlbumTitle   STRING(MAX)
) PRIMARY KEY (SingerId, AlbumId),
INTERLEAVE IN PARENT Singers ON DELETE CASCADE
"""

CREATE_TABLE_SINGERS_ = """\
CREATE TABLE Singers (
    SingerId         INT64 NOT NULL,
    FirstName        STRING(1024),
    LastName         STRING(1024),
    ) PRIMARY KEY (SingerId)
"""

retry_429 = RetryErrors(exceptions.ResourceExhausted, delay=15)


@pytest.fixture(scope="module")
def database_dialect():
    """Spanner dialect to be used for this sample.

    The dialect is used to initialize the dialect for the database.
    It can either be GoogleStandardSql or PostgreSql.
    """
    return DatabaseDialect.GOOGLE_STANDARD_SQL


@pytest.fixture(scope="module")
def create_instance_id():
    """Id for the low-cost instance."""
    return f"create-instance-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def lci_instance_id():
    """Id for the low-cost instance."""
    return f"lci-instance-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def instance_partition_instance_id():
    """Id for the instance that tests instance partitions."""
    return f"instance-partition-test-{uuid.uuid4().hex[:10]}"


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
def proto_columns_database_id():
    return f"test-db-proto-{uuid.uuid4().hex[:10]}"


@pytest.fixture(scope="module")
def database_ddl():
    """Sequence of DDL statements used to set up the database.

    Sample testcase modules can override as needed.
    """
    return [CREATE_TABLE_SINGERS, CREATE_TABLE_ALBUMS]


@pytest.fixture(scope="module")
def proto_columns_database_ddl():
    """Sequence of DDL statements used to set up the database for proto columns.

    Sample testcase modules can override as needed.
    """
    return [CREATE_TABLE_SINGERS_, CREATE_TABLE_ALBUMS]


@pytest.fixture(scope="module")
def default_leader():
    """Default leader for multi-region instances."""
    return "us-east4"


@pytest.fixture(scope="module")
def user_managed_instance_config_name(spanner_client):
    name = f"custom-python-samples-config-{uuid.uuid4().hex[:10]}"
    yield name
    snippets.delete_instance_config(
        "{}/instanceConfigs/{}".format(spanner_client.project_name, name)
    )
    return


@pytest.fixture(scope="module")
def base_instance_config_id(spanner_client):
    return "{}/instanceConfigs/{}".format(spanner_client.project_name, "nam7")


def test_create_and_update_instance_explicit(spanner_client, create_instance_id):
    # Rather than re-use 'sample_isntance', we create a new instance, to
    # ensure that the 'create_instance' snippet is tested.
    retry_429(snippets.create_instance)(create_instance_id)
    # Rather than re-use 'sample_isntance', we are using created instance, to
    # ensure that the 'update_instance' snippet is tested.
    retry_429(snippets.update_instance)(create_instance_id)
    instance = spanner_client.instance(create_instance_id)
    retry_429(instance.delete)()


def test_create_database_explicit(sample_instance, create_database_id):
    # Rather than re-use 'sample_database', we create a new database, to
    # ensure that the 'create_database' snippet is tested.
    snippets.create_database(sample_instance.instance_id, create_database_id)
    database = sample_instance.database(create_database_id)
    database.drop()


def test_create_instance_with_processing_units(capsys, lci_instance_id):
    processing_units = 500
    retry_429(snippets.create_instance_with_processing_units)(
        lci_instance_id,
        processing_units,
    )
    out, _ = capsys.readouterr()
    assert lci_instance_id in out
    assert "{} processing units".format(processing_units) in out
    spanner_client = spanner.Client()
    instance = spanner_client.instance(lci_instance_id)
    retry_429(instance.delete)()


def test_create_instance_with_autoscaling_config(capsys, lci_instance_id):
    retry_429(snippets.create_instance_with_autoscaling_config)(
        lci_instance_id,
    )
    out, _ = capsys.readouterr()
    assert lci_instance_id in out
    assert "autoscaling config" in out
    spanner_client = spanner.Client()
    instance = spanner_client.instance(lci_instance_id)
    retry_429(instance.delete)()


def test_create_and_update_instance_default_backup_schedule_type(
    capsys, lci_instance_id
):
    retry_429(snippets.create_instance_without_default_backup_schedules)(
        lci_instance_id,
    )
    create_out, _ = capsys.readouterr()
    assert lci_instance_id in create_out
    assert "without default backup schedules" in create_out

    retry_429(snippets.update_instance_default_backup_schedule_type)(
        lci_instance_id,
    )
    update_out, _ = capsys.readouterr()
    assert lci_instance_id in update_out
    assert "to have default backup schedules" in update_out
    spanner_client = spanner.Client()
    instance = spanner_client.instance(lci_instance_id)
    retry_429(instance.delete)()


def test_create_instance_partition(capsys, instance_partition_instance_id):
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_partition_instance_id)
    try:
        request = spanner_instance_admin.CreateInstanceRequest(
            parent=spanner_client.project_name,
            instance_id=instance_partition_instance_id,
            instance=spanner_instance_admin.Instance(
                config=f"{spanner_client.project_name}/instanceConfigs/nam6",
                display_name="Partition test instance",
                node_count=1,
                edition=spanner_instance_admin.Instance.Edition.ENTERPRISE_PLUS,
            ),
        )
        operation = retry_429(spanner_client.instance_admin_api.create_instance)(
            request=request
        )
        operation.result(900)

        retry_429(snippets.create_instance_partition)(
            instance_partition_instance_id, "my-instance-partition"
        )
        out, _ = capsys.readouterr()
        assert "Created instance partition my-instance-partition" in out
    finally:
        try:
            retry_429(instance.delete)()
        except Exception:
            pass


def test_update_database(capsys, instance_id, sample_database):
    snippets.update_database(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated database {}.".format(sample_database.name) in out

    # Cleanup
    sample_database.enable_drop_protection = False
    op = sample_database.update(["enable_drop_protection"])
    op.result()


def test_create_database_with_encryption_config(
    capsys, instance_id, cmek_database_id, kms_key_name
):
    snippets.create_database_with_encryption_key(
        instance_id, cmek_database_id, kms_key_name
    )
    out, _ = capsys.readouterr()
    assert cmek_database_id in out
    assert kms_key_name in out


@pytest.mark.skip(reason="skipped since the KMS keys are not added on test project")
def test_create_database_with_multiple_kms_keys(
    capsys,
    multi_region_instance,
    multi_region_instance_id,
    cmek_database_id,
    kms_key_names,
):
    snippets.create_database_with_multiple_kms_keys(
        multi_region_instance_id, cmek_database_id, kms_key_names
    )
    out, _ = capsys.readouterr()
    assert cmek_database_id in out
    assert kms_key_names[0] in out
    assert kms_key_names[1] in out
    assert kms_key_names[2] in out


def test_get_instance_config(capsys):
    instance_config = "nam6"
    snippets.get_instance_config(instance_config)
    out, _ = capsys.readouterr()
    assert instance_config in out


def test_list_instance_config(capsys):
    snippets.list_instance_config()
    out, _ = capsys.readouterr()
    assert "regional-us-central1" in out


@pytest.mark.dependency(name="create_instance_config")
def test_create_instance_config(
    capsys, user_managed_instance_config_name, base_instance_config_id
):
    snippets.create_instance_config(
        user_managed_instance_config_name, base_instance_config_id
    )
    out, _ = capsys.readouterr()
    assert "Created instance configuration" in out


@pytest.mark.dependency(depends=["create_instance_config"])
def test_update_instance_config(capsys, user_managed_instance_config_name):
    snippets.update_instance_config(user_managed_instance_config_name)
    out, _ = capsys.readouterr()
    assert "Updated instance configuration" in out


@pytest.mark.dependency(depends=["create_instance_config"])
def test_delete_instance_config(capsys, user_managed_instance_config_name):
    spanner_client = spanner.Client()
    snippets.delete_instance_config(
        "{}/instanceConfigs/{}".format(
            spanner_client.project_name, user_managed_instance_config_name
        )
    )
    out, _ = capsys.readouterr()
    assert "successfully deleted" in out


def test_list_instance_config_operations(capsys):
    snippets.list_instance_config_operations()
    out, _ = capsys.readouterr()
    assert "List instance config operations" in out


def test_list_databases(capsys, instance_id):
    snippets.list_databases(instance_id)
    out, _ = capsys.readouterr()
    assert "has default leader" in out


def test_create_database_with_default_leader(
    capsys,
    multi_region_instance,
    multi_region_instance_id,
    default_leader_database_id,
    default_leader,
):
    retry_429 = RetryErrors(exceptions.ResourceExhausted, delay=15)
    retry_429(snippets.create_database_with_default_leader)(
        multi_region_instance_id, default_leader_database_id, default_leader
    )
    out, _ = capsys.readouterr()
    assert default_leader_database_id in out
    assert default_leader in out


def test_update_database_with_default_leader(
    capsys,
    multi_region_instance,
    multi_region_instance_id,
    default_leader_database_id,
    default_leader,
):
    retry_429 = RetryErrors(exceptions.ResourceExhausted, delay=15)
    retry_429(snippets.update_database_with_default_leader)(
        multi_region_instance_id, default_leader_database_id, default_leader
    )
    out, _ = capsys.readouterr()
    assert default_leader_database_id in out
    assert default_leader in out


def test_get_database_ddl(capsys, instance_id, sample_database):
    snippets.get_database_ddl(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert sample_database.database_id in out


def test_query_information_schema_database_options(
    capsys,
    multi_region_instance,
    multi_region_instance_id,
    default_leader_database_id,
    default_leader,
):
    snippets.query_information_schema_database_options(
        multi_region_instance_id, default_leader_database_id
    )
    out, _ = capsys.readouterr()
    assert default_leader in out


@pytest.mark.dependency(name="insert_data")
def test_insert_data(capsys, instance_id, sample_database):
    snippets.insert_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Inserted data" in out


@pytest.mark.dependency(name="batch_write")
def test_batch_write(capsys, instance_id, sample_database):
    snippets.batch_write(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "could not be applied with error" not in out


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
def test_query_data_with_index(capsys, instance_id, sample_database):
    snippets.query_data_with_index(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Go, Go, Go" in out
    assert "Forever Hold Your Peace" in out
    assert "Green" not in out


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


@pytest.mark.dependency(name="write_struct_data")
def test_write_struct_data(capsys, instance_id, sample_database):
    snippets.write_struct_data(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Inserted sample data for STRUCT queries" in out


@pytest.mark.dependency(depends=["write_struct_data"])
def test_query_with_struct(capsys, instance_id, sample_database):
    snippets.query_with_struct(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 6" in out


@pytest.mark.dependency(depends=["write_struct_data"])
def test_query_with_array_of_struct(capsys, instance_id, sample_database):
    snippets.query_with_array_of_struct(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 8" in out
    assert "SingerId: 7" in out
    assert "SingerId: 6" in out


@pytest.mark.dependency(depends=["write_struct_data"])
def test_query_struct_field(capsys, instance_id, sample_database):
    snippets.query_struct_field(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 6" in out


@pytest.mark.dependency(depends=["write_struct_data"])
def test_query_nested_struct_field(capsys, instance_id, sample_database):
    snippets.query_nested_struct_field(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 6 SongName: Imagination" in out
    assert "SingerId: 9 SongName: Imagination" in out


@pytest.mark.dependency(name="insert_data_with_dml")
def test_insert_data_with_dml(capsys, instance_id, sample_database):
    snippets.insert_data_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out


@pytest.mark.dependency(name="log_commit_stats")
def test_log_commit_stats(capsys, instance_id, sample_database):
    snippets.log_commit_stats(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out
    # SingerId, FirstName, and LastName plus FullName which is generated.
    assert "4 mutation(s) in transaction." in out


@pytest.mark.dependency(name="set_max_commit_delay")
def test_set_max_commit_delay(capsys, instance_id, sample_database):
    snippets.set_max_commit_delay(instance_id, sample_database.database_id)
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


@pytest.mark.dependency(depends=["add_timestamp_column"])
def test_update_data_with_dml_timestamp(capsys, instance_id, sample_database):
    snippets.update_data_with_dml_timestamp(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "2 record(s) updated." in out


@pytest.mark.dependency(name="dml_write_read_transaction")
def test_dml_write_read_transaction(capsys, instance_id, sample_database):
    snippets.dml_write_read_transaction(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out
    assert "FirstName: Timothy, LastName: Campbell" in out


@pytest.mark.dependency(depends=["dml_write_read_transaction"])
def test_update_data_with_dml_struct(capsys, instance_id, sample_database):
    snippets.update_data_with_dml_struct(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) updated" in out


@pytest.mark.dependency(name="insert_with_dml")
def test_insert_with_dml(capsys, instance_id, sample_database):
    snippets.insert_with_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "4 record(s) inserted" in out


@pytest.mark.dependency(depends=[""])
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
def test_update_data_with_partitioned_dml(capsys, instance_id, sample_database):
    snippets.update_data_with_partitioned_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "3 records updated" in out


@pytest.mark.dependency(
    depends=[
        "insert_with_dml",
        "dml_write_read_transaction",
        "log_commit_stats",
        "set_max_commit_delay",
    ]
)
def test_delete_data_with_partitioned_dml(capsys, instance_id, sample_database):
    snippets.delete_data_with_partitioned_dml(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "7 record(s) deleted" in out


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
def test_query_data_with_array(capsys, instance_id, sample_database):
    snippets.query_data_with_array(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 19, VenueName: Venue 19, AvailableDate: 2020-11-01" in out
    assert "VenueId: 42, VenueName: Venue 42, AvailableDate: 2020-10-01" in out


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
def test_query_data_with_date(capsys, instance_id, sample_database):
    snippets.query_data_with_date(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, VenueName: Venue 4, LastContactDate: 2018-09-02" in out
    assert "VenueId: 42, VenueName: Venue 42, LastContactDate: 2018-10-01" in out


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


@pytest.mark.dependency(
    name="add_numeric_column",
    depends=["create_table_with_datatypes"],
)
def test_add_numeric_column(capsys, instance_id, sample_database):
    snippets.add_numeric_column(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert 'Altered table "Venues" on database ' in out


@pytest.mark.dependency(depends=["add_numeric_column", "insert_datatypes_data"])
def test_update_data_with_numeric(capsys, instance_id, sample_database):
    snippets.update_data_with_numeric(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated data" in out


@pytest.mark.dependency(depends=["add_numeric_column"])
def test_query_data_with_numeric_parameter(capsys, instance_id, sample_database):
    snippets.query_data_with_numeric_parameter(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 4, Revenue: 35000" in out


@pytest.mark.dependency(
    name="add_json_column",
    depends=["create_table_with_datatypes"],
)
def test_add_json_column(capsys, instance_id, sample_database):
    snippets.add_json_column(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert 'Altered table "Venues" on database ' in out


@pytest.mark.dependency(depends=["add_json_column", "insert_datatypes_data"])
def test_update_data_with_json(capsys, instance_id, sample_database):
    snippets.update_data_with_json(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Updated data" in out


@pytest.mark.dependency(depends=["add_json_column"])
def test_query_data_with_json_parameter(capsys, instance_id, sample_database):
    snippets.query_data_with_json_parameter(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "VenueId: 19, VenueDetails: {'open': True, 'rating': 9}" in out


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


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_set_transaction_tag(capsys, instance_id, sample_database):
    snippets.set_transaction_tag(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Venue capacities updated." in out
    assert "New venue inserted." in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_set_transaction_timeout(capsys, instance_id, sample_database):
    snippets.set_transaction_timeout(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out


@pytest.mark.dependency(depends=["insert_datatypes_data"])
def test_set_statement_timeout(capsys, instance_id, sample_database):
    snippets.set_statement_timeout(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) inserted." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_set_request_tag(capsys, instance_id, sample_database):
    snippets.set_request_tag(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk" in out


@pytest.mark.dependency(name="add_and_drop_database_roles", depends=["insert_data"])
def test_add_and_drop_database_roles(capsys, instance_id, sample_database):
    snippets.add_and_drop_database_roles(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Created roles new_parent and new_child and granted privileges" in out
    assert "Revoked privileges and dropped role new_child" in out


@pytest.mark.dependency(depends=["add_and_drop_database_roles"])
def test_read_data_with_database_role(capsys, instance_id, sample_database):
    snippets.read_data_with_database_role(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "ingerId: 1, FirstName: Marc, LastName: Richards" in out


@pytest.mark.dependency(depends=["add_and_drop_database_roles"])
def test_list_database_roles(capsys, instance_id, sample_database):
    snippets.list_database_roles(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "new_parent" in out


@pytest.mark.dependency(name="create_table_with_foreign_key_delete_cascade")
def test_create_table_with_foreign_key_delete_cascade(
    capsys, instance_id, sample_database
):
    snippets.create_table_with_foreign_key_delete_cascade(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert (
        "Created Customers and ShoppingCarts table with FKShoppingCartsCustomerId"
        in out
    )


@pytest.mark.dependency(
    name="alter_table_with_foreign_key_delete_cascade",
    depends=["create_table_with_foreign_key_delete_cascade"],
)
def test_alter_table_with_foreign_key_delete_cascade(
    capsys, instance_id, sample_database
):
    snippets.alter_table_with_foreign_key_delete_cascade(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "Altered ShoppingCarts table with FKShoppingCartsCustomerName" in out


@pytest.mark.dependency(depends=["alter_table_with_foreign_key_delete_cascade"])
def test_drop_foreign_key_contraint_delete_cascade(
    capsys, instance_id, sample_database
):
    snippets.drop_foreign_key_constraint_delete_cascade(
        instance_id, sample_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "Altered ShoppingCarts table to drop FKShoppingCartsCustomerName" in out


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


@pytest.mark.dependency(depends=["insert_data"])
def test_directed_read_options(capsys, instance_id, sample_database):
    snippets.directed_read_options(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk" in out


@pytest.mark.dependency(depends=["insert_data"])
def test_set_custom_timeout_and_retry(capsys, instance_id, sample_database):
    snippets.set_custom_timeout_and_retry(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk" in out


@pytest.mark.dependency(depends=["insert_data"])
def test_isolation_level_options(capsys, instance_id, sample_database):
    snippets.isolation_level_options(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) updated." in out


@pytest.mark.dependency(depends=["insert_data"])
def test_read_lock_mode_options(capsys, instance_id, sample_database):
    snippets.read_lock_mode_options(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "1 record(s) updated." in out


@pytest.mark.dependency(
    name="add_proto_types_column",
)
def test_add_proto_types_column(capsys, instance_id, proto_columns_database):
    snippets.add_proto_type_columns(instance_id, proto_columns_database.database_id)
    out, _ = capsys.readouterr()
    assert 'Altered table "Singers" on database ' in out

    snippets.insert_data(instance_id, proto_columns_database.database_id)


@pytest.mark.dependency(
    name="update_data_with_proto_message", depends=["add_proto_types_column"]
)
def test_update_data_with_proto_types(capsys, instance_id, proto_columns_database):
    snippets.update_data_with_proto_types(
        instance_id, proto_columns_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "Data updated" in out

    snippets.update_data_with_proto_types_with_dml(
        instance_id, proto_columns_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "1 record(s) updated." in out


@pytest.mark.dependency(
    depends=["add_proto_types_column", "update_data_with_proto_message"]
)
def test_query_data_with_proto_types_parameter(
    capsys, instance_id, proto_columns_database
):
    snippets.query_data_with_proto_types_parameter(
        instance_id, proto_columns_database.database_id
    )
    out, _ = capsys.readouterr()
    assert "SingerId: 2, SingerInfo: singer_id: 2" in out


@pytest.mark.dependency(name="add_split_points", depends=["insert_data"])
def test_add_split_points(capsys, instance_id, sample_database):
    snippets.add_split_points(instance_id, sample_database.database_id)
    out, _ = capsys.readouterr()
    assert "Added split points." in out
