# Copyright 2026 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
from unittest import mock

import pytest  # type: ignore

from google.auth import _regional_access_boundary_utils


@pytest.mark.asyncio
async def test_async_refresh_manager_start_refresh():
    credentials = mock.AsyncMock()
    credentials._lookup_regional_access_boundary.return_value = {
        "encodedLocations": "0xA30"
    }

    request = mock.Mock()
    request._clone.return_value = request
    rab_manager = mock.Mock()

    manager = (
        _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
    )

    manager.start_refresh(credentials, request, rab_manager)

    # Wait for the background task to finish
    await manager._worker_task

    credentials._lookup_regional_access_boundary.assert_called_once_with(request)
    rab_manager.process_regional_access_boundary_info.assert_called_once_with(
        {"encodedLocations": "0xA30"}
    )


@pytest.mark.asyncio
async def test_async_refresh_manager_duplicate_refresh_prevented():
    credentials = mock.AsyncMock()

    # Use events to control the concurrency timing
    lookup_started = asyncio.Event()
    lookup_finish = asyncio.Event()

    async def controlled_lookup(*args, **kwargs):
        lookup_started.set()  # Signal that the background lookup has started.
        await (
            lookup_finish.wait()
        )  # Block until the test allows the lookup to complete.
        return {"encodedLocations": "0xA30"}

    credentials._lookup_regional_access_boundary.side_effect = controlled_lookup

    request = mock.Mock()
    rab_manager = mock.Mock()

    manager = (
        _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
    )

    # Start the initial refresh task in the background.
    manager.start_refresh(credentials, request, rab_manager)

    # Wait until the background task has begun executing the lookup.
    await lookup_started.wait()

    # Attempt a second refresh while the initial task is still in progress.
    manager.start_refresh(credentials, request, rab_manager)

    # Unblock the initial task and wait for it to complete.
    lookup_finish.set()
    await manager._worker_task

    # Verify that the second refresh request was ignored and only one lookup occurred.
    assert credentials._lookup_regional_access_boundary.call_count == 1


def test_prepare_async_lookup_callable_no_clone():
    request = mock.Mock(spec=[])  # explicitly no _clone
    (
        new_request,
        cloned,
        is_cloned,
    ) = _regional_access_boundary_utils._prepare_async_lookup_callable(request)
    assert new_request is request
    assert cloned is request
    assert is_cloned is False


def test_prepare_async_lookup_callable_with_clone():
    request = mock.Mock()
    cloned_req = mock.Mock()
    request._clone.return_value = cloned_req

    (
        new_request,
        cloned,
        is_cloned,
    ) = _regional_access_boundary_utils._prepare_async_lookup_callable(request)
    assert new_request is cloned_req
    assert cloned is cloned_req
    assert is_cloned is True


def test_prepare_async_lookup_callable_partial():
    import functools

    request = mock.Mock()
    cloned_req = mock.Mock()
    request._clone.return_value = cloned_req

    partial_req = functools.partial(request, 1, a=2)
    (
        new_request,
        cloned,
        is_cloned,
    ) = _regional_access_boundary_utils._prepare_async_lookup_callable(partial_req)

    assert isinstance(new_request, functools.partial)
    assert new_request.func is cloned_req
    assert new_request.args == (1,)
    assert new_request.keywords == {"a": 2}
    assert cloned is cloned_req
    assert is_cloned is True


@pytest.mark.asyncio
async def test_close_cloned_request_not_cloned():
    request = mock.Mock()
    await _regional_access_boundary_utils._close_cloned_request(
        request, is_cloned=False
    )
    request.close.assert_not_called()


@pytest.mark.asyncio
async def test_close_cloned_request_sync():
    request = mock.Mock()
    await _regional_access_boundary_utils._close_cloned_request(request, is_cloned=True)
    request.close.assert_called_once()


@pytest.mark.asyncio
async def test_close_cloned_request_async():
    request = mock.Mock()
    request.close = mock.AsyncMock()
    await _regional_access_boundary_utils._close_cloned_request(request, is_cloned=True)
    request.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_cloned_request_future():
    request = mock.Mock()
    future = asyncio.Future()
    future.set_result(None)
    request.close = mock.Mock(return_value=future)

    await _regional_access_boundary_utils._close_cloned_request(request, is_cloned=True)
    request.close.assert_called_once()
    assert future.done()


@pytest.mark.asyncio
async def test_close_cloned_request_async_exception():
    request = mock.Mock()
    request.close = mock.AsyncMock(side_effect=Exception("close error"))
    # Should swallow the exception and not raise
    await _regional_access_boundary_utils._close_cloned_request(request, is_cloned=True)
    request.close.assert_awaited_once()


def test_async_refresh_manager_pickle():
    import pickle

    manager = (
        _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
    )
    manager._worker_task = mock.Mock()

    dumped = pickle.dumps(manager)
    loaded = pickle.loads(dumped)

    assert loaded._lock is not None
    assert loaded._worker_task is None


@pytest.mark.asyncio
async def test_async_worker_exception_logging():
    credentials = mock.AsyncMock()
    credentials._lookup_regional_access_boundary.side_effect = Exception("lookup fail")

    request = mock.Mock()
    request._clone.return_value = request
    rab_manager = mock.Mock()

    manager = (
        _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
    )

    with mock.patch.object(
        _regional_access_boundary_utils._LOGGER, "debug"
    ) as mock_debug:
        manager.start_refresh(credentials, request, rab_manager)
        await manager._worker_task

        mock_debug.assert_called_once()
        assert "lookup raised an exception" in mock_debug.call_args[0][0]
        rab_manager.process_regional_access_boundary_info.assert_called_once_with(None)


@pytest.mark.asyncio
async def test_async_refresh_manager_clone_failure():
    credentials = mock.AsyncMock()
    rab_manager = mock.Mock()

    # Configure mock request to raise an exception on clone
    request = mock.Mock()
    request._clone.side_effect = Exception("mock clone error")

    manager = (
        _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
    )

    manager.start_refresh(credentials, request, rab_manager)

    # Verify no worker task was created and cooldown was triggered immediately
    assert manager._worker_task is None
    rab_manager.process_regional_access_boundary_info.assert_called_once_with(None)


@pytest.mark.asyncio
async def test_async_refresh_manager_task_creation_failure(monkeypatch):
    credentials = mock.AsyncMock()
    rab_manager = mock.Mock()

    # Configure a mock request that successfully clones
    request = mock.Mock()
    cloned_req = mock.Mock()
    cloned_req.close = mock.AsyncMock()
    request._clone.return_value = cloned_req

    # Force task creation to fail
    monkeypatch.setattr(
        asyncio,
        "create_task",
        mock.Mock(side_effect=RuntimeError("loop closed")),
    )

    manager = (
        _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
    )

    with pytest.raises(RuntimeError, match="loop closed"):
        manager.start_refresh(credentials, request, rab_manager)

    # Yield control to the event loop so the scheduled close task can run
    await asyncio.sleep(0)

    # Verify the cloned session was closed immediately to prevent socket leaks
    cloned_req.close.assert_awaited_once()
    rab_manager.process_regional_access_boundary_info.assert_called_once_with(None)
