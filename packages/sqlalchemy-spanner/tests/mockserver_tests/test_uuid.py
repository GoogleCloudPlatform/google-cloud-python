# Copyright 2026 Google LLC
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

from uuid import UUID

from google.cloud.spanner_v1 import TypeCode
from sqlalchemy import Column, MetaData, Table, select, types
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.schema import CreateTable
from sqlalchemy.testing import eq_

from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner import (
    SpannerDialect,
    _type_map,
    _type_map_inv,
)
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    add_single_result,
)


class TestUuidMockServer(MockServerTestBase):
    def _get_models(self):
        class Base(DeclarativeBase):
            pass

        class UserUuid(Base):
            __tablename__ = "users_uuid"
            id: Mapped[UUID] = mapped_column(types.Uuid(), primary_key=True)

        class UserUUID(Base):
            __tablename__ = "users_UUID"
            id: Mapped[UUID] = mapped_column(types.UUID(), primary_key=True)

        class UserUuidNativeFalse(Base):
            __tablename__ = "users_uuid_native_false"
            id: Mapped[UUID] = mapped_column(
                types.Uuid(native_uuid=False),
                primary_key=True,
            )

        return UserUuid, UserUUID, UserUuidNativeFalse

    def test_uuid_type_mapping(self):
        """Test UUID is registered in _type_map and _type_map_inv."""
        assert "UUID" in _type_map
        eq_(_type_map["UUID"], types.UUID)
        assert types.UUID in _type_map_inv
        eq_(_type_map_inv[types.UUID], "UUID")
        assert types.Uuid in _type_map_inv
        eq_(_type_map_inv[types.Uuid], "UUID")

    def test_uuid_designate_type(self):
        """Test reflecting UUID type string returns types.UUID."""
        dialect = SpannerDialect()
        assert dialect.supports_native_uuid is False
        col_type = dialect._designate_type("UUID")
        eq_(col_type, types.UUID)

    def test_uuid_ddl_compilation_default(self):
        """Test DDL compilation: types.Uuid emits STRING(36) by default and
        types.UUID emits UUID by default.
        """
        dialect = SpannerDialect()
        metadata = MetaData()
        table = Table(
            "test_uuid_table",
            metadata,
            Column("legacy_id", types.Uuid, primary_key=True),
            Column("native_id", types.UUID),
        )
        statement = str(CreateTable(table).compile(dialect=dialect)).strip()
        assert "legacy_id STRING(36) NOT NULL" in statement
        assert "native_id UUID" in statement

    def test_uuid_ddl_compilation_native_enabled(self):
        """Test DDL compilation emits UUID type for types.Uuid when
        supports_native_uuid is set to True on dialect.
        """
        dialect = SpannerDialect()
        dialect.supports_native_uuid = True
        metadata = MetaData()
        table = Table(
            "test_uuid_table",
            metadata,
            Column("user_id", types.Uuid, primary_key=True),
        )
        statement = str(CreateTable(table).compile(dialect=dialect)).strip()
        assert "user_id UUID NOT NULL" in statement

    def test_uuid_ddl_compilation_native_false_override(self):
        """Test DDL compilation emits STRING(36) for native_uuid=False
        even when supports_native_uuid is set to True on dialect.
        """
        dialect = SpannerDialect()
        dialect.supports_native_uuid = True
        metadata = MetaData()
        table = Table(
            "test_uuid_table",
            metadata,
            Column("user_id", types.Uuid(native_uuid=False), primary_key=True),
        )
        statement = str(CreateTable(table).compile(dialect=dialect)).strip()
        assert "user_id STRING(36) NOT NULL" in statement

    # -----------------------------------------------------------------
    # 1. Flag is disabled (supports_native_uuid = False)
    # -----------------------------------------------------------------
    def test_1_1_flag_disabled_uuid_db_string(self):
        """1.1 Flag disabled + mapped Uuid + DB STRING(36) -> uuid.UUID"""
        UserUuid, _, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = False
        sql = "SELECT users_uuid.id\nFROM users_uuid"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.STRING, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUuid.id)).first()
            eq_(type(user_id), UUID)
            eq_(user_id, UUID(raw_uuid_str))

    def test_1_2_flag_disabled_uuid_db_uuid(self):
        """1.2 Flag disabled + mapped Uuid + DB UUID -> AttributeError"""
        UserUuid, _, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = False
        sql = "SELECT users_uuid.id\nFROM users_uuid"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.UUID, [(raw_uuid_str,)])

        with Session(engine) as session:
            try:
                _ = session.scalars(select(UserUuid.id)).first()
                assert False, "Expected AttributeError"
            except AttributeError:
                pass

    def test_1_3_flag_disabled_UUID_db_string(self):
        """1.3 Flag disabled + mapped UUID + DB STRING(36) -> uuid.UUID"""
        _, UserUUID, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = False
        sql = "SELECT `users_UUID`.id\nFROM `users_UUID`"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.STRING, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUUID.id)).first()
            eq_(type(user_id), UUID)
            eq_(user_id, UUID(raw_uuid_str))

    def test_1_4_flag_disabled_UUID_db_uuid(self):
        """1.4 Flag disabled + mapped UUID + DB UUID -> AttributeError"""
        _, UserUUID, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = False
        sql = "SELECT `users_UUID`.id\nFROM `users_UUID`"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.UUID, [(raw_uuid_str,)])

        with Session(engine) as session:
            try:
                _ = session.scalars(select(UserUUID.id)).first()
                assert False, "Expected AttributeError"
            except AttributeError:
                pass

    # -----------------------------------------------------------------
    # 2. Flag is enabled (supports_native_uuid = True)
    # -----------------------------------------------------------------
    def test_2_1_flag_enabled_uuid_db_string(self):
        """2.1 Flag enabled + mapped Uuid + DB STRING(36) -> user.id is str"""
        UserUuid, _, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = True
        sql = "SELECT users_uuid.id\nFROM users_uuid"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.STRING, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUuid.id)).first()
            eq_(type(user_id), str)
            eq_(user_id, raw_uuid_str)

    def test_2_2_flag_enabled_uuid_db_uuid(self):
        """2.2 Flag enabled + mapped Uuid + DB UUID -> user.id is uuid.UUID"""
        UserUuid, _, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = True
        sql = "SELECT users_uuid.id\nFROM users_uuid"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.UUID, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUuid.id)).first()
            eq_(type(user_id), UUID)
            eq_(user_id, UUID(raw_uuid_str))

    def test_2_3_flag_enabled_UUID_db_string(self):
        """2.3 Flag enabled + mapped UUID (all-caps) + DB STRING(36) -> str"""
        _, UserUUID, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = True
        sql = "SELECT `users_UUID`.id\nFROM `users_UUID`"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.STRING, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUUID.id)).first()
            eq_(type(user_id), str)
            eq_(user_id, raw_uuid_str)

    def test_2_4_flag_enabled_UUID_db_uuid(self):
        """2.4 Flag enabled + mapped UUID (all-caps) + DB UUID -> uuid.UUID"""
        _, UserUUID, _ = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = True
        sql = "SELECT `users_UUID`.id\nFROM `users_UUID`"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.UUID, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUUID.id)).first()
            eq_(type(user_id), UUID)
            eq_(user_id, UUID(raw_uuid_str))

    # -----------------------------------------------------------------
    # 3. Explicit native_uuid = False override
    # -----------------------------------------------------------------
    def test_3_1_flag_enabled_native_false_override_db_string(self):
        """3.1 Flag enabled + types.Uuid(native_uuid=False) + DB STRING(36)
        -> user.id is uuid.UUID (override forces conversion)
        """
        _, _, UserUuidNativeFalse = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = True
        sql = "SELECT users_uuid_native_false.id\nFROM users_uuid_native_false"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.STRING, [(raw_uuid_str,)])

        with Session(engine) as session:
            user_id = session.scalars(select(UserUuidNativeFalse.id)).first()
            eq_(type(user_id), UUID)
            eq_(user_id, UUID(raw_uuid_str))

    def test_3_2_flag_enabled_native_false_override_db_uuid(self):
        """3.2 Flag enabled + types.Uuid(native_uuid=False) + DB UUID
        -> AttributeError (override forces conversion, failing on native UUID)
        """
        _, _, UserUuidNativeFalse = self._get_models()
        engine = self.create_engine()
        engine.dialect.supports_native_uuid = True
        sql = "SELECT users_uuid_native_false.id\nFROM users_uuid_native_false"
        raw_uuid_str = "550e8400-e29b-41d4-a716-446655440000"
        add_single_result(sql, "id", TypeCode.UUID, [(raw_uuid_str,)])

        with Session(engine) as session:
            try:
                _ = session.scalars(select(UserUuidNativeFalse.id)).first()
                assert False, "Expected AttributeError"
            except AttributeError:
                pass
