# Copyright 2025 Google LLC
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

from unittest import mock

import pytest

from google.cloud.spanner_v1.metrics.metrics_tracer import MetricsTracer
from google.cloud.spanner_v1.metrics.metrics_tracer_factory import MetricsTracerFactory

pytest.importorskip("opentelemetry")


@pytest.fixture
def metrics_tracer_factory():
    factory = MetricsTracerFactory(
        enabled=True,
        service_name="test_service",
    )
    factory.set_project("test_project").set_instance(
        "test_instance"
    ).set_instance_config("test_config").set_location("test_location").set_client_hash(
        "test_hash"
    ).set_client_uid("test_uid").set_client_name("test_name").set_database(
        "test_db"
    ).enable_direct_path(False)
    return factory


def test_initialization(metrics_tracer_factory):
    assert metrics_tracer_factory.enabled is True
    assert metrics_tracer_factory.client_attributes["project_id"] == "test_project"


def test_create_metrics_tracer(metrics_tracer_factory):
    tracer = metrics_tracer_factory.create_metrics_tracer()
    assert isinstance(tracer, MetricsTracer)


def test_client_attributes(metrics_tracer_factory):
    attributes = metrics_tracer_factory.client_attributes
    assert attributes["project_id"] == "test_project"
    assert attributes["instance_id"] == "test_instance"


def test_create_metrics_tracer_with_resource_info():
    factory = MetricsTracerFactory(
        enabled=True,
        service_name="test_service",
    )
    resource_info = {
        "project": "custom_project",
        "instance": "custom_instance",
        "database": "custom_database",
    }
    tracer = factory.create_metrics_tracer(resource_info)
    assert isinstance(tracer, MetricsTracer)
    assert tracer.client_attributes["project_id"] == "custom_project"
    assert tracer.client_attributes["instance_id"] == "custom_instance"
    assert tracer.client_attributes["database"] == "custom_database"


def test_create_resource_info_and_tracer():
    factory = MetricsTracerFactory(
        enabled=True,
        service_name="test_service",
    )
    resource_info = factory.create_resource_info(
        project="pre_proj",
        instance="pre_inst",
        database="pre_db",
    )
    assert resource_info["project"] == "pre_proj"
    assert resource_info["instance"] == "pre_inst"
    assert resource_info["database"] == "pre_db"
    assert getattr(resource_info, "_client_attributes") is not None
    assert resource_info._client_attributes["project_id"] == "pre_proj"
    assert resource_info._client_attributes["instance_id"] == "pre_inst"
    assert resource_info._client_attributes["database"] == "pre_db"

    tracer = factory.create_metrics_tracer(resource_info)
    assert isinstance(tracer, MetricsTracer)
    assert tracer.client_attributes["project_id"] == "pre_proj"
    assert tracer.client_attributes["instance_id"] == "pre_inst"
    assert tracer.client_attributes["database"] == "pre_db"


def test_create_resource_info_partial_arguments():
    factory = MetricsTracerFactory(
        enabled=True,
        service_name="test_service",
    )
    resource_info = factory.create_resource_info(
        project="pre_proj",
        instance=None,
        database=None,
    )
    assert resource_info["project"] == "pre_proj"
    assert resource_info["instance"] is None
    assert resource_info["database"] is None
    assert "project_id" in resource_info._client_attributes
    assert "instance_id" not in resource_info._client_attributes
    assert "database" not in resource_info._client_attributes


def test_create_metrics_tracer_with_mock_resource_info():
    factory = MetricsTracerFactory(
        enabled=True,
        service_name="test_service",
    )
    # MagicMock dynamically returns a child Mock for _client_attributes
    mock_info = mock.MagicMock()
    mock_info.get.side_effect = lambda k: {"project": "mock_p"}.get(k)
    tracer = factory.create_metrics_tracer(mock_info)
    assert isinstance(tracer, MetricsTracer)
    # client_attributes must be a dict, not a MagicMock
    assert isinstance(tracer.client_attributes, dict)
    assert tracer.client_attributes["project_id"] == "mock_p"


def test_create_metrics_tracer_without_opentelemetry():
    factory = MetricsTracerFactory(enabled=True, service_name="test_service")
    with mock.patch(
        "google.cloud.spanner_v1.metrics.metrics_tracer_factory.HAS_OPENTELEMETRY_INSTALLED",
        False,
    ):
        assert factory.create_metrics_tracer() is None
        res_info = factory.create_resource_info(project="p", instance="i", database="d")
        assert res_info["project"] == "p"
        assert getattr(res_info, "_client_attributes", None) is None


def test_create_resource_info_does_not_overwrite_existing_attributes():
    factory = MetricsTracerFactory(enabled=True, service_name="test_service")
    factory.set_project("factory_proj")
    factory.set_instance("factory_inst")
    factory.set_database("factory_db")
    resource_info = factory.create_resource_info(
        project="new_proj",
        instance="new_inst",
        database="new_db",
    )
    assert resource_info._client_attributes["project_id"] == "factory_proj"
    assert resource_info._client_attributes["instance_id"] == "factory_inst"
    assert resource_info._client_attributes["database"] == "factory_db"
