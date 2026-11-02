# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import decimal

SCALAR_COLUMNS = [
    {"name": "int_col", "type": "int64"},
    {"name": "float_col", "type": "float64"},
    {"name": "num_col", "type": "numeric"},
    {"name": "bool_col", "type": "bool"},
    {"name": "str_col", "type": "string"},
    {"name": "bytes_col", "type": "bytes"},
    {"name": "date_col", "type": "date"},
    {"name": "time_col", "type": "time"},
    {"name": "ts_col", "type": "timestamp"},
]
SCALAR_COLUMN_NAMES = [field["name"] for field in SCALAR_COLUMNS]
SCALAR_BLOCKS = [
    [
        {
            "int_col": 123,
            "float_col": 3.14,
            "num_col": decimal.Decimal("9.99"),
            "bool_col": True,
            "str_col": "hello world",
            "bytes_col": b"ascii bytes",
            "date_col": datetime.date(1998, 9, 4),
            "time_col": datetime.time(12, 0),
            "ts_col": datetime.datetime(2000, 1, 1, 5, 0, tzinfo=datetime.timezone.utc),
        },
        {
            "int_col": 456,
            "float_col": 2.72,
            "num_col": decimal.Decimal("0.99"),
            "bool_col": False,
            "str_col": "hallo welt",
            "bytes_col": b"\xbb\xee\xff",
            "date_col": datetime.date(1995, 3, 2),
            "time_col": datetime.time(13, 37),
            "ts_col": datetime.datetime(1965, 4, 3, 2, 1, tzinfo=datetime.timezone.utc),
        },
    ],
    [
        {
            "int_col": 789,
            "float_col": 1.23,
            "num_col": decimal.Decimal("5.67"),
            "bool_col": True,
            "str_col": "こんにちは世界",
            "bytes_col": b"\x54\x69\x6d",
            "date_col": datetime.date(1970, 1, 1),
            "time_col": datetime.time(16, 20),
            "ts_col": datetime.datetime(
                1991, 8, 25, 20, 57, 8, tzinfo=datetime.timezone.utc
            ),
        }
    ],
]
