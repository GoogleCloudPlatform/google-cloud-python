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

from sqlalchemy import ForeignKey, Index, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Singer(Base):
    __tablename__ = "singers"

    singer_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]


class Album(Base):
    __tablename__ = "albums"
    __table_args__ = {
        "spanner_interleave_in": "singers",
        "spanner_interleave_on_delete_cascade": True,
    }

    singer_id: Mapped[str] = mapped_column(
        ForeignKey("singers.singer_id"), primary_key=True
    )
    album_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    album_title: Mapped[str]


class Track(Base):
    __tablename__ = "tracks"
    __table_args__ = (
        Index(
            "idx_name",
            "singer_id",
            "album_id",
            "song_name",
            spanner_interleave_in="albums",
        ),
        {
            "spanner_interleave_in": "albums",
            "spanner_interleave_on_delete_cascade": True,
        },
    )

    singer_id: Mapped[str] = mapped_column(
        ForeignKey("singers.singer_id"), primary_key=True
    )
    album_id: Mapped[str] = mapped_column(
        ForeignKey("albums.album_id"), primary_key=True
    )
    track_id: Mapped[str] = mapped_column(String(36), primary_key=True)
    song_name: Mapped[str]


Album.__table__.add_is_dependent_on(Singer.__table__)
Track.__table__.add_is_dependent_on(Album.__table__)
