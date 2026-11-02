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
import os
from typing import Optional

import pytest
from sqlalchemy import (
    BIGINT,
    Boolean,
    Column,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    delete,
    event,
    inspect,
    select,
    text,
    update,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.testing import eq_, is_none, is_not_none, is_true
from sqlalchemy.testing.plugin.plugin_base import fixtures
from sqlalchemy.types import REAL


class TestBasics(fixtures.TablesTest):
    @classmethod
    def define_tables(cls, metadata):
        numbers = Table(
            "numbers",
            metadata,
            Column("number", Integer),
            Column("name", String(20)),
            Column("alternative_name", String(20)),
            Column("prime", Boolean, server_default=text("FALSE")),
            Column("ln", REAL),
            PrimaryKeyConstraint("number"),
        )
        Index(
            "idx_numbers_name",
            numbers.c.name,
            numbers.c.prime.desc(),
            spanner_storing=[numbers.c.alternative_name],
        )
        Table(
            "users",
            metadata,
            Column("ID", Integer, primary_key=True),
            Column("name", String(20)),
        )
        # Add a foreign key example.
        Table(
            "number_colors",
            metadata,
            Column("ID", Integer, primary_key=True),
            Column(
                "number_id", Integer, ForeignKey("numbers.number", name="number_fk")
            ),
            Column("color", String(20)),
        )

        with cls.bind.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS schema"))
        Table(
            "users",
            metadata,
            Column("ID", Integer, primary_key=True),
            Column("name", String(20)),
            schema="schema",
        )
        # Add a foreign key example which crosses schema.
        Table(
            "number_colors",
            metadata,
            Column("ID", Integer, primary_key=True),
            Column(
                "number_id",
                Integer,
                ForeignKey("numbers.number", name="cross_schema_number_fk"),
            ),
            Column("color", String(20)),
            schema="schema",
        )
        # Add a composite primary key & foreign key example.
        Table(
            "composite_pk",
            metadata,
            Column("a", String, primary_key=True),
            Column("b", String, primary_key=True),
        )
        composite_fk = Table(
            "composite_fk",
            metadata,
            Column("my_a", String, primary_key=True),
            Column("my_b", String, primary_key=True),
            Column("my_c", String, primary_key=True),
            ForeignKeyConstraint(
                ["my_a", "my_b"],
                ["composite_pk.a", "composite_pk.b"],
                name="composite_fk_composite_pk_a_b",
            ),
        )
        Index(
            "idx_composte_fk_all",
            composite_fk.c.my_a,
            composite_fk.c.my_b,
            composite_fk.c.my_c,
        )

    def test_hello_world(self, connection):
        greeting = connection.execute(text("select 'Hello World'"))
        eq_("Hello World", greeting.fetchone()[0])

    def test_insert_number(self, connection):
        connection.execute(
            text(
                """insert or update into numbers (number, name, prime, ln)
                   values (1, 'One', false, cast(ln(1) as float32))"""
            )
        )
        name = connection.execute(text("select name from numbers where number=1"))
        eq_("One", name.fetchone()[0])

    def test_reflect(self, connection):
        engine = connection.engine
        meta: MetaData = MetaData()
        meta.reflect(bind=engine)
        eq_(5, len(meta.tables))
        table = meta.tables["numbers"]
        eq_(5, len(table.columns))
        eq_("number", table.columns[0].name)
        eq_(BIGINT, type(table.columns[0].type))
        is_none(table.columns[0].server_default)
        eq_("name", table.columns[1].name)
        eq_(String, type(table.columns[1].type))
        eq_("alternative_name", table.columns[2].name)
        eq_(String, type(table.columns[2].type))
        eq_("prime", table.columns[3].name)
        eq_(Boolean, type(table.columns[3].type))
        is_not_none(table.columns[3].server_default)
        eq_("FALSE", table.columns[3].server_default.arg.text)
        eq_("ln", table.columns[4].name)
        eq_(REAL, type(table.columns[4].type))
        eq_(1, len(table.indexes))
        index = next(iter(table.indexes))
        eq_(2, len(index.columns))
        eq_("name", index.columns[0].name)
        eq_("prime", index.columns[1].name)
        dialect_options = index.dialect_options["spanner"]
        eq_(1, len(dialect_options["storing"]))
        eq_("alternative_name", dialect_options["storing"][0])

    def test_table_name_overlapping_with_system_table(self, connection):
        class Base(DeclarativeBase):
            pass

        class Role(Base):
            __tablename__ = "roles"
            id: Mapped[int] = mapped_column(Integer, primary_key=True)
            name: Mapped[str] = mapped_column(String(100), nullable=True)
            type: Mapped[str] = mapped_column(String(100), nullable=True)
            description: Mapped[Optional[str]] = mapped_column(String(512))

        engine = connection.engine
        Base.metadata.create_all(engine)

        with Session(engine) as session:
            role = Role(
                id=1,
                name="Test",
                type="Test",
                description="Test",
            )
            session.add(role)
            session.commit()

    def test_orm(self, connection):
        class Base(DeclarativeBase):
            pass

        class Number(Base):
            __tablename__ = "numbers"
            number: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str] = mapped_column(String(20))
            alternative_name: Mapped[str] = mapped_column(String(20))
            prime: Mapped[bool] = mapped_column(Boolean)
            ln: Mapped[float] = mapped_column(REAL)

        class User(Base):
            __tablename__ = "users"
            ID: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str] = mapped_column(String(20))

        class SchemaUser(Base):
            __tablename__ = "users"
            __table_args__ = {"schema": "schema"}
            ID: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str] = mapped_column(String(20))

        engine = connection.engine
        with Session(engine) as session:
            number = Number(
                number=1, name="One", alternative_name="Uno", prime=False, ln=0.0
            )
            session.add(number)
            session.commit()

        level = "serializable"
        if os.environ.get("SPANNER_EMULATOR_HOST", ""):
            level = "REPEATABLE READ"
        with Session(engine.execution_options(isolation_level=level)) as session:
            user = User(name="Test")
            session.add(user)
            session.commit()

            statement = select(User).filter_by(name="Test")
            users = session.scalars(statement).all()
            eq_(1, len(users))
            is_true(users[0].ID > 0)

        with Session(engine) as session:
            user = SchemaUser(name="SchemaTest")
            session.add(user)
            session.commit()

            users = session.scalars(
                select(SchemaUser).where(SchemaUser.name == "SchemaTest")
            ).all()
            eq_(1, len(users))
            is_true(users[0].ID > 0)

            session.execute(
                update(SchemaUser)
                .where(SchemaUser.name == "SchemaTest")
                .values(name="NewName")
            )
            session.commit()

            users = session.scalars(
                select(SchemaUser).where(SchemaUser.name == "NewName")
            ).all()
            eq_(1, len(users))
            is_true(users[0].ID > 0)

            session.execute(delete(SchemaUser).where(SchemaUser.name == "NewName"))
            session.commit()

            users = session.scalars(
                select(SchemaUser).where(SchemaUser.name == "NewName")
            ).all()
            eq_(0, len(users))

    def test_multi_row_insert(self, connection):
        """Ensures we can perform multi-row inserts."""

        class Base(DeclarativeBase):
            pass

        class User(Base):
            __tablename__ = "users"
            ID: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str] = mapped_column(String(20))

        with connection.engine.begin() as conn:
            inserted_rows = list(
                conn.execute(
                    User.__table__.insert()
                    .values([{"name": "a"}, {"name": "b"}])
                    .returning(User.__table__.c.ID, User.__table__.c.name)
                )
            )

        eq_(2, len(inserted_rows))
        eq_({"a", "b"}, {row.name for row in inserted_rows})

        with connection.engine.connect() as conn:
            selected_rows = list(conn.execute(User.__table__.select()))

        eq_(len(inserted_rows), len(selected_rows))
        eq_(set(inserted_rows), set(selected_rows))

    @pytest.mark.skipif(
        os.environ.get("SPANNER_EMULATOR_HOST") is not None,
        reason=(
            "Fails in emulator due to bug: "
            "https://github.com/GoogleCloudPlatform/cloud-spanner-emulator/issues/279"
        ),
    )
    def test_cross_schema_fk_lookups(self, connection):
        """Ensures we introspect FKs within & across schema."""

        engine = connection.engine

        insp = inspect(engine)
        eq_(
            {
                (None, "number_colors"): [
                    {
                        "name": "number_fk",
                        "referred_table": "numbers",
                        "referred_schema": None,
                        "referred_columns": ["number"],
                        "constrained_columns": ["number_id"],
                    }
                ]
            },
            insp.get_multi_foreign_keys(filter_names=["number_colors"]),
        )
        eq_(
            {
                ("schema", "number_colors"): [
                    {
                        "name": "cross_schema_number_fk",
                        "referred_table": "numbers",
                        "referred_schema": None,
                        "referred_columns": ["number"],
                        "constrained_columns": ["number_id"],
                    }
                ]
            },
            insp.get_multi_foreign_keys(
                filter_names=["number_colors"], schema="schema"
            ),
        )

    def test_composite_fk_lookups(self, connection):
        """Ensures we introspect composite FKs."""

        engine = connection.engine

        insp = inspect(engine)
        eq_(
            {
                (None, "composite_fk"): [
                    {
                        "name": "composite_fk_composite_pk_a_b",
                        "referred_table": "composite_pk",
                        "referred_schema": None,
                        "referred_columns": ["a", "b"],
                        "constrained_columns": ["my_a", "my_b"],
                    }
                ]
            },
            insp.get_multi_foreign_keys(filter_names=["composite_fk"]),
        )

    def test_composite_index_lookups(self, connection):
        """Ensures we introspect composite indexes."""

        engine = connection.engine

        insp = inspect(engine)
        eq_(
            {
                (None, "composite_fk"): [
                    {
                        "name": "idx_composte_fk_all",
                        "column_names": ["my_a", "my_b", "my_c"],
                        "unique": False,
                        "column_sorting": {"my_a": "asc", "my_b": "asc", "my_c": "asc"},
                        "include_columns": [],
                        "dialect_options": {},
                    }
                ]
            },
            insp.get_multi_indexes(filter_names=["composite_fk"]),
        )

    def test_commit_timestamp(self, connection):
        """Ensures commit timestamps are set."""

        class Base(DeclarativeBase):
            pass

        class TimestampUser(Base):
            __tablename__ = "timestamp_users"
            ID: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str]
            updated_at: Mapped[datetime.datetime] = mapped_column(
                spanner_allow_commit_timestamp=True,
                default=text("PENDING_COMMIT_TIMESTAMP()"),
                # Make sure that this column is never part of a THEN RETURN clause.
                spanner_exclude_from_returning=True,
            )

        @event.listens_for(TimestampUser, "before_update")
        def before_update(mapper, connection, target):
            target.updated_at = text("PENDING_COMMIT_TIMESTAMP()")

        engine = connection.engine
        Base.metadata.create_all(engine)
        try:
            with Session(engine) as session:
                session.add(TimestampUser(name="name"))
                session.commit()

            with Session(engine) as session:
                users = list(
                    session.scalars(
                        select(TimestampUser).where(TimestampUser.name == "name")
                    )
                )
                user = users[0]

                is_not_none(user.updated_at)
                created_at = user.updated_at

                user.name = "new-name"
                session.commit()

            with Session(engine) as session:
                users = list(
                    session.scalars(
                        select(TimestampUser).where(TimestampUser.name == "new-name")
                    )
                )
                user = users[0]

                is_not_none(user.updated_at)
                is_true(user.updated_at > created_at)

        finally:
            Base.metadata.drop_all(engine)
