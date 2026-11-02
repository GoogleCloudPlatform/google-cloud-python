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

import unittest
from unittest import mock

from google.api_core import exceptions as api_exceptions
from google.cloud.exceptions import NotFound

from google.cloud.storage._bucket_metadata_cache import BucketMetadataCache


class TestBucketMetadataCache(unittest.TestCase):
    @mock.patch("threading.Thread")
    def test_lru_eviction(self, mock_thread):
        client = mock.Mock()
        cache = BucketMetadataCache(client, max_size=3)

        cache.update_cache("b1", "dest1", "loc1")
        cache.update_cache("b2", "dest2", "loc2")
        cache.update_cache("b3", "dest3", "loc3")
        cache.update_cache("b4", "dest4", "loc4")  # Evicts b1 (oldest)

        self.assertIsNone(cache.get_or_queue_fetch("b1"))
        self.assertEqual(cache.get_or_queue_fetch("b2"), ("dest2", "loc2"))
        self.assertEqual(cache.get_or_queue_fetch("b3"), ("dest3", "loc3"))
        self.assertEqual(cache.get_or_queue_fetch("b4"), ("dest4", "loc4"))

    def test_update_from_bucket(self):
        client = mock.Mock()
        cache = BucketMetadataCache(client)

        # Multi-region -> global
        b1 = mock.Mock()
        b1.name = "b1"
        b1.location = "US"
        b1.location_type = "multi-region"
        b1.project_number = 123
        cache.update_from_bucket(b1)
        self.assertEqual(
            cache.get_or_queue_fetch("b1"),
            ("//storage.googleapis.com/projects/123/buckets/b1", "global"),
        )

        # Dual-region -> global
        b2 = mock.Mock()
        b2.name = "b2"
        b2.location = "NAM4"
        b2.location_type = "dual-region"
        b2.project_number = 456
        cache.update_from_bucket(b2)
        self.assertEqual(
            cache.get_or_queue_fetch("b2"),
            ("//storage.googleapis.com/projects/456/buckets/b2", "global"),
        )

        # Region -> us-east1
        b3 = mock.Mock()
        b3.name = "b3"
        b3.location = "US-EAST1"
        b3.location_type = "region"
        b3.project_number = 789
        cache.update_from_bucket(b3)
        self.assertEqual(
            cache.get_or_queue_fetch("b3"),
            ("//storage.googleapis.com/projects/789/buckets/b3", "us-east1"),
        )

        # Missing project number -> _
        b4 = mock.Mock()
        b4.name = "b4"
        b4.location = "eu-west1"
        b4.location_type = "region"
        b4.project_number = None
        cache.update_from_bucket(b4)
        self.assertEqual(
            cache.get_or_queue_fetch("b4"),
            ("//storage.googleapis.com/projects/_/buckets/b4", "eu-west1"),
        )

    @mock.patch("threading.Thread")
    def test_get_or_queue_fetch(self, mock_thread):
        client = mock.Mock()
        cache = BucketMetadataCache(client)

        # Cache miss -> returns None immediately and spawns thread
        result = cache.get_or_queue_fetch("my-bucket")
        self.assertIsNone(result)
        mock_thread.assert_called_once()

        # Second immediate lookup -> returns None, does not spawn another thread (singleflight)
        mock_thread.reset_mock()
        result2 = cache.get_or_queue_fetch("my-bucket")
        self.assertIsNone(result2)
        mock_thread.assert_not_called()

    def test_fetch_background_success(self):
        client = mock.Mock()
        b1 = mock.Mock()
        b1.name = "b1"
        b1.location = "US-WEST1"
        b1.location_type = "region"
        b1.project_number = 999
        client.get_bucket.return_value = b1

        cache = BucketMetadataCache(client)
        cache._inflight_fetches.add("b1")

        cache._fetch_background("b1")

        self.assertEqual(
            cache.get_or_queue_fetch("b1"),
            ("//storage.googleapis.com/projects/999/buckets/b1", "us-west1"),
        )
        self.assertNotIn("b1", cache._inflight_fetches)

    def test_fetch_background_not_found(self):
        client = mock.Mock()
        client.get_bucket.side_effect = NotFound("Bucket not found")
        cache = BucketMetadataCache(client)
        cache.update_cache(
            "b1", "//storage.googleapis.com/projects/_/buckets/b1", "global"
        )
        cache._inflight_fetches.add("b1")

        cache._fetch_background("b1")

        self.assertNotIn("b1", cache._cache)
        self.assertNotIn("b1", cache._inflight_fetches)

    def test_fetch_background_forbidden(self):
        client = mock.Mock()
        client.get_bucket.side_effect = api_exceptions.Forbidden("403")
        cache = BucketMetadataCache(client)
        cache._inflight_fetches.add("b1")

        cache._fetch_background("b1")

        self.assertEqual(
            cache.get_or_queue_fetch("b1"),
            ("//storage.googleapis.com/projects/_/buckets/b1", "global"),
        )
        self.assertNotIn("b1", cache._inflight_fetches)

    @mock.patch("threading.Thread")
    def test_clear_and_evict(self, mock_thread):
        client = mock.Mock()
        cache = BucketMetadataCache(client)

        cache.update_cache("b1", "dest1", "loc1")
        cache.evict("b1")
        self.assertNotIn("b1", cache._cache)

        cache.update_cache("b2", "dest2", "loc2")
        cache.clear()
        self.assertNotIn("b2", cache._cache)

    @mock.patch("threading.Thread")
    def test_check_and_evict_queue(self, mock_thread):
        client = mock.Mock()
        cache = BucketMetadataCache(client)
        cache.update_cache("b1", "dest1", "loc1")

        cache.check_and_evict("b1")
        mock_thread.assert_called_once()
        self.assertIn("b1", cache._inflight_checks)

        # Second immediate check -> singleflight
        mock_thread.reset_mock()
        cache.check_and_evict("b1")
        mock_thread.assert_not_called()

    def test_verify_existence_background_exists(self):
        client = mock.Mock()
        b1 = mock.Mock()
        b1.exists.return_value = True
        client.bucket.return_value = b1

        cache = BucketMetadataCache(client)
        cache.update_cache("b1", "dest1", "loc1")
        cache._inflight_checks.add("b1")

        cache._verify_existence_background("b1")

        self.assertIn("b1", cache._cache)
        self.assertNotIn("b1", cache._inflight_checks)

    def test_verify_existence_background_deleted(self):
        client = mock.Mock()
        b1 = mock.Mock()
        b1.exists.return_value = False
        client.bucket.return_value = b1

        cache = BucketMetadataCache(client)
        cache.update_cache("b1", "dest1", "loc1")
        cache._inflight_checks.add("b1")

        cache._verify_existence_background("b1")

        self.assertNotIn("b1", cache._cache)
        self.assertNotIn("b1", cache._inflight_checks)
