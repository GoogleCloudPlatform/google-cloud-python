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

import datetime
import os
import uuid

import pytest
from google.api_core import retry
from google.api_core.exceptions import ClientError, PermissionDenied, ServerError
from google.cloud.environment_vars import BIGTABLE_EMULATOR
from google.type import date_pb2

from google.cloud.bigtable.data._cross_sync import CrossSync
from google.cloud.bigtable.data._metrics import OperationType
from google.cloud.bigtable.data.execute_query.metadata import SqlType
from google.cloud.bigtable.data.read_modify_write_rules import _MAX_INCREMENT_VALUE

from . import TEST_AGGREGATE_FAMILY, TEST_FAMILY, TEST_FAMILY_2, SystemTestRunner

if CrossSync.is_async:
    from google.cloud.bigtable_v2.services.bigtable.transports.grpc_asyncio import (
        _LoggingClientAIOInterceptor as GapicInterceptor,
    )
else:
    from google.cloud.bigtable_v2.services.bigtable.transports.grpc import (
        _LoggingClientInterceptor as GapicInterceptor,
    )

__CROSS_SYNC_OUTPUT__ = "tests.system.data.test_system_autogen"


TARGETS = ["table"]
if not os.environ.get(BIGTABLE_EMULATOR):
    # emulator doesn't support authorized views
    TARGETS.append("authorized_view")


@CrossSync.convert_class(
    sync_name="TempRowBuilder",
    add_mapping_for_name="TempRowBuilder",
)
class TempRowBuilderAsync:
    """
    Used to add rows to a table for testing purposes.
    """

    def __init__(self, target):
        self.rows = []
        self.target = target

    @CrossSync.convert
    async def add_row(
        self, row_key, *, family=TEST_FAMILY, qualifier=b"q", value=b"test-value"
    ):
        if isinstance(value, str):
            value = value.encode("utf-8")
        elif isinstance(value, int):
            value = value.to_bytes(8, byteorder="big", signed=True)
        request = {
            **self.target._request_path,
            "row_key": row_key,
            "mutations": [
                {
                    "set_cell": {
                        "family_name": family,
                        "column_qualifier": qualifier,
                        "value": value,
                    }
                }
            ],
        }
        await self.target.client._gapic_client.mutate_row(request)
        self.rows.append(row_key)

    @CrossSync.convert
    async def add_aggregate_row(
        self, row_key, *, family=TEST_AGGREGATE_FAMILY, qualifier=b"q", input=0
    ):
        request = {
            **self.target._request_path,
            "row_key": row_key,
            "mutations": [
                {
                    "add_to_cell": {
                        "family_name": family,
                        "column_qualifier": {"raw_value": qualifier},
                        "timestamp": {"raw_timestamp_micros": 0},
                        "input": {"int_value": input},
                    }
                }
            ],
        }
        await self.target.client._gapic_client.mutate_row(request)
        self.rows.append(row_key)

    @CrossSync.convert
    async def delete_rows(self):
        if self.rows:
            # Chunk deletions to 5,000 rows. While Bigtable officially supports up to
            # 100,000 mutations per MutateRows RPC, sending massive batches may hit
            # the default gRPC 4MB client payload size limit due to metadata
            # serialization overhead. Keeping chunks at 5,000 ensures we stay safely
            # under 4MB and minimizes transient network timeouts on live connections.
            chunk_size = 5000
            rows_list = list(self.rows)

            # Check if the test target is an Authorized View
            is_authorized_view = "authorized_view_name" in self.target._request_path

            if is_authorized_view:
                # For Authorized Views, we cannot use delete_from_row because it attempts
                # to delete families outside the view's scope. We must delete explicitly
                # from the allowed families we wrote to.
                mutations = [
                    {"delete_from_family": {"family_name": TEST_FAMILY}},
                    {"delete_from_family": {"family_name": TEST_AGGREGATE_FAMILY}},
                ]
            else:
                mutations = [{"delete_from_row": {}}]

            for i in range(0, len(rows_list), chunk_size):
                chunk = rows_list[i : i + chunk_size]
                request = {
                    **self.target._request_path,
                    "entries": [
                        {"row_key": row, "mutations": mutations} for row in chunk
                    ],
                }
                # Await and consume the gRPC stream to guarantee execution
                stream = await self.target.client._gapic_client.mutate_rows(request)
                async for response in stream:
                    for entry in response.entries:
                        if entry.status.code != 0:
                            raise RuntimeError(
                                f"Failed to delete row: {entry.status.message}"
                            )

    @CrossSync.convert
    async def retrieve_cell_value(self, target, row_key):
        """
        Helper to read an individual row
        """
        from google.cloud.bigtable.data import ReadRowsQuery

        row_list = await target.read_rows(ReadRowsQuery(row_keys=row_key))
        assert len(row_list) == 1
        row = row_list[0]
        cell = row.cells[0]
        return cell.value

    @CrossSync.convert
    async def create_row_and_mutation(
        self, table, *, start_value=b"start", new_value=b"new_value"
    ):
        """
        Helper to create a new row, and a sample set_cell mutation to change its value
        """
        from google.cloud.bigtable.data.mutations import SetCell

        row_key = uuid.uuid4().hex.encode()
        family = TEST_FAMILY
        qualifier = b"test-qualifier"
        await self.add_row(
            row_key, family=family, qualifier=qualifier, value=start_value
        )
        # ensure cell is initialized
        assert await self.retrieve_cell_value(table, row_key) == start_value

        mutation = SetCell(family=TEST_FAMILY, qualifier=qualifier, new_value=new_value)
        return row_key, mutation


@CrossSync.convert_class(sync_name="TestSystem")
class TestSystemAsync(SystemTestRunner):
    def _make_client(self):
        project = os.getenv("GOOGLE_CLOUD_PROJECT") or None
        return CrossSync.DataClient(project=project)

    @CrossSync.convert
    @CrossSync.pytest_fixture(scope="session")
    async def client(self):
        async with self._make_client() as client:
            yield client

    @CrossSync.convert
    @CrossSync.pytest_fixture(scope="session", params=TARGETS)
    async def target(self, client, table_id, authorized_view_id, instance_id, request):
        """
        This fixture runs twice: once for a standard table, and once with an authorized view

        Note: emulator doesn't support authorized views. Only use target
        """
        if request.param == "table":
            async with client.get_table(instance_id, table_id) as table:
                yield table
        elif request.param == "authorized_view":
            async with client.get_authorized_view(
                instance_id, table_id, authorized_view_id
            ) as view:
                yield view
        else:
            raise ValueError(f"unknown target type: {request.param}")

    @CrossSync.convert
    @CrossSync.pytest_fixture(scope="function")
    async def temp_rows(self, target):
        builder = CrossSync.TempRowBuilder(target)
        yield builder
        await builder.delete_rows()

    @pytest.mark.usefixtures("target")
    @pytest.mark.usefixtures("client")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=10
    )
    @CrossSync.pytest
    async def test_ping_and_warm_gapic(self, client, target):
        """
        Simple ping rpc test
        This test ensures channels are able to authenticate with backend
        """
        request = {"name": target.instance_name}
        await client._gapic_client.ping_and_warm(request)

    @pytest.mark.usefixtures("target")
    @pytest.mark.usefixtures("client")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_ping_and_warm(self, client, target):
        """
        Test ping and warm from handwritten client
        """
        results = await client._ping_and_warm_instances()
        assert len(results) == 1
        assert results[0] is None

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator mode doesn't refresh channel",
    )
    @CrossSync.pytest
    async def test_channel_refresh(self, table_id, instance_id, temp_rows):
        """
        perform requests while swapping out the grpc channel. Requests should continue without error
        """
        import time

        await temp_rows.add_row(b"test_row")
        async with self._make_client() as client:
            client._channel_refresh_task.cancel()
            channel_wrapper = client.transport.grpc_channel
            first_channel = channel_wrapper._channel
            # swap channels frequently, with large grace windows
            client._channel_refresh_task = CrossSync.create_task(
                client._manage_channel,
                refresh_interval_min=0.1,
                refresh_interval_max=0.1,
                grace_period=1,
                sync_executor=client._executor,
            )

            # hit channels with frequent requests
            end_time = time.monotonic() + 3
            async with client.get_table(instance_id, table_id) as table:
                while time.monotonic() < end_time:
                    # we expect a CancelledError if a channel is closed before completion
                    rows = await table.read_rows({})
                    assert len(rows) == 1
                    await CrossSync.yield_to_event_loop()
            # ensure channel was updated
            updated_channel = channel_wrapper._channel
            assert updated_channel is not first_channel
            # ensure interceptors are kept (gapic's logging interceptor, and metric interceptor)
            if CrossSync.is_async:
                unary_interceptors = updated_channel._unary_unary_interceptors
                assert len(unary_interceptors) == 2
                assert GapicInterceptor in [type(i) for i in unary_interceptors]
                assert client._metrics_interceptor in unary_interceptors
                stream_interceptors = updated_channel._unary_stream_interceptors
                assert len(stream_interceptors) == 1
                assert client._metrics_interceptor in stream_interceptors
            else:
                assert isinstance(
                    client.transport._logged_channel._interceptor, GapicInterceptor
                )
                assert updated_channel._interceptor == client._metrics_interceptor

    @CrossSync.pytest
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    async def test_mutation_set_cell(self, target, temp_rows):
        """
        Ensure cells can be set properly
        """
        row_key = b"bulk_mutate"
        new_value = uuid.uuid4().hex.encode()
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        await target.mutate_row(row_key, mutation)

        # ensure cell is updated
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value

    @CrossSync.pytest
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    async def test_mutation_add_to_cell(self, target, temp_rows):
        """
        Test add to cell mutation
        """
        from google.cloud.bigtable.data.mutations import AddToCell

        row_key = b"add_to_cell"
        family = TEST_AGGREGATE_FAMILY
        qualifier = b"test-qualifier"
        # add row to temp_rows, for future deletion
        await temp_rows.add_aggregate_row(row_key, family=family, qualifier=qualifier)
        # set and check cell value
        await target.mutate_row(
            row_key, AddToCell(family, qualifier, 1, timestamp_micros=0)
        )
        encoded_result = await temp_rows.retrieve_cell_value(target, row_key)
        int_result = int.from_bytes(encoded_result, byteorder="big")
        assert int_result == 1
        # update again
        await target.mutate_row(
            row_key, AddToCell(family, qualifier, 9, timestamp_micros=0)
        )
        encoded_result = await temp_rows.retrieve_cell_value(target, row_key)
        int_result = int.from_bytes(encoded_result, byteorder="big")
        assert int_result == 10

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)), reason="emulator doesn't use splits"
    )
    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_sample_row_keys(
        self, client, target, temp_rows, column_split_config
    ):
        """
        Sample keys should return a single sample in small test targets
        """
        await temp_rows.add_row(b"row_key_1")
        await temp_rows.add_row(b"row_key_2")

        results = await target.sample_row_keys()
        assert len(results) == len(column_split_config) + 1
        # first keys should match the split config
        for idx in range(len(column_split_config)):
            assert results[idx][0] == column_split_config[idx]
            assert isinstance(results[idx][1], int)
        # last sample should be empty key
        assert results[-1][0] == b""
        assert isinstance(results[-1][1], int)

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)), reason="emulator doesn't use splits"
    )
    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_sample_row_keys_w_row_range(
        self, client, target, column_split_config
    ):
        """
        Sample keys with row range should return samples within the range,
        with the last key matching the end of the range.
        """
        if len(column_split_config) < 4:
            pytest.skip("Not enough splits in column_split_config for this test")

        from google.cloud.bigtable.data import RowRange

        start_key = column_split_config[1]
        end_key = column_split_config[3]
        row_range = RowRange(start_key=start_key, end_key=end_key)

        results = await target.sample_row_keys(row_range=row_range)
        assert len(results) == 2

        assert results[0][0] == column_split_config[2]
        assert results[1][0] == column_split_config[3]

        for _, offset in results:
            assert isinstance(offset, int)

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_bulk_mutations_set_cell(self, client, target, temp_rows):
        """
        Ensure cells can be set properly
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        new_value = uuid.uuid4().hex.encode()
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])

        await target.bulk_mutate_rows([bulk_mutation])

        # ensure cell is updated
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value

    @CrossSync.pytest
    async def test_bulk_mutations_raise_exception(self, client, target):
        """
        If an invalid mutation is passed, an exception should be raised
        """
        from google.cloud.bigtable.data.exceptions import (
            FailedMutationEntryError,
            MutationsExceptionGroup,
        )
        from google.cloud.bigtable.data.mutations import RowMutationEntry, SetCell

        row_key = uuid.uuid4().hex.encode()
        mutation = SetCell(
            family="nonexistent", qualifier=b"test-qualifier", new_value=b""
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])

        with pytest.raises(MutationsExceptionGroup) as exc:
            await target.bulk_mutate_rows([bulk_mutation])
        assert len(exc.value.exceptions) == 1
        entry_error = exc.value.exceptions[0]
        assert isinstance(entry_error, FailedMutationEntryError)
        assert entry_error.index == 0
        assert entry_error.entry == bulk_mutation

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_mutations_batcher_context_manager(self, client, target, temp_rows):
        """
        test batcher with context manager. Should flush on exit
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        new_value, new_value2 = [uuid.uuid4().hex.encode() for _ in range(2)]
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        row_key2, mutation2 = await temp_rows.create_row_and_mutation(
            target, new_value=new_value2
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])
        bulk_mutation2 = RowMutationEntry(row_key2, [mutation2])

        async with target.mutations_batcher() as batcher:
            await batcher.append(bulk_mutation)
            await batcher.append(bulk_mutation2)
        # ensure cell is updated
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value
        assert len(batcher._staged_entries) == 0

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_mutations_batcher_timer_flush(self, client, target, temp_rows):
        """
        batch should occur after flush_interval seconds
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        new_value = uuid.uuid4().hex.encode()
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])
        flush_interval = 0.1
        async with target.mutations_batcher(flush_interval=flush_interval) as batcher:
            await batcher.append(bulk_mutation)
            await CrossSync.yield_to_event_loop()
            assert len(batcher._staged_entries) == 1
            await CrossSync.sleep(flush_interval + 0.1)
            assert len(batcher._staged_entries) == 0
            # ensure cell is updated
            assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_mutations_batcher_completed_callback(
        self, client, target, temp_rows
    ):
        """
        test batcher with batch completed callback. It should be called when the batcher flushes.
        """
        import mock
        from google.rpc import code_pb2, status_pb2

        from google.cloud.bigtable.data.mutations import RowMutationEntry

        callback = mock.Mock()

        new_value = uuid.uuid4().hex.encode()
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])
        flush_interval = 0.1
        async with target.mutations_batcher(flush_interval=flush_interval) as batcher:
            batcher._user_batch_completed_callback = callback
            await batcher.append(bulk_mutation)
            await CrossSync.yield_to_event_loop()
            assert len(batcher._staged_entries) == 1
            await CrossSync.sleep(flush_interval + 0.1)
            assert len(batcher._staged_entries) == 0
            callback.assert_called_once_with([status_pb2.Status(code=code_pb2.OK)])
            # ensure cell is updated
            assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_mutations_batcher_count_flush(self, client, target, temp_rows):
        """
        batch should flush after flush_limit_mutation_count mutations
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        new_value, new_value2 = [uuid.uuid4().hex.encode() for _ in range(2)]
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])
        row_key2, mutation2 = await temp_rows.create_row_and_mutation(
            target, new_value=new_value2
        )
        bulk_mutation2 = RowMutationEntry(row_key2, [mutation2])

        async with target.mutations_batcher(flush_limit_mutation_count=2) as batcher:
            await batcher.append(bulk_mutation)
            assert len(batcher._flush_jobs) == 0
            # should be noop; flush not scheduled
            assert len(batcher._staged_entries) == 1
            await batcher.append(bulk_mutation2)
            # task should now be scheduled
            assert len(batcher._flush_jobs) == 1
            # let flush complete
            for future in list(batcher._flush_jobs):
                await future
                # for sync version: grab result
                future.result()
            assert len(batcher._staged_entries) == 0
            assert len(batcher._flush_jobs) == 0
            # ensure cells were updated
            assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value
            assert (await temp_rows.retrieve_cell_value(target, row_key2)) == new_value2

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_mutations_batcher_bytes_flush(self, client, target, temp_rows):
        """
        batch should flush after flush_limit_bytes bytes
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        new_value, new_value2 = [uuid.uuid4().hex.encode() for _ in range(2)]
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, new_value=new_value
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])
        row_key2, mutation2 = await temp_rows.create_row_and_mutation(
            target, new_value=new_value2
        )
        bulk_mutation2 = RowMutationEntry(row_key2, [mutation2])

        flush_limit = bulk_mutation.size() + bulk_mutation2.size() - 1

        async with target.mutations_batcher(flush_limit_bytes=flush_limit) as batcher:
            await batcher.append(bulk_mutation)
            assert len(batcher._flush_jobs) == 0
            assert len(batcher._staged_entries) == 1
            await batcher.append(bulk_mutation2)
            # task should now be scheduled
            assert len(batcher._flush_jobs) == 1
            assert len(batcher._staged_entries) == 0
            # let flush complete
            for future in list(batcher._flush_jobs):
                await future
                # for sync version: grab result
                future.result()
            # ensure cells were updated
            assert (await temp_rows.retrieve_cell_value(target, row_key)) == new_value
            assert (await temp_rows.retrieve_cell_value(target, row_key2)) == new_value2

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_mutations_batcher_no_flush(self, client, target, temp_rows):
        """
        test with no flush requirements met
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry

        new_value = uuid.uuid4().hex.encode()
        start_value = b"unchanged"
        row_key, mutation = await temp_rows.create_row_and_mutation(
            target, start_value=start_value, new_value=new_value
        )
        bulk_mutation = RowMutationEntry(row_key, [mutation])
        row_key2, mutation2 = await temp_rows.create_row_and_mutation(
            target, start_value=start_value, new_value=new_value
        )
        bulk_mutation2 = RowMutationEntry(row_key2, [mutation2])

        size_limit = bulk_mutation.size() + bulk_mutation2.size() + 1
        async with target.mutations_batcher(
            flush_limit_bytes=size_limit, flush_limit_mutation_count=3, flush_interval=1
        ) as batcher:
            await batcher.append(bulk_mutation)
            assert len(batcher._staged_entries) == 1
            await batcher.append(bulk_mutation2)
            # flush not scheduled
            assert len(batcher._flush_jobs) == 0
            await CrossSync.yield_to_event_loop()
            assert len(batcher._staged_entries) == 2
            assert len(batcher._flush_jobs) == 0
            # ensure cells were not updated
            assert (await temp_rows.retrieve_cell_value(target, row_key)) == start_value
            assert (
                await temp_rows.retrieve_cell_value(target, row_key2)
            ) == start_value

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_mutations_batcher_large_batch(self, client, target, temp_rows):
        """
        test batcher with large batch of mutations
        """
        from google.cloud.bigtable.data.mutations import RowMutationEntry, SetCell

        add_mutation = SetCell(
            family=TEST_FAMILY, qualifier=b"test-qualifier", new_value=b"a"
        )
        row_mutations = []
        for i in range(50_000):
            row_key = uuid.uuid4().hex.encode()
            row_mutations.append(RowMutationEntry(row_key, [add_mutation]))
            # append row key for eventual deletion
            temp_rows.rows.append(row_key)

        async with target.mutations_batcher() as batcher:
            for mutation in row_mutations:
                await batcher.append(mutation)
        # ensure cell is updated
        assert len(batcher._staged_entries) == 0

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @pytest.mark.parametrize(
        "start,increment,expected",
        [
            (0, 0, 0),
            (0, 1, 1),
            (0, -1, -1),
            (1, 0, 1),
            (0, -100, -100),
            (0, 3000, 3000),
            (10, 4, 14),
            (_MAX_INCREMENT_VALUE, -_MAX_INCREMENT_VALUE, 0),
            (_MAX_INCREMENT_VALUE, 2, -_MAX_INCREMENT_VALUE),
            (-_MAX_INCREMENT_VALUE, -2, _MAX_INCREMENT_VALUE),
        ],
    )
    @CrossSync.pytest
    async def test_read_modify_write_row_increment(
        self, client, target, temp_rows, start, increment, expected
    ):
        """
        test read_modify_write_row
        """
        from google.cloud.bigtable.data.read_modify_write_rules import IncrementRule

        row_key = b"test-row-key"
        family = TEST_FAMILY
        qualifier = b"test-qualifier"
        await temp_rows.add_row(
            row_key, value=start, family=family, qualifier=qualifier
        )

        rule = IncrementRule(family, qualifier, increment)
        result = await target.read_modify_write_row(row_key, rule)
        assert result.row_key == row_key
        assert len(result) == 1
        assert result[0].family == family
        assert result[0].qualifier == qualifier
        assert int(result[0]) == expected
        # ensure that reading from server gives same value
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == result[0].value

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @pytest.mark.parametrize(
        "start,append,expected",
        [
            (b"", b"", b""),
            ("", "", b""),
            (b"abc", b"123", b"abc123"),
            (b"abc", "123", b"abc123"),
            ("", b"1", b"1"),
            (b"abc", "", b"abc"),
            (b"hello", b"world", b"helloworld"),
        ],
    )
    @CrossSync.pytest
    async def test_read_modify_write_row_append(
        self, client, target, temp_rows, start, append, expected
    ):
        """
        test read_modify_write_row
        """
        from google.cloud.bigtable.data.read_modify_write_rules import AppendValueRule

        row_key = b"test-row-key"
        family = TEST_FAMILY
        qualifier = b"test-qualifier"
        await temp_rows.add_row(
            row_key, value=start, family=family, qualifier=qualifier
        )

        rule = AppendValueRule(family, qualifier, append)
        result = await target.read_modify_write_row(row_key, rule)
        assert result.row_key == row_key
        assert len(result) == 1
        assert result[0].family == family
        assert result[0].qualifier == qualifier
        assert result[0].value == expected
        # ensure that reading from server gives same value
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == result[0].value

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_read_modify_write_row_chained(self, client, target, temp_rows):
        """
        test read_modify_write_row with multiple rules
        """
        from google.cloud.bigtable.data.read_modify_write_rules import (
            AppendValueRule,
            IncrementRule,
        )

        row_key = b"test-row-key"
        family = TEST_FAMILY
        qualifier = b"test-qualifier"
        start_amount = 1
        increment_amount = 10
        await temp_rows.add_row(
            row_key, value=start_amount, family=family, qualifier=qualifier
        )
        rule = [
            IncrementRule(family, qualifier, increment_amount),
            AppendValueRule(family, qualifier, "hello"),
            AppendValueRule(family, qualifier, "world"),
            AppendValueRule(family, qualifier, "!"),
        ]
        result = await target.read_modify_write_row(row_key, rule)
        assert result.row_key == row_key
        assert result[0].family == family
        assert result[0].qualifier == qualifier
        # result should be a bytes number string for the IncrementRules, followed by the AppendValueRule values
        assert (
            result[0].value
            == (start_amount + increment_amount).to_bytes(8, "big", signed=True)
            + b"helloworld!"
        )
        # ensure that reading from server gives same value
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == result[0].value

    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @pytest.mark.parametrize(
        "start_val,predicate_range,expected_result",
        [
            (1, (0, 2), True),
            (-1, (0, 2), False),
        ],
    )
    @CrossSync.pytest
    async def test_check_and_mutate(
        self, client, target, temp_rows, start_val, predicate_range, expected_result
    ):
        """
        test that check_and_mutate_row works applies the right mutations, and returns the right result
        """
        from google.cloud.bigtable.data.mutations import SetCell
        from google.cloud.bigtable.data.row_filters import ValueRangeFilter

        row_key = b"test-row-key"
        family = TEST_FAMILY
        qualifier = b"test-qualifier"

        await temp_rows.add_row(
            row_key, value=start_val, family=family, qualifier=qualifier
        )

        false_mutation_value = b"false-mutation-value"
        false_mutation = SetCell(
            family=TEST_FAMILY, qualifier=qualifier, new_value=false_mutation_value
        )
        true_mutation_value = b"true-mutation-value"
        true_mutation = SetCell(
            family=TEST_FAMILY, qualifier=qualifier, new_value=true_mutation_value
        )
        predicate = ValueRangeFilter(predicate_range[0], predicate_range[1])
        result = await target.check_and_mutate_row(
            row_key,
            predicate,
            true_case_mutations=true_mutation,
            false_case_mutations=false_mutation,
        )
        assert result == expected_result
        # ensure cell is updated
        expected_value = (
            true_mutation_value if expected_result else false_mutation_value
        )
        assert (await temp_rows.retrieve_cell_value(target, row_key)) == expected_value

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't raise InvalidArgument",
    )
    @pytest.mark.usefixtures("client")
    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_check_and_mutate_empty_request(self, client, target):
        """
        check_and_mutate with no true or fale mutations should raise an error
        """
        from google.api_core import exceptions

        with pytest.raises(exceptions.InvalidArgument) as e:
            await target.check_and_mutate_row(
                b"row_key", None, true_case_mutations=None, false_case_mutations=None
            )
        assert "No mutations provided" in str(e.value)

    @pytest.mark.usefixtures("target")
    @CrossSync.convert(replace_symbols={"__anext__": "__next__"})
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_stream(self, target, temp_rows):
        """
        Ensure that the read_rows_stream method works
        """
        await temp_rows.add_row(b"row_key_1")
        await temp_rows.add_row(b"row_key_2")

        # full table scan
        generator = await target.read_rows_stream({})
        first_row = await generator.__anext__()
        second_row = await generator.__anext__()
        assert first_row.row_key == b"row_key_1"
        assert second_row.row_key == b"row_key_2"
        with pytest.raises(CrossSync.StopIteration):
            await generator.__anext__()

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows(self, target, temp_rows):
        """
        Ensure that the read_rows method works
        """
        await temp_rows.add_row(b"row_key_1")
        await temp_rows.add_row(b"row_key_2")
        # full table scan
        row_list = await target.read_rows({})
        assert len(row_list) == 2
        assert row_list[0].row_key == b"row_key_1"
        assert row_list[1].row_key == b"row_key_2"

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_sharded_simple(self, target, temp_rows):
        """
        Test read rows sharded with two queries
        """
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery

        await temp_rows.add_row(b"a")
        await temp_rows.add_row(b"b")
        await temp_rows.add_row(b"c")
        await temp_rows.add_row(b"d")
        query1 = ReadRowsQuery(row_keys=[b"a", b"c"])
        query2 = ReadRowsQuery(row_keys=[b"b", b"d"])
        row_list = await target.read_rows_sharded([query1, query2])
        assert len(row_list) == 4
        assert row_list[0].row_key == b"a"
        assert row_list[1].row_key == b"c"
        assert row_list[2].row_key == b"b"
        assert row_list[3].row_key == b"d"

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_sharded_from_sample(self, target, temp_rows):
        """
        Test end-to-end sharding
        """
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery, RowRange

        await temp_rows.add_row(b"a")
        await temp_rows.add_row(b"b")
        await temp_rows.add_row(b"c")
        await temp_rows.add_row(b"d")

        table_shard_keys = await target.sample_row_keys()
        query = ReadRowsQuery(row_ranges=[RowRange(start_key=b"b", end_key=b"z")])
        shard_queries = query.shard(table_shard_keys)
        row_list = await target.read_rows_sharded(shard_queries)
        assert len(row_list) == 3
        assert row_list[0].row_key == b"b"
        assert row_list[1].row_key == b"c"
        assert row_list[2].row_key == b"d"

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_sharded_filters_limits(self, target, temp_rows):
        """
        Test read rows sharded with filters and limits
        """
        from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery
        from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

        await temp_rows.add_row(b"a")
        await temp_rows.add_row(b"b")
        await temp_rows.add_row(b"c")
        await temp_rows.add_row(b"d")

        label_filter1 = ApplyLabelFilter("first")
        label_filter2 = ApplyLabelFilter("second")
        query1 = ReadRowsQuery(row_keys=[b"a", b"c"], limit=1, row_filter=label_filter1)
        query2 = ReadRowsQuery(row_keys=[b"b", b"d"], row_filter=label_filter2)
        row_list = await target.read_rows_sharded([query1, query2])
        assert len(row_list) == 3
        assert row_list[0].row_key == b"a"
        assert row_list[1].row_key == b"b"
        assert row_list[2].row_key == b"d"
        assert row_list[0][0].labels == ["first"]
        assert row_list[1][0].labels == ["second"]
        assert row_list[2][0].labels == ["second"]

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_range_query(self, target, temp_rows):
        """
        Ensure that the read_rows method works
        """
        from google.cloud.bigtable.data import ReadRowsQuery, RowRange

        await temp_rows.add_row(b"a")
        await temp_rows.add_row(b"b")
        await temp_rows.add_row(b"c")
        await temp_rows.add_row(b"d")
        # full table scan
        query = ReadRowsQuery(row_ranges=RowRange(start_key=b"b", end_key=b"d"))
        row_list = await target.read_rows(query)
        assert len(row_list) == 2
        assert row_list[0].row_key == b"b"
        assert row_list[1].row_key == b"c"

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_single_key_query(self, target, temp_rows):
        """
        Ensure that the read_rows method works with specified query
        """
        from google.cloud.bigtable.data import ReadRowsQuery

        await temp_rows.add_row(b"a")
        await temp_rows.add_row(b"b")
        await temp_rows.add_row(b"c")
        await temp_rows.add_row(b"d")
        # retrieve specific keys
        query = ReadRowsQuery(row_keys=[b"a", b"c"])
        row_list = await target.read_rows(query)
        assert len(row_list) == 2
        assert row_list[0].row_key == b"a"
        assert row_list[1].row_key == b"c"

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_read_rows_with_filter(self, target, temp_rows):
        """
        ensure filters are applied
        """
        from google.cloud.bigtable.data import ReadRowsQuery
        from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

        await temp_rows.add_row(b"a")
        await temp_rows.add_row(b"b")
        await temp_rows.add_row(b"c")
        await temp_rows.add_row(b"d")
        # retrieve keys with filter
        expected_label = "test-label"
        row_filter = ApplyLabelFilter(expected_label)
        query = ReadRowsQuery(row_filter=row_filter)
        row_list = await target.read_rows(query)
        assert len(row_list) == 4
        for row in row_list:
            assert row[0].labels == [expected_label]

    @pytest.mark.usefixtures("target")
    @CrossSync.convert(replace_symbols={"__anext__": "__next__", "aclose": "close"})
    @CrossSync.pytest
    async def test_read_rows_stream_close(self, target, temp_rows):
        """
        Ensure that the read_rows_stream can be closed
        """
        from google.cloud.bigtable.data import ReadRowsQuery

        await temp_rows.add_row(b"row_key_1")
        await temp_rows.add_row(b"row_key_2")
        # full table scan
        query = ReadRowsQuery()
        generator = await target.read_rows_stream(query)
        # grab first row
        first_row = await generator.__anext__()
        assert first_row.row_key == b"row_key_1"
        # close stream early
        await generator.aclose()
        with pytest.raises(CrossSync.StopIteration):
            await generator.__anext__()

    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_read_row(self, target, temp_rows):
        """
        Test read_row (single row helper)
        """
        from google.cloud.bigtable.data import Row

        await temp_rows.add_row(b"row_key_1", value=b"value")
        row = await target.read_row(b"row_key_1")
        assert isinstance(row, Row)
        assert row.row_key == b"row_key_1"
        assert row.cells[0].value == b"value"

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't raise InvalidArgument",
    )
    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_read_row_missing(self, target):
        """
        Test read_row when row does not exist
        """
        from google.api_core import exceptions

        row_key = "row_key_not_exist"
        result = await target.read_row(row_key)
        assert result is None
        with pytest.raises(exceptions.InvalidArgument) as e:
            await target.read_row("")
        assert "Row keys must be non-empty" in str(e)

    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_read_row_w_filter(self, target, temp_rows):
        """
        Test read_row (single row helper)
        """
        from google.cloud.bigtable.data import Row
        from google.cloud.bigtable.data.row_filters import ApplyLabelFilter

        await temp_rows.add_row(b"row_key_1", value=b"value")
        expected_label = "test-label"
        label_filter = ApplyLabelFilter(expected_label)
        row = await target.read_row(b"row_key_1", row_filter=label_filter)
        assert isinstance(row, Row)
        assert row.row_key == b"row_key_1"
        assert row.cells[0].value == b"value"
        assert row.cells[0].labels == [expected_label]

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't raise InvalidArgument",
    )
    @pytest.mark.usefixtures("target")
    @CrossSync.pytest
    async def test_row_exists(self, target, temp_rows):
        from google.api_core import exceptions

        """Test row_exists with rows that exist and don't exist"""
        assert await target.row_exists(b"row_key_1") is False
        await temp_rows.add_row(b"row_key_1")
        assert await target.row_exists(b"row_key_1") is True
        assert await target.row_exists("row_key_1") is True
        assert await target.row_exists(b"row_key_2") is False
        assert await target.row_exists("row_key_2") is False
        assert await target.row_exists("3") is False
        await temp_rows.add_row(b"3")
        assert await target.row_exists(b"3") is True
        with pytest.raises(exceptions.InvalidArgument) as e:
            await target.row_exists("")
        assert "Row keys must be non-empty" in str(e)

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @pytest.mark.parametrize(
        "cell_value,filter_input,expect_match",
        [
            (b"abc", b"abc", True),
            (b"abc", "abc", True),
            (b".", ".", True),
            (".*", ".*", True),
            (".*", b".*", True),
            ("a", ".*", False),
            (b".*", b".*", True),
            (r"\a", r"\a", True),
            (b"\xe2\x98\x83", "☃", True),
            ("☃", "☃", True),
            (r"\C☃", r"\C☃", True),
            (1, 1, True),
            (2, 1, False),
            (68, 68, True),
            ("D", 68, False),
            (68, "D", False),
            (-1, -1, True),
            (2852126720, 2852126720, True),
            (-1431655766, -1431655766, True),
            (-1431655766, -1, False),
        ],
    )
    @CrossSync.pytest
    async def test_literal_value_filter(
        self, target, temp_rows, cell_value, filter_input, expect_match
    ):
        """
        Literal value filter does complex escaping on re2 strings.
        Make sure inputs are properly interpreted by the server
        """
        from google.cloud.bigtable.data import ReadRowsQuery
        from google.cloud.bigtable.data.row_filters import LiteralValueFilter

        f = LiteralValueFilter(filter_input)
        await temp_rows.add_row(b"row_key_1", value=cell_value)
        query = ReadRowsQuery(row_filter=f)
        row_list = await target.read_rows(query)
        assert len(row_list) == bool(expect_match), (
            f"row {type(cell_value)}({cell_value}) not found with {type(filter_input)}({filter_input}) filter"
        )

    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @pytest.mark.parametrize(
        "cell_value,mask,expect_match",
        [
            (b"\x01\x02\x03", b"\x01\x02\x03", True),
            (b"\x01\x02\x03", b"\x01\x00\x00", True),
            (b"\x00\x02\x03", b"\x01\x00\x00", False),
        ],
    )
    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="value_bitmask_filter not supported by emulator",
    )
    @CrossSync.pytest
    async def test_value_bitmask_filter(
        self, target, temp_rows, cell_value, mask, expect_match
    ):
        """
        ValueBitmaskFilter matches cells where (value & mask) == mask.
        Make sure inputs are properly interpreted by the server.
        """
        from google.cloud.bigtable.data import ReadRowsQuery
        from google.cloud.bigtable.data.row_filters import ValueBitmaskFilter

        f = ValueBitmaskFilter(mask)
        await temp_rows.add_row(b"row_key_1", value=cell_value)
        query = ReadRowsQuery(row_keys=[b"row_key_1"], row_filter=f)
        row_list = await target.read_rows(query)
        assert len(row_list) == bool(expect_match), (
            f"row {cell_value!r} not matched as {expect_match} with {mask!r} bitmask filter"
        )

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't support SQL",
    )
    @CrossSync.pytest
    async def test_authorized_view_unauthenticated(
        self, client, authorized_view_id, instance_id, table_id
    ):
        """
        Requesting family outside authorized family_subset should raise exception
        """
        from google.cloud.bigtable.data.mutations import SetCell

        async with client.get_authorized_view(
            instance_id, table_id, authorized_view_id
        ) as view:
            mutation = SetCell(family="unauthorized", qualifier="q", new_value="v")
            with pytest.raises(PermissionDenied) as e:
                await view.mutate_row(b"row-key", mutation)
            assert "outside the Authorized View" in e.value.message

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't support SQL",
    )
    @pytest.mark.usefixtures("client")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    @CrossSync.pytest
    async def test_execute_query_simple(self, client, table_id, instance_id):
        result = await client.execute_query("SELECT 1 AS a, 'foo' AS b", instance_id)
        rows = [r async for r in result]
        assert len(rows) == 1
        row = rows[0]
        assert row["a"] == 1
        assert row["b"] == "foo"

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't support SQL",
    )
    @CrossSync.pytest
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    async def test_execute_against_target(
        self, client, instance_id, table_id, temp_rows, column_family_config
    ):
        await temp_rows.add_row(b"row_key_1")
        result = await client.execute_query(
            "SELECT * FROM `" + table_id + "`", instance_id
        )
        rows = [r async for r in result]

        assert len(rows) == 1
        assert rows[0]["_key"] == b"row_key_1"
        family_map = rows[0][TEST_FAMILY]
        assert len(family_map) == 1
        assert family_map[b"q"] == b"test-value"
        assert len(rows[0][TEST_FAMILY_2]) == 0
        md = result.metadata
        # we expect it to fetch each column family, plus _key
        # add additional families here if column_family_config changes
        assert len(md) == len(column_family_config) + 1
        assert md["_key"].column_type == SqlType.Bytes()
        assert md[TEST_FAMILY].column_type == SqlType.Map(
            SqlType.Bytes(), SqlType.Bytes()
        )
        assert md[TEST_FAMILY_2].column_type == SqlType.Map(
            SqlType.Bytes(), SqlType.Bytes()
        )
        assert md[TEST_AGGREGATE_FAMILY].column_type == SqlType.Map(
            SqlType.Bytes(), SqlType.Int64()
        )

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't support SQL",
    )
    @CrossSync.pytest
    @pytest.mark.usefixtures("client")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    async def test_execute_query_params(self, client, table_id, instance_id):
        query = (
            "SELECT @stringParam AS strCol, @bytesParam as bytesCol, @int64Param AS intCol, "
            "@float32Param AS float32Col, @float64Param AS float64Col, @boolParam AS boolCol, "
            "@tsParam AS tsCol, @dateParam AS dateCol, @byteArrayParam AS byteArrayCol, "
            "@stringArrayParam AS stringArrayCol, @intArrayParam AS intArrayCol, "
            "@float32ArrayParam AS float32ArrayCol, @float64ArrayParam AS float64ArrayCol, "
            "@boolArrayParam AS boolArrayCol, @tsArrayParam AS tsArrayCol, "
            "@dateArrayParam AS dateArrayCol"
        )
        parameters = {
            "stringParam": "foo",
            "bytesParam": b"bar",
            "int64Param": 12,
            "float32Param": 1.1,
            "float64Param": 1.2,
            "boolParam": True,
            "tsParam": datetime.datetime.fromtimestamp(1000, tz=datetime.timezone.utc),
            "dateParam": datetime.date(2025, 1, 16),
            "byteArrayParam": [b"foo", b"bar", None],
            "stringArrayParam": ["foo", "bar", None],
            "intArrayParam": [1, None, 2],
            "float32ArrayParam": [1.2, None, 1.3],
            "float64ArrayParam": [1.4, None, 1.5],
            "boolArrayParam": [None, False, True],
            "tsArrayParam": [
                datetime.datetime.fromtimestamp(1000, tz=datetime.timezone.utc),
                datetime.datetime.fromtimestamp(2000, tz=datetime.timezone.utc),
                None,
            ],
            "dateArrayParam": [
                datetime.date(2025, 1, 16),
                datetime.date(2025, 1, 17),
                None,
            ],
        }
        param_types = {
            "stringParam": SqlType.String(),
            "bytesParam": SqlType.Bytes(),
            "int64Param": SqlType.Int64(),
            "float32Param": SqlType.Float32(),
            "float64Param": SqlType.Float64(),
            "boolParam": SqlType.Bool(),
            "tsParam": SqlType.Timestamp(),
            "dateParam": SqlType.Date(),
            "byteArrayParam": SqlType.Array(SqlType.Bytes()),
            "stringArrayParam": SqlType.Array(SqlType.String()),
            "intArrayParam": SqlType.Array(SqlType.Int64()),
            "float32ArrayParam": SqlType.Array(SqlType.Float32()),
            "float64ArrayParam": SqlType.Array(SqlType.Float64()),
            "boolArrayParam": SqlType.Array(SqlType.Bool()),
            "tsArrayParam": SqlType.Array(SqlType.Timestamp()),
            "dateArrayParam": SqlType.Array(SqlType.Date()),
        }

        result = await client.execute_query(
            query, instance_id, parameters=parameters, parameter_types=param_types
        )
        rows = [r async for r in result]
        assert len(rows) == 1
        row = rows[0]
        assert row["strCol"] == parameters["stringParam"]
        assert row["bytesCol"] == parameters["bytesParam"]
        assert row["intCol"] == parameters["int64Param"]
        assert row["float32Col"] == pytest.approx(parameters["float32Param"])
        assert row["float64Col"] == pytest.approx(parameters["float64Param"])
        assert row["boolCol"] == parameters["boolParam"]
        assert row["tsCol"] == parameters["tsParam"]
        assert row["dateCol"] == date_pb2.Date(year=2025, month=1, day=16)
        assert row["stringArrayCol"] == parameters["stringArrayParam"]
        assert row["byteArrayCol"] == parameters["byteArrayParam"]
        assert row["intArrayCol"] == parameters["intArrayParam"]
        assert row["float32ArrayCol"] == pytest.approx(parameters["float32ArrayParam"])
        assert row["float64ArrayCol"] == pytest.approx(parameters["float64ArrayParam"])
        assert row["boolArrayCol"] == parameters["boolArrayParam"]
        assert row["tsArrayCol"] == parameters["tsArrayParam"]
        assert row["dateArrayCol"] == [
            date_pb2.Date(year=2025, month=1, day=16),
            date_pb2.Date(year=2025, month=1, day=17),
            None,
        ]

    @pytest.mark.skipif(
        bool(os.environ.get(BIGTABLE_EMULATOR)),
        reason="emulator doesn't support SQL",
    )
    @CrossSync.pytest
    @pytest.mark.usefixtures("target")
    @CrossSync.Retry(
        predicate=retry.if_exception_type(ClientError), initial=1, maximum=5
    )
    async def test_execute_metadata_on_empty_response(
        self, client, instance_id, table_id, temp_rows, column_family_config
    ):
        await temp_rows.add_row(b"row_key_1")
        result = await client.execute_query(
            "SELECT * FROM `" + table_id + "` WHERE _key='non-existent'", instance_id
        )
        rows = [r async for r in result]

        assert len(rows) == 0
        md = result.metadata
        # we expect it to fetch each column family, plus _key
        # add additional families here if column_family_config change
        assert len(md) == len(column_family_config) + 1
        assert md["_key"].column_type == SqlType.Bytes()
        assert md[TEST_FAMILY].column_type == SqlType.Map(
            SqlType.Bytes(), SqlType.Bytes()
        )
        assert md[TEST_FAMILY_2].column_type == SqlType.Map(
            SqlType.Bytes(), SqlType.Bytes()
        )
        assert md[TEST_AGGREGATE_FAMILY].column_type == SqlType.Map(
            SqlType.Bytes(), SqlType.Int64()
        )

    @pytest.fixture(scope="session")
    def metrics_client(self, client):
        if client._emulator_host is not None:
            pytest.skip("Metrics export disabled when running against emulator")
        yield client._metrics.handlers[0]._exporter.client

    @pytest.mark.order("last")
    @pytest.mark.parametrize(
        "metric,methods",
        [
            ("attempt_latencies", [m.value for m in OperationType]),
            ("operation_latencies", [m.value for m in OperationType]),
            ("retry_count", [m.value for m in OperationType]),
            ("first_response_latencies", [OperationType.READ_ROWS]),
            ("server_latencies", [m.value for m in OperationType]),
            ("connectivity_error_count", [m.value for m in OperationType]),
            ("application_blocking_latencies", [OperationType.READ_ROWS]),
        ],
    )
    @retry.Retry(predicate=retry.if_exception_type(AssertionError, ServerError))
    def test_metric_existence(
        self, client, table_id, metrics_client, start_timestamp, metric, methods
    ):
        """
        Checks to make sure metrics were exported by tests

        Runs at the end of test suite, to let other tests write metrics
        """
        end_timestamp = datetime.datetime.now(datetime.timezone.utc)
        for m in methods:
            metric_filter = (
                f'metric.type = "bigtable.googleapis.com/client/{metric}" '
                + f'AND metric.labels.client_name = "python-bigtable/{client._client_version()}" '
                + f'AND resource.labels.table = "{table_id}" '
            )
            results = list(
                metrics_client.list_time_series(
                    name=f"projects/{client.project}",
                    filter=metric_filter,
                    interval={"start_time": start_timestamp, "end_time": end_timestamp},
                    view=0,
                )
            )
            assert len(results) > 0, f"No data found for {metric} {m}"
            for series in results:
                assert series.resource.labels.get("table") == table_id
                if "table_id" in series.metric.labels:
                    assert series.metric.labels["table_id"] == table_id
