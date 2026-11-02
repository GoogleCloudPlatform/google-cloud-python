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

import datetime
import re

import pytest

try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER  # noqa: F401
except ImportError:  # pragma: NO COVER
    import mock  # type: ignore

from google.api_core import exceptions, retry

from .test_retry_base import Test_BaseRetry


@mock.patch("time.sleep", autospec=True)
@mock.patch(
    "google.api_core.datetime_helpers.utcnow",
    return_value=datetime.datetime.min,
    autospec=True,
)
def test_retry_target_success(utcnow, sleep):
    predicate = retry.if_exception_type(ValueError)
    call_count = [0]

    def target():
        call_count[0] += 1
        if call_count[0] < 3:
            raise ValueError()
        return 42

    result = retry.retry_target(target, predicate, range(10), None)

    assert result == 42
    assert call_count[0] == 3
    sleep.assert_has_calls([mock.call(0), mock.call(1)])


@mock.patch("time.sleep", autospec=True)
@mock.patch(
    "google.api_core.datetime_helpers.utcnow",
    return_value=datetime.datetime.min,
    autospec=True,
)
def test_retry_target_w_on_error(utcnow, sleep):
    predicate = retry.if_exception_type(ValueError)
    call_count = {"target": 0}
    to_raise = ValueError()

    def target():
        call_count["target"] += 1
        if call_count["target"] < 3:
            raise to_raise
        return 42

    on_error = mock.Mock()

    result = retry.retry_target(target, predicate, range(10), None, on_error=on_error)

    assert result == 42
    assert call_count["target"] == 3

    on_error.assert_has_calls([mock.call(to_raise), mock.call(to_raise)])
    sleep.assert_has_calls([mock.call(0), mock.call(1)])


@mock.patch("time.sleep", autospec=True)
@mock.patch(
    "google.api_core.datetime_helpers.utcnow",
    return_value=datetime.datetime.min,
    autospec=True,
)
def test_retry_target_non_retryable_error(utcnow, sleep):
    predicate = retry.if_exception_type(ValueError)
    exception = TypeError()
    target = mock.Mock(side_effect=exception)

    with pytest.raises(TypeError) as exc_info:
        retry.retry_target(target, predicate, range(10), None)

    assert exc_info.value == exception
    sleep.assert_not_called()


@mock.patch("asyncio.sleep", autospec=True)
@mock.patch(
    "google.api_core.datetime_helpers.utcnow",
    return_value=datetime.datetime.min,
    autospec=True,
)
@pytest.mark.asyncio
async def test_retry_target_warning_for_retry(utcnow, sleep):
    predicate = retry.if_exception_type(ValueError)
    target = mock.AsyncMock(spec=["__call__"])

    with pytest.warns(Warning) as exc_info:
        # Note: predicate is just a filler and doesn't affect the test
        retry.retry_target(target, predicate, range(10), None)

    assert len(exc_info) == 2
    assert str(exc_info[0].message) == retry.retry_unary._ASYNC_RETRY_WARNING
    sleep.assert_not_called()


@mock.patch("time.sleep", autospec=True)
@mock.patch("time.monotonic", autospec=True)
@pytest.mark.parametrize("use_deadline_arg", [True, False])
def test_retry_target_timeout_exceeded(monotonic, sleep, use_deadline_arg):
    predicate = retry.if_exception_type(ValueError)
    exception = ValueError("meep")
    target = mock.Mock(side_effect=exception)
    # Setup the timeline so that the first call takes 5 seconds but the second
    # call takes 6, which puts the retry over the timeout.
    monotonic.side_effect = [0, 5, 11]

    # support "deadline" as an alias for "timeout"
    kwargs = {"timeout": 10} if not use_deadline_arg else {"deadline": 10}

    with pytest.raises(exceptions.RetryError) as exc_info:
        retry.retry_target(target, predicate, range(10), **kwargs)

    assert exc_info.value.cause == exception
    assert exc_info.match("Timeout of 10.0s exceeded")
    assert exc_info.match("last exception: meep")
    assert target.call_count == 2

    # Ensure the exception message does not include the target fn:
    # it may be a partial with user data embedded
    assert str(target) not in exc_info.exconly()


def test_retry_target_bad_sleep_generator():
    with pytest.raises(ValueError, match="Sleep generator"):
        retry.retry_target(mock.sentinel.target, lambda x: True, [], None)


@mock.patch("time.sleep", autospec=True)
def test_retry_target_dynamic_backoff(sleep):
    """
    sleep_generator should be iterated after on_error, to support dynamic backoff
    """
    sleep.side_effect = RuntimeError("stop after sleep")
    # start with empty sleep generator; values are added after exception in push_sleep_value
    sleep_values = []
    exception = ValueError("trigger retry")
    error_target = mock.Mock(side_effect=exception)
    inserted_sleep = 99

    def push_sleep_value(err):
        sleep_values.append(inserted_sleep)

    with pytest.raises(RuntimeError):
        retry.retry_target(
            error_target,
            predicate=lambda x: True,
            sleep_generator=sleep_values,
            on_error=push_sleep_value,
        )
    assert sleep.call_count == 1
    sleep.assert_called_once_with(inserted_sleep)


class TestRetry(Test_BaseRetry):
    def _make_one(self, *args, **kwargs):
        return retry.Retry(*args, **kwargs)

    def test___str__(self):
        def if_exception_type(exc):
            return bool(exc)  # pragma: NO COVER

        # Explicitly set all attributes as changed Retry defaults should not
        # cause this test to start failing.
        retry_ = retry.Retry(
            predicate=if_exception_type,
            initial=1.0,
            maximum=60.0,
            multiplier=2.0,
            timeout=120.0,
            on_error=None,
        )
        assert re.match(
            (
                r"<Retry predicate=<function.*?if_exception_type.*?>, "
                r"initial=1.0, maximum=60.0, multiplier=2.0, timeout=120.0, "
                r"on_error=None>"
            ),
            str(retry_),
        )

    @mock.patch("time.sleep", autospec=True)
    def test___call___and_execute_success(self, sleep):
        retry_ = retry.Retry()
        target = mock.Mock(spec=["__call__"], return_value=42)
        # __name__ is needed by functools.partial.
        target.__name__ = "target"

        decorated = retry_(target)
        target.assert_not_called()

        result = decorated("meep")

        assert result == 42
        target.assert_called_once_with("meep")
        sleep.assert_not_called()

    @mock.patch("random.uniform", autospec=True, side_effect=lambda m, n: n)
    @mock.patch("time.sleep", autospec=True)
    def test___call___and_execute_retry(self, sleep, uniform):
        on_error = mock.Mock(spec=["__call__"], side_effect=[None])
        retry_ = retry.Retry(predicate=retry.if_exception_type(ValueError))

        target = mock.Mock(spec=["__call__"], side_effect=[ValueError(), 42])
        # __name__ is needed by functools.partial.
        target.__name__ = "target"

        decorated = retry_(target, on_error=on_error)
        target.assert_not_called()

        result = decorated("meep")

        assert result == 42
        assert target.call_count == 2
        target.assert_has_calls([mock.call("meep"), mock.call("meep")])
        sleep.assert_called_once_with(retry_._initial)
        assert on_error.call_count == 1

    @mock.patch("random.uniform", autospec=True, side_effect=lambda m, n: n)
    @mock.patch("time.sleep", autospec=True)
    def test___call___and_execute_retry_hitting_timeout(self, sleep, uniform):
        on_error = mock.Mock(spec=["__call__"], side_effect=[None] * 10)
        retry_ = retry.Retry(
            predicate=retry.if_exception_type(ValueError),
            initial=1.0,
            maximum=1024.0,
            multiplier=2.0,
            timeout=30.9,
        )

        monotonic_patcher = mock.patch("time.monotonic", return_value=0)

        target = mock.Mock(spec=["__call__"], side_effect=[ValueError()] * 10)
        # __name__ is needed by functools.partial.
        target.__name__ = "target"

        decorated = retry_(target, on_error=on_error)
        target.assert_not_called()

        with monotonic_patcher as patched_monotonic:
            # Make sure that calls to fake time.sleep() also advance the mocked
            # time clock.
            def increase_time(sleep_delay):
                patched_monotonic.return_value += sleep_delay

            sleep.side_effect = increase_time

            with pytest.raises(exceptions.RetryError):
                decorated("meep")

        assert target.call_count == 5
        target.assert_has_calls([mock.call("meep")] * 5)
        assert on_error.call_count == 5

        # check the delays
        assert sleep.call_count == 4  # once between each successive target calls
        last_wait = sleep.call_args.args[0]
        total_wait = sum(call_args.args[0] for call_args in sleep.call_args_list)

        assert last_wait == 8.0
        # Next attempt would be scheduled in 16 secs, 15 + 16 = 31 > 30.9, thus
        # we do not even wait for it to be scheduled (30.9 is configured timeout).
        # This changes the previous logic of shortening the last attempt to fit
        # in the timeout. The previous logic was removed to make Python retry
        # logic consistent with the other languages and to not disrupt the
        # randomized retry delays distribution by artificially increasing a
        # probability of scheduling two (instead of one) last attempts with very
        # short delay between them, while the second retry having very low chance
        # of succeeding anyways.
        assert total_wait == 15.0

    @mock.patch("time.sleep", autospec=True)
    def test___init___without_retry_executed(self, sleep):
        _some_function = mock.Mock()

        retry_ = retry.Retry(
            predicate=retry.if_exception_type(ValueError), on_error=_some_function
        )
        # check the proper creation of the class
        assert retry_._on_error is _some_function

        target = mock.Mock(spec=["__call__"], side_effect=[42])
        # __name__ is needed by functools.partial.
        target.__name__ = "target"

        wrapped = retry_(target)

        result = wrapped("meep")

        assert result == 42
        target.assert_called_once_with("meep")
        sleep.assert_not_called()
        _some_function.assert_not_called()

    @mock.patch("random.uniform", autospec=True, side_effect=lambda m, n: n)
    @mock.patch("time.sleep", autospec=True)
    def test___init___when_retry_is_executed(self, sleep, uniform):
        _some_function = mock.Mock()

        retry_ = retry.Retry(
            predicate=retry.if_exception_type(ValueError), on_error=_some_function
        )
        # check the proper creation of the class
        assert retry_._on_error is _some_function

        target = mock.Mock(
            spec=["__call__"], side_effect=[ValueError(), ValueError(), 42]
        )
        # __name__ is needed by functools.partial.
        target.__name__ = "target"

        wrapped = retry_(target)
        target.assert_not_called()

        result = wrapped("meep")

        assert result == 42
        assert target.call_count == 3
        assert _some_function.call_count == 2
        target.assert_has_calls([mock.call("meep"), mock.call("meep")])
        sleep.assert_any_call(retry_._initial)
