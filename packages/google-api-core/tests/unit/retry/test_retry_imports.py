# Copyright 2024 Google LLC
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


def test_legacy_imports_retry_unary_sync():
    # TODO: Delete this test when when we revert these imports on the
    #       next major version release
    #       (https://github.com/googleapis/python-api-core/issues/576)
    from google.api_core.retry import (  # noqa: F401
        auth_exceptions,
        datetime_helpers,
        exceptions,
    )


def test_legacy_imports_retry_unary_async():
    # TODO: Delete this test when when we revert these imports on the
    #       next major version release
    #       (https://github.com/googleapis/python-api-core/issues/576)
    from google.api_core import retry_async  # noqa: F401

    # See https://github.com/googleapis/python-api-core/issues/586
    # for context on why we need to test this import this explicitly.
    from google.api_core.retry_async import AsyncRetry  # noqa: F401
