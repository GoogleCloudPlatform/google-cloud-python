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

import functools
import contextlib
import threading


def cached_property(fx):
    """Make the callable into a cached property.

    Similar to @property, but the function will only be called once per
    object.

    Args:
        fx (Callable[]): The property function.

    Returns:
        Callable[]: The wrapped function.
    """

    @functools.wraps(fx)
    def inner(self):
        # Quick check: If there is no cache at all, create an empty cache.
        if not hasattr(self, "_cached_values"):
            object.__setattr__(self, "_cached_values", {})

        # If and only if the function's result is not in the cache,
        # run the function.
        if fx.__name__ not in self._cached_values:
            self._cached_values[fx.__name__] = fx(self)

        # Return the value from cache.
        return self._cached_values[fx.__name__]

    return property(inner)


# Thread-local storage for the simple cache dictionary.
# This ensures that parallel generation tasks (if any) do not corrupt each other's cache.
_proto_collisions_cache_state = threading.local()


@contextlib.contextmanager
def generation_cache_context():
    """Context manager to explicitly manage the lifecycle of the generation cache.

    This manager initializes a fresh dictionary in thread-local storage when entering
    the context and strictly deletes it when exiting.

    **Memory Management:**
    The cache stores strong references to Proto objects to "pin" them in memory
    (see `cached_proto_context`). It is critical that this context manager deletes
    the dictionary in the `finally` block. Deleting the dictionary breaks the
    reference chain, allowing Python's Garbage Collector to finally free all the
    large Proto objects that were pinned during generation.
    """
    # Initialize the cache as a standard dictionary.
    _proto_collisions_cache_state.resolved_collisions = {}
    try:
        yield
    finally:
        # Delete the dictionary to free all memory and pinned objects.
        # This is essential to prevent memory leaks in long-running processes.
        del _proto_collisions_cache_state.resolved_collisions


def cached_proto_context(func):
    """Decorator to memoize `with_context` calls based on object identity and collisions.

    This mechanism provides a significant performance boost by preventing
    redundant recalculations of naming collisions during template rendering.

    Since the Proto wrapper objects are unhashable (mutable), we use `id(self)` as
    the primary cache key. Normally, this is dangerous: if the object is garbage
    collected, Python might reuse its memory address for a *new* object, leading to
    a cache collision (the "Zombie ID" bug).

    To prevent this, this decorator stores the value as a tuple: `(result, self)`.
    By keeping a reference to `self` in the cache value, we "pin" the object in
    memory. This forces the Garbage Collector to keep the object alive, guaranteeing
    that `id(self)` remains unique for the entire lifespan of the `generation_cache_context`.

    Args:
        func (Callable): The function to decorate (usually `with_context`).

    Returns:
        Callable: The wrapped function with caching and pinning logic.
    """

    @functools.wraps(func)
    def wrapper(self, *, collisions, **kwargs):
        # 1. Check for active cache (returns None if context is not active)
        context_cache = getattr(
            _proto_collisions_cache_state, "resolved_collisions", None
        )

        # If we are not inside a generation_cache_context (e.g. unit tests),
        # bypass the cache entirely.
        if context_cache is None:
            return func(self, collisions=collisions, **kwargs)

        # 2. Create the cache key
        # We use frozenset for collisions to make it hashable.
        # We use id(self) because 'self' is not hashable.
        collisions_key = frozenset(collisions) if collisions else None
        key = (id(self), collisions_key)

        # 3. Check Cache
        if key in context_cache:
            # The cache stores (result, pinned_object). We return just the result.
            return context_cache[key][0]

        # 4. Execute the actual function
        # We ensure context_cache is passed down to the recursive calls
        result = func(self, collisions=collisions, **kwargs)

        # 5. Update Cache & Pin Object
        # We store (result, self). The reference to 'self' prevents garbage collection,
        # ensuring that 'id(self)' cannot be reused for a new object while this
        # cache entry exists.
        context_cache[key] = (result, self)
        return result

    return wrapper
