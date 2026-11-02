# Copyright 2025 Google LLC All rights reserved.
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

import uuid

from model import Singer
from sample_helper import run_sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Shows how to set the isolation level for a read/write transaction.
# Spanner supports the following isolation levels:
# - SERIALIZABLE (default)
# - REPEATABLE READ
def isolation_level_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        # You can set a default isolation level for an engine.
        isolation_level="REPEATABLE READ",
        echo=True,
    )
    # You can override the default isolation level of the connection
    # by setting it in the execution_options.
    with Session(engine.execution_options(isolation_level="SERIALIZABLE")) as session:
        singer_id = str(uuid.uuid4())
        singer = Singer(id=singer_id, first_name="John", last_name="Doe")
        session.add(singer)
        session.commit()


if __name__ == "__main__":
    run_sample(isolation_level_sample)
