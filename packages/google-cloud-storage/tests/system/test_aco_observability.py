# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import concurrent.futures
import threading
import time

import pytest
from google.api_core import exceptions

from . import _helpers


def test_sequential_cache_priming(storage_client, exporter, buckets_to_delete):
    """Verifies that a cache miss returns immediately and warms the cache
    in a background thread, so a subsequent request successfully contains
    ACO destination attributes."""
    bucket_name = _helpers.unique_name("aco-priming")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    blob_name = "test_blob.txt"
    blob = bucket.blob(blob_name)
    blob.upload_from_string("hello")

    # Set up deterministic event-driven synchronization hooks
    original_update = storage_client._bucket_metadata_cache.update_cache
    update_cache_event = threading.Event()

    def monitored_update(*args, **kwargs):
        original_update(*args, **kwargs)
        update_cache_event.set()

    storage_client._bucket_metadata_cache.update_cache = monitored_update

    try:
        # Clear cache and OTel exporter logs
        storage_client._bucket_metadata_cache.clear()
        exporter.clear()

        # 1. First download (must be a cache miss)
        blob.download_as_bytes()

        spans = exporter.get_finished_spans()
        dl_spans = [s for s in spans if s.name == "Storage.Blob.downloadAsBytes"]
        assert len(dl_spans) == 1
        attrs = dl_spans[0].attributes
        assert "gcp.resource.destination.id" not in attrs
        assert "gcp.resource.destination.location" not in attrs

        # Wait deterministically for background fetch thread to populate cache
        assert update_cache_event.wait(timeout=10.0)

        # 2. Second download (must be a cache hit)
        # Clear exporter so spans we capture correspond to the second download
        # (ACO attributes should now be present)
        exporter.clear()
        blob.download_as_bytes()

        spans = exporter.get_finished_spans()
        dl_spans = [s for s in spans if s.name == "Storage.Blob.downloadAsBytes"]
        assert len(dl_spans) == 1
        attrs = dl_spans[0].attributes
        assert "gcp.resource.destination.id" in attrs
        assert "gcp.resource.destination.location" in attrs
        assert bucket_name in attrs["gcp.resource.destination.id"]
    finally:
        storage_client._bucket_metadata_cache.update_cache = original_update


def test_403_permission_cache_fallback(storage_client, buckets_to_delete):
    """Verifies that if the client does not have permission for bucket metadata
    (403 Forbidden), the cache safely stores fallback annotations to prevent
    repetitive API calls on cache misses."""
    bucket_name = _helpers.unique_name("aco-403")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    storage_client._bucket_metadata_cache.clear()

    # Set up deterministic event-driven synchronization hooks
    original_update = storage_client._bucket_metadata_cache.update_cache
    update_cache_event = threading.Event()

    def monitored_update(*args, **kwargs):
        original_update(*args, **kwargs)
        update_cache_event.set()

    storage_client._bucket_metadata_cache.update_cache = monitored_update

    original_get_bucket = storage_client.get_bucket
    forbidden_triggered = threading.Event()

    def mock_get_bucket(*args, **kwargs):
        from google.api_core.exceptions import Forbidden

        forbidden_triggered.set()
        raise Forbidden("403 Forbidden simulated for system test")

    storage_client.get_bucket = mock_get_bucket

    try:
        # Trigger background fetch
        storage_client._bucket_metadata_cache.get_or_queue_fetch(bucket_name)

        # Wait for background fetch to execute and catch the Forbidden error
        assert forbidden_triggered.wait(timeout=3.0)

        # Wait deterministically for fallback to get populated in cache
        assert update_cache_event.wait(timeout=10.0)

        # Retrieve from cache
        cached = storage_client._bucket_metadata_cache.get(bucket_name)
        assert cached is not None
        dest_id, loc = cached
        assert dest_id == f"//storage.googleapis.com/projects/_/buckets/{bucket_name}"
        assert loc == "global"
    finally:
        storage_client.get_bucket = original_get_bucket
        storage_client._bucket_metadata_cache.update_cache = original_update


def test_cache_stampede_protection(storage_client, buckets_to_delete):
    """Verifies that under highly concurrent cache miss conditions, exactly one background metadata API fetch is executed, and all caller threads safely complete without stampeding the GCS server."""
    bucket_name = _helpers.unique_name("aco-stampede")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    blob = bucket.blob("test.txt")
    blob.upload_from_string("data")

    storage_client._bucket_metadata_cache.clear()

    fetch_count = 0
    count_lock = threading.Lock()
    original_get_bucket = storage_client.get_bucket

    def monitored_get_bucket(*args, **kwargs):
        nonlocal fetch_count
        with count_lock:
            fetch_count += 1
        return original_get_bucket(*args, **kwargs)

    storage_client.get_bucket = monitored_get_bucket

    try:
        num_threads = 15
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [
                executor.submit(blob.download_as_bytes) for _ in range(num_threads)
            ]
            concurrent.futures.wait(futures)

        # Exactly 1 background GCS get_bucket fetch call must have been triggered
        assert fetch_count == 1
    finally:
        storage_client.get_bucket = original_get_bucket


def test_cache_eviction_on_bucket_404(storage_client, buckets_to_delete):
    """Verifies that if a GCS bucket is deleted out-of-band, any operations triggering a 404 NotFound will asynchronously verify the deletion and evict the bucket from the cache."""
    bucket_name = _helpers.unique_name("aco-eviction-404")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    blob = bucket.blob("test.txt")
    blob.upload_from_string("data")

    # Set up deterministic event-driven synchronization hooks
    original_update = storage_client._bucket_metadata_cache.update_cache
    original_verify = storage_client._bucket_metadata_cache._verify_existence_background

    update_cache_event = threading.Event()
    verify_event = threading.Event()

    def monitored_update(*args, **kwargs):
        original_update(*args, **kwargs)
        update_cache_event.set()

    def monitored_verify(b_name):
        try:
            original_verify(b_name)
        finally:
            verify_event.set()

    storage_client._bucket_metadata_cache.update_cache = monitored_update
    storage_client._bucket_metadata_cache._verify_existence_background = (
        monitored_verify
    )

    try:
        # Clear and warm cache
        storage_client._bucket_metadata_cache.clear()
        storage_client._bucket_metadata_cache.get_or_queue_fetch(bucket_name)

        # Wait deterministically for cache warming to complete
        assert update_cache_event.wait(timeout=10.0)
        assert storage_client._bucket_metadata_cache.get(bucket_name) is not None

        # --- 4a. 404 on Bucket (Asynchronous Eviction) ---
        # Delete GCS bucket directly via HTTP connection to bypass client.delete synchronous eviction
        query_params = {}
        if bucket.user_project is not None:
            query_params["userProject"] = bucket.user_project
        blob.delete()
        storage_client._delete_resource(bucket.path, query_params=query_params)
        buckets_to_delete.remove(bucket)

        # Attempt to load blob (raises 404 NotFound bucket error)
        with pytest.raises(exceptions.NotFound):
            blob.download_as_bytes()

        # Wait deterministically for background check_and_evict thread to complete
        assert verify_event.wait(timeout=10.0)

        # Cache must be evicted
        assert storage_client._bucket_metadata_cache.get(bucket_name) is None
    finally:
        storage_client._bucket_metadata_cache.update_cache = original_update
        storage_client._bucket_metadata_cache._verify_existence_background = (
            original_verify
        )


def test_cache_eviction_on_bucket_delete(storage_client, buckets_to_delete):
    """Verifies that direct Bucket.delete() calls synchronously evict the cache."""
    bucket_name = _helpers.unique_name("aco-eviction-delete")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    # Warm cache directly via GCS creation warming
    assert storage_client._bucket_metadata_cache.get(bucket_name) is not None

    # Synchronously delete bucket via SDK client
    bucket.delete()
    buckets_to_delete.remove(bucket)

    # Cache MUST be evicted immediately without waiting
    assert storage_client._bucket_metadata_cache.get(bucket_name) is None


def test_404_on_blob_but_bucket_exists(storage_client, buckets_to_delete):
    """Verifies that a 404 `NotFound` on a missing blob inside an
    existing bucket; triggers background `check_and_evict` which retains
    the bucket in the cache."""
    bucket_name = _helpers.unique_name("aco-blob-404")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    # Set up deterministic event-driven synchronization hooks
    original_update = storage_client._bucket_metadata_cache.update_cache
    original_verify = storage_client._bucket_metadata_cache._verify_existence_background

    update_cache_event = threading.Event()
    verify_event = threading.Event()

    def monitored_update(*args, **kwargs):
        original_update(*args, **kwargs)
        update_cache_event.set()

    def monitored_verify(b_name):
        try:
            original_verify(b_name)
        finally:
            verify_event.set()

    storage_client._bucket_metadata_cache.update_cache = monitored_update
    storage_client._bucket_metadata_cache._verify_existence_background = (
        monitored_verify
    )

    try:
        # Warm cache
        storage_client._bucket_metadata_cache.clear()
        storage_client._bucket_metadata_cache.get_or_queue_fetch(bucket_name)

        # Wait deterministically for cache priming to complete
        assert update_cache_event.wait(timeout=10.0)
        assert storage_client._bucket_metadata_cache.get(bucket_name) is not None

        # Make a 404 request to a non-existent blob inside this bucket
        non_existent_blob = bucket.blob("non_existent.txt")
        with pytest.raises(exceptions.NotFound):
            non_existent_blob.download_as_bytes()

        # Wait deterministically for background check_and_evict thread to complete
        assert verify_event.wait(timeout=10.0)

        # Bucket must STILL be retained in the cache!
        assert storage_client._bucket_metadata_cache.get(bucket_name) is not None
    finally:
        # Clean up and restore original methods
        storage_client._bucket_metadata_cache.update_cache = original_update
        storage_client._bucket_metadata_cache._verify_existence_background = (
            original_verify
        )


def test_404_on_blob_bucket_deleted(storage_client):
    """Verifies that a 404 NotFound on a missing blob when the bucket is deleted
    triggers background check_and_evict which evicts the bucket from the cache."""
    bucket_name = _helpers.unique_name("aco-blob-bucket-404")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)

    # Set up deterministic event-driven synchronization hooks
    original_update = storage_client._bucket_metadata_cache.update_cache
    original_verify = storage_client._bucket_metadata_cache._verify_existence_background

    update_cache_event = threading.Event()
    verify_event = threading.Event()

    def monitored_update(*args, **kwargs):
        original_update(*args, **kwargs)
        update_cache_event.set()

    def monitored_verify(b_name):
        try:
            original_verify(b_name)
        finally:
            verify_event.set()

    storage_client._bucket_metadata_cache.update_cache = monitored_update
    storage_client._bucket_metadata_cache._verify_existence_background = (
        monitored_verify
    )

    try:
        # Warm cache
        storage_client._bucket_metadata_cache.clear()
        storage_client._bucket_metadata_cache.get_or_queue_fetch(bucket_name)

        # Wait deterministically for cache priming to complete
        assert update_cache_event.wait(timeout=10.0)
        assert storage_client._bucket_metadata_cache.get(bucket_name) is not None

        # Delete bucket directly via GCS connection (bypassing client synchronous eviction)
        query_params = {}
        if bucket.user_project is not None:
            query_params["userProject"] = bucket.user_project
        storage_client._delete_resource(bucket.path, query_params=query_params)

        # Make 404 request to a blob (raises 404 NotFound because bucket is deleted)
        non_existent_blob = bucket.blob("non_existent.txt")
        with pytest.raises(exceptions.NotFound):
            non_existent_blob.download_as_bytes()

        # Wait deterministically for background check_and_evict thread to complete
        assert verify_event.wait(timeout=10.0)

        # Bucket must be evicted from the cache!
        assert storage_client._bucket_metadata_cache.get(bucket_name) is None
    finally:
        storage_client._bucket_metadata_cache.update_cache = original_update
        storage_client._bucket_metadata_cache._verify_existence_background = (
            original_verify
        )


def test_lru_bounded_capacity_eviction(storage_client):
    """Verifies that the cache respects the configured size bounds and correctly
    evicts the least-recently-used elements to avoid memory leaks."""
    from google.cloud.storage._bucket_metadata_cache import BucketMetadataCache

    cache = BucketMetadataCache(storage_client, max_size=5)

    # Populate with 5 buckets
    cache.update_cache("b1", "dest1", "loc1")
    cache.update_cache("b2", "dest2", "loc2")
    cache.update_cache("b3", "dest3", "loc3")
    cache.update_cache("b4", "dest4", "loc4")
    cache.update_cache("b5", "dest5", "loc5")

    # Access b1 (make it most recently used)
    cache.get("b1")

    # Add b6 (which evicts b2, the LRU item)
    cache.update_cache("b6", "dest6", "loc6")

    # Assert b2 is evicted
    assert cache.get("b2") is None
    # Assert b1 is retained
    assert cache.get("b1") == ("dest1", "loc1")
    # Assert b6 is present
    assert cache.get("b6") == ("dest6", "loc6")


def test_create_bucket_synchronous_cache_warming(storage_client, buckets_to_delete):
    """Verifies that calling client.create_bucket() synchronously warms the cache immediately upon bucket creation and does not trigger any background fetch threads."""
    # Wait for any previous inflight background fetches to complete
    start_time = time.time()
    while time.time() - start_time < 5.0:
        with storage_client._bucket_metadata_cache._lock:
            if not storage_client._bucket_metadata_cache._inflight_fetches:
                break
        time.sleep(0.1)

    bucket_name = _helpers.unique_name("aco-sync-create")
    bucket = storage_client.bucket(bucket_name)

    # Ensure cache is clear
    storage_client._bucket_metadata_cache.clear()

    # Setup background fetch monitoring hook
    original_fetch = storage_client._bucket_metadata_cache._fetch_background
    fetch_triggered = False

    def monitored_fetch(*args, **kwargs):
        nonlocal fetch_triggered
        fetch_triggered = True
        return original_fetch(*args, **kwargs)

    storage_client._bucket_metadata_cache._fetch_background = monitored_fetch

    try:
        storage_client.create_bucket(bucket)
        buckets_to_delete.append(bucket)

        # Assert cache is populated instantly (synchronously)
        cached = storage_client._bucket_metadata_cache.get(bucket_name)
        assert cached is not None
        dest_id, loc = cached
        assert bucket_name in dest_id

        # Verify that no background fetch thread was ever triggered!
        assert not fetch_triggered
    finally:
        storage_client._bucket_metadata_cache._fetch_background = original_fetch


def test_get_bucket_synchronous_cache_warming(storage_client, buckets_to_delete):
    """Verifies that calling client.get_bucket() for the first time (cache miss) synchronously warms the cache immediately without triggering any background fetch threads."""
    # Wait for any previous inflight background fetches to complete
    start_time = time.time()
    while time.time() - start_time < 5.0:
        with storage_client._bucket_metadata_cache._lock:
            if not storage_client._bucket_metadata_cache._inflight_fetches:
                break
        time.sleep(0.1)

    bucket_name = _helpers.unique_name("aco-sync-get")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    # Ensure cache is clear
    storage_client._bucket_metadata_cache.clear()

    # Setup background fetch monitoring hook
    original_fetch = storage_client._bucket_metadata_cache._fetch_background
    fetch_triggered = False

    def monitored_fetch(*args, **kwargs):
        nonlocal fetch_triggered
        fetch_triggered = True
        return original_fetch(*args, **kwargs)

    storage_client._bucket_metadata_cache._fetch_background = monitored_fetch

    try:
        # Call client.get_bucket()
        storage_client.get_bucket(bucket_name)

        # Assert cache is populated instantly (synchronously) without background delay
        cached = storage_client._bucket_metadata_cache.get(bucket_name)
        assert cached is not None
        dest_id, loc = cached
        assert bucket_name in dest_id

        # Verify that no background fetch thread was ever triggered!
        assert not fetch_triggered
    finally:
        storage_client._bucket_metadata_cache._fetch_background = original_fetch


def test_sequential_cache_priming_multi_region(
    storage_client, exporter, buckets_to_delete
):
    """Verifies that a cache miss returns immediately and warms the cache
    in a background thread for a multi-region bucket, and the resolved location
    is 'global'."""
    bucket_name = _helpers.unique_name("aco-priming-multi")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket, location="us")
    buckets_to_delete.append(bucket)

    blob_name = "test_blob.txt"
    blob = bucket.blob(blob_name)
    op_name = "Storage.Blob.downloadAsBytes"
    blob.upload_from_string("hello")

    # Set up deterministic event-driven synchronization hooks
    original_update = storage_client._bucket_metadata_cache.update_cache
    update_cache_event = threading.Event()

    def monitored_update(*args, **kwargs):
        original_update(*args, **kwargs)
        update_cache_event.set()

    storage_client._bucket_metadata_cache.update_cache = monitored_update

    try:
        # Clear cache and OTel exporter logs
        storage_client._bucket_metadata_cache.clear()
        exporter.clear()

        # 1. First download (must be a cache miss)
        blob.download_as_bytes()

        spans = exporter.get_finished_spans()
        dl_spans = [s for s in spans if s.name == op_name]
        assert len(dl_spans) == 1
        attrs = dl_spans[0].attributes
        assert "gcp.resource.destination.id" not in attrs
        assert "gcp.resource.destination.location" not in attrs

        # Wait deterministically for background fetch thread to populate cache
        assert update_cache_event.wait(timeout=10.0)

        # 2. Second download (must be a cache hit)
        exporter.clear()
        blob.download_as_bytes()

        spans = exporter.get_finished_spans()
        dl_spans = [s for s in spans if s.name == op_name]
        assert len(dl_spans) == 1
        attrs = dl_spans[0].attributes
        assert "gcp.resource.destination.id" in attrs
        assert "gcp.resource.destination.location" in attrs
        assert bucket_name in attrs["gcp.resource.destination.id"]
        # Multi-region location must be 'global'
        assert attrs["gcp.resource.destination.location"] == "global"
    finally:
        storage_client._bucket_metadata_cache.update_cache = original_update


@pytest.mark.parametrize("env_value", ["true", "1", "yes", "on"])
def test_disable_bucket_md_env_flag(
    storage_client, exporter, buckets_to_delete, monkeypatch, env_value
):
    """Verifies that setting DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA to a truthy value disables GCS
    destination annotations, even on cache hits."""
    # Clear cache and OTel exporter logs
    storage_client._bucket_metadata_cache.clear()
    exporter.clear()

    bucket_name = _helpers.unique_name("aco-disable")
    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    blob_name = "test_blob.txt"
    blob = bucket.blob(blob_name)
    blob.upload_from_string("hello")

    # Warm cache directly via GCS creation warming (client.create_bucket already primes the cache)
    assert storage_client._bucket_metadata_cache.get(bucket_name) is not None

    # Enable the DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA environment variable using monkeypatch
    monkeypatch.setenv("DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA", env_value)

    # Download (normally would be a cache hit with GCS annotations)
    blob.download_as_bytes()

    # Verify that ACO attributes are NOT present in the OTel span!
    spans = exporter.get_finished_spans()
    dl_spans = [s for s in spans if s.name == "Storage.Blob.downloadAsBytes"]
    assert len(dl_spans) == 1
    attrs = dl_spans[0].attributes
    assert "gcp.resource.destination.id" not in attrs
    assert "gcp.resource.destination.location" not in attrs
