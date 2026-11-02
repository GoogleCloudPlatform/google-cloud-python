# Copyright 2014 Google LLC
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

import unittest
from unittest import mock


class Test__LocalStack(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud._helpers import _LocalStack

        return _LocalStack

    def _make_one(self):
        return self._get_target_class()()

    def test_it(self):
        batch1, batch2 = object(), object()
        batches = self._make_one()
        self.assertEqual(list(batches), [])
        self.assertIsNone(batches.top)
        batches.push(batch1)
        self.assertIs(batches.top, batch1)
        batches.push(batch2)
        self.assertIs(batches.top, batch2)
        popped = batches.pop()
        self.assertIs(popped, batch2)
        self.assertIs(batches.top, batch1)
        self.assertEqual(list(batches), [batch1])
        popped = batches.pop()
        self.assertIsNone(batches.top)
        self.assertEqual(list(batches), [])


class Test__ensure_tuple_or_list(unittest.TestCase):
    def _call_fut(self, arg_name, tuple_or_list):
        from google.cloud._helpers import _ensure_tuple_or_list

        return _ensure_tuple_or_list(arg_name, tuple_or_list)

    def test_valid_tuple(self):
        valid_tuple_or_list = ("a", "b", "c", "d")
        result = self._call_fut("ARGNAME", valid_tuple_or_list)
        self.assertEqual(result, ["a", "b", "c", "d"])

    def test_valid_list(self):
        valid_tuple_or_list = ["a", "b", "c", "d"]
        result = self._call_fut("ARGNAME", valid_tuple_or_list)
        self.assertEqual(result, valid_tuple_or_list)

    def test_invalid(self):
        invalid_tuple_or_list = object()
        with self.assertRaises(TypeError):
            self._call_fut("ARGNAME", invalid_tuple_or_list)

    def test_invalid_iterable(self):
        invalid_tuple_or_list = "FOO"
        with self.assertRaises(TypeError):
            self._call_fut("ARGNAME", invalid_tuple_or_list)


class Test__determine_default_project(unittest.TestCase):
    def _call_fut(self, project=None):
        from google.cloud._helpers import _determine_default_project

        return _determine_default_project(project=project)

    def test_it(self):
        with mock.patch("google.auth.default", autospec=True) as default:
            default.return_value = (mock.sentinel.credentials, mock.sentinel.project)
            project = self._call_fut()

        self.assertEqual(project, mock.sentinel.project)
        default.assert_called_once_with()

    def test_explicit(self):
        with mock.patch("google.auth.default", autospec=True) as default:
            project = self._call_fut(mock.sentinel.project)

        self.assertEqual(project, mock.sentinel.project)
        self.assertFalse(default.called)


class Test__millis(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud._helpers import _millis

        return _millis(value)

    def test_one_second_from_epoch(self):
        import datetime
        from google.cloud._helpers import UTC

        WHEN = datetime.datetime(1970, 1, 1, 0, 0, 1, tzinfo=UTC)
        self.assertEqual(self._call_fut(WHEN), 1000)


class Test__microseconds_from_datetime(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud._helpers import _microseconds_from_datetime

        return _microseconds_from_datetime(value)

    def test_it(self):
        import datetime

        microseconds = 314159
        timestamp = datetime.datetime(
            1970, 1, 1, hour=0, minute=0, second=0, microsecond=microseconds
        )
        result = self._call_fut(timestamp)
        self.assertEqual(result, microseconds)


class Test__millis_from_datetime(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud._helpers import _millis_from_datetime

        return _millis_from_datetime(value)

    def test_w_none(self):
        self.assertIsNone(self._call_fut(None))

    def test_w_utc_datetime(self):
        import datetime
        from google.cloud._helpers import UTC
        from google.cloud._helpers import _microseconds_from_datetime

        NOW = datetime.datetime.now().replace(tzinfo=UTC)
        NOW_MICROS = _microseconds_from_datetime(NOW)
        MILLIS = NOW_MICROS // 1000
        result = self._call_fut(NOW)
        self.assertIsInstance(result, int)
        self.assertEqual(result, MILLIS)

    def test_w_non_utc_datetime(self):
        import datetime
        from google.cloud._helpers import _microseconds_from_datetime

        offset = datetime.timedelta(hours=-1)
        zone = datetime.timezone(offset=offset, name="CET")
        NOW = datetime.datetime(2015, 7, 28, 16, 34, 47, tzinfo=zone)
        NOW_MICROS = _microseconds_from_datetime(NOW)
        MILLIS = NOW_MICROS // 1000
        result = self._call_fut(NOW)
        self.assertIsInstance(result, int)
        self.assertEqual(result, MILLIS)

    def test_w_naive_datetime(self):
        import datetime
        from google.cloud._helpers import UTC
        from google.cloud._helpers import _microseconds_from_datetime

        NOW = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        UTC_NOW = NOW.replace(tzinfo=UTC)
        UTC_NOW_MICROS = _microseconds_from_datetime(UTC_NOW)
        MILLIS = UTC_NOW_MICROS // 1000
        result = self._call_fut(NOW)
        self.assertIsInstance(result, int)
        self.assertEqual(result, MILLIS)


class Test__datetime_from_microseconds(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud._helpers import _datetime_from_microseconds

        return _datetime_from_microseconds(value)

    def test_it(self):
        import datetime
        from google.cloud._helpers import UTC
        from google.cloud._helpers import _microseconds_from_datetime

        NOW = datetime.datetime(2015, 7, 29, 17, 45, 21, 123456, tzinfo=UTC)
        NOW_MICROS = _microseconds_from_datetime(NOW)
        self.assertEqual(self._call_fut(NOW_MICROS), NOW)


class Test___date_from_iso8601_date(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud._helpers import _date_from_iso8601_date

        return _date_from_iso8601_date(value)

    def test_todays_date(self):
        import datetime

        TODAY = datetime.date.today()
        self.assertEqual(self._call_fut(TODAY.strftime("%Y-%m-%d")), TODAY)


class Test___time_from_iso8601_time_naive(unittest.TestCase):
    def _call_fut(self, value):
        from google.cloud._helpers import _time_from_iso8601_time_naive

        return _time_from_iso8601_time_naive(value)

    def test_todays_date(self):
        import datetime

        WHEN = datetime.time(12, 9, 42)
        self.assertEqual(self._call_fut(("12:09:42")), WHEN)

    def test_w_microseconds(self):
        import datetime

        WHEN = datetime.time(12, 9, 42, 123456)
        self.assertEqual(self._call_fut(("12:09:42.123456")), WHEN)

    def test_w_millis_fail(self):
        with self.assertRaises(ValueError):
            self._call_fut("12:09:42.123")


class Test__rfc3339_to_datetime(unittest.TestCase):
    def _call_fut(self, dt_str):
        from google.cloud._helpers import _rfc3339_to_datetime

        return _rfc3339_to_datetime(dt_str)

    def test_w_bogus_zone(self):
        year = 2009
        month = 12
        day = 17
        hour = 12
        minute = 44
        seconds = 32
        micros = 123456789

        dt_str = "%d-%02d-%02dT%02d:%02d:%02d.%06dBOGUS" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
            micros,
        )
        with self.assertRaises(ValueError):
            self._call_fut(dt_str)

    def test_w_microseconds(self):
        import datetime
        from google.cloud._helpers import UTC

        year = 2009
        month = 12
        day = 17
        hour = 12
        minute = 44
        seconds = 32
        micros = 123456

        dt_str = "%d-%02d-%02dT%02d:%02d:%02d.%06dZ" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
            micros,
        )
        result = self._call_fut(dt_str)
        expected_result = datetime.datetime(
            year, month, day, hour, minute, seconds, micros, UTC
        )
        self.assertEqual(result, expected_result)

    def test_w_naonseconds(self):
        year = 2009
        month = 12
        day = 17
        hour = 12
        minute = 44
        seconds = 32
        nanos = 123456789

        dt_str = "%d-%02d-%02dT%02d:%02d:%02d.%09dZ" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
            nanos,
        )
        with self.assertRaises(ValueError):
            self._call_fut(dt_str)


class Test__rfc3339_nanos_to_datetime(unittest.TestCase):
    def _call_fut(self, dt_str):
        from google.cloud._helpers import _rfc3339_nanos_to_datetime

        return _rfc3339_nanos_to_datetime(dt_str)

    def test_w_bogus_zone(self):
        year = 2009
        month = 12
        day = 17
        hour = 12
        minute = 44
        seconds = 32
        micros = 123456789

        dt_str = "%d-%02d-%02dT%02d:%02d:%02d.%06dBOGUS" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
            micros,
        )
        with self.assertRaises(ValueError):
            self._call_fut(dt_str)

    def test_w_truncated_nanos(self):
        import datetime
        from google.cloud._helpers import UTC

        year = 2009
        month = 12
        day = 17
        hour = 12
        minute = 44
        seconds = 32
        truncateds_and_micros = [
            ("12345678", 123456),
            ("1234567", 123456),
            ("123456", 123456),
            ("12345", 123450),
            ("1234", 123400),
            ("123", 123000),
            ("12", 120000),
            ("1", 100000),
        ]

        for truncated, micros in truncateds_and_micros:
            dt_str = "%d-%02d-%02dT%02d:%02d:%02d.%sZ" % (
                year,
                month,
                day,
                hour,
                minute,
                seconds,
                truncated,
            )
            result = self._call_fut(dt_str)
            expected_result = datetime.datetime(
                year, month, day, hour, minute, seconds, micros, UTC
            )
            self.assertEqual(result, expected_result)

    def test_without_nanos(self):
        import datetime
        from google.cloud._helpers import UTC

        year = 1988
        month = 4
        day = 29
        hour = 12
        minute = 12
        seconds = 12

        dt_str = "%d-%02d-%02dT%02d:%02d:%02dZ" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
        )
        result = self._call_fut(dt_str)
        expected_result = datetime.datetime(
            year, month, day, hour, minute, seconds, 0, UTC
        )
        self.assertEqual(result, expected_result)

    def test_w_naonseconds(self):
        import datetime
        from google.cloud._helpers import UTC

        year = 2009
        month = 12
        day = 17
        hour = 12
        minute = 44
        seconds = 32
        nanos = 123456789
        micros = nanos // 1000

        dt_str = "%d-%02d-%02dT%02d:%02d:%02d.%09dZ" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
            nanos,
        )
        result = self._call_fut(dt_str)
        expected_result = datetime.datetime(
            year, month, day, hour, minute, seconds, micros, UTC
        )
        self.assertEqual(result, expected_result)


class Test__datetime_to_rfc3339(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import _datetime_to_rfc3339

        return _datetime_to_rfc3339(*args, **kwargs)

    @staticmethod
    def _make_timezone(offset):
        import datetime

        return datetime.timezone(offset=offset, name="CET")

    def test_w_utc_datetime(self):
        import datetime
        from google.cloud._helpers import UTC

        TIMESTAMP = datetime.datetime(2016, 4, 5, 13, 30, 0, tzinfo=UTC)
        result = self._call_fut(TIMESTAMP, ignore_zone=False)
        self.assertEqual(result, "2016-04-05T13:30:00.000000Z")

    def test_w_non_utc_datetime(self):
        import datetime

        zone = self._make_timezone(offset=datetime.timedelta(hours=-1))
        TIMESTAMP = datetime.datetime(2016, 4, 5, 13, 30, 0, tzinfo=zone)
        result = self._call_fut(TIMESTAMP, ignore_zone=False)
        self.assertEqual(result, "2016-04-05T14:30:00.000000Z")

    def test_w_non_utc_datetime_and_ignore_zone(self):
        import datetime

        zone = self._make_timezone(offset=datetime.timedelta(hours=-1))
        TIMESTAMP = datetime.datetime(2016, 4, 5, 13, 30, 0, tzinfo=zone)
        result = self._call_fut(TIMESTAMP)
        self.assertEqual(result, "2016-04-05T13:30:00.000000Z")

    def test_w_naive_datetime(self):
        import datetime

        TIMESTAMP = datetime.datetime(2016, 4, 5, 13, 30, 0)
        result = self._call_fut(TIMESTAMP)
        self.assertEqual(result, "2016-04-05T13:30:00.000000Z")


class Test__to_bytes(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import _to_bytes

        return _to_bytes(*args, **kwargs)

    def test_with_bytes(self):
        value = b"bytes-val"
        self.assertEqual(self._call_fut(value), value)

    def test_with_unicode(self):
        value = "string-val"
        encoded_value = b"string-val"
        self.assertEqual(self._call_fut(value), encoded_value)

    def test_unicode_non_ascii(self):
        value = "\u2013"  # Long hyphen
        encoded_value = b"\xe2\x80\x93"
        self.assertRaises(UnicodeEncodeError, self._call_fut, value)
        self.assertEqual(self._call_fut(value, encoding="utf-8"), encoded_value)

    def test_with_nonstring_type(self):
        value = object()
        self.assertRaises(TypeError, self._call_fut, value)


class Test__bytes_to_unicode(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import _bytes_to_unicode

        return _bytes_to_unicode(*args, **kwargs)

    def test_with_bytes(self):
        value = b"bytes-val"
        encoded_value = "bytes-val"
        self.assertEqual(self._call_fut(value), encoded_value)

    def test_with_unicode(self):
        value = "string-val"
        encoded_value = "string-val"
        self.assertEqual(self._call_fut(value), encoded_value)

    def test_with_nonstring_type(self):
        value = object()
        self.assertRaises(ValueError, self._call_fut, value)


class Test__pb_timestamp_to_datetime(unittest.TestCase):
    def _call_fut(self, timestamp):
        from google.cloud._helpers import _pb_timestamp_to_datetime

        return _pb_timestamp_to_datetime(timestamp)

    def test_it(self):
        import datetime
        from google.protobuf.timestamp_pb2 import Timestamp
        from google.cloud._helpers import UTC

        # Epoch is midnight on January 1, 1970 ...
        dt_stamp = datetime.datetime(
            1970,
            month=1,
            day=1,
            hour=0,
            minute=1,
            second=1,
            microsecond=1234,
            tzinfo=UTC,
        )
        # ... so 1 minute and 1 second after is 61 seconds and 1234
        # microseconds is 1234000 nanoseconds.
        timestamp = Timestamp(seconds=61, nanos=1234000)
        self.assertEqual(self._call_fut(timestamp), dt_stamp)


class Test__from_any_pb(unittest.TestCase):
    def _call_fut(self, pb_type, any_pb):
        from google.cloud._helpers import _from_any_pb

        return _from_any_pb(pb_type, any_pb)

    def test_success(self):
        from google.protobuf import any_pb2
        from google.type import date_pb2

        in_message = date_pb2.Date(year=1990)
        in_message_any = any_pb2.Any()
        in_message_any.Pack(in_message)
        out_message = self._call_fut(date_pb2.Date, in_message_any)
        self.assertEqual(in_message, out_message)

    def test_failure(
        self,
    ):
        from google.protobuf import any_pb2
        from google.type import date_pb2
        from google.type import timeofday_pb2

        in_message = any_pb2.Any()
        in_message.Pack(date_pb2.Date(year=1990))

        with self.assertRaises(TypeError):
            self._call_fut(timeofday_pb2.TimeOfDay, in_message)


class Test__pb_timestamp_to_rfc3339(unittest.TestCase):
    def _call_fut(self, timestamp):
        from google.cloud._helpers import _pb_timestamp_to_rfc3339

        return _pb_timestamp_to_rfc3339(timestamp)

    def test_it(self):
        from google.protobuf.timestamp_pb2 import Timestamp

        # Epoch is midnight on January 1, 1970 ...
        # ... so 1 minute and 1 second after is 61 seconds and 1234
        # microseconds is 1234000 nanoseconds.
        timestamp = Timestamp(seconds=61, nanos=1234000)
        self.assertEqual(self._call_fut(timestamp), "1970-01-01T00:01:01.001234Z")


class Test__datetime_to_pb_timestamp(unittest.TestCase):
    def _call_fut(self, when):
        from google.cloud._helpers import _datetime_to_pb_timestamp

        return _datetime_to_pb_timestamp(when)

    def test_it(self):
        import datetime
        from google.protobuf.timestamp_pb2 import Timestamp
        from google.cloud._helpers import UTC

        # Epoch is midnight on January 1, 1970 ...
        dt_stamp = datetime.datetime(
            1970,
            month=1,
            day=1,
            hour=0,
            minute=1,
            second=1,
            microsecond=1234,
            tzinfo=UTC,
        )
        # ... so 1 minute and 1 second after is 61 seconds and 1234
        # microseconds is 1234000 nanoseconds.
        timestamp = Timestamp(seconds=61, nanos=1234000)
        self.assertEqual(self._call_fut(dt_stamp), timestamp)


class Test__timedelta_to_duration_pb(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import _timedelta_to_duration_pb

        return _timedelta_to_duration_pb(*args, **kwargs)

    def test_it(self):
        import datetime
        from google.protobuf import duration_pb2

        seconds = microseconds = 1
        timedelta_val = datetime.timedelta(seconds=seconds, microseconds=microseconds)
        result = self._call_fut(timedelta_val)
        self.assertIsInstance(result, duration_pb2.Duration)
        self.assertEqual(result.seconds, seconds)
        self.assertEqual(result.nanos, 1000 * microseconds)

    def test_with_negative_microseconds(self):
        import datetime
        from google.protobuf import duration_pb2

        seconds = 1
        microseconds = -5
        timedelta_val = datetime.timedelta(seconds=seconds, microseconds=microseconds)
        result = self._call_fut(timedelta_val)
        self.assertIsInstance(result, duration_pb2.Duration)
        self.assertEqual(result.seconds, seconds - 1)
        self.assertEqual(result.nanos, 10**9 + 1000 * microseconds)

    def test_with_negative_seconds(self):
        import datetime
        from google.protobuf import duration_pb2

        seconds = -1
        microseconds = 5
        timedelta_val = datetime.timedelta(seconds=seconds, microseconds=microseconds)
        result = self._call_fut(timedelta_val)
        self.assertIsInstance(result, duration_pb2.Duration)
        self.assertEqual(result.seconds, seconds + 1)
        self.assertEqual(result.nanos, -(10**9 - 1000 * microseconds))


class Test__duration_pb_to_timedelta(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import _duration_pb_to_timedelta

        return _duration_pb_to_timedelta(*args, **kwargs)

    def test_it(self):
        import datetime
        from google.protobuf import duration_pb2

        seconds = microseconds = 1
        duration_pb = duration_pb2.Duration(seconds=seconds, nanos=1000 * microseconds)
        timedelta_val = datetime.timedelta(seconds=seconds, microseconds=microseconds)
        result = self._call_fut(duration_pb)
        self.assertIsInstance(result, datetime.timedelta)
        self.assertEqual(result, timedelta_val)


class Test__name_from_project_path(unittest.TestCase):
    PROJECT = "PROJECT"
    THING_NAME = "THING_NAME"
    TEMPLATE = r"projects/(?P<project>\w+)/things/(?P<name>\w+)"

    def _call_fut(self, path, project, template):
        from google.cloud._helpers import _name_from_project_path

        return _name_from_project_path(path, project, template)

    def test_w_invalid_path_length(self):
        PATH = "projects/foo"
        with self.assertRaises(ValueError):
            self._call_fut(PATH, None, self.TEMPLATE)

    def test_w_invalid_path_segments(self):
        PATH = "foo/%s/bar/%s" % (self.PROJECT, self.THING_NAME)
        with self.assertRaises(ValueError):
            self._call_fut(PATH, self.PROJECT, self.TEMPLATE)

    def test_w_mismatched_project(self):
        PROJECT1 = "PROJECT1"
        PROJECT2 = "PROJECT2"
        PATH = "projects/%s/things/%s" % (PROJECT1, self.THING_NAME)
        with self.assertRaises(ValueError):
            self._call_fut(PATH, PROJECT2, self.TEMPLATE)

    def test_w_valid_data_w_compiled_regex(self):
        import re

        template = re.compile(self.TEMPLATE)
        PATH = "projects/%s/things/%s" % (self.PROJECT, self.THING_NAME)
        name = self._call_fut(PATH, self.PROJECT, template)
        self.assertEqual(name, self.THING_NAME)

    def test_w_project_passed_as_none(self):
        PROJECT1 = "PROJECT1"
        PATH = "projects/%s/things/%s" % (PROJECT1, self.THING_NAME)
        self._call_fut(PATH, None, self.TEMPLATE)
        name = self._call_fut(PATH, None, self.TEMPLATE)
        self.assertEqual(name, self.THING_NAME)


class Test_make_secure_channel(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import make_secure_channel

        return make_secure_channel(*args, **kwargs)

    def test_it(self):
        import http.client

        credentials = object()
        host = "HOST"
        user_agent = "USER_AGENT"

        secure_authorized_channel_patch = mock.patch(
            "google.auth.transport.grpc.secure_authorized_channel", autospec=True
        )

        with secure_authorized_channel_patch as secure_authorized_channel:
            result = self._call_fut(credentials, user_agent, host)

        self.assertIs(result, secure_authorized_channel.return_value)

        expected_target = "%s:%d" % (host, http.client.HTTPS_PORT)
        expected_options = (("grpc.primary_user_agent", user_agent),)

        secure_authorized_channel.assert_called_once_with(
            credentials, mock.ANY, expected_target, options=expected_options
        )

    def test_extra_options(self):
        import http.client

        credentials = object()
        host = "HOST"
        user_agent = "USER_AGENT"
        extra_options = (("some", "option"),)

        secure_authorized_channel_patch = mock.patch(
            "google.auth.transport.grpc.secure_authorized_channel", autospec=True
        )

        with secure_authorized_channel_patch as secure_authorized_channel:
            result = self._call_fut(credentials, user_agent, host, extra_options)

        self.assertIs(result, secure_authorized_channel.return_value)

        expected_target = "%s:%d" % (host, http.client.HTTPS_PORT)
        expected_options = (("grpc.primary_user_agent", user_agent), extra_options[0])

        secure_authorized_channel.assert_called_once_with(
            credentials, mock.ANY, expected_target, options=expected_options
        )


class Test_make_secure_stub(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import make_secure_stub

        return make_secure_stub(*args, **kwargs)

    def test_it(self):
        from google.cloud._testing import _Monkey
        from google.cloud import _helpers as MUT

        result = object()
        channel_obj = object()
        channels = []
        channel_args = []

        def stub_class(channel):
            channels.append(channel)
            return result

        def mock_channel(*args, **kwargs):
            channel_args.append(args)
            channel_args.append(kwargs)
            return channel_obj

        credentials = object()
        user_agent = "you-sir-age-int"
        host = "localhost"
        extra_options = {"extra_options": ()}
        with _Monkey(MUT, make_secure_channel=mock_channel):
            stub = self._call_fut(credentials, user_agent, stub_class, host)

        self.assertIs(stub, result)
        self.assertEqual(channels, [channel_obj])
        self.assertEqual(channel_args, [(credentials, user_agent, host), extra_options])


class Test_make_insecure_stub(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud._helpers import make_insecure_stub

        return make_insecure_stub(*args, **kwargs)

    def _helper(self, target, host, port=None):
        from google.cloud._testing import _Monkey
        from google.cloud import _helpers as MUT

        mock_result = object()
        stub_inputs = []
        CHANNEL = object()

        class _GRPCModule(object):
            def insecure_channel(self, *args):
                self.insecure_channel_args = args
                return CHANNEL

        grpc_mod = _GRPCModule()

        def mock_stub_class(channel):
            stub_inputs.append(channel)
            return mock_result

        with _Monkey(MUT, grpc=grpc_mod):
            result = self._call_fut(mock_stub_class, host, port=port)

        self.assertIs(result, mock_result)
        self.assertEqual(stub_inputs, [CHANNEL])
        self.assertEqual(grpc_mod.insecure_channel_args, (target,))

    def test_with_port_argument(self):
        host = "HOST"
        port = 1025
        target = "%s:%d" % (host, port)
        self._helper(target, host, port=port)

    def test_without_port_argument(self):
        host = "HOST:1114"
        self._helper(host, host)
