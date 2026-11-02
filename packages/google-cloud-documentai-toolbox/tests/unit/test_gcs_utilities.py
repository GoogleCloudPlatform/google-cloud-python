# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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

import pytest

from google.cloud import storage
from google.cloud.documentai_toolbox import gcs_utilities

test_bucket = "test-directory"
test_prefix = "documentai/input"


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_get_bytes(mock_storage):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_ds_store = mock.Mock(name=[])
    mock_ds_store.name = "DS_Store"

    mock_blob1 = mock.Mock(name=[])
    mock_blob1.name = "gs://test-directory/1/test-annotations.json"
    mock_blob1.download_as_bytes.return_value = (
        "gs://test-directory/1/test-annotations.json"
    )

    mock_blob2 = mock.Mock(name=[])
    mock_blob2.name = "gs://test-directory/1/test-config.json"
    mock_blob2.download_as_bytes.return_value = "gs://test-directory/1/test-config.json"

    mock_blob3 = mock.Mock(name=[])
    mock_blob3.name = "gs://test-directory/1/test.pdf"
    mock_blob3.download_as_bytes.return_value = "gs://test-directory/1/test.pdf"

    client.list_blobs.return_value = [mock_ds_store, mock_blob1, mock_blob2, mock_blob3]

    actual = gcs_utilities.get_bytes(
        gcs_bucket_name="bucket",
        gcs_prefix="prefix",
    )

    assert actual == [
        "gs://test-directory/1/test-annotations.json",
        "gs://test-directory/1/test-config.json",
    ]


def test_split_gcs_uri_with_valid_format():
    gcs_uri = "gs://test-bucket/test-directory/1/"
    bucket, prefix = gcs_utilities.split_gcs_uri(gcs_uri)

    assert bucket == "test-bucket"
    assert prefix == "test-directory/1/"


def test_split_gcs_uri_with_invalid_format():
    with pytest.raises(
        ValueError,
        match="gcs_uri must follow format 'gs://{bucket_name}/{gcs_prefix}'.",
    ):
        gcs_uri = "test-bucket/test-directory/1/"
        gcs_utilities.split_gcs_uri(gcs_uri)


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_list_gcs_document_tree_with_one_folder(mock_storage):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/1/test_shard1.json",
            bucket="gs://test-directory/1",
        ),
        storage.Blob(
            name="gs://test-directory/1/test_shard2.json",
            bucket="gs://test-directory/1",
        ),
        storage.Blob(
            name="gs://test-directory/1/test_shard3.json",
            bucket="gs://test-directory/1",
        ),
    ]

    client.list_blobs.return_value = blobs

    doc_list = gcs_utilities.list_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="/"
    )

    mock_storage.Client.assert_called_once()

    assert "gs://test-directory/1" in list(doc_list.keys())


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_list_gcs_document_tree_with_3_documents(mock_storage, capfd):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard1.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard2.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard3.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
    ]

    client.list_blobs.return_value = blobs

    doc_list = gcs_utilities.list_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/1/"
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()

    assert "gs://test-directory/documentai/output/123456789/1" in list(doc_list.keys())


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_list_gcs_document_tree_with_more_than_5_document(mock_storage, capfd):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard1.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard2.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard3.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard4.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard5.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard6.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
    ]
    client.list_blobs.return_value = blobs

    doc_list = gcs_utilities.list_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/1/"
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()

    assert "gs://test-directory/documentai/output/123456789/1" in list(doc_list.keys())


def test_list_gcs_document_tree_with_gcs_uri_contains_file_type():
    with pytest.raises(ValueError, match="gcs_prefix cannot contain file types"):
        gcs_utilities.list_gcs_document_tree(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/1/test_file.json",
        )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_print_gcs_document_tree_with_one_folder(mock_storage, capfd):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/1/test_shard1.json",
            bucket="gs://test-directory/1",
        ),
        storage.Blob(
            name="gs://test-directory/1/test_shard2.json",
            bucket="gs://test-directory/1",
        ),
        storage.Blob(
            name="gs://test-directory/1/test_shard3.json",
            bucket="gs://test-directory/1",
        ),
    ]

    client.list_blobs.return_value = blobs

    gcs_utilities.print_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="/"
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert (
        out
        == """gs://test-directory/1
├──test_shard1.json
├──test_shard2.json
└──test_shard3.json\n\n"""
    )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_print_gcs_document_tree_with_3_documents(mock_storage, capfd):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard1.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard2.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard3.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
    ]

    client.list_blobs.return_value = blobs

    gcs_utilities.print_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/1/"
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert (
        out
        == """gs://test-directory/documentai/output/123456789/1
├──test_shard1.json
├──test_shard2.json
└──test_shard3.json\n\n"""
    )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_print_gcs_document_tree_with_more_than_5_document(mock_storage, capfd):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard1.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard2.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard3.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard4.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard5.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard6.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
    ]
    client.list_blobs.return_value = blobs

    gcs_utilities.print_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/1/"
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert (
        out
        == """gs://test-directory/documentai/output/123456789/1
├──test_shard1.json
├──test_shard2.json
├──test_shard3.json
├──test_shard4.json
├──test_shard5.json
│  ....
└──test_shard6.json\n\n"""
    )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_print_gcs_document_tree_with_multiple_directories(mock_storage, capfd):
    client = mock_storage.Client.return_value

    mock_bucket = mock.Mock()

    client.Bucket.return_value = mock_bucket

    blobs = [
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/0/test_shard1.json",
            bucket="gs://test-directory/documentai/output/123456789/0",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/0/test_shard2.json",
            bucket="gs://test-directory/documentai/output/123456789/0",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard3.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard4.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard5.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
        storage.Blob(
            name="gs://test-directory/documentai/output/123456789/1/test_shard6.json",
            bucket="gs://test-directory/documentai/output/123456789/1",
        ),
    ]
    client.list_blobs.return_value = blobs

    gcs_utilities.print_gcs_document_tree(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/"
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert (
        out
        == """gs://test-directory/documentai/output/123456789/0
├──test_shard1.json
└──test_shard2.json

gs://test-directory/documentai/output/123456789/1
├──test_shard3.json
├──test_shard4.json
├──test_shard5.json
└──test_shard6.json\n\n"""
    )


def test_print_gcs_document_tree_with_gcs_uri_contains_file_type():
    with pytest.raises(ValueError, match="gcs_prefix cannot contain file types"):
        gcs_utilities.print_gcs_document_tree(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/1/test_file.json",
        )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_create_batches_with_empty_directory(mock_storage, capfd):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blob = mock.Mock(name="test_directory/", content_type="", size=0)
    mock_blob.name.endswith.return_value = True

    client.list_blobs.return_value = [mock_blob]

    actual = gcs_utilities.create_batches(
        gcs_bucket_name=test_bucket, gcs_prefix=test_prefix
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert out == ""
    assert len(actual) == 0


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_create_batches_with_3_documents(mock_storage, capfd):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blobs = []
    for i in range(3):
        mock_blob = mock.Mock(
            name=f"test_file{i}.pdf", content_type="application/pdf", size=1024
        )
        mock_blob.name.endswith.return_value = False
        mock_blobs.append(mock_blob)
    client.list_blobs.return_value = mock_blobs

    actual = gcs_utilities.create_batches(
        gcs_bucket_name=test_bucket, gcs_prefix=test_prefix
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert out == ""
    assert len(actual) == 1
    assert len(actual[0].gcs_documents.documents) == 3


def test_create_batches_with_invalid_batch_size():
    with pytest.raises(
        ValueError,
        match="Batch size must be less than 1000. You provided 1001.",
    ):
        gcs_utilities.create_batches(
            gcs_bucket_name=test_bucket, gcs_prefix=test_prefix, batch_size=1001
        )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_create_batches_with_large_folder(mock_storage, capfd):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blobs = []
    for i in range(96):
        mock_blob = mock.Mock(
            name=f"test_file{i}.pdf", content_type="application/pdf", size=1024
        )
        mock_blob.name.endswith.return_value = False
        mock_blobs.append(mock_blob)
    client.list_blobs.return_value = mock_blobs

    actual = gcs_utilities.create_batches(
        gcs_bucket_name=test_bucket, gcs_prefix=test_prefix, batch_size=50
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert out == ""
    assert len(actual) == 2
    assert len(actual[0].gcs_documents.documents) == 50
    assert len(actual[1].gcs_documents.documents) == 46


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_create_batches_with_invalid_file_type(mock_storage, capfd):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blob = mock.Mock(
        name="test_file.json", content_type="application/json", size=1024
    )
    mock_blob.name.endswith.return_value = False
    client.list_blobs.return_value = [mock_blob]

    actual = gcs_utilities.create_batches(
        gcs_bucket_name=test_bucket, gcs_prefix=test_prefix
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert "Invalid Mime Type" in out
    assert not actual


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_create_batches_with_large_file(mock_storage, capfd):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blob = mock.Mock(
        name="test_file.pdf", content_type="application/pdf", size=2073741824
    )
    mock_blob.name.endswith.return_value = False
    client.list_blobs.return_value = [mock_blob]

    actual = gcs_utilities.create_batches(
        gcs_bucket_name=test_bucket, gcs_prefix=test_prefix
    )

    mock_storage.Client.assert_called_once()

    out, err = capfd.readouterr()
    assert "File size must be less than" in out
    assert not actual


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_upload_file(mock_storage):
    client = mock_storage.Client.return_value

    gcs_utilities.upload_file(
        gcs_output_directory="gs://bucket/prefix",
        file_name="file.json",
        file_content="file",
    )
    client.bucket.return_value.blob.return_value.upload_from_string.assert_called_with(
        data="file", content_type="application/json"
    )


def test_upload_file_with_format_error():
    with pytest.raises(
        ValueError,
        match="gcs_uri must follow format 'gs://{bucket_name}/{gcs_prefix}'.",
    ):
        gcs_utilities.upload_file(
            gcs_output_directory="output/path",
            file_name="document_1.json",
            file_content="Document",
        )


def test_upload_file_with_file_error():
    with pytest.raises(ValueError, match="gcs_prefix cannot contain file types"):
        gcs_utilities.upload_file(
            gcs_output_directory="gs://output/path.json",
            file_name="document_1.json",
            file_content="Document",
        )


def test_get_blobs_with_no_input():
    with pytest.raises(
        ValueError,
        match="You must provide either `gcs_uri` or both `gcs_bucket_name` and `gcs_prefix`.",
    ):
        gcs_utilities.get_blobs()


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_get_blobs_with_gcs_uri(mock_storage):
    client = mock_storage.Client.return_value
    gcs_uri = "gs://test-bucket/test-directory/1/"

    gcs_utilities.get_blobs(gcs_uri=gcs_uri)

    mock_storage.Client.assert_called_once()
    client.list_blobs.assert_called_once_with("test-bucket", prefix="test-directory/1/")


def test_get_blobs_with_file_type_error():
    with pytest.raises(ValueError, match="gcs_prefix cannot contain file types"):
        gcs_utilities.get_blobs(gcs_bucket_name="test-bucket", gcs_prefix="test.json")


def test_get_blob_invalid_uri():
    with pytest.raises(ValueError, match="gcs_uri must link to a single file."):
        gcs_utilities.get_blob("gs://test-bucket/prefix/")


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_get_blob_from_uri(mock_storage):
    gcs_uri = "gs://test-bucket/test.json"

    # Mock storage.Blob.from_uri to exist
    mock_storage.Blob.from_uri.return_value = mock.Mock(spec=storage.blob.Blob)

    gcs_utilities.get_blob(gcs_uri=gcs_uri)

    mock_storage.Blob.from_uri.assert_called_once()


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_get_blob_from_string(mock_storage):
    gcs_uri = "gs://test-bucket/test.json"

    # Mock storage.Blob to NOT have from_uri
    del mock_storage.Blob.from_uri

    mock_storage.Blob.from_string.return_value = mock.Mock(spec=storage.blob.Blob)

    gcs_utilities.get_blob(gcs_uri=gcs_uri)

    mock_storage.Blob.from_string.assert_called_once()
