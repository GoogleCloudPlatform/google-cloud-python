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

import pytest

from google.cloud.storage._lru_cache import LRUCache


def test_lru_cache_capacity():
    cache = LRUCache(capacity=3)
    assert cache.capacity == 3

    with pytest.raises(ValueError):
        LRUCache(capacity=0)

    with pytest.raises(ValueError):
        LRUCache(capacity=-1)


def test_lru_cache_put_and_get():
    cache = LRUCache(capacity=2)
    assert cache.get("a") is None
    assert cache.get("a", default="default") == "default"

    cache.put("a", 1)
    assert cache.get("a") == 1
    assert len(cache) == 1
    assert "a" in cache

    cache.put("b", 2)
    assert cache.get("b") == 2
    assert len(cache) == 2
    assert "b" in cache


def test_lru_cache_eviction():
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    # Access "a" so "b" becomes least recently used
    assert cache.get("a") == 1

    # Put "c" should evict "b"
    cache.put("c", 3)

    assert "b" not in cache
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3
    assert len(cache) == 2


def test_lru_cache_update():
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    # Update "a", so it becomes most recently used
    cache.put("a", 10)

    # Put "c" should evict "b"
    cache.put("c", 3)

    assert "b" not in cache
    assert cache.get("a") == 10
    assert cache.get("c") == 3


def test_lru_cache_clear():
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    cache.clear()
    assert len(cache) == 0
    assert "a" not in cache
    assert "b" not in cache


def test_lru_cache_delete():
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)

    cache.delete("a")
    assert len(cache) == 1
    assert "a" not in cache
    assert cache.get("a") is None
    assert cache.get("b") == 2
