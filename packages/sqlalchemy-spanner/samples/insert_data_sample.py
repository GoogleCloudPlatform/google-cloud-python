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

from model import Album, Singer, Track
from sample_helper import run_sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Shows how to insert data using SQLAlchemy, including relationships that are
# defined both as foreign keys and as interleaved tables.
def insert_data():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    with Session(engine) as session:
        singer = Singer(
            id=str(uuid.uuid4()),
            first_name="John",
            last_name="Smith",
            albums=[
                Album(
                    id=str(uuid.uuid4()),
                    title="Rainforest",
                    tracks=[
                        # Track is INTERLEAVED IN PARENT Album, but can be treated
                        # as a normal relationship in SQLAlchemy.
                        Track(track_number=1, title="Green"),
                        Track(track_number=2, title="Blue"),
                        Track(track_number=3, title="Yellow"),
                    ],
                ),
                Album(
                    id=str(uuid.uuid4()),
                    title="Butterflies",
                    tracks=[
                        Track(track_number=1, title="Purple"),
                        Track(track_number=2, title="Cyan"),
                        Track(track_number=3, title="Mauve"),
                    ],
                ),
            ],
        )
        session.add(singer)
        session.commit()

        # Use AUTOCOMMIT for sessions that only read. This is more
        # efficient than using a read/write transaction to only read.
        session.connection(execution_options={"isolation_level": "AUTOCOMMIT"})
        print(
            f"Inserted singer {singer.full_name} with {len(singer.albums)} "
            f"albums successfully"
        )


if __name__ == "__main__":
    run_sample(insert_data)
