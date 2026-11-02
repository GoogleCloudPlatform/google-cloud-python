#  Copyright 2026 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""Types."""

import datetime
from typing import Any

from google.cloud.spanner_v1 import TypeCode


def Date(year: int, month: int, day: int) -> datetime.date:
    """Construct a date object.

    Args:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        datetime.date: A date object.
    """
    return datetime.date(year, month, day)


def Time(hour: int, minute: int, second: int) -> datetime.time:
    """Construct a time object.

    Args:
        hour (int): The hour of the time.
        minute (int): The minute of the time.
        second (int): The second of the time.

    Returns:
        datetime.time: A time object.
    """
    return datetime.time(hour, minute, second)


def Timestamp(
    year: int, month: int, day: int, hour: int, minute: int, second: int
) -> datetime.datetime:
    """Construct a timestamp object.

    Args:
        year (int): The year of the timestamp.
        month (int): The month of the timestamp.
        day (int): The day of the timestamp.
        hour (int): The hour of the timestamp.
        minute (int): The minute of the timestamp.
        second (int): The second of the timestamp.

    Returns:
        datetime.datetime: A timestamp object.
    """
    return datetime.datetime(year, month, day, hour, minute, second)


def DateFromTicks(ticks: float) -> datetime.date:
    """Construct a date object from ticks.

    Args:
        ticks (float): The number of seconds since the epoch.

    Returns:
        datetime.date: A date object.
    """
    return datetime.date.fromtimestamp(ticks)


def TimeFromTicks(ticks: float) -> datetime.time:
    """Construct a time object from ticks.

    Args:
        ticks (float): The number of seconds since the epoch.

    Returns:
        datetime.time: A time object.
    """
    return datetime.datetime.fromtimestamp(ticks).time()


def TimestampFromTicks(ticks: float) -> datetime.datetime:
    """Construct a timestamp object from ticks.

    Args:
        ticks (float): The number of seconds since the epoch.

    Returns:
        datetime.datetime: A timestamp object.
    """
    return datetime.datetime.fromtimestamp(ticks)


def Binary(string: str | bytes) -> bytes:
    """Construct a binary object.

    Args:
        string (str | bytes): The string or bytes to convert.

    Returns:
        bytes: A binary object.
    """
    return bytes(string, "utf-8") if isinstance(string, str) else bytes(string)


# Type Objects for description comparison
class DBAPITypeObject:
    def __init__(self, *values: str):
        self.values = values

    def __eq__(self, other: Any) -> bool:
        return other in self.values


STRING = DBAPITypeObject("STRING")
BINARY = DBAPITypeObject("BYTES", "PROTO")
NUMBER = DBAPITypeObject("INT64", "FLOAT64", "NUMERIC")
DATETIME = DBAPITypeObject("TIMESTAMP", "DATE")
BOOLEAN = DBAPITypeObject("BOOL")
ROWID = DBAPITypeObject()


class Type(object):
    STRING = TypeCode.STRING
    BYTES = TypeCode.BYTES
    BOOL = TypeCode.BOOL
    INT64 = TypeCode.INT64
    FLOAT64 = TypeCode.FLOAT64
    DATE = TypeCode.DATE
    TIMESTAMP = TypeCode.TIMESTAMP
    NUMERIC = TypeCode.NUMERIC
    JSON = TypeCode.JSON
    PROTO = TypeCode.PROTO
    ENUM = TypeCode.ENUM


def _type_code_to_dbapi_type(type_code: int) -> DBAPITypeObject:
    if type_code == TypeCode.STRING:
        return STRING
    if type_code == TypeCode.JSON:
        return STRING
    if type_code == TypeCode.BYTES:
        return BINARY
    if type_code == TypeCode.PROTO:
        return BINARY
    if type_code == TypeCode.BOOL:
        return BOOLEAN
    if type_code == TypeCode.INT64:
        return NUMBER
    if type_code == TypeCode.FLOAT64:
        return NUMBER
    if type_code == TypeCode.NUMERIC:
        return NUMBER
    if type_code == TypeCode.DATE:
        return DATETIME
    if type_code == TypeCode.TIMESTAMP:
        return DATETIME

    return STRING
