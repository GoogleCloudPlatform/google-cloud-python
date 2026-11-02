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

import itertools
from unittest import mock

import pytest
from google.api_core import exceptions as core_exceptions

from google.cloud.ndb import _retry, tasklets

from . import utils


def mock_sleep(seconds):
    future = tasklets.Future()
    future.set_result(None)
    return future


class Test_retry:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_success():
        def callback():
            return "foo"

        retry = _retry.retry_async(callback)
        assert retry().result() == "foo"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_nested_retry():
        def callback():
            def nested_callback():
                return "bar"

            nested = _retry.retry_async(nested_callback)
            assert nested().result() == "bar"

            return "foo"

        retry = _retry.retry_async(callback)
        assert retry().result() == "foo"

    @staticmethod
    @mock.patch("google.cloud.ndb.tasklets.sleep", mock_sleep)
    @pytest.mark.usefixtures("in_context")
    def test_nested_retry_with_exception():
        error = Exception("Fail")

        def callback():
            def nested_callback():
                raise error

            nested = _retry.retry_async(nested_callback, retries=1)
            return nested()

        with pytest.raises(core_exceptions.RetryError):
            retry = _retry.retry_async(callback, retries=1)
            retry().result()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_success_callback_is_tasklet():
        tasklet_future = tasklets.Future()

        @tasklets.tasklet
        def callback():
            result = yield tasklet_future
            raise tasklets.Return(result)

        retry = _retry.retry_async(callback)
        tasklet_future.set_result("foo")
        assert retry().result() == "foo"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_unhandled_error():
        error = Exception("Spurious error")

        def callback():
            raise error

        retry = _retry.retry_async(callback)
        assert retry().exception() is error

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_api_core_unknown():
        def callback():
            raise core_exceptions.Unknown("Unknown")

        with pytest.raises(core_exceptions.RetryError) as e:
            retry = _retry.retry_async(callback, retries=1)
            retry().result()

        assert e.value.cause == "google.api_core.exceptions.Unknown"

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_transient_error(core_retry, sleep):
        core_retry.exponential_sleep_generator.return_value = itertools.count()
        core_retry.if_transient_error.return_value = True

        sleep_future = tasklets.Future("sleep")
        sleep.return_value = sleep_future

        callback = mock.Mock(side_effect=[Exception("Spurious error."), "foo"])
        retry = _retry.retry_async(callback)
        sleep_future.set_result(None)
        assert retry().result() == "foo"

        sleep.assert_called_once_with(0)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_transient_error_callback_is_tasklet(core_retry, sleep):
        """Regression test for #519

        https://github.com/googleapis/python-ndb/issues/519
        """
        core_retry.exponential_sleep_generator.return_value = itertools.count()
        core_retry.if_transient_error.return_value = True

        sleep_future = tasklets.Future("sleep")
        sleep.return_value = sleep_future

        callback = mock.Mock(
            side_effect=[
                utils.future_exception(Exception("Spurious error.")),
                utils.future_result("foo"),
            ]
        )
        retry = _retry.retry_async(callback)
        future = retry()

        # This is the important check for the bug in #519. We need to make sure
        # that we're waiting for the sleep future to complete before moving on.
        assert future.running()

        # Finish sleeping
        sleep_future.set_result(None)
        assert future.result() == "foo"

        sleep.assert_called_once_with(0)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_too_many_transient_errors(core_retry, sleep):
        core_retry.exponential_sleep_generator.return_value = itertools.count()
        core_retry.if_transient_error.return_value = True

        sleep_future = tasklets.Future("sleep")
        sleep.return_value = sleep_future
        sleep_future.set_result(None)

        error = Exception("Spurious error")

        def callback():
            raise error

        retry = _retry.retry_async(callback)
        with pytest.raises(core_exceptions.RetryError) as error_context:
            retry().check_success()

        assert error_context.value.cause is error
        assert sleep.call_count == 4
        assert sleep.call_args[0][0] == 3

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_too_many_transient_errors_pass_retries(core_retry, sleep):
        core_retry.exponential_sleep_generator.return_value = itertools.count()
        core_retry.if_transient_error.return_value = True

        sleep_future = tasklets.Future("sleep")
        sleep.return_value = sleep_future
        sleep_future.set_result(None)

        error = Exception("Spurious error")

        def callback():
            raise error

        retry = _retry.retry_async(callback, retries=4)
        with pytest.raises(core_exceptions.RetryError) as error_context:
            retry().check_success()

        assert error_context.value.cause is error
        assert sleep.call_count == 5
        assert sleep.call_args[0][0] == 4


class Test_is_transient_error:
    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_core_says_yes(core_retry):
        error = object()
        core_retry.if_transient_error.return_value = True
        assert _retry.is_transient_error(error) is True
        core_retry.if_transient_error.assert_called_once_with(error)

    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_error_is_not_transient(core_retry):
        error = Exception("whatever")
        core_retry.if_transient_error.return_value = False
        assert _retry.is_transient_error(error) is False
        core_retry.if_transient_error.assert_called_once_with(error)

    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_unavailable(core_retry):
        error = core_exceptions.ServiceUnavailable("testing")
        core_retry.if_transient_error.return_value = False
        assert _retry.is_transient_error(error) is True
        core_retry.if_transient_error.assert_called_once_with(error)

    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_internal(core_retry):
        error = core_exceptions.InternalServerError("testing")
        core_retry.if_transient_error.return_value = False
        assert _retry.is_transient_error(error) is True
        core_retry.if_transient_error.assert_called_once_with(error)

    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_unauthenticated(core_retry):
        error = core_exceptions.Unauthenticated("testing")
        core_retry.if_transient_error.return_value = False
        assert _retry.is_transient_error(error) is False
        core_retry.if_transient_error.assert_called_once_with(error)

    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_aborted(core_retry):
        error = core_exceptions.Aborted("testing")
        core_retry.if_transient_error.return_value = False
        assert _retry.is_transient_error(error) is True
        core_retry.if_transient_error.assert_called_once_with(error)

    @staticmethod
    @mock.patch("google.cloud.ndb._retry.core_retry")
    def test_unknown(core_retry):
        error = core_exceptions.Unknown("testing")
        core_retry.if_transient_error.return_value = False
        assert _retry.is_transient_error(error) is True
        core_retry.if_transient_error.assert_called_once_with(error)
