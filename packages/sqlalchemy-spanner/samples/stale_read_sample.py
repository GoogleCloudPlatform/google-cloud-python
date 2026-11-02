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
from sqlalchemy import Engine, create_engine, select, text
from sqlalchemy.orm import Session


# Shows how to execute stale reads on Spanner using SQLAlchemy.
def stale_read_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    # First get the current database timestamp. We can use this timestamp to
    # query the database at a point in time where we know it was empty.
    with Session(engine.execution_options(isolation_level="AUTOCOMMIT")) as session:
        timestamp = session.execute(select(text("current_timestamp"))).one()[0]
    print(timestamp)

    # Insert a few test rows.
    insert_test_data(engine)

    # Create a session that uses a read-only transaction with a strong timestamp
    # bound. This means that it will read all data that has been committed at the
    # time this transaction starts.
    # Read-only transactions do not take locks, and are therefore preferred
    # above read/write transactions for workloads that only read data on Spanner.
    with Session(engine.execution_options(read_only=True)) as session:
        print("Found singers with strong timestamp bound:")
        singers = session.query(Singer).order_by(Singer.last_name).all()
        for singer in singers:
            print("Singer: ", singer.full_name)

    # Create a session that uses a read-only transaction that selects data in
    # the past. We'll use the timestamp that we retrieved before inserting the
    # test data for this transaction.
    with Session(
        engine.execution_options(
            read_only=True, staleness={"read_timestamp": timestamp}
        )
    ) as session:
        print("Searching for singers using a read timestamp in the past:")
        singers = session.query(Singer).order_by(Singer.last_name).all()
        if singers:
            for singer in singers:
                print("Singer: ", singer.full_name)
        else:
            print("No singers found.")

    # Spanner also supports min_read_timestamp and max_staleness as staleness
    # options. These can only be used in auto-commit mode.
    # Spanner will choose a read timestamp that satisfies the given restriction
    # and that can be served as efficiently as possible.
    with Session(
        engine.execution_options(
            isolation_level="AUTOCOMMIT", staleness={"max_staleness": {"seconds": 15}}
        )
    ) as session:
        print("Searching for singers using a max staleness of 15 seconds:")
        singers = session.query(Singer).order_by(Singer.last_name).all()
        if singers:
            for singer in singers:
                print("Singer: ", singer.full_name)
        else:
            print("No singers found.")


def insert_test_data(engine: Engine):
    with Session(engine) as session:
        session.add_all(
            [
                Singer(id=str(uuid.uuid4()), first_name="John", last_name="Doe"),
                Singer(id=str(uuid.uuid4()), first_name="Jane", last_name="Doe"),
            ]
        )
        session.commit()


if __name__ == "__main__":
    run_sample(stale_read_sample)
