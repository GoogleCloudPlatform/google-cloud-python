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

from model import Venue
from sample_helper import run_sample
from sqlalchemy import create_engine, func, text
from sqlalchemy.orm import Session


# Shows how to use the PARSE_JSON function in Spanner using SQLAlchemy.
def parse_json_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    with Session(engine) as session:
        venue = Venue(
            code="LCH",
            active=True,
            name="Large Concert Hall",
            # The SQLAlchemy func function is very lenient and allows you to call any
            # database function that Spanner supports. Use a text instance to add a
            # specific SQL fragment to the function call.
            description=func.parse_json(
                '{"type": "Stadium", "size": 13.7391432}',
                text("wide_number_mode=>'round'"),
            ),
        )
        session.add(venue)
        session.commit()

        venue = session.query(Venue).filter_by(code="LCH").one()
        print(venue.description)


if __name__ == "__main__":
    run_sample(parse_json_sample)
