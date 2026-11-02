# Copyright (c) 2021 The PyBigQuery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import pytest

geoalchemy2 = pytest.importorskip("geoalchemy2")


def test_geoalchemy2_core(bigquery_dataset):
    """Make sure GeoAlchemy 2 Core Tutorial works as adapted to only having geography

    https://geoalchemy-2.readthedocs.io/en/latest/core_tutorial.html

    Note:

    - Bigquery doesn't have ST_BUFFER
    """

    # Connect to the DB

    from sqlalchemy import create_engine

    engine = create_engine(f"bigquery:///{bigquery_dataset}")

    # Create the Table

    from sqlalchemy import Column, MetaData, String, Table

    from sqlalchemy_bigquery import GEOGRAPHY, WKT

    metadata = MetaData()
    lake_table = Table(
        "lake", metadata, Column("name", String), Column("geog", GEOGRAPHY)
    )

    lake_table.create(engine)

    # Insertions

    conn = engine.connect()

    conn.execute(
        lake_table.insert().values(
            name="Majeur",
            geog="POLYGON((0 0,1 0,1 1,0 1,0 0))",
        )
    )

    conn.execute(
        lake_table.insert(),
        [
            {"name": "Garde", "geog": "POLYGON((1 0,3 0,3 2,1 2,1 0))"},
            {"name": "Orta", "geog": "POLYGON((3 0,6 0,6 3,3 3,3 0))"},
        ],
    )

    # Selections

    from sqlalchemy.sql import select

    assert sorted(
        (r.name, r.geog.desc[:4]) for r in conn.execute(select(lake_table))
    ) == [("Garde", "0103"), ("Majeur", "0103"), ("Orta", "0103")]

    # Spatial query

    from sqlalchemy import func

    [[result]] = conn.execute(
        select(lake_table.c.name).where(
            func.ST_Contains(lake_table.c.geog, WKT("POINT(4 1)"))
        )
    )
    assert result == "Orta"

    assert sorted(
        (r.name, int(r.area))
        for r in conn.execute(
            select(lake_table.c.name, lake_table.c.geog.ST_AREA().label("area"))
        )
    ) == [("Garde", 49452374328), ("Majeur", 12364036567), ("Orta", 111253664228)]

    # Extra: Make sure we can save a retrieved value back:

    [[geog]] = conn.execute(
        select(lake_table.c.geog).where(lake_table.c.name == "Garde")
    )
    conn.execute(lake_table.insert().values(name="test", geog=geog))
    assert (
        int(
            list(
                conn.execute(
                    select(lake_table.c.geog.st_area()).where(
                        lake_table.c.name == "test"
                    )
                )
            )[0][0]
        )
        == 49452374328
    )

    # and, while we're at it, that we can insert WKTs, although we
    # normally wouldn't want to.
    conn.execute(
        lake_table.insert().values(
            name="test2",
            geog=WKT("POLYGON((1 0,3 0,3 2,1 2,1 0))"),
        )
    )
    assert (
        int(
            list(
                conn.execute(
                    select(lake_table.c.geog.st_area()).where(
                        lake_table.c.name == "test2"
                    )
                )
            )[0][0]
        )
        == 49452374328
    )


def test_geoalchemy2_orm(bigquery_dataset):
    """Make sure GeoAlchemy 2 ORM Tutorial works as adapted to only having geometry

    https://geoalchemy-2.readthedocs.io/en/latest/orm_tutorial.html
    """

    # Connect to the DB

    from sqlalchemy import create_engine

    engine = create_engine(f"bigquery:///{bigquery_dataset}")

    # Declare a Mapping

    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    from sqlalchemy_bigquery import GEOGRAPHY, WKT

    Base = declarative_base()

    class Lake(Base):
        __tablename__ = "lake"
        # The ORM insists on an id, but bigquery doesn't auto-assign
        # ids, so we'll have to provide them below.
        id = Column(Integer, primary_key=True)
        name = Column(String)
        geog = Column(GEOGRAPHY)

    # Create the Table in the Database

    Lake.__table__.create(engine)

    # Create an Instance of the Mapped Class

    lake = Lake(id=1, name="Majeur", geog="POLYGON((0 0,1 0,1 1,0 1,0 0))")

    # Create a Session

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)

    session = Session()

    # Add New Objects

    session.add(lake)
    session.commit()

    our_lake = session.query(Lake).filter_by(name="Majeur").first()
    assert our_lake.name == "Majeur"

    from geoalchemy2 import WKBElement

    assert isinstance(our_lake.geog, WKBElement)

    session.add_all(
        [
            Lake(id=2, name="Garde", geog="POLYGON((1 0,3 0,3 2,1 2,1 0))"),
            Lake(id=3, name="Orta", geog="POLYGON((3 0,6 0,6 3,3 3,3 0))"),
        ]
    )

    session.commit()

    # Query

    query = session.query(Lake).order_by(Lake.name)
    assert [lake.name for lake in query] == ["Garde", "Majeur", "Orta"]

    assert [lake.name for lake in session.query(Lake).order_by(Lake.name).all()] == [
        "Garde",
        "Majeur",
        "Orta",
    ]

    # Make Spatial Queries

    from sqlalchemy import func

    query = session.query(Lake).filter(func.ST_Contains(Lake.geog, WKT("POINT(4 1)")))

    assert [lake.name for lake in query] == ["Orta"]

    query = (
        session.query(Lake)
        .filter(Lake.geog.ST_Intersects(WKT("LINESTRING(2 1,4 1)")))
        .order_by(Lake.name)
    )
    assert [lake.name for lake in query] == ["Garde", "Orta"]

    lake = session.query(Lake).filter_by(name="Garde").one()
    assert session.scalar(lake.geog.ST_Intersects(WKT("LINESTRING(2 1,4 1)")))

    # Use Other Spatial Functions
    query = session.query(Lake.name, func.ST_Area(Lake.geog).label("area")).order_by(
        Lake.name
    )
    assert [(name, int(area)) for name, area in query] == [
        ("Garde", 49452374328),
        ("Majeur", 12364036567),
        ("Orta", 111253664228),
    ]

    query = session.query(Lake.name, Lake.geog.ST_Area().label("area")).order_by(
        Lake.name
    )
    assert [(name, int(area)) for name, area in query] == [
        ("Garde", 49452374328),
        ("Majeur", 12364036567),
        ("Orta", 111253664228),
    ]


def test_geoalchemy2_orm_w_relationship(bigquery_dataset):
    from sqlalchemy import create_engine

    engine = create_engine(f"bigquery:///{bigquery_dataset}")

    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base

    from sqlalchemy_bigquery import GEOGRAPHY

    Base = declarative_base()

    class Treasure(Base):
        __tablename__ = "treasure"
        id = Column(Integer, primary_key=True)
        geog = Column(GEOGRAPHY)

    Treasure.__table__.create(engine)

    from sqlalchemy.orm import backref, relationship

    class Lake(Base):
        __tablename__ = "lake"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        geog = Column(GEOGRAPHY)
        treasures = relationship(
            "Treasure",
            primaryjoin="func.ST_Contains(foreign(Lake.geog), Treasure.geog).as_comparison(1, 2)",
            backref=backref("lake_rel", uselist=False),
            viewonly=True,
            uselist=True,
        )

    Lake.__table__.create(engine)

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)

    session = Session()

    session.add_all(
        [
            Treasure(id=21, geog="Point(1.5 1)"),
            Treasure(id=22, geog="Point(2.5 1.5)"),
            Treasure(id=31, geog="Point(4.5 2)"),
            Treasure(id=42, geog="Point(5.5 1.5)"),
            Lake(id=2, name="Garde", geog="POLYGON((1 0,3 0,3 2,1 2,1 0))"),
            Lake(id=3, name="Orta", geog="POLYGON((3 0,6 0,6 3,3 3,3 0))"),
        ]
    )

    session.commit()

    lakes = session.query(Lake).order_by(Lake.name).all()
    assert [(lake.id, sorted(t.id for t in lake.treasures)) for lake in lakes] == [
        (2, [21, 22]),
        (3, [31, 42]),
    ]
