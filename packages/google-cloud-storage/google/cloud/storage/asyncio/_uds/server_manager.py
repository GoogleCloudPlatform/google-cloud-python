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

"""Attach-or-spawn lifecycle management for the ``gcs-core-server`` UDS daemon.

Strategy (see the PoC design doc):

1. ``GOOGLE_CLOUD_STORAGE_UDS_SOCKET`` set -> attach to the pre-started daemon (never
   spawn, never kill).
2. Otherwise compute ``<runtime_dir>/gcs-core-<h>.sock`` where ``runtime_dir`` is
   ``$XDG_RUNTIME_DIR/gcs-core`` or ``/tmp/gcs-core-<uid>`` (``0700``, owner and
   no-symlink verified with ``lstat``) and ``h`` hashes the binary identity and the
   credential / endpoint configuration, so different configurations never share a daemon.
3. Probe the socket and verify the SERVER's uid via ``SO_PEERCRED`` (mutual auth: a
   squatted socket owned by another user is never trusted).
4. Else take ``fcntl.flock(<runtime_dir>/gcs-core-<h>.lock)``, re-probe, and spawn ONE
   shared N:1 daemon (``--idle-secs 300``) detached from the caller. Python never kills
   a shared daemon; it exits on its own after being idle.

``GOOGLE_CLOUD_STORAGE_UDS_MODE=child`` selects a 1:1 per-process daemon
(``--pdeathsig true --idle-secs 0``) for hermetic tests / serverless.
"""

from __future__ import annotations

import errno
import hashlib
import logging
import os
import shutil
import socket
import stat
import struct
import subprocess
import threading
import time
from typing import Optional

from google.cloud.storage.asyncio._uds import _config
from google.cloud.storage.asyncio._uds.errors import CoreSdkUnavailableError

logger = logging.getLogger(__name__)

DEFAULT_IDLE_SECS = 300
DEFAULT_SHM_SIZE = 64 * 1024 * 1024
DEFAULT_SPAWN_TIMEOUT_S = 15.0
BINARY_NAME = "gcs-core-server"

_lock = threading.Lock()


def _reset_after_fork() -> None:  # pragma: NO COVER - exercised in forked children
    global _lock
    _lock = threading.Lock()


if hasattr(os, "register_at_fork"):
    os.register_at_fork(after_in_child=_reset_after_fork)


def _validate_binary(path: str) -> str:
    try:
        st = os.stat(path)
    except OSError as exc:
        raise CoreSdkUnavailableError(
            f"gcs-core-server binary {path!r}: {exc}"
        ) from exc
    if stat.S_ISDIR(st.st_mode):
        raise CoreSdkUnavailableError(f"gcs-core-server binary {path!r} is a directory")
    if not os.access(path, os.X_OK):
        raise CoreSdkUnavailableError(
            f"gcs-core-server binary {path!r} is not executable"
        )
    if st.st_mode & stat.S_IWOTH:
        raise CoreSdkUnavailableError(
            f"gcs-core-server binary {path!r} is world-writable; refusing to execute it"
        )
    return os.path.abspath(path)


def resolve_binary() -> str:
    """Locates ``gcs-core-server``.

    Precedence: ``GOOGLE_CLOUD_STORAGE_UDS_BINARY`` (validated; never silently ignored),
    then ``google_cloud_storage_core.binary_path()`` (companion wheel), then ``$PATH``.
    """
    override = os.environ.get(_config.ENV_BINARY)
    if override:
        return _validate_binary(override)
    try:
        import google_cloud_storage_core  # type: ignore

        path = google_cloud_storage_core.binary_path()
        if path:
            return _validate_binary(path)
    except ImportError:
        pass
    except CoreSdkUnavailableError:
        raise
    except Exception as exc:  # pragma: NO COVER - defensive
        logger.debug("google_cloud_storage_core.binary_path() failed: %s", exc)
    found = shutil.which(BINARY_NAME)
    if found:
        return _validate_binary(found)
    raise CoreSdkUnavailableError(
        "gcs-core-server binary not found: install google-cloud-storage[uds] "
        f"(google-cloud-storage-core) or set {_config.ENV_BINARY}"
    )


def runtime_dir() -> str:
    """Returns (creating if needed) the private ``0700`` runtime directory."""
    uid = os.getuid()
    xdg = os.environ.get("XDG_RUNTIME_DIR")
    if xdg and os.path.isdir(xdg):
        path = os.path.join(xdg, "gcs-core")
    else:
        path = f"/tmp/gcs-core-{uid}"
    try:
        os.mkdir(path, 0o700)
    except FileExistsError:
        pass
    except OSError as exc:
        raise CoreSdkUnavailableError(
            f"cannot create runtime dir {path}: {exc}"
        ) from exc
    verify_private_dir(path)
    return path


def verify_private_dir(path: str) -> None:
    """Rejects runtime directories that are symlinks, not owned by us, or not ``0700``."""
    st = os.lstat(path)
    if stat.S_ISLNK(st.st_mode):
        raise CoreSdkUnavailableError(f"runtime dir {path} is a symlink")
    if not stat.S_ISDIR(st.st_mode):
        raise CoreSdkUnavailableError(f"runtime dir {path} is not a directory")
    if st.st_uid != os.getuid():
        raise CoreSdkUnavailableError(
            f"runtime dir {path} is owned by uid {st.st_uid}, not {os.getuid()}"
        )
    if stat.S_IMODE(st.st_mode) != 0o700:
        raise CoreSdkUnavailableError(
            f"runtime dir {path} has mode {oct(stat.S_IMODE(st.st_mode))}, expected 0o700"
        )


def config_hash(
    binary: str, endpoint: Optional[str], universe_domain: Optional[str]
) -> str:
    """Hash of everything the spawned daemon inherits, used to key the socket name."""
    try:
        st = os.stat(binary)
        ident = f"{binary}|{st.st_size}|{st.st_mtime_ns}"
    except OSError:
        ident = binary
    parts = [
        ident,
        endpoint or "",
        universe_domain or "",
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""),
        os.environ.get("CLOUDSDK_CONFIG", ""),
        os.environ.get("GOOGLE_CLOUD_UNIVERSE_DOMAIN", ""),
    ]
    return hashlib.sha256("\0".join(parts).encode()).hexdigest()[:12]


def peer_uid(sock: socket.socket) -> int:
    """Returns the uid of the process on the other end of a connected UDS."""
    if hasattr(socket, "SO_PEERCRED"):
        creds = sock.getsockopt(
            socket.SOL_SOCKET, socket.SO_PEERCRED, struct.calcsize("3i")
        )
        _pid, uid, _gid = struct.unpack("3i", creds)
        return uid
    if hasattr(os, "getpeereid"):  # pragma: NO COVER - macOS / BSD
        return os.getpeereid(sock.fileno())[0]  # type: ignore[attr-defined]
    # LOCAL_PEERCRED via getsockopt(SOL_LOCAL=0, LOCAL_PEERCRED=1) on Darwin.
    raw = sock.getsockopt(0, 1, 256)  # pragma: NO COVER - macOS
    return struct.unpack_from("iI", raw)[1]  # pragma: NO COVER - macOS


def verify_server_peer(sock_path: str, timeout: float = 1.0) -> bool:
    """Connects to ``sock_path`` and verifies the server runs as our uid.

    Returns ``False`` if nothing is listening; raises ``CoreSdkUnavailableError`` if a
    process owned by another uid is listening (socket squatting / impersonation).
    """
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect(sock_path)
    except (FileNotFoundError, ConnectionRefusedError):
        return False
    except OSError as exc:
        if exc.errno in (errno.ENOENT, errno.ECONNREFUSED, errno.ENOTSOCK):
            return False
        raise CoreSdkUnavailableError(f"cannot connect to {sock_path}: {exc}") from exc
    try:
        uid = peer_uid(s)
    finally:
        s.close()
    if uid != os.getuid():
        raise CoreSdkUnavailableError(
            f"{sock_path} is served by uid {uid}, not {os.getuid()}; refusing to use it"
        )
    return True


class ServerManager:
    """Attaches to (or spawns) the ``gcs-core-server`` daemon for one configuration."""

    def __init__(
        self,
        *,
        socket_path: Optional[str] = None,
        binary: Optional[str] = None,
        mode: Optional[str] = None,
        endpoint: Optional[str] = None,
        universe_domain: Optional[str] = None,
        idle_secs: int = DEFAULT_IDLE_SECS,
        shm_size: int = DEFAULT_SHM_SIZE,
        spawn_timeout: float = DEFAULT_SPAWN_TIMEOUT_S,
    ) -> None:
        self.socket_path = socket_path or os.environ.get(_config.ENV_SOCKET) or None
        self.binary = binary
        self.mode = (mode or os.environ.get(_config.ENV_TOPOLOGY) or "shared").lower()
        if self.mode not in ("shared", "child"):
            raise CoreSdkUnavailableError(
                f"{_config.ENV_TOPOLOGY} must be 'shared' or 'child', got {self.mode!r}"
            )
        self.endpoint = endpoint
        self.universe_domain = universe_domain
        self.idle_secs = idle_secs
        self.shm_size = shm_size
        self.spawn_timeout = spawn_timeout
        self.process: Optional[subprocess.Popen] = None
        self.spawned = False

    def _key(self, binary: str) -> str:
        return config_hash(binary, self.endpoint, self.universe_domain)

    def ensure_server(self) -> str:
        """Returns ``unix:///abs/path`` of a verified, running daemon."""
        if self.socket_path:
            path = os.path.abspath(self.socket_path)
            if not verify_server_peer(path):
                raise CoreSdkUnavailableError(
                    f"{_config.ENV_SOCKET}={path} is not accepting connections"
                )
            return f"unix://{path}"

        binary = self.binary or resolve_binary()
        rdir = runtime_dir()
        key = self._key(binary)
        if self.mode == "child":
            sock = os.path.join(rdir, f"gcs-core-{key}-{os.getpid()}.sock")
        else:
            sock = os.path.join(rdir, f"gcs-core-{key}.sock")

        with _lock:
            if verify_server_peer(sock):
                return f"unix://{sock}"
            import fcntl

            lock_path = os.path.join(rdir, f"gcs-core-{key}.lock")
            fd = os.open(lock_path, os.O_RDWR | os.O_CREAT | os.O_CLOEXEC, 0o600)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX)
                # Double-checked: another process may have spawned it meanwhile.
                if not verify_server_peer(sock):
                    self._spawn(binary, sock, rdir, key)
            finally:
                try:
                    fcntl.flock(fd, fcntl.LOCK_UN)
                finally:
                    os.close(fd)
        return f"unix://{sock}"

    def _spawn(self, binary: str, sock: str, rdir: str, key: str) -> None:
        args = [
            binary,
            "--socket",
            sock,
            "--default-transport",
            "grpc",
            "--shm-size",
            str(self.shm_size),
        ]
        if self.mode == "child":
            args += ["--pdeathsig", "true", "--idle-secs", "0"]
        else:
            args += ["--idle-secs", str(self.idle_secs)]
        if self.endpoint:
            args += ["--endpoint", self.endpoint]
        log_path = os.path.join(rdir, f"gcs-core-{key}.log")
        log = open(log_path, "ab")
        try:
            os.chmod(log_path, 0o600)
            logger.info("spawning %s", " ".join(args))
            self.process = subprocess.Popen(
                args,
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=log,
                close_fds=True,
                shell=False,
                start_new_session=self.mode == "shared",
            )
        except OSError as exc:
            raise CoreSdkUnavailableError(f"failed to spawn {binary}: {exc}") from exc
        finally:
            log.close()
        self.spawned = True
        deadline = time.monotonic() + self.spawn_timeout
        while time.monotonic() < deadline:
            rc = self.process.poll()
            if rc is not None:
                raise CoreSdkUnavailableError(
                    f"gcs-core-server exited with status {rc} during startup; see {log_path}"
                )
            if os.path.exists(sock) and verify_server_peer(sock):
                if os.path.exists(f"{sock}.shm") or self.shm_size == 0:
                    return
            time.sleep(0.02)
        raise CoreSdkUnavailableError(
            f"timed out after {self.spawn_timeout}s waiting for gcs-core-server on {sock}; "
            f"see {log_path}"
        )

    def shm_socket_path(self, target: str) -> str:
        assert target.startswith("unix://")
        return target[len("unix://") :] + ".shm"
