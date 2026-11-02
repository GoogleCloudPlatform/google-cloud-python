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

from sqlalchemy import Column, Integer, PickleType, String
from sqlalchemy.orm import DeclarativeBase

from google.cloud.sqlalchemy_spanner.sqlalchemy_spanner import SpannerPickleType


class Base(DeclarativeBase):
    pass


class UserPreferences(Base):
    __tablename__ = "user_preferences"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    preferences = Column(PickleType(impl=SpannerPickleType), nullable=True)
    created_at = Column(String(30), nullable=False)
