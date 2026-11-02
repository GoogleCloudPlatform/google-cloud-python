# -*- coding: utf-8 -*-
#
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest


@pytest.fixture
def target_class():
    from google.cloud.bigquery.routine.routine import ExternalRuntimeOptions

    return ExternalRuntimeOptions


@pytest.fixture
def object_under_test(target_class):
    return target_class()


def test_ctor(target_class):
    container_memory = "1G"
    container_cpu = 1
    runtime_connection = (
        "projects/my-project/locations/us-central1/connections/my-connection"
    )
    max_batching_rows = 100
    runtime_version = "python-3.11"

    instance = target_class(
        container_memory=container_memory,
        container_cpu=container_cpu,
        runtime_connection=runtime_connection,
        max_batching_rows=max_batching_rows,
        runtime_version=runtime_version,
    )

    assert instance.container_memory == container_memory
    assert instance.container_cpu == container_cpu
    assert instance.runtime_connection == runtime_connection
    assert instance.max_batching_rows == max_batching_rows
    assert instance.runtime_version == runtime_version


def test_container_memory(object_under_test):
    container_memory = "512Mi"
    object_under_test.container_memory = container_memory
    assert object_under_test.container_memory == container_memory


def test_container_cpu(object_under_test):
    container_cpu = 1
    object_under_test.container_cpu = container_cpu
    assert object_under_test.container_cpu == container_cpu


def test_runtime_connection(object_under_test):
    runtime_connection = (
        "projects/my-project/locations/us-central1/connections/my-connection"
    )
    object_under_test.runtime_connection = runtime_connection
    assert object_under_test.runtime_connection == runtime_connection


def test_max_batching_rows(object_under_test):
    max_batching_rows = 100
    object_under_test.max_batching_rows = max_batching_rows
    assert object_under_test.max_batching_rows == max_batching_rows


def test_runtime_version(object_under_test):
    runtime_version = "python-3.11"
    object_under_test.runtime_version = runtime_version
    assert object_under_test.runtime_version == runtime_version


def test_ctor_w_properties(target_class):
    properties = {
        "containerMemory": "1G",
        "containerCpu": 1,
    }
    instance = target_class(_properties=properties)
    assert instance._properties == properties


def test_ne(target_class):
    instance1 = target_class(container_memory="1G")
    instance2 = target_class(container_memory="2G")
    assert instance1 != instance2


def test_ne_false(target_class):
    instance1 = target_class(container_memory="1G")
    instance2 = target_class(container_memory="1G")
    assert not (instance1 != instance2)


def test_eq_not_implemented(object_under_test):
    assert not (object_under_test == object())
    assert object_under_test != object()


def test_from_api_repr(target_class):
    resource = {
        "containerMemory": "1G",
        "containerCpu": 1,
        "runtimeConnection": "projects/my-project/locations/us-central1/connections/my-connection",
        "maxBatchingRows": "100",
        "runtimeVersion": "python-3.11",
    }
    instance = target_class.from_api_repr(resource)

    assert instance.container_memory == "1G"
    assert instance.container_cpu == 1
    assert (
        instance.runtime_connection
        == "projects/my-project/locations/us-central1/connections/my-connection"
    )
    assert instance.max_batching_rows == 100
    assert instance.runtime_version == "python-3.11"


def test_to_api_repr(target_class):
    instance = target_class(
        container_memory="1G",
        container_cpu=1,
        runtime_connection="projects/my-project/locations/us-central1/connections/my-connection",
        max_batching_rows=100,
        runtime_version="python-3.11",
    )
    resource = instance.to_api_repr()

    assert resource == {
        "containerMemory": "1G",
        "containerCpu": 1,
        "runtimeConnection": "projects/my-project/locations/us-central1/connections/my-connection",
        "maxBatchingRows": "100",
        "runtimeVersion": "python-3.11",
    }


def test_repr(target_class):
    instance = target_class(
        container_memory="1G",
        container_cpu=1,
    )
    expected_repr = (
        "ExternalRuntimeOptions(container_cpu=1, container_memory='1G', "
        "max_batching_rows=None, runtime_connection=None, runtime_version=None)"
    )
    assert repr(instance) == expected_repr


def test_invalid_container_memory(object_under_test):
    with pytest.raises(ValueError, match="container_memory must be a string or None."):
        object_under_test.container_memory = 123


def test_invalid_container_cpu(object_under_test):
    with pytest.raises(ValueError, match="container_cpu must be an integer or None."):
        object_under_test.container_cpu = "1"


def test_invalid_runtime_connection(object_under_test):
    with pytest.raises(
        ValueError, match="runtime_connection must be a string or None."
    ):
        object_under_test.runtime_connection = 123


def test_invalid_max_batching_rows(object_under_test):
    with pytest.raises(
        ValueError, match="max_batching_rows must be an integer or None."
    ):
        object_under_test.max_batching_rows = "100"


def test_invalid_runtime_version(object_under_test):
    with pytest.raises(ValueError, match="runtime_version must be a string or None."):
        object_under_test.runtime_version = 123
