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
from google.cloud.bigtable.data._metrics.handlers._base import MetricsHandler
from google.cloud.bigtable.data.mutations import DeleteAllFromRow, SetCell

from . import _harness

if CrossSync.is_async:
    from ._base_async import AcceleratorTestBaseAsync as AcceleratorTestBase
else:
    from ._base_autogen import AcceleratorTestBase

__CROSS_SYNC_OUTPUT__ = "tests.system.data.accelerator.test_metrics_parity_autogen"


@CrossSync.convert_class(sync_name="TestMetricsParity")
class TestMetricsParityAsync(AcceleratorTestBase):
    @CrossSync.pytest
    async def test_accelerated_ops_bypass_python_metrics(self, instance_id, table_id):
        ah, nh, a_ops, n_ops = MetricsHandler(), MetricsHandler(), [], []
        ah.on_operation_complete, nh.on_operation_complete = a_ops.append, n_ops.append
        async with (
            self._make_client(use_accelerator=True) as ac,
            self._make_client(use_accelerator=False) as nc,
        ):
            async with (
                ac.get_table(instance_id, table_id) as accel_table,
                nc.get_table(instance_id, table_id) as native_table,
            ):
                self.assert_accelerator_active(accel_table)
                self.assert_native(native_table)
                accel_table.client._metrics.add_handler(ah)
                native_table.client._metrics.add_handler(nh)
                key = f"metrics-{uuid.uuid4().hex}".encode()
                for t in (accel_table, native_table):
                    await t.mutate_row(
                        key,
                        SetCell(
                            _harness.TEST_FAMILY,
                            b"q",
                            b"v",
                            timestamp_micros=1000 * _harness.MS,
                        ),
                    )
                    await t.read_row(key)
                    await t.mutate_row(key, DeleteAllFromRow())
        assert len(n_ops) >= 2 and len(a_ops) == 0
