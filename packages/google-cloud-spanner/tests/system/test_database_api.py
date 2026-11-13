# Copyright 2021 Google LLC All rights reserved.
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

import datetime
import time
import uuid

import pytest
from google.api_core import exceptions
from google.iam.v1 import policy_pb2
from google.type import expr_pb2

from google.cloud import spanner_v1
from google.cloud.spanner_admin_database_v1 import DatabaseDialect
from google.cloud.spanner_v1 import DirectedReadOptions

from . import _helpers, _sample_data

DBAPI_OPERATION_TIMEOUT = 240  # seconds
FKADC_CUSTOMERS_COLUMNS = ("CustomerId", "CustomerName")
FKADC_SHOPPING_CARTS_COLUMNS = ("CartId", "CustomerId", "CustomerName")
ALL_KEYSET = spanner_v1.KeySet(all_=True)
DIRECTED_READ_OPTIONS = {
    "include_replicas": {
        "replica_selections": [
            {
                "location": "us-west1",
                "type_": DirectedReadOptions.ReplicaSelection.Type.READ_ONLY,
            },
        ],
        "auto_failover_disabled": True,
    },
}


@pytest.fixture(scope="module")
def multiregion_instance(
    spanner_client, instance_operation_timeout, not_postgres, not_spanner_omni
):
    multi_region_instance_id = _helpers.unique_id("multi-region")
    multi_region_config = "nam3"
    config_name = "{}/instanceConfigs/{}".format(
        spanner_client.project_name, multi_region_config
    )
    create_time = str(int(time.time()))
    labels = {"python-spanner-systests": "true", "created": create_time}
    multiregion_instance = spanner_client.instance(
        instance_id=multi_region_instance_id,
        configuration_name=config_name,
        labels=labels,
    )
    operation = _helpers.retry_429_503(multiregion_instance.create)()
    operation.result(instance_operation_timeout)

    yield multiregion_instance

    _helpers.retry_429_503(multiregion_instance.delete)()


def test_list_databases(shared_instance, shared_database):
    # Since `shared_instance` is newly created in `setUpModule`, the
    # database created in `setUpClass` here will be the only one.
    database_names = [database.name for database in shared_instance.list_databases()]
    assert shared_database.name in database_names


def test_create_database_and_update_ddl(
    shared_instance, databases_to_delete, database_dialect
):
    pool = spanner_v1.BurstyPool(labels={"testcase": "create_database"})
    temp_db_id = _helpers.unique_id("temp_db")
    temp_db = shared_instance.database(
        temp_db_id, pool=pool, database_dialect=database_dialect
    )
    operation = temp_db.create()
    databases_to_delete.append(temp_db)

    # We want to make sure the operation completes.
    operation.result(DBAPI_OPERATION_TIMEOUT)  # raises on failure / timeout.

    database_ids = [database.name for database in shared_instance.list_databases()]
    assert temp_db.name in database_ids

    # Update DDL with custom operation ID and reload
    operation_id = f"a{str(uuid.uuid4())[:8]}"
    ddl_statements = [_helpers.DDL_STATEMENTS[0]]
    operation = temp_db.update_ddl(
        ddl_statements,
        operation_id=operation_id,
    )
    assert operation_id == operation.operation.name.split("/")[-1]
    operation.result(DBAPI_OPERATION_TIMEOUT)

    temp_db.reload()
    assert len(temp_db.ddl_statements) == len(ddl_statements)
    assert "contacts" in temp_db.ddl_statements[0].lower()


def test_create_and_update_database_pitr(
    not_emulator,  # PITR-lite features are not supported by the emulator
    not_postgres,
    shared_instance,
    databases_to_delete,
):
    pool = spanner_v1.BurstyPool(labels={"testcase": "create_database_pitr"})
    temp_db_id = _helpers.unique_id("pitr_db", separator="_")
    retention_period = "7d"
    ddl_statements = [
        f"ALTER DATABASE {temp_db_id}"
        f" SET OPTIONS (version_retention_period = '{retention_period}')"
    ]
    temp_db = shared_instance.database(
        temp_db_id, pool=pool, ddl_statements=ddl_statements
    )
    operation = temp_db.create()
    databases_to_delete.append(temp_db)
    operation.result(DBAPI_OPERATION_TIMEOUT)  # raises on failure / timeout.

    database_ids = [database.name for database in shared_instance.list_databases()]
    assert temp_db.name in database_ids

    temp_db.reload()
    assert temp_db.version_retention_period == retention_period

    with temp_db.snapshot() as snapshot:
        results = list(
            snapshot.execute_sql(
                "SELECT OPTION_VALUE AS version_retention_period "
                "FROM INFORMATION_SCHEMA.DATABASE_OPTIONS "
                "WHERE SCHEMA_NAME = '' "
                "AND OPTION_NAME = 'version_retention_period'"
            )
        )
        assert len(results) == 1
        assert results[0][0] == retention_period

    # Test updating PITR and passing custom operation_id
    new_retention_period = "3d"
    operation_id = f"a{str(uuid.uuid4())[:8]}"
    update_ddl_statements = [
        f"ALTER DATABASE {temp_db_id}"
        f" SET OPTIONS (version_retention_period = '{new_retention_period}')"
    ]
    operation = temp_db.update_ddl(
        update_ddl_statements,
        operation_id=operation_id,
    )
    assert operation_id == operation.operation.name.split("/")[-1]
    operation.result(DBAPI_OPERATION_TIMEOUT)

    temp_db.reload()
    assert temp_db.version_retention_period == new_retention_period

    with temp_db.snapshot() as snapshot:
        results = list(
            snapshot.execute_sql(
                "SELECT OPTION_VALUE AS version_retention_period "
                "FROM INFORMATION_SCHEMA.DATABASE_OPTIONS "
                "WHERE SCHEMA_NAME = '' "
                "AND OPTION_NAME = 'version_retention_period'"
            )
        )
        assert len(results) == 1
        assert results[0][0] == new_retention_period


def test_create_and_update_database_with_default_leader(
    not_emulator,  # Default leader setting not supported by the emulator
    not_postgres,
    not_spanner_omni,
    multiregion_instance,
    databases_to_delete,
):
    pool = spanner_v1.BurstyPool(labels={"testcase": "default_leader"})

    temp_db_id = _helpers.unique_id("dflt_ldr_db", separator="_")
    default_leader = "us-east4"
    ddl_statements = [
        f"ALTER DATABASE {temp_db_id} SET OPTIONS (default_leader = '{default_leader}')"
    ]
    temp_db = multiregion_instance.database(
        temp_db_id, pool=pool, ddl_statements=ddl_statements
    )
    operation = temp_db.create()
    databases_to_delete.append(temp_db)
    operation.result(DBAPI_OPERATION_TIMEOUT)  # raises on failure / timeout.

    database_ids = [database.name for database in multiregion_instance.list_databases()]
    assert temp_db.name in database_ids

    temp_db.reload()
    assert temp_db.default_leader == default_leader

    with temp_db.snapshot() as snapshot:
        results = list(
            snapshot.execute_sql(
                "SELECT OPTION_VALUE AS default_leader "
                "FROM INFORMATION_SCHEMA.DATABASE_OPTIONS "
                "WHERE SCHEMA_NAME = '' AND OPTION_NAME = 'default_leader'"
            )
        )
        assert len(results) == 1
        assert results[0][0] == default_leader

    # Test updating default leader on the multiregion database
    new_default_leader = "us-east1"
    update_ddl_statements = [
        f"ALTER DATABASE {temp_db_id} "
        f"SET OPTIONS (default_leader = '{new_default_leader}')"
    ]
    operation = temp_db.update_ddl(update_ddl_statements)
    operation.result(DBAPI_OPERATION_TIMEOUT)

    temp_db.reload()
    assert temp_db.default_leader == new_default_leader

    with temp_db.snapshot() as snapshot:
        results = list(
            snapshot.execute_sql(
                "SELECT OPTION_VALUE AS default_leader "
                "FROM INFORMATION_SCHEMA.DATABASE_OPTIONS "
                "WHERE SCHEMA_NAME = '' AND OPTION_NAME = 'default_leader'"
            )
        )
        assert len(results) == 1
        assert results[0][0] == new_default_leader


def test_iam_policy(
    not_emulator,
    not_spanner_omni,
    shared_instance,
    databases_to_delete,
):
    pool = spanner_v1.BurstyPool(labels={"testcase": "iam_policy"})
    temp_db_id = _helpers.unique_id("iam_db", separator="_")
    create_table = (
        "CREATE TABLE policy (\n"
        + "    Id      STRING(36) NOT NULL,\n"
        + "    Field1  STRING(36) NOT NULL\n"
        + ") PRIMARY KEY (Id)"
    )
    create_role = "CREATE ROLE parent"

    temp_db = shared_instance.database(
        temp_db_id,
        ddl_statements=[create_table, create_role],
        pool=pool,
    )
    create_op = temp_db.create()
    databases_to_delete.append(temp_db)
    create_op.result(DBAPI_OPERATION_TIMEOUT)
    policy = temp_db.get_iam_policy(3)

    assert policy.version == 0
    assert policy.etag == b"\x00 \x01"

    new_binding = policy_pb2.Binding(
        role="roles/spanner.fineGrainedAccessUser",
        members=["user:asthamohta@google.com"],
        condition=expr_pb2.Expr(
            title="condition title",
            expression='resource.name.endsWith("/databaseRoles/parent")',
        ),
    )

    policy.version = 3
    policy.bindings.append(new_binding)
    temp_db.set_iam_policy(policy)

    new_policy = temp_db.get_iam_policy(3)
    assert new_policy.version == 3
    assert len(new_policy.bindings) == 1
    assert new_policy.bindings[0] == new_binding


def test_table_not_found(shared_instance):
    temp_db_id = _helpers.unique_id("tbl_not_found", separator="_")

    correct_table = "MyTable"
    incorrect_table = "NotMyTable"

    create_table = (
        f"CREATE TABLE {correct_table} (\n"
        f"    Id      STRING(36) NOT NULL,\n"
        f"    Field1  STRING(36) NOT NULL\n"
        f") PRIMARY KEY (Id)"
    )
    create_index = f"CREATE INDEX IDX ON {incorrect_table} (Field1)"

    temp_db = shared_instance.database(
        temp_db_id, ddl_statements=[create_table, create_index]
    )
    with pytest.raises(exceptions.NotFound):
        temp_db.create()


def test_create_role_grant_access_and_list_roles(
    not_emulator,
    not_spanner_omni,
    shared_instance,
    databases_to_delete,
    database_dialect,
):
    creator_role_parent = _helpers.unique_id("role_parent", separator="_")
    creator_role_orphan = _helpers.unique_id("role_orphan", separator="_")

    temp_db_id = _helpers.unique_id("roles_db", separator="_")
    temp_db = shared_instance.database(temp_db_id, database_dialect=database_dialect)

    create_op = temp_db.create()
    databases_to_delete.append(temp_db)
    create_op.result(DBAPI_OPERATION_TIMEOUT)  # raises on failure / timeout.

    # Create role and grant select permission on table contacts for parent role.
    grant_target = (
        f"ROLE {creator_role_parent}"
        if database_dialect == DatabaseDialect.GOOGLE_STANDARD_SQL
        else f"{creator_role_parent}"
    )
    ddl_statements = [
        _helpers.DDL_STATEMENTS[0],
        f"CREATE ROLE {creator_role_parent}",
        f"CREATE ROLE {creator_role_orphan}",
        f"GRANT SELECT ON TABLE contacts TO {grant_target}",
    ]

    operation = temp_db.update_ddl(ddl_statements)
    operation.result(DBAPI_OPERATION_TIMEOUT)  # raises on failure / timeout.

    # List database roles.
    roles_list = [role.name.split("/")[-1] for role in temp_db.list_database_roles()]
    assert creator_role_parent in roles_list
    assert creator_role_orphan in roles_list

    # Perform select with orphan role on table contacts.
    # Expect PermissionDenied exception.
    orphan_db = shared_instance.database(temp_db_id, database_role=creator_role_orphan)
    with pytest.raises(exceptions.PermissionDenied):
        with orphan_db.snapshot() as snapshot:
            results = snapshot.execute_sql("SELECT * FROM contacts")
            for _ in results:
                pass

    # Perform select with parent role on table contacts. Expect success.
    parent_db = shared_instance.database(temp_db_id, database_role=creator_role_parent)
    with parent_db.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT * FROM contacts")
        for _ in results:
            pass


def test_db_batch_insert_then_db_snapshot_read(shared_database):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(sd.TABLE, sd.ALL)
        batch.insert(sd.TABLE, sd.COLUMNS, sd.ROW_DATA)

    with shared_database.snapshot(read_timestamp=batch.committed) as snapshot:
        from_snap = list(snapshot.read(sd.TABLE, sd.COLUMNS, sd.ALL))

    sd._check_rows_data(from_snap)


def test_db_batch_send_and_ack(
    not_emulator, spanner_client, database_dialect, shared_instance
):
    import uuid

    from google.api_core.exceptions import GoogleAPIError, MethodNotImplemented

    from google.cloud.spanner_admin_database_v1 import DatabaseDialect

    db_id = f"test-db-{uuid.uuid4().hex[:8]}"
    queue_name = f"test_queue_{uuid.uuid4().hex[:8]}"

    try:
        test_database = shared_instance.database(
            db_id, database_dialect=database_dialect
        )
        operation = test_database.create()
        operation.result(300)

        # Create the Queue
        if database_dialect == DatabaseDialect.POSTGRESQL:
            queue_ddl = f"""CREATE QUEUE {queue_name} (
                id bigint NOT NULL,
                "Payload" varchar NOT NULL,
                PRIMARY KEY (id)
            )"""
        else:
            queue_ddl = f"""CREATE QUEUE {queue_name} (
                Id INT64 NOT NULL,
                Payload STRING(MAX) NOT NULL
            ) PRIMARY KEY (Id)"""
        try:
            operation = test_database.update_ddl([queue_ddl])
            operation.result(600)
        except MethodNotImplemented as e:
            pytest.skip(f"Queues are not implemented yet: {e}")
        except GoogleAPIError as e:
            grpc_status_name = getattr(
                getattr(e, "grpc_status_code", None), "name", None
            )
            if (
                getattr(e, "code", None) == 501
                or grpc_status_name == "UNIMPLEMENTED"
                or "UNIMPLEMENTED" in str(e)
            ):
                pytest.skip(f"Queues are not implemented yet: {e}")
            raise

        with test_database.batch() as batch:
            batch.send(
                queue=queue_name,
                key=(2,),
                payload="Hello, Queues!",
            )

        with test_database.batch() as batch:
            batch.ack(
                queue=queue_name,
                key=(2,),
            )

    finally:
        test_database.drop()


def test_db_run_in_transaction_then_snapshot_execute_sql(shared_database):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(sd.TABLE, sd.ALL)

    def _unit_of_work(transaction, test):
        # TODO: Remove query and execute a read instead when the Emulator has been fixed
        #       and returns pre-commit tokens for streaming read results.
        rows = list(transaction.execute_sql(sd.SQL))
        # rows = list(transaction.read(test.TABLE, test.COLUMNS, sd.ALL))
        assert rows == []

        transaction.insert_or_update(test.TABLE, test.COLUMNS, test.ROW_DATA)

    shared_database.run_in_transaction(_unit_of_work, test=sd)

    with shared_database.snapshot() as after:
        rows = list(after.execute_sql(sd.SQL))

    sd._check_rows_data(rows)


def test_db_run_in_transaction_twice(shared_database):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(sd.TABLE, sd.ALL)

    def _unit_of_work(transaction, test):
        transaction.insert_or_update(test.TABLE, test.COLUMNS, test.ROW_DATA)

    shared_database.run_in_transaction(_unit_of_work, test=sd)
    shared_database.run_in_transaction(_unit_of_work, test=sd)

    with shared_database.snapshot() as after:
        rows = list(after.execute_sql(sd.SQL))
    sd._check_rows_data(rows)


def test_db_run_in_transaction_twice_4181(shared_database):
    # See https://github.com/googleapis/google-cloud-python/issues/4181
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(sd.COUNTERS_TABLE, sd.ALL)

    def _unit_of_work(transaction, name):
        transaction.insert(sd.COUNTERS_TABLE, sd.COUNTERS_COLUMNS, [[name, 0]])

    shared_database.run_in_transaction(_unit_of_work, name="id_1")

    with pytest.raises(exceptions.AlreadyExists):
        shared_database.run_in_transaction(_unit_of_work, name="id_1")

    shared_database.run_in_transaction(_unit_of_work, name="id_2")

    with shared_database.snapshot() as after:
        rows = list(after.read(sd.COUNTERS_TABLE, sd.COUNTERS_COLUMNS, sd.ALL))

    assert len(rows) == 2


def test_insertion_in_referencing_table_fkadc(not_emulator, shared_database):
    with shared_database.batch() as batch:
        batch.insert(
            table="Customers",
            columns=FKADC_CUSTOMERS_COLUMNS,
            values=[
                (1, "Marc"),
                (2, "Catalina"),
            ],
        )

    with shared_database.batch() as batch:
        batch.insert(
            table="ShoppingCarts",
            columns=FKADC_SHOPPING_CARTS_COLUMNS,
            values=[
                (1, 1, "Marc"),
            ],
        )

    with shared_database.snapshot() as snapshot:
        rows = list(
            snapshot.read(
                "ShoppingCarts", ("CartId", "CustomerId", "CustomerName"), ALL_KEYSET
            )
        )

    assert len(rows) == 1


def test_insertion_in_referencing_table_error_fkadc(not_emulator, shared_database):
    with pytest.raises(exceptions.FailedPrecondition):
        with shared_database.batch() as batch:
            batch.insert(
                table="ShoppingCarts",
                columns=FKADC_SHOPPING_CARTS_COLUMNS,
                values=[
                    (4, 4, "Naina"),
                ],
            )


def test_insertion_then_deletion_in_referenced_table_fkadc(
    not_emulator, shared_database
):
    with shared_database.batch() as batch:
        batch.insert(
            table="Customers",
            columns=FKADC_CUSTOMERS_COLUMNS,
            values=[
                (3, "Sara"),
            ],
        )

    with shared_database.batch() as batch:
        batch.insert(
            table="ShoppingCarts",
            columns=FKADC_SHOPPING_CARTS_COLUMNS,
            values=[
                (3, 3, "Sara"),
            ],
        )

    with shared_database.snapshot() as snapshot:
        rows = list(snapshot.read("ShoppingCarts", ["CartId"], ALL_KEYSET))

    assert [3] in rows

    with shared_database.batch() as batch:
        batch.delete(table="Customers", keyset=spanner_v1.KeySet(keys=[[3]]))

    with shared_database.snapshot() as snapshot:
        rows = list(snapshot.read("ShoppingCarts", ["CartId"], ALL_KEYSET))

    assert [3] not in rows


def test_insert_then_delete_referenced_key_error_fkadc(not_emulator, shared_database):
    with pytest.raises(exceptions.FailedPrecondition):
        with shared_database.batch() as batch:
            batch.insert(
                table="Customers",
                columns=FKADC_CUSTOMERS_COLUMNS,
                values=[
                    (3, "Sara"),
                ],
            )
            batch.delete(table="Customers", keyset=spanner_v1.KeySet(keys=[[3]]))


def test_insert_referencing_key_then_delete_referenced_key_error_fkadc(
    not_emulator, shared_database
):
    with shared_database.batch() as batch:
        batch.insert(
            table="Customers",
            columns=FKADC_CUSTOMERS_COLUMNS,
            values=[
                (4, "Huda"),
            ],
        )

    with pytest.raises(exceptions.FailedPrecondition):
        with shared_database.batch() as batch:
            batch.insert(
                table="ShoppingCarts",
                columns=FKADC_SHOPPING_CARTS_COLUMNS,
                values=[
                    (4, 4, "Huda"),
                ],
            )
            batch.delete(table="Customers", keyset=spanner_v1.KeySet(keys=[[4]]))


def test_information_schema_referential_constraints_fkadc(
    not_emulator, shared_database
):
    with shared_database.snapshot() as snapshot:
        rows = list(
            snapshot.execute_sql(
                "SELECT DELETE_RULE "
                "FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS "
                "WHERE CONSTRAINT_NAME = 'FKShoppingCartsCustomerId'"
            )
        )

        assert any("CASCADE" in stmt for stmt in rows)


def test_update_database_success(
    not_emulator,
    not_spanner_omni,
    shared_database,
    shared_instance,
    database_operation_timeout,
):
    old_protection = shared_database.enable_drop_protection
    new_protection = True
    shared_database.enable_drop_protection = new_protection
    operation = shared_database.update(["enable_drop_protection"])

    # We want to make sure the operation completes.
    operation.result(database_operation_timeout)  # raises on failure / timeout.

    # Create a new database instance and reload it.
    database_alt = shared_instance.database(shared_database.name.split("/")[-1])
    assert database_alt.enable_drop_protection != new_protection

    database_alt.reload()
    assert database_alt.enable_drop_protection == new_protection

    with pytest.raises(exceptions.FailedPrecondition):
        database_alt.drop()

    with pytest.raises(exceptions.FailedPrecondition):
        shared_instance.delete()

    # Make sure to put the database back the way it was for the
    # other test cases.
    shared_database.enable_drop_protection = old_protection
    shared_database.update(["enable_drop_protection"])


def test_update_database_invalid(not_emulator, shared_database):
    shared_database.enable_drop_protection = True

    # Empty `fields` is not supported.
    with pytest.raises(exceptions.InvalidArgument):
        shared_database.update([])


def test_snapshot_read_w_directed_read_options(
    shared_database, not_postgres, not_emulator
):
    _helpers.retry_has_all_dll(shared_database.reload)()
    table = "users_history"
    columns = ["id", "commit_ts", "name", "email", "deleted"]
    user_id = 1234
    name = "phred"
    email = "phred@example.com"
    row_data = [[user_id, spanner_v1.COMMIT_TIMESTAMP, name, email, False]]
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(table, sd.ALL)
        batch.insert(table, columns, row_data)

    with shared_database.snapshot() as snapshot:
        rows = list(
            snapshot.read(
                table, columns, sd.ALL, directed_read_options=DIRECTED_READ_OPTIONS
            )
        )

    assert len(rows) == 1


def test_execute_sql_w_directed_read_options(
    shared_database, not_postgres, not_emulator
):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(sd.TABLE, sd.ALL)

    def _unit_of_work(transaction, test):
        transaction.insert_or_update(test.TABLE, test.COLUMNS, test.ROW_DATA)

    shared_database.run_in_transaction(_unit_of_work, test=sd)

    with shared_database.snapshot() as snapshot:
        rows = list(
            snapshot.execute_sql(sd.SQL, directed_read_options=DIRECTED_READ_OPTIONS)
        )
    sd._check_rows_data(rows)


def test_readwrite_transaction_w_directed_read_options_w_error(
    shared_database, not_emulator, not_postgres
):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    def _transaction_read(transaction):
        list(
            transaction.read(
                sd.TABLE,
                sd.COLUMNS,
                sd.ALL,
                directed_read_options=DIRECTED_READ_OPTIONS,
            )
        )

    with pytest.raises(exceptions.InvalidArgument):
        shared_database.run_in_transaction(_transaction_read)


def test_db_batch_insert_w_max_commit_delay(shared_database):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch(
        max_commit_delay=datetime.timedelta(milliseconds=100)
    ) as batch:
        batch.delete(sd.TABLE, sd.ALL)
        batch.insert(sd.TABLE, sd.COLUMNS, sd.ROW_DATA)

    with shared_database.snapshot(read_timestamp=batch.committed) as snapshot:
        from_snap = list(snapshot.read(sd.TABLE, sd.COLUMNS, sd.ALL))

    sd._check_rows_data(from_snap)


def test_db_run_in_transaction_w_max_commit_delay(shared_database):
    _helpers.retry_has_all_dll(shared_database.reload)()
    sd = _sample_data

    with shared_database.batch() as batch:
        batch.delete(sd.TABLE, sd.ALL)

    def _unit_of_work(transaction, test):
        # TODO: Remove query and execute a read instead when the Emulator has been fixed
        #       and returns pre-commit tokens for streaming read results.
        rows = list(transaction.execute_sql(sd.SQL))
        # rows = list(transaction.read(test.TABLE, test.COLUMNS, sd.ALL))
        assert rows == []

        transaction.insert_or_update(test.TABLE, test.COLUMNS, test.ROW_DATA)

    shared_database.run_in_transaction(
        _unit_of_work, test=sd, max_commit_delay=datetime.timedelta(milliseconds=100)
    )

    with shared_database.snapshot() as after:
        rows = list(after.execute_sql(sd.SQL))

    sd._check_rows_data(rows)


def test_create_table_with_proto_columns(
    not_postgres,
    shared_instance,
    databases_to_delete,
    proto_descriptor_file,
):
    proto_cols_db_id = _helpers.unique_id("proto-columns")
    extra_ddl = [
        "CREATE PROTO BUNDLE (examples.spanner.music.SingerInfo, examples.spanner.music.Genre,)"
    ]

    proto_cols_database = shared_instance.database(
        proto_cols_db_id,
        ddl_statements=extra_ddl + _helpers.PROTO_COLUMNS_DDL_STATEMENTS,
        proto_descriptors=proto_descriptor_file,
    )
    operation = proto_cols_database.create()
    operation.result(DBAPI_OPERATION_TIMEOUT)  # raises on failure / timeout.

    databases_to_delete.append(proto_cols_database)

    proto_cols_database.reload()
    assert proto_cols_database.proto_descriptors is not None
    assert any("PROTO BUNDLE" in stmt for stmt in proto_cols_database.ddl_statements)
