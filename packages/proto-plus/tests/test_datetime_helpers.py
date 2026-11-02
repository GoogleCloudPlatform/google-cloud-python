# Copyright 2017, Google LLC
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

import calendar
import datetime

import pytest
import pytz
from google.protobuf import timestamp_pb2

from proto import datetime_helpers

ONE_MINUTE_IN_MICROSECONDS = 60 * 1e6


def test_from_microseconds():
    five_mins_from_epoch_in_microseconds = 5 * ONE_MINUTE_IN_MICROSECONDS
    five_mins_from_epoch_datetime = datetime.datetime(
        1970, 1, 1, 0, 5, 0, tzinfo=datetime.timezone.utc
    )

    result = datetime_helpers._from_microseconds(five_mins_from_epoch_in_microseconds)

    assert result == five_mins_from_epoch_datetime


def test_to_rfc3339():
    value = datetime.datetime(2016, 4, 5, 13, 30, 0)
    expected = "2016-04-05T13:30:00.000000Z"
    assert datetime_helpers._to_rfc3339(value) == expected


def test_to_rfc3339_with_utc():
    value = datetime.datetime(2016, 4, 5, 13, 30, 0, tzinfo=datetime.timezone.utc)
    expected = "2016-04-05T13:30:00.000000Z"
    assert datetime_helpers._to_rfc3339(value, ignore_zone=False) == expected


def test_to_rfc3339_with_non_utc():
    zone = pytz.FixedOffset(-60)
    value = datetime.datetime(2016, 4, 5, 13, 30, 0, tzinfo=zone)
    expected = "2016-04-05T14:30:00.000000Z"
    assert datetime_helpers._to_rfc3339(value, ignore_zone=False) == expected


def test_to_rfc3339_with_non_utc_ignore_zone():
    zone = pytz.FixedOffset(-60)
    value = datetime.datetime(2016, 4, 5, 13, 30, 0, tzinfo=zone)
    expected = "2016-04-05T13:30:00.000000Z"
    assert datetime_helpers._to_rfc3339(value, ignore_zone=True) == expected


def test_ctor_wo_nanos():
    stamp = datetime_helpers.DatetimeWithNanoseconds(2016, 12, 20, 21, 13, 47, 123456)
    assert stamp.year == 2016
    assert stamp.month == 12
    assert stamp.day == 20
    assert stamp.hour == 21
    assert stamp.minute == 13
    assert stamp.second == 47
    assert stamp.microsecond == 123456
    assert stamp.nanosecond == 123456000


def test_ctor_w_nanos():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=123456789
    )
    assert stamp.year == 2016
    assert stamp.month == 12
    assert stamp.day == 20
    assert stamp.hour == 21
    assert stamp.minute == 13
    assert stamp.second == 47
    assert stamp.microsecond == 123456
    assert stamp.nanosecond == 123456789


def test_ctor_w_micros_positional_and_nanos():
    with pytest.raises(TypeError):
        datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, 123456, nanosecond=123456789
        )


def test_ctor_w_micros_keyword_and_nanos():
    with pytest.raises(TypeError):
        datetime_helpers.DatetimeWithNanoseconds(
            2016, 12, 20, 21, 13, 47, microsecond=123456, nanosecond=123456789
        )


def test_rfc3339_wo_nanos():
    stamp = datetime_helpers.DatetimeWithNanoseconds(2016, 12, 20, 21, 13, 47, 123456)
    assert stamp.rfc3339() == "2016-12-20T21:13:47.123456Z"


def test_rfc3339_wo_nanos_w_leading_zero():
    stamp = datetime_helpers.DatetimeWithNanoseconds(2016, 12, 20, 21, 13, 47, 1234)
    assert stamp.rfc3339() == "2016-12-20T21:13:47.001234Z"


def test_rfc3339_w_nanos():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=123456789
    )
    assert stamp.rfc3339() == "2016-12-20T21:13:47.123456789Z"


def test_rfc3339_w_nanos_w_leading_zero():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=1234567
    )
    assert stamp.rfc3339() == "2016-12-20T21:13:47.001234567Z"


def test_rfc3339_w_nanos_no_trailing_zeroes():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=100000000
    )
    assert stamp.rfc3339() == "2016-12-20T21:13:47.1Z"


def test_rfc3339_w_nanos_w_leading_zero_and_no_trailing_zeros():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=1234500
    )
    assert stamp.rfc3339() == "2016-12-20T21:13:47.0012345Z"


def test_from_rfc3339_w_invalid():
    stamp = "2016-12-20T21:13:47"
    with pytest.raises(ValueError):
        datetime_helpers.DatetimeWithNanoseconds.from_rfc3339(stamp)


def test_from_rfc3339_wo_fraction():
    timestamp = "2016-12-20T21:13:47Z"
    expected = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, tzinfo=datetime.timezone.utc
    )
    stamp = datetime_helpers.DatetimeWithNanoseconds.from_rfc3339(timestamp)
    assert stamp == expected


def test_from_rfc3339_w_partial_precision():
    timestamp = "2016-12-20T21:13:47.1Z"
    expected = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, microsecond=100000, tzinfo=datetime.timezone.utc
    )
    stamp = datetime_helpers.DatetimeWithNanoseconds.from_rfc3339(timestamp)
    assert stamp == expected


def test_from_rfc3339_w_full_precision():
    timestamp = "2016-12-20T21:13:47.123456789Z"
    expected = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=123456789, tzinfo=datetime.timezone.utc
    )
    stamp = datetime_helpers.DatetimeWithNanoseconds.from_rfc3339(timestamp)
    assert stamp == expected


@pytest.mark.parametrize(
    "fractional, nanos",
    [
        ("12345678", 123456780),
        ("1234567", 123456700),
        ("123456", 123456000),
        ("12345", 123450000),
        ("1234", 123400000),
        ("123", 123000000),
        ("12", 120000000),
        ("1", 100000000),
    ],
)
def test_from_rfc3339_test_nanoseconds(fractional, nanos):
    value = "2009-12-17T12:44:32.{}Z".format(fractional)
    assert (
        datetime_helpers.DatetimeWithNanoseconds.from_rfc3339(value).nanosecond == nanos
    )


def test_timestamp_pb_wo_nanos_naive():
    stamp = datetime_helpers.DatetimeWithNanoseconds(2016, 12, 20, 21, 13, 47, 123456)
    delta = stamp.replace(tzinfo=datetime.timezone.utc) - datetime_helpers._UTC_EPOCH
    seconds = int(delta.total_seconds())
    nanos = 123456000
    timestamp = timestamp_pb2.Timestamp(seconds=seconds, nanos=nanos)
    assert stamp.timestamp_pb() == timestamp


def test_timestamp_pb_w_nanos():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, nanosecond=123456789, tzinfo=datetime.timezone.utc
    )
    delta = stamp - datetime_helpers._UTC_EPOCH
    timestamp = timestamp_pb2.Timestamp(
        seconds=int(delta.total_seconds()), nanos=123456789
    )
    assert stamp.timestamp_pb() == timestamp


def test_from_timestamp_pb_wo_nanos():
    when = datetime.datetime(
        2016, 12, 20, 21, 13, 47, 123456, tzinfo=datetime.timezone.utc
    )
    delta = when - datetime_helpers._UTC_EPOCH
    seconds = int(delta.total_seconds())
    timestamp = timestamp_pb2.Timestamp(seconds=seconds)

    stamp = datetime_helpers.DatetimeWithNanoseconds.from_timestamp_pb(timestamp)

    assert _to_seconds(when) == _to_seconds(stamp)
    assert stamp.microsecond == 0
    assert stamp.nanosecond == 0
    assert stamp.tzinfo == datetime.timezone.utc


def test_replace():
    stamp = datetime_helpers.DatetimeWithNanoseconds(
        2016, 12, 20, 21, 13, 47, 123456, tzinfo=datetime.timezone.utc
    )

    # ns and ms provided raises
    with pytest.raises(TypeError):
        stamp.replace(microsecond=1, nanosecond=0)

    # No Nanoseconds or Microseconds
    new_stamp = stamp.replace(year=2015)
    assert new_stamp.year == 2015
    assert new_stamp.microsecond == 123456
    assert new_stamp.nanosecond == 123456000

    # Nanos
    new_stamp = stamp.replace(nanosecond=789123)
    assert new_stamp.microsecond == 789
    assert new_stamp.nanosecond == 789123

    # Micros
    new_stamp = stamp.replace(microsecond=456)
    assert new_stamp.microsecond == 456
    assert new_stamp.nanosecond == 456000

    # assert _to_seconds(when) == _to_seconds(stamp)
    # assert stamp.microsecond == 0
    # assert stamp.nanosecond == 0
    # assert stamp.tzinfo == datetime.timezone.utc


def test_from_timestamp_pb_w_nanos():
    when = datetime.datetime(
        2016, 12, 20, 21, 13, 47, 123456, tzinfo=datetime.timezone.utc
    )
    delta = when - datetime_helpers._UTC_EPOCH
    seconds = int(delta.total_seconds())
    timestamp = timestamp_pb2.Timestamp(seconds=seconds, nanos=123456789)

    stamp = datetime_helpers.DatetimeWithNanoseconds.from_timestamp_pb(timestamp)

    assert _to_seconds(when) == _to_seconds(stamp)
    assert stamp.microsecond == 123456
    assert stamp.nanosecond == 123456789
    assert stamp.tzinfo == datetime.timezone.utc


def _to_seconds(value):
    """Convert a datetime to seconds since the unix epoch.

    Args:
        value (datetime.datetime): The datetime to convert.

    Returns:
        int: Microseconds since the unix epoch.
    """
    assert value.tzinfo is datetime.timezone.utc
    return calendar.timegm(value.timetuple())
