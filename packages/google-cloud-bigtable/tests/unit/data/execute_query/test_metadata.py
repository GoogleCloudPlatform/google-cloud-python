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
import pytest

from google.cloud.bigtable.data.execute_query.metadata import (
    _pb_metadata_to_metadata_types,
)
from google.cloud.bigtable_v2.types.data import ResultSetMetadata


def test_empty_metadata_fails_parsing():
    invalid_md_proto = ResultSetMetadata({"proto_schema": {"columns": []}})
    with pytest.raises(ValueError):
        _pb_metadata_to_metadata_types(invalid_md_proto)
