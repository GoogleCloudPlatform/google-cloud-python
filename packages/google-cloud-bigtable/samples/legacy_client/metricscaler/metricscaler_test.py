# Copyright 2017 Google Inc.
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

import pytest
from mock import Mock, patch
from test_utils.retry import RetryInstanceState, RetryResult

from google.cloud import bigtable
from google.cloud.bigtable import enums

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

    client = bigtable.Client(project=PROJECT, admin=True)

    serve_nodes = 1
    storage_type = enums.StorageType.SSD
    production = enums.Instance.Type.PRODUCTION
    labels = {"prod-label": "prod-label"}
    instance = client.instance(
        BIGTABLE_INSTANCE, instance_type=production, labels=labels
    )

    if not instance.exists():
        cluster = instance.cluster(
            cluster_id,
            location_id=BIGTABLE_ZONE,
            serve_nodes=serve_nodes,
            default_storage_type=storage_type,
        )
        operation = instance.create(clusters=[cluster])
        response = operation.result(480)
        print(f"Successfully created {response.name}")

        # Eventual consistency check
        retry_found = RetryResult(bool)
        retry_found(instance.exists)()

    yield

    instance.delete()


@pytest.fixture()
def dev_instance():
    cluster_id = BIGTABLE_DEV_INSTANCE

    client = bigtable.Client(project=PROJECT, admin=True)

    storage_type = enums.StorageType.SSD
    development = enums.Instance.Type.DEVELOPMENT
    labels = {"dev-label": "dev-label"}
    instance = client.instance(
        BIGTABLE_DEV_INSTANCE, instance_type=development, labels=labels
    )

    if not instance.exists():
        cluster = instance.cluster(
            cluster_id, location_id=BIGTABLE_ZONE, default_storage_type=storage_type
        )
        operation = instance.create(clusters=[cluster])
        response = operation.result(480)
        print(f"Successfully created {response.name}")

        # Eventual consistency check
        retry_found = RetryResult(bool)
        retry_found(instance.exists)()

    yield

    instance.delete()


class ClusterNodeCountPredicate:
    def __init__(self, expected_node_count):
        self.expected_node_count = expected_node_count

    def __call__(self, cluster):
        expected = self.expected_node_count
        print(f"Expected node count: {expected}; found: {cluster.serve_nodes}")
        return cluster.serve_nodes == expected


def test_scale_bigtable(instance):
    bigtable_client = bigtable.Client(admin=True)

    instance = bigtable_client.instance(BIGTABLE_INSTANCE)
    instance.reload()

    cluster = instance.cluster(BIGTABLE_INSTANCE)

    _nonzero_node_count = RetryInstanceState(
        instance_predicate=lambda c: c.serve_nodes > 0,
        max_tries=10,
    )
    _nonzero_node_count(cluster.reload)()

    original_node_count = cluster.serve_nodes

    scale_bigtable(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, True)

    scaled_node_count_predicate = ClusterNodeCountPredicate(
        original_node_count + SIZE_CHANGE_STEP
    )
    scaled_node_count_predicate.__name__ = "scaled_node_count_predicate"
    _scaled_node_count = RetryInstanceState(
        instance_predicate=scaled_node_count_predicate,
        max_tries=10,
    )
    _scaled_node_count(cluster.reload)()

    scale_bigtable(BIGTABLE_INSTANCE, BIGTABLE_INSTANCE, False)

    restored_node_count_predicate = ClusterNodeCountPredicate(original_node_count)
    restored_node_count_predicate.__name__ = "restored_node_count_predicate"
    _restored_node_count = RetryInstanceState(
        instance_predicate=restored_node_count_predicate,
        max_tries=10,
    )
    _restored_node_count(cluster.reload)()


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
