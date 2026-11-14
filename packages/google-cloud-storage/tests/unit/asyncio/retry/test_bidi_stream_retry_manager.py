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
from google.api_core import exceptions
from google.api_core.retry_async import AsyncRetry

from google.cloud.storage.asyncio.retry import base_strategy
from google.cloud.storage.asyncio.retry import (
    bidi_stream_retry_manager as manager,
)


def _is_retriable(exc):
    return isinstance(exc, exceptions.ServiceUnavailable)


DEFAULT_TEST_RETRY = AsyncRetry(predicate=_is_retriable, deadline=1)


class TestBidiStreamRetryManager:
    @pytest.mark.asyncio
    async def test_execute_success_on_first_try(self):
        mock_strategy = mock.AsyncMock(spec=base_strategy._BaseResumptionStrategy)

        async def mock_send_and_recv(*args, **kwargs):
            yield "response_1"

        retry_manager = manager._BidiStreamRetryManager(
            strategy=mock_strategy, send_and_recv=mock_send_and_recv
        )
        await retry_manager.execute(initial_state={}, retry_policy=DEFAULT_TEST_RETRY)
        mock_strategy.generate_requests.assert_called_once()
        mock_strategy.update_state_from_response.assert_called_once_with(
            "response_1", {}
        )
        mock_strategy.recover_state_on_failure.assert_not_called()

    @pytest.mark.asyncio
    async def test_execute_success_on_empty_stream(self):
        mock_strategy = mock.AsyncMock(spec=base_strategy._BaseResumptionStrategy)

        async def mock_send_and_recv(*args, **kwargs):
            if False:
                yield

        retry_manager = manager._BidiStreamRetryManager(
            strategy=mock_strategy, send_and_recv=mock_send_and_recv
        )
        await retry_manager.execute(initial_state={}, retry_policy=DEFAULT_TEST_RETRY)

        mock_strategy.generate_requests.assert_called_once()
        mock_strategy.update_state_from_response.assert_not_called()
        mock_strategy.recover_state_on_failure.assert_not_called()

    @pytest.mark.asyncio
    async def test_execute_retries_on_initial_failure_and_succeeds(self):
        mock_strategy = mock.AsyncMock(spec=base_strategy._BaseResumptionStrategy)
        attempt_count = 0

        async def mock_send_and_recv(*args, **kwargs):
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count == 1:
                raise exceptions.ServiceUnavailable("Service is down")
            else:
                yield "response_2"

        retry_manager = manager._BidiStreamRetryManager(
            strategy=mock_strategy, send_and_recv=mock_send_and_recv
        )
        retry_policy = AsyncRetry(predicate=_is_retriable, initial=0.01)

        with mock.patch("asyncio.sleep", new_callable=mock.AsyncMock):
            await retry_manager.execute(initial_state={}, retry_policy=retry_policy)

        assert attempt_count == 2
        assert mock_strategy.generate_requests.call_count == 2
        mock_strategy.recover_state_on_failure.assert_called_once()
        mock_strategy.update_state_from_response.assert_called_once_with(
            "response_2", {}
        )

    @pytest.mark.asyncio
    async def test_execute_retries_and_succeeds_mid_stream(self):
        """Test retry logic for a stream that fails after yielding some data."""
        mock_strategy = mock.AsyncMock(spec=base_strategy._BaseResumptionStrategy)
        attempt_count = 0
        # Use a list to simulate stream content for each attempt
        stream_content = [
            ["response_1", exceptions.ServiceUnavailable("Service is down")],
            ["response_2"],
        ]

        async def mock_send_and_recv(*args, **kwargs):
            nonlocal attempt_count
            content = stream_content[attempt_count]
            attempt_count += 1
            for item in content:
                if isinstance(item, Exception):
                    raise item
                else:
                    yield item

        retry_manager = manager._BidiStreamRetryManager(
            strategy=mock_strategy, send_and_recv=mock_send_and_recv
        )
        retry_policy = AsyncRetry(predicate=_is_retriable, initial=0.01)

        with mock.patch("asyncio.sleep", new_callable=mock.AsyncMock) as mock_sleep:
            await retry_manager.execute(initial_state={}, retry_policy=retry_policy)

        assert attempt_count == 2
        mock_sleep.assert_called_once()

        assert mock_strategy.generate_requests.call_count == 2
        mock_strategy.recover_state_on_failure.assert_called_once()
        assert mock_strategy.update_state_from_response.call_count == 2
        mock_strategy.update_state_from_response.assert_has_calls(
            [
                mock.call("response_1", {}),
                mock.call("response_2", {}),
            ]
        )

    @pytest.mark.asyncio
    async def test_execute_fails_immediately_on_non_retriable_error(self):
        mock_strategy = mock.AsyncMock(spec=base_strategy._BaseResumptionStrategy)

        async def mock_send_and_recv(*args, **kwargs):
            if False:
                yield
            raise exceptions.PermissionDenied("Auth error")

        retry_manager = manager._BidiStreamRetryManager(
            strategy=mock_strategy, send_and_recv=mock_send_and_recv
        )
        with pytest.raises(exceptions.PermissionDenied):
            await retry_manager.execute(
                initial_state={}, retry_policy=DEFAULT_TEST_RETRY
            )

        mock_strategy.recover_state_on_failure.assert_not_called()

    @pytest.mark.asyncio
    async def test_execute_records_retry_metrics_with_and_without_network_path_getter(
        self, monkeypatch
    ):
        from google.cloud.storage import _opentelemetry_metrics

        monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)
        monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
        mock_metrics = mock.Mock()
        mock_meter = mock.Mock()
        mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
        mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
        mock_metrics.get_meter.return_value = mock_meter
        monkeypatch.setattr(
            _opentelemetry_metrics, "metrics", mock_metrics, raising=False
        )

        recorder = _opentelemetry_metrics._MetricsRecorder(
            enable_metrics=True, rpc_system="grpc"
        )
        mock_strategy = mock.AsyncMock(spec=base_strategy._BaseResumptionStrategy)
        attempt_count = 0

        async def mock_send_and_recv(*args, **kwargs):
            nonlocal attempt_count
            attempt_count += 1
            if attempt_count == 1:
                raise exceptions.ServiceUnavailable("503")
            yield "ok"

        retry_manager = manager._BidiStreamRetryManager(
            strategy=mock_strategy,
            send_and_recv=mock_send_and_recv,
            recorder=recorder,
            network_path_getter=lambda: "directpath",
        )
        retry_policy = AsyncRetry(predicate=_is_retriable, initial=0.001)
        with _opentelemetry_metrics.start_operation(
            recorder,
            "storage.asyncio.AsyncMultiRangeDownloader.download_ranges",
            "ReadObject",
            rpc_method="google.storage.v2.Storage/BidiReadObject",
        ):
            with mock.patch("asyncio.sleep", new_callable=mock.AsyncMock):
                await retry_manager.execute(initial_state={}, retry_policy=retry_policy)

        recorder.retries_counter.add.assert_called_once()
        _, retry_kw = recorder.retries_counter.add.call_args
        assert retry_kw["attributes"]["gcp.storage.operation"] == "ReadObject"
        assert retry_kw["attributes"]["error.type"] == "UNAVAILABLE"
        assert retry_kw["attributes"]["network.path"] == "directpath"

        # Without network_path_getter on non-retryable failure
        recorder.retries_counter.add.reset_mock()

        async def fail_send_and_recv(*args, **kwargs):
            if False:
                yield
            raise exceptions.PermissionDenied("403")

        retry_manager_no_getter = manager._BidiStreamRetryManager(
            strategy=mock_strategy,
            send_and_recv=fail_send_and_recv,
            recorder=recorder,
            network_path_getter=None,
        )
        with _opentelemetry_metrics.start_operation(
            recorder,
            "storage.asyncio.AsyncMultiRangeDownloader.download_ranges",
            "ReadObject",
            rpc_method="google.storage.v2.Storage/BidiReadObject",
        ):
            with pytest.raises(exceptions.PermissionDenied):
                await retry_manager_no_getter.execute(
                    initial_state={}, retry_policy=DEFAULT_TEST_RETRY
                )
        recorder.retries_counter.add.assert_not_called()
