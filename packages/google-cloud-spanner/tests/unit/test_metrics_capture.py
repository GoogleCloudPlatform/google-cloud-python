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

from google.cloud.spanner_v1.metrics.metrics_capture import MetricsCapture
from google.cloud.spanner_v1.metrics.metrics_tracer_factory import MetricsTracerFactory
from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
    SpannerMetricsTracerFactory,
)


@pytest.fixture
def mock_tracer_factory():
    SpannerMetricsTracerFactory(enabled=True)
    with mock.patch.object(
        MetricsTracerFactory, "create_metrics_tracer"
    ) as mock_create:
        yield mock_create


def test_metrics_capture_enter(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    with MetricsCapture() as capture:
        assert capture is not None
        mock_tracer_factory.assert_called_once()
        mock_tracer.record_operation_start.assert_called_once()


def test_metrics_capture_exit(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    with MetricsCapture():
        pass

    mock_tracer.record_operation_completion.assert_called_once()


def test_metrics_capture_reuse(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    capture = MetricsCapture()
    with capture:
        assert SpannerMetricsTracerFactory.get_current_tracer() is mock_tracer

    assert SpannerMetricsTracerFactory.get_current_tracer() is None
    assert capture._token is None
    assert capture._tracer is None

    # Reusing the same context manager instance must not raise an error
    with capture:
        assert SpannerMetricsTracerFactory.get_current_tracer() is mock_tracer

    assert SpannerMetricsTracerFactory.get_current_tracer() is None
    assert capture._token is None
    assert capture._tracer is None


def test_metrics_capture_with_resource_info(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer
    resource_info = {
        "project": "test-project",
        "instance": "test-instance",
        "database": "test-database",
    }

    with MetricsCapture(resource_info):
        pass

    mock_tracer_factory.assert_called_once_with(resource_info)
    mock_tracer.record_operation_completion.assert_called_once()


def test_metrics_capture_retains_tracer_when_context_cleared(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    with MetricsCapture() as capture:
        # Simulate inner code modifying or clearing current tracer
        assert capture._tracer is mock_tracer

    mock_tracer.record_operation_completion.assert_called_once()


def test_metrics_capture_handles_value_error_on_reset(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    with mock.patch.object(
        SpannerMetricsTracerFactory,
        "reset_current_tracer",
        side_effect=ValueError("Token was created in a different Context"),
    ):
        # Exiting context must not raise ValueError
        with MetricsCapture():
            pass

    mock_tracer.record_operation_completion.assert_called_once()


def test_metrics_capture_disabled():
    SpannerMetricsTracerFactory(enabled=False)
    try:
        with MetricsCapture() as capture:
            assert capture is not None
            assert capture._token is None
            assert SpannerMetricsTracerFactory.get_current_tracer() is None
    finally:
        SpannerMetricsTracerFactory(enabled=True)


def test_metrics_capture_exit_without_token():
    capture = MetricsCapture()
    assert capture.__exit__(None, None, None) is False


def test_metrics_capture_partial_resource_info(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    with MetricsCapture({"project": "p"}):
        pass
    mock_tracer_factory.assert_called_once_with({"project": "p"})

    mock_tracer_factory.reset_mock()
    mock_tracer.reset_mock()
    with MetricsCapture({"instance": "i"}):
        pass
    mock_tracer_factory.assert_called_once_with({"instance": "i"})

    mock_tracer_factory.reset_mock()
    mock_tracer.reset_mock()
    with MetricsCapture({"database": "d"}):
        pass
    mock_tracer_factory.assert_called_once_with({"database": "d"})


def test_metrics_capture_tracer_is_none(mock_tracer_factory):
    mock_tracer_factory.return_value = None
    with MetricsCapture():
        pass


def test_metrics_capture_exit_suppresses_metrics_tracer_exception(
    mock_tracer_factory,
):
    mock_tracer = mock.Mock()
    mock_tracer.record_operation_completion.side_effect = RuntimeError(
        "metrics recording failed"
    )
    mock_tracer_factory.return_value = mock_tracer

    # Exception from record_operation_completion must be caught and not propagated
    with MetricsCapture():
        pass
    mock_tracer.record_operation_completion.assert_called_once()


def test_metrics_capture_without_opentelemetry():
    with mock.patch(
        "google.cloud.spanner_v1.metrics.metrics_capture.HAS_OPENTELEMETRY_INSTALLED",
        False,
    ):
        with MetricsCapture() as capture:
            assert capture._token is None


def test_metrics_capture_enter_resets_token_on_start_failure(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer.record_operation_start.side_effect = RuntimeError("start failed")
    mock_tracer_factory.return_value = mock_tracer

    capture = MetricsCapture()
    with pytest.raises(RuntimeError):
        with capture:
            pass

    assert capture._token is None
    assert capture._tracer is None


def test_metrics_capture_enter_resets_token_when_token_is_none(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer.record_operation_start.side_effect = RuntimeError("start failed")
    mock_tracer_factory.return_value = mock_tracer

    capture = MetricsCapture()
    with mock.patch.object(
        SpannerMetricsTracerFactory,
        "set_current_tracer",
        return_value=None,
    ):
        with pytest.raises(RuntimeError):
            with capture:
                pass

    assert capture._token is None
    assert capture._tracer is None


def test_metrics_capture_enter_handles_value_error_on_reset(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer.record_operation_start.side_effect = RuntimeError("start failed")
    mock_tracer_factory.return_value = mock_tracer

    capture = MetricsCapture()
    with mock.patch.object(
        SpannerMetricsTracerFactory,
        "reset_current_tracer",
        side_effect=ValueError("Token was created in a different Context"),
    ):
        with pytest.raises(RuntimeError):
            with capture:
                pass

    assert capture._token is None
    assert capture._tracer is None


def test_metrics_capture_exit_error_resets_token(mock_tracer_factory):
    mock_tracer = mock.Mock()
    mock_tracer_factory.return_value = mock_tracer

    with pytest.raises(RuntimeError, match="User code failure"):
        with MetricsCapture():
            assert SpannerMetricsTracerFactory.get_current_tracer() is mock_tracer
            raise RuntimeError("User code failure")

    assert SpannerMetricsTracerFactory.get_current_tracer() is None
