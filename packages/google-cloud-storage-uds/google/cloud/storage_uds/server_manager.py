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

"""Lifecycle manager for the standalone Rust `gcs-accelerator-server` subprocess.

Follows the Cloud Bigtable Accelerator separate-process lifecycle model:
1. Check if a server is already listening on the target Unix Domain Socket.
2. Start the server if it is not running and record its PID in a `.pid` file.
3. Wait for the server to signal readiness on its UDS socket.
4. On client close, optionally leave the server running for reuse across clients
   or terminate it via `SIGTERM` and clean up the PID and UDS files.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import shutil
import signal
import socket
import subprocess
import time


class AcceleratorStartupError(RuntimeError):
    """Raised when the `gcs-accelerator-server` sidecar fails to start or bind."""


@dataclass(frozen=True)
class ProcessMetrics:
    """CPU time and Resident Set Size (RSS) snapshot for a Linux process."""

    pid: int
    cpu_seconds: float
    rss_mib: float


def read_process_metrics(pid: int) -> ProcessMetrics:
    """Read cumulative user+system CPU seconds and VmRSS MiB from `/proc/<pid>`.

    Args:
        pid: Process ID to inspect.

    Returns:
        A `ProcessMetrics` snapshot with cumulative CPU time in seconds and
        resident memory in MiB.
    """
    clk_tck = os.sysconf("SC_CLK_TCK")
    stat_path = Path(f"/proc/{pid}/stat")
    status_path = Path(f"/proc/{pid}/status")

    cpu_seconds = 0.0
    if stat_path.exists():
        raw_stat = stat_path.read_text(encoding="utf-8")
        # Fields after the last ')' are 1-indexed starting at field 3 (state).
        # utime is field 14 (index 11 after ')') and stime is field 15 (index 12).
        after_comm = raw_stat.rsplit(")", 1)[-1].split()
        if len(after_comm) > 12:
            utime_ticks = int(after_comm[11])
            stime_ticks = int(after_comm[12])
            cpu_seconds = (utime_ticks + stime_ticks) / float(clk_tck)

    rss_mib = 0.0
    if status_path.exists():
        for line in status_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("VmRSS:"):
                parts = line.split()
                if len(parts) >= 2:
                    rss_mib = int(parts[1]) / 1024.0
                break

    return ProcessMetrics(pid=pid, cpu_seconds=cpu_seconds, rss_mib=rss_mib)


def resolve_default_binary() -> Path:
    """Locate the compiled `gcs-accelerator-server` Rust binary.

    Returns:
        Path to the executable `gcs-accelerator-server` binary.

    Raises:
        AcceleratorStartupError: If the binary cannot be found.
    """
    env_bin = os.environ.get("GCS_ACCELERATOR_BIN")
    if env_bin:
        candidate = Path(env_bin)
        if candidate.is_file():
            return candidate
        raise AcceleratorStartupError(
            f"GCS_ACCELERATOR_BIN points to missing file: {candidate}"
        )

    pkg_root = Path(__file__).resolve().parents[3]
    for profile in ("release", "debug"):
        candidate = pkg_root / "target" / profile / "gcs-accelerator-server"
        if candidate.is_file():
            return candidate

    which_bin = shutil.which("gcs-accelerator-server")
    if which_bin:
        return Path(which_bin)

    raise AcceleratorStartupError(
        "Could not locate `gcs-accelerator-server` binary. Build it with "
        "`cargo build --release` in `packages/google-cloud-storage-uds`."
    )


def _is_uds_listening(uds_path: Path) -> bool:
    """Return True if a process is actively accepting connections on `uds_path`."""
    if not uds_path.exists():
        return False
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            sock.connect(str(uds_path))
        return True
    except OSError:
        return False


class AcceleratorServerManager:
    """Manages the lifecycle of the `gcs-accelerator-server` sidecar over UDS."""

    def __init__(
        self,
        uds_path: str | Path | None = None,
        pid_file: str | Path | None = None,
        binary_path: str | Path | None = None,
        worker_threads: int = 4,
        shutdown_on_close: bool = True,
        prewarm_clients: bool = False,
        startup_timeout_s: float = 10.0,
    ) -> None:
        """Initialize the UDS server manager.

        Args:
            uds_path: Path to the Unix Domain Socket file. Defaults to
                `/tmp/gcs_accelerator_<uid>.sock`.
            pid_file: Path to the PID file. Defaults to
                `/tmp/gcs_accelerator_<uid>.pid`.
            binary_path: Optional explicit path to `gcs-accelerator-server`.
            worker_threads: Number of Tokio worker threads for the Rust server.
            shutdown_on_close: Whether `close()` terminates the sidecar server.
            prewarm_clients: Whether the Rust server should pre-initialize GCS
                credentials and HTTP/gRPC pools before reporting ready.
            startup_timeout_s: Maximum seconds to wait for server startup.
        """
        uid = os.getuid()
        self._uds_path = (
            Path(uds_path)
            if uds_path is not None
            else Path(f"/tmp/gcs_accelerator_{uid}.sock")
        )
        self._pid_file = (
            Path(pid_file)
            if pid_file is not None
            else Path(f"/tmp/gcs_accelerator_{uid}.pid")
        )
        self._binary_path = (
            Path(binary_path) if binary_path is not None else None
        )
        self._worker_threads = worker_threads
        self._shutdown_on_close = shutdown_on_close
        self._prewarm_clients = prewarm_clients
        self._startup_timeout_s = startup_timeout_s
        self._process: subprocess.Popen[str] | None = None
        self._pid: int | None = None
        self._reused_existing: bool = False

    @property
    def uds_path(self) -> Path:
        """Path to the Unix Domain Socket file."""
        return self._uds_path

    @property
    def target_uri(self) -> str:
        """gRPC target URI (`unix:///absolute/path/to/socket`) for channel creation."""
        return f"unix://{self._uds_path.resolve()}"

    @property
    def pid(self) -> int | None:
        """Process ID of the active `gcs-accelerator-server` sidecar."""
        if self._pid is not None:
            return self._pid
        if self._pid_file.exists():
            try:
                return int(self._pid_file.read_text(encoding="utf-8").strip())
            except ValueError:
                return None
        return None

    @property
    def reused_existing(self) -> bool:
        """True if this manager attached to an already-running UDS server."""
        return self._reused_existing

    def ensure_running(self) -> int:
        """Ensure the Rust UDS gRPC server is listening, starting it if needed.

        Returns:
            The PID of the running `gcs-accelerator-server` process.

        Raises:
            AcceleratorStartupError: If the server fails to start within timeout.
        """
        if _is_uds_listening(self._uds_path):
            self._reused_existing = True
            existing_pid = self.pid
            if existing_pid is not None:
                self._pid = existing_pid
                return existing_pid

        binary = (
            self._binary_path
            if self._binary_path is not None
            else resolve_default_binary()
        )
        cmd = [
            str(binary),
            "--uds-path",
            str(self._uds_path),
            "--pid-file",
            str(self._pid_file),
            "--worker-threads",
            str(self._worker_threads),
        ]
        if self._prewarm_clients:
            cmd.append("--prewarm")

        self._process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
        self._reused_existing = False

        deadline = time.monotonic() + self._startup_timeout_s
        while time.monotonic() < deadline:
            if self._process.poll() is not None:
                stderr_out = (
                    self._process.stderr.read()
                    if self._process.stderr is not None
                    else ""
                )
                raise AcceleratorStartupError(
                    f"gcs-accelerator-server exited early with code "
                    f"{self._process.returncode}: {stderr_out}"
                )
            if _is_uds_listening(self._uds_path):
                self._pid = self._process.pid
                return self._process.pid
            time.sleep(0.01)

        self.close(force=True)
        raise AcceleratorStartupError(
            f"Timed out waiting {self._startup_timeout_s}s for UDS server at "
            f"{self._uds_path}"
        )

    def get_server_metrics(self) -> ProcessMetrics | None:
        """Return CPU and RSS metrics for the Rust sidecar process if known."""
        server_pid = self.pid
        if server_pid is None:
            return None
        return read_process_metrics(server_pid)

    def close(self, *, force: bool = False) -> None:
        """Stop the sidecar server if `shutdown_on_close` or `force` is True.

        Args:
            force: If True, terminate the server even when `shutdown_on_close`
                was configured as False.
        """
        if not force and not self._shutdown_on_close:
            return

        if self._process is not None:
            if self._process.poll() is None:
                self._process.terminate()
                try:
                    self._process.wait(timeout=3.0)
                except subprocess.TimeoutExpired:
                    self._process.kill()
                    self._process.wait(timeout=1.0)
            if self._process.stdout is not None:
                self._process.stdout.close()
            if self._process.stderr is not None:
                self._process.stderr.close()
            self._process = None
        else:
            target_pid = self.pid
            if target_pid is not None:
                try:
                    os.kill(target_pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass

        for path in (self._uds_path, self._pid_file):
            try:
                if path.exists():
                    path.unlink()
            except OSError:
                pass
        self._pid = None

