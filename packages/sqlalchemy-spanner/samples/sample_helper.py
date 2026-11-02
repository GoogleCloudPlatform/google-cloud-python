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

import os
from typing import Callable

from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import AlreadyExists
from google.auth.credentials import AnonymousCredentials
from google.cloud.spanner_v1 import Client
from google.cloud.spanner_v1.database import Database
from model import Base
from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs


def run_sample(sample_method: Callable):
    registry.register(
        "spanner",
        "google.cloud.sqlalchemy_spanner.sqlalchemy_spanner",
        "SpannerDialect",
    )
    emulator = None
    if os.getenv("USE_EXISTING_EMULATOR") == "true":
        if os.getenv("SPANNER_EMULATOR_HOST") is None:
            os.environ["SPANNER_EMULATOR_HOST"] = "localhost:9010"
            _create_instance_and_database("9010")
    else:
        os.environ["SPANNER_EMULATOR_HOST"] = ""
        emulator, port = start_emulator()
        os.environ["SPANNER_EMULATOR_HOST"] = "localhost:" + str(port)
    try:
        _create_tables()
        sample_method()
    finally:
        if emulator is not None:
            emulator.stop()


def start_emulator() -> (DockerContainer, str):
    emulator = DockerContainer(
        "gcr.io/cloud-spanner-emulator/emulator"
    ).with_exposed_ports(9010)
    emulator.start()
    wait_for_logs(emulator, "gRPC server listening at 0.0.0.0:9010")
    port = str(emulator.get_exposed_port(9010))
    _create_instance_and_database(port)
    return emulator, port


def _create_instance_and_database(port: str):
    client = Client(
        project="sample-project",
        credentials=AnonymousCredentials(),
        client_options=ClientOptions(
            api_endpoint="localhost:" + port,
        ),
    )
    configs = list(client.list_instance_configs())
    instance_config = configs[0].name
    instance_id = "sample-instance"
    database_id = "sample-database"

    instance = client.instance(instance_id, instance_config)
    try:
        created_op = instance.create()
        created_op.result(1800)  # block until completion
    except AlreadyExists:
        # Ignore
        print("Using existing instance")

    database: Database = instance.database(database_id)
    if database.exists():
        database.drop()
    created_op = database.create()
    created_op.result(1800)


def _create_tables():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    Base.metadata.create_all(engine)
