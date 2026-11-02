# Copyright 2025 Google LLC
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
import email
import http.client
import io
import json

import pytest

from google.cloud.bigquery.table import TableReference

from .helpers import make_connection


PROJECT = "test-project"
TABLE_REF = TableReference.from_string(f"{PROJECT}.test_dataset.test_table")
EXPECTED_CONFIGURATION = {
    "load": {
        "destinationTable": {
            "projectId": PROJECT,
            "datasetId": "test_dataset",
            "tableId": "test_table",
        },
        "sourceFormat": "CSV",
    }
}


@pytest.fixture(autouse=True)
def mock_sleep(monkeypatch):
    sleep = mock.Mock()
    monkeypatch.setattr("time.sleep", sleep)


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_client(*args, **kw):
    from google.cloud.bigquery.client import Client

    kw["credentials"] = _make_credentials()
    kw["project"] = PROJECT
    return Client(*args, **kw)


def _make_file_obj(contents=b"some data"):
    return io.BytesIO(contents)


def _make_response(status_code, content=b"", headers=None):
    response = mock.Mock(spec=["status_code", "content", "request", "headers"])
    response.status_code = status_code
    response.content = content
    response.headers = headers or {}
    response.request = mock.Mock(spec=["headers"])
    return response


def _make_resumable_upload_responses(num_bytes):
    # In a real scenario, the upload URL is returned in a 'Location'
    # header.
    return [
        _make_response(
            http.client.OK,
            headers={"location": "http://test.invalid/upload-id"},
        ),
        _make_response(
            http.client.OK, content=json.dumps({"size": num_bytes}).encode("utf-8")
        ),
    ]


def _make_transport(responses=None):
    import google.auth.transport.requests

    transport = mock.create_autospec(
        google.auth.transport.requests.AuthorizedSession, instance=True
    )
    transport.request.side_effect = responses
    return transport


def _mock_requests_response(status_code, headers, content=b""):
    return mock.Mock(
        content=content,
        headers=headers,
        status_code=status_code,
        spec=["content", "headers", "status_code"],
    )


def _mock_transport(status_code, headers, content=b""):
    fake_transport = mock.Mock(spec=["request"])
    fake_response = _mock_requests_response(status_code, headers, content=content)
    fake_transport.request.return_value = fake_response
    return fake_transport


def _initiate_resumable_upload_helper(num_retries=None, mtls=False):
    from google.resumable_media.requests import ResumableUpload
    from google.cloud.bigquery.client import _DEFAULT_CHUNKSIZE
    from google.cloud.bigquery.client import _GENERIC_CONTENT_TYPE
    from google.cloud.bigquery.client import _get_upload_headers
    from google.cloud.bigquery.job import LoadJob
    from google.cloud.bigquery.job import LoadJobConfig
    from google.cloud.bigquery.job import SourceFormat

    # Create mocks to be checked for doing transport.
    resumable_url = "http://test.invalid?upload_id=hey-you"
    response_headers = {"location": resumable_url}
    fake_transport = _mock_transport(http.client.OK, response_headers)
    client = _make_client(_http=fake_transport)
    conn = client._connection = make_connection()
    if mtls:
        conn.get_api_base_url_for_mtls = mock.Mock(return_value="https://foo.mtls")

    # Create some mock arguments and call the method under test.
    data = b"goodbye gudbi gootbee"
    stream = io.BytesIO(data)
    config = LoadJobConfig()
    config.source_format = SourceFormat.CSV
    job = LoadJob(None, None, TABLE_REF, client, job_config=config)
    metadata = job.to_api_repr()
    upload, transport_out = client._initiate_resumable_upload(
        stream, metadata, num_retries, None
    )

    # Check the returned values.
    assert isinstance(upload, ResumableUpload)

    host_name = "https://foo.mtls" if mtls else "https://bigquery.googleapis.com"
    upload_url = (
        f"{host_name}/upload/bigquery/v2/projects/{PROJECT}/jobs?uploadType=resumable"
    )
    assert upload.upload_url == upload_url
    expected_headers = _get_upload_headers(conn.user_agent)
    assert upload._headers == expected_headers
    assert not upload.finished
    assert upload._chunk_size == _DEFAULT_CHUNKSIZE
    assert upload._stream is stream
    assert upload._total_bytes is None
    assert upload._content_type == _GENERIC_CONTENT_TYPE
    assert upload.resumable_url == resumable_url

    retry_strategy = upload._retry_strategy
    assert retry_strategy.max_sleep == 64.0
    if num_retries is None:
        assert retry_strategy.max_cumulative_retry == 600.0
        assert retry_strategy.max_retries is None
    else:
        assert retry_strategy.max_cumulative_retry is None
        assert retry_strategy.max_retries == num_retries
    assert transport_out is fake_transport
    # Make sure we never read from the stream.
    assert stream.tell() == 0

    # Check the mocks.
    request_headers = expected_headers.copy()
    request_headers["x-upload-content-type"] = _GENERIC_CONTENT_TYPE
    fake_transport.request.assert_called_once_with(
        "POST",
        upload_url,
        data=json.dumps(metadata).encode("utf-8"),
        headers=request_headers,
        timeout=mock.ANY,
    )


def test__initiate_resumable_upload():
    _initiate_resumable_upload_helper()


def test__initiate_resumable_upload_mtls():
    _initiate_resumable_upload_helper(mtls=True)


def test_initiate_resumable_upload_with_retry():
    _initiate_resumable_upload_helper(num_retries=11)


def _do_multipart_upload_success_helper(
    get_boundary, num_retries=None, project=None, mtls=False
):
    from google.cloud.bigquery.client import _get_upload_headers
    from google.cloud.bigquery.job import LoadJob
    from google.cloud.bigquery.job import LoadJobConfig
    from google.cloud.bigquery.job import SourceFormat

    fake_transport = _mock_transport(http.client.OK, {})
    client = _make_client(_http=fake_transport)
    conn = client._connection = make_connection()
    if mtls:
        conn.get_api_base_url_for_mtls = mock.Mock(return_value="https://foo.mtls")

    if project is None:
        project = PROJECT

    # Create some mock arguments.
    data = b"Bzzzz-zap \x00\x01\xf4"
    stream = io.BytesIO(data)
    config = LoadJobConfig()
    config.source_format = SourceFormat.CSV
    job = LoadJob(None, None, TABLE_REF, client, job_config=config)
    metadata = job.to_api_repr()
    size = len(data)

    response = client._do_multipart_upload(
        stream, metadata, size, num_retries, None, project=project
    )

    # Check the mocks and the returned value.
    assert response is fake_transport.request.return_value
    assert stream.tell() == size
    get_boundary.assert_called_once_with()

    host_name = "https://foo.mtls" if mtls else "https://bigquery.googleapis.com"
    upload_url = (
        f"{host_name}/upload/bigquery/v2/projects/{project}/jobs?uploadType=multipart"
    )
    payload = (
        b"--==0==\r\n"
        b"content-type: application/json; charset=UTF-8\r\n\r\n"
        b"%(json_metadata)s"
        b"\r\n"
        b"--==0==\r\n"
        b"content-type: */*\r\n\r\n"
        b"%(data)s"
        b"\r\n"
        b"--==0==--"
    ) % {b"json_metadata": json.dumps(metadata).encode("utf-8"), b"data": data}

    headers = _get_upload_headers(conn.user_agent)
    headers["content-type"] = b'multipart/related; boundary="==0=="'
    fake_transport.request.assert_called_once_with(
        "POST", upload_url, data=payload, headers=headers, timeout=mock.ANY
    )


@mock.patch("google.resumable_media._upload.get_boundary", return_value=b"==0==")
def test__do_multipart_upload(get_boundary):
    _do_multipart_upload_success_helper(get_boundary)


@mock.patch("google.resumable_media._upload.get_boundary", return_value=b"==0==")
def test__do_multipart_upload_mtls(get_boundary):
    _do_multipart_upload_success_helper(get_boundary, mtls=True)


@mock.patch("google.resumable_media._upload.get_boundary", return_value=b"==0==")
def test_do_multipart_upload_with_retry(get_boundary):
    _do_multipart_upload_success_helper(get_boundary, num_retries=8)


@mock.patch("google.resumable_media._upload.get_boundary", return_value=b"==0==")
def test__do_multipart_upload_with_custom_project(get_boundary):
    _do_multipart_upload_success_helper(get_boundary, project="custom-project")


def test__do_resumable_upload():
    file_obj = _make_file_obj()
    file_obj_len = len(file_obj.getvalue())
    transport = _make_transport(_make_resumable_upload_responses(file_obj_len))
    client = _make_client(_http=transport)

    result = client._do_resumable_upload(file_obj, EXPECTED_CONFIGURATION, None, None)

    content = result.content.decode("utf-8")
    assert json.loads(content) == {"size": file_obj_len}

    transport.request.assert_any_call(
        "POST",
        mock.ANY,
        data=json.dumps(EXPECTED_CONFIGURATION).encode("utf-8"),
        headers=mock.ANY,
        timeout=mock.ANY,
    )


def test__do_resumable_upload_custom_project():
    file_obj = _make_file_obj()
    file_obj_len = len(file_obj.getvalue())
    transport = _make_transport(_make_resumable_upload_responses(file_obj_len))
    client = _make_client(_http=transport)

    result = client._do_resumable_upload(
        file_obj,
        EXPECTED_CONFIGURATION,
        None,
        None,
        project="custom-project",
    )

    content = result.content.decode("utf-8")
    assert json.loads(content) == {"size": file_obj_len}

    transport.request.assert_any_call(
        "POST",
        mock.ANY,
        data=json.dumps(EXPECTED_CONFIGURATION).encode("utf-8"),
        headers=mock.ANY,
        timeout=mock.ANY,
    )

    initiation_url = next(
        (
            call[0][1]
            for call in transport.request.call_args_list
            if call[0][0] == "POST" and "uploadType=resumable" in call[0][1]
        ),
        None,
    )
    assert initiation_url is not None
    assert "projects/custom-project" in initiation_url


def test__do_resumable_upload_custom_timeout():
    file_obj = _make_file_obj()
    file_obj_len = len(file_obj.getvalue())
    transport = _make_transport(_make_resumable_upload_responses(file_obj_len))
    client = _make_client(_http=transport)

    client._do_resumable_upload(
        file_obj, EXPECTED_CONFIGURATION, num_retries=0, timeout=3.14
    )

    for call_args in transport.request.call_args_list:
        assert call_args[1].get("timeout") == 3.14


def test__do_multipart_upload_request_body():
    transport = _make_transport([_make_response(http.client.OK)])
    client = _make_client(_http=transport)
    file_obj = _make_file_obj()
    file_obj_len = len(file_obj.getvalue())

    client._do_multipart_upload(
        file_obj, EXPECTED_CONFIGURATION, file_obj_len, None, None
    )

    request_args = transport.request.mock_calls[0][2]
    request_data = request_args["data"].decode("utf-8")
    request_headers = request_args["headers"]

    request_content = email.message_from_string(
        "Content-Type: {}\n{}".format(
            request_headers["content-type"].decode("utf-8"), request_data
        )
    )

    configuration_data = request_content.get_payload(0).get_payload()
    binary_data = request_content.get_payload(1).get_payload()

    assert json.loads(configuration_data) == EXPECTED_CONFIGURATION
    assert binary_data.encode("utf-8") == file_obj.getvalue()


def test__do_multipart_upload_wrong_size():
    client = _make_client()
    file_obj = _make_file_obj()
    file_obj_len = len(file_obj.getvalue())

    with pytest.raises(ValueError):
        client._do_multipart_upload(file_obj, {}, file_obj_len + 1, None, None)


def test_schema_from_json_with_file_path():
    from google.cloud.bigquery.schema import SchemaField

    file_content = """
    [
      {
        "description": "quarter",
        "mode": "REQUIRED",
        "name": "qtr",
        "type": "STRING"
      },
      {
        "description": "sales representative",
        "mode": "NULLABLE",
        "name": "rep",
        "type": "STRING"
      },
      {
        "description": "total sales",
        "mode": "NULLABLE",
        "name": "sales",
        "type": "FLOAT"
      }
    ]"""

    expected = [
        SchemaField("qtr", "STRING", "REQUIRED", description="quarter"),
        SchemaField(
            "rep",
            "STRING",
            "NULLABLE",
            description="sales representative",
        ),
        SchemaField(
            "sales",
            "FLOAT",
            "NULLABLE",
            description="total sales",
        ),
    ]

    client = _make_client()
    mock_file_path = "/mocked/file.json"

    open_patch = mock.patch("builtins.open", new=mock.mock_open(read_data=file_content))

    with open_patch as _mock_file:
        actual = client.schema_from_json(mock_file_path)
        _mock_file.assert_called_once_with(mock_file_path)
        _mock_file.return_value.read.assert_called_once()

    assert expected == actual
