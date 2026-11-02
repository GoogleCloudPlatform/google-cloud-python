# Copyright 2017 Google LLC
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

import itertools
import re
from unittest import mock

import pytest
import requests.exceptions
from google.auth import exceptions as auth_exceptions

from google.api_core import exceptions, retry


def test_if_exception_type():
    predicate = retry.if_exception_type(ValueError)

    assert predicate(ValueError())
    assert not predicate(TypeError())


def test_if_exception_type_multiple():
    predicate = retry.if_exception_type(ValueError, TypeError)

    assert predicate(ValueError())
    assert predicate(TypeError())
    assert not predicate(RuntimeError())


def test_if_transient_error():
    assert retry.if_transient_error(exceptions.InternalServerError(""))
    assert retry.if_transient_error(exceptions.TooManyRequests(""))
    assert retry.if_transient_error(exceptions.ServiceUnavailable(""))
    assert retry.if_transient_error(requests.exceptions.ConnectionError(""))
    assert retry.if_transient_error(requests.exceptions.ChunkedEncodingError(""))
    assert retry.if_transient_error(auth_exceptions.TransportError(""))
    assert not retry.if_transient_error(exceptions.InvalidArgument(""))


# Make uniform return half of its maximum, which will be the calculated
# sleep time.
@mock.patch("random.uniform", autospec=True, side_effect=lambda m, n: n)
def test_exponential_sleep_generator_base_2(uniform):
    gen = retry.exponential_sleep_generator(1, 60, multiplier=2)

    result = list(itertools.islice(gen, 8))
    assert result == [1, 2, 4, 8, 16, 32, 60, 60]


def test_build_retry_error_empty_list():
    """
    attempt to build a retry error with no errors encountered
    should return a generic RetryError
    """
    from google.api_core.retry import RetryFailureReason, build_retry_error

    reason = RetryFailureReason.NON_RETRYABLE_ERROR
    src, cause = build_retry_error([], reason, 10)
    assert isinstance(src, exceptions.RetryError)
    assert cause is None
    assert src.message == "Unknown error"


def test_build_retry_error_preserves_cause():
    """
    build_retry_error should preserve __cause__ from chained exceptions.
    """
    from google.api_core.retry import RetryFailureReason, build_retry_error

    # Create an exception with explicit cause
    cause = ValueError("root cause")
    exc = RuntimeError("wrapper")
    exc.__cause__ = cause

    src, found_cause = build_retry_error(
        [exc], RetryFailureReason.NON_RETRYABLE_ERROR, None
    )

    assert src is exc
    assert found_cause is cause


def test_build_retry_error_timeout_message():
    """
    should provide helpful error message when timeout is reached
    """
    from google.api_core.retry import RetryFailureReason, build_retry_error

    reason = RetryFailureReason.TIMEOUT
    cause = RuntimeError("timeout")
    src, found_cause = build_retry_error([ValueError(), cause], reason, 10)
    assert isinstance(src, exceptions.RetryError)
    assert src.message == "Timeout of 10.0s exceeded"
    # should attach appropriate cause
    assert found_cause is cause


def test_build_retry_error_empty_timeout():
    """
    attempt to build a retry error when timeout is None
    should return a generic timeout error message
    """
    from google.api_core.retry import RetryFailureReason, build_retry_error

    reason = RetryFailureReason.TIMEOUT
    src, _ = build_retry_error([], reason, None)
    assert isinstance(src, exceptions.RetryError)
    assert src.message == "Timeout exceeded"


class Test_BaseRetry(object):
    def _make_one(self, *args, **kwargs):
        return retry.retry_base._BaseRetry(*args, **kwargs)

    def test_constructor_defaults(self):
        retry_ = self._make_one()
        assert retry_._predicate == retry.if_transient_error
        assert retry_._initial == 1
        assert retry_._maximum == 60
        assert retry_._multiplier == 2
        assert retry_._timeout == 120
        assert retry_._on_error is None
        assert retry_.timeout == 120
        assert retry_.timeout == 120

    def test_constructor_options(self):
        _some_function = mock.Mock()

        retry_ = self._make_one(
            predicate=mock.sentinel.predicate,
            initial=1,
            maximum=2,
            multiplier=3,
            timeout=4,
            on_error=_some_function,
        )
        assert retry_._predicate == mock.sentinel.predicate
        assert retry_._initial == 1
        assert retry_._maximum == 2
        assert retry_._multiplier == 3
        assert retry_._timeout == 4
        assert retry_._on_error is _some_function

    @pytest.mark.parametrize("use_deadline", [True, False])
    @pytest.mark.parametrize("value", [None, 0, 1, 4, 42, 5.5])
    def test_with_timeout(self, use_deadline, value):
        retry_ = self._make_one(
            predicate=mock.sentinel.predicate,
            initial=1,
            maximum=2,
            multiplier=3,
            timeout=4,
            on_error=mock.sentinel.on_error,
        )
        new_retry = (
            retry_.with_timeout(value)
            if not use_deadline
            else retry_.with_deadline(value)
        )
        assert retry_ is not new_retry
        assert new_retry._timeout == value
        assert (
            new_retry.timeout == value
            if not use_deadline
            else new_retry.deadline == value
        )

        # the rest of the attributes should remain the same
        assert new_retry._predicate is retry_._predicate
        assert new_retry._initial == retry_._initial
        assert new_retry._maximum == retry_._maximum
        assert new_retry._multiplier == retry_._multiplier
        assert new_retry._on_error is retry_._on_error

    def test_with_predicate(self):
        retry_ = self._make_one(
            predicate=mock.sentinel.predicate,
            initial=1,
            maximum=2,
            multiplier=3,
            timeout=4,
            on_error=mock.sentinel.on_error,
        )
        new_retry = retry_.with_predicate(mock.sentinel.predicate)
        assert retry_ is not new_retry
        assert new_retry._predicate == mock.sentinel.predicate

        # the rest of the attributes should remain the same
        assert new_retry._timeout == retry_._timeout
        assert new_retry._initial == retry_._initial
        assert new_retry._maximum == retry_._maximum
        assert new_retry._multiplier == retry_._multiplier
        assert new_retry._on_error is retry_._on_error

    def test_with_delay_noop(self):
        retry_ = self._make_one(
            predicate=mock.sentinel.predicate,
            initial=1,
            maximum=2,
            multiplier=3,
            timeout=4,
            on_error=mock.sentinel.on_error,
        )
        new_retry = retry_.with_delay()
        assert retry_ is not new_retry
        assert new_retry._initial == retry_._initial
        assert new_retry._maximum == retry_._maximum
        assert new_retry._multiplier == retry_._multiplier

    @pytest.mark.parametrize(
        "originals,updated,expected",
        [
            [(1, 2, 3), (4, 5, 6), (4, 5, 6)],
            [(1, 2, 3), (0, 0, 0), (0, 0, 0)],
            [(1, 2, 3), (None, None, None), (1, 2, 3)],
            [(0, 0, 0), (None, None, None), (0, 0, 0)],
            [(1, 2, 3), (None, 0.5, None), (1, 0.5, 3)],
            [(1, 2, 3), (None, 0.5, 4), (1, 0.5, 4)],
            [(1, 2, 3), (9, None, None), (9, 2, 3)],
        ],
    )
    def test_with_delay(self, originals, updated, expected):
        retry_ = self._make_one(
            predicate=mock.sentinel.predicate,
            initial=originals[0],
            maximum=originals[1],
            multiplier=originals[2],
            timeout=14,
            on_error=mock.sentinel.on_error,
        )
        new_retry = retry_.with_delay(
            initial=updated[0], maximum=updated[1], multiplier=updated[2]
        )
        assert retry_ is not new_retry
        assert new_retry._initial == expected[0]
        assert new_retry._maximum == expected[1]
        assert new_retry._multiplier == expected[2]

        # the rest of the attributes should remain the same
        assert new_retry._timeout == retry_._timeout
        assert new_retry._predicate is retry_._predicate
        assert new_retry._on_error is retry_._on_error

    def test_with_delay_partial_options(self):
        retry_ = self._make_one(
            predicate=mock.sentinel.predicate,
            initial=1,
            maximum=2,
            multiplier=3,
            timeout=4,
            on_error=mock.sentinel.on_error,
        )
        new_retry = retry_.with_delay(initial=4)
        assert retry_ is not new_retry
        assert new_retry._initial == 4
        assert new_retry._maximum == 2
        assert new_retry._multiplier == 3

        new_retry = retry_.with_delay(maximum=4)
        assert retry_ is not new_retry
        assert new_retry._initial == 1
        assert new_retry._maximum == 4
        assert new_retry._multiplier == 3

        new_retry = retry_.with_delay(multiplier=4)
        assert retry_ is not new_retry
        assert new_retry._initial == 1
        assert new_retry._maximum == 2
        assert new_retry._multiplier == 4

        # the rest of the attributes should remain the same
        assert new_retry._timeout == retry_._timeout
        assert new_retry._predicate is retry_._predicate
        assert new_retry._on_error is retry_._on_error

    def test___str__(self):
        def if_exception_type(exc):
            return bool(exc)  # pragma: NO COVER

        # Explicitly set all attributes as changed Retry defaults should not
        # cause this test to start failing.
        retry_ = self._make_one(
            predicate=if_exception_type,
            initial=1.0,
            maximum=60.0,
            multiplier=2.0,
            timeout=120.0,
            on_error=None,
        )
        assert re.match(
            (
                r"<_BaseRetry predicate=<function.*?if_exception_type.*?>, "
                r"initial=1.0, maximum=60.0, multiplier=2.0, timeout=120.0, "
                r"on_error=None>"
            ),
            str(retry_),
        )
