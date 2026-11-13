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
"""Root pytest configuration for the package.

Keeps ``pytest.ini`` portable across ``pytest-asyncio`` versions by registering
``asyncio_default_fixture_loop_scope`` and ``asyncio_default_test_loop_scope``
when running under older ``pytest-asyncio`` (<0.23).
"""


def pytest_addoption(parser):
    for name, help_text in (
        (
            "asyncio_default_fixture_loop_scope",
            "default event-loop scope for asyncio fixtures (pytest-asyncio)",
        ),
        (
            "asyncio_default_test_loop_scope",
            "default event-loop scope for asyncio tests (pytest-asyncio)",
        ),
    ):
        try:
            parser.addini(name, help_text, default=None)
        except ValueError:
            pass
