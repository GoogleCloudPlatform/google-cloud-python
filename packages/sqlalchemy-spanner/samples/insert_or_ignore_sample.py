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

import uuid

from model import Singer
from sample_helper import run_sample
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from google.cloud.sqlalchemy_spanner.dml import insert_or_ignore


# Shows how to use insert-or-ignore using SQLAlchemy and Spanner.
def insert_or_ignore_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    with Session(engine) as session:
        stmt = (
            insert_or_ignore(Singer)
            .values(
                id=str(uuid.uuid4()),
                first_name="John",
                last_name="Smith",
            )
            .returning(Singer.id)
        )
        singer_id = session.execute(stmt).scalar()
        print(singer_id)

        # Use AUTOCOMMIT for sessions that only read. This is more
        # efficient than using a read/write transaction to only read.
        session.connection(execution_options={"isolation_level": "AUTOCOMMIT"})
        stmt = select(Singer).where(Singer.id == singer_id)
        singer = session.execute(stmt).scalar()
        print(f"Inserted or ignored singer {singer.full_name} successfully")


if __name__ == "__main__":
    run_sample(insert_or_ignore_sample)
