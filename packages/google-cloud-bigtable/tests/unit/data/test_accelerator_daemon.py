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

import json
import os
import re
import unittest.mock

import pytest

from google.cloud.bigtable.data._accelerator import _daemon
from google.cloud.bigtable.data._accelerator._daemon import (
    _DEFAULT_STARTUP_TIMEOUT,
    _IDENTITY_FILENAME,
    _STARTUP_TIMEOUT_ENV_VAR,
    AcceleratorDaemon,
    _resolve_startup_timeout,  # noqa: F401 (used indirectly by AcceleratorDaemon)
)


def _make_daemon(tmp_path, **kwargs):
    # Use binary_path= so the constructor doesn't require the bundled binary;
    # tests that call start() monkeypatch Popen separately.
    fake_binary = tmp_path / "fake-binary"
    fake_binary.touch()
    kwargs.setdefault("binary_path", str(fake_binary))
    return AcceleratorDaemon(**kwargs)


# Captured at import time, before the autouse fixture patches _cleanup_tempdir
# to a no-op.  Tests that need to exercise the real implementation call this
# directly as _real_cleanup_tempdir(daemon_instance).
_real_cleanup_tempdir = AcceleratorDaemon._cleanup_tempdir


class TestExtraEnv:
    def test_default_env_none(self, tmp_path, monkeypatch):
        captured = {}

        def fake_popen(argv, **kwargs):
            captured.update(kwargs)
            raise _StopStart()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        daemon = _make_daemon(tmp_path)
        with pytest.raises(_StopStart):
            daemon.start()
        # No extra_env -> inherit parent environment (env=None).
        assert captured["env"] is None

    def test_extra_env_merged_over_parent(self, tmp_path, monkeypatch):
        captured = {}

        def fake_popen(argv, **kwargs):
            captured.update(kwargs)
            raise _StopStart()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        monkeypatch.setenv("EXISTING", "keep")
        daemon = _make_daemon(
            tmp_path,
            extra_env={"GOOGLE_APPLICATION_CREDENTIALS": "/path/to/key.json"},
        )
        with pytest.raises(_StopStart):
            daemon.start()
        env = captured["env"]
        assert env["GOOGLE_APPLICATION_CREDENTIALS"] == "/path/to/key.json"
        # Parent env is preserved (merged, not replaced).
        assert env["EXISTING"] == "keep"

    @pytest.mark.parametrize("is_windows", [False, True])
    def test_spawns_in_isolated_process_group(self, tmp_path, monkeypatch, is_windows):
        captured = {}

        def fake_popen(argv, **kwargs):
            captured.update(kwargs)
            raise _StopStart()

        monkeypatch.setattr(_daemon, "_IS_WINDOWS", is_windows)
        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        if is_windows:
            monkeypatch.setattr(
                _daemon.subprocess,
                "CREATE_NEW_PROCESS_GROUP",
                0x00000200,
                raising=False,
            )
            monkeypatch.setattr(_daemon.socket, "AF_UNIX", 1, raising=False)
        daemon = _make_daemon(tmp_path)
        with pytest.raises(_StopStart):
            daemon.start()
        if is_windows:
            assert captured.get("creationflags") == 0x00000200
            assert "start_new_session" not in captured
        else:
            assert captured.get("start_new_session") is True
            assert "creationflags" not in captured


class TestReadIdentity:
    def test_reads_and_unlinks(self, tmp_path):
        daemon = _make_daemon(tmp_path)
        d = tmp_path / "accel-tmp"
        d.mkdir()
        daemon._tempdir = str(d)
        identity_path = d / _IDENTITY_FILENAME
        identity_path.write_text(
            json.dumps({"principal": "svc@proj.iam.gserviceaccount.com"})
        )
        result = daemon.read_identity()
        assert result["principal"] == "svc@proj.iam.gserviceaccount.com"
        # The identity is verified once, then consumed.
        assert not identity_path.exists()

    def test_not_started_raises(self, tmp_path):
        daemon = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="has not been started"):
            daemon.read_identity()

    def test_missing_file_raises(self, tmp_path):
        daemon = _make_daemon(tmp_path)
        d = tmp_path / "accel-tmp"
        d.mkdir()
        daemon._tempdir = str(d)
        with pytest.raises(RuntimeError, match="did not write"):
            daemon.read_identity()


class TestAuthSecret:
    def test_raises_before_start(self, tmp_path):
        daemon = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="has not been started"):
            _ = daemon.auth_secret

    def test_secret_written_to_stdin(self, tmp_path, monkeypatch):
        """The secret is urlsafe and ends with a newline on the wire."""
        written = bytearray()

        class FakeStdin:
            def write(self, data):
                written.extend(data)

            def flush(self):
                pass

        class FakeProc:
            pid = 12345
            stdin = FakeStdin()

            def poll(self):
                return None

        def fake_popen(argv, **kwargs):
            return FakeProc()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        daemon = _make_daemon(tmp_path)
        # _wait_until_ready will fail immediately (process is fake); we just
        # need to get past the stdin-write step, so patch _wait_until_ready.
        monkeypatch.setattr(daemon, "_wait_until_ready", lambda timeout: None)
        daemon.start()
        payload = written.decode()
        assert payload.endswith("\n"), "secret payload must end with newline"
        token = payload.rstrip("\n")
        assert token == daemon.auth_secret
        # token_urlsafe(32) produces ≥32 chars of base64url characters.
        assert len(token) >= 32
        assert re.fullmatch(r"[A-Za-z0-9_\-]+", token), "expected urlsafe token"

    def test_broken_pipe_kills_and_reraises(self, tmp_path, monkeypatch):
        """A broken pipe during secret write force-kills the daemon and raises."""

        class FakeStdin:
            def write(self, data):
                raise OSError("broken pipe")

            def flush(self):
                pass

        class FakeProc:
            pid = 12345
            stdin = FakeStdin()

            def poll(self):
                return None

        def fake_popen(argv, **kwargs):
            return FakeProc()

        killed = []
        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        monkeypatch.setattr(
            AcceleratorDaemon, "_force_kill", lambda self: killed.append(True)
        )
        daemon = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="auth secret"):
            daemon.start()
        assert killed, "_force_kill should have been called on broken pipe"


class _StopStart(Exception):
    """Sentinel to abort AcceleratorDaemon.start() right after Popen so the test
    never waits on a real socket."""


@pytest.fixture(autouse=True)
def _no_cleanup_crash(monkeypatch, tmp_path):
    # start() force-kills and cleans up on the _StopStart exception; make those
    # no-ops so the fake (never-really-spawned) process doesn't blow up.
    monkeypatch.setattr(AcceleratorDaemon, "_force_kill", lambda self: None)
    monkeypatch.setattr(AcceleratorDaemon, "_cleanup_tempdir", lambda self: None)

    # Keep the daemon's tempdir inside pytest's tmp so nothing leaks to /tmp.
    def fake_mkdtemp(prefix=""):
        d = tmp_path / "accel-tmp"
        os.makedirs(d, exist_ok=True)
        return str(d)

    monkeypatch.setattr(_daemon.tempfile, "mkdtemp", fake_mkdtemp)

    yield


@pytest.fixture
def no_af_unix(monkeypatch):
    """Make the socket module look the way CPython's does on Windows.

    The family is simply absent there — the OS and gRPC's C-core support
    AF_UNIX, the socket module just never exposed it — so every branch keyed on
    ``hasattr(socket, "AF_UNIX")`` is reachable from a POSIX test run.
    """
    monkeypatch.delattr(_daemon.socket, "AF_UNIX", raising=False)


# ---------------------------------------------------------------------------
# Properties before/after start
# ---------------------------------------------------------------------------


class TestPropertiesBeforeStart:
    def test_uds_path_before_start_raises(self, tmp_path):
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="has not been started"):
            _ = d.uds_path

    def test_log_path_before_start_raises(self, tmp_path):
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="has not been started"):
            _ = d.log_path

    def test_pid_before_start_raises(self, tmp_path):
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="has not been started"):
            _ = d.pid

    def test_is_running_before_start_is_false(self, tmp_path):
        d = _make_daemon(tmp_path)
        assert d.is_running is False

    def test_is_running_with_live_proc(self, tmp_path):
        d = _make_daemon(tmp_path)
        proc_mock = unittest.mock.Mock()
        proc_mock.poll.return_value = None  # still running
        d._proc = proc_mock
        assert d.is_running is True

    def test_is_running_with_dead_proc(self, tmp_path):
        d = _make_daemon(tmp_path)
        proc_mock = unittest.mock.Mock()
        proc_mock.poll.return_value = 0  # exited
        d._proc = proc_mock
        assert d.is_running is False


# ---------------------------------------------------------------------------
# Binary resolution
# ---------------------------------------------------------------------------


class TestResolveBinaryPath:
    def test_missing_binary_raises_file_not_found(self, tmp_path):
        from google.cloud.bigtable.data._accelerator._daemon import _resolve_binary_path

        with unittest.mock.patch("os.path.isfile", return_value=False):
            with pytest.raises(FileNotFoundError, match="Accelerator binary not found"):
                _resolve_binary_path()

    @pytest.mark.parametrize(
        "is_windows,expected",
        [(False, "bin/accelerator"), (True, "bin/accelerator.exe")],
    )
    def test_binary_name_follows_platform(self, monkeypatch, is_windows, expected):
        """Windows wheels stage the binary under the .exe name Go gives it."""
        monkeypatch.setattr(_daemon, "_IS_WINDOWS", is_windows)
        with unittest.mock.patch("os.path.isfile", return_value=True):
            resolved = _daemon._resolve_binary_path()
        assert resolved.endswith(expected)


# ---------------------------------------------------------------------------
# start() failure modes
# ---------------------------------------------------------------------------


class TestStartFailures:
    def test_called_twice_raises(self, tmp_path, monkeypatch):
        def fake_popen(argv, **kwargs):
            raise _StopStart()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        d = _make_daemon(tmp_path)
        # Manually set _proc so it looks like it was already started.
        d._proc = unittest.mock.Mock()
        with pytest.raises(RuntimeError, match="called twice"):
            d.start()

    def test_popen_oserror_raises_runtime_error(self, tmp_path, monkeypatch):
        def bad_popen(argv, **kwargs):
            raise OSError("permission denied")

        monkeypatch.setattr(_daemon.subprocess, "Popen", bad_popen)
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="Failed to spawn"):
            d.start()

    def test_process_exits_during_startup_raises(self, tmp_path, monkeypatch):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = 1  # exited immediately
        proc_mock.stdin = unittest.mock.Mock()

        monkeypatch.setattr(_daemon.subprocess, "Popen", lambda *a, **kw: proc_mock)
        # _cleanup_tempdir is already a no-op via autouse fixture, but
        # _force_kill is too — that's fine, we just need the start to raise.
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "0.1")
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="exited during startup"):
            d.start()

    def test_uds_never_appears_raises_timeout(self, tmp_path, monkeypatch):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = None  # alive but UDS never arrives
        proc_mock.stdin = unittest.mock.Mock()

        monkeypatch.setattr(_daemon.subprocess, "Popen", lambda *a, **kw: proc_mock)
        # Nothing ever binds the socket, so the readiness channel stays in
        # TRANSIENT_FAILURE and the deadline is what ends the wait.
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "0.05")
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="did not become ready"):
            d.start()

    def test_no_af_unix_raises_os_error(self, tmp_path, monkeypatch, no_af_unix):
        d = _make_daemon(tmp_path)
        with pytest.raises(OSError, match="AF_UNIX"):
            d.start()


# ---------------------------------------------------------------------------
# close() lifecycle
# ---------------------------------------------------------------------------


class TestClose:
    def test_close_before_start_is_noop(self, tmp_path):
        d = _make_daemon(tmp_path)
        d.close()  # should not raise

    def test_close_graceful_via_stdin_eof(self, tmp_path):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = None
        proc_mock.stdin = unittest.mock.Mock()
        # First wait call returns True (exited after stdin close).
        d = _make_daemon(tmp_path)
        d._proc = proc_mock

        with (
            unittest.mock.patch.object(d, "_wait_for_exit", return_value=True),
            unittest.mock.patch.object(d, "_cleanup_tempdir"),
        ):
            d.close()

        proc_mock.stdin.close.assert_called_once()
        proc_mock.terminate.assert_not_called()
        proc_mock.kill.assert_not_called()

    def test_close_escalates_to_sigterm(self, tmp_path):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = None
        proc_mock.stdin = unittest.mock.Mock()
        d = _make_daemon(tmp_path)
        d._proc = proc_mock

        wait_results = iter([False, True])  # stdin wait fails, sigterm wait succeeds

        with (
            unittest.mock.patch.object(d, "_wait_for_exit", side_effect=wait_results),
            unittest.mock.patch.object(d, "_cleanup_tempdir"),
        ):
            d.close()

        proc_mock.terminate.assert_called_once()
        proc_mock.kill.assert_not_called()

    def test_close_escalates_to_sigkill(self, tmp_path):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = None
        proc_mock.stdin = unittest.mock.Mock()
        d = _make_daemon(tmp_path)
        d._proc = proc_mock

        # Both stdin and sigterm waits fail → sigkill.
        wait_results = iter([False, False, True])

        with (
            unittest.mock.patch.object(d, "_wait_for_exit", side_effect=wait_results),
            unittest.mock.patch.object(d, "_cleanup_tempdir"),
        ):
            d.close()

        proc_mock.terminate.assert_called_once()
        proc_mock.kill.assert_called_once()

    def test_close_clears_proc_reference(self, tmp_path):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = None
        proc_mock.stdin = unittest.mock.Mock()
        d = _make_daemon(tmp_path)
        d._proc = proc_mock

        with (
            unittest.mock.patch.object(d, "_wait_for_exit", return_value=True),
            unittest.mock.patch.object(d, "_cleanup_tempdir"),
        ):
            d.close()

        assert d._proc is None


# ---------------------------------------------------------------------------
# _cleanup_tempdir: state clearing
# ---------------------------------------------------------------------------


class TestCleanupTempdir:
    def test_clears_all_state_fields(self, tmp_path):
        d = _make_daemon(tmp_path)
        d._tempdir = str(tmp_path / "accel-tmp")
        d._uds_path = str(tmp_path / "sock")
        d._log_path = str(tmp_path / "daemon.log")
        d._auth_secret = "super-secret"

        _real_cleanup_tempdir(d)

        assert d._tempdir is None
        assert d._uds_path is None
        assert d._log_path is None
        assert d._auth_secret is None

    def test_removes_tempdir_from_disk(self, tmp_path):
        d = _make_daemon(tmp_path)
        td = tmp_path / "accel-tmp"
        td.mkdir()
        d._tempdir = str(td)

        _real_cleanup_tempdir(d)

        assert not td.exists()

    def test_noop_when_tempdir_is_none(self, tmp_path):
        d = _make_daemon(tmp_path)
        _real_cleanup_tempdir(d)  # should not raise


# ---------------------------------------------------------------------------
# Context manager
# ---------------------------------------------------------------------------


class TestContextManager:
    def test_enter_calls_start_and_returns_self(self, tmp_path, monkeypatch):
        def fake_popen(argv, **kwargs):
            raise _StopStart()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        d = _make_daemon(tmp_path)
        with (
            unittest.mock.patch.object(d, "start") as start_mock,
            unittest.mock.patch.object(d, "close"),
        ):
            result = d.__enter__()
        start_mock.assert_called_once()
        assert result is d

    def test_exit_calls_close(self, tmp_path):
        d = _make_daemon(tmp_path)
        with unittest.mock.patch.object(d, "close") as close_mock:
            d.__exit__(None, None, None)
        close_mock.assert_called_once()


# ---------------------------------------------------------------------------
# _read_log_tail
# ---------------------------------------------------------------------------


class TestReadLogTail:
    def test_reads_tail_of_log(self, tmp_path):
        d = _make_daemon(tmp_path)
        log = tmp_path / "daemon.log"
        log.write_bytes(b"hello world")
        d._log_path = str(log)
        tail = d._read_log_tail()
        assert "hello world" in tail

    def test_truncates_to_max_bytes(self, tmp_path):
        d = _make_daemon(tmp_path)
        log = tmp_path / "daemon.log"
        log.write_bytes(b"x" * 8192)
        d._log_path = str(log)
        tail = d._read_log_tail(max_bytes=100)
        assert len(tail) <= 100

    def test_missing_log_returns_empty(self, tmp_path):
        d = _make_daemon(tmp_path)
        d._log_path = str(tmp_path / "nonexistent.log")
        assert d._read_log_tail() == ""

    def test_no_log_path_returns_empty(self, tmp_path):
        d = _make_daemon(tmp_path)
        d._log_path = None
        assert d._read_log_tail() == ""


# ---------------------------------------------------------------------------
# _wait_for_exit
# ---------------------------------------------------------------------------


class TestWaitForExit:
    def test_returns_true_when_no_proc(self, tmp_path):
        d = _make_daemon(tmp_path)
        assert d._wait_for_exit(1.0) is True

    def test_returns_true_when_proc_exits_in_time(self, tmp_path):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.wait.return_value = 0  # exited
        d = _make_daemon(tmp_path)
        d._proc = proc_mock
        assert d._wait_for_exit(1.0) is True

    def test_returns_false_on_timeout(self, tmp_path):
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.wait.side_effect = subprocess.TimeoutExpired(cmd="x", timeout=0.1)
        d = _make_daemon(tmp_path)
        d._proc = proc_mock
        assert d._wait_for_exit(0.1) is False


# ---------------------------------------------------------------------------
# read_identity: corrupt JSON
# ---------------------------------------------------------------------------


class TestReadIdentityCorruptJson:
    def test_corrupt_json_raises_runtime_error(self, tmp_path):
        d = _make_daemon(tmp_path)
        dd = tmp_path / "accel-tmp"
        dd.mkdir(exist_ok=True)
        d._tempdir = str(dd)
        identity_path = dd / _IDENTITY_FILENAME
        identity_path.write_text("{not valid json}")
        with pytest.raises(RuntimeError, match="Failed to read"):
            d.read_identity()

    def test_read_identity_unlinks_even_on_error(self, tmp_path):
        d = _make_daemon(tmp_path)
        dd = tmp_path / "accel-tmp2"
        dd.mkdir(exist_ok=True)
        d._tempdir = str(dd)
        identity_path = dd / _IDENTITY_FILENAME
        identity_path.write_text("{bad json}")
        try:
            d.read_identity()
        except RuntimeError:
            pass
        # File should be unlinked regardless of the parse error.
        assert not identity_path.exists()


# ---------------------------------------------------------------------------
# CLI flags passed to Popen
# ---------------------------------------------------------------------------


class TestCliFlags:
    def test_cli_flags_appended_to_argv(self, tmp_path, monkeypatch):
        captured = {}

        def fake_popen(argv, **kwargs):
            captured["argv"] = argv
            raise _StopStart()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        d = _make_daemon(
            tmp_path,
            cli_flags=[
                "--project",
                "proj",
                "--instance",
                "inst",
                "--app-profile",
                "prof",
            ],
        )
        with pytest.raises(_StopStart):
            d.start()

        argv = captured["argv"]
        assert "--uds-path" in argv
        assert "--project" in argv
        assert argv[argv.index("--project") + 1] == "proj"
        assert "--instance" in argv
        assert argv[argv.index("--instance") + 1] == "inst"
        assert "--app-profile" in argv
        assert argv[argv.index("--app-profile") + 1] == "prof"


# ---------------------------------------------------------------------------
# Startup timeout env variable (_resolve_startup_timeout)
# ---------------------------------------------------------------------------


class TestResolveStartupTimeout:
    """Tests for the BIGTABLE_ACCELERATOR_STARTUP_TIMEOUT env-var override.

    The remote implementation raises ValueError for invalid values rather than
    warning and falling back — invalid env vars are deployment misconfigurations
    and should surface loudly.
    """

    def test_no_env_var_returns_default(self, monkeypatch):
        monkeypatch.delenv(_STARTUP_TIMEOUT_ENV_VAR, raising=False)
        assert _resolve_startup_timeout() == _DEFAULT_STARTUP_TIMEOUT

    def test_empty_string_returns_default(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "")
        assert _resolve_startup_timeout() == _DEFAULT_STARTUP_TIMEOUT

    def test_valid_integer_string_overrides(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "30")
        assert _resolve_startup_timeout() == 30.0

    def test_valid_float_string_overrides(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "0.5")
        assert _resolve_startup_timeout() == 0.5

    def test_non_numeric_string_raises_value_error(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "not-a-number")
        with pytest.raises(ValueError, match="not a valid number of seconds"):
            _resolve_startup_timeout()

    def test_whitespace_only_raises_value_error(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "   ")
        with pytest.raises(ValueError, match="not a valid number of seconds"):
            _resolve_startup_timeout()

    def test_negative_value_raises_value_error(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "-1")
        with pytest.raises(ValueError, match="must be a positive, finite "):
            _resolve_startup_timeout()

    def test_zero_raises_value_error(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "0")
        with pytest.raises(ValueError, match="must be a positive, finite "):
            _resolve_startup_timeout()

    def test_zero_float_raises_value_error(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "0.0")
        with pytest.raises(ValueError, match="must be a positive, finite "):
            _resolve_startup_timeout()

    @pytest.mark.parametrize("raw", ["inf", "Infinity", "+inf", "-inf", "nan", "NaN"])
    def test_non_finite_value_raises_value_error(self, monkeypatch, raw):
        # float() happily parses these. "inf" clears the `> 0` check and would
        # hang startup forever; "nan" clears it too (NaN comparisons are always
        # False) and poisons the readiness loop's deadline arithmetic.
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, raw)
        with pytest.raises(ValueError, match="must be a positive, finite "):
            _resolve_startup_timeout()

    def test_error_message_includes_env_var_name_and_value(self, monkeypatch):
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "bad")
        with pytest.raises(ValueError) as exc_info:
            _resolve_startup_timeout()
        msg = str(exc_info.value)
        assert _STARTUP_TIMEOUT_ENV_VAR in msg
        assert "bad" in msg

    def test_daemon_constructor_picks_up_env_var(self, tmp_path, monkeypatch):
        """End-to-end: env var flows into AcceleratorDaemon._startup_timeout."""
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "42")
        d = _make_daemon(tmp_path)
        assert d._startup_timeout == 42.0

    def test_daemon_constructor_invalid_env_var_raises(self, tmp_path, monkeypatch):
        """Invalid env var causes constructor to raise ValueError."""
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "xyz")
        with pytest.raises(ValueError, match="not a valid number of seconds"):
            _make_daemon(tmp_path)


# ---------------------------------------------------------------------------
# Windows (win_amd64 / win32)
# ---------------------------------------------------------------------------


class TestWindows:
    """Windows reaches the daemon over the same AF_UNIX socket as every other
    platform. What differs is that CPython's socket module does not expose the
    family, so nothing here may depend on ``socket.AF_UNIX`` — readiness goes
    through gRPC's C-core, which does speak it."""

    def test_start_is_not_blocked_by_missing_af_unix(
        self, tmp_path, monkeypatch, no_af_unix
    ):
        """The AF_UNIX guard must not fire on Windows: a missing family there
        says something about CPython, not about the platform."""
        monkeypatch.setattr(_daemon, "_IS_WINDOWS", True)

        def fake_popen(argv, **kwargs):
            raise _StopStart()

        monkeypatch.setattr(_daemon.subprocess, "Popen", fake_popen)
        d = _make_daemon(tmp_path)
        # Reaching Popen means the guard let us through.
        with pytest.raises(_StopStart):
            d.start()

    def test_readiness_does_not_touch_socket_af_unix(
        self, tmp_path, monkeypatch, no_af_unix
    ):
        """Readiness must work with no ``socket.AF_UNIX`` at all.

        This is the whole reason the probe is a gRPC channel: with the family
        absent, the wait still has to reach its timeout honestly rather than
        raise AttributeError or shortcut to "ready" off the bind artifact.
        """
        import subprocess

        proc_mock = unittest.mock.Mock(spec=subprocess.Popen)
        proc_mock.poll.return_value = None  # alive, but never binds
        proc_mock.stdin = unittest.mock.Mock()
        monkeypatch.setattr(_daemon, "_IS_WINDOWS", True)
        monkeypatch.setattr(_daemon.subprocess, "Popen", lambda *a, **kw: proc_mock)
        monkeypatch.setenv(_STARTUP_TIMEOUT_ENV_VAR, "0.05")
        d = _make_daemon(tmp_path)
        with pytest.raises(RuntimeError, match="did not become ready"):
            d.start()

    def test_readiness_reaches_a_real_grpc_server(self, tmp_path):
        """And the positive case: a server that completes the HTTP/2 handshake
        is what READY means, so the probe returns rather than timing out."""
        from concurrent import futures

        import grpc

        sock = tmp_path / _daemon._SOCKET_FILENAME
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
        server.add_insecure_port(_daemon._uds_target(str(sock)))
        server.start()
        try:
            d = _make_daemon(tmp_path)
            d._proc = unittest.mock.Mock(**{"poll.return_value": None})
            d._uds_path = str(sock)
            d._wait_until_ready(10.0)  # returns, or the test times out
        finally:
            server.stop(None)

    def test_uds_target_accepts_a_windows_path(self):
        """The channel target must survive a drive-lettered path.

        ``unix://`` opens a URI authority component, so ``unix://C:\\...``
        parses ``C:`` as the authority and gRPC refuses to build the channel at
        all — the accelerator would start, verify, and then fail every routed
        RPC. Constructing the channel is the assertion; it raises on a bad
        target before any connection is attempted.
        """
        import grpc

        from google.cloud.bigtable.data._async._accelerator_client import (
            _uds_target as _async_uds_target,
        )
        from google.cloud.bigtable.data._sync_autogen._accelerator_client import (
            _uds_target,
        )

        win_path = r"C:\Users\me\AppData\Local\Temp\bt-accel-abc123\sock"
        assert _uds_target(win_path) == "unix:" + win_path
        assert _async_uds_target(win_path) == _uds_target(win_path)
        channel = grpc.insecure_channel(_uds_target(win_path))
        try:
            stub = channel.unary_unary(
                "/google.bigtable.v2.Bigtable/MutateRow",
                request_serializer=lambda _: b"",
                response_deserializer=lambda payload: payload,
            )
            with pytest.raises(grpc.RpcError) as exc_info:
                stub(None, timeout=0.5)
        finally:
            channel.close()
        # UNAVAILABLE means the target resolved and nothing was listening, which
        # is the expected outcome. A malformed target fails earlier, as UNKNOWN.
        assert exc_info.value.code() == grpc.StatusCode.UNAVAILABLE
