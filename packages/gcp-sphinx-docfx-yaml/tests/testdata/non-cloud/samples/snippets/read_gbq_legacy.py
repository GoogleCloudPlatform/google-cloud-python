# Copyright 2019. PyData Development Team
# Distributed under BSD 3-Clause License.
# See LICENSE.txt for details.

"""Simple query example."""

import argparse

import pandas_gbq


def main(project_id):
    # [S bigquery_pandas_gbq_read_gbq_legacy]
    sql = """
    SELECT country_name, alpha_2_code
    FROM [bigquery-public-data:utility_us.country_code_iso]
    WHERE alpha_2_code LIKE 'Z%'
    """
    df = pandas_gbq.read_gbq(
        sql,
        project_id=project_id,
        # Set the dialect to "legacy" to use legacy SQL syntax. As of
        # pandas-gbq version 0.10.0, the default dialect is "standard".
        dialect="legacy",
    )
    # [E bigquery_pandas_gbq_read_gbq_legacy]
    print(df)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id")
    args = parser.parse_args()
    main(args.project_id)
