# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

import proto  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore

from google.cloud.firestore_v1.types import common, document, firestore
from google.cloud.firestore_v1.types import query as gcf_query

__protobuf__ = proto.module(
    package="tests.unit.v1",
    manifest={
        "TestFile",
        "Test",
        "GetTest",
        "CreateTest",
        "SetTest",
        "UpdateTest",
        "UpdatePathsTest",
        "DeleteTest",
        "SetOption",
        "QueryTest",
        "Clause",
        "Select",
        "Where",
        "OrderBy",
        "Cursor_",
        "DocSnapshot",
        "FieldPath",
        "ListenTest",
        "Snapshot",
        "DocChange",
    },
)


class TestFile(proto.Message):
    r"""A collection of tests.

    Attributes:
        tests (Sequence[google.cloud.firestore_v1.types.Test]):

    """

    tests = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Test",
    )


class Test(proto.Message):
    r"""A Test describes a single client method call and its expected
    result.

    Attributes:
        description (str):
            short description of the test
        comment (str):
            a comment describing the behavior being
            tested
        get (google.cloud.firestore_v1.types.GetTest):

        create (google.cloud.firestore_v1.types.CreateTest):

        set_ (google.cloud.firestore_v1.types.SetTest):

        update (google.cloud.firestore_v1.types.UpdateTest):

        update_paths (google.cloud.firestore_v1.types.UpdatePathsTest):

        delete (google.cloud.firestore_v1.types.DeleteTest):

        query (google.cloud.firestore_v1.types.QueryTest):

        listen (google.cloud.firestore_v1.types.ListenTest):

    """

    description = proto.Field(proto.STRING, number=1)

    comment = proto.Field(proto.STRING, number=10)

    get = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="test",
        message="GetTest",
    )

    create = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="test",
        message="CreateTest",
    )

    set_ = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="test",
        message="SetTest",
    )

    update = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="test",
        message="UpdateTest",
    )

    update_paths = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="test",
        message="UpdatePathsTest",
    )

    delete = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="test",
        message="DeleteTest",
    )

    query = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="test",
        message="QueryTest",
    )

    listen = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="test",
        message="ListenTest",
    )


class GetTest(proto.Message):
    r"""Call to the DocumentRef.Get method.

    Attributes:
        doc_ref_path (str):
            The path of the doc, e.g.
            "projects/projectID/databases/(default)/documents/C/d".
        request (google.cloud.firestore_v1.types.GetDocumentRequest):
            The request that the call should send to the
            Firestore service.
    """

    doc_ref_path = proto.Field(proto.STRING, number=1)

    request = proto.Field(
        proto.MESSAGE,
        number=2,
        message=firestore.GetDocumentRequest,
    )


class CreateTest(proto.Message):
    r"""Call to DocumentRef.Create.

    Attributes:
        doc_ref_path (str):
            The path of the doc, e.g.
            "projects/projectID/databases/(default)/documents/C/d".
        json_data (str):
            The data passed to Create, as JSON. The
            strings "Delete" and "ServerTimestamp" denote
            the two special sentinel values. Values that
            could be interpreted as integers (i.e. digit
            strings) should be treated as integers.
        request (google.cloud.firestore_v1.types.CommitRequest):
            The request that the call should generate.
        is_error (bool):
            If true, the call should result in an error
            without generating a request. If this is true,
            request should not be set.
    """

    doc_ref_path = proto.Field(proto.STRING, number=1)

    json_data = proto.Field(proto.STRING, number=2)

    request = proto.Field(
        proto.MESSAGE,
        number=3,
        message=firestore.CommitRequest,
    )

    is_error = proto.Field(proto.BOOL, number=4)


class SetTest(proto.Message):
    r"""A call to DocumentRef.Set.

    Attributes:
        doc_ref_path (str):
            path of doc
        option (google.cloud.firestore_v1.types.SetOption):
            option to the Set call, if any
        json_data (str):
            data (see CreateTest.json_data)
        request (google.cloud.firestore_v1.types.CommitRequest):
            expected request
        is_error (bool):
            call signals an error
    """

    doc_ref_path = proto.Field(proto.STRING, number=1)

    option = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SetOption",
    )

    json_data = proto.Field(proto.STRING, number=3)

    request = proto.Field(
        proto.MESSAGE,
        number=4,
        message=firestore.CommitRequest,
    )

    is_error = proto.Field(proto.BOOL, number=5)


class UpdateTest(proto.Message):
    r"""A call to the form of DocumentRef.Update that represents the
    data as a map or dictionary.

    Attributes:
        doc_ref_path (str):
            path of doc
        precondition (google.cloud.firestore_v1.types.Precondition):
            precondition in call, if any
        json_data (str):
            data (see CreateTest.json_data)
        request (google.cloud.firestore_v1.types.CommitRequest):
            expected request
        is_error (bool):
            call signals an error
    """

    doc_ref_path = proto.Field(proto.STRING, number=1)

    precondition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Precondition,
    )

    json_data = proto.Field(proto.STRING, number=3)

    request = proto.Field(
        proto.MESSAGE,
        number=4,
        message=firestore.CommitRequest,
    )

    is_error = proto.Field(proto.BOOL, number=5)


class UpdatePathsTest(proto.Message):
    r"""A call to the form of DocumentRef.Update that represents the
    data as a list of field paths and their values.

    Attributes:
        doc_ref_path (str):
            path of doc
        precondition (google.cloud.firestore_v1.types.Precondition):
            precondition in call, if any
        field_paths (Sequence[google.cloud.firestore_v1.types.FieldPath]):
            parallel sequences: field_paths[i] corresponds to
            json_values[i]
        json_values (Sequence[str]):
            the argument values, as JSON
        request (google.cloud.firestore_v1.types.CommitRequest):
            expected rquest
        is_error (bool):
            call signals an error
    """

    doc_ref_path = proto.Field(proto.STRING, number=1)

    precondition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Precondition,
    )

    field_paths = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="FieldPath",
    )

    json_values = proto.RepeatedField(proto.STRING, number=4)

    request = proto.Field(
        proto.MESSAGE,
        number=5,
        message=firestore.CommitRequest,
    )

    is_error = proto.Field(proto.BOOL, number=6)


class DeleteTest(proto.Message):
    r"""A call to DocmentRef.Delete

    Attributes:
        doc_ref_path (str):
            path of doc
        precondition (google.cloud.firestore_v1.types.Precondition):

        request (google.cloud.firestore_v1.types.CommitRequest):
            expected rquest
        is_error (bool):
            call signals an error
    """

    doc_ref_path = proto.Field(proto.STRING, number=1)

    precondition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Precondition,
    )

    request = proto.Field(
        proto.MESSAGE,
        number=3,
        message=firestore.CommitRequest,
    )

    is_error = proto.Field(proto.BOOL, number=4)


class SetOption(proto.Message):
    r"""An option to the DocumentRef.Set call.

    Attributes:
        all_ (bool):
            if true, merge all fields ("fields" is
            ignored).
        fields (Sequence[google.cloud.firestore_v1.types.FieldPath]):
            field paths for a Merge option
    """

    all_ = proto.Field(proto.BOOL, number=1)

    fields = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FieldPath",
    )


class QueryTest(proto.Message):
    r"""

    Attributes:
        coll_path (str):
            path of collection, e.g.
            "projects/projectID/databases/(default)/documents/C".
        clauses (Sequence[google.cloud.firestore_v1.types.Clause]):

        query (google.cloud.firestore_v1.types.StructuredQuery):

        is_error (bool):

    """

    coll_path = proto.Field(proto.STRING, number=1)

    clauses = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Clause",
    )

    query = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcf_query.StructuredQuery,
    )

    is_error = proto.Field(proto.BOOL, number=4)


class Clause(proto.Message):
    r"""

    Attributes:
        select (google.cloud.firestore_v1.types.Select):

        where (google.cloud.firestore_v1.types.Where):

        order_by (google.cloud.firestore_v1.types.OrderBy):

        offset (int):

        limit (int):

        start_at (google.cloud.firestore_v1.types.Cursor_):

        start_after (google.cloud.firestore_v1.types.Cursor_):

        end_at (google.cloud.firestore_v1.types.Cursor_):

        end_before (google.cloud.firestore_v1.types.Cursor_):

    """

    select = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="clause",
        message="Select",
    )

    where = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="clause",
        message="Where",
    )

    order_by = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="clause",
        message="OrderBy",
    )

    offset = proto.Field(proto.INT32, number=4, oneof="clause")

    limit = proto.Field(proto.INT32, number=5, oneof="clause")

    start_at = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="clause",
        message="Cursor_",
    )

    start_after = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="clause",
        message="Cursor_",
    )

    end_at = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="clause",
        message="Cursor_",
    )

    end_before = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="clause",
        message="Cursor_",
    )


class Select(proto.Message):
    r"""

    Attributes:
        fields (Sequence[google.cloud.firestore_v1.types.FieldPath]):

    """

    fields = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FieldPath",
    )


class Where(proto.Message):
    r"""

    Attributes:
        path (google.cloud.firestore_v1.types.FieldPath):

        op (str):

        json_value (str):

    """

    path = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FieldPath",
    )

    op = proto.Field(proto.STRING, number=2)

    json_value = proto.Field(proto.STRING, number=3)


class OrderBy(proto.Message):
    r"""

    Attributes:
        path (google.cloud.firestore_v1.types.FieldPath):

        direction (str):
            "asc" or "desc".
    """

    path = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FieldPath",
    )

    direction = proto.Field(proto.STRING, number=2)


class Cursor_(proto.Message):
    r"""

    Attributes:
        doc_snapshot (google.cloud.firestore_v1.types.DocSnapshot):
            one of:
        json_values (Sequence[str]):

    """

    doc_snapshot = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DocSnapshot",
    )

    json_values = proto.RepeatedField(proto.STRING, number=2)


class DocSnapshot(proto.Message):
    r"""

    Attributes:
        path (str):

        json_data (str):

    """

    path = proto.Field(proto.STRING, number=1)

    json_data = proto.Field(proto.STRING, number=2)


class FieldPath(proto.Message):
    r"""

    Attributes:
        field (Sequence[str]):

    """

    field = proto.RepeatedField(proto.STRING, number=1)


class ListenTest(proto.Message):
    r"""A test of the Listen streaming RPC (a.k.a. FireStore watch). If the
    sequence of responses is provided to the implementation, it should
    produce the sequence of snapshots. If is_error is true, an error
    should occur after the snapshots.

    The tests assume that the query is
    Collection("projects/projectID/databases/(default)/documents/C").OrderBy("a",
    Ascending)

    The watch target ID used in these tests is 1. Test interpreters
    should either change their client's ID for testing, or change the ID
    in the tests before running them.

    Attributes:
        responses (Sequence[google.cloud.firestore_v1.types.ListenResponse]):

        snapshots (Sequence[google.cloud.firestore_v1.types.Snapshot]):

        is_error (bool):

    """

    responses = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=firestore.ListenResponse,
    )

    snapshots = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Snapshot",
    )

    is_error = proto.Field(proto.BOOL, number=3)


class Snapshot(proto.Message):
    r"""

    Attributes:
        docs (Sequence[google.cloud.firestore_v1.types.Document]):

        changes (Sequence[google.cloud.firestore_v1.types.DocChange]):

        read_time (google.protobuf.timestamp_pb2.Timestamp):

    """

    docs = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=document.Document,
    )

    changes = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="DocChange",
    )

    read_time = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp.Timestamp,
    )


class DocChange(proto.Message):
    r"""

    Attributes:
        kind (google.cloud.firestore_v1.types.DocChange.Kind):

        doc (google.cloud.firestore_v1.types.Document):

        old_index (int):

        new_index (int):

    """

    class Kind(proto.Enum):
        r""""""

        KIND_UNSPECIFIED = 0
        ADDED = 1
        REMOVED = 2
        MODIFIED = 3

    kind = proto.Field(
        proto.ENUM,
        number=1,
        enum=Kind,
    )

    doc = proto.Field(
        proto.MESSAGE,
        number=2,
        message=document.Document,
    )

    old_index = proto.Field(proto.INT32, number=3)

    new_index = proto.Field(proto.INT32, number=4)


__all__ = tuple(sorted(__protobuf__.manifest))
