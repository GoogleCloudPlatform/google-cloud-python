# Copyright 2024 Google LLC
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

from unittest import mock

import pytest
from google.api_core.exceptions import DeadlineExceeded, Forbidden
from google.rpc import status_pb2

from google.cloud.bigtable.data._cross_sync import CrossSync
from google.cloud.bigtable.data._metrics import ActiveOperationMetric
from google.cloud.bigtable.data.mutations import DeleteAllFromRow, RowMutationEntry
from google.cloud.bigtable_v2.types import MutateRowsResponse

__CROSS_SYNC_OUTPUT__ = "tests.unit.data._sync_autogen.test__mutate_rows"


@CrossSync.convert_class("TestMutateRowsOperation")
class TestMutateRowsOperationAsync:
    def _target_class(self):
        return CrossSync._MutateRowsOperation

    def _make_one(self, *args, **kwargs):
        if not args:
            fake_target = CrossSync.Mock()
            fake_target._request_path = {"table_name": "table"}
            fake_target.app_profile_id = None
            kwargs["gapic_client"] = kwargs.pop("gapic_client", mock.Mock())
            kwargs["target"] = kwargs.pop("target", fake_target)
            kwargs["operation_timeout"] = kwargs.pop("operation_timeout", 5)
            kwargs["attempt_timeout"] = kwargs.pop("attempt_timeout", 0.1)
            kwargs["retryable_exceptions"] = kwargs.pop("retryable_exceptions", ())
            kwargs["mutation_entries"] = kwargs.pop("mutation_entries", [])
            kwargs["metric"] = kwargs.pop(
                "metric", ActiveOperationMetric("MUTATE_ROWS")
            )
        return self._target_class()(*args, **kwargs)

    def _make_mutation(self, count=1, size=1):
        mutation = RowMutationEntry("k", [DeleteAllFromRow() for _ in range(count)])
        mutation.size = lambda: size
        return mutation

    @CrossSync.convert
    async def _mock_stream(self, mutation_list, error_dict, omit_indices=None):
        omit_indices = omit_indices or set()
        for idx, entry in enumerate(mutation_list):
            if idx in omit_indices:
                # simulate a server that closes the stream OK without returning
                # a response entry for this mutation
                continue
            code = error_dict.get(idx, 0)
            yield MutateRowsResponse(
                entries=[
                    MutateRowsResponse.Entry(
                        index=idx, status=status_pb2.Status(code=code)
                    )
                ]
            )

    def _make_mock_gapic(self, mutation_list, error_dict=None, omit_indices=None):
        mock_fn = CrossSync.Mock()
        if error_dict is None:
            error_dict = {}
        mock_fn.side_effect = lambda *args, **kwargs: self._mock_stream(
            mutation_list, error_dict, omit_indices
        )
        return mock_fn

    def test_ctor(self):
        """
        test that constructor sets all the attributes correctly
        """
        from google.api_core.exceptions import Aborted, DeadlineExceeded

        from google.cloud.bigtable.data._async._mutate_rows import _EntryWithProto
        from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete

        client = mock.Mock()
        table = mock.Mock()
        entries = [self._make_mutation(), self._make_mutation()]
        operation_timeout = 0.05
        attempt_timeout = 0.01
        metric = mock.Mock()
        retryable_exceptions = ()
        instance = self._make_one(
            client,
            table,
            entries,
            operation_timeout,
            attempt_timeout,
            metric,
            retryable_exceptions,
        )
        # running gapic_fn should trigger a client call with baked-in args
        assert client.mutate_rows.call_count == 0
        instance._gapic_fn()
        assert client.mutate_rows.call_count == 1
        # entries should be passed down
        entries_w_pb = [_EntryWithProto(e, e._to_pb()) for e in entries]
        assert instance.mutations == entries_w_pb
        # timeout_gen should generate per-attempt timeout
        assert next(instance.timeout_generator) == attempt_timeout
        # ensure predicate is set
        assert instance.is_retryable is not None
        assert instance.is_retryable(DeadlineExceeded("")) is False
        assert instance.is_retryable(Aborted("")) is False
        assert instance.is_retryable(_MutateRowsIncomplete("")) is True
        assert instance.is_retryable(RuntimeError("")) is False
        assert instance.remaining_indices == list(range(len(entries)))
        assert instance.errors == {}
        assert instance._operation_metric == metric

    def test_ctor_too_many_entries(self):
        """
        should raise an error if an operation is created with more than 100,000 entries
        """
        from google.cloud.bigtable.data._async._mutate_rows import (
            _MUTATE_ROWS_REQUEST_MUTATION_LIMIT,
        )

        assert _MUTATE_ROWS_REQUEST_MUTATION_LIMIT == 100_000

        client = mock.Mock()
        table = mock.Mock()
        entries = [self._make_mutation()] * (_MUTATE_ROWS_REQUEST_MUTATION_LIMIT + 1)
        operation_timeout = 0.05
        attempt_timeout = 0.01
        with pytest.raises(ValueError) as e:
            self._make_one(
                client,
                table,
                entries,
                operation_timeout,
                attempt_timeout,
                mock.Mock(),
            )
        assert "mutate_rows requests can contain at most 100000 mutations" in str(
            e.value
        )
        assert "Found 100001" in str(e.value)

    @CrossSync.pytest
    async def test_mutate_rows_operation(self):
        """
        Test successful case of mutate_rows_operation
        """
        client = mock.Mock()
        table = mock.Mock()
        metric = ActiveOperationMetric("MUTATE_ROWS")
        entries = [self._make_mutation(), self._make_mutation()]
        operation_timeout = 0.05
        cls = self._target_class()
        with mock.patch(
            f"{cls.__module__}.{cls.__name__}._run_attempt", CrossSync.Mock()
        ) as attempt_mock:
            instance = self._make_one(
                client, table, entries, operation_timeout, operation_timeout, metric
            )
            await instance.start()
            assert attempt_mock.call_count == 1

    @pytest.mark.parametrize("exc_type", [RuntimeError, ZeroDivisionError, Forbidden])
    @CrossSync.pytest
    async def test_mutate_rows_attempt_exception(self, exc_type):
        """
        exceptions raised from attempt should be raised in MutationsExceptionGroup
        """
        client = CrossSync.Mock()
        table = mock.Mock()
        table._request_path = {"table_name": "table"}
        metric = ActiveOperationMetric("MUTATE_ROWS")
        table.app_profile_id = None
        entries = [self._make_mutation(), self._make_mutation()]
        operation_timeout = 0.05
        expected_exception = exc_type("test")
        client.mutate_rows.side_effect = expected_exception
        found_exc = None
        try:
            instance = self._make_one(
                client, table, entries, operation_timeout, operation_timeout, metric
            )
            await instance._run_attempt()
        except Exception as e:
            found_exc = e
        assert client.mutate_rows.call_count == 1
        assert type(found_exc) is exc_type
        assert found_exc == expected_exception
        assert len(instance.errors) == 2
        assert len(instance.remaining_indices) == 0

    @pytest.mark.parametrize("exc_type", [RuntimeError, ZeroDivisionError, Forbidden])
    @CrossSync.pytest
    async def test_mutate_rows_exception(self, exc_type):
        """
        exceptions raised from retryable should be raised in MutationsExceptionGroup
        """
        from google.cloud.bigtable.data.exceptions import (
            FailedMutationEntryError,
            MutationsExceptionGroup,
        )

        client = mock.Mock()
        table = mock.Mock()
        metric = ActiveOperationMetric("MUTATE_ROWS")
        entries = [self._make_mutation(), self._make_mutation()]
        operation_timeout = 0.05
        expected_cause = exc_type("abort")
        with mock.patch.object(
            self._target_class(),
            "_run_attempt",
            CrossSync.Mock(),
        ) as attempt_mock:
            attempt_mock.side_effect = expected_cause
            found_exc = None
            try:
                instance = self._make_one(
                    client, table, entries, operation_timeout, operation_timeout, metric
                )
                await instance.start()
            except MutationsExceptionGroup as e:
                found_exc = e
            assert attempt_mock.call_count == 1
            assert len(found_exc.exceptions) == 2
            assert isinstance(found_exc.exceptions[0], FailedMutationEntryError)
            assert isinstance(found_exc.exceptions[1], FailedMutationEntryError)
            assert found_exc.exceptions[0].__cause__ == expected_cause
            assert found_exc.exceptions[1].__cause__ == expected_cause

    @pytest.mark.parametrize(
        "exc_type",
        [DeadlineExceeded, RuntimeError],
    )
    @CrossSync.pytest
    async def test_mutate_rows_exception_retryable_eventually_pass(self, exc_type):
        """
        If an exception fails but eventually passes, it should not raise an exception
        """

        client = mock.Mock()
        table = mock.Mock()
        metric = ActiveOperationMetric("MUTATE_ROWS")
        entries = [self._make_mutation()]
        operation_timeout = 1
        expected_cause = exc_type("retry")
        num_retries = 2
        with mock.patch.object(
            self._target_class(),
            "_run_attempt",
            CrossSync.Mock(),
        ) as attempt_mock:
            attempt_mock.side_effect = [expected_cause] * num_retries + [None]
            instance = self._make_one(
                client,
                table,
                entries,
                operation_timeout,
                operation_timeout,
                metric,
                retryable_exceptions=(exc_type,),
            )
            await instance.start()
            assert attempt_mock.call_count == num_retries + 1

    @CrossSync.pytest
    async def test_mutate_rows_incomplete_ignored(self):
        """
        MutateRowsIncomplete exceptions should not be added to error list
        """
        from google.api_core.exceptions import DeadlineExceeded

        from google.cloud.bigtable.data.exceptions import (
            MutationsExceptionGroup,
            _MutateRowsIncomplete,
        )

        client = mock.Mock()
        table = mock.Mock()
        metric = ActiveOperationMetric("MUTATE_ROWS")
        entries = [self._make_mutation()]
        operation_timeout = 0.05
        with mock.patch.object(
            self._target_class(),
            "_run_attempt",
            CrossSync.Mock(),
        ) as attempt_mock:
            attempt_mock.side_effect = _MutateRowsIncomplete("ignored")
            found_exc = None
            try:
                instance = self._make_one(
                    client, table, entries, operation_timeout, operation_timeout, metric
                )
                await instance.start()
            except MutationsExceptionGroup as e:
                found_exc = e
            assert attempt_mock.call_count > 0
            assert len(found_exc.exceptions) == 1
            assert isinstance(found_exc.exceptions[0].__cause__, DeadlineExceeded)

    @CrossSync.pytest
    async def test_run_attempt_single_entry_success(self):
        """Test mutating a single entry"""
        mutation = self._make_mutation()
        expected_timeout = 1.3
        mock_gapic_fn = self._make_mock_gapic({0: mutation})
        instance = self._make_one(
            mutation_entries=[mutation],
            attempt_timeout=expected_timeout,
        )
        with mock.patch.object(instance, "_gapic_fn", mock_gapic_fn):
            await instance._run_attempt()
        assert len(instance.remaining_indices) == 0
        assert mock_gapic_fn.call_count == 1
        _, kwargs = mock_gapic_fn.call_args
        assert kwargs["timeout"] == expected_timeout
        request = kwargs["request"]
        assert request.entries == [mutation._to_pb()]

    @CrossSync.pytest
    async def test_run_attempt_empty_request(self):
        """Calling with no mutations should result in no API calls"""
        mock_gapic_fn = self._make_mock_gapic([])
        instance = self._make_one(
            mutation_entries=[],
        )
        await instance._run_attempt()
        assert mock_gapic_fn.call_count == 0

    @CrossSync.pytest
    async def test_run_attempt_partial_success_retryable(self):
        """Some entries succeed, but one fails. Should report the proper index, and raise incomplete exception"""
        from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete

        success_mutation = self._make_mutation()
        success_mutation_2 = self._make_mutation()
        failure_mutation = self._make_mutation()
        mutations = [success_mutation, failure_mutation, success_mutation_2]
        mock_gapic_fn = self._make_mock_gapic(mutations, error_dict={1: 300})
        instance = self._make_one(
            mutation_entries=mutations,
        )
        instance.is_retryable = lambda x: True
        with mock.patch.object(instance, "_gapic_fn", mock_gapic_fn):
            with pytest.raises(_MutateRowsIncomplete):
                await instance._run_attempt()
        assert instance.remaining_indices == [1]
        assert 0 not in instance.errors
        assert len(instance.errors[1]) == 1
        assert instance.errors[1][0].grpc_status_code == 300
        assert 2 not in instance.errors

    @CrossSync.pytest
    async def test_run_attempt_partial_success_non_retryable(self):
        """Some entries succeed, but one fails. Exception marked as non-retryable. Do not raise incomplete error"""
        success_mutation = self._make_mutation()
        success_mutation_2 = self._make_mutation()
        failure_mutation = self._make_mutation()
        mutations = [success_mutation, failure_mutation, success_mutation_2]
        mock_gapic_fn = self._make_mock_gapic(mutations, error_dict={1: 300})
        instance = self._make_one(
            mutation_entries=mutations,
        )
        instance.is_retryable = lambda x: False
        with mock.patch.object(instance, "_gapic_fn", mock_gapic_fn):
            await instance._run_attempt()
        assert instance.remaining_indices == []
        assert 0 not in instance.errors
        assert len(instance.errors[1]) == 1
        assert instance.errors[1][0].grpc_status_code == 300
        assert 2 not in instance.errors

    @CrossSync.pytest
    async def test_run_attempt_missing_entry_retryable(self):
        """If the server closes the stream successfully but omits a response
        entry, the unanswered mutation must not be treated as successful. It
        should be recorded as a retryable _MutateRowsIncomplete error so
        idempotent entries are retried."""
        from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete

        mutations = [
            self._make_mutation(),
            self._make_mutation(),
            self._make_mutation(),
        ]
        # server omits the response entry for index 1
        mock_gapic_fn = self._make_mock_gapic(mutations, omit_indices={1})
        instance = self._make_one(mutation_entries=mutations)
        instance.is_retryable = lambda x: True
        with mock.patch.object(instance, "_gapic_fn", mock_gapic_fn):
            with pytest.raises(_MutateRowsIncomplete):
                await instance._run_attempt()
        assert instance.remaining_indices == [1]
        assert 0 not in instance.errors
        assert len(instance.errors[1]) == 1
        assert isinstance(instance.errors[1][0], _MutateRowsIncomplete)
        assert 2 not in instance.errors

    @CrossSync.pytest
    async def test_run_attempt_missing_entry_non_retryable(self):
        """A missing response entry for a non-retryable mutation is surfaced as
        a failure rather than being silently dropped."""
        from google.cloud.bigtable.data.exceptions import _MutateRowsIncomplete

        mutations = [self._make_mutation(), self._make_mutation()]
        # server omits the response entry for index 0
        mock_gapic_fn = self._make_mock_gapic(mutations, omit_indices={0})
        instance = self._make_one(mutation_entries=mutations)
        instance.is_retryable = lambda x: False
        with mock.patch.object(instance, "_gapic_fn", mock_gapic_fn):
            await instance._run_attempt()
        assert instance.remaining_indices == []
        assert len(instance.errors[0]) == 1
        assert isinstance(instance.errors[0][0], _MutateRowsIncomplete)
        assert 1 not in instance.errors
