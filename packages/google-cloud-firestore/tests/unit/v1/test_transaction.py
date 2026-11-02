# Copyright 2017 Google LLC All rights reserved.
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

import mock
import pytest

from tests.unit.v1.test_base_query import _make_query_response


def _make_transaction(*args, **kwargs):
    from google.cloud.firestore_v1.transaction import Transaction

    return Transaction(*args, **kwargs)


def test_transaction_constructor_defaults():
    from google.cloud.firestore_v1.transaction import MAX_ATTEMPTS

    transaction = _make_transaction(mock.sentinel.client)
    assert transaction._client is mock.sentinel.client
    assert transaction._write_pbs == []
    assert transaction._max_attempts == MAX_ATTEMPTS
    assert not transaction._read_only
    assert transaction._id is None
    assert transaction.write_results is None
    assert transaction.commit_time is None


def test_transaction_constructor_explicit():
    transaction = _make_transaction(
        mock.sentinel.client, max_attempts=10, read_only=True
    )
    assert transaction._client is mock.sentinel.client
    assert transaction._write_pbs == []
    assert transaction._max_attempts == 10
    assert transaction._read_only
    assert transaction._id is None


def test_transaction__add_write_pbs_failure():
    from google.cloud.firestore_v1.base_transaction import _WRITE_READ_ONLY

    batch = _make_transaction(mock.sentinel.client, read_only=True)
    assert batch._write_pbs == []
    with pytest.raises(ValueError) as exc_info:
        batch._add_write_pbs([mock.sentinel.write])

    assert exc_info.value.args == (_WRITE_READ_ONLY,)
    assert batch._write_pbs == []


def test_transaction__add_write_pbs():
    batch = _make_transaction(mock.sentinel.client)
    assert batch._write_pbs == []
    batch._add_write_pbs([mock.sentinel.write])
    assert batch._write_pbs == [mock.sentinel.write]


def test_transaction__clean_up():
    transaction = _make_transaction(mock.sentinel.client)
    transaction._write_pbs.extend([mock.sentinel.write_pb1, mock.sentinel.write])
    transaction._id = b"not-this-time-my-friend"

    ret_val = transaction._clean_up()
    assert ret_val is None

    assert transaction._write_pbs == []
    assert transaction._id is None


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__begin(database):
    from google.cloud.firestore_v1.services.firestore import client as firestore_client
    from google.cloud.firestore_v1.types import firestore

    # Create a minimal fake GAPIC with a dummy result.
    firestore_api = mock.create_autospec(
        firestore_client.FirestoreClient, instance=True
    )
    txn_id = b"to-begin"
    response = firestore.BeginTransactionResponse(transaction=txn_id)
    firestore_api.begin_transaction.return_value = response

    # Attach the fake GAPIC to a real client.
    client = _make_client(database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a transaction and ``begin()`` it.
    transaction = _make_transaction(client)
    assert transaction._id is None

    ret_val = transaction._begin()
    assert ret_val is None
    assert transaction._id == txn_id

    # Verify the called mock.
    firestore_api.begin_transaction.assert_called_once_with(
        request={"database": client._database_string, "options": None},
        metadata=client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__begin_failure(database):
    from google.cloud.firestore_v1.base_transaction import _CANT_BEGIN

    client = _make_client(database=database)
    transaction = _make_transaction(client)
    transaction._id = b"not-none"

    with pytest.raises(ValueError) as exc_info:
        transaction._begin()

    err_msg = _CANT_BEGIN.format(transaction._id)
    assert exc_info.value.args == (err_msg,)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__rollback(database):
    from google.protobuf import empty_pb2

    from google.cloud.firestore_v1.services.firestore import client as firestore_client

    # Create a minimal fake GAPIC with a dummy result.
    firestore_api = mock.create_autospec(
        firestore_client.FirestoreClient, instance=True
    )
    firestore_api.rollback.return_value = empty_pb2.Empty()

    # Attach the fake GAPIC to a real client.
    client = _make_client(database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a transaction and roll it back.
    transaction = _make_transaction(client)
    txn_id = b"to-be-r\x00lled"
    transaction._id = txn_id
    ret_val = transaction._rollback()
    assert ret_val is None
    assert transaction._id is None

    # Verify the called mock.
    firestore_api.rollback.assert_called_once_with(
        request={"database": client._database_string, "transaction": txn_id},
        metadata=client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__rollback_not_allowed(database):
    from google.cloud.firestore_v1.base_transaction import _CANT_ROLLBACK

    client = _make_client(database=database)
    transaction = _make_transaction(client)
    assert transaction._id is None

    with pytest.raises(ValueError) as exc_info:
        transaction._rollback()

    assert exc_info.value.args == (_CANT_ROLLBACK,)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__rollback_failure(database):
    from google.api_core import exceptions

    from google.cloud.firestore_v1.services.firestore import client as firestore_client

    # Create a minimal fake GAPIC with a dummy failure.
    firestore_api = mock.create_autospec(
        firestore_client.FirestoreClient, instance=True
    )
    exc = exceptions.InternalServerError("Fire during rollback.")
    firestore_api.rollback.side_effect = exc

    # Attach the fake GAPIC to a real client.
    client = _make_client(database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a transaction and roll it back.
    transaction = _make_transaction(client)
    txn_id = b"roll-bad-server"
    transaction._id = txn_id

    with pytest.raises(exceptions.InternalServerError) as exc_info:
        transaction._rollback()

    assert exc_info.value is exc
    assert transaction._id is None
    assert transaction._write_pbs == []

    # Verify the called mock.
    firestore_api.rollback.assert_called_once_with(
        request={"database": client._database_string, "transaction": txn_id},
        metadata=client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__commit(database):
    import datetime

    from google.protobuf.timestamp_pb2 import Timestamp

    from google.cloud.firestore_v1.services.firestore import client as firestore_client
    from google.cloud.firestore_v1.types import firestore, write

    # Create a minimal fake GAPIC with a dummy result.
    firestore_api = mock.create_autospec(
        firestore_client.FirestoreClient, instance=True
    )
    commit_time = Timestamp()
    commit_time.FromDatetime(datetime.datetime.now())
    results = [write.WriteResult(update_time=commit_time)]
    commit_response = firestore.CommitResponse(
        write_results=results, commit_time=commit_time
    )
    firestore_api.commit.return_value = commit_response

    # Attach the fake GAPIC to a real client.
    client = _make_client("phone-joe", database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a transaction with some mutations and call _commit().
    transaction = _make_transaction(client)
    txn_id = b"under-over-thru-woods"
    transaction._id = txn_id
    document = client.document("zap", "galaxy", "ship", "space")
    transaction.set(document, {"apple": 4.5})
    write_pbs = transaction._write_pbs[::]

    write_results = transaction._commit()
    assert write_results == list(commit_response.write_results)
    # Make sure transaction has no more "changes".
    assert transaction._id is None
    assert transaction._write_pbs == []
    # ensure write_results and commit_time were set
    assert transaction.write_results == results
    assert transaction.commit_time.timestamp_pb() == commit_time

    # Verify the mocks.
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": write_pbs,
            "transaction": txn_id,
        },
        metadata=client._rpc_metadata,
    )


def test_transaction__commit_not_allowed():
    from google.cloud.firestore_v1.base_transaction import _CANT_COMMIT

    transaction = _make_transaction(mock.sentinel.client)
    assert transaction._id is None
    with pytest.raises(ValueError) as exc_info:
        transaction._commit()

    assert exc_info.value.args == (_CANT_COMMIT,)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction__commit_failure(database):
    from google.api_core import exceptions

    from google.cloud.firestore_v1.services.firestore import client as firestore_client

    # Create a minimal fake GAPIC with a dummy failure.
    firestore_api = mock.create_autospec(
        firestore_client.FirestoreClient, instance=True
    )
    exc = exceptions.InternalServerError("Fire during commit.")
    firestore_api.commit.side_effect = exc

    # Attach the fake GAPIC to a real client.
    client = _make_client(database=database)
    client._firestore_api_internal = firestore_api

    # Actually make a transaction with some mutations and call _commit().
    transaction = _make_transaction(client)
    txn_id = b"beep-fail-commit"
    transaction._id = txn_id
    transaction.create(client.document("up", "down"), {"water": 1.0})
    transaction.delete(client.document("up", "left"))
    write_pbs = transaction._write_pbs[::]

    with pytest.raises(exceptions.InternalServerError) as exc_info:
        transaction._commit()

    assert exc_info.value is exc
    assert transaction._id == txn_id
    assert transaction._write_pbs == write_pbs

    # Verify the called mock.
    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": write_pbs,
            "transaction": txn_id,
        },
        metadata=client._rpc_metadata,
    )


def _transaction_get_all_helper(retry=None, timeout=None, read_time=None):
    from google.cloud.firestore_v1 import _helpers

    client = mock.Mock(spec=["get_all"])
    transaction = _make_transaction(client)
    ref1, ref2 = mock.Mock(), mock.Mock()
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)
    if read_time is not None:
        kwargs["read_time"] = read_time

    result = transaction.get_all([ref1, ref2], **kwargs)

    client.get_all.assert_called_once_with(
        [ref1, ref2],
        transaction=transaction,
        **kwargs,
    )
    assert result is client.get_all.return_value


def test_transaction_get_all():
    _transaction_get_all_helper()


def test_transaction_get_all_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _transaction_get_all_helper(retry=retry, timeout=timeout)


def test_transaction_get_all_w_read_time():
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    _transaction_get_all_helper(read_time=read_time)


def _transaction_get_w_document_ref_helper(
    retry=None,
    timeout=None,
    explain_options=None,
    read_time=None,
):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.document import DocumentReference

    client = mock.Mock(spec=["get_all"])
    transaction = _make_transaction(client)
    ref = DocumentReference("documents", "doc-id")
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    if explain_options is not None:
        kwargs["explain_options"] = explain_options
    if read_time is not None:
        kwargs["read_time"] = read_time

    result = transaction.get(ref, **kwargs)

    # explain_options should not be in the request even if it's provided.
    kwargs.pop("explain_options", None)

    assert result is client.get_all.return_value
    client.get_all.assert_called_once_with([ref], transaction=transaction, **kwargs)


def test_transaction_get_w_document_ref():
    _transaction_get_w_document_ref_helper()


def test_transaction_get_w_document_ref_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _transaction_get_w_document_ref_helper(retry=retry, timeout=timeout)


def test_transaction_get_w_document_ref_w_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    with pytest.raises(ValueError, match="`ref_or_query` is `AsyncDocumentReference`"):
        _transaction_get_w_document_ref_helper(
            explain_options=ExplainOptions(analyze=True),
        )


def test_transaction_get_w_document_ref_w_read_time():
    _transaction_get_w_document_ref_helper(
        read_time=datetime.datetime.now(tz=datetime.timezone.utc)
    )


def _transaction_get_w_query_helper(
    retry=None,
    timeout=None,
    explain_options=None,
    read_time=None,
):
    from google.cloud.firestore_v1 import _helpers
    from google.cloud.firestore_v1.query import Query
    from google.cloud.firestore_v1.query_profile import (
        ExplainMetrics,
        QueryExplainError,
    )
    from google.cloud.firestore_v1.stream_generator import StreamGenerator

    # Create a minimal fake GAPIC.
    firestore_api = mock.Mock(spec=["run_query"])

    # Attach the fake GAPIC to a real client.
    client = _make_client()
    client._firestore_api_internal = firestore_api

    # Make a **real** collection reference as parent.
    parent = client.collection("dee")

    # Add a dummy response to the minimal fake GAPIC.
    _, expected_prefix = parent._parent_info()
    name = "{}/sleep".format(expected_prefix)
    data = {"snooze": 10}
    if explain_options is not None:
        explain_metrics = {"execution_stats": {"results_returned": 1}}
    else:
        explain_metrics = None
    response_pb = _make_query_response(
        name=name, data=data, explain_metrics=explain_metrics
    )
    firestore_api.run_query.return_value = iter([response_pb])
    kwargs = _helpers.make_retry_timeout_kwargs(retry, timeout)

    # Run the transaction with query.
    transaction = _make_transaction(client)
    txn_id = b"beep-fail-commit"
    transaction._id = txn_id
    query = Query(parent)
    returned_generator = transaction.get(
        query,
        **kwargs,
        explain_options=explain_options,
        read_time=read_time,
    )

    # Verify the response.
    assert isinstance(returned_generator, StreamGenerator)
    results = list(returned_generator)
    assert len(results) == 1
    snapshot = results[0]
    assert snapshot.reference._path == ("dee", "sleep")
    assert snapshot.to_dict() == data

    # Verify explain_metrics.
    if explain_options is None:
        with pytest.raises(QueryExplainError, match="explain_options not set"):
            returned_generator.get_explain_metrics()
    else:
        explain_metrics = returned_generator.get_explain_metrics()
        assert isinstance(explain_metrics, ExplainMetrics)
        assert explain_metrics.execution_stats.results_returned == 1

    # Create expected request body.
    parent_path, _ = parent._parent_info()
    request = {
        "parent": parent_path,
        "structured_query": query._to_protobuf(),
        "transaction": b"beep-fail-commit",
    }
    if explain_options is not None:
        request["explain_options"] = explain_options._to_dict()
    if read_time is not None:
        request["read_time"] = read_time

    # Verify the mock call.
    firestore_api.run_query.assert_called_once_with(
        request=request,
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_transaction_get_w_query():
    _transaction_get_w_query_helper()


def test_transaction_get_w_query_w_retry_timeout():
    from google.api_core.retry import Retry

    retry = Retry(predicate=object())
    timeout = 123.0
    _transaction_get_w_query_helper(retry=retry, timeout=timeout)


def test_transaction_get_w_query_w_explain_options():
    from google.cloud.firestore_v1.query_profile import ExplainOptions

    _transaction_get_w_query_helper(explain_options=ExplainOptions(analyze=True))


def test_transaction_get_w_query_w_read_time():
    read_time = datetime.datetime.now(tz=datetime.timezone.utc)
    _transaction_get_w_query_helper(read_time=read_time)


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transaction_get_failure(database):
    client = _make_client(database=database)
    transaction = _make_transaction(client)
    ref_or_query = object()
    with pytest.raises(ValueError):
        transaction.get(ref_or_query)


def _make__transactional(*args, **kwargs):
    from google.cloud.firestore_v1.transaction import _Transactional

    return _Transactional(*args, **kwargs)


def test__transactional_constructor():
    wrapped = _make__transactional(mock.sentinel.callable_)
    assert wrapped.to_wrap is mock.sentinel.callable_
    assert wrapped.current_id is None
    assert wrapped.retry_id is None


@pytest.mark.parametrize("database", [None, "somedb"])
def test__transactional__pre_commit_success(database):
    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"totes-began"
    transaction = _make_transaction_pb(txn_id, database=database)
    result = wrapped._pre_commit(transaction, "pos", key="word")
    assert result is mock.sentinel.result

    assert transaction._id == txn_id
    assert wrapped.current_id == txn_id
    assert wrapped.retry_id == txn_id

    # Verify mocks.
    to_wrap.assert_called_once_with(transaction, "pos", key="word")
    firestore_api = transaction._client._firestore_api
    firestore_api.begin_transaction.assert_called_once_with(
        request={"database": transaction._client._database_string, "options": None},
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_not_called()
    firestore_api.commit.assert_not_called()


@pytest.mark.parametrize("database", [None, "somedb"])
def test__transactional__pre_commit_retry_id_already_set_success(database):
    from google.cloud.firestore_v1.types import common

    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)
    txn_id1 = b"already-set"
    wrapped.retry_id = txn_id1

    txn_id2 = b"ok-here-too"
    transaction = _make_transaction_pb(txn_id2, database=database)
    result = wrapped._pre_commit(transaction)
    assert result is mock.sentinel.result

    assert transaction._id == txn_id2
    assert wrapped.current_id == txn_id2
    assert wrapped.retry_id == txn_id1

    # Verify mocks.
    to_wrap.assert_called_once_with(transaction)
    firestore_api = transaction._client._firestore_api
    options_ = common.TransactionOptions(
        read_write=common.TransactionOptions.ReadWrite(retry_transaction=txn_id1)
    )
    firestore_api.begin_transaction.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "options": options_,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_not_called()
    firestore_api.commit.assert_not_called()


@pytest.mark.parametrize("database", [None, "somedb"])
def test__transactional___call__success_first_attempt(database):
    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"whole-enchilada"
    transaction = _make_transaction_pb(txn_id, database=database)
    result = wrapped(transaction, "a", b="c")
    assert result is mock.sentinel.result

    assert transaction._id is None
    assert wrapped.current_id == txn_id
    assert wrapped.retry_id == txn_id

    # Verify mocks.
    to_wrap.assert_called_once_with(transaction, "a", b="c")
    firestore_api = transaction._client._firestore_api
    firestore_api.begin_transaction.assert_called_once_with(
        request={"database": transaction._client._database_string, "options": None},
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_not_called()
    firestore_api.commit.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "writes": [],
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test__transactional___call__success_second_attempt(database):
    from google.api_core import exceptions

    from google.cloud.firestore_v1.types import common, firestore, write

    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"whole-enchilada"
    transaction = _make_transaction_pb(txn_id, database=database)

    # Actually force the ``commit`` to fail on first / succeed on second.
    exc = exceptions.Aborted("Contention junction.")
    firestore_api = transaction._client._firestore_api
    firestore_api.commit.side_effect = [
        exc,
        firestore.CommitResponse(write_results=[write.WriteResult()]),
    ]

    # Call the __call__-able ``wrapped``.
    result = wrapped(transaction, "a", b="c")
    assert result is mock.sentinel.result

    assert transaction._id is None
    assert wrapped.current_id == txn_id
    assert wrapped.retry_id == txn_id

    # Verify mocks.
    wrapped_call = mock.call(transaction, "a", b="c")
    assert to_wrap.mock_calls, [wrapped_call == wrapped_call]
    firestore_api = transaction._client._firestore_api
    db_str = transaction._client._database_string
    options_ = common.TransactionOptions(
        read_write=common.TransactionOptions.ReadWrite(retry_transaction=txn_id)
    )
    expected_calls = [
        mock.call(
            request={"database": db_str, "options": None},
            metadata=transaction._client._rpc_metadata,
        ),
        mock.call(
            request={"database": db_str, "options": options_},
            metadata=transaction._client._rpc_metadata,
        ),
    ]
    assert firestore_api.begin_transaction.mock_calls == expected_calls
    firestore_api.rollback.assert_not_called()
    commit_call = mock.call(
        request={"database": db_str, "writes": [], "transaction": txn_id},
        metadata=transaction._client._rpc_metadata,
    )
    assert firestore_api.commit.mock_calls == [commit_call, commit_call]


@pytest.mark.parametrize("database", [None, "somedb"])
@pytest.mark.parametrize("max_attempts", [1, 5])
def test_transactional___call__failure_max_attempts(database, max_attempts):
    """
    rasie retryable error and exhause max_attempts
    """
    from google.api_core import exceptions

    from google.cloud.firestore_v1.transaction import _EXCEED_ATTEMPTS_TEMPLATE
    from google.cloud.firestore_v1.types import common

    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"attempt_exhaustion"
    transaction = _make_transaction_pb(
        txn_id, database=database, max_attempts=max_attempts
    )

    # Actually force the ``commit`` to fail.
    exc = exceptions.Aborted("Contention just once.")
    firestore_api = transaction._client._firestore_api
    firestore_api.commit.side_effect = exc

    # Call the __call__-able ``wrapped``.
    with pytest.raises(ValueError) as exc_info:
        wrapped(transaction, "here", there=1.5)

    err_msg = _EXCEED_ATTEMPTS_TEMPLATE.format(transaction._max_attempts)
    assert exc_info.value.args == (err_msg,)
    # should retain cause exception
    assert exc_info.value.__cause__ == exc

    assert transaction._id is None
    assert wrapped.current_id == txn_id
    assert wrapped.retry_id == txn_id

    # Verify mocks.
    assert to_wrap.call_count == max_attempts
    to_wrap.assert_called_with(transaction, "here", there=1.5)
    assert firestore_api.begin_transaction.call_count == max_attempts
    options_ = common.TransactionOptions(
        read_write=common.TransactionOptions.ReadWrite(retry_transaction=txn_id)
    )
    expected_calls = [
        mock.call(
            request={
                "database": transaction._client._database_string,
                "options": None if i == 0 else options_,
            },
            metadata=transaction._client._rpc_metadata,
        )
        for i in range(max_attempts)
    ]
    assert firestore_api.begin_transaction.call_args_list == expected_calls
    assert firestore_api.commit.call_count == max_attempts
    firestore_api.commit.assert_called_with(
        request={
            "database": transaction._client._database_string,
            "writes": [],
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
@pytest.mark.parametrize("max_attempts", [1, 5])
def test_transactional___call__failure_readonly(database, max_attempts):
    """
    readonly transaction should never retry
    """
    from google.api_core import exceptions

    from google.cloud.firestore_v1.types import common

    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"read_only_fail"
    transaction = _make_transaction_pb(
        txn_id, database=database, max_attempts=max_attempts, read_only=True
    )

    # Actually force the ``commit`` to fail.
    exc = exceptions.Aborted("Contention just once.")
    firestore_api = transaction._client._firestore_api
    firestore_api.commit.side_effect = exc

    # Call the __call__-able ``wrapped``.
    with pytest.raises(exceptions.Aborted) as exc_info:
        wrapped(transaction, "here", there=1.5)

    assert exc_info.value == exc

    assert transaction._id is None
    assert wrapped.current_id == txn_id
    assert wrapped.retry_id == txn_id

    # Verify mocks.
    to_wrap.assert_called_once_with(transaction, "here", there=1.5)
    firestore_api.begin_transaction.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "options": common.TransactionOptions(
                read_only=common.TransactionOptions.ReadOnly()
            ),
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.commit.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "writes": [],
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
@pytest.mark.parametrize("max_attempts", [1, 5])
def test_transactional___call__failure_with_non_retryable(database, max_attempts):
    """
    call fails due to an exception that is not retryable.
    Should rollback raise immediately
    """
    from google.api_core import exceptions

    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"non_retryable"
    transaction = _make_transaction_pb(
        txn_id, database=database, max_attempts=max_attempts
    )

    # Actually force the ``commit`` to fail.
    exc = exceptions.InvalidArgument("non retryable")
    firestore_api = transaction._client._firestore_api
    firestore_api.commit.side_effect = exc

    # Call the __call__-able ``wrapped``.
    with pytest.raises(exceptions.InvalidArgument) as exc_info:
        wrapped(transaction, "here", there=1.5)

    assert exc_info.value == exc

    assert transaction._id is None
    assert wrapped.current_id == txn_id

    # Verify mocks.
    to_wrap.assert_called_once_with(transaction, "here", there=1.5)
    firestore_api.begin_transaction.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "options": None,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.commit.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "writes": [],
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )


@pytest.mark.parametrize("database", [None, "somedb"])
def test_transactional___call__failure_with_rollback_failure(database):
    """
    Test second failure as part of rollback
    should maintain first failure as __context__
    """
    from google.api_core import exceptions

    to_wrap = mock.Mock(return_value=mock.sentinel.result, spec=[])
    wrapped = _make__transactional(to_wrap)

    txn_id = b"non_retryable"
    transaction = _make_transaction_pb(txn_id, database=database, max_attempts=1)

    # Actually force the ``commit`` to fail.
    exc = exceptions.InvalidArgument("first error")
    firestore_api = transaction._client._firestore_api
    firestore_api.commit.side_effect = exc
    # also force a second error on rollback
    rb_exc = exceptions.InternalServerError("second error")
    firestore_api.rollback.side_effect = rb_exc

    # Call the __call__-able ``wrapped``.
    # should raise second error with first error as __context__
    with pytest.raises(exceptions.InternalServerError) as exc_info:
        wrapped(transaction, "here", there=1.5)

    assert exc_info.value == rb_exc
    assert exc_info.value.__context__ == exc

    assert transaction._id is None
    assert wrapped.current_id == txn_id

    # Verify mocks.
    to_wrap.assert_called_once_with(transaction, "here", there=1.5)
    firestore_api.begin_transaction.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "options": None,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.rollback.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )
    firestore_api.commit.assert_called_once_with(
        request={
            "database": transaction._client._database_string,
            "writes": [],
            "transaction": txn_id,
        },
        metadata=transaction._client._rpc_metadata,
    )


def test_transactional_factory():
    from google.cloud.firestore_v1.transaction import _Transactional, transactional

    wrapped = transactional(mock.sentinel.callable_)
    assert isinstance(wrapped, _Transactional)
    assert wrapped.to_wrap is mock.sentinel.callable_


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(project="feral-tom-cat", database=None):
    from google.cloud.firestore_v1.client import Client

    credentials = _make_credentials()
    return Client(project=project, credentials=credentials, database=database)


def _make_transaction_pb(txn_id, database=None, **txn_kwargs):
    from google.protobuf import empty_pb2

    from google.cloud.firestore_v1.services.firestore import client as firestore_client
    from google.cloud.firestore_v1.transaction import Transaction
    from google.cloud.firestore_v1.types import firestore, write

    # Create a fake GAPIC ...
    firestore_api = mock.create_autospec(
        firestore_client.FirestoreClient, instance=True
    )
    # ... with a dummy ``BeginTransactionResponse`` result ...
    begin_response = firestore.BeginTransactionResponse(transaction=txn_id)
    firestore_api.begin_transaction.return_value = begin_response
    # ... and a dummy ``Rollback`` result ...
    firestore_api.rollback.return_value = empty_pb2.Empty()
    # ... and a dummy ``Commit`` result.
    commit_response = firestore.CommitResponse(write_results=[write.WriteResult()])
    firestore_api.commit.return_value = commit_response

    # Attach the fake GAPIC to a real client.
    client = _make_client(database=database)
    client._firestore_api_internal = firestore_api

    return Transaction(client, **txn_kwargs)
