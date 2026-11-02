# Copyright 2014 Google LLC
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

import http.client

import mock
import pytest
import requests

from google.cloud.datastore.helpers import set_database_id_to_request


def test__make_retry_timeout_kwargs_w_empty():
    from google.cloud.datastore._http import _make_retry_timeout_kwargs

    expected = {}
    assert _make_retry_timeout_kwargs(None, None) == expected


def test__make_retry_timeout_kwargs_w_retry():
    from google.cloud.datastore._http import _make_retry_timeout_kwargs

    retry = object()
    expected = {"retry": retry}
    assert _make_retry_timeout_kwargs(retry, None) == expected


def test__make_retry_timeout_kwargs_w_timeout():
    from google.cloud.datastore._http import _make_retry_timeout_kwargs

    timeout = 5.0
    expected = {"timeout": timeout}
    assert _make_retry_timeout_kwargs(None, timeout) == expected


def test__make_retry_timeout_kwargs_w_both():
    from google.cloud.datastore._http import _make_retry_timeout_kwargs

    retry = object()
    timeout = 5.0
    expected = {"retry": retry, "timeout": timeout}
    assert _make_retry_timeout_kwargs(retry, timeout) == expected


def test__make_request_pb_w_empty_dict():
    from google.cloud.datastore._http import _make_request_pb

    request = {}

    foo = _make_request_pb(request, Foo)

    assert isinstance(foo, Foo)
    assert foo.bar is None
    assert foo.baz is None


def test__make_request_pb_w_partial_dict():
    from google.cloud.datastore._http import _make_request_pb

    request = {"bar": "Bar"}

    foo = _make_request_pb(request, Foo)

    assert isinstance(foo, Foo)
    assert foo.bar == "Bar"
    assert foo.baz is None


def test__make_request_pb_w_complete_dict():
    from google.cloud.datastore._http import _make_request_pb

    request = {"bar": "Bar", "baz": "Baz"}

    foo = _make_request_pb(request, Foo)

    assert isinstance(foo, Foo)
    assert foo.bar == "Bar"
    assert foo.baz == "Baz"


def test__make_request_pb_w_instance():
    from google.cloud.datastore._http import _make_request_pb

    passed = Foo()

    foo = _make_request_pb(passed, Foo)

    assert foo is passed


def _request_helper(retry=None, timeout=None, database=None):
    from google.cloud import _http as connection_module
    from google.cloud.datastore._http import _request, _update_headers

    project = "PROJECT"
    method = "METHOD"
    data = b"DATA"
    base_url = "http://api-url"
    user_agent = "USER AGENT"
    client_info = _make_client_info(user_agent)
    response_data = "CONTENT"

    http = _make_requests_session([_make_response(content=response_data)])

    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = _request(
        http, project, method, data, base_url, client_info, database=database, **kwargs
    )
    assert response == response_data

    # Check that the mocks were called as expected.
    expected_url = _build_expected_url(base_url, project, method)
    expected_headers = {
        "Content-Type": "application/x-protobuf",
        "User-Agent": user_agent,
        connection_module.CLIENT_INFO_HEADER: user_agent,
        "x-goog-request-params": f"project_id={project}",
    }
    _update_headers(expected_headers, project, database_id=database)
    if retry is not None:
        retry.assert_called_once_with(http.request)

    kwargs.pop("retry", None)
    http.request.assert_called_once_with(
        method="POST", url=expected_url, headers=expected_headers, data=data, **kwargs
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test__request_defaults(database_id):
    _request_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test__request_w_retry(database_id):
    retry = mock.MagicMock()
    _request_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test__request_w_timeout(database_id):
    timeout = 5.0
    _request_helper(timeout=timeout, database=database_id)


def test__request_failure():
    from google.cloud.exceptions import BadRequest
    from google.rpc import code_pb2, status_pb2

    from google.cloud.datastore._http import _request

    project = "PROJECT"
    method = "METHOD"
    data = "DATA"
    uri = "http://api-url"
    user_agent = "USER AGENT"
    client_info = _make_client_info(user_agent)

    error = status_pb2.Status()
    error.message = "Entity value is indexed."
    error.code = code_pb2.FAILED_PRECONDITION

    session = _make_requests_session(
        [_make_response(http.client.BAD_REQUEST, content=error.SerializeToString())]
    )

    with pytest.raises(BadRequest) as exc:
        _request(session, project, method, data, uri, client_info, None)

    expected_message = "400 Entity value is indexed."
    assert exc.match(expected_message)


def _rpc_helper(retry=None, timeout=None, database=None):
    from google.cloud.datastore._http import _rpc
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    http = object()
    project = "projectOK"
    method = "beginTransaction"
    base_url = "test.invalid"
    client_info = _make_client_info()
    request_pb = datastore_pb2.BeginTransactionRequest(project_id=project)

    response_pb = datastore_pb2.BeginTransactionResponse(transaction=b"7830rmc")

    kwargs = _retry_timeout_kw(retry, timeout)

    patch = mock.patch(
        "google.cloud.datastore._http._request",
        return_value=response_pb._pb.SerializeToString(),
    )
    with patch as mock_request:
        result = _rpc(
            http,
            project,
            method,
            base_url,
            client_info,
            request_pb,
            datastore_pb2.BeginTransactionResponse,
            database,
            **kwargs,
        )

    assert result == response_pb._pb

    mock_request.assert_called_once_with(
        http,
        project,
        method,
        request_pb._pb.SerializeToString(),
        base_url,
        client_info,
        database,
        **kwargs,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test__rpc_defaults(database_id):
    _rpc_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test__rpc_w_retry(database_id):
    retry = mock.MagicMock()
    _rpc_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test__rpc_w_timeout(database_id):
    timeout = 5.0
    _rpc_helper(timeout=timeout, database=database_id)


def test_api_ctor():
    client = object()
    ds_api = _make_http_datastore_api(client)
    assert ds_api.client is client


def _lookup_single_helper(
    read_consistency=None,
    transaction=None,
    empty=True,
    retry=None,
    timeout=None,
    database=None,
):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2

    project = "PROJECT"
    key_pb = _make_key_pb(project)

    options_kw = {}
    if read_consistency is not None:
        options_kw["read_consistency"] = read_consistency
    if transaction is not None:
        options_kw["transaction"] = transaction

    read_options = datastore_pb2.ReadOptions(**options_kw)

    rsp_pb = datastore_pb2.LookupResponse()

    if not empty:
        entity = entity_pb2.Entity()
        entity.key._pb.CopyFrom(key_pb._pb)
        rsp_pb._pb.found.add(entity=entity._pb)

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )
    ds_api = _make_http_datastore_api(client)
    request = {
        "project_id": project,
        "keys": [key_pb],
        "read_options": read_options,
    }
    set_database_id_to_request(request, database)
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.lookup(request=request, **kwargs)

    response == rsp_pb._pb

    if empty:
        assert len(response.found) == 0
    else:
        assert len(response.found) == 1

    assert len(response.missing) == 0
    assert len(response.deferred) == 0

    uri = _build_expected_url(client._base_url, project, "lookup")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.LookupRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )

    if retry is not None:
        retry.assert_called_once_with(http.request)

    assert list(request.keys) == [key_pb._pb]
    assert request.read_options == read_options._pb


def test_api_lookup_single_key_miss():
    _lookup_single_helper()


def test_api_lookup_single_key_miss_w_read_consistency():
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    read_consistency = datastore_pb2.ReadOptions.ReadConsistency.EVENTUAL
    _lookup_single_helper(read_consistency=read_consistency)


def test_api_lookup_single_key_miss_w_transaction():
    transaction = b"TRANSACTION"
    _lookup_single_helper(transaction=transaction)


def test_api_lookup_single_key_hit():
    _lookup_single_helper(empty=False)


def test_api_lookup_single_key_hit_w_retry():
    retry = mock.MagicMock()
    _lookup_single_helper(empty=False, retry=retry)


def test_api_lookup_single_key_hit_w_timeout():
    timeout = 5.0
    _lookup_single_helper(empty=False, timeout=timeout)


def _lookup_multiple_helper(
    found=0, missing=0, deferred=0, retry=None, timeout=None, database=None
):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2

    project = "PROJECT"
    key_pb1 = _make_key_pb(project)
    key_pb2 = _make_key_pb(project, id_=2345)
    keys = [key_pb1, key_pb2]
    read_options = datastore_pb2.ReadOptions()

    rsp_pb = datastore_pb2.LookupResponse()

    found_keys = []
    for i_found in range(found):
        key = keys[i_found]
        found_keys.append(key._pb)
        entity = entity_pb2.Entity()
        entity.key._pb.CopyFrom(key._pb)
        rsp_pb._pb.found.add(entity=entity._pb)

    missing_keys = []
    for i_missing in range(missing):
        key = keys[i_missing]
        missing_keys.append(key._pb)
        entity = entity_pb2.Entity()
        entity.key._pb.CopyFrom(key._pb)
        rsp_pb._pb.missing.add(entity=entity._pb)

    deferred_keys = []
    for i_deferred in range(deferred):
        key = keys[i_deferred]
        deferred_keys.append(key._pb)
        rsp_pb._pb.deferred.append(key._pb)

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )
    ds_api = _make_http_datastore_api(client)
    request = {
        "project_id": project,
        "keys": keys,
        "read_options": read_options,
    }
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.lookup(request=request, **kwargs)

    assert response == rsp_pb._pb

    assert [found.entity.key for found in response.found] == found_keys
    assert [missing.entity.key for missing in response.missing] == missing_keys
    assert list(response.deferred) == deferred_keys

    uri = _build_expected_url(client._base_url, project, "lookup")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.LookupRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )
    assert list(request.keys) == [key_pb1._pb, key_pb2._pb]
    assert request.read_options == read_options._pb


def test_api_lookup_multiple_keys_w_empty_response():
    _lookup_multiple_helper()


def test_api_lookup_multiple_keys_w_retry():
    retry = mock.MagicMock()
    _lookup_multiple_helper(retry=retry)


def test_api_lookup_multiple_keys_w_timeout():
    timeout = 5.0
    _lookup_multiple_helper(timeout=timeout)


def test_api_lookup_multiple_keys_w_found():
    _lookup_multiple_helper(found=2)


def test_api_lookup_multiple_keys_w_missing():
    _lookup_multiple_helper(missing=2)


def test_api_lookup_multiple_keys_w_deferred():
    _lookup_multiple_helper(deferred=2)


def _run_query_helper(
    read_consistency=None,
    transaction=None,
    namespace=None,
    found=0,
    retry=None,
    timeout=None,
    database=None,
):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2
    from google.cloud.datastore_v1.types import query as query_pb2

    project = "PROJECT"
    kind = "Nonesuch"
    query_pb = query_pb2.Query(kind=[query_pb2.KindExpression(name=kind)])

    partition_kw = {"project_id": project}
    if namespace is not None:
        partition_kw["namespace_id"] = namespace

    partition_id = entity_pb2.PartitionId(**partition_kw)

    options_kw = {}
    if read_consistency is not None:
        options_kw["read_consistency"] = read_consistency
    if transaction is not None:
        options_kw["transaction"] = transaction
    read_options = datastore_pb2.ReadOptions(**options_kw)

    cursor = b"\x00"
    batch_kw = {
        "entity_result_type": query_pb2.EntityResult.ResultType.FULL,
        "end_cursor": cursor,
        "more_results": query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS,
    }
    if found:
        batch_kw["entity_results"] = [
            query_pb2.EntityResult(entity=entity_pb2.Entity())
        ] * found
    rsp_pb = datastore_pb2.RunQueryResponse(
        batch=query_pb2.QueryResultBatch(**batch_kw)
    )

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )
    ds_api = _make_http_datastore_api(client)
    request = {
        "project_id": project,
        "partition_id": partition_id,
        "read_options": read_options,
        "query": query_pb,
    }
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.run_query(request=request, **kwargs)

    assert response == rsp_pb._pb

    uri = _build_expected_url(client._base_url, project, "runQuery")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.RunQueryRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )
    assert request.partition_id == partition_id._pb
    assert request.query == query_pb._pb
    assert request.read_options == read_options._pb


def test_api_run_query_simple():
    _run_query_helper()


def test_api_run_query_w_retry():
    retry = mock.MagicMock()
    _run_query_helper(retry=retry)


def test_api_run_query_w_timeout():
    timeout = 5.0
    _run_query_helper(timeout=timeout)


def test_api_run_query_w_read_consistency():
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    read_consistency = datastore_pb2.ReadOptions.ReadConsistency.EVENTUAL
    _run_query_helper(read_consistency=read_consistency)


def test_api_run_query_w_transaction():
    transaction = b"TRANSACTION"
    _run_query_helper(transaction=transaction)


def test_api_run_query_w_namespace_nonempty_result():
    namespace = "NS"
    _run_query_helper(namespace=namespace, found=1)


def _run_aggregation_query_helper(
    transaction=None, retry=None, timeout=None, database=None
):
    from google.cloud.datastore_v1.types import aggregation_result
    from google.cloud.datastore_v1.types import datastore as datastore_pb2
    from google.cloud.datastore_v1.types import entity as entity_pb2
    from google.cloud.datastore_v1.types import query as query_pb2

    project = "PROJECT"
    kind = "Nonesuch"
    query_pb = query_pb2.Query(kind=[query_pb2.KindExpression(name=kind)])

    aggregation_query_pb = query_pb2.AggregationQuery()
    aggregation_query_pb.nested_query = query_pb
    count_aggregation = query_pb2.AggregationQuery.Aggregation()
    count_aggregation.alias = "total"
    aggregation_query_pb.aggregations.append(count_aggregation)
    partition_kw = {"project_id": project}

    partition_id = entity_pb2.PartitionId(**partition_kw)

    options_kw = {}

    if transaction is not None:
        options_kw["transaction"] = transaction
    read_options = datastore_pb2.ReadOptions(**options_kw)

    batch_kw = {
        "more_results": query_pb2.QueryResultBatch.MoreResultsType.NO_MORE_RESULTS,
    }
    rsp_pb = datastore_pb2.RunAggregationQueryResponse(
        batch=aggregation_result.AggregationResultBatch(**batch_kw)
    )

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )
    ds_api = _make_http_datastore_api(client)
    request = {
        "project_id": project,
        "partition_id": partition_id,
        "read_options": read_options,
        "aggregation_query": aggregation_query_pb,
    }
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.run_aggregation_query(request=request, **kwargs)

    assert response == rsp_pb._pb

    uri = _build_expected_url(client._base_url, project, "runAggregationQuery")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.RunAggregationQueryRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )

    assert request.partition_id == partition_id._pb
    assert request.aggregation_query == aggregation_query_pb._pb
    assert request.read_options == read_options._pb


def test_api_run_aggregation_query_simple():
    _run_aggregation_query_helper()


def test_api_run_aggregation_query_w_retry():
    retry = mock.MagicMock()
    _run_aggregation_query_helper(retry=retry)


def test_api_run_aggregation_query_w_timeout():
    timeout = 5.0
    _run_aggregation_query_helper(timeout=timeout)


def test_api_run_aggregation_query_w_transaction():
    transaction = b"TRANSACTION"
    _run_aggregation_query_helper(transaction=transaction)


def _begin_transaction_helper(options=None, retry=None, timeout=None, database=None):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    transaction = b"TRANSACTION"
    rsp_pb = datastore_pb2.BeginTransactionResponse()
    rsp_pb.transaction = transaction

    # Create mock HTTP and client with response.
    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )

    # Make request.
    ds_api = _make_http_datastore_api(client)
    request = {"project_id": project}
    set_database_id_to_request(request, database)
    if options is not None:
        request["transaction_options"] = options

    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.begin_transaction(request=request, **kwargs)

    # Check the result and verify the callers.
    assert response == rsp_pb._pb

    uri = _build_expected_url(client._base_url, project, "beginTransaction")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.BeginTransactionRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_begin_transaction_wo_options(database_id):
    _begin_transaction_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_begin_transaction_w_options(database_id):
    from google.cloud.datastore_v1.types import TransactionOptions

    read_only = TransactionOptions.ReadOnly._meta.pb()
    options = TransactionOptions(read_only=read_only)
    _begin_transaction_helper(options=options, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_begin_transaction_w_retry(database_id):
    retry = mock.MagicMock()
    _begin_transaction_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_begin_transaction_w_timeout(database_id):
    timeout = 5.0
    _begin_transaction_helper(timeout=timeout, database=database_id)


def _commit_helper(transaction=None, retry=None, timeout=None, database=None):
    from google.cloud.datastore.helpers import _new_value_pb
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    key_pb = _make_key_pb(project, database=database)
    rsp_pb = datastore_pb2.CommitResponse()
    req_pb = datastore_pb2.CommitRequest()
    mutation = req_pb._pb.mutations.add()
    insert = mutation.upsert
    insert.key.CopyFrom(key_pb._pb)
    value_pb = _new_value_pb(insert, "foo")
    value_pb.string_value = "Foo"

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )

    rq_class = datastore_pb2.CommitRequest
    ds_api = _make_http_datastore_api(client)

    request = {"project_id": project, "mutations": [mutation]}
    set_database_id_to_request(request, database)
    if transaction is not None:
        request["transaction"] = transaction
        mode = request["mode"] = rq_class.Mode.TRANSACTIONAL
    else:
        mode = request["mode"] = rq_class.Mode.NON_TRANSACTIONAL

    kwargs = _retry_timeout_kw(retry, timeout, http)

    result = ds_api.commit(request=request, **kwargs)

    assert result == rsp_pb._pb

    uri = _build_expected_url(client._base_url, project, "commit")
    request = _verify_protobuf_call(
        http,
        uri,
        rq_class(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )
    assert list(request.mutations) == [mutation]
    assert request.mode == mode

    if transaction is not None:
        assert request.transaction == transaction
    else:
        assert request.transaction == b""


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_commit_wo_transaction(database_id):
    _commit_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_commit_w_transaction(database_id):
    transaction = b"xact"

    _commit_helper(transaction=transaction, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_commit_w_retry(database_id):
    retry = mock.MagicMock()
    _commit_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_commit_w_timeout(database_id):
    timeout = 5.0
    _commit_helper(timeout=timeout, database=database_id)


def _rollback_helper(retry=None, timeout=None, database=None):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    transaction = b"xact"
    rsp_pb = datastore_pb2.RollbackResponse()

    # Create mock HTTP and client with response.
    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )

    # Make request.
    ds_api = _make_http_datastore_api(client)
    request = {"project_id": project, "transaction": transaction}
    set_database_id_to_request(request, database)
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.rollback(request=request, **kwargs)

    # Check the result and verify the callers.
    assert response == rsp_pb._pb

    uri = _build_expected_url(client._base_url, project, "rollback")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.RollbackRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )
    assert request.transaction == transaction


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_rollback_ok(database_id):
    _rollback_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_rollback_w_retry(database_id):
    retry = mock.MagicMock()
    _rollback_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_rollback_w_timeout(database_id):
    timeout = 5.0
    _rollback_helper(timeout=timeout, database=database_id)


def _allocate_ids_helper(count=0, retry=None, timeout=None, database=None):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    before_key_pbs = []
    after_key_pbs = []
    rsp_pb = datastore_pb2.AllocateIdsResponse()

    for i_count in range(count):
        requested = _make_key_pb(project, id_=None, database=database)
        before_key_pbs.append(requested)
        allocated = _make_key_pb(project, id_=i_count, database=database)
        after_key_pbs.append(allocated)
        rsp_pb._pb.keys.add().CopyFrom(allocated._pb)

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )
    ds_api = _make_http_datastore_api(client)

    request = {"project_id": project, "keys": before_key_pbs}
    set_database_id_to_request(request, database)
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.allocate_ids(request=request, **kwargs)

    assert response == rsp_pb._pb
    assert list(response.keys) == [i._pb for i in after_key_pbs]

    uri = _build_expected_url(client._base_url, project, "allocateIds")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.AllocateIdsRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )
    assert len(request.keys) == len(before_key_pbs)
    for key_before, key_after in zip(before_key_pbs, request.keys):
        assert key_before == key_after


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_allocate_ids_empty(database_id):
    _allocate_ids_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_allocate_ids_non_empty(database_id):
    _allocate_ids_helper(count=2, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_allocate_ids_w_retry(database_id):
    retry = mock.MagicMock()
    _allocate_ids_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_allocate_ids_w_timeout(database_id):
    timeout = 5.0
    _allocate_ids_helper(timeout=timeout, database=database_id)


def _reserve_ids_helper(count=0, retry=None, timeout=None, database=None):
    from google.cloud.datastore_v1.types import datastore as datastore_pb2

    project = "PROJECT"
    before_key_pbs = []
    rsp_pb = datastore_pb2.ReserveIdsResponse()

    for i_count in range(count):
        requested = _make_key_pb(project, id_=i_count, database=database)
        before_key_pbs.append(requested)

    http = _make_requests_session(
        [_make_response(content=rsp_pb._pb.SerializeToString())]
    )
    client_info = _make_client_info()
    client = mock.Mock(
        _http=http,
        _base_url="test.invalid",
        _client_info=client_info,
        spec=["_http", "_base_url", "_client_info"],
    )
    ds_api = _make_http_datastore_api(client)

    request = {"project_id": project, "keys": before_key_pbs}
    set_database_id_to_request(request, database)
    kwargs = _retry_timeout_kw(retry, timeout, http)

    response = ds_api.reserve_ids(request=request, **kwargs)

    assert response == rsp_pb._pb

    uri = _build_expected_url(client._base_url, project, "reserveIds")
    request = _verify_protobuf_call(
        http,
        uri,
        datastore_pb2.AllocateIdsRequest(project_id=project),
        retry=retry,
        timeout=timeout,
        project=project,
        database=database,
    )
    assert len(request.keys) == len(before_key_pbs)
    for key_before, key_after in zip(before_key_pbs, request.keys):
        assert key_before == key_after


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_reserve_ids_empty(database_id):
    _reserve_ids_helper(database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_reserve_ids_non_empty(database_id):
    _reserve_ids_helper(count=2, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_reserve_ids_w_retry(database_id):
    retry = mock.MagicMock()
    _reserve_ids_helper(retry=retry, database=database_id)


@pytest.mark.parametrize("database_id", [None, "somedb"])
def test_api_reserve_ids_w_timeout(database_id):
    timeout = 5.0
    _reserve_ids_helper(timeout=timeout, database=database_id)


def test_update_headers_without_database_id():
    from google.cloud.datastore._http import _update_headers

    headers = {}
    project_id = "someproject"
    _update_headers(headers, project_id)
    assert headers["x-goog-request-params"] == f"project_id={project_id}"


def test_update_headers_with_database_id():
    from google.cloud.datastore._http import _update_headers

    headers = {}
    project_id = "someproject"
    database_id = "somedb"
    _update_headers(headers, project_id, database_id=database_id)
    assert (
        headers["x-goog-request-params"]
        == f"project_id={project_id}&database_id={database_id}"
    )


def _make_http_datastore_api(*args, **kwargs):
    from google.cloud.datastore._http import HTTPDatastoreAPI

    return HTTPDatastoreAPI(*args, **kwargs)


def _make_response(status=http.client.OK, content=b"", headers={}):
    response = requests.Response()
    response.status_code = status
    response._content = content
    response.headers = headers
    response.request = requests.Request()
    return response


def _make_requests_session(responses):
    session = mock.create_autospec(requests.Session, instance=True)
    session.request.side_effect = responses
    return session


def _build_expected_url(api_base_url, project, method):
    from google.cloud.datastore._http import API_VERSION

    return "/".join([api_base_url, API_VERSION, "projects", project + ":" + method])


def _make_key_pb(project, id_=1234, database=None):
    from google.cloud.datastore.key import Key

    path_args = ("Kind",)
    if id_ is not None:
        path_args += (id_,)
    return Key(*path_args, project=project, database=database).to_protobuf()


_USER_AGENT = "TESTING USER AGENT"


def _make_client_info(user_agent=_USER_AGENT):
    from google.api_core.client_info import ClientInfo

    client_info = mock.create_autospec(ClientInfo)
    client_info.to_user_agent.return_value = user_agent
    return client_info


def _verify_protobuf_call(
    http, expected_url, pb, retry=None, timeout=None, project=None, database=None
):
    from google.cloud import _http as connection_module
    from google.cloud.datastore._http import _update_headers

    expected_headers = {
        "Content-Type": "application/x-protobuf",
        "User-Agent": _USER_AGENT,
        connection_module.CLIENT_INFO_HEADER: _USER_AGENT,
        "x-goog-request-params": f"project_id={pb.project_id}",
    }
    _update_headers(expected_headers, project, database_id=database)
    if retry is not None:
        retry.assert_called_once_with(http.request)

    if timeout is not None:
        http.request.assert_called_once_with(
            method="POST",
            url=expected_url,
            headers=expected_headers,
            data=mock.ANY,
            timeout=timeout,
        )
    else:
        http.request.assert_called_once_with(
            method="POST", url=expected_url, headers=expected_headers, data=mock.ANY
        )

    data = http.request.mock_calls[0][2]["data"]
    pb._pb.ParseFromString(data)
    return pb


def _retry_timeout_kw(retry, timeout, http=None):
    kwargs = {}

    if retry is not None:
        kwargs["retry"] = retry
        if http is not None:
            retry.return_value = http.request

    if timeout is not None:
        kwargs["timeout"] = timeout

    return kwargs


class Foo:
    def __init__(self, bar=None, baz=None):
        self.bar = bar
        self.baz = baz
