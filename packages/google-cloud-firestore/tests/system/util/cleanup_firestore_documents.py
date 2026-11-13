# Copyright 2017 Google LLC
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
"""Prune leaked root collections and documents from Firestore system test DBs.

Examples:
    # 1. Dry-run on (default) database to inspect counts and sample names:
    python tests/system/util/cleanup_firestore_documents.py --dry-run

    # 2. Prune leaked collections older than 2 hours on (default):
    python tests/system/util/cleanup_firestore_documents.py

    # 3. Prune leaked collections on the secondary named database:
    python tests/system/util/cleanup_firestore_documents.py --database system-tests-named-db
"""

from __future__ import annotations

import argparse
import asyncio
import os
import re
import time

import google.auth
from google.api_core import exceptions as core_exceptions
from google.api_core import retry_async as retries
from google.oauth2 import service_account

from google.cloud.firestore_v1 import AsyncClient
from google.cloud.firestore_v1.field_path import FieldPath

# Permanent seed collections (vector_search, pipeline_e2e) and shared static
# parent collections used by active single-doc/collection-group system tests.
PROTECTED_COLLECTIONS = frozenset(
    {
        # Bootstrapped seed collections (must never be deleted)
        "vector_search",
        "books",
        "timestamps",
        "vectors",
        "errors",
        "cities",
        "restaurants",
        "system_tests",
        # Shared static collections used by single-doc / watch / cg tests
        "users",
        "i-did-it",
        "made",
        "created",
        "here-to-be",
        "abcde",
        "top",
        "a",
        "abc",
        "def",
        "ghi",
    }
)

_TIMESTAMP_RE = re.compile(r"(?<!\d)(\d{13}|\d{10})(?!\d)")

_RETRY = retries.AsyncRetry(
    initial=0.2,
    maximum=30.0,
    multiplier=1.5,
    predicate=retries.if_exception_type(
        core_exceptions.DeadlineExceeded,
        core_exceptions.InternalServerError,
        core_exceptions.ServiceUnavailable,
        core_exceptions.Aborted,
    ),
    deadline=300.0,
)

_MAX_BATCH_SIZE = 500


def _get_credentials_and_project(project_override: str | None):
    creds_path = os.environ.get("FIRESTORE_APPLICATION_CREDENTIALS")
    if creds_path:
        credentials = service_account.Credentials.from_service_account_file(creds_path)
        project = (
            project_override
            or os.environ.get("GCLOUD_PROJECT")
            or os.environ.get("GOOGLE_CLOUD_PROJECT")
            or credentials.project_id
        )
    else:
        credentials, default_project = google.auth.default()
        project = (
            project_override
            or os.environ.get("GCLOUD_PROJECT")
            or os.environ.get("GOOGLE_CLOUD_PROJECT")
            or default_project
        )
    return credentials, project


def _extract_timestamp_seconds(collection_id: str, now_sec: float) -> float | None:
    """Extract embedded Unix timestamp (seconds or ms) from unique_resource_id."""
    for match in _TIMESTAMP_RE.finditer(collection_id):
        raw = int(match.group(1))
        if len(match.group(1)) == 13:
            sec = raw / 1000.0
        else:
            sec = float(raw)
        if 1_400_000_000 <= sec <= now_sec + 86_400:
            return sec
    return None


async def _prune_database(args: argparse.Namespace) -> None:
    credentials, project = _get_credentials_and_project(args.project)
    db_display = args.database or "(default)"
    print(f"Target project:  {project}")
    print(f"Target database: {db_display}")
    print(
        f"Mode:            {'DRY RUN (no deletes)' if args.dry_run else 'LIVE DELETE'}"
    )
    print(f"Min age filter:  {args.min_age_minutes} minutes")

    client = AsyncClient(
        project=project, credentials=credentials, database=args.database
    )

    now_sec = time.time()
    min_age_sec = args.min_age_minutes * 60.0

    to_delete_ids: list[str] = []
    protected_ids: list[str] = []
    no_timestamp_ids: list[str] = []
    recent_ids: list[str] = []

    t0 = time.monotonic()
    deadline = (t0 + args.max_seconds) if args.max_seconds else None
    list_deadline = (t0 + args.max_seconds * 0.5) if args.max_seconds else None
    scanned_total = 0
    print("\nListing root collections...")
    async for col_ref in client.collections(retry=_RETRY, timeout=300.0):
        scanned_total += 1
        col_id = col_ref.id
        if col_id in PROTECTED_COLLECTIONS:
            protected_ids.append(col_id)
        else:
            created_sec = _extract_timestamp_seconds(col_id, now_sec)
            if created_sec is None:
                # Never delete collections without an embedded unique_resource_id
                # timestamp — they may be permanent seed/manual/cross-SDK data.
                no_timestamp_ids.append(col_id)
            elif (now_sec - created_sec) < min_age_sec:
                recent_ids.append(col_id)
            else:
                to_delete_ids.append(col_id)

        if scanned_total % 2000 == 0:
            elapsed = time.monotonic() - t0
            print(f"  Listed {scanned_total:,} collections ({elapsed:.1f}s)...")

        if args.limit and not args.dry_run and len(to_delete_ids) >= args.limit:
            print(
                f"  Reached --limit {args.limit:,} eligible collections; stopping scan early."
            )
            break
        if (
            list_deadline is not None
            and not args.dry_run
            and len(to_delete_ids) > 0
            and time.monotonic() >= list_deadline
        ):
            print(
                f"  Reached 50% of --max-seconds ({args.max_seconds:.0f}s) during listing; "
                "proceeding to delete collected batch."
            )
            break

    list_elapsed = time.monotonic() - t0
    print(
        f"\nScan complete in {list_elapsed:.1f}s ({scanned_total:,} total):\n"
        f"  Protected (kept):           {len(protected_ids):,}\n"
        f"  No timestamp (kept):        {len(no_timestamp_ids):,}\n"
        f"  Recent <{args.min_age_minutes}m (kept):      {len(recent_ids):,}\n"
        f"  Eligible to prune:          {len(to_delete_ids):,}"
    )

    if protected_ids:
        print(f"  Protected names found:      {sorted(protected_ids)}")
    if no_timestamp_ids:
        print(f"  Sample no-timestamp kept:   {no_timestamp_ids[:10]}")
    if to_delete_ids:
        sample = to_delete_ids[:10]
        print(f"  Sample collections to prune: {sample}")

    if args.limit and len(to_delete_ids) > args.limit:
        print(f"\nApplying --limit {args.limit:,} (of {len(to_delete_ids):,}).")
        to_delete_ids = to_delete_ids[: args.limit]

    if args.dry_run or not to_delete_ids:
        return

    print(
        f"\nPruning {len(to_delete_ids):,} collections "
        f"(concurrency={args.concurrency})..."
    )
    sem = asyncio.Semaphore(args.concurrency)
    doc_queue: asyncio.Queue = asyncio.Queue(maxsize=args.concurrency * _MAX_BATCH_SIZE)

    collections_scanned = 0
    collections_skipped_timeout = 0
    docs_deleted = 0
    failed_collections = 0
    prune_start = time.monotonic()

    async def scan_collection(col_id: str) -> None:
        nonlocal collections_scanned, collections_skipped_timeout, failed_collections
        if deadline is not None and time.monotonic() >= deadline:
            collections_skipped_timeout += 1
            return
        async with sem:
            if deadline is not None and time.monotonic() >= deadline:
                collections_skipped_timeout += 1
                return
            try:
                query = (
                    client.collection(col_id)
                    .recursive()
                    .select([FieldPath.document_id()])
                )
                async for snap in query.stream(retry=_RETRY, timeout=120.0):
                    await doc_queue.put(snap.reference)
            except Exception as exc:
                failed_collections += 1
                print(f"  [WARN] Failed scanning {col_id}: {exc}")
            finally:
                collections_scanned += 1

    async def batch_deleter() -> None:
        nonlocal docs_deleted
        while True:
            first_ref = await doc_queue.get()
            if first_ref is None:
                doc_queue.task_done()
                return

            refs = [first_ref]
            saw_sentinel = False
            while len(refs) < _MAX_BATCH_SIZE:
                try:
                    next_ref = doc_queue.get_nowait()
                except asyncio.QueueEmpty:
                    break
                if next_ref is None:
                    saw_sentinel = True
                    doc_queue.task_done()
                    break
                refs.append(next_ref)

            batch = client.batch()
            for ref in refs:
                batch.delete(ref)
            try:
                await batch.commit(retry=_RETRY, timeout=120.0)
                docs_deleted += len(refs)
            except Exception as exc:
                print(f"  [WARN] Batch commit failed ({len(refs)} docs): {exc}")
            finally:
                for _ in refs:
                    doc_queue.task_done()

            if saw_sentinel:
                return

    async def progress_reporter(done_event: asyncio.Event) -> None:
        while not done_event.is_set():
            try:
                await asyncio.wait_for(done_event.wait(), timeout=5.0)
            except asyncio.TimeoutError:
                elapsed = time.monotonic() - prune_start
                rate = collections_scanned / elapsed if elapsed > 0 else 0.0
                print(
                    f"  Progress: {collections_scanned:,}/{len(to_delete_ids):,} "
                    f"collections ({rate:.1f} colls/s) | "
                    f"{docs_deleted:,} docs deleted ({elapsed:.0f}s)"
                )

    num_deleters = max(4, args.concurrency // 2)
    deleter_tasks = [asyncio.create_task(batch_deleter()) for _ in range(num_deleters)]
    done_event = asyncio.Event()
    reporter_task = asyncio.create_task(progress_reporter(done_event))

    await asyncio.gather(*(scan_collection(cid) for cid in to_delete_ids))
    for _ in range(num_deleters):
        await doc_queue.put(None)
    await asyncio.gather(*deleter_tasks)

    done_event.set()
    await reporter_task

    total_elapsed = time.monotonic() - prune_start
    print(
        f"\nDone in {total_elapsed:.1f}s: scanned {collections_scanned:,} collections "
        f"({failed_collections} errors, {collections_skipped_timeout:,} deferred by --max-seconds), "
        f"deleted {docs_deleted:,} documents."
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--project",
        default=None,
        help="GCP project ID (defaults to FIRESTORE_APPLICATION_CREDENTIALS / ADC).",
    )
    parser.add_argument(
        "--database",
        default=None,
        help="Firestore database ID (defaults to '(default)').",
    )
    parser.add_argument(
        "--min-age-minutes",
        type=float,
        default=120.0,
        help="Skip collections whose embedded timestamp is newer than this (default: 120m).",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=50,
        help="Max concurrent recursive collection scans (default: 50).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Optional cap on number of collections to prune in one run (0 = all).",
    )
    parser.add_argument(
        "--max-seconds",
        type=float,
        default=0.0,
        help="Optional soft time budget in seconds for the whole prune run (0 = unlimited).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List collection counts and samples without deleting anything.",
    )
    args = parser.parse_args()
    asyncio.run(_prune_database(args))


if __name__ == "__main__":
    main()
