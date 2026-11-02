# Copyright 2026 Google LLC All rights reserved.
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

from __future__ import annotations

from uuid import UUID, uuid4

from sample_helper import run_sample
from sqlalchemy import create_engine, select, types
from sqlalchemy.dialects import registry
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

registry.register(
    "spanner",
    "google.cloud.sqlalchemy_spanner.sqlalchemy_spanner",
    "SpannerDialect",
)


class Base(DeclarativeBase):
    pass


# -----------------------------------------------------------------------------
# GUIDELINES FOR USERS / CUSTOMERS:
#
# 1. types.Uuid() (CamelCase - Recommended):
#    - supports_native_uuid = False (default): Compiles to `STRING(36)`.
#    - supports_native_uuid = True:            Compiles to `UUID`.
#    - Works seamlessly for inserts and queries across both configurations.
#
# 2. types.UUID() (All-Caps - Native Spanner Type):
#    - IMPORTANT: Use `types.UUID()` ONLY when `supports_native_uuid = True`
#      is enabled on your dialect/engine for native Cloud Spanner UUID columns.
#
# 3. types.Uuid(native_uuid=False) (Explicit Override):
#    - Forces `STRING(36)` storage even when `supports_native_uuid = True`.
# -----------------------------------------------------------------------------


class CustomerLegacy(Base):
    """Uses types.Uuid() -> Compiles to STRING(36) by default."""

    __tablename__ = "customers_legacy"
    id: Mapped[UUID] = mapped_column(types.Uuid(), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()


class CustomerNative(Base):
    """Uses types.UUID() -> ALWAYS compiles to native UUID type in Spanner DDL,

    even when supports_native_uuid=False.
    """

    __tablename__ = "customers_native"
    id: Mapped[UUID] = mapped_column(types.UUID(), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()


class CustomerExplicitString(Base):
    """Uses types.Uuid(native_uuid=False) -> ALWAYS compiles to STRING(36)."""

    __tablename__ = "customers_explicit_string"
    id: Mapped[UUID] = mapped_column(
        types.Uuid(native_uuid=False),
        primary_key=True,
        default=uuid4,
    )
    name: Mapped[str] = mapped_column()


def run_with_flag_disabled():
    """Scenario 1: supports_native_uuid = False (Default).

    - types.Uuid() emits STRING(36) in DDL.
    - types.Uuid(native_uuid=False) emits STRING(36) in DDL.
    """
    sep = "=" * 73
    print(f"\n{sep}")
    print("SCENARIO 1: Flag Disabled (supports_native_uuid=False)")
    print(sep)
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    engine.dialect.supports_native_uuid = False
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cust_legacy = CustomerLegacy(name="Alice_Legacy_FlagDisabled")
        cust_override = CustomerExplicitString(name="Diana_String_FlagDisabled")
        session.add_all([cust_legacy, cust_override])
        session.commit()

        fetched_legacy = session.scalars(
            select(CustomerLegacy).filter_by(id=cust_legacy.id)
        ).one()
        print(
            "--> [Flag Disabled] Legacy Customer ID "
            f"({type(fetched_legacy.id).__name__}): {fetched_legacy.id}"
        )

        fetched_override = session.scalars(
            select(CustomerExplicitString).filter_by(id=cust_override.id)
        ).one()
        print(
            "--> [Flag Disabled] Explicit STRING Customer ID "
            f"({type(fetched_override.id).__name__}): {fetched_override.id}"
        )


def run_with_flag_enabled():
    """Scenario 2: supports_native_uuid = True.

    - types.Uuid() emits UUID in DDL when flag enabled.
    - types.UUID() ALWAYS emits UUID in DDL.
    - types.Uuid(native_uuid=False) explicitly emits STRING(36).
    """
    sep = "=" * 73
    print(f"\n{sep}")
    print("SCENARIO 2: Flag Enabled (supports_native_uuid=True)")
    print(sep)
    engine = create_engine(
        "spanner:///projects/sample-project/"
        "instances/sample-instance/"
        "databases/sample-database",
        echo=True,
    )
    engine.dialect.supports_native_uuid = True
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        cust_legacy = CustomerLegacy(name="Charlie_Legacy_FlagEnabled")
        cust_native = CustomerNative(name="Bob_Native_FlagEnabled")
        cust_override = CustomerExplicitString(name="Diana_String_FlagEnabled")
        session.add_all([cust_legacy, cust_native, cust_override])
        session.commit()

        fetched_legacy = session.scalars(
            select(CustomerLegacy).filter_by(id=cust_legacy.id)
        ).one()
        print(
            "--> [Flag Enabled] Legacy Customer ID "
            f"({type(fetched_legacy.id).__name__}): {fetched_legacy.id}"
        )

        fetched_native = session.scalars(
            select(CustomerNative).filter_by(id=cust_native.id)
        ).one()
        print(
            "--> [Flag Enabled] Native Customer ID "
            f"({type(fetched_native.id).__name__}): {fetched_native.id}"
        )

        fetched_override = session.scalars(
            select(CustomerExplicitString).filter_by(id=cust_override.id)
        ).one()
        print(
            "--> [Flag Enabled] Explicit STRING Customer ID "
            f"({type(fetched_override.id).__name__}): {fetched_override.id}"
        )


def uuid_sample():
    """Demonstrates how to use types.Uuid vs types.UUID with Spanner SQLAlchemy

    under both supports_native_uuid=False and supports_native_uuid=True.
    """
    run_with_flag_disabled()
    run_with_flag_enabled()


if __name__ == "__main__":
    run_sample(uuid_sample)
