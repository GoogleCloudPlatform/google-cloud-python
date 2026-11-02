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
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Shows how to map and use the DATE and TIMESTAMP data types in Spanner.
def date_and_timestamp_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    with Session(engine) as session:
        # Singer has a property birthdate, which is mapped to a DATE column.
        # Use the datetime.date type for this.
        singer = Singer(
            id=str(uuid.uuid4()),
            first_name="John",
            last_name="Doe",
            birthdate=datetime.date(1979, 10, 14),
        )
        venue = Venue(code="CH", name="Concert Hall", active=True)
        # Concert has a property `start_time`, which is mapped to a TIMESTAMP
        # column. Use the datetime.datetime type for this.
        concert = Concert(
            venue=venue,
            start_time=datetime.datetime(2024, 11, 7, 19, 30, 0),
            singer=singer,
            title="John Doe - Live in Concert Hall",
        )
        session.add_all([singer, venue, concert])
        session.commit()

        # Use AUTOCOMMIT for sessions that only read. This is more
        # efficient than using a read/write transaction to only read.
        session.connection(execution_options={"isolation_level": "AUTOCOMMIT"})
        print(
            f"{singer.full_name}, born on {singer.birthdate}, has planned "
            f"a concert that starts on {concert.start_time} in {venue.name}."
        )


if __name__ == "__main__":
    run_sample(date_and_timestamp_sample)
