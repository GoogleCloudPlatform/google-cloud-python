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
import logging
from unittest import mock

import pytest
from google.api_core import exceptions as core_exceptions

from google.cloud.ndb import _transaction, exceptions, tasklets
from google.cloud.ndb import context as context_module


class Test_in_transaction:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_false():
        assert _transaction.in_transaction() is False

    @staticmethod
    def test_true(in_context):
        with in_context.new(transaction=b"tx123").use():
            assert _transaction.in_transaction() is True


class Test_transaction:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_propagation_nested():
        with pytest.raises(exceptions.BadRequestError):
            _transaction.transaction(
                None, propagation=context_module.TransactionOptions.NESTED
            )

    @staticmethod
    def test_already_in_transaction(in_context):
        with in_context.new(transaction=b"tx123").use():
            with pytest.raises(NotImplementedError):
                _transaction.transaction(None)

    @staticmethod
    def test_transaction_inherits_and_merges_cache(in_context):
        original_cache = in_context.cache
        in_context.cache["test"] = "original value"
        with in_context.new(transaction=b"tx123").use() as new_context:
            assert new_context.cache is not original_cache
            assert new_context.cache["test"] == original_cache["test"]
            new_context.cache["test"] = "new_value"
            assert new_context.cache["test"] != original_cache["test"]
        assert in_context.cache["test"] == "new_value"

    @staticmethod
    @mock.patch("google.cloud.ndb._transaction.transaction_async")
    def test_success(transaction_async):
        transaction_async.return_value.result.return_value = 42
        assert _transaction.transaction("callback") == 42
        transaction_async.assert_called_once_with(
            "callback",
            read_only=False,
            retries=3,
            join=False,
            xg=True,
            propagation=None,
        )


class Test_transaction_async:
    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_success(_datastore_api):
        context_module.get_context().cache["foo"] = "bar"

        def callback():
            # The transaction uses its own in-memory cache, which should be empty in
            # the transaction context and not include the key set above.
            context = context_module.get_context()
            assert not context.cache

            return "I tried, momma."

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        future = _transaction.transaction_async(callback)

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_success_w_callbacks(_datastore_api):
        context_module.get_context().cache["foo"] = "bar"
        on_commit_callback = mock.Mock()
        transaction_complete_callback = mock.Mock()

        def callback():
            # The transaction uses its own in-memory cache, which should be empty in
            # the transaction context and not include the key set above.
            context = context_module.get_context()
            assert not context.cache

            context.call_on_commit(on_commit_callback)
            context.call_on_transaction_complete(transaction_complete_callback)
            return "I tried, momma."

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        future = _transaction.transaction_async(callback)

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."
        on_commit_callback.assert_called_once_with()
        transaction_complete_callback.assert_called_once_with()

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_failure_w_callbacks(_datastore_api):
        class SpuriousError(Exception):
            pass

        context_module.get_context().cache["foo"] = "bar"
        on_commit_callback = mock.Mock()
        transaction_complete_callback = mock.Mock()

        def callback():
            context = context_module.get_context()
            assert not context.cache
            context.call_on_commit(on_commit_callback)
            context.call_on_transaction_complete(transaction_complete_callback)
            raise SpuriousError()

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        rollback_future = tasklets.Future("rollback transaction")
        _datastore_api.rollback.return_value = rollback_future

        future = _transaction.transaction_async(callback)

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.commit.assert_not_called()
        _datastore_api.rollback.assert_called_once_with(b"tx123")
        rollback_future.set_result(None)

        with pytest.raises(SpuriousError):
            future.result()

        on_commit_callback.assert_not_called()
        transaction_complete_callback.assert_called_once_with()

    @staticmethod
    def test_success_join(in_context):
        def callback():
            return "I tried, momma."

        with in_context.new(transaction=b"tx123").use():
            future = _transaction.transaction_async(callback, join=True)

        assert future.result() == "I tried, momma."

    @staticmethod
    def test_success_join_callback_returns_future(in_context):
        future = tasklets.Future()

        def callback():
            return future

        with in_context.new(transaction=b"tx123").use():
            future = _transaction.transaction_async(callback, join=True)

        future.set_result("I tried, momma.")
        assert future.result() == "I tried, momma."

    @staticmethod
    def test_success_propagation_mandatory(in_context):
        def callback():
            return "I tried, momma."

        with mock.patch(
            "google.cloud.ndb._transaction.transaction_async_",
            side_effect=_transaction.transaction_async_,
        ) as transaction_async_:
            with in_context.new(transaction=b"tx123").use():
                future = _transaction.transaction_async(
                    callback,
                    join=False,
                    propagation=context_module.TransactionOptions.MANDATORY,
                )

        assert future.result() == "I tried, momma."

        transaction_async_.assert_called_once_with(
            callback,
            3,
            False,
            True,
            True,
            None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_failure_propagation_mandatory():
        with pytest.raises(exceptions.BadRequestError):
            _transaction.transaction_async(
                None,
                join=False,
                propagation=context_module.TransactionOptions.MANDATORY,
            )

    @staticmethod
    def test_invalid_propagation():
        with pytest.raises(ValueError):
            _transaction.transaction_async(
                None,
                propagation=99,
            )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_invalid_join(caplog, in_context):
        def callback():
            return "I tried, momma."

        provided_join_arg = False

        with mock.patch(
            "google.cloud.ndb._transaction.transaction_async_",
            side_effect=_transaction.transaction_async_,
        ) as transaction_async_:
            with in_context.new(transaction=b"tx123").use():
                with caplog.at_level(logging.WARNING):
                    future = _transaction.transaction_async(
                        callback,
                        join=provided_join_arg,
                        propagation=context_module.TransactionOptions.MANDATORY,
                    )

        assert future.result() == "I tried, momma."
        assert "Modifying join behaviour to maintain old NDB behaviour" in caplog.text

        transaction_async_.assert_called_once_with(
            callback,
            3,
            False,
            True,
            (not provided_join_arg),
            None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_propagation_with_no_join_arg(caplog):
        with caplog.at_level(logging.WARNING):
            ctx, join = _transaction._Propagation(
                context_module.TransactionOptions.ALLOWED
            ).handle_propagation()
        assert (
            "Modifying join behaviour to maintain old NDB behaviour" not in caplog.text
        )
        assert ctx is None
        assert join

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    def test_failure_propagation():
        with pytest.raises(exceptions.NoLongerImplementedError):
            _transaction.transaction_async_(
                None,
                propagation=context_module.TransactionOptions.ALLOWED,
            )

    @staticmethod
    def test_propagation_allowed_already_in_transaction(in_context):
        def callback():
            return "I tried, momma."

        with mock.patch(
            "google.cloud.ndb._transaction.transaction_async_",
            side_effect=_transaction.transaction_async_,
        ) as transaction_async_:
            with in_context.new(transaction=b"tx123").use():
                future = _transaction.transaction_async(
                    callback,
                    join=False,
                    propagation=context_module.TransactionOptions.ALLOWED,
                )

        assert future.result() == "I tried, momma."

        transaction_async_.assert_called_once_with(
            callback,
            3,
            False,
            True,
            True,
            None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_propagation_allowed_not_yet_in_transaction(_datastore_api):
        def callback():
            return "I tried, momma."

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        with mock.patch(
            "google.cloud.ndb._transaction.transaction_async_",
            side_effect=_transaction.transaction_async_,
        ) as transaction_async_:
            future = _transaction.transaction_async(
                callback,
                join=False,
                propagation=context_module.TransactionOptions.ALLOWED,
            )

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."

        transaction_async_.assert_called_once_with(
            callback,
            3,
            False,
            True,
            True,
            None,
        )

    @staticmethod
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_propagation_independent_already_in_transaction(_datastore_api, in_context):
        def callback():
            return "I tried, momma."

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        with mock.patch(
            "google.cloud.ndb._transaction.transaction_async_",
            side_effect=_transaction.transaction_async_,
        ) as transaction_async_:
            with in_context.new(transaction=b"tx123").use():
                future = _transaction.transaction_async(
                    callback,
                    join=True,
                    propagation=context_module.TransactionOptions.INDEPENDENT,
                )

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx456")

        _datastore_api.commit.assert_called_once_with(b"tx456", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."

        transaction_async_.assert_called_once_with(
            callback,
            3,
            False,
            False,
            True,
            None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_propagation_independent_not_yet_in_transaction(_datastore_api):
        def callback():
            return "I tried, momma."

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        with mock.patch(
            "google.cloud.ndb._transaction.transaction_async_",
            side_effect=_transaction.transaction_async_,
        ) as transaction_async_:
            future = _transaction.transaction_async(
                callback,
                join=False,
                propagation=context_module.TransactionOptions.INDEPENDENT,
            )

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."

        transaction_async_.assert_called_once_with(
            callback,
            3,
            False,
            False,
            True,
            None,
        )

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_success_no_retries(_datastore_api):
        def callback():
            return "I tried, momma."

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        future = _transaction.transaction_async(callback, retries=0)

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_success_callback_is_tasklet(_datastore_api):
        tasklet = tasklets.Future("tasklet")

        def callback():
            return tasklet

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future

        future = _transaction.transaction_async(callback)

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        tasklet.set_result("I tried, momma.")

        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)
        commit_future.set_result(None)

        assert future.result() == "I tried, momma."

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_run_inner_loop(_datastore_api):
        begin_futures = [
            tasklets.Future("begin transaction 1"),
            tasklets.Future("begin transaction 2"),
        ]
        _datastore_api.begin_transaction.side_effect = begin_futures

        commit_futures = [
            tasklets.Future("commit transaction 1"),
            tasklets.Future("commit transaction 2"),
        ]
        _datastore_api.commit.side_effect = commit_futures

        @tasklets.tasklet
        def callback():
            # Scheduling the sleep call here causes control to go back up to
            # the main loop before this tasklet, running in the transaction
            # loop, has finished, forcing a call to run_inner_loop via the idle
            # handler.
            yield tasklets.sleep(0)

        @tasklets.tasklet
        def some_tasklet():
            # This tasklet runs in the main loop. In order to get results back
            # from the transaction_async calls, the run_inner_loop idle handler
            # will have to be run.
            yield [
                _transaction.transaction_async(callback),
                _transaction.transaction_async(callback),
            ]

            # Scheduling this sleep call forces the run_inner_loop idle handler
            # to be run again so we can run it in the case when there is no
            # more work to be done in the transaction. (Branch coverage.)
            yield tasklets.sleep(0)

            raise tasklets.Return("I tried, momma.")

        future = some_tasklet()

        begin_futures[0].set_result(b"tx123")
        begin_futures[1].set_result(b"tx234")
        commit_futures[0].set_result(None)
        commit_futures[1].set_result(None)

        assert future.result() == "I tried, momma."

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_error(_datastore_api):
        error = Exception("Spurious error.")

        def callback():
            raise error

        begin_future = tasklets.Future("begin transaction")
        _datastore_api.begin_transaction.return_value = begin_future

        rollback_future = tasklets.Future("rollback transaction")
        _datastore_api.rollback.return_value = rollback_future

        future = _transaction.transaction_async(callback)

        _datastore_api.begin_transaction.assert_called_once_with(False, retries=0)
        begin_future.set_result(b"tx123")

        _datastore_api.rollback.assert_called_once_with(b"tx123")
        rollback_future.set_result(None)

        assert future.exception() is error

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._retry.core_retry")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_transient_error(_datastore_api, core_retry, sleep):
        core_retry.exponential_sleep_generator.return_value = itertools.count()
        core_retry.if_transient_error.return_value = True

        callback = mock.Mock(side_effect=[Exception("Spurious error."), "foo"])

        begin_future = tasklets.Future("begin transaction")
        begin_future.set_result(b"tx123")
        _datastore_api.begin_transaction.return_value = begin_future

        rollback_future = tasklets.Future("rollback transaction")
        _datastore_api.rollback.return_value = rollback_future
        rollback_future.set_result(None)

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future
        commit_future.set_result(None)

        sleep_future = tasklets.Future("sleep")
        sleep_future.set_result(None)
        sleep.return_value = sleep_future

        future = _transaction.transaction_async(callback)
        assert future.result() == "foo"

        _datastore_api.begin_transaction.call_count == 2
        _datastore_api.rollback.assert_called_once_with(b"tx123")
        sleep.assert_called_once_with(0)
        _datastore_api.commit.assert_called_once_with(b"tx123", retries=0)

    @staticmethod
    @pytest.mark.usefixtures("in_context")
    @mock.patch("google.cloud.ndb.tasklets.sleep")
    @mock.patch("google.cloud.ndb._retry.core_retry")
    @mock.patch("google.cloud.ndb._datastore_api")
    def test_too_many_transient_errors(_datastore_api, core_retry, sleep):
        core_retry.exponential_sleep_generator.return_value = itertools.count()
        core_retry.if_transient_error.return_value = True

        error = Exception("Spurious error.")

        def callback():
            raise error

        begin_future = tasklets.Future("begin transaction")
        begin_future.set_result(b"tx123")
        _datastore_api.begin_transaction.return_value = begin_future

        rollback_future = tasklets.Future("rollback transaction")
        _datastore_api.rollback.return_value = rollback_future
        rollback_future.set_result(None)

        commit_future = tasklets.Future("commit transaction")
        _datastore_api.commit.return_value = commit_future
        commit_future.set_result(None)

        sleep_future = tasklets.Future("sleep")
        sleep_future.set_result(None)
        sleep.return_value = sleep_future

        future = _transaction.transaction_async(callback)
        with pytest.raises(core_exceptions.RetryError) as error_context:
            future.check_success()

        assert error_context.value.cause is error

        assert _datastore_api.begin_transaction.call_count == 4
        assert _datastore_api.rollback.call_count == 4
        assert sleep.call_count == 4
        _datastore_api.commit.assert_not_called()


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api")
def test_transactional(_datastore_api):
    @_transaction.transactional()
    def simple_function(a, b):
        return a + b

    begin_future = tasklets.Future("begin transaction")
    _datastore_api.begin_transaction.return_value = begin_future

    commit_future = tasklets.Future("commit transaction")
    _datastore_api.commit.return_value = commit_future

    begin_future.set_result(b"tx123")
    commit_future.set_result(None)

    res = simple_function(100, 42)
    assert res == 142


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api")
def test_transactional_async(_datastore_api):
    @_transaction.transactional_async()
    def simple_function(a, b):
        return a + b

    begin_future = tasklets.Future("begin transaction")
    _datastore_api.begin_transaction.return_value = begin_future

    commit_future = tasklets.Future("commit transaction")
    _datastore_api.commit.return_value = commit_future

    begin_future.set_result(b"tx123")
    commit_future.set_result(None)

    res = simple_function(100, 42)
    assert res.result() == 142


@pytest.mark.usefixtures("in_context")
@mock.patch("google.cloud.ndb._datastore_api")
def test_transactional_tasklet(_datastore_api):
    @_transaction.transactional_tasklet()
    def generator_function(dependency):
        value = yield dependency
        raise tasklets.Return(value + 42)

    begin_future = tasklets.Future("begin transaction")
    _datastore_api.begin_transaction.return_value = begin_future

    commit_future = tasklets.Future("commit transaction")
    _datastore_api.commit.return_value = commit_future

    begin_future.set_result(b"tx123")
    commit_future.set_result(None)

    dependency = tasklets.Future()
    dependency.set_result(100)

    res = generator_function(dependency)
    assert res.result() == 142


@pytest.mark.usefixtures("in_context")
def test_non_transactional_out_of_transaction():
    @_transaction.non_transactional()
    def simple_function(a, b):
        return a + b

    res = simple_function(100, 42)
    assert res == 142


@pytest.mark.usefixtures("in_context")
def test_non_transactional_in_transaction(in_context):
    with in_context.new(transaction=b"tx123").use():

        def simple_function(a, b):
            return a + b

        wrapped_function = _transaction.non_transactional()(simple_function)

        res = wrapped_function(100, 42)
        assert res == 142

        with pytest.raises(exceptions.BadRequestError):
            wrapped_function = _transaction.non_transactional(allow_existing=False)(
                simple_function
            )
            wrapped_function(100, 42)
