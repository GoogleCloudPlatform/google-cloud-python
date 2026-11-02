# Copyright 2024 Google LLC All rights reserved.
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

from google.cloud.spanner_dbapi.parsed_statement import AutocommitDmlMode
from sample_helper import run_sample
from sqlalchemy import create_engine, text


# Shows how to use Partitioned DML using SQLAlchemy and Spanner.
def partitioned_dml_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    # Get a connection in auto-commit mode.
    # Partitioned DML can only be executed in auto-commit mode, as each
    # Partitioned DML transaction can only consist of one statement.
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
        # Set the DML mode to PARTITIONED_NON_ATOMIC.
        connection.connection.set_autocommit_dml_mode(
            AutocommitDmlMode.PARTITIONED_NON_ATOMIC
        )
        # Use a bulk update statement to back-fill a column.
        lower_bound_rowcount = connection.execute(
            text("update venues set active=true where active is null")
        ).rowcount
        # Partitioned DML returns the lower-bound update count.
        print("Updated at least ", lower_bound_rowcount, " venue records")


if __name__ == "__main__":
    run_sample(partitioned_dml_sample)
