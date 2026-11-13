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

from sqlalchemy import types
from sqlalchemy.testing import eq_, fixtures

from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner import SpannerDialect, _type_map


class TokenlistTest(fixtures.TestBase):
    def test_tokenlist_reflection_type_mapping(self):
        """Test mockserver reflection mapping for TOKENLIST columns."""
        dialect = SpannerDialect()
        eq_(_type_map.get("TOKENLIST"), types.String)
        col_type = dialect._designate_type("TOKENLIST")
        eq_(col_type, types.String)
