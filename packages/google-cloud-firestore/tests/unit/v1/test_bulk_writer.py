# # Copyright 2021 Google LLC All rights reserved.
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
from typing import List, NoReturn, Optional, Tuple, Type

import aiounittest  # type: ignore
import mock
import pytest

from google.cloud.firestore_v1 import async_client, base_client, client


def _make_no_send_bulk_writer(*args, **kwargs):
    from google.rpc import status_pb2

    from google.cloud.firestore_v1._helpers import build_timestamp
    from google.cloud.firestore_v1.bulk_batch import BulkWriteBatch
    from google.cloud.firestore_v1.bulk_writer import BulkWriter, BulkWriterOperation
    from google.cloud.firestore_v1.types.firestore import BatchWriteResponse
    from google.cloud.firestore_v1.types.write import WriteResult
    from tests.unit.v1._test_helpers import FakeThreadPoolExecutor

    class NoSendBulkWriter(BulkWriter):
        """Test-friendly BulkWriter subclass whose `_send` method returns faked
        BatchWriteResponse instances and whose _process_response` method stores
        those faked instances for later evaluation."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._responses: List[
                Tuple[BulkWriteBatch, BatchWriteResponse, BulkWriterOperation]
            ] = []
            self._fail_indices: List[int] = []

        def _send(self, batch: BulkWriteBatch) -> BatchWriteResponse:
            """Generate a fake `BatchWriteResponse` for the supplied batch instead
            of actually submitting it to the server.
            """
            return BatchWriteResponse(
                write_results=[
                    WriteResult(update_time=build_timestamp())
                    if index not in self._fail_indices
                    else WriteResult()
                    for index, el in enumerate(batch._document_references.values())
                ],
                status=[
                    status_pb2.Status(code=0 if index not in self._fail_indices else 1)
                    for index, el in enumerate(batch._document_references.values())
                ],
            )

        def _process_response(
            self,
            batch: BulkWriteBatch,
            response: BatchWriteResponse,
            operations: List[BulkWriterOperation],
        ) -> NoReturn:
            super()._process_response(batch, response, operations)
            self._responses.append((batch, response, operations))

        def _instantiate_executor(self):
            return FakeThreadPoolExecutor()

    return NoSendBulkWriter(*args, **kwargs)


def _make_credentials():
    from google.auth.credentials import Credentials

    return mock.create_autospec(Credentials, project_id="project-id")


class _SyncClientMixin:
    """Mixin which helps a `_BaseBulkWriterTests` subclass simulate usage of
    synchronous Clients, Collections, DocumentReferences, etc."""

    _PRESERVES_CLIENT = True

    @staticmethod
    def _make_client() -> client.Client:
        return client.Client(credentials=_make_credentials(), project="project-id")


class _AsyncClientMixin:
    """Mixin which helps a `_BaseBulkWriterTests` subclass simulate usage of
    AsyncClients, AsyncCollections, AsyncDocumentReferences, etc."""

    _PRESERVES_CLIENT = False

    @staticmethod
    def _make_client() -> async_client.AsyncClient:
        return async_client.AsyncClient(
            credentials=_make_credentials(), project="project-id"
        )


class _BaseBulkWriterTests:
    def _basebulkwriter_ctor_helper(self, **kw):
        from google.cloud.firestore_v1.bulk_writer import BulkWriterOptions

        client = self._make_client()

        if not self._PRESERVES_CLIENT:
            sync_copy = client._sync_copy = object()

        bw = _make_no_send_bulk_writer(client, **kw)

        if self._PRESERVES_CLIENT:
            assert bw._client is client
        else:
            assert bw._client is sync_copy

        if "options" in kw:
            assert bw._options is kw["options"]
        else:
            assert bw._options == BulkWriterOptions()

    def test_basebulkwriter_ctor_defaults(self):
        self._basebulkwriter_ctor_helper()

    def test_basebulkwriter_ctor_explicit(self):
        from google.cloud.firestore_v1.bulk_writer import BulkRetry, BulkWriterOptions

        options = BulkWriterOptions(retry=BulkRetry.immediate)
        self._basebulkwriter_ctor_helper(options=options)

    def test_bulkwriteroperation_ctor(self):
        from google.cloud.firestore_v1.bulk_writer import BulkWriterOperation

        op = BulkWriterOperation()
        assert op.attempts == 0
        attempts = 9
        op2 = BulkWriterOperation(attempts)
        assert op2.attempts == attempts

    def _doc_iter(self, client, num: int, ids: Optional[List[str]] = None):
        for _ in range(num):
            id: Optional[str] = ids[_] if ids else None
            yield _get_document_reference(client, id=id), {"id": _}

    def _verify_bw_activity(self, bw, counts: List[Tuple[int, int]]):
        """
        Args:
            bw: (BulkWriter)
                The BulkWriter instance to inspect.
            counts: (tuple) A sequence of integer pairs, with 0-index integers
                representing the size of sent batches, and 1-index integers
                representing the number of times batches of that size should
                have been sent.
        """
        from google.cloud.firestore_v1.types.firestore import BatchWriteResponse

        total_batches = sum([el[1] for el in counts])
        assert len(bw._responses) == total_batches
        docs_count = {}
        resp: BatchWriteResponse
        for _, resp, ops in bw._responses:
            docs_count.setdefault(len(resp.write_results), 0)
            docs_count[len(resp.write_results)] += 1

        assert len(docs_count) == len(counts)
        for size, num_sent in counts:
            assert docs_count[size] == num_sent

        # Assert flush leaves no operation behind
        assert len(bw._operations) == 0

    def test_basebulkwriter_create_calls_send_correctly(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for ref, data in self._doc_iter(client, 101):
            bw.create(ref, data)
        bw.flush()
        # Full batches with 20 items should have been sent 5 times, and a 1-item
        # batch should have been sent once.
        self._verify_bw_activity(
            bw,
            [
                (
                    20,
                    5,
                ),
                (
                    1,
                    1,
                ),
            ],
        )

    def test_basebulkwriter_delete_calls_send_correctly(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for ref, _ in self._doc_iter(client, 101):
            bw.delete(ref)
        bw.flush()
        # Full batches with 20 items should have been sent 5 times, and a 1-item
        # batch should have been sent once.
        self._verify_bw_activity(
            bw,
            [
                (
                    20,
                    5,
                ),
                (
                    1,
                    1,
                ),
            ],
        )

    def test_basebulkwriter_delete_separates_batch(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        ref = _get_document_reference(client, id="asdf")
        bw.create(ref, {})
        bw.delete(ref)
        bw.flush()
        # Consecutive batches each with 1 operation should have been sent
        self._verify_bw_activity(
            bw,
            [
                (
                    1,
                    2,
                )
            ],
        )

    def test_basebulkwriter_set_calls_send_correctly(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for ref, data in self._doc_iter(client, 101):
            bw.set(ref, data)
        bw.flush()
        # Full batches with 20 items should have been sent 5 times, and a 1-item
        # batch should have been sent once.
        self._verify_bw_activity(
            bw,
            [
                (
                    20,
                    5,
                ),
                (
                    1,
                    1,
                ),
            ],
        )

    def test_basebulkwriter_update_calls_send_correctly(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for ref, data in self._doc_iter(client, 101):
            bw.update(ref, data)
        bw.flush()
        # Full batches with 20 items should have been sent 5 times, and a 1-item
        # batch should have been sent once.
        self._verify_bw_activity(
            bw,
            [
                (
                    20,
                    5,
                ),
                (
                    1,
                    1,
                ),
            ],
        )

    def test_basebulkwriter_update_separates_batch(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        ref = _get_document_reference(client, id="asdf")
        bw.create(ref, {})
        bw.update(ref, {"field": "value"})
        bw.flush()
        # Full batches with 20 items should have been sent 5 times, and a 1-item
        # batch should have been sent once.
        self._verify_bw_activity(
            bw,
            [
                (
                    1,
                    2,
                )
            ],
        )

    def test_basebulkwriter_invokes_success_callbacks_successfully(self):
        from google.cloud.firestore_v1.base_document import BaseDocumentReference
        from google.cloud.firestore_v1.bulk_batch import BulkWriteBatch
        from google.cloud.firestore_v1.bulk_writer import BulkWriter
        from google.cloud.firestore_v1.types.firestore import BatchWriteResponse
        from google.cloud.firestore_v1.types.write import WriteResult

        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        bw._fail_indices = []
        bw._sent_batches = 0
        bw._sent_documents = 0

        def _on_batch(batch, response, bulk_writer):
            assert isinstance(batch, BulkWriteBatch)
            assert isinstance(response, BatchWriteResponse)
            assert isinstance(bulk_writer, BulkWriter)
            bulk_writer._sent_batches += 1

        def _on_write(ref, result, bulk_writer):
            assert isinstance(ref, BaseDocumentReference)
            assert isinstance(result, WriteResult)
            assert isinstance(bulk_writer, BulkWriter)
            bulk_writer._sent_documents += 1

        bw.on_write_result(_on_write)
        bw.on_batch_result(_on_batch)

        for ref, data in self._doc_iter(client, 101):
            bw.create(ref, data)
        bw.flush()

        assert bw._sent_batches == 6
        assert bw._sent_documents == 101
        assert len(bw._operations) == 0

    def test_basebulkwriter_invokes_error_callbacks_successfully(self):
        from google.cloud.firestore_v1.bulk_writer import BulkWriteFailure

        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._sent_batches = 0
        bw._sent_documents = 0
        bw._total_retries = 0

        times_to_retry = 1

        def _on_batch(batch, response, bulk_writer):
            bulk_writer._sent_batches += 1

        def _on_write(ref, result, bulk_writer):
            bulk_writer._sent_documents += 1  # pragma: NO COVER

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_batch_result(_on_batch)
        bw.on_write_result(_on_write)
        bw.on_write_error(_on_error)

        for ref, data in self._doc_iter(client, 1):
            bw.create(ref, data)
        bw.flush()

        assert bw._sent_documents == 0
        assert bw._total_retries == times_to_retry
        assert bw._sent_batches == 2
        assert len(bw._operations) == 0

    def test_basebulkwriter_invokes_error_callbacks_successfully_multiple_retries(self):
        from google.cloud.firestore_v1.bulk_writer import (
            BulkRetry,
            BulkWriteFailure,
            BulkWriterOptions,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._sent_batches = 0
        bw._sent_documents = 0
        bw._total_retries = 0

        times_to_retry = 10

        def _on_batch(batch, response, bulk_writer):
            bulk_writer._sent_batches += 1

        def _on_write(ref, result, bulk_writer):
            bulk_writer._sent_documents += 1

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_batch_result(_on_batch)
        bw.on_write_result(_on_write)
        bw.on_write_error(_on_error)

        for ref, data in self._doc_iter(client, 2):
            bw.create(ref, data)
        bw.flush()

        assert bw._sent_documents == 1
        assert bw._total_retries == times_to_retry
        assert bw._sent_batches == times_to_retry + 1
        assert len(bw._operations) == 0

    def test_basebulkwriter_default_error_handler(self):
        from google.cloud.firestore_v1.bulk_writer import BulkRetry, BulkWriterOptions

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        bw._attempts = 0

        def _on_error(error, bw):
            bw._attempts = error.attempts
            return bw._default_on_error(error, bw)

        bw.on_write_error(_on_error)

        # First document in each batch will "fail"
        bw._fail_indices = [0]
        for ref, data in self._doc_iter(client, 1):
            bw.create(ref, data)
        bw.flush()
        assert bw._attempts == 15

    def test_basebulkwriter_handles_errors_and_successes_correctly(self):
        from google.cloud.firestore_v1.bulk_writer import (
            BulkRetry,
            BulkWriteFailure,
            BulkWriterOptions,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._sent_batches = 0
        bw._sent_documents = 0
        bw._total_retries = 0

        times_to_retry = 1

        def _on_batch(batch, response, bulk_writer):
            bulk_writer._sent_batches += 1

        def _on_write(ref, result, bulk_writer):
            bulk_writer._sent_documents += 1

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_batch_result(_on_batch)
        bw.on_write_result(_on_write)
        bw.on_write_error(_on_error)

        for ref, data in self._doc_iter(client, 40):
            bw.create(ref, data)
        bw.flush()

        # 19 successful writes per batch
        assert bw._sent_documents == 38
        assert bw._total_retries == times_to_retry * 2
        assert bw._sent_batches == 4
        assert len(bw._operations) == 0

    def test_basebulkwriter_create_retriable(self):
        from google.cloud.firestore_v1.bulk_writer import (
            BulkRetry,
            BulkWriteFailure,
            BulkWriterOptions,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._total_retries = 0
        times_to_retry = 6

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_write_error(_on_error)

        for ref, data in self._doc_iter(client, 1):
            bw.create(ref, data)
        bw.flush()

        assert bw._total_retries == times_to_retry
        assert len(bw._operations) == 0

    def test_basebulkwriter_delete_retriable(self):
        from google.cloud.firestore_v1.bulk_writer import (
            BulkRetry,
            BulkWriteFailure,
            BulkWriterOptions,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._total_retries = 0
        times_to_retry = 6

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_write_error(_on_error)

        for ref, _ in self._doc_iter(client, 1):
            bw.delete(ref)
        bw.flush()

        assert bw._total_retries == times_to_retry
        assert len(bw._operations) == 0

    def test_basebulkwriter_set_retriable(self):
        from google.cloud.firestore_v1.bulk_writer import (
            BulkRetry,
            BulkWriteFailure,
            BulkWriterOptions,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._total_retries = 0
        times_to_retry = 6

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_write_error(_on_error)

        for ref, data in self._doc_iter(client, 1):
            bw.set(ref, data)
        bw.flush()

        assert bw._total_retries == times_to_retry
        assert len(bw._operations) == 0

    def test_basebulkwriter_update_retriable(self):
        from google.cloud.firestore_v1.bulk_writer import (
            BulkRetry,
            BulkWriteFailure,
            BulkWriterOptions,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client,
            options=BulkWriterOptions(retry=BulkRetry.immediate),
        )
        # First document in each batch will "fail"
        bw._fail_indices = [0]
        bw._total_retries = 0
        times_to_retry = 6

        def _on_error(error, bw) -> bool:
            assert isinstance(error, BulkWriteFailure)
            should_retry = error.attempts < times_to_retry
            if should_retry:
                bw._total_retries += 1
            return should_retry

        bw.on_write_error(_on_error)

        for ref, data in self._doc_iter(client, 1):
            bw.update(ref, data)
        bw.flush()

        assert bw._total_retries == times_to_retry
        assert len(bw._operations) == 0

    def test_basebulkwriter_serial_calls_send_correctly(self):
        from google.cloud.firestore_v1.bulk_writer import BulkWriterOptions, SendMode

        client = self._make_client()
        bw = _make_no_send_bulk_writer(
            client, options=BulkWriterOptions(mode=SendMode.serial)
        )
        for ref, data in self._doc_iter(client, 101):
            bw.create(ref, data)
        bw.flush()
        # Full batches with 20 items should have been sent 5 times, and a 1-item
        # batch should have been sent once.
        self._verify_bw_activity(
            bw,
            [
                (
                    20,
                    5,
                ),
                (
                    1,
                    1,
                ),
            ],
        )

    def test_basebulkwriter_separates_same_document(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for ref, data in self._doc_iter(client, 2, ["same-id", "same-id"]):
            bw.create(ref, data)
        bw.flush()
        # Seeing the same document twice should lead to separate batches
        # Expect to have sent 1-item batches twice.
        self._verify_bw_activity(
            bw,
            [
                (
                    1,
                    2,
                )
            ],
        )

    def test_basebulkwriter_separates_same_document_different_operation(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for ref, data in self._doc_iter(client, 1, ["same-id"]):
            bw.create(ref, data)
            bw.set(ref, data)
        bw.flush()
        # Seeing the same document twice should lead to separate batches.
        # Expect to have sent 1-item batches twice.
        self._verify_bw_activity(
            bw,
            [
                (
                    1,
                    2,
                )
            ],
        )

    def test_basebulkwriter_ensure_sending_repeatedly_callable(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        bw._is_sending = True
        bw._ensure_sending()

    def test_basebulkwriter_flush_close_repeatedly_callable(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        bw.flush()
        bw.flush()
        bw.close()

    def test_basebulkwriter_flush_sends_in_progress(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        bw.create(_get_document_reference(client), {"whatever": "you want"})
        bw.flush()
        self._verify_bw_activity(
            bw,
            [
                (
                    1,
                    1,
                )
            ],
        )

    def test_basebulkwriter_flush_sends_all_queued_batches(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        for _ in range(2):
            bw.create(_get_document_reference(client), {"whatever": "you want"})
            bw._queued_batches.append(bw._operations)
            bw._reset_operations()
        bw.flush()
        self._verify_bw_activity(
            bw,
            [
                (
                    1,
                    2,
                )
            ],
        )

    def test_basebulkwriter_cannot_add_after_close(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        bw.close()
        with pytest.raises(Exception):
            bw._verify_not_closed()

    def test_basebulkwriter_multiple_flushes(self):
        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        bw.flush()
        bw.flush()

    def test_basebulkwriter_update_raises_with_bad_option(self):
        from google.cloud.firestore_v1._helpers import ExistsOption

        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)
        with pytest.raises(ValueError):
            bw.update(
                _get_document_reference(client, "id"),
                {},
                option=ExistsOption(exists=True),
            )

    def test_basebulkwriter_reentrancy_empty_deque_retry(self):
        # See https://github.com/googleapis/google-cloud-python/issues/16138
        import bisect
        import datetime

        from google.cloud.firestore_v1.bulk_writer import (
            BulkWriterCreateOperation,
            OperationRetry,
        )

        client = self._make_client()
        bw = _make_no_send_bulk_writer(client)

        ref1 = _get_document_reference(client, id="doc1")
        ref2 = _get_document_reference(client, id="doc2")
        data = {"field": "value"}

        # Put ref1 in current operations to trigger a document path collision
        # and subsequent flush/enqueue when we create ref1 again.
        bw.create(ref1, data)

        run_at = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(
            seconds=1
        )

        retry1 = OperationRetry(
            operation=BulkWriterCreateOperation(reference=ref1, document_data=data),
            run_at=run_at,
        )
        retry2 = OperationRetry(
            operation=BulkWriterCreateOperation(reference=ref2, document_data=data),
            run_at=run_at,
        )

        bisect.insort(bw._retries, retry1)
        bisect.insort(bw._retries, retry2)

        # This should not raise IndexError: pop from an empty deque due to re-entrant scheduling
        bw._schedule_ready_retries()


class TestSyncBulkWriter(_SyncClientMixin, _BaseBulkWriterTests):
    """All BulkWriters are opaquely async, but this one simulates a BulkWriter
    dealing with synchronous DocumentReferences."""


class TestAsyncBulkWriter(
    _AsyncClientMixin, _BaseBulkWriterTests, aiounittest.AsyncTestCase
):
    """All BulkWriters are opaquely async, but this one simulates a BulkWriter
    dealing with AsyncDocumentReferences."""


def _make_sync_client() -> client.Client:
    return client.Client(credentials=_make_credentials(), project="project-id")


def test_scheduling_max_in_flight_honored():
    bw = _make_no_send_bulk_writer(_make_sync_client())
    # Calling this method sets up all the internal timekeeping machinery
    bw._rate_limiter.take_tokens(20)

    # Now we pretend that all tokens have been consumed. This will force us
    # to wait actual, real world milliseconds before being cleared to send more
    bw._rate_limiter._available_tokens = 0

    st = datetime.datetime.now()

    # Make a real request, subject to the actual real world clock.
    # As this request is 1/10th the per second limit, we should wait ~100ms
    bw._request_send(50)

    assert datetime.datetime.now() - st > datetime.timedelta(milliseconds=90)


def test_scheduling_operation_retry_scheduling():
    from google.cloud.firestore_v1.bulk_writer import (
        BulkWriterCreateOperation,
        OperationRetry,
    )

    now = datetime.datetime.now()
    one_second_from_now = now + datetime.timedelta(seconds=1)

    db = _make_sync_client()
    operation = BulkWriterCreateOperation(
        reference=db.collection("asdf").document("asdf"),
        document_data={"does.not": "matter"},
    )
    operation2 = BulkWriterCreateOperation(
        reference=db.collection("different").document("document"),
        document_data={"different": "values"},
    )

    op1 = OperationRetry(operation=operation, run_at=now)
    op2 = OperationRetry(operation=operation2, run_at=now)
    op3 = OperationRetry(operation=operation, run_at=one_second_from_now)

    assert op1 < op3
    assert op1 < op3.run_at
    assert op2 < op3
    assert op2 < op3.run_at

    # Because these have the same values for `run_at`, neither should conclude
    # they are less than the other. It is okay that if we checked them with
    # greater-than evaluation, they would return True (because
    # @functools.total_ordering flips the result from __lt__). In practice,
    # this only arises for actual ties, and we don't care how actual ties are
    # ordered as we maintain the sorted list of scheduled retries.
    assert not (op1 < op2)
    assert not (op2 < op1)


def _get_document_reference(
    client: base_client.BaseClient,
    collection_name: Optional[str] = "col",
    id: Optional[str] = None,
) -> Type:
    return client.collection(collection_name).document(id)
