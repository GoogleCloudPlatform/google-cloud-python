# Copyright 2020 Google LLC
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
import importlib
import sys
from unittest import mock

try:
    import opentelemetry.sdk as opentelemetry
except ImportError:
    opentelemetry = None

if opentelemetry is not None:
    try:
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
    except (ImportError, AttributeError) as exc:  # pragma: NO COVER
        msg = "Error importing from opentelemetry, is the installed version compatible?"
        raise ImportError(msg) from exc

import pytest

from google.cloud.bigquery import opentelemetry_tracing

TEST_SPAN_NAME = "bar"
TEST_SPAN_ATTRIBUTES = {"foo": "baz"}


@pytest.fixture
def setup():
    importlib.reload(opentelemetry_tracing)
    tracer_provider = TracerProvider()
    memory_exporter = InMemorySpanExporter()
    span_processor = SimpleSpanProcessor(memory_exporter)
    tracer_provider.add_span_processor(span_processor)

    # OpenTelemetry API >= 0.12b0 does not allow overriding the tracer once
    # initialized, thus directly override (and then restore) the internal global var.
    orig_trace_provider = trace._TRACER_PROVIDER
    trace._TRACER_PROVIDER = tracer_provider

    yield memory_exporter

    trace._TRACER_PROVIDER = orig_trace_provider


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_opentelemetry_not_installed(setup, monkeypatch):
    monkeypatch.setitem(sys.modules, "opentelemetry", None)
    importlib.reload(opentelemetry_tracing)
    assert not opentelemetry_tracing._warned_telemetry
    with opentelemetry_tracing.create_span("No-op for opentelemetry") as span:
        assert span is None
        assert opentelemetry_tracing._warned_telemetry


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_opentelemetry_not_installed_doesnt_warn(setup, monkeypatch):
    monkeypatch.setitem(sys.modules, "opentelemetry", None)
    importlib.reload(opentelemetry_tracing)
    opentelemetry_tracing._warned_telemetry = True
    with opentelemetry_tracing.create_span("No-op for opentelemetry") as span:
        assert span is None
        assert opentelemetry_tracing._warned_telemetry


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_opentelemetry_success(setup):
    expected_attributes = {"foo": "baz", "db.system": "BigQuery"}

    with opentelemetry_tracing.create_span(
        TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, client=None, job_ref=None
    ) as span:
        assert span is not None
        assert span.name == TEST_SPAN_NAME
        assert span.attributes == expected_attributes


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_default_client_attributes(setup):
    expected_attributes = {
        "foo": "baz",
        "db.system": "BigQuery",
        "db.name": "test_project",
        "location": "test_location",
    }
    with mock.patch("google.cloud.bigquery.client.Client") as test_client:
        test_client.project = "test_project"
        test_client.location = "test_location"
        with opentelemetry_tracing.create_span(
            TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, client=test_client
        ) as span:
            assert span is not None
            assert span.name == TEST_SPAN_NAME
            assert span.attributes == expected_attributes


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_default_job_attributes(setup):
    import google.cloud._helpers

    time_created = datetime.datetime(
        2010, 5, 19, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    started_time = datetime.datetime(
        2011, 10, 1, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    ended_time = datetime.datetime(
        2011, 10, 2, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )
    error_result = [
        {"errorResult1": "some_error_result1", "errorResult2": "some_error_result2"}
    ]

    expected_attributes = {
        "db.system": "BigQuery",
        "db.name": "test_project_id",
        "location": "test_location",
        "num_child_jobs": "0",
        "job_id": "test_job_id",
        "foo": "baz",
        "parent_job_id": "parent_job_id",
        "timeCreated": time_created.isoformat(),
        "timeStarted": started_time.isoformat(),
        "timeEnded": ended_time.isoformat(),
        "hasErrors": True,
        "state": "some_job_state",
        "total_bytes_billed": 42,
        "total_bytes_processed": 13,
    }
    with mock.patch("google.cloud.bigquery.job._AsyncJob") as test_job_ref:
        test_job_ref.job_id = "test_job_id"
        test_job_ref.location = "test_location"
        test_job_ref.project = "test_project_id"
        test_job_ref.num_child_jobs = "0"
        test_job_ref.parent_job_id = "parent_job_id"
        test_job_ref.created = time_created
        test_job_ref.started = started_time
        test_job_ref.ended = ended_time
        test_job_ref.error_result = error_result
        test_job_ref.state = "some_job_state"
        test_job_ref.total_bytes_billed = 42
        test_job_ref.total_bytes_processed = 13

        with opentelemetry_tracing.create_span(
            TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, job_ref=test_job_ref
        ) as span:
            assert span is not None
            assert span.name == TEST_SPAN_NAME
            assert span.attributes == expected_attributes


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_optional_job_attributes(setup):
    # This test ensures we don't propagate unset values into span attributes
    import google.cloud._helpers

    time_created = datetime.datetime(
        2010, 5, 19, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
    )

    with mock.patch("google.cloud.bigquery.job._AsyncJob") as test_job_ref:
        test_job_ref.job_id = "test_job_id"
        test_job_ref.location = None
        test_job_ref.project = "test_project_id"
        test_job_ref.created = time_created
        test_job_ref.state = "some_job_state"
        test_job_ref.num_child_jobs = None
        test_job_ref.parent_job_id = None
        test_job_ref.total_bytes_billed = None
        test_job_ref.total_bytes_processed = None

        with opentelemetry_tracing.create_span(
            TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, job_ref=test_job_ref
        ) as span:
            assert span is not None
            for val in span.attributes.values():
                assert val is not None


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_default_no_data_leakage(setup):
    import google.auth.credentials
    from google.cloud.bigquery import client
    from google.cloud.bigquery import job

    mock_credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    test_client = client.Client(
        project="test_project", credentials=mock_credentials, location="test_location"
    )

    expected_attributes = {
        "foo": "baz",
        "db.system": "BigQuery",
        "db.name": "test_project",
        "location": "test_location",
    }
    with opentelemetry_tracing.create_span(
        TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, client=test_client
    ) as span:
        assert span.name == TEST_SPAN_NAME
        assert span.attributes == expected_attributes

    test_job_reference = job._JobReference(
        job_id="test_job_id", project="test_project_id", location="test_location"
    )
    test_client = client.Client(
        project="test_project", credentials=mock_credentials, location="test_location"
    )
    test_job = job._AsyncJob(job_id=test_job_reference, client=test_client)

    expected_attributes = {
        "db.system": "BigQuery",
        "db.name": "test_project_id",
        "location": "test_location",
        "num_child_jobs": 0,
        "job_id": "test_job_id",
        "foo": "baz",
        "hasErrors": False,
    }

    with opentelemetry_tracing.create_span(
        TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, job_ref=test_job
    ) as span:
        assert span.name == TEST_SPAN_NAME
        assert span.attributes == expected_attributes


@pytest.mark.skipif(opentelemetry is None, reason="Require `opentelemetry`")
def test_span_creation_error(setup):
    import google.auth.credentials
    from google.cloud.bigquery import client
    from google.api_core.exceptions import GoogleAPICallError, InvalidArgument

    mock_credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    test_client = client.Client(
        project="test_project", credentials=mock_credentials, location="test_location"
    )

    expected_attributes = {
        "foo": "baz",
        "db.system": "BigQuery",
        "db.name": "test_project",
        "location": "test_location",
    }
    with pytest.raises(GoogleAPICallError):
        with opentelemetry_tracing.create_span(
            TEST_SPAN_NAME, attributes=TEST_SPAN_ATTRIBUTES, client=test_client
        ) as span:
            assert span.name == TEST_SPAN_NAME
            assert span.attributes == expected_attributes
            raise InvalidArgument("test_error")
