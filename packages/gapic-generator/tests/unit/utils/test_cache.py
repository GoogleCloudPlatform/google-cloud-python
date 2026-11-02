# Copyright 2018 Google LLC
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

from gapic.utils import cache


def test_cached_property():
    class Foo:
        def __init__(self):
            self.call_count = 0

        @cache.cached_property
        def bar(self):
            self.call_count += 1
            return 42

    foo = Foo()
    assert foo.call_count == 0
    assert foo.bar == 42
    assert foo.call_count == 1
    assert foo.bar == 42
    assert foo.call_count == 1


def test_cached_proto_context():
    class Foo:
        def __init__(self):
            self.call_count = 0

        # We define a signature that matches the real Proto.with_context
        # to ensure arguments are propagated correctly.
        @cache.cached_proto_context
        def with_context(self, collisions, *, skip_fields=False, visited_messages=None):
            self.call_count += 1
            return f"val-{self.call_count}"

    foo = Foo()

    # 1. Test Bypass (No Context)
    # The cache is not active, so every call increments the counter.
    assert foo.with_context(collisions={"a"}) == "val-1"
    assert foo.with_context(collisions={"a"}) == "val-2"

    # 2. Test Context Activation
    with cache.generation_cache_context():
        # Reset counter to make tracking easier
        foo.call_count = 0

        # A. Basic Cache Hit
        assert foo.with_context(collisions={"a"}) == "val-1", "a"
        assert foo.with_context(collisions={"a"}) == "val-1"  # Hit
        assert foo.call_count == 1

        # B. Collision Difference
        # Changing collisions creates a new key
        assert foo.with_context(collisions={"b"}) == "val-2"
        assert foo.call_count == 2

    # 3. Context Cleared
    # Everything should be forgotten now.
    assert (
        getattr(cache._proto_collisions_cache_state, "resolved_collisions", None)
        is None
    )
    assert foo.with_context(collisions={"a"}) == "val-3"
