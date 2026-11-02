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

from model import Album, Singer, Track
from sample_helper import run_sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Shows how to use a default column with SQLAlchemy and Spanner.
def default_column_value_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    with Session(engine) as session:
        # The Track model has a `recorded_at` property that is set to
        # CURRENT_TIMESTAMP if no other value is supplied.
        singer = Singer(id=str(uuid.uuid4()), first_name="John", last_name="Doe")
        album = Album(id=str(uuid.uuid4()), title="My album", singer=singer)

        # This track will use the default CURRENT_TIMESTAMP for the recorded_at
        # property.
        track1 = Track(
            id=str(uuid.uuid4()),
            track_number=1,
            title="My track 1",
            album=album,
        )
        track2 = Track(
            id=str(uuid.uuid4()),
            track_number=2,
            title="My track 2",
            recorded_at=datetime.datetime(2024, 11, 7, 10, 0, 0),
            album=album,
        )
        session.add_all([singer, album, track1, track2])
        session.commit()
        print(f"Track 1 was recorded at: {track1.recorded_at}")
        print(f"Track 2 was recorded at: {track2.recorded_at}")


if __name__ == "__main__":
    run_sample(default_column_value_sample)
