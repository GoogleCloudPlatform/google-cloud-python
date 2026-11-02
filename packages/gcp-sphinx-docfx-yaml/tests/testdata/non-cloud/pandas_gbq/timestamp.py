# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Helpers for working with TIMESTAMP data type.

Private module.
"""

import pandas.api.types


def localize_df(df, schema_fields):
    """Localize any TIMESTAMP columns to tz-aware type.

    In pandas versions before 0.24.0, DatetimeTZDtype cannot be used as the
    dtype in Series/DataFrame construction, so localize those columns after
    the DataFrame is constructed.

    Parameters
    ----------
    schema_fields: sequence of dict
        BigQuery schema in parsed JSON data format.
    df: pandaas.DataFrame
        DataFrame in which to localize TIMESTAMP columns.


    Returns
    -------
    pandas.DataFrame
        DataFrame with localized TIMESTAMP columns.
    """
    for field in schema_fields:
        column = str(field["name"])
        if "mode" in field and field["mode"].upper() == "REPEATED":
            continue

        if (
            field["type"].upper() == "TIMESTAMP"
            and pandas.api.types.is_datetime64_ns_dtype(df.dtypes[column])
            and df[column].dt.tz is None
        ):
            df[column] = df[column].dt.tz_localize("UTC")

    return df
