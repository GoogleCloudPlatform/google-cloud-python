# Copyright 2026 Google LLC
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

"""Unit and system tests for metricscaler.py"""

import os
import uuid
from unittest.mock import Mock, patch

import pytest
from google.api_core.exceptions import NotFound
from test_utils.retry import RetryResult

from google.cloud import bigtable_admin_v2

from . import metricscaler
from .metricscaler import get_cpu_load, get_storage_utilization, main, scale_bigtable

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
BIGTABLE_ZONE = os.environ.get("BIGTABLE_ZONE", "us-central1-b")
SIZE_CHANGE_STEP = 3
INSTANCE_ID_FORMAT = "metric-scale-test-{}"
BIGTABLE_INSTANCE = INSTANCE_ID_FORMAT.format(str(uuid.uuid4())[:10])
BIGTABLE_DEV_INSTANCE = INSTANCE_ID_FORMAT.format(str(uuid.uuid4())[:10])


# System tests to verify API calls succeed


@patch.object(metricscaler, "query")
def test_get_cpu_load(monitoring_v3_query):
    iter_mock = monitoring_v3_query.Query().select_resources().iter
    iter_mock.return_value = iter([Mock(points=[Mock(value=Mock(double_value=1.0))])])
    assert float(get_cpu_load(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE)) > 0.0


@patch.object(metricscaler, "query")
def test_get_storage_utilization(monitoring_v3_query):
    iter_mock = monitoring_v3_query.Query().select_resources().iter
    iter_mock.return_value = iter([Mock(points=[Mock(value=Mock(double_value=1.0))])])
    assert float(get_storage_utilization(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE)) > 0.0


@pytest.fixture()
def instance():
    cluster_id = BIGTABLE_INSTANCE

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    project_path = client.common_project_path(PROJECT)
    instance_path = client.instance_path(PROJECT, BIGTABLE_INSTANCE)

    cluster = bigtable_admin_v2.Cluster(
        location=client.common_location_path(PROJECT, BIGTABLE_ZONE),
        serve_nodes=1,
        default_storage_type=bigtable_admin_v2.StorageType.SSD,
    )
    instance_obj = bigtable_admin_v2.Instance(
        display_name=BIGTABLE_INSTANCE,
        type_=bigtable_admin_v2.Instance.Type.PRODUCTION,
        labels={"prod-label": "prod-label"},
    )

    try:
        client.get_instance(name=instance_path)
    except NotFound:
        operation = client.create_instance(
            parent=project_path,
            instance_id=BIGTABLE_INSTANCE,
            instance=instance_obj,
            clusters={cluster_id: cluster},
        )
        response = operation.result(480)
        print(f"Successfully created {response.name}")

    yield

    client.delete_instance(name=instance_path)


@pytest.fixture()
def dev_instance():
    cluster_id = BIGTABLE_DEV_INSTANCE

    client = bigtable_admin_v2.BigtableInstanceAdminClient()
    project_path = client.common_project_path(PROJECT)
    instance_path = client.instance_path(PROJECT, BIGTABLE_DEV_INSTANCE)

    cluster = bigtable_admin_v2.Cluster(
        location=client.common_location_path(PROJECT, BIGTABLE_ZONE),
        default_storage_type=bigtable_admin_v2.StorageType.SSD,
    )
    instance_obj = bigtable_admin_v2.Instance(
        display_name=BIGTABLE_DEV_INSTANCE,
        type_=bigtable_admin_v2.Instance.Type.DEVELOPMENT,
        labels={"dev-label": "dev-label"},
    )

    try:
        client.get_instance(name=instance_path)
    except NotFound:
        operation = client.create_instance(
            parent=project_path,
            instance_id=BIGTABLE_DEV_INSTANCE,
            instance=instance_obj,
            clusters={cluster_id: cluster},
        )
        response = operation.result(480)
        print(f"Successfully created {response.name}")

    yield

    client.delete_instance(name=instance_path)


class ClusterNodeCountPredicate:
    def __init__(self, expected_node_count):
        self.expected_node_count = expected_node_count

    def __call__(self, cluster):
        expected = self.expected_node_count
        print(f"Expected node count: {expected}; found: {cluster.serve_nodes}")
        return cluster.serve_nodes == expected


def test_scale_bigtable(instance):
    bigtable_client = bigtable_admin_v2.BigtableInstanceAdminClient()
    cluster_path = bigtable_client.cluster_path(
        PROJECT, BIGTABLE_INSTANCE, BIGTABLE_INSTANCE
    )

    def get_cluster():
        return bigtable_client.get_cluster(name=cluster_path)

    _nonzero_node_count = RetryResult(
        lambda c: c.serve_nodes > 0,
        max_tries=10,
    )
    cluster = _nonzero_node_count(get_cluster)()

    original_node_count = cluster.serve_nodes

    scale_bigtable(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, True)

    scaled_node_count_predicate = ClusterNodeCountPredicate(
        original_node_count + SIZE_CHANGE_STEP
    )
    scaled_node_count_predicate.__name__ = "scaled_node_count_predicate"
    _scaled_node_count = RetryResult(
        scaled_node_count_predicate,
        max_tries=10,
    )
    _scaled_node_count(get_cluster)()

    scale_bigtable(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, False)

    restored_node_count_predicate = ClusterNodeCountPredicate(original_node_count)
    restored_node_count_predicate.__name__ = "restored_node_count_predicate"
    _restored_node_count = RetryResult(
        restored_node_count_predicate,
        max_tries=10,
    )
    _restored_node_count(get_cluster)()


def test_handle_dev_instance(capsys, dev_instance):
    with pytest.raises(ValueError):
        scale_bigtable(BIGTABLE_DEV_INSTANCE, BIGTABLE_DEV_INSTANCE, True)


@patch("time.sleep")
@patch.object(metricscaler, "get_storage_utilization")
@patch.object(metricscaler, "get_cpu_load")
@patch.object(metricscaler, "scale_bigtable")
def test_main(scale_bigtable, get_cpu_load, get_storage_utilization, sleep):
    SHORT_SLEEP = 5
    LONG_SLEEP = 10

    # Test okay CPU, okay storage utilization
    get_cpu_load.return_value = 0.5
    get_storage_utilization.return_value = 0.5

    main(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, 0.6, 0.3, 0.6, SHORT_SLEEP, LONG_SLEEP)
    scale_bigtable.assert_not_called()
    scale_bigtable.reset_mock()

    # Test high CPU, okay storage utilization
    get_cpu_load.return_value = 0.7
    get_storage_utilization.return_value = 0.5
    main(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, 0.6, 0.3, 0.6, SHORT_SLEEP, LONG_SLEEP)
    scale_bigtable.assert_called_once_with(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, True)
    scale_bigtable.reset_mock()

    # Test low CPU, okay storage utilization
    get_storage_utilization.return_value = 0.5
    get_cpu_load.return_value = 0.2
    main(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, 0.6, 0.3, 0.6, SHORT_SLEEP, LONG_SLEEP)
    scale_bigtable.assert_called_once_with(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, False)
    scale_bigtable.reset_mock()

    # Test okay CPU, high storage utilization
    get_cpu_load.return_value = 0.5
    get_storage_utilization.return_value = 0.7

    main(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, 0.6, 0.3, 0.6, SHORT_SLEEP, LONG_SLEEP)
    scale_bigtable.assert_called_once_with(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, True)
    scale_bigtable.reset_mock()

    # Test high CPU, high storage utilization
    get_cpu_load.return_value = 0.7
    get_storage_utilization.return_value = 0.7
    main(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, 0.6, 0.3, 0.6, SHORT_SLEEP, LONG_SLEEP)
    scale_bigtable.assert_called_once_with(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, True)
    scale_bigtable.reset_mock()

    # Test low CPU, high storage utilization
    get_cpu_load.return_value = 0.2
    get_storage_utilization.return_value = 0.7
    main(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, 0.6, 0.3, 0.6, SHORT_SLEEP, LONG_SLEEP)
    scale_bigtable.assert_called_once_with(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, True)
    scale_bigtable.reset_mock()


if __name__ == "__main__":
    test_get_cpu_load()
