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

from model import Concert, Singer, TicketSale, Venue
from sample_helper import run_sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Shows how to use a bit-reversed sequence for primary key generation.
#
# The TicketSale model uses a bit-reversed sequence for automatic primary key
# generation:
#
# id: Mapped[int] = mapped_column(
#         BigInteger,
#         Sequence("ticket_sale_id"),
#         server_default=TextClause("GET_NEXT_SEQUENCE_VALUE(SEQUENCE ticket_sale_id)"),
#         primary_key=True,
#     )
#
# This leads to the following table definition:
#
# CREATE TABLE ticket_sales (
# 	id INT64 NOT NULL DEFAULT (GET_NEXT_SEQUENCE_VALUE(SEQUENCE ticket_sale_id)),
#   ...
# ) PRIMARY KEY (id)
def bit_reversed_sequence_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    with Session(engine) as session:
        singer = Singer(id=str(uuid.uuid4()), first_name="John", last_name="Doe")
        venue = Venue(code="CH", name="Concert Hall", active=True)
        concert = Concert(
            venue=venue,
            start_time=datetime.datetime(2024, 11, 7, 19, 30, 0),
            singer=singer,
            title="John Doe - Live in Concert Hall",
        )
        # TicketSale automatically generates a primary key value using a
        # bit-reversed sequence. We therefore do not need to specify a primary
        # key value when we create an instance of TicketSale.
        ticket_sale = TicketSale(
            concert=concert, customer_name="Alice Doe", seats=["A010", "A011", "A012"]
        )
        session.add_all([singer, venue, concert, ticket_sale])
        session.commit()


if __name__ == "__main__":
    run_sample(bit_reversed_sequence_sample)
