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

from __future__ import annotations

import gc
import glob
import os
import tempfile
import time
from dataclasses import dataclass
from typing import Any, Iterable, Sequence

from google.cloud.bigtable.data import (
    AddToCell,
    DeleteAllFromFamily,
    DeleteAllFromRow,
    DeleteRangeFromColumn,
    SetCell,
)
from google.cloud.bigtable.data._accelerator import _daemon
from google.cloud.bigtable.data.row import Row

# Millisecond timestamp granularity (Bigtable default).
MS = 1000

# Column families created by the shared system-test conftest.
TEST_FAMILY = "test-family"
TEST_FAMILY_2 = "test-family-2"
TEST_AGGREGATE_FAMILY = "test-aggregate-family"
_AGGREGATE_VALUE_BYTES = 8

# Guard window (in ops) to avoid opposite-kind mutations on the same key within
# a retry straggler window.
DELETE_AFTER_WRITE_GUARD_OPS = 512

# Env var used by tests / runners to override the binary location.
BIN_ENV_VAR = "BIGTABLE_ACCELERATOR_BIN"

Expected = tuple  # (family: str, qualifier: bytes, timestamp_micros: int, value: bytes)


class ExpectedState:
    def __init__(self) -> None:
        self._rows: dict[bytes, dict[tuple[str, bytes], dict[int, Any]]] = {}

    def set_cell(
        self, row_key: bytes, family: str, qualifier: bytes, value: bytes, ts: int
    ) -> SetCell:
        if ts % MS != 0:
            raise ValueError(
                "timestamps must be millisecond-granular (multiple of 1000)"
            )
        col = self._rows.setdefault(row_key, {}).setdefault((family, qualifier), {})
        col[ts] = value
        return SetCell(family, qualifier, value, timestamp_micros=ts)

    def add_to_cell(
        self, row_key: bytes, qualifier: bytes, delta: int, ts: int
    ) -> AddToCell:
        if ts % MS != 0:
            raise ValueError(
                "timestamps must be millisecond-granular (multiple of 1000)"
            )
        col = self._rows.setdefault(row_key, {}).setdefault(
            (TEST_AGGREGATE_FAMILY, qualifier), {}
        )
        col[ts] = int(col.get(ts, 0)) + delta
        return AddToCell(TEST_AGGREGATE_FAMILY, qualifier, delta, timestamp_micros=ts)

    def delete_range_from_column(
        self,
        row_key: bytes,
        family: str,
        qualifier: bytes,
        start: int | None = None,
        end: int | None = None,
    ) -> DeleteRangeFromColumn:
        col = self._rows.get(row_key, {}).get((family, qualifier))
        if col is not None:
            lo = 0 if start is None else start
            for ts in list(col):
                if ts >= lo and (end is None or ts < end):
                    del col[ts]
            if not col:
                self._rows[row_key].pop((family, qualifier), None)
                if not self._rows[row_key]:
                    self._rows.pop(row_key, None)
        return DeleteRangeFromColumn(family, qualifier, start, end)

    def delete_from_family(self, row_key: bytes, family: str) -> DeleteAllFromFamily:
        row = self._rows.get(row_key)
        if row is not None:
            for key in [k for k in row if k[0] == family]:
                del row[key]
            if not row:
                self._rows.pop(row_key, None)
        return DeleteAllFromFamily(family)

    def delete_from_row(self, row_key: bytes) -> DeleteAllFromRow:
        self._rows.pop(row_key, None)
        return DeleteAllFromRow()

    def expected_cells(self, row_key: bytes) -> list[Expected]:
        row = self._rows.get(row_key, {})
        out: list[Expected] = []
        for family, qualifier in sorted(row, key=lambda k: (k[0], k[1])):
            for ts in sorted(row[(family, qualifier)], reverse=True):
                value = row[(family, qualifier)][ts]
                if family == TEST_AGGREGATE_FAMILY:
                    value = int(value).to_bytes(
                        _AGGREGATE_VALUE_BYTES, "big", signed=True
                    )
                out.append((family, qualifier, ts, value))
        return out

    def row_is_empty(self, row_key: bytes) -> bool:
        return not self._rows.get(row_key)

    def keys(self) -> Iterable[bytes]:
        return list(self._rows)


def normalize_row(row: Row | None) -> list[Expected]:
    if row is None:
        return []
    return [
        (cell.family, cell.qualifier, cell.timestamp_micros, cell.value)
        for cell in row.cells
    ]


def _fmt(cells: Sequence[Expected]) -> str:
    return (
        "\n".join(f"  {fam}:{qual!r}@{ts} = {val!r}" for (fam, qual, ts, val) in cells)
        or "  <empty>"
    )


def assert_rows_equivalent(
    label_a: str,
    cells_a: Sequence[Expected],
    label_b: str,
    cells_b: Sequence[Expected],
) -> None:
    if list(cells_a) != list(cells_b):
        raise AssertionError(
            f"row mismatch between {label_a} and {label_b}:\n"
            f"{label_a}:\n{_fmt(cells_a)}\n{label_b}:\n{_fmt(cells_b)}"
        )


def resolve_binary() -> str | None:
    override = os.environ.get(BIN_ENV_VAR)
    if override:
        return override if os.path.isfile(override) else None
    try:
        return _daemon._resolve_binary_path()
    except FileNotFoundError:
        return None


def require_binary_or_skip() -> str:
    import pytest

    path = resolve_binary()
    if path is None:
        pytest.skip(
            "No accelerator daemon binary available "
            f"(set {BIN_ENV_VAR} or install a wheel that bundles it)."
        )
    return path


def require_real_bigtable_or_skip() -> None:
    import pytest
    from google.cloud.environment_vars import BIGTABLE_EMULATOR

    if os.environ.get(BIGTABLE_EMULATOR):
        pytest.skip("accelerator is not supported against the emulator")
    if not (os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("PROJECT_ID")):
        pytest.skip("no GOOGLE_CLOUD_PROJECT set for live accelerator tests")


def accel_tempdirs() -> set[str]:
    return set(glob.glob(os.path.join(tempfile.gettempdir(), "bt-accel-*")))


@dataclass
class LeakSnapshot:
    child_pids: set[int]
    num_fds: int
    tempdirs: set[str]


class ProcessIntrospector:
    def __init__(self) -> None:
        import psutil

        self._psutil = psutil
        self._proc = psutil.Process(os.getpid())

    def snapshot(self) -> LeakSnapshot:
        children = set()
        for child in self._proc.children(recursive=True):
            try:
                children.add(child.pid)
            except self._psutil.Error:
                pass
        try:
            num_fds = self._proc.num_fds()
        except (self._psutil.Error, AttributeError):
            num_fds = -1
        return LeakSnapshot(
            child_pids=children, num_fds=num_fds, tempdirs=accel_tempdirs()
        )

    def assert_no_leaks(
        self,
        before: LeakSnapshot,
        *,
        fd_slack: int = 8,
        label: str = "",
        settle_timeout: float = 5.0,
    ) -> None:
        after = self.snapshot()
        prefix = f"[{label}] " if label else ""
        leaked_children = after.child_pids - before.child_pids
        leaked_dirs = after.tempdirs - before.tempdirs
        assert not leaked_children, (
            f"{prefix}leaked {len(leaked_children)} daemon subprocess(es): "
            f"{sorted(leaked_children)}"
        )
        assert not leaked_dirs, f"{prefix}leaked accel tempdirs: {sorted(leaked_dirs)}"
        if before.num_fds < 0 or after.num_fds < 0:
            return
        gc.collect()
        min_fds = after.num_fds
        deadline = time.monotonic() + settle_timeout
        while min_fds > before.num_fds + fd_slack and time.monotonic() < deadline:
            time.sleep(0.1)
            cur = self.snapshot().num_fds
            if cur >= 0:
                min_fds = min(min_fds, cur)
        assert min_fds <= before.num_fds + fd_slack, (
            f"{prefix}fd count grew from {before.num_fds} to {min_fds} "
            f"(slack {fd_slack}) and did not drain within {settle_timeout:g}s"
        )


def force_kill_daemon(daemon: Any) -> None:
    proc = getattr(daemon, "_proc", None)
    if proc is None:
        return
    try:
        proc.kill()
    except Exception:
        pass
    try:
        proc.wait(timeout=2.0)
    except Exception:
        pass


def daemon_pid(table: Any) -> int | None:
    daemon = getattr(table, "_accelerator_daemon", None)
    if daemon is None:
        return None
    try:
        return daemon.pid
    except RuntimeError:
        return None


def pid_alive(pid: int) -> bool:
    import psutil

    try:
        proc = psutil.Process(pid)
        return proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
    except psutil.Error:
        return False


class RandomOps:
    def __init__(
        self,
        seed: int,
        key_prefix: bytes = b"accel-",
        *,
        include_aggregate: bool = False,
    ):
        import random

        self._rand = random.Random(seed)
        self._keyspace = [key_prefix + f"{i:08d}".encode() for i in range(64)]
        self._families = [TEST_FAMILY, TEST_FAMILY_2]
        self._qualifiers = [f"q{i}".encode() for i in range(self._rand.randint(2, 16))]
        self._agg_qualifiers = [f"agg{i}".encode() for i in range(4)]
        self._include_aggregate = include_aggregate
        self._op_index = 0
        self._last_write_op: dict[bytes, int] = {}
        self._last_delete_op: dict[bytes, int] = {}

    def key(self) -> bytes:
        return self._rand.choice(self._keyspace)

    def value(self, max_len: int = 64) -> bytes:
        n = self._rand.randint(0, max_len)
        return bytes(self._rand.getrandbits(8) for _ in range(n))

    def ms_timestamp(self) -> int:
        return self._rand.randint(1, 2_000_000) * MS

    def family(self) -> str:
        return self._rand.choice(self._families)

    def qualifier(self) -> bytes:
        return self._rand.choice(self._qualifiers)

    def agg_qualifier(self) -> bytes:
        return self._rand.choice(self._agg_qualifiers)

    def add_delta(self) -> int:
        return self._rand.randint(-(2**20), 2**20)

    def _delete_target(self) -> tuple[str, bytes]:
        if self._include_aggregate and self._rand.random() < 0.30:
            return TEST_AGGREGATE_FAMILY, self.agg_qualifier()
        return self.family(), self.qualifier()

    def _delete_family(self) -> str:
        families = self._families + (
            [TEST_AGGREGATE_FAMILY] if self._include_aggregate else []
        )
        return self._rand.choice(families)

    def _build_multi_cf_mutations(
        self, key: bytes, expected_state: ExpectedState
    ) -> list[object]:
        """Build an atomic write list touching multiple CFs and qualifiers."""
        mutations: list[object] = []
        for idx, fam in enumerate(self._families):
            max_cols = min(3, len(self._qualifiers))
            min_cols = 2 if idx == 0 and max_cols >= 2 else 1
            num_cols = self._rand.randint(min_cols, max_cols)
            for qual in self._rand.sample(self._qualifiers, num_cols):
                mutations.append(
                    expected_state.set_cell(
                        key, fam, qual, self.value(), self.ms_timestamp()
                    )
                )
        if self._include_aggregate and self._rand.random() < 0.5:
            mutations.append(
                expected_state.add_to_cell(
                    key, self.agg_qualifier(), self.add_delta(), self.ms_timestamp()
                )
            )
        self._rand.shuffle(mutations)
        return mutations

    def build_mutation(self, expected_state: ExpectedState) -> tuple[bytes, object]:
        self._op_index += 1
        roll = self._rand.random()
        key = self.key()
        last_write = self._last_write_op.get(key)
        last_delete = self._last_delete_op.get(key)
        recently_written = (
            last_write is not None
            and self._op_index - last_write <= DELETE_AFTER_WRITE_GUARD_OPS
        )
        recently_deleted = (
            last_delete is not None
            and self._op_index - last_delete <= DELETE_AFTER_WRITE_GUARD_OPS
        )
        if recently_deleted and not recently_written:
            self._last_delete_op[key] = self._op_index
            return key, expected_state.delete_from_row(key)
        if self._include_aggregate and roll < 0.18:
            self._last_write_op[key] = self._op_index
            return key, expected_state.add_to_cell(
                key, self.agg_qualifier(), self.add_delta(), self.ms_timestamp()
            )
        if roll < 0.70 or recently_written:
            self._last_write_op[key] = self._op_index
            if self._rand.random() < 0.35:
                return key, self._build_multi_cf_mutations(key, expected_state)
            return key, expected_state.set_cell(
                key, self.family(), self.qualifier(), self.value(), self.ms_timestamp()
            )
        self._last_delete_op[key] = self._op_index
        if roll < 0.82:
            a = self._rand.choice([None, self.ms_timestamp()])
            b = self._rand.choice([None, self.ms_timestamp()])
            if a is not None and b is not None and a > b:
                a, b = b, a
            fam, qual = self._delete_target()
            return key, expected_state.delete_range_from_column(key, fam, qual, a, b)
        if roll < 0.92:
            return key, expected_state.delete_from_family(key, self._delete_family())
        return key, expected_state.delete_from_row(key)
