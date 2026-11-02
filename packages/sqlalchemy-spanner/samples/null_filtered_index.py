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

from sample_helper import run_sample
from sqlalchemy import Index, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

# Shows how to create a null-filtered index.
#
# A null-filtered index does not index NULL values. This is useful for
# maintaining smaller indexes over sparse columns.
# https://cloud.google.com/spanner/docs/secondary-indexes#null-indexing-disable


class Base(DeclarativeBase):
    pass


class Singer(Base):
    __tablename__ = "singers_with_null_filtered_index"
    __table_args__ = (
        Index("uq_null_filtered_name", "name", unique=True, spanner_null_filtered=True),
    )

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str | None]


def null_filtered_index_sample():
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    Base.metadata.create_all(engine)

    # We can create singers with a name of jdoe and NULL.
    with Session(engine) as session:
        session.add(Singer(name="jdoe"))
        session.add(Singer(name=None))
        session.commit()

    # The unique index will stop us from adding another jdoe.
    with Session(engine) as session:
        session.add(Singer(name="jdoe"))
        try:
            session.commit()
        except IntegrityError:
            session.rollback()

    # The index is null filtered, so we can still add another
    # NULL name. The NULL values are not part of the index.
    with Session(engine) as session:
        session.add(Singer(name=None))
        session.commit()


if __name__ == "__main__":
    run_sample(null_filtered_index_sample)
