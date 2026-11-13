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

import uuid

from google.cloud.bigtable.data._cross_sync import CrossSync
from google.cloud.bigtable.data.mutations import SetCell

from . import _harness

if CrossSync.is_async:
    from ._base_async import AcceleratorTestBaseAsync as AcceleratorTestBase
else:
    from ._base_autogen import AcceleratorTestBase

__CROSS_SYNC_OUTPUT__ = (
    "tests.system.data.accelerator.test_default_and_fallback_autogen"
)


@CrossSync.convert_class(sync_name="TestDefaultAndFallback")
class TestDefaultAndFallbackAsync(AcceleratorTestBase):
    @CrossSync.pytest
    async def test_default_enables_accelerator(self, default_table, janitor):
        assert default_table._accelerator_client is not None
        key = janitor.track(f"contract-{uuid.uuid4().hex}".encode())
        await default_table.mutate_row(
            key,
            SetCell(
                _harness.TEST_FAMILY, b"q", b"v", timestamp_micros=1000 * _harness.MS
            ),
        )
        assert (await default_table.read_row(key)).cells[0].value == b"v"

    @CrossSync.pytest
    async def test_explicit_false_uses_native(self, native_table, janitor):
        assert (
            native_table._accelerator_client is None
            and native_table._accelerator_daemon is None
        )
        key = janitor.track(f"contract-{uuid.uuid4().hex}".encode())
        await native_table.mutate_row(
            key,
            SetCell(
                _harness.TEST_FAMILY, b"q", b"v", timestamp_micros=1000 * _harness.MS
            ),
        )
        assert (await native_table.read_row(key)).cells[0].value == b"v"
