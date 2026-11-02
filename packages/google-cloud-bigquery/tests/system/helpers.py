# Copyright 2021 Google LLC
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

import contextlib
import datetime
import decimal
import uuid

import google.api_core.exceptions
import test_utils.retry

from google.cloud._helpers import UTC

_naive = datetime.datetime(2016, 12, 5, 12, 41, 9)
_naive_microseconds = datetime.datetime(2016, 12, 5, 12, 41, 9, 250000)
_stamp = "%s %s" % (_naive.date().isoformat(), _naive.time().isoformat())
_date = _naive.date().isoformat()
_stamp_microseconds = _stamp + ".250000"
_zoned = _naive.replace(tzinfo=UTC)
_zoned_microseconds = _naive_microseconds.replace(tzinfo=UTC)
_numeric = decimal.Decimal("123456789.123456789")


# Examples of most data types to test with query() and DB-API.
STANDARD_SQL_EXAMPLES = [
    ("SELECT 1", 1),
    ("SELECT 1.3", 1.3),
    ("SELECT TRUE", True),
    ('SELECT "ABC"', "ABC"),
    ('SELECT CAST("foo" AS BYTES)', b"foo"),
    ('SELECT TIMESTAMP "%s"' % (_stamp,), _zoned),
    (
        'SELECT TIMESTAMP "%s"' % (_stamp_microseconds,),
        _zoned_microseconds,
    ),
    ('SELECT DATETIME(TIMESTAMP "%s")' % (_stamp,), _naive),
    (
        'SELECT DATETIME(TIMESTAMP "%s")' % (_stamp_microseconds,),
        _naive_microseconds,
    ),
    ('SELECT DATE(TIMESTAMP "%s")' % (_stamp,), _naive.date()),
    ('SELECT TIME(TIMESTAMP "%s")' % (_stamp,), _naive.time()),
    ('SELECT NUMERIC "%s"' % (_numeric,), _numeric),
    ("SELECT (1, 2)", {"_field_1": 1, "_field_2": 2}),
    (
        "SELECT ((1, 2), (3, 4), 5)",
        {
            "_field_1": {"_field_1": 1, "_field_2": 2},
            "_field_2": {"_field_1": 3, "_field_2": 4},
            "_field_3": 5,
        },
    ),
    ("SELECT [1, 2, 3]", [1, 2, 3]),
    (
        "SELECT ([1, 2], 3, [4, 5])",
        {"_field_1": [1, 2], "_field_2": 3, "_field_3": [4, 5]},
    ),
    (
        "SELECT [(1, 2, 3), (4, 5, 6)]",
        [
            {"_field_1": 1, "_field_2": 2, "_field_3": 3},
            {"_field_1": 4, "_field_2": 5, "_field_3": 6},
        ],
    ),
    (
        "SELECT [([1, 2, 3], 4), ([5, 6], 7)]",
        [{"_field_1": [1, 2, 3], "_field_2": 4}, {"_field_1": [5, 6], "_field_2": 7}],
    ),
    ("SELECT ARRAY(SELECT STRUCT([1, 2]))", [{"_field_1": [1, 2]}]),
    ("SELECT ST_GeogPoint(1, 2)", "POINT(1 2)"),
    (
        "SELECT RANGE<DATE> '[UNBOUNDED, %s)'" % _date,
        {"start": None, "end": _naive.date()},
    ),
]


def temp_suffix():
    now = datetime.datetime.now()
    return f"{now.strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"


def _rate_limit_exceeded(forbidden):
    """Predicate: pass only exceptions with 'rateLimitExceeded' as reason."""
    return any(error["reason"] == "rateLimitExceeded" for error in forbidden._errors)


# We need to wait to stay within the rate limits.
# The alternative outcome is a 403 Forbidden response from upstream, which
# they return instead of the more appropriate 429.
# See https://cloud.google.com/bigquery/quota-policy
retry_403 = test_utils.retry.RetryErrors(
    google.api_core.exceptions.Forbidden,
    error_predicate=_rate_limit_exceeded,
)


@contextlib.contextmanager
def patch_tracked_requests():
    """Context manager to patch google-auth requests and track/close their HTTP sessions.

    This prevents socket leaks in system tests that use Workload Identity or metadata server auth,
    including background Regional Access Boundary (RAB) refresh threads that deepcopy Request.
    """
    import threading
    import time
    import google.auth.transport.requests

    original_init = google.auth.transport.requests.Request.__init__
    # Only a __setstate__ defined on Request itself is put back on exit, so an
    # inherited one isn't copied onto the class.
    original_setstate = google.auth.transport.requests.Request.__dict__.get(
        "__setstate__"
    )
    tracked_requests = []

    def patched_init(self, session=None):
        original_init(self, session=session)
        if session is None:
            tracked_requests.append(self)

    def patched_setstate(self, state):
        # Regional Access Boundary (RAB) refresh threads in google-auth
        # copy.deepcopy() the Request object, which bypasses __init__ and
        # restores state via __setstate__. Track those cloned instances so
        # their urllib3 sessions are also closed on exit.
        if original_setstate is not None:
            original_setstate(self, state)
        else:
            self.__dict__.update(state)
        tracked_requests.append(self)

    google.auth.transport.requests.Request.__init__ = patched_init
    google.auth.transport.requests.Request.__setstate__ = patched_setstate
    try:
        yield tracked_requests
    finally:
        google.auth.transport.requests.Request.__init__ = original_init
        if original_setstate is not None:
            google.auth.transport.requests.Request.__setstate__ = original_setstate
        else:
            delattr(google.auth.transport.requests.Request, "__setstate__")
        # Wait up to 5 seconds in total for in-flight background RAB refresh
        # threads before closing the tracked HTTP sessions, so they don't open
        # a new socket after close().
        deadline = time.monotonic() + 5.0
        for thread in list(threading.enumerate()):
            if type(thread).__name__ == "_RegionalAccessBoundaryRefreshThread":
                thread.join(timeout=max(0.0, deadline - time.monotonic()))
        for req in tracked_requests:
            if hasattr(req, "session") and req.session is not None:
                req.session.close()
