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
"""Unit tests for how the client decides whether to start the accelerator
daemon. The accelerator is on by default and must degrade gracefully: it
disables itself (with a warning) when the emulator is set or the daemon can't
start, unless the caller passed an explicit ``use_accelerator=True`` — then a
conflicting emulator or a daemon that fails to start is a hard error. These
exercise the pure enablement helpers on the async target without spinning up a
full client or event loop."""

import unittest.mock
from types import SimpleNamespace

import pytest

from google.cloud.bigtable.data._async.client import (
    _AcceleratorIdentityError,
    _DataApiTargetAsync,
)


class _ConcreteTarget(_DataApiTargetAsync):
    """Minimal concrete subclass so the abstract base can be instantiated."""

    @property
    def _request_path(self):
        return {}


def _bare_target(start, emulator=None, blocked_reason=None):
    """A target that skips __init__, wired with a fake client and a fake
    ``_start_accelerator`` so we can observe the enablement decision."""
    t = object.__new__(_ConcreteTarget)
    t.client = SimpleNamespace(
        _emulator_host=emulator,
        _accelerator_blocked_reason=blocked_reason,
        project="p",
    )
    t.instance_id = "i"
    t.app_profile_id = None
    t._accelerator_daemon = "SENTINEL"
    t._accelerator_client = "SENTINEL"
    t._start_accelerator = start
    return t


def _ok_start(target):
    def _start():
        target._accelerator_client = "STARTED"
        target._accelerator_daemon = "STARTED"

    return _start


class TestMaybeStartAccelerator:
    def test_emulator_auto_disables_with_warning(self):
        """Default (non-explicit) + emulator: warn and use the native client."""
        called = []
        t = _bare_target(emulator="localhost:8086", start=lambda: called.append(1))
        with pytest.warns(RuntimeWarning, match="Accelerator disabled"):
            t._maybe_start_accelerator(explicit=False)
        assert called == []

    def test_emulator_explicit_raises(self):
        """Explicit use_accelerator=True + emulator is a hard misconfiguration."""
        t = _bare_target(emulator="localhost:8086", start=lambda: None)
        with pytest.raises(RuntimeError, match="use_accelerator=True is not supported"):
            t._maybe_start_accelerator(explicit=True)

    def test_blocked_reason_disables_with_warning(self):
        """A non-reproducible in-memory secret keeps us on the native client."""
        called = []
        t = _bare_target(
            start=lambda: called.append(1),
            blocked_reason="in-memory credentials cannot be forwarded",
        )
        with pytest.warns(RuntimeWarning, match="Accelerator disabled"):
            t._maybe_start_accelerator(explicit=False)
        assert called == []

    def test_blocked_reason_explicit_raises(self):
        """Explicit use_accelerator=True + blocked auth config raises RuntimeError."""
        called = []
        t = _bare_target(
            start=lambda: called.append(1),
            blocked_reason="in-memory credentials cannot be forwarded",
        )
        with pytest.raises(
            RuntimeError,
            match="use_accelerator=True is not supported: in-memory credentials cannot be forwarded",
        ):
            t._maybe_start_accelerator(explicit=True)
        assert called == []

    def test_start_failure_falls_back_to_native(self):
        """A default (non-explicit) daemon start failure (e.g. binary missing)
        never propagates; it warns and leaves the target on the native client."""

        def _boom():
            raise FileNotFoundError("no bundled binary")

        t = _bare_target(emulator=None, start=_boom)
        with pytest.warns(RuntimeWarning, match="Failed to start"):
            t._maybe_start_accelerator(explicit=False)
        assert t._accelerator_client is None
        assert t._accelerator_daemon is None

    def test_start_failure_explicit_raises(self):
        """An explicit use_accelerator=True must not silently fall back: a daemon
        start failure propagates to the caller."""

        def _boom():
            raise FileNotFoundError("no bundled binary")

        t = _bare_target(emulator=None, start=_boom)
        with pytest.raises(FileNotFoundError, match="no bundled binary"):
            t._maybe_start_accelerator(explicit=True)

    def test_successful_start(self):
        t = _bare_target(emulator=None, start=None)
        t._start_accelerator = _ok_start(t)
        t._maybe_start_accelerator(explicit=False)
        assert t._accelerator_client == "STARTED"
        assert t._accelerator_daemon == "STARTED"

    def test_keyboard_interrupt_propagates(self):
        """Only Exception is swallowed; BaseException (Ctrl-C) must propagate."""

        def _interrupt():
            raise KeyboardInterrupt()

        t = _bare_target(emulator=None, start=_interrupt)
        with pytest.raises(KeyboardInterrupt):
            t._maybe_start_accelerator(explicit=False)

    def test_identity_error_auto_warns_and_falls_back(self, monkeypatch):
        """Identity mismatch on auto path warns and falls back — no NameError."""

        def _start():
            raise _AcceleratorIdentityError("principal mismatch")

        t = _bare_target(emulator=None, start=_start)
        with pytest.warns(RuntimeWarning, match="Accelerator disabled"):
            t._maybe_start_accelerator(explicit=False)
        assert t._accelerator_client is None
        assert t._accelerator_daemon is None

    def test_identity_error_explicit_raises(self, monkeypatch):
        """Identity mismatch on explicit path re-raises _AcceleratorIdentityError, not NameError."""

        def _start():
            raise _AcceleratorIdentityError("principal mismatch")

        t = _bare_target(emulator=None, start=_start)
        with pytest.raises(_AcceleratorIdentityError, match="principal mismatch"):
            t._maybe_start_accelerator(explicit=True)

    def test_start_accelerator_propagates_identity_error(self, monkeypatch):
        """_start_accelerator must not catch _AcceleratorIdentityError internally.

        Previously, _start_accelerator absorbed the error and returned normally,
        making _maybe_start_accelerator's explicit=True re-raise unreachable.
        """
        import google.cloud.bigtable.data._async.client as _mod

        mock_server = unittest.mock.MagicMock()
        mock_server.start.return_value = None

        t = object.__new__(_ConcreteTarget)
        t.client = SimpleNamespace(
            project="p",
            _accelerator_flags=[],
            _accelerator_env={},
        )
        t.instance_id = "i"
        t.app_profile_id = None
        t._accelerator_daemon = None
        t._accelerator_client = None
        t._verify_daemon_identity = unittest.mock.MagicMock(
            side_effect=_AcceleratorIdentityError("identity mismatch")
        )

        monkeypatch.setattr(_mod, "AcceleratorDaemon", lambda **_: mock_server)

        with pytest.raises(_AcceleratorIdentityError, match="identity mismatch"):
            t._start_accelerator()

        mock_server.close.assert_called_once()
