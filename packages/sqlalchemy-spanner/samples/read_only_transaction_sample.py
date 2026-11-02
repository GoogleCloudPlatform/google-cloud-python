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

import datetime
import uuid

from model import Concert, Singer, Venue
from sample_helper import run_sample
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session


# Shows how to execute a read-only transaction on Spanner using SQLAlchemy.
def read_only_transaction_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    # First insert a few test rows that can be queried in a read-only transaction.
    insert_test_data(engine)

    # Create a session that uses a read-only transaction.
    # Read-only transactions do not take locks, and are therefore preferred
    # above read/write transactions for workloads that only read data on Spanner.
    with Session(engine.execution_options(read_only=True)) as session:
        print("Singers ordered by last name")
        singers = session.query(Singer).order_by(Singer.last_name).all()
        for singer in singers:
            print("Singer: ", singer.full_name)

        print()
        print("Singers ordered by first name")
        singers = session.query(Singer).order_by(Singer.first_name).all()
        for singer in singers:
            print("Singer: ", singer.full_name)


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
    run_sample(read_only_transaction_sample)
