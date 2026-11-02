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

import functools
import glob
import json
import os

import mock
import proto as proto_plus
import pytest
from google.protobuf.timestamp_pb2 import Timestamp

from google.cloud.firestore_v1.types import document, firestore, write
from tests.unit.v1 import conformance_tests


def _load_test_json(filename):
    shortname = os.path.split(filename)[-1]

    with open(filename, "r") as tp_file:
        tp_json = tp_file.read()

    test_file = conformance_tests.TestFile.from_json(tp_json)

    for test_proto in test_file.tests:
        test_proto.description = test_proto.description + " (%s)" % shortname
        yield test_proto


_here = os.path.dirname(__file__)
_glob_expr = "{}/testdata/*.json".format(_here)
_globs = glob.glob(_glob_expr)
ALL_TESTPROTOS = []
for filename in sorted(_globs):
    ALL_TESTPROTOS.extend(_load_test_json(filename))

_CREATE_TESTPROTOS = [
    test_proto for test_proto in ALL_TESTPROTOS if "create" in test_proto
]

_GET_TESTPROTOS = [test_proto for test_proto in ALL_TESTPROTOS if "get" in test_proto]

_SET_TESTPROTOS = [test_proto for test_proto in ALL_TESTPROTOS if "set_" in test_proto]

_UPDATE_TESTPROTOS = [
    test_proto for test_proto in ALL_TESTPROTOS if "update" in test_proto
]

_UPDATE_PATHS_TESTPROTOS = [
    test_proto for test_proto in ALL_TESTPROTOS if "update_paths" in test_proto
]

_DELETE_TESTPROTOS = [
    test_proto for test_proto in ALL_TESTPROTOS if "delete" in test_proto
]

_LISTEN_TESTPROTOS = [
    test_proto for test_proto in ALL_TESTPROTOS if "listen" in test_proto
]

_QUERY_TESTPROTOS = [
    test_proto for test_proto in ALL_TESTPROTOS if "query" in test_proto
]


def _mock_firestore_api():
    firestore_api = mock.Mock(spec=["commit"])
    commit_response = firestore.CommitResponse(write_results=[write.WriteResult()])
    firestore_api.commit.return_value = commit_response
    return firestore_api


def _make_client_document(firestore_api, testcase):
    import google.auth.credentials

    from google.cloud.firestore_v1 import Client
    from google.cloud.firestore_v1.base_client import DEFAULT_DATABASE

    _, project, _, database, _, doc_path = testcase.doc_ref_path.split("/", 5)
    assert database == DEFAULT_DATABASE

    # Attach the fake GAPIC to a real client.
    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    client = Client(project=project, credentials=credentials)
    client._firestore_api_internal = firestore_api
    return client, client.document(doc_path)


def _run_testcase(testcase, call, firestore_api, client):
    if getattr(testcase, "is_error", False):
        # TODO: is there a subclass of Exception we can check for?
        with pytest.raises(Exception):
            call()
    else:
        call()

        wrapped_writes = [
            write.Write.wrap(write_pb) for write_pb in testcase.request.writes
        ]

        expected_request = {
            "database": client._database_string,
            "writes": wrapped_writes,
            "transaction": None,
        }

        firestore_api.commit.assert_called_once_with(
            request=expected_request,
            metadata=client._rpc_metadata,
        )


@pytest.mark.parametrize("test_proto", _CREATE_TESTPROTOS)
def test_create_testprotos(test_proto):
    testcase = test_proto.create
    firestore_api = _mock_firestore_api()
    client, doc = _make_client_document(firestore_api, testcase)
    data = convert_data(json.loads(testcase.json_data))
    call = functools.partial(doc.create, data)
    _run_testcase(testcase, call, firestore_api, client)


@pytest.mark.parametrize("test_proto", _GET_TESTPROTOS)
def test_get_testprotos(test_proto):
    testcase = test_proto.get
    firestore_api = mock.Mock(spec=["batch_get_documents", "_client"])
    response = firestore.BatchGetDocumentsResponse()
    response.read_time = Timestamp(seconds=0, nanos=0)
    response.found = document.Document()
    response.found.fields = {}
    response.found.create_time = Timestamp(seconds=0, nanos=0)
    response.found.update_time = Timestamp(seconds=0, nanos=0)
    firestore_api.batch_get_documents.return_value = iter([response])
    firestore_api._client._database_string = "projects/projectID/databases/(default)"
    client, doc = _make_client_document(firestore_api, testcase)
    response.found.name = doc._document_path

    doc.get()  # No '.textprotos' for errors, field_paths.

    expected_request = {
        "database": firestore_api._client._database_string,
        "documents": [doc._document_path],
        "mask": None,
        "transaction": None,
    }

    firestore_api.batch_get_documents.assert_called_once_with(
        request=expected_request,
        metadata=client._rpc_metadata,
    )


@pytest.mark.parametrize("test_proto", _SET_TESTPROTOS)
def test_set_testprotos(test_proto):
    testcase = test_proto.set_
    firestore_api = _mock_firestore_api()
    client, doc = _make_client_document(firestore_api, testcase)
    data = convert_data(json.loads(testcase.json_data))
    if "option" in testcase:
        merge = convert_set_option(testcase.option)
    else:
        merge = False
    call = functools.partial(doc.set, data, merge=merge)
    _run_testcase(testcase, call, firestore_api, client)


@pytest.mark.parametrize("test_proto", _UPDATE_TESTPROTOS)
def test_update_testprotos(test_proto):
    testcase = test_proto.update
    firestore_api = _mock_firestore_api()
    client, doc = _make_client_document(firestore_api, testcase)
    data = convert_data(json.loads(testcase.json_data))
    if "precondition" in testcase:
        option = convert_precondition(testcase.precondition)
    else:
        option = None
    call = functools.partial(doc.update, data, option)
    _run_testcase(testcase, call, firestore_api, client)


@pytest.mark.skip(reason="Python has no way to call update with a list of field paths.")
@pytest.mark.parametrize("test_proto", _UPDATE_PATHS_TESTPROTOS)
def test_update_paths_testprotos(test_proto):  # pragma: NO COVER
    pass


@pytest.mark.parametrize("test_proto", _DELETE_TESTPROTOS)
def test_delete_testprotos(test_proto):
    testcase = test_proto.delete
    firestore_api = _mock_firestore_api()
    client, doc = _make_client_document(firestore_api, testcase)
    if "precondition" in testcase:
        option = convert_precondition(testcase.precondition)
    else:
        option = None
    call = functools.partial(doc.delete, option)
    _run_testcase(testcase, call, firestore_api, client)


@pytest.mark.parametrize("test_proto", _LISTEN_TESTPROTOS)
def test_listen_testprotos(test_proto):  # pragma: NO COVER
    # test_proto.listen has 'reponses' messages,
    # 'google.firestore_v1.ListenResponse'
    # and then an expected list of 'snapshots' (local 'Snapshot'), containing
    # 'docs' (list of 'google.firestore_v1.Document'),
    # 'changes' (list lof local 'DocChange', and 'read_time' timestamp.
    import google.auth.credentials

    from google.cloud.firestore_v1 import Client, DocumentSnapshot, Watch

    testcase = test_proto.listen
    testname = test_proto.description

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    client = Client(project="project", credentials=credentials)
    # conformance data has db string as this
    db_str = "projects/projectID/databases/(default)"
    client._database_string_internal = db_str
    with mock.patch("google.cloud.firestore_v1.watch.ResumableBidiRpc"):
        with mock.patch("google.cloud.firestore_v1.watch.BackgroundConsumer"):
            # conformance data sets WATCH_TARGET_ID to 1
            with mock.patch("google.cloud.firestore_v1.watch.WATCH_TARGET_ID", 1):
                snapshots = []

                def callback(keys, applied_changes, read_time):
                    snapshots.append((keys, applied_changes, read_time))

                collection = DummyCollection(client=client)
                query = DummyQuery(parent=collection)
                watch = Watch.for_query(query, callback, DocumentSnapshot)

                wrapped_responses = [
                    firestore.ListenResponse.wrap(proto._pb)
                    if isinstance(proto, proto_plus.Message)
                    else firestore.ListenResponse.wrap(proto)
                    for proto in testcase.responses
                ]
                if testcase.is_error:
                    try:
                        for proto in wrapped_responses:
                            watch.on_snapshot(proto)
                    except RuntimeError:
                        # listen-target-add-wrong-id.textpro
                        # listen-target-remove.textpro
                        pass

                else:
                    for proto in wrapped_responses:
                        watch.on_snapshot(proto)

                    assert len(snapshots) == len(testcase.snapshots)
                    for i, (expected_snapshot, actual_snapshot) in enumerate(
                        zip(testcase.snapshots, snapshots)
                    ):
                        expected_changes = expected_snapshot.changes
                        actual_changes = actual_snapshot[1]
                        if len(expected_changes) != len(actual_changes):
                            raise AssertionError(
                                "change length mismatch in %s (snapshot #%s)"
                                % (testname, i)
                            )
                        for y, (expected_change, actual_change) in enumerate(
                            zip(expected_changes, actual_changes)
                        ):
                            expected_change_kind = expected_change.kind
                            actual_change_kind = actual_change.type.value
                            if expected_change_kind != actual_change_kind:
                                raise AssertionError(
                                    "change type mismatch in %s (snapshot #%s, change #%s')"
                                    % (testname, i, y)
                                )


@pytest.mark.parametrize("test_proto", _QUERY_TESTPROTOS)
def test_query_testprotos(test_proto):  # pragma: NO COVER
    testcase = test_proto.query
    if testcase.is_error:
        with pytest.raises(Exception):
            query = parse_query(testcase)
            query._to_protobuf()
    else:
        query = parse_query(testcase)
        found = query._to_protobuf()
        assert found == testcase.query


def convert_data(v):
    # Replace the strings 'ServerTimestamp' and 'Delete' with the corresponding
    # sentinels.
    from google.cloud.firestore_v1 import (
        DELETE_FIELD,
        SERVER_TIMESTAMP,
        ArrayRemove,
        ArrayUnion,
    )

    if v == "ServerTimestamp":
        return SERVER_TIMESTAMP
    elif v == "Delete":
        return DELETE_FIELD
    elif isinstance(v, list):
        if v[0] == "ArrayRemove":
            return ArrayRemove([convert_data(e) for e in v[1:]])
        if v[0] == "ArrayUnion":
            return ArrayUnion([convert_data(e) for e in v[1:]])
        return [convert_data(e) for e in v]
    elif isinstance(v, dict):
        return {k: convert_data(v2) for k, v2 in v.items()}
    elif v == "NaN":
        return float(v)
    else:
        return v


def convert_set_option(option):
    from google.cloud.firestore_v1 import _helpers

    if option.fields:
        return [
            _helpers.FieldPath(*field.field).to_api_repr() for field in option.fields
        ]

    assert option.all_
    return True


def convert_precondition(precond):
    from google.cloud.firestore_v1 import Client

    if isinstance(precond, proto_plus.Message):
        precond_pb = precond._pb
    else:
        precond_pb = precond

    if precond_pb.HasField("exists"):
        return Client.write_option(exists=precond.exists)

    assert precond_pb.HasField("update_time")
    return Client.write_option(last_update_time=precond.update_time)


class DummyRpc(object):  # pragma: NO COVER
    def __init__(
        self,
        listen,
        should_recover,
        should_terminate=None,
        initial_request=None,
        metadata=None,
    ):
        self.listen = listen
        self.initial_request = initial_request
        self.should_recover = should_recover
        self.should_terminate = should_terminate
        self.closed = False
        self.callbacks = []
        self._metadata = metadata

    def add_done_callback(self, callback):
        self.callbacks.append(callback)

    def close(self):
        self.closed = True


class DummyBackgroundConsumer(object):  # pragma: NO COVER
    started = False
    stopped = False
    is_active = True

    def __init__(self, rpc, on_snapshot):
        self._rpc = rpc
        self.on_snapshot = on_snapshot

    def start(self):
        self.started = True

    def stop(self):
        self.stopped = True
        self.is_active = False


class DummyCollection(object):
    def __init__(self, client, parent=None):
        self._client = client
        self._parent = parent

    def _parent_info(self):
        return "{}/documents".format(self._client._database_string), None


class DummyQuery(object):  # pragma: NO COVER
    def __init__(self, parent):
        self._parent = parent
        self._comparator = lambda x, y: 1

    @property
    def _client(self):
        return self._parent._client

    def _to_protobuf(self):
        from google.cloud.firestore_v1.types import query

        query_kwargs = {
            "select": None,
            "from_": None,
            "where": None,
            "order_by": None,
            "start_at": None,
            "end_at": None,
        }
        return query.StructuredQuery(**query_kwargs)


def parse_query(testcase):
    # 'query' testcase contains:
    # - 'coll_path':  collection ref path.
    # - 'clauses':  array of one or more 'Clause' elements
    # - 'query': the actual google.firestore_v1.StructuredQuery message
    #            to be constructed.
    # - 'is_error' (as other testcases).
    #
    # 'Clause' elements are unions of:
    # - 'select':  [field paths]
    # - 'where': (field_path, op, json_value)
    # - 'order_by': (field_path, direction)
    # - 'offset': int
    # - 'limit': int
    # - 'start_at': 'Cursor'
    # - 'start_after': 'Cursor'
    # - 'end_at': 'Cursor'
    # - 'end_before': 'Cursor'
    #
    # 'Cursor' contains either:
    # - 'doc_snapshot': 'DocSnapshot'
    # - 'json_values': [string]
    #
    # 'DocSnapshot' contains:
    # 'path': str
    # 'json_data': str
    from google.auth.credentials import Credentials

    from google.cloud.firestore_v1 import Client, Query

    _directions = {"asc": Query.ASCENDING, "desc": Query.DESCENDING}

    credentials = mock.create_autospec(Credentials)
    client = Client("projectID", credentials)
    path = parse_path(testcase.coll_path)
    collection = client.collection(*path)
    query = collection

    for clause in testcase.clauses:
        if "select" in clause:
            field_paths = [
                ".".join(field_path.field) for field_path in clause.select.fields
            ]
            query = query.select(field_paths)
        elif "where" in clause:
            path = ".".join(clause.where.path.field)
            value = convert_data(json.loads(clause.where.json_value))
            query = query.where(path, clause.where.op, value)
        elif "order_by" in clause:
            path = ".".join(clause.order_by.path.field)
            direction = clause.order_by.direction
            direction = _directions.get(direction, direction)
            query = query.order_by(path, direction=direction)
        elif "offset" in clause:
            query = query.offset(clause.offset)
        elif "limit" in clause:
            query = query.limit(clause.limit)
        elif "start_at" in clause:
            cursor = parse_cursor(clause.start_at, client)
            query = query.start_at(cursor)
        elif "start_after" in clause:
            cursor = parse_cursor(clause.start_after, client)
            query = query.start_after(cursor)
        elif "end_at" in clause:
            cursor = parse_cursor(clause.end_at, client)
            query = query.end_at(cursor)
        elif "end_before" in clause:
            cursor = parse_cursor(clause.end_before, client)
            query = query.end_before(cursor)
        else:  # pragma: NO COVER
            raise ValueError("Unknown query clause: {}".format(clause))

    return query


def parse_path(path):
    _, relative = path.split("documents/")
    return relative.split("/")


def parse_cursor(cursor, client):
    from google.cloud.firestore_v1 import DocumentReference, DocumentSnapshot

    if "doc_snapshot" in cursor:
        path = parse_path(cursor.doc_snapshot.path)
        doc_ref = DocumentReference(*path, client=client)

        return DocumentSnapshot(
            reference=doc_ref,
            data=json.loads(cursor.doc_snapshot.json_data),
            exists=True,
            read_time=None,
            create_time=None,
            update_time=None,
        )

    values = [json.loads(value) for value in cursor.json_values]
    return convert_data(values)
