# Copyright 2018 Google LLC
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

"""User-friendly container for Google Cloud Bigtable RowSet"""

from google.cloud._helpers import _to_bytes  # type: ignore

from google.cloud.bigtable.data.read_rows_query import (
    ReadRowsQuery,
)
from google.cloud.bigtable.data.read_rows_query import (
    RowRange as BaseRowRange,
)
from google.cloud.bigtable.helpers import _MappableAttributesMixin


def _calculate_prefix_end_key(prefix: bytes) -> bytes | None:
    """Calculates the exclusive upper bound for a prefix scan by incrementing the last byte.

    Trailing 0xFF bytes roll over. Returns None if prefix consists entirely of 0xFF (no upper bound).
    """
    stripped = prefix.rstrip(b"\xff")
    if not stripped:
        return None
    return stripped[:-1] + bytes([stripped[-1] + 1])


class RowSet(object):
    """Convenience wrapper of google.bigtable.v2.RowSet

    Useful for creating a set of row keys and row ranges, which can
    be passed to read_rows method of class:`.Table.read_rows`.
    """

    def __init__(self):
        self._read_rows_query = ReadRowsQuery()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._read_rows_query == other._read_rows_query

    def __ne__(self, other):
        return not self == other

    @property
    def row_keys(self):
        return self._read_rows_query.row_keys

    @property
    def row_ranges(self):
        return self._read_rows_query.row_ranges

    def add_row_key(self, row_key):
        """Add row key to row_keys list.

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_api_add_row_key]
            :end-before: [END bigtable_api_add_row_key]
            :dedent: 4

        :type row_key: bytes
        :param row_key: The key of a row to read
        """
        self._read_rows_query.add_key(row_key)

    def add_row_range(self, row_range):
        """Add row_range to row_ranges list.

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_api_add_row_range]
            :end-before: [END bigtable_api_add_row_range]
            :dedent: 4

        :type row_range: class:`RowRange`
        :param row_range: The row range object having start and end key
        """
        self._read_rows_query.add_range(row_range)

    def add_row_range_from_keys(
        self, start_key=None, end_key=None, start_inclusive=True, end_inclusive=False
    ):
        """Add row range to row_ranges list from the row keys

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_api_row_range_from_keys]
            :end-before: [END bigtable_api_row_range_from_keys]
            :dedent: 4

        :type start_key: bytes
        :param start_key: (Optional) Start key of the row range. If left empty,
                          will be interpreted as the empty string.

        :type end_key: bytes
        :param end_key: (Optional) End key of the row range. If left empty,
                        will be interpreted as the empty string and range will
                        be unbounded on the high end.

        :type start_inclusive: bool
        :param start_inclusive: (Optional) Whether the ``start_key`` should be
                        considered inclusive. The default is True (inclusive).

        :type end_inclusive: bool
        :param end_inclusive: (Optional) Whether the ``end_key`` should be
                  considered inclusive. The default is False (exclusive).
        """
        row_range = RowRange(start_key, end_key, start_inclusive, end_inclusive)
        self._read_rows_query.add_range(row_range)

    def add_row_range_with_prefix(self, row_key_prefix):
        """Add row range to row_ranges list that start with the row_key_prefix from the row keys

        For example:

        .. literalinclude:: snippets_table.py
            :start-after: [START bigtable_api_add_row_range_with_prefix]
            :end-before: [END bigtable_api_add_row_range_with_prefix]

        :type row_key_prefix: str | bytes
        :param row_key_prefix: To retrieve  all rows that start with this row key prefix.
                            Prefix cannot be zero length."""

        prefix_bytes = _to_bytes(row_key_prefix, encoding="utf-8")
        if not prefix_bytes:
            raise ValueError("row_key_prefix cannot be empty.")
        end_key = _calculate_prefix_end_key(prefix_bytes)
        self.add_row_range_from_keys(prefix_bytes, end_key)


class RowRange(_MappableAttributesMixin, BaseRowRange):
    """Convenience wrapper of google.bigtable.v2.RowRange

    :type start_key: str | bytes
    :param start_key: (Optional) Start key of the row range. If left empty,
                      will be interpreted as the empty string.

    :type end_key: str | bytes
    :param end_key: (Optional) End key of the row range. If left empty,
                    will be interpreted as the empty string and range will
                    be unbounded on the high end.

    :type start_inclusive: bool
    :param start_inclusive: (Optional) Whether the ``start_key`` should be
                  considered inclusive. The default is True (inclusive).

    :type end_inclusive: bool
    :param end_inclusive: (Optional) Whether the ``end_key`` should be
                  considered inclusive. The default is False (exclusive).
    """

    _attribute_map = {
        "start_inclusive": "start_is_inclusive",
        "end_inclusive": "end_is_inclusive",
    }

    def get_range_kwargs(self):
        """Convert row range object to dict which can be passed to
        google.bigtable.v2.RowRange add method.
        """
        range_kwargs = {}
        if self.start_key is not None:
            key = "start_key_closed" if self.start_is_inclusive else "start_key_open"
            range_kwargs[key] = self.start_key
        if self.end_key is not None:
            key = "end_key_closed" if self.end_is_inclusive else "end_key_open"
            range_kwargs[key] = self.end_key
        return range_kwargs
