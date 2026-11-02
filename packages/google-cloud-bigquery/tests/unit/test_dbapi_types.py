# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import datetime
import unittest

import pytest

import google.cloud._helpers
from google.cloud.bigquery.dbapi import types


class TestTypes(unittest.TestCase):
    def test_binary_type(self):
        self.assertEqual("BYTES", types.BINARY)
        self.assertEqual("RECORD", types.BINARY)
        self.assertEqual("STRUCT", types.BINARY)
        self.assertNotEqual("STRING", types.BINARY)

    def test_timefromticks(self):
        somedatetime = datetime.datetime(
            2017, 2, 18, 12, 47, 26, tzinfo=google.cloud._helpers.UTC
        )
        epoch = datetime.datetime(1970, 1, 1, tzinfo=google.cloud._helpers.UTC)
        ticks = (somedatetime - epoch).total_seconds()
        self.assertEqual(
            types.TimeFromTicks(ticks, google.cloud._helpers.UTC),
            datetime.time(12, 47, 26, tzinfo=google.cloud._helpers.UTC),
        )


class CustomBinary:
    def __bytes__(self):
        return b"Google"


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("hello", b"hello"),
        ("\u1f60", "\u1f60".encode("utf-8")),
        (b"hello", b"hello"),
        (bytearray(b"hello"), b"hello"),
        (memoryview(b"hello"), b"hello"),
        (CustomBinary(), b"Google"),
    ],
)
def test_binary_constructor(raw, expected):
    assert types.Binary(raw) == expected


@pytest.mark.parametrize("bad", (42, 42.0, None))
def test_invalid_binary_constructor(bad):
    with pytest.raises(TypeError):
        types.Binary(bad)
