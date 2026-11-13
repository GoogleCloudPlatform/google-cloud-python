# pylint: disable=protected-access
# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

import glob
import json
import os
import shutil
from unittest import mock
from xml.etree import ElementTree

import pytest
from google.cloud.vision import AnnotateFileResponse

from google.cloud import documentai
from google.cloud.documentai_toolbox import document, gcs_utilities


def get_bytes(file_name):
    result = []
    for filename in glob.glob(os.path.join(file_name, "*.json")):
        with open(os.path.join(os.getcwd(), filename), "rb") as f:
            result.append(f.read())

    return result


@pytest.fixture
def get_bytes_single_file_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/0")
        yield byte_factory


@pytest.fixture
def get_bytes_multiple_files_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/1")
        yield byte_factory


@pytest.fixture
def get_bytes_unordered_files_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/unordered_shards")
        yield byte_factory


@pytest.fixture(params=["tests/unit/resources/0", "tests/unit/resources/1"])
def get_bytes_multiple_directories_mock(request):
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes(request.param)
        yield byte_factory


@pytest.fixture
def get_bytes_form_parser_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/form_parser")
        yield byte_factory


@pytest.fixture
def get_bytes_splitter_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/splitter")
        yield byte_factory


@pytest.fixture
def get_bytes_classifier_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/classifier")
        yield byte_factory


@pytest.fixture
def get_bytes_images_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/images")
        yield byte_factory


@pytest.fixture
def get_bytes_empty_directory_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/fake_directory")
        yield byte_factory


@pytest.fixture
def get_bytes_missing_shard_mock():
    with mock.patch.object(gcs_utilities, "get_bytes") as byte_factory:
        byte_factory.return_value = get_bytes("tests/unit/resources/missing_shard")
        yield byte_factory


@pytest.fixture
def get_blob_mock():
    with mock.patch.object(gcs_utilities, "get_blob") as blob_factory:
        mock_blob = mock.Mock()
        mock_blob.download_as_bytes.return_value = get_bytes("tests/unit/resources/0")[
            0
        ]
        blob_factory.return_value = mock_blob
        yield blob_factory


def create_document_with_images_without_bbox(get_bytes_images_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )
    get_bytes_images_mock.assert_called_once()

    del (
        doc.entities[0]
        .documentai_object.page_anchor.page_refs[0]
        .bounding_poly.normalized_vertices
    )
    return doc


def test_get_shards_with_gcs_uri_contains_file_type():
    with pytest.raises(ValueError, match="gcs_prefix cannot contain file types"):
        document._get_shards(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/0.json",
        )


def test_get_shards_with_valid_gcs_uri(get_bytes_single_file_mock):
    actual = document._get_shards(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )

    get_bytes_single_file_mock.assert_called_once()
    # We are testing only one of the fields to make sure the file content could be loaded.
    assert actual[0].pages[0].page_number == 1


def test_get_shards_with_no_shards(get_bytes_empty_directory_mock):
    with pytest.raises(ValueError, match="Incomplete Document - No JSON files found."):
        document._get_shards(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/0/",
        )
        get_bytes_empty_directory_mock.assert_called_once()


def test_get_shards_with_missing_shard(get_bytes_missing_shard_mock):
    with pytest.raises(
        ValueError,
        match=r"Invalid Document - shardInfo\.shardCount",
    ):
        document._get_shards(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/0/",
        )
        get_bytes_missing_shard_mock.assert_called_once()


def test_pages_from_shards():
    shards = []
    for byte in get_bytes("tests/unit/resources/0"):
        shards.append(documentai.Document.from_json(byte))

    actual = document._pages_from_shards(shards=shards)
    assert len(actual[0].paragraphs) == 31

    for page_index, page in enumerate(actual):
        assert page.page_number == page_index + 1


def test_entities_from_shards():
    shards = []
    for byte in get_bytes("tests/unit/resources/0"):
        shards.append(documentai.Document.from_json(byte))

    actual = document._entities_from_shards(shards=shards)

    assert actual[0].mention_text == "$140.00"
    assert actual[0].type_ == "vat"
    assert actual[1].mention_text == "$140.00"
    assert actual[1].type_ == "vat/tax_amount"
    assert actual[1].normalized_text == "140 USD"


# For documents labeled in Document AI Workbench
def test_entities_from_shards_with_hex_ids():
    shards = []
    for byte in get_bytes("tests/unit/resources/hex_ids"):
        shards.append(documentai.Document.from_json(byte))

    actual = document._entities_from_shards(shards=shards)

    assert actual[0].documentai_object.id == "ef4fd8a921c0ea81"
    assert actual[0].mention_text == "453,945"
    assert actual[0].type_ == "application_number"
    assert actual[1].documentai_object.id == "ef4fd8a921c0e000"
    assert actual[1].mention_text == "G06F 1/26"
    assert actual[1].type_ == "class_international"


def test_entities_from_shards_classifier(get_bytes_classifier_mock):
    shards = document._get_shards(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )
    get_bytes_classifier_mock.assert_called_once()

    actual = document._entities_from_shards(shards=shards)

    # Check for error reported in https://github.com/googleapis/python-documentai-toolbox/issues/332
    assert repr(actual)
    assert actual[0].type_ == "computer_vision"
    assert round(actual[0].documentai_object.confidence, 8) == 0.47925246
    assert actual[0].documentai_object.id == "0"
    assert actual[1].type_ == "crypto"
    assert round(actual[1].documentai_object.confidence, 8) == 0.0433604
    assert actual[1].documentai_object.id == "1"
    assert actual[2].type_ == "med_tech"
    assert round(actual[2].documentai_object.confidence, 8) == 0.26732057
    assert actual[2].documentai_object.id == "2"
    assert actual[3].type_ == "other"
    assert round(actual[3].documentai_object.confidence, 8) == 0.2100666
    assert actual[3].documentai_object.id == "3"


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.documentai")
def test_get_batch_process_metadata_with_valid_operation(
    mock_docai,
):
    mock_client = mock_docai.DocumentProcessorServiceClient.return_value

    metadata = documentai.BatchProcessMetadata(
        state=documentai.BatchProcessMetadata.State.SUCCEEDED,
        individual_process_statuses=[
            documentai.BatchProcessMetadata.IndividualProcessStatus(
                input_gcs_source="gs://test-directory/documentai/input.pdf",
                output_gcs_destination="gs://test-directory/documentai/output/123456789/1",
            )
        ],
    )

    mock_operation = mock.Mock(
        done=True,
        metadata=mock.Mock(
            type_url="type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
            value=documentai.BatchProcessMetadata.serialize(metadata),
        ),
    )

    mock_client.get_operation.return_value = mock_operation

    operation_name = "projects/123456/locations/us/operations/7890123"
    timeout = 1
    document._get_batch_process_metadata(operation_name, timeout=timeout)

    mock_client.get_operation.assert_called()
    mock_docai.BatchProcessMetadata.deserialize.assert_called()


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.documentai")
def test_get_batch_process_metadata_with_running_operation(
    mock_docai,
):
    mock_client = mock_docai.DocumentProcessorServiceClient.return_value

    metadata = documentai.BatchProcessMetadata(
        state=documentai.BatchProcessMetadata.State.SUCCEEDED,
        individual_process_statuses=[
            documentai.BatchProcessMetadata.IndividualProcessStatus(
                input_gcs_source="gs://test-directory/documentai/input.pdf",
                output_gcs_destination="gs://test-directory/documentai/output/123456789/1",
            )
        ],
    )

    mock_operation_running = mock.Mock(done=False)
    mock_operation_finished = mock.Mock(
        done=True,
        metadata=mock.Mock(
            type_url="type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
            value=documentai.BatchProcessMetadata.serialize(metadata),
        ),
    )

    mock_client.get_operation.side_effect = [
        mock_operation_running,
        mock_operation_finished,
    ]

    operation_name = "projects/123456/locations/us/operations/7890123"
    document._get_batch_process_metadata(operation_name)

    mock_client.get_operation.assert_called()
    mock_docai.BatchProcessMetadata.deserialize.assert_called()


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.documentai")
def test_get_batch_process_metadata_with_no_metadata(mock_docai):
    with pytest.raises(
        ValueError,
        match="Operation does not contain metadata:",
    ):
        mock_client = mock_docai.DocumentProcessorServiceClient.return_value

        operation_name = "projects/123456/locations/us/operations/7890123"
        mock_operation = mock.Mock(done=True, metadata=None)
        mock_client.get_operation.return_value = mock_operation

        document._get_batch_process_metadata(operation_name)


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.documentai")
def test_get_batch_process_metadata_with_invalid_metadata_type(mock_docai):
    with pytest.raises(
        ValueError,
        match="Operation metadata type is not",
    ):
        mock_client = mock_docai.DocumentProcessorServiceClient.return_value

        operation_name = "projects/123456/locations/us/operations/7890123"
        mock_operation = mock.Mock(
            done=True,
            metadata=mock.Mock(
                type_url="type.googleapis.com/google.cloud.documentai.uiv1beta3.TrainProcessorVersionResponse",
            ),
        )
        mock_client.get_operation.return_value = mock_operation

        document._get_batch_process_metadata(operation_name)


def test_get_batch_process_metadata_with_invalid_operation_name():
    with pytest.raises(
        ValueError,
        match="Invalid Operation Name",
    ):
        document._get_batch_process_metadata(
            "projects//locations/us/operations/7890123"
        )


def test_bigquery_column_name():
    string_map = {
        "Phone #:": "phone_num",
        "Emergency Contact:": "emergency_contact",
        "Marital Status:": "marital_status",
        "Are you currently taking any medication? (If yes, please describe):": "are_you_currently_taking_any_medication_if_yes_please_describe",
        "Describe your medical concerns (symptoms, diagnoses, etc):": "describe_your_medical_concerns_symptoms_diagnoses_etc",
    }

    for key, value in string_map.items():
        assert document._bigquery_column_name(key) == value


def test_document_from_document_path_with_single_shard():
    actual = document.Document.from_document_path(
        document_path="tests/unit/resources/0/toolbox_invoice_test-0.json"
    )
    assert len(actual.pages) == 1


def test_document_from_document_path_with_directory():
    actual = document.Document.from_document_path(
        document_path="tests/unit/resources/0/"
    )
    assert len(actual.pages) == 1


def test_document_from_documentai_document_with_single_shard():
    with open(
        "tests/unit/resources/0/toolbox_invoice_test-0.json", "r", encoding="utf-8"
    ) as f:
        doc = documentai.Document.from_json(f.read())

    actual = document.Document.from_documentai_document(documentai_document=doc)
    assert len(actual.pages) == 1
    # checking cached value
    assert len(actual.pages) == 1

    assert len(actual.text) > 0
    assert len(actual.text) > 0


def test_document_from_documentai_document_layout_parser():
    with open(
        "tests/unit/resources/layout_parser/layout_parser.json", "r", encoding="utf-8"
    ) as f:
        doc = documentai.Document.from_json(f.read())

    actual = document.Document.from_documentai_document(documentai_document=doc)

    chunk_list = list(actual.chunks)
    assert len(chunk_list) == 2
    assert chunk_list[0].chunk_id == "c1"
    assert "CHAPTER I" in chunk_list[0].content
    assert chunk_list[0].page_span.page_start == 1
    assert chunk_list[0].page_span.page_end == 8

    assert chunk_list[1].chunk_id == "c2"
    assert "Was that me?" in chunk_list[1].content
    assert chunk_list[1].page_span.page_start == 8
    assert chunk_list[1].page_span.page_end == 15

    block_list = list(actual.document_layout_blocks)

    for i, block in enumerate(block_list, start=1):
        assert int(block.block_id) == i

    assert len(block_list) == 175
    assert block_list[0].block_id == "1"
    assert block_list[0].text_block.text == "CHAPTER I"
    assert block_list[0].text_block.type_ == "heading-1"
    assert block_list[0].text_block.blocks
    assert block_list[0].page_span.page_start == 1
    assert block_list[0].page_span.page_end == 8

    assert block_list[1].block_id == "2"
    assert block_list[1].text_block.text == "IN WHICH We Are Introduced to"
    assert block_list[1].text_block.type_ == "paragraph"
    assert block_list[1].page_span.page_start == 1
    assert block_list[1].page_span.page_end == 1


def test_document_from_gcs_with_single_shard(get_bytes_single_file_mock):
    actual = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )

    get_bytes_single_file_mock.assert_called_once()
    assert len(actual.pages) == 1
    # checking cached value
    assert len(actual.pages) == 1

    assert len(actual.text) > 0
    assert len(actual.text) > 0


def test_document_from_gcs_with_multiple_shards(get_bytes_multiple_files_mock):
    actual = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/1/"
    )
    get_bytes_multiple_files_mock.assert_called_once()

    assert len(actual.pages) == 48
    # checking cached value
    assert len(actual.pages) == 48

    assert len(actual.text) > 0
    assert len(actual.text) > 0


def test_document_from_gcs_with_unordered_shards(get_bytes_unordered_files_mock):
    actual = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/2/"
    )
    get_bytes_unordered_files_mock.assert_called_once()

    expected_shard_count = len(actual.shards)
    current_text_offset = 0
    for expected_shard_index, shard in enumerate(actual.shards):
        assert int(shard.shard_info.shard_index) == expected_shard_index
        assert int(shard.shard_info.shard_count) == expected_shard_count
        assert int(shard.shard_info.text_offset) == current_text_offset
        current_text_offset += len(shard.text)

    for page_index, page in enumerate(actual.pages):
        assert page.page_number == page_index + 1


def test_document_from_gcs_uri(get_blob_mock):
    actual = document.Document.from_gcs_uri(
        gcs_uri="gs://test-directory/documentai/output/123456789/0/document.json"
    )

    get_blob_mock.assert_called_once()

    assert (
        actual.gcs_uri
        == "gs://test-directory/documentai/output/123456789/0/document.json"
    )
    assert len(actual.pages) == 1
    # checking cached value
    assert len(actual.pages) == 1

    assert len(actual.text) > 0
    assert len(actual.text) > 0


def test_document_from_batch_process_metadata_with_multiple_input_files(
    get_bytes_multiple_directories_mock,
):
    mock_metadata = mock.Mock(
        state=documentai.BatchProcessMetadata.State.SUCCEEDED,
        individual_process_statuses=[
            mock.Mock(
                input_gcs_source="gs://test-directory/documentai/input.pdf",
                output_gcs_destination="gs://test-directory/documentai/output/123456789/1",
            ),
            mock.Mock(
                input_gcs_source="gs://test-directory/documentai/input2.pdf",
                output_gcs_destination="gs://test-directory/documentai/output/123456789/2",
            ),
        ],
    )
    documents = document.Document.from_batch_process_metadata(mock_metadata)

    get_bytes_multiple_directories_mock.assert_called()
    assert get_bytes_multiple_directories_mock.call_count == 2
    assert len(documents) == 2

    assert documents[0].gcs_bucket_name == "test-directory"
    assert documents[0].gcs_prefix == "documentai/output/123456789/1/"
    assert documents[0].gcs_input_uri == "gs://test-directory/documentai/input.pdf"

    assert documents[1].gcs_bucket_name == "test-directory"
    assert documents[1].gcs_prefix == "documentai/output/123456789/2/"
    assert documents[1].gcs_input_uri == "gs://test-directory/documentai/input2.pdf"


def test_document_from_batch_process_metadata_with_multiple_input_files_matching_prefix(
    get_bytes_multiple_directories_mock,
):
    mock_metadata = mock.Mock(
        state=documentai.BatchProcessMetadata.State.SUCCEEDED,
        individual_process_statuses=[
            mock.Mock(
                input_gcs_source="gs://test-directory/documentai/input.pdf",
                output_gcs_destination="gs://test-directory/documentai/output/123456789/1",
            ),
            mock.Mock(
                input_gcs_source="gs://test-directory/documentai/input2.pdf",
                output_gcs_destination="gs://test-directory/documentai/output/123456789/11",
            ),
        ],
    )
    documents = document.Document.from_batch_process_metadata(mock_metadata)

    get_bytes_multiple_directories_mock.assert_called()
    assert get_bytes_multiple_directories_mock.call_count == 2
    assert len(documents) == 2

    assert documents[0].gcs_bucket_name == "test-directory"
    assert documents[0].gcs_prefix == "documentai/output/123456789/1/"
    assert documents[0].gcs_input_uri == "gs://test-directory/documentai/input.pdf"

    assert documents[1].gcs_bucket_name == "test-directory"
    assert documents[1].gcs_prefix == "documentai/output/123456789/11/"
    assert documents[1].gcs_input_uri == "gs://test-directory/documentai/input2.pdf"


def test_document_from_batch_process_metadata_with_failed_operation():
    with pytest.raises(
        ValueError,
        match="Batch Process Failed: Internal Error Occured",
    ):
        mock_metadata = mock.Mock(
            state=documentai.BatchProcessMetadata.State.FAILED,
            state_message="Internal Error Occured",
        )
        document.Document.from_batch_process_metadata(mock_metadata)


def test_search_page_with_target_string(get_bytes_single_file_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )

    actual_pages = doc.search_pages(target_string="contract")

    get_bytes_single_file_mock.assert_called_once()
    assert len(actual_pages) == 1


def test_search_page_with_target_pattern(get_bytes_single_file_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )

    actual_regex = doc.search_pages(pattern=r"\$\d+(?:\.\d+)?")

    get_bytes_single_file_mock.assert_called_once()
    assert len(actual_regex) == 1


def test_search_page_with_multiple_pages(get_bytes_multiple_files_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )

    actual_pages = doc.search_pages(target_string="Invoice")

    get_bytes_multiple_files_mock.assert_called_once()
    assert len(actual_pages) == 48


def test_search_page_with_no_results(get_bytes_single_file_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0/"
    )

    actual_pages = doc.search_pages(target_string="Google")

    get_bytes_single_file_mock.assert_called_once()
    assert len(actual_pages) == 0


def test_search_page_with_regex_and_str(get_bytes_single_file_mock):
    with pytest.raises(
        ValueError,
        match="Exactly one of target_string and pattern must be specified.",
    ):
        doc = document.Document.from_gcs(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/0/",
        )
        doc.search_pages(pattern=r"^\$?(\d*(\d\.?|\.\d{1,2}))$", target_string="hello")

        get_bytes_single_file_mock.assert_called_once()


def test_search_page_with_none(get_bytes_single_file_mock):
    with pytest.raises(
        ValueError,
        match="Exactly one of target_string and pattern must be specified.",
    ):
        doc = document.Document.from_gcs(
            gcs_bucket_name="test-directory",
            gcs_prefix="documentai/output/123456789/0/",
        )
        doc.search_pages()

        get_bytes_single_file_mock.assert_called_once()


def test_get_entity_by_type(get_bytes_single_file_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )

    actual = doc.get_entity_by_type(target_type="receiver_address")

    get_bytes_single_file_mock.assert_called_once()

    assert len(actual) == 1
    assert actual[0].type_ == "receiver_address"
    assert actual[0].mention_text == "222 Main Street\nAnytown, USA"


def test_get_form_field_by_name(get_bytes_form_parser_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )
    actual = doc.get_form_field_by_name(target_field="Phone #:")

    get_bytes_form_parser_mock.assert_called_once()

    assert len(actual) == 1
    assert actual[0].field_name == "Phone #:"
    assert actual[0].field_value == "(906) 917-3486"


def test_form_fields_to_dict(get_bytes_form_parser_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )
    actual = doc.form_fields_to_dict()

    get_bytes_form_parser_mock.assert_called_once()

    assert len(actual) == 17
    assert actual.get("address") == "24 Barney Lane"
    assert actual.get("city") == "Towaco"


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.bigquery")
def test_form_fields_to_bigquery(mock_bigquery, get_bytes_form_parser_mock):
    client = mock_bigquery.Client.return_value

    mock_table = mock.Mock()
    client.dataset.table.return_value = mock_table

    mock_load_job = mock.Mock()
    client.load_table_from_json.return_value = mock_load_job

    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )

    actual = doc.form_fields_to_bigquery(
        dataset_name="test_dataset", table_name="test_table", project_id="test_project"
    )

    get_bytes_form_parser_mock.assert_called_once()
    mock_bigquery.Client.assert_called_once()

    assert actual


def test_entities_to_dict(get_bytes_single_file_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )
    actual = doc.entities_to_dict()

    get_bytes_single_file_mock.assert_called_once()

    assert len(actual) == 25
    assert actual.get("vat") == "$140.00"
    assert actual.get("vat_tax_amount") == "$140.00"


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.bigquery")
def test_entities_to_bigquery(mock_bigquery, get_bytes_single_file_mock):
    client = mock_bigquery.Client.return_value

    mock_table = mock.Mock()
    client.dataset.table.return_value = mock_table

    mock_load_job = mock.Mock()
    client.load_table_from_json.return_value = mock_load_job

    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )

    actual = doc.entities_to_bigquery(
        dataset_name="test_dataset", table_name="test_table", project_id="test_project"
    )

    get_bytes_single_file_mock.assert_called_once()
    mock_bigquery.Client.assert_called_once()

    assert actual


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.Pdf")
def test_split_pdf(mock_Pdf, get_bytes_splitter_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )
    mock_input_file = mock.Mock()
    mock_Pdf.open.return_value.__enter__.return_value.name = mock_input_file

    mock_output_file = mock.Mock()
    mock_Pdf.new.return_value = mock_output_file

    actual = doc.split_pdf(
        pdf_path="procurement_multi_document.pdf", output_path="splitter/output/"
    )

    get_bytes_splitter_mock.assert_called_once()

    assert actual == [
        "procurement_multi_document_pg1_invoice_statement.pdf",
        "procurement_multi_document_pg2_receipt_statement.pdf",
        "procurement_multi_document_pg3_other.pdf",
        "procurement_multi_document_pg4_utility_statement.pdf",
        "procurement_multi_document_pg5_restaurant_statement.pdf",
        "procurement_multi_document_pg6-7_other.pdf",
    ]


def test_split_pdf_with_non_splitter(get_bytes_classifier_mock):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )

    with pytest.raises(
        ValueError,
        match="Entities do not contain start or end pages.",
    ):
        doc.split_pdf(
            pdf_path="procurement_multi_document.pdf", output_path="splitter/output/"
        )

    get_bytes_classifier_mock.assert_called_once()


@mock.patch("google.cloud.documentai_toolbox.wrappers.document.Pdf")
def test_split_pdf_sanitizes_entity_type_path_traversal(
    mock_Pdf, get_bytes_splitter_mock
):
    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )
    mock_output_file = mock.Mock()
    mock_Pdf.new.return_value = mock_output_file

    # Entity types are read from the parsed Document and may carry path
    # separators or traversal sequences.
    doc.entities[0].type_ = "../../../../etc:passwd"

    output_path = "splitter/output/"
    actual = doc.split_pdf(
        pdf_path="procurement_multi_document.pdf", output_path=output_path
    )

    get_bytes_splitter_mock.assert_called_once()

    resolved_output = os.path.realpath(output_path)
    for call in mock_output_file.save.call_args_list:
        written_path = os.path.realpath(call.args[0])
        assert written_path == resolved_output or written_path.startswith(
            resolved_output + os.sep
        )

    assert actual[0] == "procurement_multi_document_pg1_.._.._.._.._etc_passwd.pdf"


def test_convert_document_to_annotate_file_response():
    doc = document.Document.from_document_path(
        document_path="tests/unit/resources/0/toolbox_invoice_test-0.json"
    )

    actual = doc.convert_document_to_annotate_file_response()

    with open("tests/unit/resources/toolbox_invoice_test-0-vision.json", "r") as f:
        invoice_json = f.read()

    expected = AnnotateFileResponse.from_json(invoice_json)

    assert actual.responses[0].text_annotations[0].description == "Invoice"
    assert len(actual.responses[0].text_annotations) == 86

    assert len(actual.responses[0].full_text_annotation.pages) == 1
    assert actual.responses[0].full_text_annotation.text is not None

    assert actual == expected


def test_convert_document_to_annotate_file_json_response():
    doc = document.Document.from_document_path(
        document_path="tests/unit/resources/0/toolbox_invoice_test-0.json"
    )

    actual = doc.convert_document_to_annotate_file_json_response()

    with open("tests/unit/resources/toolbox_invoice_test-0-vision.json", "r") as f:
        expected = f.read()

    assert actual == expected


def test_export_images(get_bytes_images_mock):
    output_path = "resources/output/"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
        assert not os.path.exists(output_path)

    doc = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/0"
    )

    os.makedirs(output_path)

    actual = doc.export_images(
        output_path=output_path,
        output_file_prefix="exported_photo",
        output_file_extension="png",
    )
    get_bytes_images_mock.assert_called_once()

    assert actual == [
        "exported_photo_0_Portrait.png",
    ]

    assert os.path.exists(output_path)
    shutil.rmtree(output_path)


def test_export_images_empty_bounding_box(get_bytes_images_mock):
    output_path = "resources/output/"

    doc = create_document_with_images_without_bbox(get_bytes_images_mock)
    actual = doc.export_images(
        output_path=output_path,
        output_file_prefix="exported_photo",
        output_file_extension="png",
    )
    get_bytes_images_mock.assert_called_once()

    assert not actual


def test_export_hocr_str():
    wrapped_document = document.Document.from_document_path(
        document_path="tests/unit/resources/0/toolbox_invoice_test-0.json"
    )

    actual_hocr = wrapped_document.export_hocr_str(title="toolbox_invoice_test-0")
    assert actual_hocr

    element = ElementTree.fromstring(actual_hocr)
    assert element is not None

    with open(
        "tests/unit/resources/toolbox_invoice_test_0_hocr.xml", "r", encoding="utf-8"
    ) as f:
        expected = f.read()

    assert actual_hocr == expected


def test_export_hocr_str_with_blank_document():
    wrapped_document = document.Document.from_document_path(
        document_path="tests/unit/resources/blank_document.json"
    )

    actual_hocr = wrapped_document.export_hocr_str(title="hocr_blank")

    assert actual_hocr

    element = ElementTree.fromstring(actual_hocr)
    assert element is not None


def test_export_hocr_str_with_escape_characters():
    wrapped_document = document.Document.from_document_path(
        document_path="tests/unit/resources/toolbox_invoice_test-0-hocr-escape.json"
    )

    actual_hocr = wrapped_document.export_hocr_str(title="hocr-escape")
    assert actual_hocr

    element = ElementTree.fromstring(actual_hocr)
    assert element is not None

    with open(
        "tests/unit/resources/toolbox_invoice_test-0-hocr-escape.xml",
        "r",
        encoding="utf-8",
    ) as f:
        expected = f.read()

    assert actual_hocr == expected


def test_export_hocr_str_escapes_title():
    wrapped_document = document.Document.from_document_path(
        document_path="tests/unit/resources/0/toolbox_invoice_test-0.json"
    )

    actual_hocr = wrapped_document.export_hocr_str(
        title="</title><script>alert(1)</script>"
    )

    assert "<script>alert(1)</script>" not in actual_hocr

    element = ElementTree.fromstring(actual_hocr)
    assert element is not None
    title_element = element.find(".//{http://www.w3.org/1999/xhtml}title")
    assert title_element.text == "</title><script>alert(1)</script>"


def test_document_to_merged_documentai_document(get_bytes_multiple_files_mock):
    wrapped_document = document.Document.from_gcs(
        gcs_bucket_name="test-directory", gcs_prefix="documentai/output/123456789/1/"
    )
    get_bytes_multiple_files_mock.assert_called_once()

    actual = documentai.Document.to_json(
        wrapped_document.to_merged_documentai_document()
    )
    with open("tests/unit/resources/merged_document/merged_shards.json", "r") as f:
        merged_document = documentai.Document.from_json(f.read())
        expected = documentai.Document.to_json(merged_document)

    assert actual == expected


def test_document_to_merged_documentai_document_one_shard():
    path = "tests/unit/resources/0/toolbox_invoice_test-0.json"

    with open(path, "r", encoding="utf-8") as f:
        documentai_document = documentai.Document.from_json(f.read())

    wrapped_document = document.Document.from_documentai_document(documentai_document)
    actual = wrapped_document.to_merged_documentai_document()

    assert actual == documentai_document


def test_apply_text_offset():
    path = "tests/unit/resources/1/toolbox_large_document_test-1.json"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        documentai_document = documentai.Document.from_json(content)

    assert documentai_document.shard_info.text_offset == 4350

    doc_dict = documentai.Document.to_dict(documentai_document)
    document._apply_text_offset(
        doc_dict, int(documentai_document.shard_info.text_offset)
    )

    actual = documentai.Document.from_json(json.dumps(doc_dict))
    assert actual.entities[0].text_anchor.text_segments[0].start_index == 4616
    assert actual.entities[0].text_anchor.text_segments[0].end_index == 4622
    assert actual.entities[0].text_anchor.text_segments[3].start_index == 4634
    assert actual.entities[0].text_anchor.text_segments[3].end_index == 4640

    assert (
        actual.pages[0].blocks[0].layout.text_anchor.text_segments[0].start_index
    ) == 4350
    assert (
        actual.pages[0].blocks[0].layout.text_anchor.text_segments[0].end_index == 4358
    )
