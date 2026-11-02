# Copyright 2023 Google LLC
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

import sys
import unittest
from unittest import mock

import pytest

import google.cloud.bigtable.data.exceptions as bigtable_exceptions


class TracebackTests311:
    """
    Provides a set of tests that should be run on python 3.11 and above,
    to verify that the exception traceback looks as expected
    """

    @pytest.mark.skipif(
        sys.version_info < (3, 11), reason="requires python3.11 or higher"
    )
    def test_311_traceback(self):
        """
        Exception customizations should not break rich exception group traceback in python 3.11
        """
        import traceback

        sub_exc1 = RuntimeError("first sub exception")
        sub_exc2 = ZeroDivisionError("second sub exception")
        sub_group = self._make_one(excs=[sub_exc2])
        exc_group = self._make_one(excs=[sub_exc1, sub_group])

        expected_traceback = (
            f"  | google.cloud.bigtable.data.exceptions.{type(exc_group).__name__}: {str(exc_group)}",
            "  +-+---------------- 1 ----------------",
            "    | RuntimeError: first sub exception",
            "    +---------------- 2 ----------------",
            f"    | google.cloud.bigtable.data.exceptions.{type(sub_group).__name__}: {str(sub_group)}",
            "    +-+---------------- 1 ----------------",
            "      | ZeroDivisionError: second sub exception",
            "      +------------------------------------",
        )
        exception_caught = False
        try:
            raise exc_group
        except self._get_class():
            exception_caught = True
            tb = traceback.format_exc()
            tb_relevant_lines = tuple(tb.splitlines()[3:])
            assert expected_traceback == tb_relevant_lines
        assert exception_caught

    @pytest.mark.skipif(
        sys.version_info < (3, 11), reason="requires python3.11 or higher"
    )
    def test_311_traceback_with_cause(self):
        """
        traceback should display nicely with sub-exceptions with __cause__ set
        """
        import traceback

        sub_exc1 = RuntimeError("first sub exception")
        cause_exc = ImportError("cause exception")
        sub_exc1.__cause__ = cause_exc
        sub_exc2 = ZeroDivisionError("second sub exception")
        exc_group = self._make_one(excs=[sub_exc1, sub_exc2])

        expected_traceback = (
            f"  | google.cloud.bigtable.data.exceptions.{type(exc_group).__name__}: {str(exc_group)}",
            "  +-+---------------- 1 ----------------",
            "    | ImportError: cause exception",
            "    | ",
            "    | The above exception was the direct cause of the following exception:",
            "    | ",
            "    | RuntimeError: first sub exception",
            "    +---------------- 2 ----------------",
            "    | ZeroDivisionError: second sub exception",
            "    +------------------------------------",
        )
        exception_caught = False
        try:
            raise exc_group
        except self._get_class():
            exception_caught = True
            tb = traceback.format_exc()
            tb_relevant_lines = tuple(tb.splitlines()[3:])
            assert expected_traceback == tb_relevant_lines
        assert exception_caught

    @pytest.mark.skipif(
        sys.version_info < (3, 11), reason="requires python3.11 or higher"
    )
    def test_311_exception_group(self):
        """
        Python 3.11+ should handle exepctions as native exception groups
        """
        exceptions = [RuntimeError("mock"), ValueError("mock")]
        instance = self._make_one(excs=exceptions)
        # ensure split works as expected
        runtime_error, others = instance.split(lambda e: isinstance(e, RuntimeError))
        assert runtime_error.exceptions[0] == exceptions[0]
        assert others.exceptions[0] == exceptions[1]


class TracebackTests310:
    """
    Provides a set of tests that should be run on python 3.10 and under,
    to verify that the exception traceback looks as expected
    """

    @pytest.mark.skipif(
        sys.version_info >= (3, 11), reason="requires python3.10 or lower"
    )
    def test_310_traceback(self):
        """
        Exception customizations should not break rich exception group traceback in python 3.10
        """
        import traceback

        sub_exc1 = RuntimeError("first sub exception")
        sub_exc2 = ZeroDivisionError("second sub exception")
        sub_group = self._make_one(excs=[sub_exc2])
        exc_group = self._make_one(excs=[sub_exc1, sub_group])
        found_message = str(exc_group).splitlines()[0]
        found_sub_message = str(sub_group).splitlines()[0]

        expected_traceback = (
            f"google.cloud.bigtable.data.exceptions.{type(exc_group).__name__}: {found_message}",
            "--+----------------  1 ----------------",
            "  | RuntimeError: first sub exception",
            "  +----------------  2 ----------------",
            f"  | {type(sub_group).__name__}: {found_sub_message}",
            "  --+----------------  1 ----------------",
            "    | ZeroDivisionError: second sub exception",
            "    +------------------------------------",
        )
        exception_caught = False
        try:
            raise exc_group
        except self._get_class():
            exception_caught = True
            tb = traceback.format_exc()
            tb_relevant_lines = tuple(tb.splitlines()[3:])
            assert expected_traceback == tb_relevant_lines
        assert exception_caught

    @pytest.mark.skipif(
        sys.version_info >= (3, 11), reason="requires python3.10 or lower"
    )
    def test_310_traceback_with_cause(self):
        """
        traceback should display nicely with sub-exceptions with __cause__ set
        """
        import traceback

        sub_exc1 = RuntimeError("first sub exception")
        cause_exc = ImportError("cause exception")
        sub_exc1.__cause__ = cause_exc
        sub_exc2 = ZeroDivisionError("second sub exception")
        exc_group = self._make_one(excs=[sub_exc1, sub_exc2])
        found_message = str(exc_group).splitlines()[0]

        expected_traceback = (
            f"google.cloud.bigtable.data.exceptions.{type(exc_group).__name__}: {found_message}",
            "--+----------------  1 ----------------",
            "  | ImportError: cause exception",
            "  | ",
            "  | The above exception was the direct cause of the following exception:",
            "  | ",
            "  | RuntimeError: first sub exception",
            "  +----------------  2 ----------------",
            "  | ZeroDivisionError: second sub exception",
            "  +------------------------------------",
        )
        exception_caught = False
        try:
            raise exc_group
        except self._get_class():
            exception_caught = True
            tb = traceback.format_exc()
            tb_relevant_lines = tuple(tb.splitlines()[3:])
            assert expected_traceback == tb_relevant_lines
        assert exception_caught


class TestBigtableExceptionGroup(TracebackTests311, TracebackTests310):
    """
    Subclass for MutationsExceptionGroup, RetryExceptionGroup, and ShardedReadRowsExceptionGroup
    """

    def _get_class(self):
        from google.cloud.bigtable.data.exceptions import _BigtableExceptionGroup

        return _BigtableExceptionGroup

    def _make_one(self, message="test_message", excs=None):
        if excs is None:
            excs = [RuntimeError("mock")]

        return self._get_class()(message, excs=excs)

    def test_raise(self):
        """
        Create exception in raise statement, which calls __new__ and __init__
        """
        test_msg = "test message"
        test_excs = [Exception(test_msg)]
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(test_msg, test_excs)
        found_message = str(e.value).splitlines()[
            0
        ]  # added to prase out subexceptions in <3.11
        assert found_message == test_msg
        assert list(e.value.exceptions) == test_excs

    def test_raise_empty_list(self):
        """
        Empty exception lists are not supported
        """
        with pytest.raises(ValueError) as e:
            raise self._make_one(excs=[])
        assert "non-empty sequence" in str(e.value)

    def test_exception_handling(self):
        """
        All versions should inherit from exception
        and support tranditional exception handling
        """
        instance = self._make_one()
        assert isinstance(instance, Exception)
        try:
            raise instance
        except Exception as e:
            assert isinstance(e, Exception)
            assert e == instance
            was_raised = True
        assert was_raised


class TestMutationsExceptionGroup(TestBigtableExceptionGroup):
    def _get_class(self):
        from google.cloud.bigtable.data.exceptions import MutationsExceptionGroup

        return MutationsExceptionGroup

    def _make_one(self, excs=None, num_entries=3):
        if excs is None:
            excs = [RuntimeError("mock")]

        return self._get_class()(excs, num_entries)

    @pytest.mark.parametrize(
        "exception_list,total_entries,expected_message",
        [
            ([Exception()], 1, "1 failed entry from 1 attempted."),
            ([Exception()], 2, "1 failed entry from 2 attempted."),
            (
                [Exception(), RuntimeError()],
                2,
                "2 failed entries from 2 attempted.",
            ),
        ],
    )
    def test_raise(self, exception_list, total_entries, expected_message):
        """
        Create exception in raise statement, which calls __new__ and __init__
        """
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(exception_list, total_entries)
        found_message = str(e.value).splitlines()[
            0
        ]  # added to prase out subexceptions in <3.11
        assert found_message == expected_message
        assert list(e.value.exceptions) == exception_list

    def test_raise_custom_message(self):
        """
        should be able to set a custom error message
        """
        custom_message = "custom message"
        exception_list = [Exception()]
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(exception_list, 5, message=custom_message)
        found_message = str(e.value).splitlines()[
            0
        ]  # added to prase out subexceptions in <3.11
        assert found_message == custom_message
        assert list(e.value.exceptions) == exception_list

    @pytest.mark.parametrize(
        "first_list_len,second_list_len,total_excs,entry_count,expected_message",
        [
            (3, 0, 3, 4, "3 failed entries from 4 attempted."),
            (1, 0, 1, 2, "1 failed entry from 2 attempted."),
            (0, 1, 1, 2, "1 failed entry from 2 attempted."),
            (2, 2, 4, 4, "4 failed entries from 4 attempted."),
            (
                1,
                1,
                3,
                2,
                "3 failed entries from 2 attempted. (first 1 and last 1 attached as sub-exceptions; 1 truncated)",
            ),
            (
                1,
                2,
                100,
                2,
                "100 failed entries from 2 attempted. (first 1 and last 2 attached as sub-exceptions; 97 truncated)",
            ),
            (
                2,
                1,
                4,
                9,
                "4 failed entries from 9 attempted. (first 2 and last 1 attached as sub-exceptions; 1 truncated)",
            ),
            (
                3,
                0,
                10,
                10,
                "10 failed entries from 10 attempted. (first 3 attached as sub-exceptions; 7 truncated)",
            ),
            (
                0,
                3,
                10,
                10,
                "10 failed entries from 10 attempted. (last 3 attached as sub-exceptions; 7 truncated)",
            ),
        ],
    )
    def test_from_truncated_lists(
        self, first_list_len, second_list_len, total_excs, entry_count, expected_message
    ):
        """
        Should be able to make MutationsExceptionGroup using a pair of
        lists representing a larger truncated list of exceptions
        """
        first_list = [Exception()] * first_list_len
        second_list = [Exception()] * second_list_len
        with pytest.raises(self._get_class()) as e:
            raise self._get_class().from_truncated_lists(
                first_list, second_list, total_excs, entry_count
            )
        found_message = str(e.value).splitlines()[
            0
        ]  # added to prase out subexceptions in <3.11
        assert found_message == expected_message
        assert list(e.value.exceptions) == first_list + second_list


class TestRetryExceptionGroup(TestBigtableExceptionGroup):
    def _get_class(self):
        from google.cloud.bigtable.data.exceptions import RetryExceptionGroup

        return RetryExceptionGroup

    def _make_one(self, excs=None):
        if excs is None:
            excs = [RuntimeError("mock")]

        return self._get_class()(excs=excs)

    @pytest.mark.parametrize(
        "exception_list,expected_message",
        [
            ([Exception()], "1 failed attempt"),
            ([Exception(), RuntimeError()], "2 failed attempts"),
            (
                [Exception(), ValueError("test")],
                "2 failed attempts",
            ),
            (
                [
                    bigtable_exceptions.RetryExceptionGroup(
                        [Exception(), ValueError("test")]
                    )
                ],
                "1 failed attempt",
            ),
        ],
    )
    def test_raise(self, exception_list, expected_message):
        """
        Create exception in raise statement, which calls __new__ and __init__
        """
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(exception_list)
        found_message = str(e.value).splitlines()[
            0
        ]  # added to prase out subexceptions in <3.11
        assert found_message == expected_message
        assert list(e.value.exceptions) == exception_list


class TestShardedReadRowsExceptionGroup(TestBigtableExceptionGroup):
    def _get_class(self):
        from google.cloud.bigtable.data.exceptions import ShardedReadRowsExceptionGroup

        return ShardedReadRowsExceptionGroup

    def _make_one(self, excs=None, succeeded=None, num_entries=3):
        if excs is None:
            excs = [RuntimeError("mock")]
        succeeded = succeeded or []

        return self._get_class()(excs, succeeded, num_entries)

    @pytest.mark.parametrize(
        "exception_list,succeeded,total_entries,expected_message",
        [
            ([Exception()], [], 1, "1 sub-exception (from 1 query attempted)"),
            ([Exception()], [1], 2, "1 sub-exception (from 2 queries attempted)"),
            (
                [Exception(), RuntimeError()],
                [0, 1],
                2,
                "2 sub-exceptions (from 2 queries attempted)",
            ),
        ],
    )
    def test_raise(self, exception_list, succeeded, total_entries, expected_message):
        """
        Create exception in raise statement, which calls __new__ and __init__
        """
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(exception_list, succeeded, total_entries)
        found_message = str(e.value).splitlines()[
            0
        ]  # added to prase out subexceptions in <3.11
        assert found_message == expected_message
        assert list(e.value.exceptions) == exception_list
        assert e.value.successful_rows == succeeded


class TestFailedMutationEntryError:
    def _get_class(self):
        from google.cloud.bigtable.data.exceptions import FailedMutationEntryError

        return FailedMutationEntryError

    def _make_one(self, idx=9, entry=mock.Mock(), cause=RuntimeError("mock")):
        return self._get_class()(idx, entry, cause)

    def test_raise(self):
        """
        Create exception in raise statement, which calls __new__ and __init__
        """
        test_idx = 2
        test_entry = mock.Mock()
        test_exc = ValueError("test")
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(test_idx, test_entry, test_exc)
        assert str(e.value) == "Failed idempotent mutation entry at index 2"
        assert e.value.index == test_idx
        assert e.value.entry == test_entry
        assert e.value.__cause__ == test_exc
        assert isinstance(e.value, Exception)
        assert test_entry.is_idempotent.call_count == 1

    def test_raise_idempotent(self):
        """
        Test raise with non idempotent entry
        """
        test_idx = 2
        test_entry = unittest.mock.Mock()
        test_entry.is_idempotent.return_value = False
        test_exc = ValueError("test")
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(test_idx, test_entry, test_exc)
        assert str(e.value) == "Failed non-idempotent mutation entry at index 2"
        assert e.value.index == test_idx
        assert e.value.entry == test_entry
        assert e.value.__cause__ == test_exc
        assert test_entry.is_idempotent.call_count == 1

    def test_no_index(self):
        """
        Instances without an index should display different error string
        """
        test_idx = None
        test_entry = unittest.mock.Mock()
        test_exc = ValueError("test")
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(test_idx, test_entry, test_exc)
        assert str(e.value) == "Failed idempotent mutation entry"
        assert e.value.index == test_idx
        assert e.value.entry == test_entry
        assert e.value.__cause__ == test_exc
        assert isinstance(e.value, Exception)
        assert test_entry.is_idempotent.call_count == 1


class TestFailedQueryShardError:
    def _get_class(self):
        from google.cloud.bigtable.data.exceptions import FailedQueryShardError

        return FailedQueryShardError

    def _make_one(self, idx=9, query=mock.Mock(), cause=RuntimeError("mock")):
        return self._get_class()(idx, query, cause)

    def test_raise(self):
        """
        Create exception in raise statement, which calls __new__ and __init__
        """
        test_idx = 2
        test_query = mock.Mock()
        test_exc = ValueError("test")
        with pytest.raises(self._get_class()) as e:
            raise self._get_class()(test_idx, test_query, test_exc)
        assert str(e.value) == "Failed query at index 2"
        assert e.value.index == test_idx
        assert e.value.query == test_query
        assert e.value.__cause__ == test_exc
        assert isinstance(e.value, Exception)
