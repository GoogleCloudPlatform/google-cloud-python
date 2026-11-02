# -*- coding: utf-8 -*-
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

import google.auth.credentials
from google.api_core import gapic_v1

from google.cloud.firestore_v1 import _helpers
from google.cloud.firestore_v1.client import Client
from google.cloud.firestore_v1.document import DocumentReference
from google.cloud.firestore_v1.types import common, document, firestore, write
from google.cloud.firestore_v1.vector import Vector


def _make_commit_response():
    response = mock.create_autospec(firestore.CommitResponse)
    response.write_results = [mock.sentinel.write_result]
    response.commit_time = mock.sentinel.commit_time
    return response


def _make_firestore_api():
    firestore_api = mock.Mock()
    firestore_api.commit.mock_add_spec(spec=["commit"])
    firestore_api.commit.return_value = _make_commit_response()
    return firestore_api


def _make_client(firestore_api):
    client = Client(
        project="dignity",
        credentials=mock.Mock(spec=google.auth.credentials.Credentials),
        database=None,
    )
    client._firestore_api_internal = firestore_api
    return client


def test_compare_vector():
    vector1 = Vector([1.0, 2.0, 3.0])
    vector2 = Vector([1, 2, 3.0])

    assert vector1 == vector2


def test_compare_different_type():
    vector1 = Vector([1.0, 2.0, 3.0])
    vector2 = [1.0, 2.0, 3.0]

    assert vector1 != vector2


def test_vector_get_items():
    vector = Vector([1.0, 2.0, 3.0])

    assert vector[0] == 1.0
    assert vector[1] == 2.0
    assert vector[-1] == 3.0


def test_vector_len():
    vector = Vector([1.0, 2.0, 3.0])

    assert len(vector) == 3


def test_decode_vector_type():
    firestore_api = _make_firestore_api()
    client = _make_client(firestore_api)
    val = _helpers.decode_dict(
        {
            "value": document.Value(
                array_value=document.ArrayValue(
                    values=[
                        document.Value(double_value=1.0),
                        document.Value(double_value=2.0),
                        document.Value(double_value=3.0),
                    ]
                )
            ),
            "__type__": document.Value(string_value="__vector__"),
        },
        client,
    )
    assert isinstance(val, Vector)

    val = _helpers.decode_dict(
        {
            "value": document.Value(
                array_value=document.ArrayValue(
                    values=[
                        document.Value(double_value=1.0),
                        document.Value(double_value=2.0),
                        document.Value(double_value=3.0),
                    ]
                )
            ),
            "__type__": document.Value(string_value="__not_vector__"),
        },
        client,
    )
    assert not (isinstance(val, Vector))


def test_vector():
    vector = Vector([1.0, 2.0, 3.0])
    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = _make_firestore_api()
    client = _make_client(firestore_api)

    # Actually make a document and call create().
    mocked_document = DocumentReference("foo", "twelve", client=client)
    document_data = {"hello": "goodbye", "embedding": vector}
    mocked_document.create(document_data)

    write_pb = write.Write(
        update=document.Document(
            name=mocked_document._document_path,
            fields={
                "hello": document.Value(string_value="goodbye"),
                "embedding": document.Value(
                    map_value=document.MapValue(
                        fields={
                            "value": document.Value(
                                array_value=document.ArrayValue(
                                    values=[
                                        document.Value(double_value=1.0),
                                        document.Value(double_value=2.0),
                                        document.Value(double_value=3.0),
                                    ]
                                )
                            ),
                            "__type__": document.Value(string_value="__vector__"),
                        }
                    )
                ),
            },
        ),
        current_document=common.Precondition(exists=False),
    )

    kwargs = _helpers.make_retry_timeout_kwargs(gapic_v1.method.DEFAULT, None)

    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )


def test_vector_convert_to_double():
    vector = Vector([4, 5, 6])
    # Create a minimal fake GAPIC with a dummy response.
    firestore_api = _make_firestore_api()
    client = _make_client(firestore_api)

    # Actually make a document and call create().
    mocked_document = DocumentReference("foo", "twelve", client=client)
    document_data = {"hello": "goodbye", "embedding": vector}
    mocked_document.create(document_data)

    write_pb = write.Write(
        update=document.Document(
            name=mocked_document._document_path,
            fields={
                "hello": document.Value(string_value="goodbye"),
                "embedding": document.Value(
                    map_value=document.MapValue(
                        fields={
                            "value": document.Value(
                                array_value=document.ArrayValue(
                                    values=[
                                        document.Value(double_value=4.0),
                                        document.Value(double_value=5.0),
                                        document.Value(double_value=6.0),
                                    ]
                                )
                            ),
                            "__type__": document.Value(string_value="__vector__"),
                        }
                    )
                ),
            },
        ),
        current_document=common.Precondition(exists=False),
    )

    kwargs = _helpers.make_retry_timeout_kwargs(gapic_v1.method.DEFAULT, None)

    firestore_api.commit.assert_called_once_with(
        request={
            "database": client._database_string,
            "writes": [write_pb],
            "transaction": None,
        },
        metadata=client._rpc_metadata,
        **kwargs,
    )
