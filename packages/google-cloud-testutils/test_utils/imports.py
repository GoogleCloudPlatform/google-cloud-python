# Copyright 2019 Google LLC
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

import builtins
from unittest import mock


def maybe_fail_import(predicate):
    """Create and return a patcher that conditionally makes an import fail.

    Args:
        predicate (Callable[[...], bool]): A callable that, if it returns `True`,
            triggers an `ImportError`. It must accept the same arguments as the
            built-in `__import__` function.
            https://docs.python.org/3/library/functions.html#__import__

    Returns:
        A mock patcher object that can be used to enable patched import behavior.
    """
    orig_import = builtins.__import__

    def custom_import(name, globals=None, locals=None, fromlist=(), level=0):
        if predicate(name, globals, locals, fromlist, level):
            raise ImportError
        return orig_import(name, globals, locals, fromlist, level)

    return mock.patch.object(builtins, "__import__", new=custom_import)
