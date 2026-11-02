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


# Shows how to transaction tags and statement tags with Spanner and SQLAlchemy.
def tags_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    # Set a transaction_tag in the execution options for the session to set
    # a transaction tag.
    with Session(
        engine.execution_options(transaction_tag="my_transaction_tag")
    ) as session:
        # The transaction that is automatically started by SQLAlchemy will use the
        # transaction tag that is specified in the execution options.

        # Execute a query with a request tag.
        singer_id = str(uuid.uuid4())
        singer = session.get(
            Singer, singer_id, execution_options={"request_tag": "my_tag_1"}
        )

        # Add the singer if it was not found.
        if singer is None:
            # The session.Add(..) function does not support execution_options, but we can
            # set the execution_options on the connection of this session. This will be
            # propagated to the next statement that is executed on the connection.
            session.connection().execution_options(request_tag="insert_singer")
            singer = Singer(id=singer_id, first_name="John", last_name="Doe")
            session.add(singer)
        session.commit()


if __name__ == "__main__":
    run_sample(tags_sample)
