# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timedelta, timezone

from google.protobuf import duration_pb2, timestamp_pb2

import proto
from proto.datetime_helpers import DatetimeWithNanoseconds
from proto.marshal.marshal import BaseMarshal


def test_timestamp_read():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo(event_time=timestamp_pb2.Timestamp(seconds=1335020400))

    assert isinstance(foo.event_time, DatetimeWithNanoseconds)
    assert foo.event_time.year == 2012
    assert foo.event_time.month == 4
    assert foo.event_time.day == 21
    assert foo.event_time.hour == 15
    assert foo.event_time.minute == 0
    assert foo.event_time.tzinfo == timezone.utc


def test_timestamp_write_init():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo(event_time=DatetimeWithNanoseconds(2012, 4, 21, 15, tzinfo=timezone.utc))
    assert isinstance(foo.event_time, DatetimeWithNanoseconds)
    assert isinstance(Foo.pb(foo).event_time, timestamp_pb2.Timestamp)
    assert foo.event_time.year == 2012
    assert foo.event_time.month == 4
    assert foo.event_time.hour == 15
    assert Foo.pb(foo).event_time.seconds == 1335020400


def test_timestamp_write():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo()
    dns = DatetimeWithNanoseconds(2012, 4, 21, 15, tzinfo=timezone.utc)
    foo.event_time = dns
    assert isinstance(foo.event_time, DatetimeWithNanoseconds)
    assert isinstance(Foo.pb(foo).event_time, timestamp_pb2.Timestamp)
    assert foo.event_time.year == 2012
    assert foo.event_time.month == 4
    assert foo.event_time.hour == 15
    assert Foo.pb(foo).event_time.seconds == 1335020400


def test_timestamp_write_pb2():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo()
    foo.event_time = timestamp_pb2.Timestamp(seconds=1335020400)
    assert isinstance(foo.event_time, DatetimeWithNanoseconds)
    assert isinstance(Foo.pb(foo).event_time, timestamp_pb2.Timestamp)
    assert foo.event_time.year == 2012
    assert foo.event_time.month == 4
    assert foo.event_time.hour == 15
    assert Foo.pb(foo).event_time.seconds == 1335020400


def test_timestamp_write_string():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo()
    foo.event_time = "2012-04-21T15:00:00Z"
    assert isinstance(foo.event_time, DatetimeWithNanoseconds)
    assert isinstance(Foo.pb(foo).event_time, timestamp_pb2.Timestamp)
    assert foo.event_time.year == 2012
    assert foo.event_time.month == 4
    assert foo.event_time.hour == 15
    assert Foo.pb(foo).event_time.seconds == 1335020400


def test_timestamp_rmw_nanos():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo()
    foo.event_time = DatetimeWithNanoseconds(
        2012, 4, 21, 15, 0, 0, 1, tzinfo=timezone.utc
    )
    assert foo.event_time.microsecond == 1
    assert Foo.pb(foo).event_time.nanos == 1000
    foo.event_time = foo.event_time.replace(microsecond=2)
    assert foo.event_time.microsecond == 2
    assert Foo.pb(foo).event_time.nanos == 2000


def test_timestamp_absence():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo()
    assert foo.event_time is None


def test_timestamp_del():
    class Foo(proto.Message):
        event_time = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    foo = Foo(event_time=DatetimeWithNanoseconds(2012, 4, 21, 15, tzinfo=timezone.utc))
    del foo.event_time
    assert foo.event_time is None


def test_duration_read():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo(ttl=duration_pb2.Duration(seconds=60, nanos=1000))
    assert isinstance(foo.ttl, timedelta)
    assert isinstance(Foo.pb(foo).ttl, duration_pb2.Duration)
    assert foo.ttl.days == 0
    assert foo.ttl.seconds == 60
    assert foo.ttl.microseconds == 1


def test_duration_write_init():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo(ttl=timedelta(days=2))
    assert isinstance(foo.ttl, timedelta)
    assert isinstance(Foo.pb(foo).ttl, duration_pb2.Duration)
    assert foo.ttl.days == 2
    assert foo.ttl.seconds == 0
    assert foo.ttl.microseconds == 0
    assert Foo.pb(foo).ttl.seconds == 86400 * 2


def test_duration_write():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo()
    foo.ttl = timedelta(seconds=120)
    assert isinstance(foo.ttl, timedelta)
    assert isinstance(Foo.pb(foo).ttl, duration_pb2.Duration)
    assert foo.ttl.seconds == 120
    assert Foo.pb(foo).ttl.seconds == 120


def test_duration_write_pb2():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo()
    foo.ttl = duration_pb2.Duration(seconds=120)
    assert isinstance(foo.ttl, timedelta)
    assert isinstance(Foo.pb(foo).ttl, duration_pb2.Duration)
    assert foo.ttl.seconds == 120
    assert Foo.pb(foo).ttl.seconds == 120


def test_duration_write_string():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo()
    foo.ttl = "120s"
    assert isinstance(foo.ttl, timedelta)
    assert isinstance(Foo.pb(foo).ttl, duration_pb2.Duration)
    assert foo.ttl.seconds == 120
    assert Foo.pb(foo).ttl.seconds == 120


def test_duration_write_string_nested():
    class Foo(proto.Message):
        foo_field: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    Foo(foo_field="300s")

    class Bar(proto.Message):
        bar_field = proto.Field(proto.MESSAGE, number=1, message=Foo)

    bar = Bar({"bar_field": {"foo_field": "300s"}})
    assert isinstance(bar.bar_field.foo_field, timedelta)
    assert isinstance(Bar.pb(bar).bar_field.foo_field, duration_pb2.Duration)
    assert bar.bar_field.foo_field.seconds == 300
    assert Bar.pb(bar).bar_field.foo_field.seconds == 300


def test_duration_del():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo(ttl=timedelta(seconds=900))
    del foo.ttl
    assert isinstance(foo.ttl, timedelta)
    assert foo.ttl.days == 0
    assert foo.ttl.seconds == 0
    assert foo.ttl.microseconds == 0


def test_duration_nanos_rmw():
    class Foo(proto.Message):
        ttl = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    foo = Foo(ttl=timedelta(microseconds=50))
    assert foo.ttl.microseconds == 50
    assert Foo.pb(foo).ttl.nanos == 50000
    foo.ttl = timedelta(microseconds=25)
    assert Foo.pb(foo).ttl.nanos == 25000
    assert foo.ttl.microseconds == 25


def test_timestamp_to_python_idempotent():
    # This path can never run in the current configuration because proto
    # values are the only thing ever saved, and `to_python` is a read method.
    #
    # However, we test idempotency for consistency with `to_proto` and
    # general resiliency.
    marshal = BaseMarshal()
    py_value = DatetimeWithNanoseconds(2012, 4, 21, 15, tzinfo=timezone.utc)
    assert marshal.to_python(timestamp_pb2.Timestamp, py_value) is py_value


def test_duration_to_python_idempotent():
    # This path can never run in the current configuration because proto
    # values are the only thing ever saved, and `to_python` is a read method.
    #
    # However, we test idempotency for consistency with `to_proto` and
    # general resiliency.
    marshal = BaseMarshal()
    py_value = timedelta(seconds=240)
    assert marshal.to_python(duration_pb2.Duration, py_value) is py_value


def test_vanilla_datetime_construction():
    # 99% of users are going to want to pass in regular datetime objects.
    # Make sure that this interoperates well with nanosecond precision.
    class User(proto.Message):
        birthday = proto.Field(timestamp_pb2.Timestamp, number=1)

    # Our user WAs born yesterday.
    bday = datetime.now(tz=timezone.utc) + timedelta(days=-1)
    u = User(birthday=bday)
    assert u.birthday == bday
