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
import os
import time

import pytest

from google.cloud import spanner_v1
from google.cloud.spanner_admin_database_v1 import DatabaseDialect
from google.cloud.spanner_admin_database_v1.types.backup import (
    CreateBackupEncryptionConfig,
)

from . import _helpers

# Disable builtin metrics for system tests by default to avoid 401 errors
# from the background thread exporting to Cloud Monitoring without permissions.
os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "true"


@pytest.fixture(scope="function")
def if_create_instance():
    if not _helpers.CREATE_INSTANCE:
        pytest.skip(f"{_helpers.CREATE_INSTANCE_ENVVAR} not set in environment.")


@pytest.fixture(scope="function")
def no_create_instance():
    if _helpers.CREATE_INSTANCE:
        pytest.skip(f"{_helpers.CREATE_INSTANCE_ENVVAR} set in environment.")


@pytest.fixture(scope="function")
def if_backup_tests():
    if _helpers.SKIP_BACKUP_TESTS:
        pytest.skip(f"{_helpers.SKIP_BACKUP_TESTS_ENVVAR} set in environment.")


@pytest.fixture(scope="function")
def not_emulator():
    if _helpers.USE_EMULATOR:
        pytest.skip(f"{_helpers.USE_EMULATOR_ENVVAR} set in environment.")


@pytest.fixture(scope="module")
def not_spanner_omni():
    if _helpers.USE_SPANNER_OMNI:
        pytest.skip(f"{_helpers.USE_SPANNER_OMNI_ENVVAR} set in environment.")


@pytest.fixture(scope="session")
def not_postgres(database_dialect):
    if database_dialect == DatabaseDialect.POSTGRESQL:
        pytest.skip(
            f"{_helpers.DATABASE_DIALECT_ENVVAR} set to POSTGRES in environment."
        )


@pytest.fixture(scope="session")
def not_google_standard_sql(database_dialect):
    if database_dialect == DatabaseDialect.GOOGLE_STANDARD_SQL:
        pytest.skip(
            f"{_helpers.DATABASE_DIALECT_ENVVAR} set to GOOGLE_STANDARD_SQL in environment."
        )


@pytest.fixture(scope="session")
def not_postgres_emulator(database_dialect):
    if database_dialect == DatabaseDialect.POSTGRESQL and _helpers.USE_EMULATOR:
        pytest.skip(
            f"{_helpers.DATABASE_DIALECT_ENVVAR} set to POSTGRESQL and {_helpers.USE_EMULATOR_ENVVAR} set in "
            "environment."
        )


@pytest.fixture(scope="session")
def database_dialect():
    return (
        DatabaseDialect[_helpers.DATABASE_DIALECT]
        if _helpers.DATABASE_DIALECT
        else DatabaseDialect.GOOGLE_STANDARD_SQL
    )


@pytest.fixture(scope="session")
def proto_descriptor_file():
    import os

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "testdata/descriptors.pb")
    file = open(filename, "rb")
    yield file.read()
    file.close()


@pytest.fixture(scope="session")
def spanner_client():
    if _helpers.USE_EMULATOR:
        from google.auth.credentials import AnonymousCredentials

        credentials = AnonymousCredentials()
        return spanner_v1.Client(
            project=_helpers.EMULATOR_PROJECT,
            credentials=credentials,
        )
    elif _helpers.USE_SPANNER_OMNI:
        return spanner_v1.Client(
            use_plain_text=_helpers.USE_PLAIN_TEXT,
            ca_certificate=_helpers.CA_CERTIFICATE,
            client_certificate=_helpers.CLIENT_CERTIFICATE,
            client_key=_helpers.CLIENT_KEY,
            client_options={"api_endpoint": _helpers.SPANNER_OMNI},
            instance_type="omni",
            username=_helpers.SPANNER_OMNI_USER,
            password=_helpers.SPANNER_OMNI_PASSWORD,
        )
    else:
        client_options = {"api_endpoint": _helpers.API_ENDPOINT}
        return spanner_v1.Client(
            client_options=client_options
        )  # use google.auth.default credentials


@pytest.fixture(scope="session")
def instance_operation_timeout():
    return _helpers.INSTANCE_OPERATION_TIMEOUT_IN_SECONDS


@pytest.fixture(scope="session")
def database_operation_timeout():
    return _helpers.DATABASE_OPERATION_TIMEOUT_IN_SECONDS


@pytest.fixture(scope="session")
def backup_operation_timeout():
    return _helpers.BACKUP_OPERATION_TIMEOUT_IN_SECONDS


@pytest.fixture(scope="session")
def shared_instance_id():
    if _helpers.CREATE_INSTANCE:
        return f"{_helpers.unique_id('google-cloud')}"
    if _helpers.USE_SPANNER_OMNI:
        return _helpers.SPANNER_OMNI_INSTANCE
    return _helpers.INSTANCE_ID


@pytest.fixture(scope="session")
def instance_configs(spanner_client):
    configs = list(_helpers.retry_503(spanner_client.list_instance_configs)())

    if not _helpers.USE_EMULATOR and not _helpers.USE_SPANNER_OMNI:
        # Defend against back-end returning configs for regions we aren't
        # actually allowed to use.
        configs = [config for config in configs if "-us-" in config.name]

    yield configs


@pytest.fixture(scope="session")
def instance_config(instance_configs):
    if not instance_configs:
        raise ValueError("No instance configs found.")

    import random

    us_configs = [
        config
        for config in instance_configs
        if config.display_name in ["us-south1", "us-east4"]
    ]

    config = (
        random.choice(us_configs) if us_configs else random.choice(instance_configs)
    )
    yield config


@pytest.fixture(scope="session")
def existing_instances(spanner_client):
    instances = list(_helpers.retry_503(spanner_client.list_instances)())

    yield instances


@pytest.fixture(scope="session")
def shared_instance(
    spanner_client,
    instance_operation_timeout,
    shared_instance_id,
    instance_config,
    existing_instances,  # evalutate before creating one
):
    _helpers.cleanup_old_instances(spanner_client)

    if _helpers.CREATE_INSTANCE:
        from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin

        create_time = str(int(time.time()))
        labels = {"python-spanner-systests": "true", "created": create_time}

        request = spanner_instance_admin.CreateInstanceRequest(
            parent=spanner_client.project_name,
            instance_id=shared_instance_id,
            instance=spanner_instance_admin.Instance(
                config=instance_config.name,
                display_name=shared_instance_id,
                node_count=1,
                labels=labels,
                edition=spanner_instance_admin.Instance.Edition.ENTERPRISE,
            ),
        )
        created_op = _helpers.retry_429_503(
            spanner_client.instance_admin_api.create_instance
        )(request=request)
        created_op.result(instance_operation_timeout)  # block until completion

        instance = spanner_client.instance(
            shared_instance_id, instance_config.name, labels=labels
        )

    else:  # reuse existing instance
        instance = spanner_client.instance(shared_instance_id)
        instance.reload()

    _helpers.cleanup_stale_databases(instance)

    yield instance

    if _helpers.CREATE_INSTANCE:
        _helpers.retry_429_503(instance.delete)()


@pytest.fixture(scope="session")
def shared_database(
    shared_instance, database_operation_timeout, database_dialect, proto_descriptor_file
):
    database_name = _helpers.unique_id("test_database")
    pool = spanner_v1.BurstyPool(labels={"testcase": "database_api"})
    if database_dialect == DatabaseDialect.POSTGRESQL:
        database = shared_instance.database(
            database_name,
            pool=pool,
            database_dialect=database_dialect,
        )
        operation = database.create()
        operation.result(database_operation_timeout)  # raises on failure / timeout.

        operation = database.update_ddl(ddl_statements=_helpers.DDL_STATEMENTS)
        operation.result(database_operation_timeout)  # raises on failure / timeout.

    else:
        database = shared_instance.database(
            database_name,
            ddl_statements=_helpers.DDL_STATEMENTS,
            pool=pool,
            database_dialect=database_dialect,
            proto_descriptors=proto_descriptor_file,
        )
        operation = database.create()
        operation.result(database_operation_timeout)  # raises on failure / timeout.

    yield database

    database.drop()


@pytest.fixture(scope="session")
def shared_backup(shared_instance, shared_database, backup_operation_timeout):
    backup_name = _helpers.unique_id("test_backup")
    expire_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        days=3
    )
    source_encryption_enum = CreateBackupEncryptionConfig.EncryptionType
    source_encryption_config = CreateBackupEncryptionConfig(
        encryption_type=source_encryption_enum.GOOGLE_DEFAULT_ENCRYPTION,
    )
    backup = shared_instance.backup(
        backup_name,
        database=shared_database,
        expire_time=expire_time,
        encryption_config=source_encryption_config,
    )
    operation = backup.create()
    operation.result(backup_operation_timeout)  # raises on failure / timeout.

    yield backup

    backup.delete()


@pytest.fixture(scope="function")
def databases_to_delete():
    to_delete = []

    yield to_delete

    for database in to_delete:
        database.drop()
