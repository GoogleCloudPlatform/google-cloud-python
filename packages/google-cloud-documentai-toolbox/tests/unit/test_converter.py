# pylint: disable=protected-access
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
#

try:
    from unittest import mock
except ImportError:  # pragma: NO COVER
    import mock

import pytest

from google.cloud import documentai
from google.cloud.documentai_toolbox.converters import converter
from google.cloud.documentai_toolbox.converters.config.block import Block


@mock.patch("google.cloud.documentai_toolbox.converters.converter.documentai")
def test_get_base_ocr(mock_docai):
    mock_client = mock_docai.DocumentProcessorServiceClient.return_value

    mock_client.process_document.return_value.document = "Done"

    actual = converter._get_base_ocr(
        project_id="project_id",
        location="location",
        processor_id="processor_id",
        file_bytes="file",
        mime_type="application/pdf",
    )

    mock_client.process_document.assert_called()
    assert actual == "Done"


def test_get_entity_content_type_3():
    docproto = documentai.Document()
    page = documentai.Document.Page()
    dimensions = documentai.Document.Page.Dimension()
    dimensions.width = 2550
    dimensions.height = 3300
    page.dimension = dimensions
    docproto.pages = [page]
    with open("tests/unit/resources/converters/test_type_3.json", "r") as (f):
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_3.json", "r") as (f):
        config = f.read()

    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )

    actual = converter._get_entity_content(blocks=b, docproto=docproto)

    assert actual[0].type == "BusinessName"
    assert actual[0].mention_text == "normalized 411 I.T. Group"


def test_get_entity_content_type_2():
    docproto = documentai.Document()
    page = documentai.Document.Page()
    dimensions = documentai.Document.Page.Dimension()
    dimensions.width = 2550
    dimensions.height = 3300
    page.dimension = dimensions
    docproto.pages = [page]
    with open("tests/unit/resources/converters/test_type_2.json", "r") as (f):
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_2.json", "r") as (f):
        config = f.read()

    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )

    actual = converter._get_entity_content(blocks=b, docproto=docproto)

    assert actual[0].type == "invoice_id"
    assert actual[0].mention_text == "4748"


def test_get_entity_content_type_1():
    docproto = documentai.Document()
    page = documentai.Document.Page()
    dimensions = documentai.Document.Page.Dimension()
    dimensions.width = 2550
    dimensions.height = 3300
    page.dimension = dimensions
    docproto.pages = [page]
    with open("tests/unit/resources/converters/test_type_1.json", "r") as (f):
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_1.json", "r") as (f):
        config = f.read()

    b = Block.load_blocks_from_schema(
        input_data=invoice, input_config=config, base_docproto=docproto
    )

    actual = converter._get_entity_content(blocks=b, docproto=docproto)

    assert actual[0].type == "BusinessName"
    assert actual[0].mention_text == "411 I.T. Group"


@mock.patch("google.cloud.documentai_toolbox.converters.converter._get_base_ocr")
def test_convert_to_docproto_with_config(mock_ocr):
    docproto = documentai.Document()
    page = documentai.Document.Page()
    dimensions = documentai.Document.Page.Dimension()
    dimensions.width = 2550
    dimensions.height = 3300
    page.dimension = dimensions
    docproto.pages = [page]
    mock_ocr.return_value = docproto

    with open("tests/unit/resources/converters/test_type_3.json", "rb") as (f):
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_3.json", "rb") as (f):
        config = f.read()
    with open("tests/unit/resources/toolbox_invoice_test.pdf", "rb") as (f):
        pdf = f.read()

    actual = converter._convert_to_docproto_with_config(
        name="test_document",
        annotated_bytes=invoice,
        config_bytes=config,
        document_bytes=pdf,
        project_id="project_id",
        processor_id="processor_id",
        location="location",
        wait_time=0,
    )

    assert len(actual.pages) == 1
    assert len(actual.entities) == 1
    assert actual.entities[0].type == "BusinessName"
    assert actual.entities[0].mention_text == "normalized 411 I.T. Group"


@mock.patch("google.cloud.documentai_toolbox.converters.converter._get_base_ocr")
def test_convert_to_docproto_with_config_with_error(mock_ocr, capfd):
    mock_ocr.return_value = None

    with open("tests/unit/resources/converters/test_type_3.json", "rb") as (f):
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_3.json", "rb") as (f):
        config = f.read()
    with open("tests/unit/resources/toolbox_invoice_test.pdf", "rb") as (f):
        pdf = f.read()

    actual = converter._convert_to_docproto_with_config(
        name="test_document",
        annotated_bytes=invoice,
        config_bytes=config,
        document_bytes=pdf,
        project_id="project_id",
        processor_id="processor_id",
        location="location",
        wait_time=1,
    )

    out, err = capfd.readouterr()

    assert actual is None
    assert "Could Not Convert test_document" in out


@mock.patch("google.cloud.documentai_toolbox.converters.converter._get_base_ocr")
def test_convert_to_docproto_with_config_with_error_and_retry(mock_ocr, capfd):
    mock_ocr.return_value = None

    with open("tests/unit/resources/converters/test_type_3.json", "rb") as (f):
        invoice = f.read()
    with open("tests/unit/resources/converters/test_config_type_3.json", "rb") as (f):
        config = f.read()
    with open("tests/unit/resources/toolbox_invoice_test.pdf", "rb") as (f):
        pdf = f.read()

    actual = converter._convert_to_docproto_with_config(
        name="test_document",
        annotated_bytes=invoice,
        config_bytes=config,
        document_bytes=pdf,
        project_id="project_id",
        processor_id="processor_id",
        location="location",
        wait_time=1,
        max_retries=2,
    )

    out, err = capfd.readouterr()

    assert actual is None
    assert "Could Not Convert test_document" in out


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_get_bytes(mock_storage):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_ds_store = mock.Mock(name=[])
    mock_ds_store.name = ".DS_Store"

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

    actual = converter._get_bytes(
        gcs_uri="gs://bucket/prefix",
        annotation_file_prefix="annotations",
        config_file_prefix="config",
    )

    assert actual == (
        "gs://test-directory/1/test-annotations.json",
        "gs://test-directory/1/test.pdf",
        "gs://test-directory/1/test-config.json",
        "prefix",
    )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
def test_get_bytes_with_error(mock_storage):
    with pytest.raises(Exception, match="Fail"):
        client = mock_storage.Client.return_value
        mock_bucket = mock.Mock()
        client.Bucket.return_value = mock_bucket

        mock_blob1 = mock.Mock(name=[])
        mock_blob1.name = "gs://test-directory/1/test-annotations.json"
        mock_blob1.download_as_bytes.side_effect = Exception("Fail")

        client.list_blobs.return_value = [mock_blob1]

        converter._get_bytes(
            gcs_uri="gs://bucket/prefix",
            annotation_file_prefix="annotations",
            config_file_prefix="config",
        )


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._get_bytes",
    return_value="file_bytes",
)
def test_get_files(mock_storage, mock_get_bytes):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_ds_store = mock.Mock(name=[])
    mock_ds_store.name = ".DS_Store"

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

    blob_list = [mock_ds_store, mock_blob1, mock_blob2, mock_blob3]
    actual = converter._get_files(blob_list=blob_list)

    assert actual[0].result() == "file_bytes"


@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._convert_to_docproto_with_config",
)
def test_get_docproto_files(mocked_convert_docproto):
    mock_result = mock.Mock()
    mock_result.result.return_value = [
        "annotated_bytes",
        "document_bytes",
        "config_bytes",
        "document_1",
    ]

    document = documentai.Document()
    entities = [documentai.Document.Entity(type_="test_type", mention_text="test_text")]
    document.entities = entities

    mocked_convert_docproto.return_value = document
    (
        actual_files,
        actual_unique_types,
        actual_did_not_convert,
    ) = converter._get_docproto_files(
        futures_list=[mock_result],
        project_id="project-id",
        processor_id="processor-id",
        location="us",
    )
    assert "test_type" in actual_files["document_1"]
    assert "test_text" in actual_files["document_1"]
    assert "test_type" in actual_unique_types
    mocked_convert_docproto.assert_called_with(
        annotated_bytes="annotated_bytes",
        document_bytes="document_bytes",
        config_bytes="config_bytes",
        project_id="project-id",
        location="us",
        processor_id="processor-id",
        name="document_1",
    )


@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._convert_to_docproto_with_config",
)
def test_get_docproto_files_with_no_docproto(mocked_convert_docproto):
    mock_result = mock.Mock()
    mock_result.result.return_value = [
        "annotated_bytes",
        "document_bytes",
        "config_bytes",
        "document_1",
    ]

    mocked_convert_docproto.return_value = None
    (
        actual_files,
        actual_unique_types,
        actual_did_not_convert,
    ) = converter._get_docproto_files(
        futures_list=[mock_result],
        project_id="project-id",
        processor_id="processor-id",
        location="us",
    )
    assert "document_1" in actual_did_not_convert
    mocked_convert_docproto.assert_called_with(
        annotated_bytes="annotated_bytes",
        document_bytes="document_bytes",
        config_bytes="config_bytes",
        project_id="project-id",
        location="us",
        processor_id="processor-id",
        name="document_1",
    )


@mock.patch(
    "google.cloud.documentai_toolbox.utilities.gcs_utilities.upload_file",
)
def test_upload(mock_upload_file):
    files = {}
    files["document_1"] = "Document"
    converter._upload(files, gcs_output_path="gs://output/")

    mock_upload_file.assert_called_with("gs://output/", "document_1.json", "Document")


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._get_docproto_files",
    return_value=(["file1"], ["test_label"], []),
)
@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._upload",
    return_value="Done",
)
def test_convert_from_config(mock_storage, mock_get_docproto_files, mock_upload, capfd):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blob1 = mock.Mock(name="gs://test-directory/1/test-annotations.json")
    mock_blob1.download_as_bytes.return_value = (
        "gs://test-directory/1/test-annotations.json"
    )

    mock_blob2 = mock.Mock(name="gs://test-directory/1/test-config.json")
    mock_blob2.download_as_bytes.return_value = "gs://test-directory/1/test-config.json"

    mock_blob3 = mock.Mock(name="gs://test-directory/1/test.pdf")
    mock_blob3.download_as_bytes.return_value = "gs://test-directory/1/test.pdf"

    client.list_blobs.return_value = [mock_blob1, mock_blob2, mock_blob3]

    converter.convert_from_config(
        project_id="project-id",
        location="location",
        processor_id="project-id",
        gcs_input_path="gs://test-directory/1",
        gcs_output_path="gs://test-directory/1/output",
    )

    out, err = capfd.readouterr()
    assert "test_label" in out


@mock.patch("google.cloud.documentai_toolbox.utilities.gcs_utilities.storage")
@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._get_docproto_files",
    return_value=(["file1"], ["test_label"], ["document_2"]),
)
@mock.patch(
    "google.cloud.documentai_toolbox.converters.converter._upload",
    return_value="Done",
)
def test_convert_from_config_with_one_failed_document(
    mock_storage, mock_get_docproto_files, mock_upload, capfd
):
    client = mock_storage.Client.return_value
    mock_bucket = mock.Mock()
    client.Bucket.return_value = mock_bucket

    mock_blob1 = mock.Mock(name="gs://test-directory/1/test-annotations.json")
    mock_blob1.download_as_bytes.return_value = (
        "gs://test-directory/1/test-annotations.json"
    )

    mock_blob2 = mock.Mock(name="gs://test-directory/1/test-config.json")
    mock_blob2.download_as_bytes.return_value = "gs://test-directory/1/test-config.json"

    mock_blob3 = mock.Mock(name="gs://test-directory/1/test.pdf")
    mock_blob3.download_as_bytes.return_value = "gs://test-directory/1/test.pdf"

    client.list_blobs.return_value = [mock_blob1, mock_blob2, mock_blob3]

    converter.convert_from_config(
        project_id="project-id",
        location="location",
        processor_id="project-id",
        gcs_input_path="gs://test-directory/",
        gcs_output_path="gs://test-directory-output/",
    )

    out, err = capfd.readouterr()
    assert "test_label" in out
    assert "Did not convert 1 documents" in out
    assert "document_2" in out


def test_convert_from_config_with_gcs_path_error():
    with pytest.raises(
        ValueError,
        match="gcs_uri must follow format 'gs://{bucket_name}/{gcs_prefix}'.",
    ):
        converter.convert_from_config(
            project_id="project-id",
            location="location",
            processor_id="project-id",
            gcs_input_path="test-directory/1",
            gcs_output_path="gs://test-directory/1/output",
        )


def test_convert_from_config_with_file_error():
    with pytest.raises(ValueError, match="gcs_prefix cannot contain file types"):
        converter.convert_from_config(
            project_id="project-id",
            location="location",
            processor_id="project-id",
            gcs_input_path="gs://test-directory/1.json",
            gcs_output_path="gs://test-directory/1/output",
        )
