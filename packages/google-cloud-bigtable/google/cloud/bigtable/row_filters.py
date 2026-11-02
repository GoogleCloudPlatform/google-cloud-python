# Copyright 2016 Google LLC
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

"""Filters for Google Cloud Bigtable Row classes."""

import struct

from google.cloud.bigtable.data.row_filters import (  # noqa: F401
    ApplyLabelFilter,
    BlockAllFilter,
    CellsColumnLimitFilter,
    CellsRowLimitFilter,
    CellsRowOffsetFilter,
    ColumnQualifierRegexFilter,
    FamilyNameRegexFilter,
    PassAllFilter,
    RowFilter,
    RowFilterChain,
    RowFilterUnion,
    RowKeyRegexFilter,
    RowSampleFilter,
    SinkFilter,
    StripValueTransformerFilter,
    TimestampRange,
    ValueBitmaskFilter,
    ValueRangeFilter,
    ValueRegexFilter,
    _BoolFilter,
    _CellCountFilter,
    _FilterCombination,
    _RegexFilter,
)
from google.cloud.bigtable.data.row_filters import (
    ColumnRangeFilter as BaseColumnRangeFilter,
)
from google.cloud.bigtable.data.row_filters import (
    ConditionalRowFilter as BaseConditionalRowFilter,
)
from google.cloud.bigtable.data.row_filters import (
    TimestampRangeFilter as BaseTimestampRangeFilter,
)
from google.cloud.bigtable.helpers import _MappableAttributesMixin

_PACK_I64 = struct.Struct(">q").pack


def _deprecated_to_pb(self):
    import warnings

    warnings.warn(
        "`to_pb()` is deprecated and will be removed in a future release. "
        "Filter objects should be passed directly to Bigtable client read and query "
        "methods without manual protobuf conversion.",
        DeprecationWarning,
        stacklevel=2,
    )
    return self._to_pb()


# Provide to_pb alias with DeprecationWarning for backwards compatibility with legacy client code
RowFilter.to_pb = _deprecated_to_pb  # type: ignore[attr-defined]
TimestampRange.to_pb = _deprecated_to_pb  # type: ignore[attr-defined]
# The classes defined below are to provide constructors and members
# that have an interface that does not match the one used by the data
# client, for backwards compatibility purposes.

# Each underscored class is an ABC. Make them into classes that can be
# instantiated with a placeholder to_dict method for consistency.


class TimestampRangeFilter(BaseTimestampRangeFilter):
    """Row filter that limits cells to a range of time.

    :type range_: :class:`TimestampRange`
    :param range_: Range of time that cells should match against.
    """

    def __init__(self, range_):
        self.range_ = range_

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(range_={self.range_!r})"


class ExactValueFilter(ValueRegexFilter):
    """Row filter for an exact value.


    :type value: bytes or str or int
    :param value:
        a literal string encodable as ASCII, or the
        equivalent bytes, or an integer (which will be packed into 8-bytes).
    """

    def __init__(self, value):
        if isinstance(value, int):
            value = _PACK_I64(value)
        super(ExactValueFilter, self).__init__(value)


class ColumnRangeFilter(_MappableAttributesMixin, BaseColumnRangeFilter):
    """A row filter to restrict to a range of columns.

    Both the start and end column can be included or excluded in the range.
    By default, we include them both, but this can be changed with optional
    flags.

    :type column_family_id: str
    :param column_family_id: The column family that contains the columns. Must
                             be of the form ``[_a-zA-Z0-9][-_.a-zA-Z0-9]*``.

    :type start_column: bytes
    :param start_column: The start of the range of columns. If no value is
                         used, the backend applies no upper bound to the
                         values.

    :type end_column: bytes
    :param end_column: The end of the range of columns. If no value is used,
                       the backend applies no upper bound to the values.

    :type inclusive_start: bool
    :param inclusive_start: Boolean indicating if the start column should be
                            included in the range (or excluded). Defaults
                            to :data:`True` if ``start_column`` is passed and
                            no ``inclusive_start`` was given.

    :type inclusive_end: bool
    :param inclusive_end: Boolean indicating if the end column should be
                          included in the range (or excluded). Defaults
                          to :data:`True` if ``end_column`` is passed and
                          no ``inclusive_end`` was given.

    :raises: :class:`ValueError <exceptions.ValueError>` if ``inclusive_start``
             is set but no ``start_column`` is given or if ``inclusive_end``
             is set but no ``end_column`` is given
    """

    _attribute_map = {
        "column_family_id": "family_id",
        "start_column": "start_qualifier",
        "end_column": "end_qualifier",
    }


class ConditionalRowFilter(_MappableAttributesMixin, BaseConditionalRowFilter):
    """Conditional row filter which exhibits ternary behavior.

    Executes one of two filters based on another filter. If the ``base_filter``
    returns any cells in the row, then ``true_filter`` is executed. If not,
    then ``false_filter`` is executed.

    .. note::

        The ``base_filter`` does not execute atomically with the true and false
        filters, which may lead to inconsistent or unexpected results.

        Additionally, executing a :class:`ConditionalRowFilter` has poor
        performance on the server, especially when ``false_filter`` is set.

    :type base_filter: :class:`RowFilter`
    :param base_filter: The filter to condition on before executing the
                        true/false filters.

    :type true_filter: :class:`RowFilter`
    :param true_filter: (Optional) The filter to execute if there are any cells
                        matching ``base_filter``. If not provided, no results
                        will be returned in the true case.

    :type false_filter: :class:`RowFilter`
    :param false_filter: (Optional) The filter to execute if there are no cells
                         matching ``base_filter``. If not provided, no results
                         will be returned in the false case.
    """

    _attribute_map = {"base_filter": "predicate_filter"}


__all__ = (
    "RowFilter",
    "SinkFilter",
    "PassAllFilter",
    "BlockAllFilter",
    "RowKeyRegexFilter",
    "RowSampleFilter",
    "FamilyNameRegexFilter",
    "ColumnQualifierRegexFilter",
    "TimestampRange",
    "TimestampRangeFilter",
    "ColumnRangeFilter",
    "ValueRegexFilter",
    "ExactValueFilter",
    "ValueRangeFilter",
    "ValueBitmaskFilter",
    "CellsRowOffsetFilter",
    "CellsRowLimitFilter",
    "CellsColumnLimitFilter",
    "StripValueTransformerFilter",
    "ApplyLabelFilter",
    "RowFilterChain",
    "RowFilterUnion",
    "ConditionalRowFilter",
)
