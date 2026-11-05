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
#

import grpc
import mock
import pytest
from google.api_core import exceptions as core_exceptions
from google.protobuf import any_pb2
from google.rpc import code_pb2, error_details_pb2, status_pb2

import google.cloud.bigtable.data._helpers as _helpers
import google.cloud.bigtable.data.exceptions as bt_exceptions
from google.cloud.bigtable.data._helpers import TABLE_DEFAULT


class TestAttemptTimeoutGenerator:
    @pytest.mark.parametrize(
        "request_t,operation_t,expected_list",
        [
            (1, 3.5, [1, 1, 1, 0.5, 0, 0]),
            (None, 3.5, [3.5, 2.5, 1.5, 0.5, 0, 0]),
            (10, 5, [5, 4, 3, 2, 1, 0, 0]),
            (3, 3, [3, 2, 1, 0, 0, 0, 0]),
            (0, 3, [0, 0, 0]),
            (3, 0, [0, 0, 0]),
            (-1, 3, [0, 0, 0]),
            (3, -1, [0, 0, 0]),
        ],
    )
    def test_attempt_timeout_generator(self, request_t, operation_t, expected_list):
        """
        test different values for timeouts. Clock is incremented by 1 second for each item in expected_list
        """
        timestamp_start = 123
        with mock.patch("time.monotonic") as mock_monotonic:
            mock_monotonic.return_value = timestamp_start
            generator = _helpers._attempt_timeout_generator(request_t, operation_t)
            for val in expected_list:
                mock_monotonic.return_value += 1
                assert next(generator) == val

    @pytest.mark.parametrize(
        "request_t,operation_t,expected",
        [
            (1, 3.5, 1),
            (None, 3.5, 3.5),
            (10, 5, 5),
            (5, 10, 5),
            (3, 3, 3),
            (0, 3, 0),
            (3, 0, 0),
            (-1, 3, 0),
            (3, -1, 0),
        ],
    )
    def test_attempt_timeout_frozen_time(self, request_t, operation_t, expected):
        """test with time.monotonic frozen"""
        timestamp_start = 123
        with mock.patch("time.monotonic") as mock_monotonic:
            mock_monotonic.return_value = timestamp_start
            generator = _helpers._attempt_timeout_generator(request_t, operation_t)
            assert next(generator) == expected
            # value should not change without time.monotonic changing
            assert next(generator) == expected

    def test_attempt_timeout_w_sleeps(self):
        """use real sleep values to make sure it matches expectations"""
        from time import sleep

        operation_timeout = 1
        generator = _helpers._attempt_timeout_generator(None, operation_timeout)
        expected_value = operation_timeout
        sleep_time = 0.1
        for i in range(3):
            found_value = next(generator)
            assert abs(found_value - expected_value) < 0.1
            sleep(sleep_time)
            expected_value -= sleep_time


class TestValidateTimeouts:
    def test_validate_timeouts_error_messages(self):
        with pytest.raises(ValueError) as e:
            _helpers._validate_timeouts(operation_timeout=1, attempt_timeout=-1)
        assert "attempt_timeout must be greater than 0" in str(e.value)
        with pytest.raises(ValueError) as e:
            _helpers._validate_timeouts(operation_timeout=-1, attempt_timeout=1)
        assert "operation_timeout must be greater than 0" in str(e.value)

    @pytest.mark.parametrize(
        "args,expected",
        [
            ([1, None, False], False),
            ([1, None, True], True),
            ([1, 1, False], True),
            ([1, 1, True], True),
            ([1, 1], True),
            ([1, None], False),
            ([2, 1], True),
            ([0, 1], False),
            ([1, 0], False),
            ([60, None], False),
            ([600, None], False),
            ([600, 600], True),
        ],
    )
    def test_validate_with_inputs(self, args, expected):
        """
        test whether an exception is thrown with different inputs
        """
        success = False
        try:
            _helpers._validate_timeouts(*args)
            success = True
        except ValueError:
            pass
        assert success == expected


class TestGetTimeouts:
    @pytest.mark.parametrize(
        "input_times,input_table,expected",
        [
            ((2, 1), {}, (2, 1)),
            ((2, 4), {}, (2, 2)),
            ((2, None), {}, (2, 2)),
            (
                (TABLE_DEFAULT.DEFAULT, TABLE_DEFAULT.DEFAULT),
                {"operation": 3, "attempt": 2},
                (3, 2),
            ),
            (
                (TABLE_DEFAULT.READ_ROWS, TABLE_DEFAULT.READ_ROWS),
                {"read_rows_operation": 3, "read_rows_attempt": 2},
                (3, 2),
            ),
            (
                (TABLE_DEFAULT.MUTATE_ROWS, TABLE_DEFAULT.MUTATE_ROWS),
                {"mutate_rows_operation": 3, "mutate_rows_attempt": 2},
                (3, 2),
            ),
            ((10, TABLE_DEFAULT.DEFAULT), {"attempt": None}, (10, 10)),
            ((10, TABLE_DEFAULT.DEFAULT), {"attempt": 5}, (10, 5)),
            ((10, TABLE_DEFAULT.DEFAULT), {"attempt": 100}, (10, 10)),
            ((TABLE_DEFAULT.DEFAULT, 10), {"operation": 12}, (12, 10)),
            ((TABLE_DEFAULT.DEFAULT, 10), {"operation": 3}, (3, 3)),
        ],
    )
    def test_get_timeouts(self, input_times, input_table, expected):
        """
        test input/output mappings for a variety of valid inputs
        """
        fake_table = mock.Mock()
        for key in input_table.keys():
            # set the default fields in our fake table mock
            setattr(fake_table, f"default_{key}_timeout", input_table[key])
        t1, t2 = _helpers._get_timeouts(input_times[0], input_times[1], fake_table)
        assert t1 == expected[0]
        assert t2 == expected[1]

    @pytest.mark.parametrize(
        "input_times,input_table",
        [
            ([0, 1], {}),
            ([1, 0], {}),
            ([None, 1], {}),
            ([TABLE_DEFAULT.DEFAULT, 1], {"operation": None}),
            ([TABLE_DEFAULT.DEFAULT, 1], {"operation": 0}),
            ([1, TABLE_DEFAULT.DEFAULT], {"attempt": 0}),
        ],
    )
    def test_get_timeouts_invalid(self, input_times, input_table):
        """
        test with inputs that should raise error during validation step
        """
        fake_table = mock.Mock()
        for key in input_table.keys():
            # set the default fields in our fake table mock
            setattr(fake_table, f"default_{key}_timeout", input_table[key])
        with pytest.raises(ValueError):
            _helpers._get_timeouts(input_times[0], input_times[1], fake_table)


class TestAlignTimeouts:
    @pytest.mark.parametrize(
        "input_times,expected",
        [
            ((2, 1), (2, 1)),
            ((2, 4), (2, 2)),
            ((2, None), (2, 2)),
        ],
    )
    def test_get_timeouts(self, input_times, expected):
        """
        test input/output mappings for a variety of valid inputs
        """
        t1, t2 = _helpers._align_timeouts(input_times[0], input_times[1])
        assert t1 == expected[0]
        assert t2 == expected[1]

    @pytest.mark.parametrize(
        "input_times",
        [
            ([0, 1]),
            ([1, 0]),
            ([None, 1]),
        ],
    )
    def test_get_timeouts_invalid(self, input_times):
        """
        test with inputs that should raise error during validation step
        """
        with pytest.raises(ValueError):
            _helpers._align_timeouts(input_times[0], input_times[1])


class TestRstStreamAwarePredicate:
    @pytest.mark.parametrize(
        "retryable_exceptions,exception,expected_is_retryable",
        [
            (
                [core_exceptions.Aborted, core_exceptions.InternalServerError],
                core_exceptions.InternalServerError("Sorry"),
                True,
            ),
            (
                [core_exceptions.Aborted, core_exceptions.InternalServerError],
                core_exceptions.DataLoss("Sorry"),
                False,
            ),
            (
                [core_exceptions.ServiceUnavailable, core_exceptions.Aborted],
                core_exceptions.InternalServerError("Sorry"),
                False,
            ),
            (
                [core_exceptions.ServiceUnavailable, core_exceptions.Aborted],
                core_exceptions.InternalServerError(
                    _helpers._RETRYABLE_INTERNAL_ERROR_MESSAGES[0]
                ),
                True,
            ),
            (
                [core_exceptions.InternalServerError, core_exceptions.Aborted],
                core_exceptions.InternalServerError(
                    _helpers._RETRYABLE_INTERNAL_ERROR_MESSAGES[0]
                ),
                True,
            ),
        ],
    )
    def test_rst_stream_aware_predicate(
        self, retryable_exceptions, exception, expected_is_retryable
    ):
        predicate = _helpers._rst_stream_aware_predicate(*retryable_exceptions)
        assert predicate(exception) is expected_is_retryable


class TestGetStatusesFromMutationsExceptionGroup:
    @pytest.mark.parametrize(
        "failed_idx,cause_exc,expected_status",
        [
            (
                0,
                core_exceptions.DeadlineExceeded(
                    "Operation timed out after 40 seconds"
                ),
                status_pb2.Status(
                    code=code_pb2.DEADLINE_EXCEEDED,
                    message="Operation timed out after 40 seconds",
                ),
            ),
            (
                0,
                RuntimeError("Something happened"),
                status_pb2.Status(code=code_pb2.UNKNOWN, message="Something happened"),
            ),
            (
                0,
                bt_exceptions.RetryExceptionGroup(
                    excs=[
                        core_exceptions.ServiceUnavailable("Service Unavailable"),
                        core_exceptions.ServiceUnavailable("Service Unavailable"),
                        core_exceptions.DeadlineExceeded(
                            "Operation timed out after 40 seconds"
                        ),
                    ]
                ),
                status_pb2.Status(
                    code=code_pb2.DEADLINE_EXCEEDED,
                    message="Operation timed out after 40 seconds",
                ),
            ),
            (
                0,
                bt_exceptions.RetryExceptionGroup(
                    excs=[
                        core_exceptions.ServiceUnavailable("Service Unavailable"),
                        core_exceptions.ServiceUnavailable("Service Unavailable"),
                        RuntimeError("Something happened"),
                    ]
                ),
                status_pb2.Status(code=code_pb2.UNKNOWN, message="Something happened"),
            ),
            (
                0,
                None,
                status_pb2.Status(
                    code=code_pb2.UNKNOWN, message="An unknown error has occurred"
                ),
            ),
            (
                100,
                RuntimeError("Something happened"),
                status_pb2.Status(code=code_pb2.OK),
            ),
            (
                None,
                RuntimeError("Something happened"),
                status_pb2.Status(code=code_pb2.OK),
            ),
        ],
    )
    def test_get_statuses_from_mutations_exception_group(
        self, failed_idx, cause_exc, expected_status
    ):
        mutation_exception_group = bt_exceptions.MutationsExceptionGroup(
            excs=[
                bt_exceptions.FailedMutationEntryError(
                    failed_idx=failed_idx,
                    failed_mutation_entry=mock.Mock(),
                    cause=cause_exc,
                )
            ],
            total_entries=1,
            message="Mutations failed.",
        )

        statuses = _helpers._get_statuses_from_mutations_exception_group(
            mutation_exception_group, 1
        )
        assert statuses[0] == expected_status

    def test_get_status_packs_unpacked_error_details(self):
        err_info = error_details_pb2.ErrorInfo(
            reason="IAM_PERMISSION_DENIED",
            domain="bigtable.googleapis.com",
            metadata={"resource": "projects/p/instances/i/tables/t"},
        )
        retry_info = error_details_pb2.RetryInfo()
        already_packed = any_pb2.Any()
        already_packed.Pack(retry_info)

        proto_plus_wrapper = mock.Mock()
        proto_plus_wrapper._pb = error_details_pb2.DebugInfo(detail="stack")

        exc = core_exceptions.PermissionDenied(
            "Permission denied",
            details=[err_info, already_packed, proto_plus_wrapper, "ignored"],
        )

        status = _helpers._get_status(exc)
        assert status.code == code_pb2.PERMISSION_DENIED
        assert status.message == "Permission denied"
        assert len(status.details) == 3

        unpacked_err_info = error_details_pb2.ErrorInfo()
        assert status.details[0].Unpack(unpacked_err_info)
        assert unpacked_err_info == err_info

        assert status.details[1] == already_packed

        unpacked_debug_info = error_details_pb2.DebugInfo()
        assert status.details[2].Unpack(unpacked_debug_info)
        assert unpacked_debug_info == proto_plus_wrapper._pb

    def test_get_status_handles_malformed_details_and_exceptions(self):
        err_info = error_details_pb2.ErrorInfo(
            reason="IAM_PERMISSION_DENIED",
            domain="bigtable.googleapis.com",
        )

        class BrokenWrapper:
            @property
            def _pb(self):
                raise RuntimeError("broken _pb property")

        exc = core_exceptions.PermissionDenied(
            None,
            details=[BrokenWrapper(), err_info],
        )
        status = _helpers._get_status(exc)
        assert status.code == code_pb2.PERMISSION_DENIED
        assert status.message == ""
        assert len(status.details) == 1

        unpacked_err_info = error_details_pb2.ErrorInfo()
        assert status.details[0].Unpack(unpacked_err_info)
        assert unpacked_err_info == err_info

        # Non-iterable details falls back to UNKNOWN without raising
        malformed_exc = core_exceptions.PermissionDenied(
            "Permission denied",
            details=123,  # type: ignore[arg-type]
        )
        fallback_status = _helpers._get_status(malformed_exc)
        assert fallback_status.code == code_pb2.UNKNOWN
        assert "Permission denied" in fallback_status.message


class TestGetRetryableErrors:
    @pytest.mark.parametrize(
        "input_codes,input_table,expected",
        [
            ((), {}, []),
            ((Exception,), {}, [Exception]),
            (TABLE_DEFAULT.DEFAULT, {"default": [Exception]}, [Exception]),
            (
                TABLE_DEFAULT.READ_ROWS,
                {"default_read_rows": (RuntimeError, ValueError)},
                [RuntimeError, ValueError],
            ),
            (
                TABLE_DEFAULT.MUTATE_ROWS,
                {"default_mutate_rows": (ValueError,)},
                [ValueError],
            ),
            ((4,), {}, [core_exceptions.DeadlineExceeded]),
            (
                [grpc.StatusCode.DEADLINE_EXCEEDED],
                {},
                [core_exceptions.DeadlineExceeded],
            ),
            (
                (14, grpc.StatusCode.ABORTED, RuntimeError),
                {},
                [
                    core_exceptions.ServiceUnavailable,
                    core_exceptions.Aborted,
                    RuntimeError,
                ],
            ),
        ],
    )
    def test_get_retryable_errors(self, input_codes, input_table, expected):
        """
        test input/output mappings for a variety of valid inputs
        """
        fake_table = mock.Mock()
        for key in input_table.keys():
            # set the default fields in our fake table mock
            setattr(fake_table, f"{key}_retryable_errors", input_table[key])
        result = _helpers._get_retryable_errors(input_codes, fake_table)
        assert result == expected

    @pytest.mark.parametrize(
        "invalid_code",
        [
            0,
            grpc.StatusCode.OK,
            -1,
            999,
            True,
            False,
            "INVALID",
        ],
    )
    def test_get_error_type_invalid_status_code(self, invalid_code):
        with pytest.raises(ValueError, match="Invalid gRPC error status code"):
            _helpers._get_error_type(invalid_code)
        with pytest.raises(ValueError, match="Invalid gRPC error status code"):
            _helpers._get_retryable_errors([invalid_code], mock.Mock())


class TestTrackedBackoffGenerator:
    def test_tracked_backoff_generator_history(self):
        """
        Should be able to retrieve historical results from backoff generator
        """
        generator = _helpers.TrackedBackoffGenerator(
            initial=0, multiplier=2, maximum=10
        )
        got_list = [next(generator) for _ in range(20)]

        # check all values are correct
        for i in range(19, 0, -1):
            assert generator.get_attempt_backoff(i) == got_list[i]
        # check a random value out of order
        assert generator.get_attempt_backoff(5) == got_list[5]

    @mock.patch("random.uniform", side_effect=lambda a, b: b)
    def test_tracked_backoff_generator_defaults(self, mock_uniform):
        """
        Should generate values with default parameters

        initial=0.01, multiplier=2, maximum=60
        """
        generator = _helpers.TrackedBackoffGenerator()
        expected_values = [0.01, 0.02, 0.04, 0.08, 0.16]
        for expected in expected_values:
            assert next(generator) == pytest.approx(expected)

    @mock.patch("random.uniform", side_effect=lambda a, b: b)
    def test_tracked_backoff_generator_with_maximum(self, mock_uniform):
        """
        Should cap the backoff at the maximum value
        """
        generator = _helpers.TrackedBackoffGenerator(initial=1, multiplier=2, maximum=5)
        expected_values = [1, 2, 4, 5, 5, 5]
        for expected in expected_values:
            assert next(generator) == expected

    def test_get_attempt_backoff_out_of_bounds(self):
        """
        get_attempt_backoff should raise IndexError for out of bounds index
        """
        generator = _helpers.TrackedBackoffGenerator()
        next(generator)
        next(generator)
        with pytest.raises(IndexError):
            generator.get_attempt_backoff(2)
        with pytest.raises(IndexError):
            generator.get_attempt_backoff(-3)

    def test_set_next_full_set(self):
        """
        try always using set_next to populate generator
        """
        generator = _helpers.TrackedBackoffGenerator()
        for idx, val in enumerate(range(100, 0, -1)):
            generator.set_next(val)
            got = next(generator)
            assert got == val
            assert generator.get_attempt_backoff(idx) == val

    def test_set_next_negative_value(self):
        generator = _helpers.TrackedBackoffGenerator()
        with pytest.raises(ValueError):
            generator.set_next(-1)

    @mock.patch("random.uniform", side_effect=lambda a, b: b)
    def test_interleaved_set_next(self, mock_uniform):
        import itertools

        generator = _helpers.TrackedBackoffGenerator(
            initial=1, multiplier=2, maximum=128
        )
        # values we expect generator to create
        expected_values = [2**i for i in range(8)]
        # values we will insert
        inserted_values = [9, 61, 0, 4, 33, 12, 18, 2]
        for idx in range(8):
            assert next(generator) == expected_values[idx]
            generator.set_next(inserted_values[idx])
            assert next(generator) == inserted_values[idx]
        # check to make sure history is as we expect
        generator.history = itertools.chain.from_iterable(
            zip(expected_values, inserted_values)
        )

    @mock.patch("random.uniform", side_effect=lambda a, b: b)
    def test_set_next_replacement(self, mock_uniform):
        generator = _helpers.TrackedBackoffGenerator(initial=1)
        generator.set_next(99)
        generator.set_next(88)
        assert next(generator) == 88
        assert next(generator) == 1
