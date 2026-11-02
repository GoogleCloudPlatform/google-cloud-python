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

import types

from google.cloud.ndb import tasklets


def verify___all__(module_obj):
    expected = []
    for name in dir(module_obj):
        if not name.startswith("_"):
            value = getattr(module_obj, name)
            if not isinstance(value, types.ModuleType):
                expected.append(name)
    expected.sort(key=str.lower)
    actual = sorted(module_obj.__all__, key=str.lower)
    if actual != expected:
        print("In __all__ but not expected:", set(actual) - set(expected))
        print("In expected but not __all__:", set(expected) - set(actual))
    assert actual == expected


def future_result(result):
    """Return a future with the given result."""
    future = tasklets.Future()
    future.set_result(result)
    return future


def future_exception(exception):
    """Return a future with the given result."""
    future = tasklets.Future()
    future.set_exception(exception)
    return future


def future_results(*results):
    """Return a sequence of futures for the given results."""
    return [future_result(result) for result in results]
