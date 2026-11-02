# Copyright 2011 Google LLC
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

import pytest
from google.cloud.environment_vars import BIGTABLE_EMULATOR
from test_utils.system import unique_resource_id

from google.cloud.bigtable.client import Client

from . import _helpers


@pytest.fixture(scope="session")
def in_emulator():
    return os.getenv(BIGTABLE_EMULATOR) is not None


@pytest.fixture(scope="session")
def kms_key_name():
    return os.getenv("KMS_KEY_NAME")


@pytest.fixture(scope="session")
def with_kms_key_name(kms_key_name):
    if kms_key_name is None:
        pytest.skip("Test requires KMS_KEY_NAME environment variable")
    return kms_key_name


@pytest.fixture(scope="session")
def skip_on_emulator(in_emulator):
    if in_emulator:
        pytest.skip("Emulator does not support this feature")


@pytest.fixture(scope="session")
def unique_suffix():
    return unique_resource_id("-")


@pytest.fixture(scope="session")
def location_id():
    return "us-central1-c"


@pytest.fixture(scope="session")
def serve_nodes():
    return 3


@pytest.fixture(scope="session")
def label_key():
    return "python-system"


@pytest.fixture(scope="session")
def instance_labels(label_key):
    return {label_key: _helpers.label_stamp()}


@pytest.fixture(scope="session")
def admin_client():
    return Client(admin=True)


@pytest.fixture(scope="session")
def service_account(admin_client):
    from google.oauth2.service_account import Credentials

    if not isinstance(admin_client._credentials, Credentials):
        pytest.skip("These tests require a service account credential")
    return admin_client._credentials


@pytest.fixture(scope="session")
def admin_instance_id(unique_suffix):
    return f"g-c-p{unique_suffix}"


@pytest.fixture(scope="session")
def admin_cluster_id(admin_instance_id):
    return f"{admin_instance_id}-cluster"


@pytest.fixture(scope="session")
def admin_instance(admin_client, admin_instance_id, instance_labels):
    return admin_client.instance(admin_instance_id, labels=instance_labels)


@pytest.fixture(scope="session")
def admin_cluster(admin_instance, admin_cluster_id, location_id, serve_nodes):
    return admin_instance.cluster(
        admin_cluster_id,
        location_id=location_id,
        serve_nodes=serve_nodes,
    )


@pytest.fixture(scope="session")
def admin_cluster_with_autoscaling(
    admin_instance,
    admin_cluster_id,
    location_id,
    min_serve_nodes,
    max_serve_nodes,
    cpu_utilization_percent,
):
    return admin_instance.cluster(
        admin_cluster_id,
        location_id=location_id,
        min_serve_nodes=min_serve_nodes,
        max_serve_nodes=max_serve_nodes,
        cpu_utilization_percent=cpu_utilization_percent,
    )


@pytest.fixture(scope="session")
def admin_instance_populated(admin_instance, admin_cluster, in_emulator):
    # Emulator does not support instance admin operations (create / delete).
    # See: https://cloud.google.com/bigtable/docs/emulator
    if not in_emulator:
        operation = admin_instance.create(clusters=[admin_cluster])
        operation.result(timeout=240)

    yield admin_instance

    if not in_emulator:
        _helpers.retry_429(admin_instance.delete)()


@pytest.fixture(scope="session")
def data_client():
    return Client(admin=False)


@pytest.fixture(scope="session")
def data_instance_id(unique_suffix):
    return f"g-c-p-d{unique_suffix}"


@pytest.fixture(scope="session")
def data_cluster_id(data_instance_id):
    return f"{data_instance_id}-cluster"


@pytest.fixture(scope="session")
def data_instance_populated(
    admin_client,
    data_instance_id,
    instance_labels,
    data_cluster_id,
    location_id,
    serve_nodes,
    in_emulator,
):
    instance = admin_client.instance(data_instance_id, labels=instance_labels)
    # Emulator does not support instance admin operations (create / delete).
    # See: https://cloud.google.com/bigtable/docs/emulator
    if not in_emulator:
        cluster = instance.cluster(
            data_cluster_id,
            location_id=location_id,
            serve_nodes=serve_nodes,
        )
        operation = instance.create(clusters=[cluster])
        operation.result(timeout=240)

    yield instance

    if not in_emulator:
        _helpers.retry_429(instance.delete)()


@pytest.fixture(scope="function")
def instances_to_delete():
    instances_to_delete = []

    yield instances_to_delete

    for instance in instances_to_delete:
        _helpers.retry_429(instance.delete)()


@pytest.fixture(scope="session")
def min_serve_nodes(in_emulator):
    return 1


@pytest.fixture(scope="session")
def max_serve_nodes(in_emulator):
    return 8


@pytest.fixture(scope="session")
def cpu_utilization_percent(in_emulator):
    return 10
