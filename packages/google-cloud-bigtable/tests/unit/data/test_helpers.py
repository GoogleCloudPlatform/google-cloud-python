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
#

import pytest

from google.cloud.bigtable.helpers import batched


class TestBatched:
    @pytest.mark.parametrize(
        "input_list,batch_size,expected",
        [
            ([1, 2, 3, 4, 5], 3, [[1, 2, 3], [4, 5]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
            ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
            ([1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]),
            ([1, 2, 3, 4, 5], 5, [[1, 2, 3, 4, 5]]),
            ([], 1, []),
        ],
    )
    def test_batched(self, input_list, batch_size, expected):
        result = list(batched(input_list, batch_size))
        assert list(map(list, result)) == expected

    @pytest.mark.parametrize(
        "input_list,batch_size",
        [
            ([1], 0),
            ([1], -1),
        ],
    )
    def test_batched_errs(self, input_list, batch_size):
        with pytest.raises(ValueError):
            list(batched(input_list, batch_size))
