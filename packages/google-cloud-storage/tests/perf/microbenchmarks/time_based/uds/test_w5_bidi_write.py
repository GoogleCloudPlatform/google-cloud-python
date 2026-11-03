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
"""Workload 5 (W5): time-based BidiWrites via ``AsyncAppendableObjectWriter``.

N worker processes (multiprocessing ``spawn``) each loop
``open() -> append(append_size) ... -> close(finalize_on_close=True)`` for
objects of ``object_size`` during ``duration_s`` seconds after a
``warmup_s`` warmup, for every mode x topology x ``FLUSH_INTERVAL_BYTES``
variant x round in ``config.yaml`` (overridable by ``UDS_BENCH_*`` env vars
and, when run as a script, by CLI args). Every object written is named
``uds-bench-<run id>-...`` and deleted by its worker after the measured window;
a GAPIC-mode prefix sweep afterwards deletes anything left behind.

Uses the shared harness in ``test_w4_bidi_read.py`` (config, orchestration,
resource sampling, JSON reporting, cleanup).

Examples (from ``packages/google-cloud-storage``)::

    UDS_BENCH_WORKERS=2 UDS_BENCH_DURATION_S=5 UDS_BENCH_WARMUP_S=1 \\
    UDS_BENCH_OBJECT_SIZE=8MiB UDS_BENCH_ROUNDS=1 UDS_BENCH_FLUSH_INTERVAL_BYTES=2MiB \\
        pytest -s tests/perf/microbenchmarks/time_based/uds/test_w5_bidi_write.py \\
        --force-use-core-sdk

    python tests/perf/microbenchmarks/time_based/uds/test_w5_bidi_write.py \\
        --workers 2 --duration 5 --warmup 1 --rounds 1 --object-size 8MiB \\
        --append-size 2MiB --flush-interval-bytes 2MiB,8MiB \\
        --bucket chandrasiri-gcsfs-zb --force-use-core-sdk
"""

from __future__ import annotations

import asyncio
import os
import sys
import time
import traceback
from typing import Any, Dict, List, Optional, Sequence, Tuple

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import test_w4_bidi_read as harness  # noqa: E402  (shared harness; no GCS imports at load)

# AsyncAppendableObjectWriter requires FLUSH_INTERVAL_BYTES to be a multiple of 2 MiB.
_WRITER_CHUNK_BYTES = 2 * 1024 * 1024


def w5_matrix(cfg: harness.BenchConfig) -> List[Tuple[str, str, int]]:
    for fi in cfg.flush_interval_bytes:
        if fi < _WRITER_CHUNK_BYTES or fi % _WRITER_CHUNK_BYTES:
            raise ValueError(f"flush_interval_bytes must be a positive multiple of 2 MiB, got {fi}")
    if not cfg.flush_interval_bytes:
        raise ValueError("flush_interval_bytes must not be empty")
    return [
        (mode, topology, fi)
        for mode, topology in harness.mode_topology_matrix(cfg)
        for fi in cfg.flush_interval_bytes
    ]


def w5_id(mode: str, topology: str, flush_interval: int) -> str:
    return f"{harness.matrix_id(mode, topology)}-flush{harness.format_size(flush_interval)}"


def w5_prefix(run_id: str, mode: str, topology: str, flush_interval: int, round_idx: int) -> str:
    return (
        f"{harness.OBJECT_PREFIX}{run_id}-{harness.matrix_id(mode, topology)}-"
        f"f{harness.format_size(flush_interval)}-r{round_idx}-"
    )


async def _w5_worker_async(
    idx: int,
    cfg: harness.BenchConfig,
    flush_interval: int,
    name_prefix: str,
    chan: Any,
    start_evt: Any,
    window: Any,
    state: Dict[str, List[str]],
) -> Dict[str, Any]:
    from google.cloud.storage.asyncio.async_appendable_object_writer import (
        AsyncAppendableObjectWriter,
    )

    client = harness.make_grpc_client()
    # One random chunk reused for every append (keeps per-worker memory at
    # ~append_size instead of object_size); the tail covers non-multiples.
    chunk = os.urandom(min(cfg.append_size, cfg.object_size))
    tail_len = cfg.object_size % len(chunk)
    tail = chunk[:tail_len] if tail_len else b""
    created = state["created"]
    op_lat: List[float] = []
    open_lat: List[float] = []
    append_lat: List[float] = []
    finalize_lat: List[float] = []
    nbytes = ops = unmeasured = 0
    try:
        chan.put(("ready", idx, os.getpid()))
        await harness.wait_for_start(start_evt, 2 * cfg.setup_timeout_s)
        warmup_end, end = window[0], window[1]
        seq = 0
        while True:
            t0 = time.monotonic()
            if t0 >= end:
                break
            name = f"{name_prefix}w{idx:03d}-{seq:06d}"
            seq += 1
            created.append(name)  # record before open so cleanup covers partial objects
            writer = AsyncAppendableObjectWriter(
                client,
                cfg.bucket,
                name,
                writer_options={"FLUSH_INTERVAL_BYTES": flush_interval},
            )
            await writer.open()
            t_open = time.monotonic()
            appends: List[float] = []
            remaining = cfg.object_size
            while remaining > 0:
                data = chunk if remaining >= len(chunk) else tail
                ta = time.monotonic()
                await writer.append(data)
                appends.append(time.monotonic() - ta)
                remaining -= len(data)
            t_fin = time.monotonic()
            obj = await writer.close(finalize_on_close=True)
            t1 = time.monotonic()
            size = getattr(obj, "size", None)
            if size is not None and size != cfg.object_size:
                raise AssertionError(f"{name}: finalized size {size} != {cfg.object_size}")
            if t0 >= warmup_end and t1 <= end:
                op_lat.append(t1 - t0)
                open_lat.append(t_open - t0)
                append_lat.extend(appends)
                finalize_lat.append(t1 - t_fin)
                nbytes += cfg.object_size
                ops += 1
            else:
                unmeasured += 1
    finally:
        # Outside the measured window (the sampler stops at window end).
        state["leftover"] = list(created)
        if created:
            state["leftover"] = await harness.delete_names_async(client, cfg.bucket, created)
    return {
        "worker": idx,
        "pid": os.getpid(),
        "latencies_s": op_lat,
        "open_latencies_s": open_lat,
        "append_latencies_s": append_lat,
        "finalize_latencies_s": finalize_lat,
        "bytes": nbytes,
        "ops": ops,
        "unmeasured_ops": unmeasured,
        "objects_created": len(created),
        "leftover_objects": state["leftover"],
    }


def _w5_worker(
    idx: int,
    cfg_dict: Dict[str, Any],
    mode: str,
    topology: str,
    chan: Any,
    start_evt: Any,
    window: Any,
    flush_interval: int,
    name_prefix: str,
) -> None:
    harness.apply_mode_env(mode, topology)  # before google.cloud.storage is imported
    harness.apply_cpu_affinity()
    state: Dict[str, List[str]] = {"created": [], "leftover": []}
    try:
        cfg = harness.BenchConfig(**cfg_dict)
        payload = asyncio.run(
            _w5_worker_async(idx, cfg, flush_interval, name_prefix, chan, start_evt, window, state)
        )
        chan.put(("result", idx, payload))
    except BaseException:  # noqa: BLE001 - report everything to the parent
        leftover = state["leftover"] or state["created"]
        chan.put(("error", idx, {"traceback": traceback.format_exc(), "leftover_objects": leftover}))


def run_w5_entry(
    cfg: harness.BenchConfig,
    run_id: str,
    mode: str,
    topology: str,
    flush_interval: int,
    report: harness.Report,
) -> List[Dict[str, Any]]:
    """Runs every round of one mode/topology/flush-interval matrix entry."""
    runs = []
    for round_idx in range(cfg.rounds):
        prefix = w5_prefix(run_id, mode, topology, flush_interval, round_idx)
        leftovers: List[str] = []
        try:
            outcome = harness.run_workers(
                cfg, mode, topology, _w5_worker, lambda i: (flush_interval, prefix)
            )
            leftovers = outcome.leftover_objects
        except harness.BenchmarkError as e:
            leftovers = e.leftover_objects
            report.add_error(f"{w5_id(mode, topology, flush_interval)} round {round_idx}", e)
            raise
        finally:
            report.add_cleanup(harness.delete_objects(cfg, leftovers, sweep_prefix=prefix))
        run = harness.summarize_run(
            "w5",
            cfg,
            mode,
            topology,
            round_idx,
            outcome,
            variant={"flush_interval": harness.format_size(flush_interval)},
        )
        run["flush_interval_bytes"] = flush_interval
        run["append_size"] = cfg.append_size
        run["object_size"] = cfg.object_size
        run["objects_created"] = sum(p["objects_created"] for p in outcome.payloads)
        report.add(run)
        runs.append(run)
    return runs


def _w5_check(cfg: harness.BenchConfig, runs: List[Dict[str, Any]]) -> None:
    for run in runs:
        assert run["ops"] > 0, (
            f"{run['label']} round {run['round']}: no open->append->finalize cycle completed "
            f"inside the {cfg.duration_s}s window (increase duration or reduce object size)"
        )
        assert run["bytes"] == run["ops"] * cfg.object_size


W5_DESCRIPTION = "Workload 5: N processes x AsyncAppendableObjectWriter open->append->finalize BidiWrites."

# pytest owns sys.argv, so pytest runs use config.yaml + UDS_BENCH_* env only.
_CFG = harness.load_config(None, "w5")
_MATRIX = w5_matrix(_CFG)


@pytest.fixture(scope="module")
def w5_env():
    run_id = harness.new_run_id("w5")
    report = harness.Report(_CFG, "w5", run_id)
    print("\n" + harness.describe_config(_CFG, "w5"), flush=True)
    try:
        yield run_id, report
    finally:
        report.add_cleanup(
            harness.delete_objects(_CFG, [], sweep_prefix=f"{harness.OBJECT_PREFIX}{run_id}-")
        )
        report.print_summary()


@pytest.mark.parametrize(
    "mode,topology,flush_interval", _MATRIX, ids=[w5_id(*entry) for entry in _MATRIX]
)
def test_w5_bidi_write(w5_env, mode, topology, flush_interval):
    run_id, report = w5_env
    runs = run_w5_entry(_CFG, run_id, mode, topology, flush_interval, report)
    _w5_check(_CFG, runs)


def main(argv: Optional[Sequence[str]] = None) -> int:
    cfg = harness.load_config(sys.argv[1:] if argv is None else argv, "w5", W5_DESCRIPTION)
    matrix = w5_matrix(cfg)
    run_id = harness.new_run_id("w5")
    report = harness.Report(cfg, "w5", run_id)
    print(harness.describe_config(cfg, "w5"), flush=True)
    print(f"Results: {report.path}", flush=True)
    try:
        for mode, topology, flush_interval in matrix:
            _w5_check(cfg, run_w5_entry(cfg, run_id, mode, topology, flush_interval, report))
    finally:
        report.add_cleanup(
            harness.delete_objects(cfg, [], sweep_prefix=f"{harness.OBJECT_PREFIX}{run_id}-")
        )
        report.print_summary()
    return 0


if __name__ == "__main__":
    sys.exit(main())
