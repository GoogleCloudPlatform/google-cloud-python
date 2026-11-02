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

from sample_helper import run_sample
from sqlalchemy import create_engine, select, text


def quickstart():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database"
    )
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as connection:
        results = connection.execute(select(text("'Hello World!'"))).fetchall()
        print("\nMessage from Spanner: ", results[0][0], "\n")


if __name__ == "__main__":
    run_sample(quickstart)
