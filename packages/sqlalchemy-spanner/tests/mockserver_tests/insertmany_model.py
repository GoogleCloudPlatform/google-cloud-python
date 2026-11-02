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
from datetime import datetime

from sqlalchemy import String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class SingerUUID(Base):
    __tablename__ = "singers_uuid"
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        server_default=text("GENERATE_UUID()"),
        default=lambda: str(uuid.uuid4()),
        insert_sentinel=True,
    )
    name: Mapped[str]
    inserted_at: Mapped[datetime] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP()")
    )


class SingerIntID(Base):
    __tablename__ = "singers_int_id"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    inserted_at: Mapped[datetime] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP()")
    )
