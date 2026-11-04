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
"""Hermetic tests for ``google.cloud.storage.asyncio._uds.server_manager``.

No real ``gcs-core-server`` is used: a tiny Python script (written to
``tmp_path``) stands in for it, binding ``--socket`` and ``<socket>.shm``.
"""

import errno
import gc
import importlib.util
import json
import os
import shutil
import signal
import socket
import stat
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
import types
from unittest import mock

import pytest

from google.cloud.storage.asyncio._uds import _config, server_manager
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError

_FAKE_SERVER = textwrap.dedent(
    """\
    #!{python}
    import json, os, signal, socket, sys, time

    args = sys.argv[1:]

    def opt(name):
        return args[args.index(name) + 1] if name in args else None

    sock_path = opt("--socket")
    with open(os.environ["FAKE_GCS_CORE_RECORD"], "a") as f:
        f.write(json.dumps({{"pid": os.getpid(), "sid": os.getsid(0), "argv": args}}) + "\\n")
    behavior = os.environ.get("FAKE_GCS_CORE_BEHAVIOR", "ok")
    if behavior == "exit":
        sys.exit(3)
    time.sleep(float(os.environ.get("FAKE_GCS_CORE_DELAY", "0")))
    if behavior == "hang":
        time.sleep(3600)
    signal.signal(signal.SIGTERM, lambda *a: sys.exit(0))
    paths = [sock_path] if behavior == "no_shm" else [sock_path, sock_path + ".shm"]
    socks = []
    for p in paths:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(p)
        s.listen(64)
        s.setblocking(False)
        socks.append(s)
    while True:
        for s in socks:
            try:
                c, _ = s.accept()
                c.close()
            except BlockingIOError:
                pass
        time.sleep(0.005)
    """
)


@pytest.fixture
def clean_env(monkeypatch):
    for key in (
        _config.ENV_SOCKET,
        _config.ENV_BINARY,
        _config.ENV_TOPOLOGY,
        _config.ENV_FORCE,
        _config.ENV_MODE,
        "GOOGLE_APPLICATION_CREDENTIALS",
        "CLOUDSDK_CONFIG",
        "GOOGLE_CLOUD_UNIVERSE_DOMAIN",
        "FAKE_GCS_CORE_BEHAVIOR",
        "FAKE_GCS_CORE_DELAY",
    ):
        monkeypatch.delenv(key, raising=False)
    # Make sure no real companion package is picked up.
    monkeypatch.setitem(sys.modules, "google_cloud_storage_core", None)
    return monkeypatch


@pytest.fixture
def xdg(clean_env):
    # Short path: AF_UNIX socket paths are limited to ~108 bytes.
    d = tempfile.mkdtemp(prefix="x", dir="/tmp")
    clean_env.setenv("XDG_RUNTIME_DIR", d)
    yield d
    shutil.rmtree(d, ignore_errors=True)


def _make_exe(path, body="#!/bin/sh\nexit 0\n", mode=0o755):
    with open(path, "w") as f:
        f.write(body)
    os.chmod(path, mode)
    return str(path)


@pytest.fixture
def fake_server(tmp_path, clean_env):
    """Writes the fake gcs-core-server and kills everything it spawned."""
    record = tmp_path / "record.jsonl"
    record.touch()
    clean_env.setenv("FAKE_GCS_CORE_RECORD", str(record))
    binary = _make_exe(
        tmp_path / "gcs-core-server", _FAKE_SERVER.format(python=sys.executable)
    )

    def entries():
        with open(record) as f:
            return [json.loads(line) for line in f if line.strip()]

    ns = types.SimpleNamespace(binary=binary, record=record, entries=entries)
    yield ns
    for entry in entries():
        try:
            os.kill(entry["pid"], signal.SIGKILL)
        except ProcessLookupError:
            pass
        try:
            os.waitpid(entry["pid"], 0)
        except ChildProcessError:
            pass


def _alive(pid):
    # ``pid`` is our (Popen) child: a non-zero waitpid() means it exited (zombie).
    done, _ = os.waitpid(pid, os.WNOHANG)
    return done == 0


# ---------------------------------------------------------------- resolve_binary


def test_resolve_binary_env_override(tmp_path, clean_env):
    exe = _make_exe(tmp_path / "custom-server")
    clean_env.setenv(_config.ENV_BINARY, exe)
    assert server_manager.resolve_binary() == os.path.abspath(exe)


def test_resolve_binary_env_override_relative_path_is_made_absolute(
    tmp_path, clean_env
):
    _make_exe(tmp_path / "rel-server")
    clean_env.chdir(tmp_path)
    clean_env.setenv(_config.ENV_BINARY, "rel-server")
    assert server_manager.resolve_binary() == str(tmp_path / "rel-server")


@pytest.mark.parametrize(
    "kind,match",
    [
        ("dir", "is a directory"),
        ("nonexec", "not executable"),
        ("world_writable", "world-writable"),
        ("missing", "No such file"),
    ],
)
def test_resolve_binary_env_override_is_validated(tmp_path, clean_env, kind, match):
    path = tmp_path / "bad"
    if kind == "dir":
        path.mkdir()
    elif kind == "nonexec":
        _make_exe(path, mode=0o644)
    elif kind == "world_writable":
        _make_exe(path, mode=0o777)
    # A valid binary on PATH must NOT be used as a silent fallback.
    good_dir = tmp_path / "bin"
    good_dir.mkdir()
    _make_exe(good_dir / server_manager.BINARY_NAME)
    clean_env.setenv("PATH", str(good_dir))
    clean_env.setenv(_config.ENV_BINARY, str(path))
    with pytest.raises(CoreSdkUnavailableError, match=match):
        server_manager.resolve_binary()


def test_resolve_binary_precedence_env_then_companion_then_path(tmp_path, clean_env):
    env_exe = _make_exe(tmp_path / "env-server")
    wheel_exe = _make_exe(tmp_path / "wheel-server")
    path_dir = tmp_path / "bin"
    path_dir.mkdir()
    path_exe = _make_exe(path_dir / server_manager.BINARY_NAME)
    clean_env.setenv("PATH", str(path_dir))
    companion = types.ModuleType("google_cloud_storage_core")
    companion.binary_path = lambda: wheel_exe
    clean_env.setitem(sys.modules, "google_cloud_storage_core", companion)

    clean_env.setenv(_config.ENV_BINARY, env_exe)
    assert server_manager.resolve_binary() == env_exe

    clean_env.delenv(_config.ENV_BINARY)
    assert server_manager.resolve_binary() == wheel_exe

    companion.binary_path = lambda: None
    assert server_manager.resolve_binary() == path_exe

    clean_env.setitem(sys.modules, "google_cloud_storage_core", None)  # not installed
    assert server_manager.resolve_binary() == path_exe


def test_resolve_binary_companion_invalid_path_is_not_silently_ignored(
    tmp_path, clean_env
):
    path_dir = tmp_path / "bin"
    path_dir.mkdir()
    _make_exe(path_dir / server_manager.BINARY_NAME)
    clean_env.setenv("PATH", str(path_dir))
    companion = types.ModuleType("google_cloud_storage_core")
    companion.binary_path = lambda: str(tmp_path / "missing")
    clean_env.setitem(sys.modules, "google_cloud_storage_core", companion)
    with pytest.raises(CoreSdkUnavailableError):
        server_manager.resolve_binary()


def test_resolve_binary_not_found(tmp_path, clean_env):
    empty = tmp_path / "empty"
    empty.mkdir()
    clean_env.setenv("PATH", str(empty))
    with pytest.raises(CoreSdkUnavailableError, match=_config.ENV_BINARY):
        server_manager.resolve_binary()


def test_resolve_binary_path_entry_is_validated(tmp_path, clean_env):
    path_dir = tmp_path / "bin"
    path_dir.mkdir()
    _make_exe(path_dir / server_manager.BINARY_NAME, mode=0o777)
    clean_env.setenv("PATH", str(path_dir))
    with pytest.raises(CoreSdkUnavailableError, match="world-writable"):
        server_manager.resolve_binary()


# ------------------------------------------------------------------- runtime_dir


def test_runtime_dir_created_private_under_xdg(xdg):
    path = server_manager.runtime_dir()
    assert path == os.path.join(xdg, "gcs-core")
    st = os.lstat(path)
    assert stat.S_ISDIR(st.st_mode)
    assert stat.S_IMODE(st.st_mode) == 0o700
    assert st.st_uid == os.getuid()
    assert server_manager.runtime_dir() == path  # idempotent


def test_runtime_dir_falls_back_to_tmp_without_xdg(clean_env):
    clean_env.setenv("XDG_RUNTIME_DIR", "/nonexistent-xdg-dir-for-test")
    made, verified = [], []
    clean_env.setattr(server_manager.os, "mkdir", lambda p, m: made.append((p, m)))
    clean_env.setattr(server_manager, "verify_private_dir", verified.append)
    expected = f"/tmp/gcs-core-{os.getuid()}"
    assert server_manager.runtime_dir() == expected
    assert made == [(expected, 0o700)]
    assert verified == [expected]


def test_runtime_dir_rejects_group_or_world_accessible_dir(xdg):
    os.mkdir(os.path.join(xdg, "gcs-core"), 0o700)
    os.chmod(os.path.join(xdg, "gcs-core"), 0o755)
    with pytest.raises(CoreSdkUnavailableError, match="expected 0o700"):
        server_manager.runtime_dir()


def test_runtime_dir_rejects_symlink(xdg):
    target = os.path.join(xdg, "elsewhere")
    os.mkdir(target, 0o700)
    os.symlink(target, os.path.join(xdg, "gcs-core"))
    with pytest.raises(CoreSdkUnavailableError, match="symlink"):
        server_manager.runtime_dir()


def test_runtime_dir_rejects_non_directory(xdg):
    with open(os.path.join(xdg, "gcs-core"), "w"):
        pass
    with pytest.raises(CoreSdkUnavailableError, match="not a directory"):
        server_manager.runtime_dir()


def test_verify_private_dir_rejects_foreign_owner(tmp_path, monkeypatch):
    d = tmp_path / "rd"
    d.mkdir(mode=0o700)
    real_uid = os.getuid()
    monkeypatch.setattr(server_manager.os, "getuid", lambda: real_uid + 1)
    with pytest.raises(CoreSdkUnavailableError, match="owned by uid"):
        server_manager.verify_private_dir(str(d))


def test_runtime_dir_mkdir_failure_is_core_sdk_unavailable(clean_env, tmp_path):
    clean_env.setenv("XDG_RUNTIME_DIR", str(tmp_path))

    def _fail(path, mode):
        raise PermissionError(errno.EACCES, "denied")

    clean_env.setattr(server_manager.os, "mkdir", _fail)
    with pytest.raises(CoreSdkUnavailableError, match="cannot create runtime dir"):
        server_manager.runtime_dir()


# ------------------------------------------------------------------- config_hash


def test_config_hash_is_stable_and_short(tmp_path, clean_env):
    exe = _make_exe(tmp_path / "srv")
    h = server_manager.config_hash(exe, "https://e", "u")
    assert h == server_manager.config_hash(exe, "https://e", "u")
    assert len(h) == 12
    int(h, 16)


def test_config_hash_differs_by_endpoint_universe_and_credential_env(
    tmp_path, clean_env
):
    exe = _make_exe(tmp_path / "srv")
    base = server_manager.config_hash(exe, None, None)
    hashes = {
        base,
        server_manager.config_hash(exe, "http://127.0.0.1:9000", None),
        server_manager.config_hash(exe, "https://storage.example.com", None),
        server_manager.config_hash(exe, None, "example.com"),
    }
    for env in (
        "GOOGLE_APPLICATION_CREDENTIALS",
        "CLOUDSDK_CONFIG",
        "GOOGLE_CLOUD_UNIVERSE_DOMAIN",
    ):
        clean_env.setenv(env, f"/some/{env}")
        hashes.add(server_manager.config_hash(exe, None, None))
        clean_env.delenv(env)
    assert len(hashes) == 7
    assert server_manager.config_hash(exe, None, None) == base


def test_config_hash_differs_by_binary_identity(tmp_path, clean_env):
    exe = _make_exe(tmp_path / "srv")
    h1 = server_manager.config_hash(exe, None, None)
    with open(exe, "a") as f:
        f.write("# rebuilt\n")
    os.utime(exe, ns=(1, 1))
    assert server_manager.config_hash(exe, None, None) != h1
    other = _make_exe(tmp_path / "srv2")
    assert server_manager.config_hash(other, None, None) != h1
    # A missing binary still hashes (by path).
    assert len(server_manager.config_hash(str(tmp_path / "gone"), None, None)) == 12


# ----------------------------------------------------------- peer verification


def test_peer_uid_of_socketpair_is_our_uid():
    a, b = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        assert server_manager.peer_uid(a) == os.getuid()
    finally:
        a.close()
        b.close()


@pytest.fixture
def listener():
    d = tempfile.mkdtemp(prefix="l", dir="/tmp")
    path = os.path.join(d, "srv.sock")
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind(path)
    s.listen(8)
    yield path
    s.close()
    shutil.rmtree(d, ignore_errors=True)


def test_verify_server_peer_true_for_our_listener(listener):
    assert server_manager.verify_server_peer(listener) is True


def test_verify_server_peer_false_when_nothing_listens(tmp_path):
    assert server_manager.verify_server_peer(str(tmp_path / "missing.sock")) is False
    # Bound but not listening -> ECONNREFUSED.
    d = tempfile.mkdtemp(prefix="l", dir="/tmp")
    try:
        path = os.path.join(d, "dead.sock")
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(path)
        try:
            assert server_manager.verify_server_peer(path) is False
        finally:
            s.close()
        # A regular file at the socket path.
        regular = os.path.join(d, "file.sock")
        with open(regular, "w"):
            pass
        assert server_manager.verify_server_peer(regular) is False
    finally:
        shutil.rmtree(d, ignore_errors=True)


def test_verify_server_peer_rejects_foreign_uid(listener, monkeypatch):
    monkeypatch.setattr(server_manager, "peer_uid", lambda s: os.getuid() + 1)
    with pytest.raises(CoreSdkUnavailableError, match="refusing to use it"):
        server_manager.verify_server_peer(listener)


def _patch_connect_error(monkeypatch, err):
    class _Sock:
        def __init__(self, family, kind):
            assert (family, kind) == (socket.AF_UNIX, socket.SOCK_STREAM)

        def settimeout(self, timeout):
            pass

        def connect(self, path):
            raise err

    fake = types.SimpleNamespace(
        AF_UNIX=socket.AF_UNIX, SOCK_STREAM=socket.SOCK_STREAM, socket=_Sock
    )
    monkeypatch.setattr(server_manager, "socket", fake)


def test_verify_server_peer_false_for_enotsock(monkeypatch):
    _patch_connect_error(monkeypatch, OSError(errno.ENOTSOCK, "not a socket"))
    assert server_manager.verify_server_peer("/run/whatever.sock") is False


def test_verify_server_peer_raises_on_other_connect_errors(monkeypatch):
    _patch_connect_error(monkeypatch, PermissionError(errno.EACCES, "denied"))
    with pytest.raises(CoreSdkUnavailableError, match="cannot connect to") as info:
        server_manager.verify_server_peer("/run/whatever.sock")
    assert isinstance(info.value.__cause__, PermissionError)


def test_module_import_without_register_at_fork(monkeypatch):
    """Platforms without ``os.register_at_fork`` skip the after-fork lock reset."""
    monkeypatch.delattr(os, "register_at_fork")
    spec = importlib.util.spec_from_file_location(
        "_server_manager_without_fork_hook", server_manager.__file__
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module._lock is not server_manager._lock
    assert module.BINARY_NAME == server_manager.BINARY_NAME


# ----------------------------------------------------------------- ServerManager


def test_server_manager_mode_selection(clean_env):
    assert server_manager.ServerManager().mode == "shared"
    clean_env.setenv(_config.ENV_TOPOLOGY, "CHILD")
    assert server_manager.ServerManager().mode == "child"
    assert server_manager.ServerManager(mode="shared").mode == "shared"
    with pytest.raises(CoreSdkUnavailableError, match="'shared' or 'child'"):
        server_manager.ServerManager(mode="sidecar")


def test_attach_via_socket_env_never_spawns(listener, clean_env, monkeypatch):
    clean_env.setenv(_config.ENV_SOCKET, listener)
    clean_env.setenv(_config.ENV_BINARY, "/nonexistent/gcs-core-server")

    boom = mock.Mock(side_effect=AssertionError("must not resolve or spawn"))
    monkeypatch.setattr(server_manager, "resolve_binary", boom)
    monkeypatch.setattr(server_manager.ServerManager, "_spawn", boom)
    mgr = server_manager.ServerManager()
    assert mgr.socket_path == listener
    target = mgr.ensure_server()
    assert target == f"unix://{listener}"
    assert mgr.spawned is False
    assert mgr.process is None
    assert mgr.shm_socket_path(target) == f"{listener}.shm"
    boom.assert_not_called()


def test_ensure_server_double_checked_lock_skips_spawn(xdg, monkeypatch):
    """Another process spawned the daemon while we waited for the flock."""
    probes = iter([False, True])
    monkeypatch.setattr(server_manager, "verify_server_peer", lambda p: next(probes))
    spawn = mock.Mock()
    monkeypatch.setattr(server_manager.ServerManager, "_spawn", spawn)
    mgr = server_manager.ServerManager(binary="/nonexistent/gcs-core-server")
    target = mgr.ensure_server()
    key = mgr._key("/nonexistent/gcs-core-server")
    sock = os.path.join(xdg, "gcs-core", f"gcs-core-{key}.sock")
    assert target == f"unix://{sock}"
    spawn.assert_not_called()
    assert mgr.spawned is False


def test_attach_via_socket_env_not_listening_raises(tmp_path, clean_env):
    clean_env.setenv(_config.ENV_SOCKET, str(tmp_path / "nobody.sock"))
    with pytest.raises(CoreSdkUnavailableError, match="not accepting connections"):
        server_manager.ServerManager().ensure_server()


def test_spawn_shared_daemon(fake_server, xdg):
    mgr = server_manager.ServerManager(binary=fake_server.binary, mode="shared")
    target = mgr.ensure_server()
    key = server_manager.config_hash(fake_server.binary, None, None)
    sock = os.path.join(xdg, "gcs-core", f"gcs-core-{key}.sock")
    assert target == f"unix://{sock}"
    assert mgr.spawned is True
    assert os.path.exists(sock) and os.path.exists(f"{sock}.shm")
    (entry,) = fake_server.entries()
    argv = entry["argv"]
    assert argv[argv.index("--socket") + 1] == sock
    assert argv[argv.index("--default-transport") + 1] == "grpc"
    assert argv[argv.index("--shm-size") + 1] == str(server_manager.DEFAULT_SHM_SIZE)
    assert argv[argv.index("--idle-secs") + 1] == str(server_manager.DEFAULT_IDLE_SECS)
    assert "--pdeathsig" not in argv
    assert "--endpoint" not in argv
    # Detached from the caller's session (start_new_session=True).
    assert entry["sid"] == entry["pid"]
    log = os.path.join(xdg, "gcs-core", f"gcs-core-{key}.log")
    assert stat.S_IMODE(os.stat(log).st_mode) == 0o600

    # A second manager attaches to the running daemon instead of spawning.
    mgr2 = server_manager.ServerManager(binary=fake_server.binary, mode="shared")
    assert mgr2.ensure_server() == target
    assert mgr2.spawned is False
    assert len(fake_server.entries()) == 1


def test_spawn_child_daemon_socket_keyed_by_pid(fake_server, xdg):
    mgr = server_manager.ServerManager(binary=fake_server.binary, mode="child")
    target = mgr.ensure_server()
    assert target.endswith(f"-{os.getpid()}.sock")
    (entry,) = fake_server.entries()
    argv = entry["argv"]
    assert argv[argv.index("--pdeathsig") + 1] == "true"
    assert argv[argv.index("--idle-secs") + 1] == "0"
    assert entry["sid"] != entry["pid"]  # stays in the caller's session
    # The shared-mode socket for the same config is a different path.
    key = server_manager.config_hash(fake_server.binary, None, None)
    assert target != f"unix://{os.path.join(xdg, 'gcs-core', f'gcs-core-{key}.sock')}"


def test_spawn_passes_endpoint_and_keys_socket_on_it(fake_server, xdg):
    a = server_manager.ServerManager(
        binary=fake_server.binary, mode="shared", endpoint="http://127.0.0.1:9000"
    )
    b = server_manager.ServerManager(binary=fake_server.binary, mode="shared")
    ta, tb = a.ensure_server(), b.ensure_server()
    assert ta != tb
    argvs = [e["argv"] for e in fake_server.entries()]
    assert len(argvs) == 2
    assert argvs[0][argvs[0].index("--endpoint") + 1] == "http://127.0.0.1:9000"
    assert "--endpoint" not in argvs[1]


def test_python_never_kills_the_shared_daemon(fake_server, xdg):
    mgr = server_manager.ServerManager(binary=fake_server.binary, mode="shared")
    mgr.ensure_server()
    pid = fake_server.entries()[0]["pid"]
    assert not any(
        hasattr(mgr, name) for name in ("kill", "terminate", "shutdown", "stop")
    )
    del mgr
    gc.collect()
    time.sleep(0.2)
    assert _alive(pid)


def test_concurrent_threads_spawn_only_one_daemon(fake_server, xdg, monkeypatch):
    monkeypatch.setenv("FAKE_GCS_CORE_DELAY", "0.5")
    results, errors = [], []

    def run():
        try:
            mgr = server_manager.ServerManager(binary=fake_server.binary, mode="shared")
            results.append(mgr.ensure_server())
        except Exception as exc:  # pragma: NO COVER - reported below
            errors.append(exc)

    threads = [threading.Thread(target=run) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(30)
    assert not errors
    assert len(results) == 4 and len(set(results)) == 1
    assert len(fake_server.entries()) == 1


def test_concurrent_processes_spawn_only_one_daemon(fake_server, xdg, monkeypatch):
    monkeypatch.setenv("FAKE_GCS_CORE_DELAY", "1.0")
    code = textwrap.dedent(
        f"""
        from google.cloud.storage.asyncio._uds import server_manager
        print(server_manager.ServerManager(binary={fake_server.binary!r}, mode="shared").ensure_server())
        """
    )
    procs = [
        subprocess.Popen(
            [sys.executable, "-c", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(2)
    ]
    outs = []
    for p in procs:
        out, err = p.communicate(timeout=60)
        assert p.returncode == 0, err
        outs.append(out.strip())
    assert outs[0] == outs[1] and outs[0].startswith("unix://")
    assert len(fake_server.entries()) == 1  # flock + double-checked probe


def test_spawn_startup_exit_raises(fake_server, xdg, monkeypatch):
    monkeypatch.setenv("FAKE_GCS_CORE_BEHAVIOR", "exit")
    mgr = server_manager.ServerManager(binary=fake_server.binary, mode="child")
    with pytest.raises(CoreSdkUnavailableError, match="exited with status 3"):
        mgr.ensure_server()


def test_spawn_timeout_raises(fake_server, xdg, monkeypatch):
    monkeypatch.setenv("FAKE_GCS_CORE_BEHAVIOR", "hang")
    mgr = server_manager.ServerManager(
        binary=fake_server.binary, mode="child", spawn_timeout=0.5
    )
    with pytest.raises(CoreSdkUnavailableError, match="timed out"):
        mgr.ensure_server()
    mgr.process.kill()
    mgr.process.wait()


def test_spawn_waits_for_shm_socket_unless_shm_disabled(fake_server, xdg, monkeypatch):
    monkeypatch.setenv("FAKE_GCS_CORE_BEHAVIOR", "no_shm")
    no_shm = server_manager.ServerManager(
        binary=fake_server.binary, mode="child", shm_size=0
    )
    assert no_shm.ensure_server().startswith("unix://")
    args = fake_server.entries()[0]["argv"]
    assert args[args.index("--shm-size") + 1] == "0"
    no_shm.process.kill()
    no_shm.process.wait()

    waits = server_manager.ServerManager(
        binary=fake_server.binary,
        mode="shared",
        endpoint="http://other",
        spawn_timeout=0.5,
    )
    with pytest.raises(CoreSdkUnavailableError, match="timed out"):
        waits.ensure_server()


def test_spawn_failure_is_core_sdk_unavailable(tmp_path, xdg):
    not_exec = _make_exe(tmp_path / "not-exec", mode=0o644)
    mgr = server_manager.ServerManager(binary=not_exec, mode="child")
    with pytest.raises(CoreSdkUnavailableError, match="failed to spawn"):
        mgr.ensure_server()
