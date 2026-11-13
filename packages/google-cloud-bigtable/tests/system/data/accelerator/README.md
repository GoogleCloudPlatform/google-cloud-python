# Cloud Bigtable Accelerator System Tests

Shared environment setup, fixtures, and state/process helpers for live Cloud Bigtable Python accelerator system tests. Tests using this harness run against a real Cloud Bigtable instance and a real Go accelerator binary; emulator and binary-less environments skip cleanly.

## Harness Components

- [`conftest.py`](conftest.py): Registers the `accelerator` and `slow` pytest markers, provides `tmp_bin_dir`, and wraps `get_table()` on both sync and async data clients to inject `BIGTABLE_TEST_APP_PROFILE` (or `CBT_APP_PROFILE_ID`) when no `app_profile_id` is passed.
- [`_base_async.py`](_base_async.py) / [`_base_autogen.py`](_base_autogen.py): Define `AcceleratorTestBaseAsync` and its CrossSync sibling `AcceleratorTestBase`. They enforce live-instance and binary prerequisites per session, expose `client`, `accel_client`, `native_client`, `accel_table`, `native_table`, `default_table`, and `janitor` cleanup fixtures, and assert `table._accelerator_client` state via `assert_accelerator_active()` and `assert_native()`.
- [`_harness.py`](_harness.py): Provides the in-memory reference model (`ExpectedState`, `normalize_row`, `assert_rows_equivalent`), seeded workload generator (`RandomOps` with atomic multi-family/multi-column batches and `DELETE_AFTER_WRITE_GUARD_OPS = 512`), process leak/kill helpers (`ProcessIntrospector`, `force_kill_daemon`, `daemon_pid`, `pid_alive`), and binary/environment gates (`resolve_binary`, `require_binary_or_skip`, `require_real_bigtable_or_skip`).
- Package root [`pytest.ini`](../../../../pytest.ini) & [`conftest.py`](../../../../conftest.py): Set session-scoped `pytest-asyncio` loops and register the loop-scope ini options so older `pytest-asyncio` (<0.23) versions do not warn or fail.

## Environment Variables

| Variable | Required | Purpose |
| --- | --- | --- |
| `GOOGLE_CLOUD_PROJECT` (or `PROJECT_ID`) | Yes | Target GCP project; tests skip if unset. |
| `BIGTABLE_EMULATOR_HOST` | Must be unset | Emulator runs skip because the Go accelerator does not support the emulator. |
| `BIGTABLE_ACCELERATOR_BIN` | No | Path to a locally built Go accelerator binary; overrides the wheel-bundled binary lookup (`_daemon._resolve_binary_path()`). |
| `BIGTABLE_TEST_APP_PROFILE` (or `CBT_APP_PROFILE_ID`) | No | Default app profile ID injected into `get_table()` calls. |

## Running Locally & Syncing

Run pytest from `packages/google-cloud-bigtable/` once a compiled Go binary (or bundled wheel) and GCP project are available:

```bash
BIGTABLE_ACCELERATOR_BIN=/path/to/accelerator \
GOOGLE_CLOUD_PROJECT=my-project \
pytest tests/system/data/accelerator -v
```

If you edit `_base_async.py`, regenerate `_base_autogen.py` from `packages/google-cloud-bigtable/` with `nox -s generate_sync`.
