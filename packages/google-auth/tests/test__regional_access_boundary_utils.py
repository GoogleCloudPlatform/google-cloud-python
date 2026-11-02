# Copyright 2026 Google LLC
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

import datetime
import logging
from unittest import mock

import pytest  # type: ignore

from google.auth import (
    _credentials_async,
    _helpers,
    _regional_access_boundary_utils,
    credentials,
)
from google.oauth2 import credentials as oauth2_credentials


@pytest.fixture
def rab_caplog(caplog):
    """Fixture to configure logging capture and ensure propagation for RAB utilities."""

    caplog.set_level(
        logging.DEBUG, logger="google.auth._regional_access_boundary_utils"
    )

    google_logger = logging.getLogger("google")
    original_propagate = google_logger.propagate
    google_logger.propagate = True
    try:
        yield caplog
    finally:
        google_logger.propagate = original_propagate


class CredentialsImpl(credentials.CredentialsWithRegionalAccessBoundary):
    def __init__(self, universe_domain=None):
        super(CredentialsImpl, self).__init__()
        if universe_domain:
            self._universe_domain = universe_domain

    def _perform_refresh_token(self, request):
        self.token = "refreshed-token"
        self.expiry = (
            datetime.datetime.utcnow()
            + _helpers.REFRESH_THRESHOLD
            + datetime.timedelta(seconds=5)
        )

    def with_quota_project(self, quota_project_id):
        raise NotImplementedError()

    def _build_regional_access_boundary_lookup_url(self):
        # Using self.token here to make the URL dynamic for testing purposes
        return "http://mock.url/lookup_for_{}".format(self.token)

    def _make_copy(self):
        new_credentials = self.__class__()
        self._copy_regional_access_boundary_manager(new_credentials)
        return new_credentials


class TestCredentialsWithRegionalAccessBoundary(object):
    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    def test_maybe_start_refresh_is_skipped_if_not_expired(self, mock_start_refresh):
        creds = CredentialsImpl()
        creds._rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="0xABC",
            expiry=_helpers.utcnow() + datetime.timedelta(hours=2),
            cooldown_expiry=None,
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        creds._maybe_start_regional_access_boundary_refresh(
            mock.Mock(), "http://example.com"
        )
        mock_start_refresh.assert_not_called()

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    def test_maybe_start_refresh_triggered_if_soft_expired(self, mock_start_refresh):
        creds = CredentialsImpl()
        creds._rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="0xABC",
            expiry=_helpers.utcnow() + datetime.timedelta(minutes=30),
            cooldown_expiry=None,
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        request = mock.Mock()
        creds._maybe_start_regional_access_boundary_refresh(
            request, "http://example.com"
        )
        mock_start_refresh.assert_called_once_with(creds, request, creds._rab_manager)

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    def test_maybe_start_refresh_is_skipped_if_cooldown_active(
        self, mock_start_refresh
    ):
        creds = CredentialsImpl()
        creds._rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations=None,
            expiry=None,
            cooldown_expiry=_helpers.utcnow() + datetime.timedelta(minutes=5),
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        creds._maybe_start_regional_access_boundary_refresh(
            mock.Mock(), "http://example.com"
        )
        mock_start_refresh.assert_not_called()

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    @pytest.mark.parametrize(
        "url",
        [
            "https://my-service.us-east1.rep.googleapis.com",
            "https://my-service.us-east1.rep.sandbox.googleapis.com",
            "https://my-service.us-east1.rep.mtls.googleapis.com",
            "https://my-service.us-east1.rep.mtls.sandbox.googleapis.com",
        ],
    )
    def test_maybe_start_refresh_is_skipped_for_regional_endpoint(
        self, mock_start_refresh, url
    ):
        creds = CredentialsImpl()
        creds._maybe_start_regional_access_boundary_refresh(mock.Mock(), url)
        mock_start_refresh.assert_not_called()

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    def test_maybe_start_refresh_is_triggered(self, mock_start_refresh):
        creds = CredentialsImpl()
        request = mock.Mock()
        creds._maybe_start_regional_access_boundary_refresh(
            request, "http://example.com"
        )
        mock_start_refresh.assert_called_once_with(creds, request, creds._rab_manager)

    def test_apply_headers_success(self):
        creds = CredentialsImpl()
        creds._rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="0xABC",
            expiry=_helpers.utcnow() + datetime.timedelta(hours=1),
            cooldown_expiry=None,
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        headers = {}
        creds._rab_manager.apply_headers(headers)
        assert headers == {"x-allowed-locations": "0xABC"}

    def test_apply_headers_removes_header_if_none(self):
        creds = CredentialsImpl()
        creds._rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations=None,
            expiry=_helpers.utcnow() + datetime.timedelta(hours=1),
            cooldown_expiry=None,
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        headers = {"x-allowed-locations": "0xABC"}
        creds._rab_manager.apply_headers(headers)
        assert headers == {}

    def test_apply_headers_removes_header_if_empty(self):
        creds = CredentialsImpl()
        creds._rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="",
            expiry=_helpers.utcnow() + datetime.timedelta(hours=1),
            cooldown_expiry=None,
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        headers = {"x-allowed-locations": "0xABC"}
        creds._rab_manager.apply_headers(headers)
        assert headers == {}

    def test_set_blocking_regional_access_boundary_lookup(self):
        creds = CredentialsImpl()
        assert not creds._rab_manager._use_blocking_regional_access_boundary_lookup

        new_creds = creds._set_blocking_regional_access_boundary_lookup()
        assert new_creds is creds
        assert creds._rab_manager._use_blocking_regional_access_boundary_lookup

    def test_set_regional_access_boundary(self):
        creds = CredentialsImpl()
        seed = {
            "encodedLocations": "0xABC",
            "expiry": _helpers.utcnow() + datetime.timedelta(hours=1),
        }
        new_creds = creds._set_regional_access_boundary(seed)
        assert new_creds is creds
        assert creds._rab_manager._data.encoded_locations == "0xABC"
        assert creds._rab_manager._data.expiry == seed["expiry"]
        assert creds._rab_manager._data.cooldown_expiry is None

    def test_regional_access_boundary_getter(self):
        creds = CredentialsImpl()
        assert creds.regional_access_boundary is None

        seed = {
            "encodedLocations": "0xABC",
            "expiry": _helpers.utcnow() + datetime.timedelta(hours=1),
        }
        creds._set_regional_access_boundary(seed)
        assert creds.regional_access_boundary == "0xABC"

    def test_regional_access_boundary_expiry_getter(self):
        creds = CredentialsImpl()
        assert creds.regional_access_boundary_expiry is None

        seed = {
            "encodedLocations": "0xABC",
            "expiry": _helpers.utcnow() + datetime.timedelta(hours=1),
        }
        creds._set_regional_access_boundary(seed)
        assert creds.regional_access_boundary_expiry == seed["expiry"]

    def test_copy_regional_access_boundary_state(self):
        source_creds = CredentialsImpl()
        snapshot = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="0xABC",
            expiry=_helpers.utcnow(),
            cooldown_expiry=_helpers.utcnow(),
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )
        source_creds._rab_manager._data = snapshot

        target_creds = CredentialsImpl()
        source_creds._copy_regional_access_boundary_manager(target_creds)

        assert target_creds._rab_manager is not source_creds._rab_manager
        assert target_creds._rab_manager._data is source_creds._rab_manager._data

    def test_serialization(self):
        import pickle

        manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()
        manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="0xABC",
            expiry=_helpers.utcnow(),
            cooldown_expiry=_helpers.utcnow(),
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )

        pickled = pickle.dumps(manager)
        unpickled = pickle.loads(pickled)

        assert unpickled._data == manager._data
        assert unpickled._update_lock is not None
        assert unpickled.refresh_manager._lock is not None
        assert unpickled.refresh_manager._worker is None

    def test_unpickle_old_credentials_without_rab(self):
        creds = CredentialsImpl()
        old_state = creds.__dict__.copy()
        if "_rab_manager" in old_state:
            del old_state["_rab_manager"]
        if "_use_non_blocking_refresh" in old_state:
            del old_state["_use_non_blocking_refresh"]
        if "_refresh_worker" in old_state:
            del old_state["_refresh_worker"]

        new_instance = CredentialsImpl.__new__(CredentialsImpl)
        new_instance.__setstate__(old_state)

        assert hasattr(new_instance, "_rab_manager")
        assert new_instance._rab_manager is not None
        assert new_instance._use_non_blocking_refresh is False
        assert new_instance._refresh_worker is not None

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    def test_maybe_start_refresh_is_skipped_if_non_default_universe_domain(
        self, mock_start_refresh
    ):
        creds = CredentialsImpl(universe_domain="not.googleapis.com")
        creds._maybe_start_regional_access_boundary_refresh(
            mock.Mock(), "http://example.com"
        )
        mock_start_refresh.assert_not_called()

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager.start_refresh"
    )
    @mock.patch("urllib.parse.urlparse")
    def test_maybe_start_refresh_handles_url_parse_errors(
        self, mock_urlparse, mock_start_refresh
    ):
        mock_urlparse.side_effect = ValueError("Malformed URL")
        creds = CredentialsImpl()
        request = mock.Mock()
        creds._maybe_start_regional_access_boundary_refresh(
            request, "http://malformed-url"
        )
        mock_start_refresh.assert_called_once_with(creds, request, creds._rab_manager)

    @mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryManager.start_blocking_refresh"
    )
    def test_maybe_start_refresh_blocking(self, mock_start_blocking_refresh):
        creds = CredentialsImpl()
        creds._rab_manager._use_blocking_regional_access_boundary_lookup = True
        request = mock.Mock()
        creds._maybe_start_regional_access_boundary_refresh(
            request, "http://example.com"
        )
        mock_start_blocking_refresh.assert_called_once_with(creds, request)

    def test_start_blocking_refresh_success(self):
        creds = CredentialsImpl()
        request = mock.Mock()

        with mock.patch.object(
            creds,
            "_lookup_regional_access_boundary",
            return_value={"encodedLocations": "0xABC"},
        ) as mock_lookup:
            creds._rab_manager.start_blocking_refresh(creds, request)

            mock_lookup.assert_called_once_with(request, fail_fast=True)
            assert creds._rab_manager._data.encoded_locations == "0xABC"

    def test_start_blocking_refresh_failure(self):
        creds = CredentialsImpl()
        request = mock.Mock()

        with mock.patch.object(
            creds, "_lookup_regional_access_boundary", side_effect=Exception("error")
        ) as mock_lookup:
            creds._rab_manager.start_blocking_refresh(creds, request)

            mock_lookup.assert_called_once_with(request, fail_fast=True)
            assert creds._rab_manager._data.encoded_locations is None
            assert creds._rab_manager._data.cooldown_expiry is not None

    def test_start_blocking_refresh_with_async_credentials(self):
        creds = CredentialsImpl()
        request = mock.Mock()

        with mock.patch.object(
            creds,
            "_lookup_regional_access_boundary",
            new_callable=mock.AsyncMock,
        ) as mock_lookup:
            creds._rab_manager.start_blocking_refresh(creds, request)

            mock_lookup.assert_not_called()
            assert creds._rab_manager._data.encoded_locations is None
            assert creds._rab_manager._data.cooldown_expiry is not None

    @mock.patch("copy.deepcopy")
    def test_start_refresh_deepcopy_failure(self, mock_deepcopy):
        mock_deepcopy.side_effect = Exception("deepcopy error")
        creds = CredentialsImpl()
        request = mock.Mock()

        creds._rab_manager.refresh_manager.start_refresh(
            creds, request, creds._rab_manager
        )

        assert creds._rab_manager.refresh_manager._worker is None

    @mock.patch.object(CredentialsImpl, "_lookup_regional_access_boundary")
    def test_lookup_regional_access_boundary_success(self, mock_lookup_rab):
        creds = CredentialsImpl()
        request = mock.Mock()
        rab_manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()

        mock_lookup_rab.return_value = {
            "locations": ["us-east1"],
            "encodedLocations": "0xABC123",
        }

        worker = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread(
            creds, request, rab_manager
        )
        worker.run()

        mock_lookup_rab.assert_called_once_with(request)
        assert rab_manager._data.encoded_locations == "0xABC123"
        assert rab_manager._data.expiry is not None
        assert rab_manager._data.cooldown_expiry is None

    @mock.patch.object(CredentialsImpl, "_lookup_regional_access_boundary")
    def test_lookup_regional_access_boundary_failure(self, mock_lookup_rab, rab_caplog):
        creds = CredentialsImpl()
        request = mock.Mock()
        rab_manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()

        mock_lookup_rab.return_value = None

        worker = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread(
            creds, request, rab_manager
        )
        worker.run()

        mock_lookup_rab.assert_called_once_with(request)
        assert rab_manager._data.encoded_locations is None
        assert rab_manager._data.expiry is None
        assert rab_manager._data.cooldown_expiry is not None

        # RAB failures should be logged at DEBUG level.
        assert any(
            t[1] == logging.DEBUG
            and "Regional Access Boundary lookup failed. Entering cooldown." in t[2]
            for t in rab_caplog.record_tuples
        )

    def test_lookup_regional_access_boundary_null_url(self):
        creds = oauth2_credentials.Credentials(token="token")
        request = mock.Mock()
        result = creds._lookup_regional_access_boundary(request)
        assert result is None
        request.assert_not_called()

    def test_credentials_with_regional_access_boundary_initialization(self):
        creds = CredentialsImpl()
        assert creds._rab_manager._data.encoded_locations is None
        assert creds._rab_manager._data.expiry is None
        assert creds._rab_manager._data.cooldown_expiry is None
        assert creds._rab_manager._data.cooldown_duration == (
            credentials._regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN
        )
        assert creds._rab_manager._update_lock is not None

    @mock.patch("google.auth._helpers.utcnow")
    def test_regional_access_boundary_refresh_thread_run_success(self, mock_utcnow):
        mock_now = datetime.datetime(2025, 1, 1, 12, 0, 0)
        mock_utcnow.return_value = mock_now

        creds = mock.Mock()
        request = mock.Mock()
        rab_manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()

        creds._lookup_regional_access_boundary.return_value = {
            "locations": ["us-east1"],
            "encodedLocations": "0xABC123",
        }

        worker = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread(
            creds, request, rab_manager
        )
        worker.run()

        assert rab_manager._data.encoded_locations == "0xABC123"
        expected_expiry = (
            mock_now
            + _regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_TTL
        )
        assert rab_manager._data.expiry == expected_expiry
        assert rab_manager._data.cooldown_expiry is None

    @mock.patch("google.auth._helpers.utcnow")
    def test_regional_access_boundary_refresh_thread_run_failure(
        self, mock_utcnow, rab_caplog
    ):
        mock_now = datetime.datetime(2025, 1, 1, 12, 0, 0)
        mock_utcnow.return_value = mock_now

        creds = mock.Mock()
        request = mock.Mock()
        rab_manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()

        initial_cooldown = rab_manager._data.cooldown_duration

        creds._lookup_regional_access_boundary.side_effect = Exception(
            "Network failure"
        )

        worker = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread(
            creds, request, rab_manager
        )
        worker.run()

        assert rab_manager._data.encoded_locations is None
        assert rab_manager._data.expiry is None
        expected_cooldown_expiry = mock_now + initial_cooldown
        assert rab_manager._data.cooldown_expiry == expected_cooldown_expiry
        assert rab_manager._data.cooldown_duration == initial_cooldown * 2

        # RAB failures should be logged at DEBUG level.
        assert any(
            t[1] == logging.DEBUG
            and "Asynchronous Regional Access Boundary lookup raised an exception"
            in t[2]
            for t in rab_caplog.record_tuples
        )
        assert any(
            t[1] == logging.DEBUG
            and "Regional Access Boundary lookup failed. Entering cooldown." in t[2]
            for t in rab_caplog.record_tuples
        )

    @mock.patch("google.auth._helpers.utcnow")
    def test_regional_access_boundary_refresh_thread_run_failure_hard_expiry(
        self, mock_utcnow
    ):
        mock_now = datetime.datetime(2025, 1, 1, 12, 0, 0)
        mock_utcnow.return_value = mock_now

        creds = mock.Mock()
        request = mock.Mock()
        rab_manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()

        # Simulate existing data that has hard expired
        rab_manager._data = _regional_access_boundary_utils._RegionalAccessBoundaryData(
            encoded_locations="0xExpiredToken",
            expiry=mock_now - datetime.timedelta(hours=1),
            cooldown_expiry=None,
            cooldown_duration=_regional_access_boundary_utils.DEFAULT_REGIONAL_ACCESS_BOUNDARY_COOLDOWN,
        )

        creds._lookup_regional_access_boundary.side_effect = Exception(
            "Network failure"
        )

        worker = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread(
            creds, request, rab_manager
        )
        worker.run()

        # Assert data was aggressively cleared rather than reused due to total expiration
        assert rab_manager._data.encoded_locations is None
        assert rab_manager._data.expiry is None
        assert rab_manager._data.cooldown_expiry is not None

    def test_regional_access_boundary_refresh_manager_start_refresh_safety_lock(self):
        manager = (
            _regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager()
        )
        creds = mock.Mock()
        request = mock.Mock()
        rab_manager = mock.Mock()

        mock_worker = mock.Mock()
        mock_worker.is_alive.return_value = True
        manager._worker = mock_worker

        with mock.patch(
            "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread"
        ) as mock_thread_class:
            manager.start_refresh(creds, request, rab_manager)

            mock_thread_class.assert_not_called()
            assert manager._worker == mock_worker


class AsyncCredentialsImpl(_credentials_async.CredentialsWithRegionalAccessBoundary):
    def __init__(self, universe_domain=None):
        super().__init__()
        if universe_domain:
            self._universe_domain = universe_domain

    async def _perform_refresh_token(self, request):
        self.token = "refreshed-token"
        self.expiry = (
            _helpers.utcnow()
            + _helpers.REFRESH_THRESHOLD
            + datetime.timedelta(seconds=5)
        )

    def with_quota_project(self, quota_project_id):
        raise NotImplementedError()

    def _build_regional_access_boundary_lookup_url(self, request=None):
        # Using self.token here to make the URL dynamic for testing purposes
        return "http://mock.url/lookup_for_{}".format(self.token)

    def _make_copy(self):
        new_credentials = self.__class__()
        self._copy_regional_access_boundary_manager(new_credentials)
        return new_credentials


class TestAsyncCredentialsWithRegionalAccessBoundary(object):
    @pytest.mark.asyncio
    async def test_maybe_start_refresh_async_blocking(self):
        creds = AsyncCredentialsImpl()
        creds._rab_manager._use_blocking_regional_access_boundary_lookup = True
        request = mock.Mock()

        with mock.patch.object(
            creds._rab_manager,
            "start_blocking_refresh_async",
            new_callable=mock.AsyncMock,
        ) as mock_start_blocking:
            await creds._maybe_start_regional_access_boundary_refresh_async(
                request, "http://example.com"
            )
            mock_start_blocking.assert_called_once_with(creds, request)

    @pytest.mark.asyncio
    async def test_start_blocking_refresh_async_success(self):
        creds = AsyncCredentialsImpl()
        request = mock.Mock()

        with mock.patch.object(
            creds,
            "_lookup_regional_access_boundary",
            new_callable=mock.AsyncMock,
            return_value={"encodedLocations": "0xABC"},
        ) as mock_lookup:
            await creds._rab_manager.start_blocking_refresh_async(creds, request)

            mock_lookup.assert_called_once_with(request, fail_fast=True)
            assert creds._rab_manager._data.encoded_locations == "0xABC"

    @pytest.mark.asyncio
    async def test_start_blocking_refresh_async_failure(self):
        creds = AsyncCredentialsImpl()
        request = mock.Mock()

        with mock.patch.object(
            creds,
            "_lookup_regional_access_boundary",
            new_callable=mock.AsyncMock,
            side_effect=Exception("error"),
        ) as mock_lookup:
            await creds._rab_manager.start_blocking_refresh_async(creds, request)

            mock_lookup.assert_called_once_with(request, fail_fast=True)
            assert creds._rab_manager._data.encoded_locations is None
            assert creds._rab_manager._data.cooldown_expiry is not None

    @pytest.mark.asyncio
    async def test_async_refresh_manager_session_closed_ignored(self):
        credentials = mock.AsyncMock()
        # Simulate a closed session RuntimeError when invoking the boundary lookup
        credentials._lookup_regional_access_boundary.side_effect = RuntimeError(
            "Session is closed"
        )

        request = mock.Mock()
        request._clone.return_value = request
        rab_manager = mock.Mock()

        manager = (
            _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
        )

        # Trigger refresh, which starts a background task that should swallow the error
        manager.start_refresh(credentials, request, rab_manager)

        # Wait for the background worker task to terminate
        await manager._worker_task

        # Verify that the lookup was still triggered but failed open cleanly
        credentials._lookup_regional_access_boundary.assert_called_once_with(request)
        rab_manager.process_regional_access_boundary_info.assert_called_once_with(None)

    @pytest.mark.asyncio
    async def test_start_refresh_async_clones_request_and_unwraps_partial(self):
        import functools

        credentials = mock.AsyncMock()
        credentials._lookup_regional_access_boundary.return_value = {
            "encodedLocations": "0xA30"
        }

        mock_request = mock.Mock()
        mock_cloned_request = mock.Mock()
        mock_request._clone.return_value = mock_cloned_request
        mock_cloned_request.close = mock.AsyncMock()

        # Wrap in a functools.partial to simulate AuthorizedSession.request() timeouts
        partial_request = functools.partial(mock_request, timeout=180)

        rab_manager = mock.Mock()

        manager = (
            _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
        )
        manager.start_refresh(credentials, partial_request, rab_manager)

        await manager._worker_task

        # Verify that actual_request._clone() was called
        mock_request._clone.assert_called_once()

        # Verify that the lookup ran on a re-wrapped partial of the cloned request
        called_arg = credentials._lookup_regional_access_boundary.call_args[0][0]
        assert isinstance(called_arg, functools.partial)
        assert called_arg.func is mock_cloned_request
        assert called_arg.keywords == {"timeout": 180}

        # Verify that the cloned request was closed cleanly in the finally block
        mock_cloned_request.close.assert_awaited_once()
        rab_manager.process_regional_access_boundary_info.assert_called_once_with(
            {"encodedLocations": "0xA30"}
        )

    @pytest.mark.asyncio
    async def test_start_refresh_suppresses_request_clone_exception(self):
        from google.auth import exceptions

        credentials = mock.AsyncMock()

        request = mock.Mock()
        request._clone.side_effect = exceptions.TransportError(
            "Cannot clone a closed transport."
        )

        rab_manager = mock.Mock()
        manager = (
            _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
        )

        manager.start_refresh(credentials, request, rab_manager)

        assert manager._worker_task is None
        credentials._lookup_regional_access_boundary.assert_not_called()
        rab_manager.process_regional_access_boundary_info.assert_called_once_with(None)

    @pytest.mark.asyncio
    async def test_start_refresh_async_mimics_ephemeral_session_closed_bug(self):
        # Specifically mimics the real-world race condition where a fast foreground main call
        # pulls the rug out from under the background worker when using an un-cloned session.
        import asyncio

        manager = (
            _regional_access_boundary_utils._AsyncRegionalAccessBoundaryRefreshManager()
        )

        worker_started_event = asyncio.Event()
        foreground_closed_event = asyncio.Event()

        class EphemeralRequest:
            def __init__(self):
                self.closed = False

            async def __call__(self, *args, **kwargs):
                worker_started_event.set()
                await foreground_closed_event.wait()
                if self.closed:
                    raise RuntimeError("Session is closed")
                return "success"

        ephemeral_req = EphemeralRequest()

        credentials = mock.AsyncMock()

        async def mock_lookup(req):
            return await req()

        credentials._lookup_regional_access_boundary.side_effect = mock_lookup

        rab_manager = mock.Mock()

        # Start the background refresh worker
        manager.start_refresh(credentials, ephemeral_req, rab_manager)

        # Wait until the background worker has actually started its speculative request
        await worker_started_event.wait()

        # Simulate fast foreground primary call closing the session
        ephemeral_req.closed = True
        foreground_closed_event.set()

        # Await the background worker task to settle
        await manager._worker_task

        # Verify that the background worker hit the "Session is closed" error and failed open cleanly
        rab_manager.process_regional_access_boundary_info.assert_called_once_with(None)


def test_get_service_account_rab_endpoint(monkeypatch):
    from google.auth.transport import _mtls_helper

    # Test Standard TLS
    monkeypatch.setattr(_mtls_helper, "check_use_client_cert", lambda: False)
    url = _regional_access_boundary_utils.get_service_account_rab_endpoint(
        "test@example.com"
    )
    assert (
        url
        == "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/test@example.com/allowedLocations"
    )

    # Test mTLS
    monkeypatch.setattr(_mtls_helper, "check_use_client_cert", lambda: True)
    url = _regional_access_boundary_utils.get_service_account_rab_endpoint(
        "test@example.com"
    )
    assert (
        url
        == "https://iamcredentials.mtls.googleapis.com/v1/projects/-/serviceAccounts/test@example.com/allowedLocations"
    )


def test_get_workforce_pool_rab_endpoint(monkeypatch):
    from google.auth.transport import _mtls_helper

    # Test Standard TLS
    monkeypatch.setattr(_mtls_helper, "check_use_client_cert", lambda: False)
    url = _regional_access_boundary_utils.get_workforce_pool_rab_endpoint("POOL_ID")
    assert (
        url
        == "https://iamcredentials.googleapis.com/v1/locations/global/workforcePools/POOL_ID/allowedLocations"
    )

    # Test mTLS
    monkeypatch.setattr(_mtls_helper, "check_use_client_cert", lambda: True)
    url = _regional_access_boundary_utils.get_workforce_pool_rab_endpoint("POOL_ID")
    assert (
        url
        == "https://iamcredentials.mtls.googleapis.com/v1/locations/global/workforcePools/POOL_ID/allowedLocations"
    )


def test_get_workload_identity_pool_rab_endpoint(monkeypatch):
    from google.auth.transport import _mtls_helper

    # Test Standard TLS
    monkeypatch.setattr(_mtls_helper, "check_use_client_cert", lambda: False)
    url = _regional_access_boundary_utils.get_workload_identity_pool_rab_endpoint(
        "PROJECT_NUM", "POOL_ID"
    )
    assert (
        url
        == "https://iamcredentials.googleapis.com/v1/projects/PROJECT_NUM/locations/global/workloadIdentityPools/POOL_ID/allowedLocations"
    )

    # Test mTLS
    monkeypatch.setattr(_mtls_helper, "check_use_client_cert", lambda: True)
    url = _regional_access_boundary_utils.get_workload_identity_pool_rab_endpoint(
        "PROJECT_NUM", "POOL_ID"
    )
    assert (
        url
        == "https://iamcredentials.mtls.googleapis.com/v1/projects/PROJECT_NUM/locations/global/workloadIdentityPools/POOL_ID/allowedLocations"
    )


def test_sync_refresh_manager_pickle():
    import pickle

    manager = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager()
    manager._worker = mock.Mock()

    dumped = pickle.dumps(manager)
    loaded = pickle.loads(dumped)

    assert loaded._lock is not None
    assert loaded._worker is None


def test_manager_eq_different_type():
    manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()
    assert manager != "not a manager"


def test_set_initial_regional_access_boundary_empty():
    manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()
    manager.set_initial_regional_access_boundary(
        encoded_locations="", expiry=datetime.datetime.now()
    )
    assert manager._data.encoded_locations == ""
    assert manager._data.expiry is None


def test_set_initial_regional_access_boundary_with_value():
    manager = _regional_access_boundary_utils._RegionalAccessBoundaryManager()
    expiry = datetime.datetime.now()
    manager.set_initial_regional_access_boundary(
        encoded_locations="us-east1", expiry=expiry
    )
    assert manager._data.encoded_locations == "us-east1"
    assert manager._data.expiry == expiry


def test_sync_refresh_manager_start_refresh_executes():
    manager = _regional_access_boundary_utils._RegionalAccessBoundaryRefreshManager()
    creds = mock.Mock()
    request = mock.Mock()
    rab_manager = mock.Mock()

    with mock.patch(
        "google.auth._regional_access_boundary_utils._RegionalAccessBoundaryRefreshThread"
    ) as mock_thread_class:
        mock_thread = mock.Mock()
        mock_thread_class.return_value = mock_thread

        manager.start_refresh(creds, request, rab_manager)

        mock_thread_class.assert_called_once()
        mock_thread.start.assert_called_once()
