# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
from unittest import mock

import google.api_core.exceptions
import pytest
from google.api_core.gapic_v1 import client_info
from google.auth import credentials

from google.cloud.bigquery_storage_v1 import types

PROJECT = "my-project"
SERVICE_ACCOUNT_PROJECT = "project-from-credentials"


@pytest.fixture()
def mock_transport(monkeypatch):
    from google.cloud.bigquery_storage_v1.services.big_query_read import transports

    transport = mock.create_autospec(
        transports.grpc.BigQueryReadGrpcTransport, instance=True
    )

    transport.create_read_session = mock.Mock(name="fake_create_read_session")
    transport.read_rows = mock.Mock(name="fake_read_rows")
    transports.grpc.BigQueryReadGrpcTransport._prep_wrapped_messages(
        transport, client_info.ClientInfo()
    )

    # _credentials property for TPC support
    transport._credentials = ""

    return transport


@pytest.fixture()
def client_under_test(mock_transport):
    from google.cloud import bigquery_storage

    return bigquery_storage.BigQueryReadClient(transport=mock_transport)


def test_constructor_w_client_info():
    from google.cloud import bigquery_storage
    from google.cloud.bigquery_storage_v1.services import big_query_read

    class MyTransport:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    transport_class_patcher = mock.patch.object(
        big_query_read.BigQueryReadClient,
        "get_transport_class",
        return_value=MyTransport,
    )

    with transport_class_patcher:
        client_under_test = bigquery_storage.BigQueryReadClient(
            client_info=client_info.ClientInfo(
                client_library_version="test-client-version"
            ),
        )

    transport_client_info = client_under_test._transport.kwargs["client_info"]
    user_agent = transport_client_info.to_user_agent()
    assert "test-client-version" in user_agent


def test_create_read_session(mock_transport, client_under_test):
    # validate test assumptions
    assert client_under_test._transport is mock_transport

    rpc_callable = mock.Mock()
    mock_transport._wrapped_methods[mock_transport.create_read_session] = rpc_callable
    table = "projects/{}/datasets/{}/tables/{}".format(
        "data-project-id", "dataset_id", "table_id"
    )

    read_session = types.ReadSession()
    read_session.table = table

    client_under_test.create_read_session(
        parent="projects/other-project", read_session=read_session
    )

    expected_session_arg = types.CreateReadSessionRequest(
        parent="projects/other-project", read_session=read_session
    )
    rpc_callable.assert_called_once_with(
        expected_session_arg, metadata=mock.ANY, retry=mock.ANY, timeout=mock.ANY
    )


def test_create_read_session_retries_serviceunavailable(
    mock_transport, client_under_test
):
    """Regression test for https://github.com/googleapis/python-bigquery-storage/issues/969."""
    # validate test assumptions
    assert client_under_test._transport is mock_transport

    mock_transport.create_read_session.side_effect = [
        google.api_core.exceptions.ServiceUnavailable("connection reset"),
        google.api_core.exceptions.ServiceUnavailable("connection reset"),
        types.ReadSession(),
    ]
    table = "projects/{}/datasets/{}/tables/{}".format(
        "data-project-id", "dataset_id", "table_id"
    )
    read_session = types.ReadSession()
    read_session.table = table

    # with pytest.raises(google.api_core.exceptions.ServiceUnavailable):
    client_under_test.create_read_session(
        parent="projects/other-project", read_session=read_session
    )

    expected_session_arg = types.CreateReadSessionRequest(
        parent="projects/other-project", read_session=read_session
    )
    expected_call = mock.call(expected_session_arg, metadata=mock.ANY, timeout=mock.ANY)
    mock_transport.create_read_session.assert_has_calls(
        [
            expected_call,
            expected_call,
            expected_call,
        ]
    )


def test_read_rows(mock_transport, client_under_test):
    stream_name = "teststream"
    offset = 0

    client_under_test.read_rows(stream_name)

    expected_request = types.ReadRowsRequest(read_stream=stream_name, offset=offset)
    mock_transport.create_read_session.read_rows(
        expected_request, metadata=mock.ANY, timeout=mock.ANY
    )


def test_read_rows_with_arrow_serialization_options(mock_transport, client_under_test):
    rpc_callable = mock.Mock()
    mock_transport._wrapped_methods[mock_transport.read_rows] = rpc_callable
    options = {"buffer_compression": "LZ4_FRAME"}

    client_under_test.read_rows(
        "teststream", offset=10, arrow_serialization_options=options
    )

    rpc_callable.assert_called_once_with(
        types.ReadRowsRequest(
            read_stream="teststream", offset=10, arrow_serialization_options=options
        ),
        metadata=mock.ANY,
        retry=mock.ANY,
        timeout=mock.ANY,
    )


def test_read_rows_reconnect_resends_arrow_serialization_options(
    mock_transport, client_under_test
):
    def first_stream():
        yield types.ReadRowsResponse(row_count=5)
        raise google.api_core.exceptions.ServiceUnavailable("transient disconnect")

    rpc_callable = mock.Mock(
        side_effect=[first_stream(), iter([types.ReadRowsResponse(row_count=3)])]
    )
    mock_transport._wrapped_methods[mock_transport.read_rows] = rpc_callable
    options = {"buffer_compression": "ZSTD"}

    stream = client_under_test.read_rows(
        "teststream", offset=10, arrow_serialization_options=options
    )

    assert [m.row_count for m in stream] == [5, 3]
    assert rpc_callable.call_args_list == [
        mock.call(
            types.ReadRowsRequest(
                read_stream="teststream",
                offset=offset,
                arrow_serialization_options=options,
            ),
            metadata=mock.ANY,
            retry=mock.ANY,
            timeout=mock.ANY,
        )
        for offset in (10, 15)
    ]


@pytest.mark.parametrize(
    "module_under_test",
    ["google.cloud.bigquery_storage_v1", "google.cloud.bigquery_storage_v1beta2"],
)
def test_init_default_client_info(module_under_test):
    mut = importlib.import_module(module_under_test)
    creds = mock.Mock(spec=credentials.Credentials)
    expected_client_info = f"gccl/{mut.__version__}"

    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as mock_wrap:
        mut.BigQueryWriteClient(credentials=creds)

        assert mock_wrap.call_count > 0
        for call in mock_wrap.call_args_list:
            client_info = call.kwargs.get("client_info")
            assert client_info is not None
            assert expected_client_info in client_info.to_user_agent()


_KEEPALIVE_OPTIONS = [
    ("grpc.keepalive_time_ms", 60 * 1000),
    ("grpc.keepalive_timeout_ms", 60 * 1000),
]


@pytest.mark.parametrize("transport", [None, "grpc"])
def test_constructor_default_transport_sends_keepalive(transport):
    from google.cloud import bigquery_storage

    kwargs = {} if transport is None else {"transport": transport}
    with mock.patch(
        "google.api_core.grpc_helpers.create_channel", autospec=True
    ) as create_channel:
        client = bigquery_storage.BigQueryReadClient(
            credentials=credentials.AnonymousCredentials(), **kwargs
        )

    create_channel.assert_called_once()
    options = create_channel.call_args.kwargs["options"]
    for option in _KEEPALIVE_OPTIONS:
        assert option in options
    # The transport's own channel options are kept.
    assert ("grpc.max_receive_message_length", -1) in options
    assert client._transport.grpc_channel is create_channel.return_value


def test_constructor_keeps_given_transport(mock_transport):
    from google.cloud import bigquery_storage

    client = bigquery_storage.BigQueryReadClient(transport=mock_transport)

    assert client._transport is mock_transport


def test_constructor_keeps_given_transport_callable(mock_transport):
    from google.cloud import bigquery_storage

    create_transport = mock.Mock(return_value=mock_transport)
    client = bigquery_storage.BigQueryReadClient(
        credentials=credentials.AnonymousCredentials(), transport=create_transport
    )

    create_transport.assert_called_once()
    assert client._transport is mock_transport
