# Copyright 2019. PyData Development Team
# Distributed under BSD 3-Clause License.
# See LICENSE.txt for details.

"""Simple query example."""

import argparse


def main(project_id):
    # [S bigquery_pandas_gbq_read_gbq_simple]
    import pandas_gbq

    # TODO: Set project_id to your Google Cloud Platform project ID.
    # project_id = "my-project"

    sql = """
    SELECT country_name, alpha_2_code
    FROM `bigquery-public-data.utility_us.country_code_iso`
    WHERE alpha_2_code LIKE 'A%'
    """
    df = pandas_gbq.read_gbq(sql, project_id=project_id)
    # [E bigquery_pandas_gbq_read_gbq_simple]
    print(df)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id")
    args = parser.parse_args()
    main(args.project_id)
