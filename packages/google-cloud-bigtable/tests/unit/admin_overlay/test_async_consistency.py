# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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

from unittest import mock

import pytest

from google.cloud.bigtable_admin_v2.overlay.types import async_consistency
from google.cloud.bigtable_admin_v2.types import bigtable_table_admin

TRUE_CONSISTENCY_RESPONSE = bigtable_table_admin.CheckConsistencyResponse(
    consistent=True
)

FALSE_CONSISTENCY_RESPONSE = bigtable_table_admin.CheckConsistencyResponse(
    consistent=False
)


def async_mock_check_consistency_callable(max_poll_count=1):
    # Return False max_poll_count - 1 times, then True, for a total of
    # max_poll_count calls.
    side_effect = [FALSE_CONSISTENCY_RESPONSE] * (max_poll_count - 1)
    side_effect.append(TRUE_CONSISTENCY_RESPONSE)
    return mock.AsyncMock(spec=["__call__"], side_effect=side_effect)


@pytest.mark.asyncio
async def test_check_consistency_future_cancel():
    check_consistency_call = async_mock_check_consistency_callable()
    future = async_consistency._AsyncCheckConsistencyPollingFuture(
        check_consistency_call
    )
    with pytest.raises(NotImplementedError):
        future.cancel()

    with pytest.raises(NotImplementedError):
        future.cancelled()


@pytest.mark.asyncio
async def test_check_consistency_future_result():
    times = 5
    check_consistency_call = async_mock_check_consistency_callable(times)
    future = async_consistency._AsyncCheckConsistencyPollingFuture(
        check_consistency_call
    )
    is_consistent = await future.result()

    assert is_consistent
    check_consistency_call.assert_has_calls([mock.call()] * times)

    # Check that calling result again doesn't produce more calls.
    is_consistent = future.result()

    assert is_consistent
    check_consistency_call.assert_has_calls([mock.call()] * times)
