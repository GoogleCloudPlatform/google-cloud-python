# Copyright 2024 Google LLC All rights reserved.
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

import pytest

from google.cloud import spanner_v1
from google.cloud.spanner_admin_database_v1 import DatabaseDialect

from .. import _helpers


@pytest.fixture(scope="session")
def spanner_client():
    if _helpers.USE_EMULATOR:
        from google.auth.credentials import AnonymousCredentials

        credentials = AnonymousCredentials()
        return spanner_v1.AsyncClient(
            project=_helpers.EMULATOR_PROJECT,
            credentials=credentials,
        )
    elif _helpers.USE_SPANNER_OMNI:
        return spanner_v1.AsyncClient(
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
        return spanner_v1.AsyncClient(client_options=client_options)


@pytest.fixture(autouse=True)
def reset_cached_apis(request, spanner_client):
    """Reset cached API clients to prevent Event Loop is closed errors between tests."""
    spanner_client._database_admin_api = None
    spanner_client._instance_admin_api = None
    if "shared_database" in request.fixturenames:
        try:
            db = request.getfixturevalue("shared_database")
            if hasattr(db, "_spanner_api"):
                db._spanner_api = None
        except Exception:
            pass


@pytest.fixture(scope="session")
def instance_operation_timeout():
    return _helpers.INSTANCE_OPERATION_TIMEOUT_IN_SECONDS


@pytest.fixture(scope="session")
def database_operation_timeout():
    return _helpers.DATABASE_OPERATION_TIMEOUT_IN_SECONDS


@pytest.fixture(scope="session")
def shared_instance_id():
    if _helpers.CREATE_INSTANCE:
        return f"{_helpers.unique_id('g-c-async')}"
    if _helpers.USE_SPANNER_OMNI:
        return _helpers.SPANNER_OMNI_INSTANCE
    return _helpers.INSTANCE_ID


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

    dirname = os.path.dirname(os.path.dirname(__file__))
    filename = os.path.join(dirname, "testdata/descriptors.pb")
    file = open(filename, "rb")
    yield file.read()
    file.close()


@pytest.fixture(scope="session")
async def instance_configs(spanner_client):
    configs = []
    async for config in await spanner_client.list_instance_configs():
        configs.append(config)

    if not _helpers.USE_EMULATOR and not _helpers.USE_SPANNER_OMNI:
        # Defend against back-end returning configs for regions we aren't
        # actually allowed to use.
        configs = [config for config in configs if "-us-" in config.name]

    yield configs


@pytest.fixture(scope="session")
async def instance_config(instance_configs):
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
async def shared_instance(
    spanner_client,
    instance_operation_timeout,
    shared_instance_id,
    instance_config,
):
    spanner_client._instance_admin_api = None

    if _helpers.CREATE_INSTANCE:
        import time

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
        created_op = await spanner_client.instance_admin_api.create_instance(
            request=request
        )
        await created_op.result(instance_operation_timeout)

        instance = spanner_client.instance(
            shared_instance_id, instance_config.name, labels=labels
        )
    else:
        instance = spanner_client.instance(shared_instance_id, instance_config.name)
        await instance.reload()

    yield instance

    if _helpers.CREATE_INSTANCE:
        await instance.delete()


@pytest.fixture(scope="session")
async def shared_database(
    shared_instance, database_operation_timeout, database_dialect, proto_descriptor_file
):
    spanner_client = shared_instance._client
    spanner_client._database_admin_api = None
    database_name = _helpers.unique_id("test_db_async")
    pool = spanner_v1.AsyncBurstyPool(labels={"testcase": "database_api_async"})

    if database_dialect == DatabaseDialect.POSTGRESQL:
        database = await shared_instance.database(
            database_name,
            pool=pool,
            database_dialect=database_dialect,
        )
        op = await database.create()
        await op.result(database_operation_timeout)

        op = await database.update_ddl(ddl_statements=_helpers.DDL_STATEMENTS)
        await op.result(database_operation_timeout)
    else:
        database = await shared_instance.database(
            database_name,
            ddl_statements=_helpers.DDL_STATEMENTS,
            pool=pool,
            database_dialect=database_dialect,
            proto_descriptors=proto_descriptor_file,
        )
        op = await database.create()
        await op.result(database_operation_timeout)

    yield database

    try:
        await database.drop()
        await database.close()
    except RuntimeError:
        pass


@pytest.fixture(scope="function")
async def databases_to_delete():
    to_delete = []
    yield to_delete
    for db in to_delete:
        await db.drop()
        await db.close()


@pytest.fixture(scope="session")
def not_postgres(database_dialect):
    if database_dialect == DatabaseDialect.POSTGRESQL:
        pytest.skip("Skip for Postgres")


@pytest.fixture(scope="function")
def not_emulator():
    if _helpers.USE_EMULATOR:
        pytest.skip(f"{_helpers.USE_EMULATOR_ENVVAR} set in environment.")
