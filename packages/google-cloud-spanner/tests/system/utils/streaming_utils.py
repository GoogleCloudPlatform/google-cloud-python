# Copyright 2017 Google LLC
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

import collections
import os

INSTANCE_NAME = "gcp-streaming-systests"
DATABASE_NAME = "testing"
_SHOULD_PRINT = os.getenv("GOOGLE_CLOUD_NO_PRINT") != "true"


class _TableDesc(
    collections.namedtuple(
        "TableDesc", ("table", "row_count", "value_size", "column_count")
    )
):
    def value(self):
        return "X" * self.value_size


FOUR_KAY = _TableDesc("four_kay", 1000, 4096, 1)
FORTY_KAY = _TableDesc("forty_kay", 100, 4096 * 10, 1)
FOUR_HUNDRED_KAY = _TableDesc("four_hundred_kay", 25, 4096 * 100, 1)
FOUR_MEG = _TableDesc("four_meg", 10, 2048 * 1024, 2)


def print_func(message):
    if _SHOULD_PRINT:
        print(message)
