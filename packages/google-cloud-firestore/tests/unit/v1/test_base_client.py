# Copyright 2020 Google LLC All rights reserved.
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

import grpc
import mock
import pytest

PROJECT = "my-prahjekt"


def _make_base_client(*args, **kwargs):
    from google.cloud.firestore_v1.base_client import BaseClient

    return BaseClient(*args, **kwargs)


def _make_default_base_client():
    credentials = _make_credentials()
    return _make_base_client(project=PROJECT, credentials=credentials)


def test_baseclient_constructor_with_emulator_host_defaults():
    from google.auth.credentials import AnonymousCredentials

    from google.cloud.firestore_v1.base_client import (
        _DEFAULT_EMULATOR_PROJECT,
        _FIRESTORE_EMULATOR_HOST,
    )

    emulator_host = "localhost:8081"

    with mock.patch("os.environ", {_FIRESTORE_EMULATOR_HOST: emulator_host}):
        client = _make_base_client()

    assert client._emulator_host == emulator_host
    assert isinstance(client._credentials, AnonymousCredentials)
    assert client.project == _DEFAULT_EMULATOR_PROJECT


def test_baseclient_constructor_with_emulator_host_w_project():
    from google.auth.credentials import AnonymousCredentials

    from google.cloud.firestore_v1.base_client import _FIRESTORE_EMULATOR_HOST

    emulator_host = "localhost:8081"

    with mock.patch("os.environ", {_FIRESTORE_EMULATOR_HOST: emulator_host}):
        client = _make_base_client(project=PROJECT)

    assert client._emulator_host == emulator_host
    assert isinstance(client._credentials, AnonymousCredentials)


def test_baseclient_constructor_with_emulator_host_w_creds():
    from google.cloud.firestore_v1.base_client import (
        _DEFAULT_EMULATOR_PROJECT,
        _FIRESTORE_EMULATOR_HOST,
    )

    credentials = _make_credentials()
    emulator_host = "localhost:8081"

    with mock.patch("os.environ", {_FIRESTORE_EMULATOR_HOST: emulator_host}):
        client = _make_base_client(credentials=credentials)

    assert client._emulator_host == emulator_host
    assert client._credentials is credentials
    assert client.project == _DEFAULT_EMULATOR_PROJECT


def test_baseclient__firestore_api_helper_w_already():
    client = _make_default_base_client()
    internal = client._firestore_api_internal = mock.Mock()

    transport_class = mock.Mock()
    client_class = mock.Mock()
    client_module = mock.Mock()

    api = client._firestore_api_helper(transport_class, client_class, client_module)

    assert api is internal
    transport_class.assert_not_called()
    client_class.assert_not_called()


def test_baseclient__firestore_api_helper_wo_emulator():
    client = _make_default_base_client()
    client_options = client._client_options = mock.Mock()
    target = client._target
    assert client._firestore_api_internal is None

    transport_class = mock.Mock()
    client_class = mock.Mock()
    client_module = mock.Mock()

    api = client._firestore_api_helper(transport_class, client_class, client_module)

    assert api is client_class.return_value
    assert client._firestore_api_internal is api
    channel_options = [
        ("grpc.keepalive_time_ms", 30000),
        ("grpc.max_send_message_length", -1),
        ("grpc.max_receive_message_length", -1),
    ]
    transport_class.create_channel.assert_called_once_with(
        target, credentials=client._credentials, options=channel_options
    )
    transport_class.assert_called_once_with(
        host=target,
        channel=transport_class.create_channel.return_value,
    )
    client_class.assert_called_once_with(
        transport=transport_class.return_value, client_options=client_options
    )


def test_baseclient__firestore_api_helper_async_wo_emulator():
    from google.cloud.firestore_v1.services.firestore.transports.grpc_asyncio import (
        FirestoreGrpcAsyncIOTransport,
    )

    client = _make_default_base_client()
    client_options = client._client_options = mock.Mock()
    target = client._target
    assert client._firestore_api_internal is None

    transport_class = mock.Mock(spec=FirestoreGrpcAsyncIOTransport)
    client_class = mock.Mock()
    client_module = mock.Mock()

    api = client._firestore_api_helper(transport_class, client_class, client_module)

    assert api is client_class.return_value
    assert client._firestore_api_internal is api
    channel_options = [
        ("grpc.keepalive_time_ms", 30000),
        ("grpc.max_send_message_length", -1),
        ("grpc.max_receive_message_length", -1),
    ]
    transport_class.create_channel.assert_called_once_with(
        target, credentials=client._credentials, options=channel_options
    )
    transport_class.assert_called_once_with(
        host=target,
        channel=transport_class.create_channel.return_value,
    )
    client_class.assert_called_once_with(
        transport=transport_class.return_value, client_options=client_options
    )


def test_baseclient__firestore_api_helper_w_emulator():
    emulator_host = "localhost:8081"
    with mock.patch("os.getenv") as getenv:
        getenv.return_value = emulator_host
        client = _make_default_base_client()

    client_options = client._client_options = mock.Mock()
    emulator_channel = client._emulator_channel = mock.Mock()
    assert client._firestore_api_internal is None

    transport_class = mock.Mock(__name__="TestTransport")
    client_class = mock.Mock()
    client_module = mock.Mock()

    api = client._firestore_api_helper(transport_class, client_class, client_module)

    assert api is client_class.return_value
    assert api is client._firestore_api_internal

    emulator_channel.assert_called_once_with(transport_class)
    transport_class.assert_called_once_with(
        host=emulator_host,
        channel=emulator_channel.return_value,
    )
    client_class.assert_called_once_with(
        transport=transport_class.return_value, client_options=client_options
    )


def test_baseclient___database_string_property():
    credentials = _make_credentials()
    database = "cheeeeez"
    client = _make_base_client(
        project=PROJECT, credentials=credentials, database=database
    )
    assert client._database_string_internal is None
    database_string = client._database_string
    expected = "projects/{}/databases/{}".format(client.project, client._database)
    assert database_string == expected
    assert database_string is client._database_string_internal

    # Swap it out with a unique value to verify it is cached.
    client._database_string_internal = mock.sentinel.cached
    assert client._database_string is mock.sentinel.cached


def test_baseclient___rpc_metadata_property():
    credentials = _make_credentials()
    database = "quanta"
    client = _make_base_client(
        project=PROJECT, credentials=credentials, database=database
    )

    assert client._rpc_metadata == [
        ("google-cloud-resource-prefix", client._database_string),
    ]


def test_baseclient__rpc_metadata_property_with_emulator():
    emulator_host = "localhost:8081"
    with mock.patch("os.getenv") as getenv:
        getenv.return_value = emulator_host

        credentials = _make_credentials()
        database = "quanta"
        client = _make_base_client(
            project=PROJECT, credentials=credentials, database=database
        )

    assert client._rpc_metadata == [
        ("google-cloud-resource-prefix", client._database_string),
        ("authorization", "Bearer owner"),
    ]


def test_baseclient__emulator_channel():
    from google.cloud.firestore_v1.services.firestore.transports.grpc import (
        FirestoreGrpcTransport,
    )
    from google.cloud.firestore_v1.services.firestore.transports.grpc_asyncio import (
        FirestoreGrpcAsyncIOTransport,
    )

    emulator_host = "localhost:8081"
    credentials = _make_credentials()
    database = "quanta"
    with mock.patch("os.getenv") as getenv:
        getenv.return_value = emulator_host
        credentials.id_token = None
        client = _make_base_client(
            project=PROJECT, credentials=credentials, database=database
        )

    # checks that a channel is created
    channel = client._emulator_channel(FirestoreGrpcTransport)
    assert isinstance(channel, grpc.Channel)
    channel = client._emulator_channel(FirestoreGrpcAsyncIOTransport)
    assert isinstance(channel, grpc.aio.Channel)

    # Verify that when credentials are provided with an id token it is used
    # for channel construction
    # NOTE: On windows, emulation requires an insecure channel. If this is
    # altered to use a secure channel, start by verifying that it still
    # works as expected on windows.
    with mock.patch("os.getenv") as getenv:
        getenv.return_value = emulator_host
        credentials.id_token = "test"
        client = _make_base_client(
            project=PROJECT, credentials=credentials, database=database
        )
    with mock.patch("grpc.insecure_channel") as insecure_channel:
        channel = client._emulator_channel(FirestoreGrpcTransport)
        insecure_channel.assert_called_once_with(
            emulator_host,
            options=[
                ("Authorization", "Bearer test"),
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    with mock.patch("grpc.aio.insecure_channel") as aio_insecure_channel:
        channel = client._emulator_channel(FirestoreGrpcAsyncIOTransport)
        aio_insecure_channel.assert_called_once_with(
            emulator_host,
            options=[
                ("Authorization", "Bearer test"),
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


def test_baseclient__target_helper_w_emulator_host():
    emulator_host = "localhost:8081"
    credentials = _make_credentials()
    database = "quanta"
    with mock.patch("os.getenv") as getenv:
        getenv.return_value = emulator_host
        credentials.id_token = None
        client = _make_base_client(
            project=PROJECT, credentials=credentials, database=database
        )

    assert client._target_helper(None) == emulator_host


def test_baseclient__target_helper_w_client_options_w_endpoint():
    credentials = _make_credentials()
    endpoint = "https://api.example.com/firestore"
    client_options = {"api_endpoint": endpoint}
    client = _make_base_client(
        project=PROJECT,
        credentials=credentials,
        client_options=client_options,
    )

    assert client._target_helper(None) == endpoint


def test_baseclient__target_helper_w_client_options_wo_endpoint():
    credentials = _make_credentials()
    endpoint = "https://api.example.com/firestore"
    client_options = {}
    client_class = mock.Mock(instance=False, DEFAULT_ENDPOINT=endpoint)
    client = _make_base_client(
        project=PROJECT,
        credentials=credentials,
        client_options=client_options,
    )

    assert client._target_helper(client_class) == endpoint


def test_baseclient__target_helper_wo_client_options():
    credentials = _make_credentials()
    endpoint = "https://api.example.com/firestore"
    client_class = mock.Mock(instance=False, DEFAULT_ENDPOINT=endpoint)
    client = _make_base_client(
        project=PROJECT,
        credentials=credentials,
    )

    assert client._target_helper(client_class) == endpoint


def test_baseclient_field_path():
    from google.cloud.firestore_v1.base_client import BaseClient

    assert BaseClient.field_path("a", "b", "c") == "a.b.c"


def test_baseclient_write_option_last_update():
    from google.protobuf import timestamp_pb2

    from google.cloud.firestore_v1._helpers import LastUpdateOption
    from google.cloud.firestore_v1.base_client import BaseClient

    timestamp = timestamp_pb2.Timestamp(seconds=1299767599, nanos=811111097)

    option = BaseClient.write_option(last_update_time=timestamp)
    assert isinstance(option, LastUpdateOption)
    assert option._last_update_time == timestamp


def test_baseclient_write_option_exists():
    from google.cloud.firestore_v1._helpers import ExistsOption
    from google.cloud.firestore_v1.base_client import BaseClient

    option1 = BaseClient.write_option(exists=False)
    assert isinstance(option1, ExistsOption)
    assert not option1._exists

    option2 = BaseClient.write_option(exists=True)
    assert isinstance(option2, ExistsOption)
    assert option2._exists


def test_baseclient_write_open_neither_arg():
    from google.cloud.firestore_v1.base_client import _BAD_OPTION_ERR, BaseClient

    with pytest.raises(TypeError) as exc_info:
        BaseClient.write_option()

    assert exc_info.value.args == (_BAD_OPTION_ERR,)


def test_baseclient_write_multiple_args():
    from google.cloud.firestore_v1.base_client import _BAD_OPTION_ERR, BaseClient

    with pytest.raises(TypeError) as exc_info:
        BaseClient.write_option(exists=False, last_update_time=mock.sentinel.timestamp)

    assert exc_info.value.args == (_BAD_OPTION_ERR,)


def test_baseclient_write_bad_arg():
    from google.cloud.firestore_v1.base_client import _BAD_OPTION_ERR, BaseClient

    with pytest.raises(TypeError) as exc_info:
        BaseClient.write_option(spinach="popeye")

    extra = "{!r} was provided".format("spinach")
    assert exc_info.value.args == (_BAD_OPTION_ERR, extra)


def test__reference_info():
    from google.cloud.firestore_v1.base_client import _reference_info

    expected_doc_paths = ["/a/b", "/a/b/c/d", "/a/b", "/f/g"]
    documents = [mock.Mock(_document_path=path) for path in expected_doc_paths]

    document_paths, reference_map = _reference_info(documents)

    assert document_paths == expected_doc_paths
    # reference3 over-rides reference1.
    expected_map = {
        path: document
        for path, document in list(zip(expected_doc_paths, documents))[1:]
    }
    assert reference_map == expected_map


def test__get_reference_success():
    from google.cloud.firestore_v1.base_client import _get_reference

    doc_path = "a/b/c"
    reference_map = {doc_path: mock.sentinel.reference}
    assert _get_reference(doc_path, reference_map) is mock.sentinel.reference


def test__get_reference_failure():
    from google.cloud.firestore_v1.base_client import _BAD_DOC_TEMPLATE, _get_reference

    doc_path = "1/888/call-now"
    with pytest.raises(ValueError) as exc_info:
        _get_reference(doc_path, {})

    err_msg = _BAD_DOC_TEMPLATE.format(doc_path)
    assert exc_info.value.args == (err_msg,)


def _dummy_ref_string():
    from google.cloud.firestore_v1.base_client import DEFAULT_DATABASE

    project = "bazzzz"
    collection_id = "fizz"
    document_id = "buzz"
    return "projects/{}/databases/{}/documents/{}/{}".format(
        project, DEFAULT_DATABASE, collection_id, document_id
    )


def test__parse_batch_get_found():
    from google.cloud._helpers import _datetime_to_pb_timestamp

    from google.cloud.firestore_v1.base_client import _parse_batch_get
    from google.cloud.firestore_v1.document import DocumentSnapshot
    from google.cloud.firestore_v1.types import document

    now = datetime.datetime.now(tz=datetime.timezone.utc)
    read_time = _datetime_to_pb_timestamp(now)
    delta = datetime.timedelta(seconds=100)
    update_time = _datetime_to_pb_timestamp(now - delta)
    create_time = _datetime_to_pb_timestamp(now - 2 * delta)

    ref_string = _dummy_ref_string()
    document_pb = document.Document(
        name=ref_string,
        fields={
            "foo": document.Value(double_value=1.5),
            "bar": document.Value(string_value="skillz"),
        },
        create_time=create_time,
        update_time=update_time,
    )
    response_pb = _make_batch_response(found=document_pb, read_time=read_time)

    reference_map = {ref_string: mock.sentinel.reference}
    snapshot = _parse_batch_get(response_pb, reference_map, mock.sentinel.client)
    assert isinstance(snapshot, DocumentSnapshot)
    assert snapshot._reference is mock.sentinel.reference
    assert snapshot._data == {"foo": 1.5, "bar": "skillz"}
    assert snapshot._exists
    assert snapshot.read_time.timestamp_pb() == read_time
    assert snapshot.create_time.timestamp_pb() == create_time
    assert snapshot.update_time.timestamp_pb() == update_time


def test__parse_batch_get_missing():
    from google.cloud.firestore_v1.base_client import _parse_batch_get
    from google.cloud.firestore_v1.document import DocumentReference

    ref_string = _dummy_ref_string()
    response_pb = _make_batch_response(missing=ref_string)
    document = DocumentReference("fizz", "bazz", client=mock.sentinel.client)
    reference_map = {ref_string: document}
    snapshot = _parse_batch_get(response_pb, reference_map, mock.sentinel.client)
    assert not snapshot.exists
    assert snapshot.id == "bazz"
    assert snapshot._data is None


def test__parse_batch_get_unset_result_type():
    from google.cloud.firestore_v1.base_client import _parse_batch_get

    response_pb = _make_batch_response()
    with pytest.raises(ValueError):
        _parse_batch_get(response_pb, {}, mock.sentinel.client)


def test__parse_batch_get_unknown_result_type():
    from google.cloud.firestore_v1.base_client import _parse_batch_get

    response_pb = mock.Mock()
    response_pb._pb.mock_add_spec(spec=["WhichOneof"])
    response_pb._pb.WhichOneof.return_value = "zoob_value"

    with pytest.raises(ValueError):
        _parse_batch_get(response_pb, {}, mock.sentinel.client)

    response_pb._pb.WhichOneof.assert_called_once_with("result")


def test__get_doc_mask_w_none():
    from google.cloud.firestore_v1.base_client import _get_doc_mask

    assert _get_doc_mask(None) is None


def test__get_doc_mask_w_paths():
    from google.cloud.firestore_v1.base_client import _get_doc_mask
    from google.cloud.firestore_v1.types import common

    field_paths = ["a.b", "c"]
    result = _get_doc_mask(field_paths)
    expected = common.DocumentMask(field_paths=field_paths)
    assert result == expected


def _make_credentials():
    import google.oauth2.credentials

    return mock.Mock(spec=google.oauth2.credentials.Credentials)


def _make_batch_response(**kwargs):
    from google.cloud.firestore_v1.types import firestore

    return firestore.BatchGetDocumentsResponse(**kwargs)
