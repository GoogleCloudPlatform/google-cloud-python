# Copyright (c) 2019 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import itertools
import typing

import pandas


def list_columns_and_indexes(dataframe, index=True):
    """Return all index and column names with dtypes.

    Returns:
        Sequence[Tuple[str, dtype]]:
            Returns a sorted list of indexes and column names with
            corresponding dtypes. If an index is missing a name or has the
            same name as a column, the index is omitted.
    """
    column_names = frozenset(dataframe.columns)
    columns_and_indexes = []
    if index:
        if isinstance(dataframe.index, pandas.MultiIndex):
            for name in dataframe.index.names:
                if name and name not in column_names:
                    values = dataframe.index.get_level_values(
                        typing.cast(typing.Union[str, int], name)
                    )
                    columns_and_indexes.append((name, values.dtype))
        else:
            if dataframe.index.name and dataframe.index.name not in column_names:
                columns_and_indexes.append(
                    (dataframe.index.name, dataframe.index.dtype)
                )

    columns_and_indexes += zip(dataframe.columns, dataframe.dtypes)
    return columns_and_indexes


def first_valid(series):
    first_valid_index = series.first_valid_index()
    if first_valid_index is not None:
        return series.at[first_valid_index]


def first_array_valid(series):
    """Return the first "meaningful" element from the array series.

    Here, "meaningful" means the first non-None element in one of the arrays that can
    be used for type detextion.
    """
    first_valid_index = series.first_valid_index()
    if first_valid_index is None:
        return None

    valid_array = series.at[first_valid_index]
    valid_item = next((item for item in valid_array if not pandas.isna(item)), None)

    if valid_item is not None:
        return valid_item

    # Valid item is None because all items in the "valid" array are invalid. Try
    # to find a true valid array manually.
    for array in itertools.islice(series, first_valid_index + 1, None):
        try:
            array_iter = iter(array)
        except TypeError:
            continue  # Not an array, apparently, e.g. None, thus skip.
        valid_item = next((item for item in array_iter if not pandas.isna(item)), None)
        if valid_item is not None:
            break

    return valid_item
