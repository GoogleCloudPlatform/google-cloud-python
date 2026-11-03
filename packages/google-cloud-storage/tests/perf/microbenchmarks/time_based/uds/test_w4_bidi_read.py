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
"""Workload 4 (W4): time-based BidiReads via ``AsyncMultiRangeDownloader``.

N worker processes (multiprocessing ``spawn``) each open one
``AsyncMultiRangeDownloader`` on a pre-created object of ``object_size`` and
issue random ``range_size`` ``download_ranges`` calls for ``duration_s``
seconds after a ``warmup_s`` warmup. The run is repeated for every
mode x topology x round in ``config.yaml`` (overridable by ``UDS_BENCH_*``
env vars and, when run as a script, by CLI args).

Only public APIs are used: ``AsyncGrpcClient(attempt_direct_path=False)``
(gRPC CloudPath only), ``AsyncMultiRangeDownloader`` and
``AsyncAppendableObjectWriter`` (object setup). The Rust UDS core is selected
transparently through the env vars documented in ``config.yaml``; each worker
sets them for its mode *before* importing ``google.cloud.storage``.

This module also hosts the shared harness (config loading, process
orchestration, resource sampling, JSON reporting, object setup/cleanup) that
``test_w5_bidi_write.py`` imports.

Examples (from ``packages/google-cloud-storage``)::

    # pytest (yaml + UDS_BENCH_* env only; --force-use-core-sdk => uds-* modes only)
    UDS_BENCH_WORKERS=2 UDS_BENCH_DURATION_S=5 UDS_BENCH_WARMUP_S=1 \\
    UDS_BENCH_OBJECT_SIZE=8MiB UDS_BENCH_ROUNDS=1 \\
        pytest -s tests/perf/microbenchmarks/time_based/uds/test_w4_bidi_read.py \\
        --force-use-core-sdk

    # script
    python tests/perf/microbenchmarks/time_based/uds/test_w4_bidi_read.py \\
        --workers 2 --duration 5 --warmup 1 --rounds 1 --object-size 8MiB \\
        --range-size 1MiB --bucket chandrasiri-gcsfs-zb --force-use-core-sdk
"""

from __future__ import annotations

import argparse
import asyncio
import dataclasses
import io
import json
import math
import multiprocessing
import os
import queue
import random
import re
import socket
import statistics
import sys
import tempfile
import threading
import time
import traceback
import uuid
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import psutil
import pytest

# NOTE: nothing from ``google.cloud.storage`` may be imported at module level.
# Spawned workers import this module *before* ``apply_mode_env`` runs, and the
# UDS selection env vars must be in place before the library is imported.

_HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(_HERE, "config.yaml")

OBJECT_PREFIX = "uds-bench-"
MODES = ("gapic", "uds-inline", "uds-shm")
TOPOLOGIES = ("shared", "child")
READ_BUFFERS = ("prealloc", "bytesio", "discard")

FORCE_FLAG = "--force-use-core-sdk"
FORCE_XOPTION = "gcs_force_use_core_sdk"
ENV_FORCE = "GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK"
ENV_UDS = "GOOGLE_CLOUD_STORAGE_UDS"
ENV_UDS_MODE = "GOOGLE_CLOUD_STORAGE_UDS_MODE"
ENV_UDS_SHM = "GOOGLE_CLOUD_STORAGE_UDS_SHM"
DAEMON_PROCESS_NAME = "gcs-core-server"
ENV_DAEMON_PIDS = "UDS_BENCH_DAEMON_PIDS"  # optional explicit daemon pids
ENV_IRQ_AFFINITY = "UDS_BENCH_IRQ_AFFINITY"  # "0" disables IRQ CPU exclusion

_TRUTHY = ("1", "true", "yes", "on", "y")
# Flush interval used only for *setup* objects (must be a multiple of 2 MiB).
_SETUP_FLUSH_INTERVAL_BYTES = 1026 * 1024 * 1024
_SETUP_APPEND_SIZE = 16 * 1024 * 1024
_MiB = 1024 * 1024
_GiB = 1024 * 1024 * 1024


class BenchmarkError(RuntimeError):
    """A benchmark run failed; carries objects that may still need deleting."""

    def __init__(self, message: str, leftover_objects: Iterable[str] = ()):
        super().__init__(message)
        self.leftover_objects = list(leftover_objects)


# --------------------------------------------------------------------------
# Configuration: config.yaml < UDS_BENCH_* env vars < CLI args
# --------------------------------------------------------------------------


@dataclasses.dataclass
class BenchConfig:
    project: str = "vaibhavpratap-sdk-test"
    bucket: str = "chandrasiri-gcsfs-zb"
    bucket_zone: str = "us-west4-a"
    runner_vm: str = "chandrasiri-rcu-us-central1-a"
    runner_zone: str = "us-central1-a"
    object_size: int = 200 * 1000 * 1000
    workers: int = 48
    concurrency: int = 1
    duration_s: float = 300.0
    warmup_s: float = 30.0
    rounds: int = 3
    modes: List[str] = dataclasses.field(default_factory=lambda: list(MODES))
    topologies: List[str] = dataclasses.field(default_factory=lambda: list(TOPOLOGIES))
    range_size: int = 16 * _MiB
    ranges_per_op: int = 1
    num_objects: int = 0
    read_buffer: str = "prealloc"
    append_size: int = 16 * _MiB
    flush_interval_bytes: List[int] = dataclasses.field(
        default_factory=lambda: [16 * _MiB, 128 * _MiB]
    )
    output_dir: str = ""
    setup_timeout_s: float = 600.0
    kill_spawned_daemons: bool = True
    # Derived (not configurable via yaml/env/CLI specs below).
    force_core_sdk: bool = False
    modes_explicit: bool = False


# (field, env var, CLI flag, kind, help)
_SPECS: List[Tuple[str, str, str, str, str]] = [
    ("project", "UDS_BENCH_PROJECT", "--project", "str", "GCP project (listing/cleanup)."),
    ("bucket", "UDS_BENCH_BUCKET", "--bucket", "str", "Rapid (zonal) bucket name."),
    ("bucket_zone", "UDS_BENCH_BUCKET_ZONE", "--bucket-zone", "str", "Bucket zone (metadata only)."),
    ("runner_vm", "UDS_BENCH_RUNNER_VM", "--runner-vm", "str", "Runner VM (metadata only)."),
    ("runner_zone", "UDS_BENCH_RUNNER_ZONE", "--runner-zone", "str", "Runner zone (metadata only)."),
    ("object_size", "UDS_BENCH_OBJECT_SIZE", "--object-size", "size", "Object size, e.g. 200MB, 8MiB."),
    ("workers", "UDS_BENCH_WORKERS", "--workers", "int", "Worker processes."),
    ("concurrency", "UDS_BENCH_CONCURRENCY", "--concurrency", "int", "Coroutines per worker."),
    ("duration_s", "UDS_BENCH_DURATION_S", "--duration", "float", "Measured seconds per run."),
    ("warmup_s", "UDS_BENCH_WARMUP_S", "--warmup", "float", "Warmup seconds per run."),
    ("rounds", "UDS_BENCH_ROUNDS", "--rounds", "int", "Rounds per matrix entry."),
    ("modes", "UDS_BENCH_MODES", "--modes", "list", "Comma list of gapic,uds-inline,uds-shm."),
    ("topologies", "UDS_BENCH_TOPOLOGIES", "--topologies", "list", "Comma list of shared,child."),
    ("range_size", "UDS_BENCH_RANGE_SIZE", "--range-size", "size", "W4 range size."),
    ("ranges_per_op", "UDS_BENCH_RANGES_PER_OP", "--ranges-per-op", "int", "W4 ranges per download_ranges call."),
    ("num_objects", "UDS_BENCH_NUM_OBJECTS", "--num-objects", "int", "W4 objects (0 => one per worker)."),
    ("read_buffer", "UDS_BENCH_READ_BUFFER", "--read-buffer", "str", "W4 sink: prealloc|bytesio|discard."),
    ("append_size", "UDS_BENCH_APPEND_SIZE", "--append-size", "size", "W5 bytes per append() call."),
    ("flush_interval_bytes", "UDS_BENCH_FLUSH_INTERVAL_BYTES", "--flush-interval-bytes", "sizelist", "W5 comma list, e.g. 16MiB,128MiB."),
    ("output_dir", "UDS_BENCH_OUTPUT_DIR", "--output-dir", "str", "JSON results dir."),
    ("setup_timeout_s", "UDS_BENCH_SETUP_TIMEOUT_S", "--setup-timeout", "float", "Worker startup / object setup timeout."),
    ("kill_spawned_daemons", "UDS_BENCH_KILL_SPAWNED_DAEMONS", "--kill-spawned-daemons", "bool", "Kill gcs-core-server daemons spawned by a run (true|false)."),
]

_SIZE_UNITS = {
    "": 1, "b": 1,
    "k": 1000, "kb": 1000, "m": 1000**2, "mb": 1000**2, "g": 1000**3, "gb": 1000**3,
    "ki": 1024, "kib": 1024, "mi": 1024**2, "mib": 1024**2, "gi": 1024**3, "gib": 1024**3,
}


def parse_size(value: Any) -> int:
    """Parses ``8MiB`` / ``200MB`` / ``1048576`` into bytes."""
    if isinstance(value, bool):
        raise ValueError(f"invalid size: {value!r}")
    if isinstance(value, int):
        return value
    text = str(value).strip().lower().replace("_", "")
    match = re.fullmatch(r"(\d+(?:\.\d+)?)\s*([a-z]*)", text)
    if not match or match.group(2) not in _SIZE_UNITS:
        raise ValueError(f"invalid size: {value!r}")
    return int(float(match.group(1)) * _SIZE_UNITS[match.group(2)])


def format_size(n: int) -> str:
    for unit, factor in (("GiB", _GiB), ("MiB", _MiB), ("KiB", 1024)):
        if n >= factor and n % factor == 0:
            return f"{n // factor}{unit}"
    return f"{n}B"


def _as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        items = [str(v) for v in value]
    else:
        items = str(value).split(",")
    return [i.strip().strip("'\"") for i in items if i.strip()]


def _coerce(kind: str, value: Any) -> Any:
    if kind == "str":
        return "" if value is None else str(value)
    if kind == "int":
        return int(value)
    if kind == "float":
        return float(value)
    if kind == "size":
        return parse_size(value)
    if kind == "list":
        return [v.lower() for v in _as_list(value)]
    if kind == "sizelist":
        return [parse_size(v) for v in _as_list(value)]
    if kind == "bool":
        return value if isinstance(value, bool) else str(value).strip().lower() in _TRUTHY
    raise ValueError(kind)


def _unquote(text: str) -> str:
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "'\"":
        return text[1:-1]
    return text


def load_yaml_config(path: str = CONFIG_PATH) -> Dict[str, Any]:
    """Loads config.yaml with PyYAML, or a tiny flat-yaml fallback parser."""
    if not os.path.exists(path):
        return {}
    try:
        import yaml  # type: ignore

        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        pass
    data: Dict[str, Any] = {}
    with open(path, "r") as f:
        for raw in f:
            if not raw.strip() or raw[0] in " \t#":
                continue
            line = raw.split("#", 1)[0].rstrip()
            if ":" not in line:
                continue
            key, val = line.split(":", 1)
            val = val.strip()
            if val.startswith("[") and val.endswith("]"):
                data[key.strip()] = [_unquote(x) for x in val[1:-1].split(",") if x.strip()]
            else:
                data[key.strip()] = _unquote(val)
    return data


def force_flag_present(argv: Optional[Sequence[str]] = None) -> bool:
    """True if ``--force-use-core-sdk`` was requested (argv, -X option or env)."""
    args = sys.argv if argv is None else argv
    if FORCE_FLAG in args:
        return True
    if FORCE_XOPTION in getattr(sys, "_xoptions", {}):
        return True
    if os.environ.get(ENV_FORCE, "").strip().lower() in _TRUTHY:
        return True
    return os.environ.get(ENV_UDS, "").strip().lower() == "on"


def build_arg_parser(workload: str, description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=f"test_{workload}",
        description=description,
        epilog=(
            "Every option defaults to config.yaml, overridden by the UDS_BENCH_* env var "
            "shown in brackets. --force-use-core-sdk (without --modes/UDS_BENCH_MODES) "
            "restricts the matrix to uds-* modes."
        ),
    )
    for field, env, flag, kind, help_text in _SPECS:
        parser.add_argument(flag, dest=field, default=None, type=str, help=f"{help_text} [{env}]")
    try:
        from google.cloud.storage.asyncio._uds._config import add_core_sdk_cli_flags
    except ImportError:
        add_core_sdk_cli_flags = None
    if add_core_sdk_cli_flags is not None:
        add_core_sdk_cli_flags(parser)
    else:
        parser.add_argument(
            FORCE_FLAG,
            dest="force_use_core_sdk",
            action="store_true",
            help="Run only uds-* modes; fail loudly instead of falling back to GAPIC.",
        )
    return parser


def load_config(
    argv: Optional[Sequence[str]] = None,
    workload: str = "w4",
    description: str = "",
) -> BenchConfig:
    """Builds the config. ``argv=None`` => yaml + env only (pytest mode)."""
    values: Dict[str, Any] = dataclasses.asdict(BenchConfig())
    yaml_values = load_yaml_config()
    kinds = {field: kind for field, _, _, kind, _ in _SPECS}
    for field in kinds:
        if field in yaml_values and yaml_values[field] is not None:
            values[field] = yaml_values[field]
    explicit = set()
    for field, env, _, _, _ in _SPECS:
        if os.environ.get(env, "").strip():
            values[field] = os.environ[env]
            explicit.add(field)
    force = force_flag_present()
    if argv is not None:
        ns = build_arg_parser(workload, description).parse_args(list(argv))
        for field in kinds:
            v = getattr(ns, field, None)
            if v is not None:
                values[field] = v
                explicit.add(field)
        force = force or bool(getattr(ns, "force_use_core_sdk", False)) or FORCE_FLAG in argv
    for field, kind in kinds.items():
        values[field] = _coerce(kind, values[field])
    values["force_core_sdk"] = force
    values["modes_explicit"] = "modes" in explicit
    if force and not values["modes_explicit"]:
        values["modes"] = [m for m in values["modes"] if m != "gapic"] or ["uds-shm"]
    if "range_size" not in explicit and values["range_size"] > values["object_size"]:
        # e.g. `--object-size 8MiB` smoke runs with the default 16 MiB range.
        values["range_size"] = values["object_size"]
    cfg = BenchConfig(**values)
    validate_config(cfg)
    return cfg


def validate_config(cfg: BenchConfig) -> None:
    bad = [m for m in cfg.modes if m not in MODES]
    if bad or not cfg.modes:
        raise ValueError(f"modes must be a non-empty subset of {MODES}, got {cfg.modes}")
    bad = [t for t in cfg.topologies if t not in TOPOLOGIES]
    if bad or not cfg.topologies:
        raise ValueError(f"topologies must be a non-empty subset of {TOPOLOGIES}, got {cfg.topologies}")
    if cfg.read_buffer not in READ_BUFFERS:
        raise ValueError(f"read_buffer must be one of {READ_BUFFERS}, got {cfg.read_buffer}")
    for name in ("workers", "concurrency", "rounds", "ranges_per_op", "object_size", "range_size", "append_size"):
        if getattr(cfg, name) < 1:
            raise ValueError(f"{name} must be >= 1, got {getattr(cfg, name)}")
    if cfg.num_objects < 0:
        raise ValueError("num_objects must be >= 0")
    if cfg.duration_s <= 0 or cfg.warmup_s < 0:
        raise ValueError("duration_s must be > 0 and warmup_s >= 0")
    if cfg.range_size > cfg.object_size:
        raise ValueError(f"range_size ({cfg.range_size}) > object_size ({cfg.object_size})")
    if not cfg.bucket:
        raise ValueError("bucket must be set")
    if any(m != "gapic" for m in cfg.modes) and sys.platform == "win32":
        raise ValueError("uds-* modes are not supported on Windows")


def mode_topology_matrix(cfg: BenchConfig) -> List[Tuple[str, str]]:
    """gapic runs once (topology n/a); uds-* modes run once per topology."""
    out: List[Tuple[str, str]] = []
    for mode in cfg.modes:
        if mode == "gapic":
            out.append((mode, "n/a"))
        else:
            out.extend((mode, topo) for topo in cfg.topologies)
    return out


def matrix_id(mode: str, topology: str) -> str:
    return mode if mode == "gapic" else f"{mode}-{topology}"


def new_run_id(workload: str) -> str:
    return f"{workload}-{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"


# --------------------------------------------------------------------------
# Per-process mode selection (called in spawned children before any import
# of google.cloud.storage).
# --------------------------------------------------------------------------


def apply_mode_env(mode: str, topology: str) -> None:
    """Sets/clears the UDS selection env vars for ``mode`` in this process."""
    for key in (ENV_FORCE, ENV_UDS, ENV_UDS_MODE, ENV_UDS_SHM):
        os.environ.pop(key, None)
    # Spawned children inherit the parent's sys.argv / -X options; the mode is
    # controlled exclusively via env vars below.
    sys.argv = [a for a in sys.argv if a != FORCE_FLAG]
    xoptions = getattr(sys, "_xoptions", None)
    if isinstance(xoptions, dict):
        xoptions.pop(FORCE_XOPTION, None)
    if mode == "gapic":
        os.environ[ENV_UDS] = "off"
        return
    if mode not in MODES:
        raise ValueError(f"unknown mode {mode!r}")
    os.environ[ENV_FORCE] = "1"  # fail loudly; never silently measure GAPIC
    os.environ[ENV_UDS_MODE] = topology
    if mode == "uds-inline":
        os.environ[ENV_UDS_SHM] = "off"


def apply_cpu_affinity() -> None:
    """Mirrors the sibling harness: keep workers off NIC IRQ CPUs (best effort)."""
    if os.environ.get(ENV_IRQ_AFFINITY, "1").strip().lower() in ("0", "false", "off", "no"):
        return
    try:
        from tests.perf.microbenchmarks._utils import get_irq_affinity

        irq_cpus = get_irq_affinity()
        if irq_cpus:
            allowed = {i for i in range(os.cpu_count() or 1) if i not in irq_cpus}
            if allowed:
                os.sched_setaffinity(0, allowed)
    except Exception:  # noqa: BLE001 - optional optimisation only
        pass


async def wait_for_start(start_evt: Any, timeout: float) -> None:
    loop = asyncio.get_running_loop()
    if not await loop.run_in_executor(None, start_evt.wait, timeout):
        raise TimeoutError(f"start signal not received within {timeout}s")


def make_grpc_client() -> Any:
    from google.cloud.storage.asyncio.async_grpc_client import AsyncGrpcClient

    # gRPC CloudPath only: DirectPath must never be attempted in these benchmarks.
    return AsyncGrpcClient(attempt_direct_path=False)


# --------------------------------------------------------------------------
# Resource sampling (Python workers vs gcs-core-server daemons)
# --------------------------------------------------------------------------


def find_daemon_pids() -> set:
    """PIDs of this user's ``gcs-core-server`` processes (+ UDS_BENCH_DAEMON_PIDS)."""
    uid = os.getuid()
    pids = set()
    for proc in psutil.process_iter(["pid", "name", "uids", "cmdline"]):
        try:
            info = proc.info
            uids = info.get("uids")
            if uids is not None and uids.real != uid:
                continue
            names = {info.get("name") or ""}
            cmdline = info.get("cmdline") or []
            if cmdline:
                names.add(os.path.basename(cmdline[0]))
            if DAEMON_PROCESS_NAME in names:
                pids.add(info["pid"])
        except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
            continue
    for item in os.environ.get(ENV_DAEMON_PIDS, "").split(","):
        if item.strip().isdigit() and psutil.pid_exists(int(item)):
            pids.add(int(item))
    return pids


def kill_processes(pids: Iterable[int], timeout: float = 5.0) -> List[int]:
    procs = []
    for pid in pids:
        try:
            p = psutil.Process(pid)
            p.terminate()
            procs.append(p)
        except psutil.Error:
            continue
    _, alive = psutil.wait_procs(procs, timeout=timeout)
    for p in alive:
        try:
            p.kill()
        except psutil.Error:
            pass
    return [p.pid for p in procs]


def read_pss_bytes(pid: int) -> Optional[int]:
    """Proportional set size from /proc/<pid>/smaps_rollup (shared pages split)."""
    try:
        with open(f"/proc/{pid}/smaps_rollup", "r") as f:
            for line in f:
                if line.startswith("Pss:"):
                    return int(line.split()[1]) * 1024
    except (OSError, ValueError, IndexError):
        pass
    try:
        return psutil.Process(pid).memory_full_info().pss
    except (psutil.Error, AttributeError):
        return None


def cgroup_dir() -> Optional[str]:
    """cgroup v2 directory of this process, if any."""
    try:
        with open("/proc/self/cgroup", "r") as f:
            for line in f:
                if line.startswith("0::"):
                    path = os.path.join("/sys/fs/cgroup", line.strip()[3:].lstrip("/"))
                    return path if os.path.isdir(path) else None
    except OSError:
        pass
    return None


def _read_int_file(path: Optional[str]) -> Optional[int]:
    if not path:
        return None
    try:
        with open(path, "r") as f:
            return int(f.read().strip())
    except (OSError, ValueError):
        return None


class ResourceSampler:
    """Samples CPU seconds and memory of worker processes and UDS daemons.

    CPU: user+system seconds consumed between ``begin()`` and ``end()``.
    Memory: peak over 1 s samples of the *sum* of PSS (memfd/shm pages shared
    between a worker and the daemon are counted once in total) and of RSS, plus
    cgroup v2 ``memory.current`` (sampled peak) and ``memory.peak`` (lifetime).
    """

    def __init__(self, worker_pids: Iterable[int], track_daemons: bool, interval: float = 1.0):
        self._workers: Dict[int, psutil.Process] = {}
        for pid in worker_pids:
            try:
                self._workers[pid] = psutil.Process(pid)
            except psutil.Error:
                pass
        self._track_daemons = track_daemons
        self._daemons: Dict[int, psutil.Process] = {}
        self._interval = interval
        self._cpu0: Dict[int, float] = {}
        self._last_cpu: Dict[int, float] = {}
        self._peak: Dict[str, int] = {}
        self._samples = 0
        self._cg = cgroup_dir()
        self._cg_peak: Optional[int] = None
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()

    def _refresh_daemons(self) -> None:
        if not self._track_daemons:
            return
        for pid in find_daemon_pids():
            if pid not in self._daemons:
                try:
                    self._daemons[pid] = psutil.Process(pid)
                except psutil.Error:
                    pass

    def _snapshot_cpu(self) -> None:
        for procs in (self._workers, self._daemons):
            for pid, proc in list(procs.items()):
                try:
                    t = proc.cpu_times()
                    self._last_cpu[pid] = t.user + t.system
                except psutil.Error:
                    pass

    def _bump(self, key: str, value: Optional[int]) -> None:
        if value is not None and value > self._peak.get(key, 0):
            self._peak[key] = value

    def _sample_memory(self) -> None:
        totals = {"python_pss": 0, "daemon_pss": 0, "python_rss": 0, "daemon_rss": 0}
        for group, procs in (("python", self._workers), ("daemon", self._daemons)):
            for pid, proc in list(procs.items()):
                try:
                    rss = proc.memory_info().rss
                except psutil.Error:
                    continue
                pss = read_pss_bytes(pid)
                totals[f"{group}_rss"] += rss
                totals[f"{group}_pss"] += pss if pss is not None else rss
                self._bump(f"{group}_single_rss_max", rss)
        for key, value in totals.items():
            self._bump(key, value)
        self._bump("total_pss", totals["python_pss"] + totals["daemon_pss"])
        self._bump("total_rss", totals["python_rss"] + totals["daemon_rss"])
        if self._cg:
            self._bump("cgroup_current", _read_int_file(os.path.join(self._cg, "memory.current")))
        self._samples += 1

    def _tick(self) -> None:
        with self._lock:
            self._refresh_daemons()
            self._snapshot_cpu()
            self._sample_memory()

    def _loop(self) -> None:
        while not self._stop.wait(self._interval):
            try:
                self._tick()
            except Exception:  # noqa: BLE001 - sampling must never kill a run
                pass

    def begin(self) -> None:
        with self._lock:
            self._refresh_daemons()
            self._snapshot_cpu()
            self._cpu0 = dict(self._last_cpu)
            self._sample_memory()
        self._thread = threading.Thread(target=self._loop, name="uds-bench-sampler", daemon=True)
        self._thread.start()

    def end(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join()
        self._tick()
        if self._cg:
            self._cg_peak = _read_int_file(os.path.join(self._cg, "memory.peak"))

    def metrics(self) -> Dict[str, Any]:
        def cpu(procs: Dict[int, psutil.Process]) -> float:
            return sum(
                max(0.0, self._last_cpu[pid] - self._cpu0.get(pid, 0.0))
                for pid in procs
                if pid in self._last_cpu
            )

        return {
            "python_cpu_s": cpu(self._workers),
            "daemon_cpu_s": cpu(self._daemons) if self._track_daemons else None,
            "python_worker_pids": sorted(self._workers),
            "daemon_pids": sorted(self._daemons),
            "peak_pss_bytes": {
                "python": self._peak.get("python_pss"),
                "daemon": self._peak.get("daemon_pss", 0) if self._track_daemons else None,
                "total": self._peak.get("total_pss"),
            },
            "peak_rss_bytes": {
                "python": self._peak.get("python_rss"),
                "daemon": self._peak.get("daemon_rss", 0) if self._track_daemons else None,
                "total": self._peak.get("total_rss"),
                "max_single_python": self._peak.get("python_single_rss_max"),
                "max_single_daemon": self._peak.get("daemon_single_rss_max"),
            },
            "cgroup": {
                "path": self._cg,
                "memory_current_peak_bytes": self._peak.get("cgroup_current"),
                # memory.peak is the cgroup *lifetime* high-water mark (includes
                # everything before this run); use the sampled current peak for
                # per-run comparisons.
                "memory_peak_lifetime_bytes": self._cg_peak,
            },
            "memory_samples": self._samples,
        }


# --------------------------------------------------------------------------
# Process orchestration
# --------------------------------------------------------------------------


@dataclasses.dataclass
class RunOutcome:
    payloads: List[Dict[str, Any]]
    resources: Dict[str, Any]
    window_s: float
    spawned_daemons: List[int]
    leftover_objects: List[str]


def run_workers(
    cfg: BenchConfig,
    mode: str,
    topology: str,
    target: Callable[..., None],
    extra_args: Callable[[int], tuple],
) -> RunOutcome:
    """Spawns ``cfg.workers`` processes running ``target`` and measures them.

    ``target(idx, cfg_dict, mode, topology, chan, start_evt, window, *extra)``
    must put ``("ready", idx, pid)`` once set up, wait for ``start_evt``, run
    until ``window[1]`` (measuring ops in ``[window[0], window[1]]``; both are
    ``time.monotonic()`` values, system-wide on Linux) and finally put
    ``("result", idx, payload)`` or ``("error", idx, {"traceback", "leftover_objects"})``.
    """
    ctx = multiprocessing.get_context("spawn")
    chan = ctx.Queue()
    start_evt = ctx.Event()
    window = ctx.Array("d", [0.0, 0.0], lock=False)
    cfg_dict = dataclasses.asdict(cfg)
    n = cfg.workers
    daemons_before = find_daemon_pids() if mode != "gapic" else set()
    procs = [
        ctx.Process(
            target=target,
            args=(i, cfg_dict, mode, topology, chan, start_evt, window, *extra_args(i)),
            name=f"uds-bench-worker-{i}",
        )
        for i in range(n)
    ]
    ready: Dict[int, int] = {}
    results: Dict[int, Dict[str, Any]] = {}
    errors: Dict[int, str] = {}
    leftovers: List[str] = []
    spawned: List[int] = []
    sampler: Optional[ResourceSampler] = None

    def handle(msg: tuple) -> None:
        kind, idx, data = msg
        if kind == "ready":
            ready[idx] = data
        elif kind == "result":
            results[idx] = data
            leftovers.extend(data.get("leftover_objects", []))
        elif kind == "error":
            errors[idx] = data.get("traceback", repr(data))
            leftovers.extend(data.get("leftover_objects", []))

    def pump(until: float, done: Callable[[], bool], stop_on_error: bool) -> None:
        while not done() and not (stop_on_error and errors):
            remaining = until - time.monotonic()
            if remaining <= 0:
                return
            try:
                handle(chan.get(timeout=min(1.0, remaining)))
                continue
            except queue.Empty:
                pass
            for i, p in enumerate(procs):
                if p.exitcode is not None and i not in results and i not in errors:
                    try:  # the process may have reported just before exiting
                        while True:
                            handle(chan.get(timeout=0.5))
                    except queue.Empty:
                        pass
                    if i not in results and i not in errors:
                        errors[i] = f"worker {i} exited with code {p.exitcode} without reporting"

    def fail(message: str) -> BenchmarkError:
        details = "\n".join(f"--- worker {i} ---\n{tb}" for i, tb in sorted(errors.items())[:5])
        return BenchmarkError(f"[{matrix_id(mode, topology)}] {message}\n{details}", leftovers)

    try:
        for p in procs:
            p.start()
        pump(time.monotonic() + cfg.setup_timeout_s, lambda: len(ready) == n, True)
        if errors:
            raise fail(f"{len(errors)} worker(s) failed during setup")
        if len(ready) != n:
            raise fail(f"only {len(ready)}/{n} workers ready after {cfg.setup_timeout_s}s")

        now = time.monotonic()
        window[0] = now + cfg.warmup_s
        window[1] = window[0] + cfg.duration_s
        sampler = ResourceSampler(ready.values(), track_daemons=mode != "gapic")
        start_evt.set()
        pump(window[0], lambda: False, True)
        sampler.begin()
        pump(window[1], lambda: False, True)
        sampler.end()
        if errors:
            raise fail(f"{len(errors)} worker(s) failed during the measured window")

        grace = max(120.0, cfg.setup_timeout_s)
        pump(window[1] + grace, lambda: len(results) + len(errors) == n, False)
        if errors:
            raise fail(f"{len(errors)} worker(s) failed")
        if len(results) != n:
            raise fail(f"only {len(results)}/{n} workers reported within {grace}s after the window")
        for p in procs:
            p.join(timeout=30)
    finally:
        start_evt.set()
        for p in procs:
            if p.is_alive():
                p.terminate()
                p.join(5)
                if p.is_alive():
                    p.kill()
                    p.join(5)
        chan.close()
        if mode != "gapic" and cfg.kill_spawned_daemons:
            spawned = kill_processes(find_daemon_pids() - daemons_before)

    return RunOutcome(
        payloads=[results[i] for i in range(n)],
        resources=sampler.metrics() if sampler else {},
        window_s=cfg.duration_s,
        spawned_daemons=spawned,
        leftover_objects=leftovers,
    )


# --------------------------------------------------------------------------
# Statistics & reporting
# --------------------------------------------------------------------------


def percentile(sorted_values: Sequence[float], q: float) -> Optional[float]:
    if not sorted_values:
        return None
    k = (len(sorted_values) - 1) * q
    lo = math.floor(k)
    hi = min(lo + 1, len(sorted_values) - 1)
    return sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * (k - lo)


def latency_summary_ms(values_s: Iterable[float]) -> Dict[str, Any]:
    s = sorted(v * 1000.0 for v in values_s)
    if not s:
        return {"count": 0}
    return {
        "count": len(s),
        "min": s[0],
        "mean": statistics.fmean(s),
        "p50": percentile(s, 0.50),
        "p90": percentile(s, 0.90),
        "p99": percentile(s, 0.99),
        "max": s[-1],
    }


def _per_gib(cpu_s: Optional[float], nbytes: int) -> Optional[float]:
    if cpu_s is None or nbytes <= 0:
        return None
    return cpu_s / (nbytes / _GiB)


def summarize_run(
    workload: str,
    cfg: BenchConfig,
    mode: str,
    topology: str,
    round_idx: int,
    outcome: RunOutcome,
    variant: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Aggregates worker payloads (``*latencies_s`` lists, bytes, ops)."""
    payloads = outcome.payloads
    nbytes = sum(p["bytes"] for p in payloads)
    ops = sum(p["ops"] for p in payloads)
    lat_keys = sorted({k for p in payloads for k in p if k.endswith("latencies_s")})
    latencies = {
        ("latency_ms" if k == "latencies_s" else k.replace("latencies_s", "latency_ms")): latency_summary_ms(
            v for p in payloads for v in p.get(k, [])
        )
        for k in lat_keys
    }
    res = outcome.resources
    window = outcome.window_s
    py_cpu = res.get("python_cpu_s")
    dm_cpu = res.get("daemon_cpu_s")
    label = matrix_id(mode, topology)
    if variant:
        label += "/" + ",".join(f"{k}={v}" for k, v in variant.items())
    warnings = []
    if mode != "gapic" and not res.get("daemon_pids"):
        warnings.append(f"no '{DAEMON_PROCESS_NAME}' process observed during a {mode} run")
    return {
        "workload": workload,
        "label": label,
        "mode": mode,
        "topology": topology,
        "variant": variant or {},
        "round": round_idx,
        "workers": cfg.workers,
        "concurrency": cfg.concurrency,
        "duration_s": window,
        "warmup_s": cfg.warmup_s,
        "ops": ops,
        "unmeasured_ops": sum(p.get("unmeasured_ops", 0) for p in payloads),
        "bytes": nbytes,
        "ops_per_s": ops / window,
        "throughput_MBps": nbytes / 1e6 / window,
        "throughput_MiBps": nbytes / _MiB / window,
        **latencies,
        "python_cpu_s": py_cpu,
        "daemon_cpu_s": dm_cpu,
        "python_cpu_s_per_GiB": _per_gib(py_cpu, nbytes),
        "daemon_cpu_s_per_GiB": _per_gib(dm_cpu, nbytes),
        "total_cpu_s_per_GiB": _per_gib((py_cpu or 0.0) + (dm_cpu or 0.0), nbytes),
        "resources": res,
        "spawned_daemons_killed": outcome.spawned_daemons,
        "warnings": warnings,
    }


def _median(values: Iterable[Optional[float]]) -> Optional[float]:
    vals = [v for v in values if v is not None]
    return statistics.median(vals) if vals else None


def summarize_rounds(runs: List[Dict[str, Any]]) -> Dict[str, Any]:
    groups: Dict[str, List[Dict[str, Any]]] = {}
    for run in runs:
        groups.setdefault(run["label"], []).append(run)
    summary = {}
    for label, items in groups.items():
        lat = [r.get("latency_ms", {}) for r in items]
        summary[label] = {
            "rounds": len(items),
            "throughput_MBps_median": _median(r["throughput_MBps"] for r in items),
            "throughput_MBps_mean": statistics.fmean(r["throughput_MBps"] for r in items),
            "latency_p50_ms_median": _median(l.get("p50") for l in lat),
            "latency_p90_ms_median": _median(l.get("p90") for l in lat),
            "latency_p99_ms_median": _median(l.get("p99") for l in lat),
            "python_cpu_s_per_GiB_median": _median(r["python_cpu_s_per_GiB"] for r in items),
            "daemon_cpu_s_per_GiB_median": _median(r["daemon_cpu_s_per_GiB"] for r in items),
            "peak_pss_total_bytes_max": max(
                (r["resources"].get("peak_pss_bytes", {}).get("total") or 0) for r in items
            ),
        }
    return summary


class Report:
    """Accumulates runs and rewrites the JSON results file after every run."""

    def __init__(self, cfg: BenchConfig, workload: str, run_id: str):
        out_dir = cfg.output_dir or os.path.join(tempfile.gettempdir(), "uds-bench-results")
        os.makedirs(out_dir, exist_ok=True)
        self.path = os.path.join(out_dir, f"{run_id}.json")
        self.doc: Dict[str, Any] = {
            "workload": workload,
            "run_id": run_id,
            "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "host": socket.gethostname(),
            "cpu_count": os.cpu_count(),
            "python": sys.version,
            "config": dataclasses.asdict(cfg),
            "runs": [],
            "summary": {},
            "cleanup": [],
            "errors": [],
        }
        self.write()

    def add(self, run: Dict[str, Any]) -> None:
        self.doc["runs"].append(run)
        self.doc["summary"] = summarize_rounds(self.doc["runs"])
        self.write()
        lat = run.get("latency_ms", {})
        print(
            f"[{run['workload']}] {run['label']} round {run['round']}: "
            f"{run['throughput_MBps']:.1f} MB/s, {run['ops']} ops, "
            f"p50/p90/p99 = {_fmt(lat.get('p50'))}/{_fmt(lat.get('p90'))}/{_fmt(lat.get('p99'))} ms, "
            f"py CPU {_fmt(run['python_cpu_s_per_GiB'])} s/GiB, "
            f"daemon CPU {_fmt(run['daemon_cpu_s_per_GiB'])} s/GiB",
            flush=True,
        )

    def add_cleanup(self, cleanup: Dict[str, Any]) -> None:
        self.doc["cleanup"].append(cleanup)
        self.write()

    def add_error(self, label: str, error: BaseException) -> None:
        self.doc["errors"].append({"label": label, "error": str(error)})
        self.write()

    def write(self) -> None:
        self.doc["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        tmp = f"{self.path}.tmp"
        with open(tmp, "w") as f:
            json.dump(self.doc, f, indent=2, sort_keys=False, default=str)
        os.replace(tmp, self.path)

    def print_summary(self) -> None:
        print(f"\n{self.doc['workload']} results: {self.path}", flush=True)
        header = f"{'label':<44} {'rnds':>4} {'MB/s':>10} {'p50 ms':>9} {'p90 ms':>9} {'p99 ms':>9} {'pyCPU/GiB':>10} {'dmCPU/GiB':>10} {'peakPSS MiB':>12}"
        print(header)
        print("-" * len(header))
        for label, s in self.doc["summary"].items():
            print(
                f"{label:<44} {s['rounds']:>4} {_fmt(s['throughput_MBps_median']):>10} "
                f"{_fmt(s['latency_p50_ms_median']):>9} {_fmt(s['latency_p90_ms_median']):>9} "
                f"{_fmt(s['latency_p99_ms_median']):>9} {_fmt(s['python_cpu_s_per_GiB_median']):>10} "
                f"{_fmt(s['daemon_cpu_s_per_GiB_median']):>10} {_fmt(s['peak_pss_total_bytes_max'] / _MiB):>12}",
                flush=True,
            )


def _fmt(v: Optional[float]) -> str:
    return "n/a" if v is None else f"{v:.2f}"


# --------------------------------------------------------------------------
# Object setup / cleanup (always via a GAPIC-mode helper process, so cleanup
# works even if the UDS backend is broken).
# --------------------------------------------------------------------------


def _init_gapic_process() -> None:
    apply_mode_env("gapic", "n/a")


def _check_name(name: str) -> None:
    if not name.startswith(OBJECT_PREFIX):
        raise ValueError(f"refusing to touch non-benchmark object {name!r}")


async def _create_object_async(bucket: str, name: str, size: int) -> int:
    from google.cloud.storage.asyncio.async_appendable_object_writer import (
        AsyncAppendableObjectWriter,
    )

    writer = AsyncAppendableObjectWriter(
        make_grpc_client(),
        bucket,
        name,
        writer_options={"FLUSH_INTERVAL_BYTES": _SETUP_FLUSH_INTERVAL_BYTES},
    )
    await writer.open()
    chunk = os.urandom(min(_SETUP_APPEND_SIZE, size))
    written = 0
    while written < size:
        n = min(len(chunk), size - written)
        await writer.append(chunk if n == len(chunk) else chunk[:n])
        written += n
    obj = await writer.close(finalize_on_close=True)
    if getattr(obj, "size", size) != size:
        raise BenchmarkError(f"setup object {name} has size {obj.size}, expected {size}")
    return written


def _create_object_task(args: Tuple[str, str, int]) -> Tuple[str, int]:
    bucket, name, size = args
    _check_name(name)
    return name, asyncio.run(_create_object_async(bucket, name, size))


def create_objects(cfg: BenchConfig, names: Sequence[str], size: int) -> None:
    """Creates ``names`` (finalized appendable objects of ``size``) in parallel."""
    if not names:
        return
    ctx = multiprocessing.get_context("spawn")
    procs = max(1, min(len(names), os.cpu_count() or 1, 16))
    print(f"Creating {len(names)} x {format_size(size)} objects in gs://{cfg.bucket} ...", flush=True)
    t0 = time.monotonic()
    with ctx.Pool(procs, initializer=_init_gapic_process) as pool:
        created = pool.map(_create_object_task, [(cfg.bucket, n, size) for n in names])
    if sum(c[1] for c in created) != size * len(names):
        raise BenchmarkError("setup uploaded an unexpected number of bytes", names)
    print(f"Created {len(names)} objects in {time.monotonic() - t0:.1f}s", flush=True)


async def delete_names_async(client: Any, bucket: str, names: Iterable[str], parallelism: int = 32) -> List[str]:
    """Deletes ``names``; returns those that could not be deleted (NotFound == deleted)."""
    from google.api_core import exceptions as api_exceptions

    sem = asyncio.Semaphore(parallelism)

    async def one(name: str) -> Optional[str]:
        _check_name(name)
        async with sem:
            try:
                await client.delete_object(bucket, name)
            except api_exceptions.NotFound:
                pass
            except Exception:  # noqa: BLE001 - reported to the caller
                return name
        return None

    failed = await asyncio.gather(*(one(n) for n in dict.fromkeys(names)))
    return [n for n in failed if n]


def _delete_task(bucket: str, project: str, names: List[str], sweep_prefix: Optional[str]) -> Dict[str, Any]:
    todo = list(dict.fromkeys(names))
    listing_error = None
    if sweep_prefix:
        _check_name(sweep_prefix)
        try:
            from google.cloud import storage

            client = storage.Client(project=project or None)
            todo.extend(b.name for b in client.list_blobs(bucket, prefix=sweep_prefix))
            todo = list(dict.fromkeys(todo))
        except Exception as e:  # noqa: BLE001 - fall back to the known names
            listing_error = repr(e)

    async def run() -> List[str]:
        return await delete_names_async(make_grpc_client(), bucket, todo)

    failed = asyncio.run(run()) if todo else []
    return {
        "sweep_prefix": sweep_prefix,
        "attempted": len(todo),
        "failed": failed,
        "listing_error": listing_error,
    }


def delete_objects(cfg: BenchConfig, names: Iterable[str], sweep_prefix: Optional[str] = None) -> Dict[str, Any]:
    """Deletes ``names`` plus everything under ``sweep_prefix``. Never raises."""
    names = list(names)
    if not names and not sweep_prefix:
        return {"attempted": 0, "failed": []}
    ctx = multiprocessing.get_context("spawn")
    try:
        with ctx.Pool(1, initializer=_init_gapic_process) as pool:
            result = pool.apply(_delete_task, (cfg.bucket, cfg.project, names, sweep_prefix))
    except Exception as e:  # noqa: BLE001
        result = {"sweep_prefix": sweep_prefix, "attempted": len(names), "failed": names, "error": repr(e)}
    if result.get("failed") or result.get("error"):
        print(f"WARNING: cleanup left objects behind: {result}", file=sys.stderr, flush=True)
    else:
        print(f"Cleanup: deleted {result['attempted']} object(s) (prefix {sweep_prefix})", flush=True)
    return result


def describe_config(cfg: BenchConfig, workload: str) -> str:
    return (
        f"{workload}: gs://{cfg.bucket} ({cfg.bucket_zone}) project={cfg.project} "
        f"runner={cfg.runner_vm} ({cfg.runner_zone}) workers={cfg.workers} "
        f"concurrency={cfg.concurrency} object={format_size(cfg.object_size)} "
        f"duration={cfg.duration_s}s warmup={cfg.warmup_s}s rounds={cfg.rounds} "
        f"modes={cfg.modes} topologies={cfg.topologies} force_core_sdk={cfg.force_core_sdk}"
    )


# --------------------------------------------------------------------------
# W4: BidiReads
# --------------------------------------------------------------------------


class _PreallocBuffer:
    """Copies each chunk into a reused bytearray: one copy into user memory per
    byte (same for every mode) without allocation churn or GIL-heavy BytesIO."""

    def __init__(self, capacity: int):
        self._mv = memoryview(bytearray(capacity))
        self.size = 0

    def reset(self) -> "_PreallocBuffer":
        self.size = 0
        return self

    def write(self, data: Any) -> int:
        src = memoryview(data)
        if src.format != "B" or src.ndim != 1:
            src = src.cast("B")
        end = self.size + src.nbytes
        if end > len(self._mv):
            raise ValueError(f"received {end} bytes for a {len(self._mv)}-byte range")
        self._mv[self.size:end] = src
        self.size = end
        return src.nbytes


class _BytesIOBuffer:
    def __init__(self, capacity: int):
        self._bio = io.BytesIO()

    def reset(self) -> "_BytesIOBuffer":
        self._bio.seek(0)
        self._bio.truncate()
        return self

    def write(self, data: Any) -> int:
        return self._bio.write(data)

    @property
    def size(self) -> int:
        return self._bio.tell()


class _DiscardBuffer:
    """Counts bytes only (no copy); NOTE: flatters zero-copy paths."""

    def __init__(self, capacity: int):
        self.size = 0

    def reset(self) -> "_DiscardBuffer":
        self.size = 0
        return self

    def write(self, data: Any) -> int:
        n = memoryview(data).nbytes
        self.size += n
        return n


_BUFFERS = {"prealloc": _PreallocBuffer, "bytesio": _BytesIOBuffer, "discard": _DiscardBuffer}


async def _w4_reader(mrd: Any, cfg: BenchConfig, warmup_end: float, end: float, rng: random.Random) -> Tuple[List[float], int, int, int]:
    bufs = [_BUFFERS[cfg.read_buffer](cfg.range_size) for _ in range(cfg.ranges_per_op)]
    expected = cfg.range_size * cfg.ranges_per_op
    max_offset = cfg.object_size - cfg.range_size
    latencies: List[float] = []
    nbytes = ops = unmeasured = 0
    while True:
        t0 = time.monotonic()
        if t0 >= end:
            break
        ranges = [(rng.randint(0, max_offset), cfg.range_size, b.reset()) for b in bufs]
        await mrd.download_ranges(ranges)
        t1 = time.monotonic()
        got = sum(b.size for b in bufs)
        if got != expected:
            raise AssertionError(f"download_ranges returned {got} bytes, expected {expected}")
        if t0 >= warmup_end and t1 <= end:
            latencies.append(t1 - t0)
            nbytes += got
            ops += 1
        else:
            unmeasured += 1
    return latencies, nbytes, ops, unmeasured


async def _w4_worker_async(idx: int, cfg: BenchConfig, object_name: str, chan: Any, start_evt: Any, window: Any) -> Dict[str, Any]:
    from google.cloud.storage.asyncio.async_multi_range_downloader import (
        AsyncMultiRangeDownloader,
    )

    client = make_grpc_client()
    mrd = await AsyncMultiRangeDownloader.create_mrd(client, cfg.bucket, object_name)
    try:
        chan.put(("ready", idx, os.getpid()))
        await wait_for_start(start_evt, 2 * cfg.setup_timeout_s)
        warmup_end, end = window[0], window[1]
        seed = (os.getpid() << 16) ^ idx ^ time.time_ns()
        parts = await asyncio.gather(
            *(
                _w4_reader(mrd, cfg, warmup_end, end, random.Random(seed + c))
                for c in range(cfg.concurrency)
            )
        )
    finally:
        await mrd.close()
    return {
        "worker": idx,
        "pid": os.getpid(),
        "object": object_name,
        "latencies_s": [v for p in parts for v in p[0]],
        "bytes": sum(p[1] for p in parts),
        "ops": sum(p[2] for p in parts),
        "unmeasured_ops": sum(p[3] for p in parts),
    }


def _w4_worker(idx: int, cfg_dict: Dict[str, Any], mode: str, topology: str, chan: Any, start_evt: Any, window: Any, object_name: str) -> None:
    apply_mode_env(mode, topology)  # before google.cloud.storage is imported
    apply_cpu_affinity()
    try:
        cfg = BenchConfig(**cfg_dict)
        payload = asyncio.run(_w4_worker_async(idx, cfg, object_name, chan, start_evt, window))
        chan.put(("result", idx, payload))
    except BaseException:  # noqa: BLE001 - report everything to the parent
        chan.put(("error", idx, {"traceback": traceback.format_exc(), "leftover_objects": []}))


def w4_object_names(cfg: BenchConfig, run_id: str) -> List[str]:
    count = cfg.num_objects or cfg.workers
    return [f"{OBJECT_PREFIX}{run_id}-obj-{i:04d}" for i in range(count)]


def run_w4_entry(cfg: BenchConfig, mode: str, topology: str, object_names: Sequence[str], report: Report) -> List[Dict[str, Any]]:
    """Runs every round of one mode/topology matrix entry."""
    runs = []
    for round_idx in range(cfg.rounds):
        try:
            outcome = run_workers(
                cfg,
                mode,
                topology,
                _w4_worker,
                lambda i: (object_names[i % len(object_names)],),
            )
        except BenchmarkError as e:
            report.add_error(f"{matrix_id(mode, topology)} round {round_idx}", e)
            raise
        run = summarize_run("w4", cfg, mode, topology, round_idx, outcome)
        run["range_size"] = cfg.range_size
        run["ranges_per_op"] = cfg.ranges_per_op
        run["object_size"] = cfg.object_size
        run["read_buffer"] = cfg.read_buffer
        report.add(run)
        runs.append(run)
    return runs


def _w4_check(cfg: BenchConfig, runs: List[Dict[str, Any]]) -> None:
    for run in runs:
        assert run["ops"] > 0, (
            f"{run['label']} round {run['round']}: no download_ranges completed inside the "
            f"{cfg.duration_s}s window (increase duration or reduce range/object size)"
        )
        assert run["bytes"] == run["ops"] * cfg.range_size * cfg.ranges_per_op


W4_DESCRIPTION = "Workload 4: N processes x AsyncMultiRangeDownloader random-range BidiReads."

# pytest owns sys.argv, so pytest runs use config.yaml + UDS_BENCH_* env only.
_CFG = load_config(None, "w4")
_MATRIX = mode_topology_matrix(_CFG)


@pytest.fixture(scope="module")
def w4_env():
    run_id = new_run_id("w4")
    report = Report(_CFG, "w4", run_id)
    names = w4_object_names(_CFG, run_id)
    print("\n" + describe_config(_CFG, "w4"), flush=True)
    try:
        create_objects(_CFG, names, _CFG.object_size)
        yield names, report
    finally:
        report.add_cleanup(delete_objects(_CFG, names, sweep_prefix=f"{OBJECT_PREFIX}{run_id}-"))
        report.print_summary()


@pytest.mark.parametrize("mode,topology", _MATRIX, ids=[matrix_id(m, t) for m, t in _MATRIX])
def test_w4_bidi_read(w4_env, mode, topology):
    names, report = w4_env
    runs = run_w4_entry(_CFG, mode, topology, names, report)
    _w4_check(_CFG, runs)


def main(argv: Optional[Sequence[str]] = None) -> int:
    cfg = load_config(sys.argv[1:] if argv is None else argv, "w4", W4_DESCRIPTION)
    run_id = new_run_id("w4")
    report = Report(cfg, "w4", run_id)
    names = w4_object_names(cfg, run_id)
    print(describe_config(cfg, "w4"), flush=True)
    print(f"Results: {report.path}", flush=True)
    try:
        create_objects(cfg, names, cfg.object_size)
        for mode, topology in mode_topology_matrix(cfg):
            _w4_check(cfg, run_w4_entry(cfg, mode, topology, names, report))
    finally:
        report.add_cleanup(delete_objects(cfg, names, sweep_prefix=f"{OBJECT_PREFIX}{run_id}-"))
        report.print_summary()
    return 0


if __name__ == "__main__":
    sys.exit(main())
