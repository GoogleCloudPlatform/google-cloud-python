# Copyright 2020 Google LLC
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

import asyncio
import datetime
import re

try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER  # noqa: F401
except ImportError:  # pragma: NO COVER
    import mock  # type: ignore

import pytest

from google.api_core import exceptions, retry_async
from google.api_core.retry import retry_streaming_async

from ...unit.retry.test_retry_base import Test_BaseRetry


@pytest.mark.asyncio
async def test_retry_streaming_target_bad_sleep_generator():
    from google.api_core.retry.retry_streaming_async import retry_target_stream

    with pytest.raises(ValueError, match="Sleep generator"):
        await retry_target_stream(None, lambda x: True, [], None).__anext__()


@mock.patch("asyncio.sleep", autospec=True)
@pytest.mark.asyncio
async def test_retry_streaming_target_dynamic_backoff(sleep):
    """
    sleep_generator should be iterated after on_error, to support dynamic backoff
    """
    from functools import partial

    from google.api_core.retry.retry_streaming_async import retry_target_stream

    sleep.side_effect = RuntimeError("stop after sleep")
    # start with empty sleep generator; values are added after exception in push_sleep_value
    sleep_values = []
    error_target = partial(TestAsyncStreamingRetry._generator_mock, error_on=0)
    inserted_sleep = 99

    def push_sleep_value(err):
        sleep_values.append(inserted_sleep)

    with pytest.raises(RuntimeError):
        await retry_target_stream(
            error_target,
            predicate=lambda x: True,
            sleep_generator=sleep_values,
            on_error=push_sleep_value,
        ).__anext__()
    assert sleep.call_count == 1
    sleep.assert_called_once_with(inserted_sleep)


class TestAsyncStreamingRetry(Test_BaseRetry):
    def _make_one(self, *args, **kwargs):
        return retry_streaming_async.AsyncStreamingRetry(*args, **kwargs)

    def test___str__(self):
        def if_exception_type(exc):
            return bool(exc)  # pragma: NO COVER

        # Explicitly set all attributes as changed Retry defaults should not
        # cause this test to start failing.
        retry_ = retry_streaming_async.AsyncStreamingRetry(
            predicate=if_exception_type,
            initial=1.0,
            maximum=60.0,
            multiplier=2.0,
            timeout=120.0,
            on_error=None,
        )
        assert re.match(
            (
                r"<AsyncStreamingRetry predicate=<function.*?if_exception_type.*?>, "
                r"initial=1.0, maximum=60.0, multiplier=2.0, timeout=120.0, "
                r"on_error=None>"
            ),
            str(retry_),
        )

    @staticmethod
    async def _generator_mock(
        num=5,
        error_on=None,
        exceptions_seen=None,
        sleep_time=0,
    ):
        """
        Helper to create a mock generator that yields a number of values
        Generator can optionally raise an exception on a specific iteration

        Args:
          - num (int): the number of values to yield
          - error_on (int): if given, the generator will raise a ValueError on the specified iteration
          - exceptions_seen (list): if given, the generator will append any exceptions to this list before raising
          - sleep_time (int): if given, the generator will asyncio.sleep for this many seconds before yielding each value
        """
        try:
            for i in range(num):
                if sleep_time:
                    await asyncio.sleep(sleep_time)
                if error_on is not None and i == error_on:
                    raise ValueError("generator mock error")
                yield i
        except (Exception, BaseException, GeneratorExit) as e:
            # keep track of exceptions seen by generator
            if exceptions_seen is not None:
                exceptions_seen.append(e)
            raise

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___generator_success(self, sleep):
        """
        Test that a retry-decorated generator yields values as expected
        This test checks a generator with no issues
        """
        from collections.abc import AsyncGenerator

        retry_ = retry_streaming_async.AsyncStreamingRetry()
        decorated = retry_(self._generator_mock)

        num = 10
        generator = await decorated(num)
        # check types
        assert isinstance(generator, AsyncGenerator)
        assert isinstance(self._generator_mock(num), AsyncGenerator)
        # check yield contents
        unpacked = [i async for i in generator]
        assert len(unpacked) == num
        expected = [i async for i in self._generator_mock(num)]
        for a, b in zip(unpacked, expected):
            assert a == b
        sleep.assert_not_called()

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___generator_retry(self, sleep):
        """
        Tests that a retry-decorated generator will retry on errors
        """
        on_error = mock.Mock(return_value=None)
        retry_ = retry_streaming_async.AsyncStreamingRetry(
            on_error=on_error,
            predicate=retry_async.if_exception_type(ValueError),
            timeout=None,
        )
        generator = await retry_(self._generator_mock)(error_on=3)
        # error thrown on 3
        # generator should contain 0, 1, 2 looping
        unpacked = [await generator.__anext__() for i in range(10)]
        assert unpacked == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
        assert on_error.call_count == 3
        await generator.aclose()

    @mock.patch("random.uniform", autospec=True, side_effect=lambda m, n: n)
    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.parametrize("use_deadline_arg", [True, False])
    @pytest.mark.asyncio
    async def test___call___generator_retry_hitting_timeout(
        self, sleep, uniform, use_deadline_arg
    ):
        """
        Tests that a retry-decorated generator will throw a RetryError
        after using the time budget
        """
        import time

        timeout_val = 9.9
        # support "deadline" as an alias for "timeout"
        timeout_kwarg = (
            {"timeout": timeout_val}
            if not use_deadline_arg
            else {"deadline": timeout_val}
        )

        on_error = mock.Mock()
        retry_ = retry_streaming_async.AsyncStreamingRetry(
            predicate=retry_async.if_exception_type(ValueError),
            initial=1.0,
            maximum=1024.0,
            multiplier=2.0,
            **timeout_kwarg,
        )

        time_now = time.monotonic()
        now_patcher = mock.patch(
            "time.monotonic",
            return_value=time_now,
        )

        decorated = retry_(self._generator_mock, on_error=on_error)
        generator = await decorated(error_on=1)

        with now_patcher as patched_now:
            # Make sure that calls to fake asyncio.sleep() also advance the mocked
            # time clock.
            def increase_time(sleep_delay):
                patched_now.return_value += sleep_delay

            sleep.side_effect = increase_time

            with pytest.raises(exceptions.RetryError):
                [i async for i in generator]

        assert on_error.call_count == 4
        # check the delays
        assert sleep.call_count == 3  # once between each successive target calls
        last_wait = sleep.call_args.args[0]
        total_wait = sum(call_args.args[0] for call_args in sleep.call_args_list)
        # next wait would have put us over, so ended early
        assert last_wait == 4
        assert total_wait == 7

    @pytest.mark.asyncio
    async def test___call___generator_cancellations(self):
        """
        cancel calls should propagate to the generator
        """
        # test without cancel as retryable
        retry_ = retry_streaming_async.AsyncStreamingRetry()
        utcnow = datetime.datetime.now(datetime.timezone.utc)
        mock.patch("google.api_core.datetime_helpers.utcnow", return_value=utcnow)
        generator = await retry_(self._generator_mock)(sleep_time=0.2)
        assert await generator.__anext__() == 0
        task = asyncio.create_task(generator.__anext__())
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        with pytest.raises(StopAsyncIteration):
            await generator.__anext__()

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_generator_send(self, sleep):
        """
        Send should be passed through retry into target generator
        """

        async def _mock_send_gen():
            """
            always yield whatever was sent in
            """
            in_ = yield
            while True:
                in_ = yield in_

        retry_ = retry_streaming_async.AsyncStreamingRetry()

        decorated = retry_(_mock_send_gen)

        generator = await decorated()
        result = await generator.__anext__()
        # first yield should be None
        assert result is None
        in_messages = ["test_1", "hello", "world"]
        out_messages = []
        for msg in in_messages:
            recv = await generator.asend(msg)
            out_messages.append(recv)
        assert in_messages == out_messages
        await generator.aclose()

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___generator_send_retry(self, sleep):
        """
        Send should be retried if target generator raises an error
        """
        on_error = mock.Mock(return_value=None)
        retry_ = retry_streaming_async.AsyncStreamingRetry(
            on_error=on_error,
            predicate=retry_async.if_exception_type(ValueError),
            timeout=None,
        )
        generator = await retry_(self._generator_mock)(error_on=3)
        with pytest.raises(TypeError) as exc_info:
            await generator.asend("cannot send to fresh generator")
        assert exc_info.match("can't send non-None value")
        await generator.aclose()

        # error thrown on 3
        # generator should contain 0, 1, 2 looping
        generator = await retry_(self._generator_mock)(error_on=3)
        assert await generator.__anext__() == 0
        unpacked = [await generator.asend(i) for i in range(10)]
        assert unpacked == [1, 2, 0, 1, 2, 0, 1, 2, 0, 1]
        assert on_error.call_count == 3
        await generator.aclose()

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_generator_close(self, sleep):
        """
        Close should be passed through retry into target generator
        """
        retry_ = retry_streaming_async.AsyncStreamingRetry()
        decorated = retry_(self._generator_mock)
        exception_list = []
        generator = await decorated(10, exceptions_seen=exception_list)
        for i in range(2):
            await generator.__anext__()
        await generator.aclose()

        assert isinstance(exception_list[0], GeneratorExit)
        with pytest.raises(StopAsyncIteration):
            # calling next on closed generator should raise error
            await generator.__anext__()

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_new_generator_close(self, sleep):
        """
        Close should be passed through retry into target generator,
        even when it hasn't been iterated yet
        """
        retry_ = retry_streaming_async.AsyncStreamingRetry()
        decorated = retry_(self._generator_mock)
        exception_list = []
        generator = await decorated(10, exceptions_seen=exception_list)
        await generator.aclose()

        with pytest.raises(StopAsyncIteration):
            # calling next on closed generator should raise error
            await generator.__anext__()

    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_generator_throw(self, sleep):
        """
        Throw should be passed through retry into target generator
        """

        # The generator should not retry when it encounters a non-retryable error
        retry_ = retry_streaming_async.AsyncStreamingRetry(
            predicate=retry_async.if_exception_type(ValueError),
        )
        decorated = retry_(self._generator_mock)
        exception_list = []
        generator = await decorated(10, exceptions_seen=exception_list)
        for i in range(2):
            await generator.__anext__()
        with pytest.raises(BufferError):
            await generator.athrow(BufferError("test"))
        assert isinstance(exception_list[0], BufferError)
        with pytest.raises(StopAsyncIteration):
            # calling next on closed generator should raise error
            await generator.__anext__()

        # In contrast, the generator should retry if we throw a retryable exception
        exception_list = []
        generator = await decorated(10, exceptions_seen=exception_list)
        for i in range(2):
            await generator.__anext__()
        throw_val = await generator.athrow(ValueError("test"))
        assert throw_val == 0
        assert isinstance(exception_list[0], ValueError)
        # calling next on generator should not raise error, because it was retried
        assert await generator.__anext__() == 1

    @pytest.mark.parametrize("awaitable_wrapped", [True, False])
    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_iterable_send(self, sleep, awaitable_wrapped):
        """
        Send should work like next if the wrapped iterable does not support it
        """
        retry_ = retry_streaming_async.AsyncStreamingRetry()

        def iterable_fn():
            class CustomIterable:
                def __init__(self):
                    self.i = -1

                def __aiter__(self):
                    return self

                async def __anext__(self):
                    self.i += 1
                    return self.i

            return CustomIterable()

        if awaitable_wrapped:

            async def wrapper():
                return iterable_fn()

            decorated = retry_(wrapper)
        else:
            decorated = retry_(iterable_fn)

        retryable = await decorated()
        # initiate the generator by calling next
        result = await retryable.__anext__()
        assert result == 0
        # test sending values
        assert await retryable.asend("test") == 1
        assert await retryable.asend("test2") == 2
        assert await retryable.asend("test3") == 3
        await retryable.aclose()

    @pytest.mark.parametrize("awaitable_wrapped", [True, False])
    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_iterable_close(self, sleep, awaitable_wrapped):
        """
        close should be handled by wrapper if wrapped iterable does not support it
        """
        retry_ = retry_streaming_async.AsyncStreamingRetry()

        def iterable_fn():
            class CustomIterable:
                def __init__(self):
                    self.i = -1

                def __aiter__(self):
                    return self

                async def __anext__(self):
                    self.i += 1
                    return self.i

            return CustomIterable()

        if awaitable_wrapped:

            async def wrapper():
                return iterable_fn()

            decorated = retry_(wrapper)
        else:
            decorated = retry_(iterable_fn)

        # try closing active generator
        retryable = await decorated()
        assert await retryable.__anext__() == 0
        await retryable.aclose()
        with pytest.raises(StopAsyncIteration):
            await retryable.__anext__()
        # try closing new generator
        new_retryable = await decorated()
        await new_retryable.aclose()
        with pytest.raises(StopAsyncIteration):
            await new_retryable.__anext__()

    @pytest.mark.parametrize("awaitable_wrapped", [True, False])
    @mock.patch("asyncio.sleep", autospec=True)
    @pytest.mark.asyncio
    async def test___call___with_iterable_throw(self, sleep, awaitable_wrapped):
        """
        Throw should work even if the wrapped iterable does not support it
        """

        predicate = retry_async.if_exception_type(ValueError)
        retry_ = retry_streaming_async.AsyncStreamingRetry(predicate=predicate)

        def iterable_fn():
            class CustomIterable:
                def __init__(self):
                    self.i = -1

                def __aiter__(self):
                    return self

                async def __anext__(self):
                    self.i += 1
                    return self.i

            return CustomIterable()

        if awaitable_wrapped:

            async def wrapper():
                return iterable_fn()

            decorated = retry_(wrapper)
        else:
            decorated = retry_(iterable_fn)

        # try throwing with active generator
        retryable = await decorated()
        assert await retryable.__anext__() == 0
        # should swallow errors in predicate
        await retryable.athrow(ValueError("test"))
        # should raise errors not in predicate
        with pytest.raises(BufferError):
            await retryable.athrow(BufferError("test"))
        with pytest.raises(StopAsyncIteration):
            await retryable.__anext__()
        # try throwing with new generator
        new_retryable = await decorated()
        with pytest.raises(BufferError):
            await new_retryable.athrow(BufferError("test"))
        with pytest.raises(StopAsyncIteration):
            await new_retryable.__anext__()

    @pytest.mark.asyncio
    async def test_exc_factory_non_retryable_error(self):
        """
        generator should give the option to override exception creation logic
        test when non-retryable error is thrown
        """
        from google.api_core.retry import RetryFailureReason
        from google.api_core.retry.retry_streaming_async import retry_target_stream

        timeout = 6
        sent_errors = [ValueError("test"), ValueError("test2"), BufferError("test3")]
        expected_final_err = RuntimeError("done")
        expected_source_err = ZeroDivisionError("test4")

        def factory(*args, **kwargs):
            assert len(kwargs) == 0
            assert args[0] == sent_errors
            assert args[1] == RetryFailureReason.NON_RETRYABLE_ERROR
            assert args[2] == timeout
            return expected_final_err, expected_source_err

        generator = retry_target_stream(
            self._generator_mock,
            retry_async.if_exception_type(ValueError),
            [0] * 3,
            timeout=timeout,
            exception_factory=factory,
        )
        # initialize the generator
        await generator.__anext__()
        # trigger some retryable errors
        await generator.athrow(sent_errors[0])
        await generator.athrow(sent_errors[1])
        # trigger a non-retryable error
        with pytest.raises(expected_final_err.__class__) as exc_info:
            await generator.athrow(sent_errors[2])
        assert exc_info.value == expected_final_err
        assert exc_info.value.__cause__ == expected_source_err

    @pytest.mark.asyncio
    async def test_exc_factory_timeout(self):
        """
        generator should give the option to override exception creation logic
        test when timeout is exceeded
        """
        import time

        from google.api_core.retry import RetryFailureReason
        from google.api_core.retry.retry_streaming_async import retry_target_stream

        timeout = 2
        time_now = time.monotonic()
        now_patcher = mock.patch(
            "time.monotonic",
            return_value=time_now,
        )

        with now_patcher as patched_now:
            timeout = 2
            sent_errors = [ValueError("test"), ValueError("test2"), ValueError("test3")]
            expected_final_err = RuntimeError("done")
            expected_source_err = ZeroDivisionError("test4")

            def factory(*args, **kwargs):
                assert len(kwargs) == 0
                assert args[0] == sent_errors
                assert args[1] == RetryFailureReason.TIMEOUT
                assert args[2] == timeout
                return expected_final_err, expected_source_err

            generator = retry_target_stream(
                self._generator_mock,
                retry_async.if_exception_type(ValueError),
                [0] * 3,
                timeout=timeout,
                exception_factory=factory,
            )
            # initialize the generator
            await generator.__anext__()
            # trigger some retryable errors
            await generator.athrow(sent_errors[0])
            await generator.athrow(sent_errors[1])
            # trigger a timeout
            patched_now.return_value += timeout + 1
            with pytest.raises(expected_final_err.__class__) as exc_info:
                await generator.athrow(sent_errors[2])
            assert exc_info.value == expected_final_err
            assert exc_info.value.__cause__ == expected_source_err
