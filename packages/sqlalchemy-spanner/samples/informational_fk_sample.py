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

import datetime
import uuid

from model import Concert, Singer, TicketSale, Venue
from sample_helper import run_sample
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


# Shows how to create a non-enforced foreign key.
#
# The TicketSale model contains two foreign keys that are not enforced by Spanner.
# This allows the related records to be deleted without the need to delete the
# corresponding TicketSale record.
#
#     __table_args__ = (
#         ForeignKeyConstraint(
#             ["venue_code", "start_time", "singer_id"],
#             ["concerts.venue_code", "concerts.start_time", "concerts.singer_id"],
#             spanner_not_enforced=True,
#         ),
#     )
#     singer_id: Mapped[str] = mapped_column(String(36), ForeignKey("singers.id", spanner_not_enforced=True))
#
# See https://cloud.google.com/spanner/docs/foreign-keys/overview#informational-foreign-keys
# for more information on informational foreign key constrains.
def informational_fk_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    # First create a singer, venue, concert and ticket_sale.
    singer_id = str(uuid.uuid4())
    ticket_sale_id = None
    with Session(engine) as session:
        singer = Singer(id=singer_id, first_name="John", last_name="Doe")
        venue = Venue(code="CH", name="Concert Hall", active=True)
        concert = Concert(
            venue=venue,
            start_time=datetime.datetime(2024, 11, 7, 19, 30, 0),
            singer=singer,
            title="John Doe - Live in Concert Hall",
        )
        ticket_sale = TicketSale(
            concert=concert, customer_name="Alice Doe", seats=["A010", "A011", "A012"]
        )
        session.add_all([singer, venue, concert, ticket_sale])
        session.commit()
        ticket_sale_id = ticket_sale.id

    # Now delete both the singer and concert that are referenced by the ticket_sale record.
    # This is possible as the foreign key constraints between ticket_sales and singers/concerts
    # are not enforced.
    with Session(engine) as session:
        session.delete(concert)
        session.delete(singer)
        session.commit()

    # Verify that the ticket_sale record still exists, while the concert and singer have been
    # deleted.
    with Session(engine) as session:
        ticket_sale = session.get(TicketSale, ticket_sale_id)
        singer = session.get(Singer, singer_id)
        concert = session.get(
            Concert, ("CH", datetime.datetime(2024, 11, 7, 19, 30, 0), singer_id)
        )
        print(
            "Ticket sale found: {}\nSinger found: {}\nConcert found: {}\n".format(
                ticket_sale is not None, singer is not None, concert is not None
            )
        )


if __name__ == "__main__":
    run_sample(informational_fk_sample)
