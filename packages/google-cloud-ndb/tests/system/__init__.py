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
import operator
import time

KIND = "SomeKind"
OTHER_KIND = "OtherKind"


def eventually(f, predicate, timeout=120, interval=2):
    """Runs `f` in a loop, hoping for eventual success.

    Some things we're trying to test in Datastore are eventually
    consistent-we'll write something to the Datastore and can read back out
    data, eventually. This is particularly true for metadata, where we can
    write an entity to Datastore and it takes some amount of time for metadata
    about the entity's "kind" to update to match the new data just written,
    which can be challenging for system testing.

    With `eventually`, you can pass in a callable `predicate` which can tell us
    whether the Datastore is now in a consistent state, at least for the piece
    we're trying to test. This function will call the predicate repeatedly in a
    loop until it either returns `True` or `timeout` is exceeded.

    Args:
        f (Callable[[], Any]): A function to be called. Its result will be
            passed to ``predicate`` to determine success or failure.
        predicate (Callable[[Any], bool]): A function to be called with the
            result of calling ``f``. A return value of :data:`True` indicates a
            consistent state and will cause `eventually` to return so execution
            can proceed in the calling context.
        timeout (float): Time in seconds to wait for predicate to return
            `True`. After this amount of time, `eventually` will return
            regardless of `predicate` return value.
        interval (float): Time in seconds to wait in between invocations of
            `predicate`.

    Returns:
        Any: The return value of ``f``.

    Raises:
        AssertionError: If ``predicate`` fails to return :data:`True` before
            the timeout has expired.
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        value = f()
        if predicate(value):
            return value
        time.sleep(interval)

    assert predicate(value)


def length_equals(n):
    """Returns predicate that returns True if passed a sequence of length `n`.

    For use with `eventually`.
    """

    def predicate(sequence):
        return len(sequence) == n

    return predicate


def equals(n):
    """Returns predicate that returns True if passed `n`.

    For use with `eventually`.
    """
    return functools.partial(operator.eq, n)
