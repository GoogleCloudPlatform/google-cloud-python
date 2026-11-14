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

import logging
from typing import Any, AsyncIterator, Callable, Optional

from google.cloud.storage import _opentelemetry_metrics
from google.cloud.storage.asyncio.retry.base_strategy import (
    _BaseResumptionStrategy,
)

logger = logging.getLogger(__name__)


class _BidiStreamRetryManager:
    """Manages the generic retry loop for a bidi streaming operation."""

    def __init__(
        self,
        strategy: _BaseResumptionStrategy,
        send_and_recv: Callable[..., AsyncIterator[Any]],
        recorder: Optional[Any] = None,
        network_path_getter: Optional[Callable[[], Optional[str]]] = None,
    ):
        """Initializes the retry manager.
        Args:
            strategy: The strategy for managing the state of a specific
                bidi operation (e.g., reads or writes).
            send_and_recv: An async callable that opens a new gRPC stream.
            recorder: Optional `_MetricsRecorder` for retry metric accounting.
            network_path_getter: Optional callable returning the current ``network.path``.
        """
        self._strategy = strategy
        self._send_and_recv = send_and_recv
        self._recorder = recorder
        self._network_path_getter = network_path_getter

    async def execute(self, initial_state: Any, retry_policy):
        """
        Executes the bidi operation with the configured retry policy.
        Args:
            initial_state: An object containing all state for the operation.
            retry_policy: The `google.api_core.retry.AsyncRetry` object to
                govern the retry behavior for this specific operation.
        """
        state = initial_state

        async def attempt():
            current_op = _opentelemetry_metrics.get_current_operation()
            attempts_before = current_op.recorded_attempts if current_op else 0
            requests = self._strategy.generate_requests(state)
            stream = self._send_and_recv(requests, state)
            try:
                async for response in stream:
                    self._strategy.update_state_from_response(response, state)
                if self._recorder is not None:
                    _opentelemetry_metrics.record_pending_retry(
                        self._recorder,
                        network_path=(
                            self._network_path_getter()
                            if self._network_path_getter is not None
                            else None
                        ),
                    )
                return
            except Exception as e:
                will_retry = bool(retry_policy._predicate(e))
                if self._recorder is not None:
                    _opentelemetry_metrics.handle_unrecorded_retryable_failure(
                        self._recorder,
                        e,
                        attempts_before=attempts_before,
                        will_retry=will_retry,
                        network_path=(
                            self._network_path_getter()
                            if self._network_path_getter is not None
                            else None
                        ),
                    )
                if will_retry:
                    logger.warning(
                        f"Bidi stream operation failed: {e}. Attempting state recovery and retry."
                    )
                    await self._strategy.recover_state_on_failure(e, state)
                raise e

        wrapped_attempt = retry_policy(attempt)

        await wrapped_attempt()
