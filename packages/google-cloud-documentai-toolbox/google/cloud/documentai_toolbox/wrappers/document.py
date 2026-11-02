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
"""Wrappers for Document AI Document type."""

import collections
import copy
import dataclasses
import glob
import os
import re
from functools import cached_property
from typing import Any, Dict, Iterable, Iterator, List, Optional, Type, Union

from google.api_core.client_options import ClientOptions
from google.api_core.operation import from_gapic as operation_from_gapic
from google.cloud.vision import AnnotateFileResponse
from google.longrunning.operations_pb2 import GetOperationRequest
from jinja2 import Environment, PackageLoader
from pikepdf import Pdf

from google.cloud import bigquery, documentai
from google.cloud.documentai_toolbox import constants
from google.cloud.documentai_toolbox.converters import vision_helpers
from google.cloud.documentai_toolbox.utilities import gcs_utilities
from google.cloud.documentai_toolbox.wrappers.entity import Entity
from google.cloud.documentai_toolbox.wrappers.page import FormField, Page


def _chunks_from_shards(
    shards: List[documentai.Document],
) -> Iterator[documentai.Document.ChunkedDocument.Chunk]:
    for shard in shards:
        for chunk in shard.chunked_document.chunks:
            yield chunk


def _document_layout_blocks_from_shards(
    shards: List[documentai.Document],
) -> Iterator[documentai.Document.DocumentLayout.DocumentLayoutBlock]:
    def extract_blocks(
        blocks: Iterable[documentai.Document.DocumentLayout.DocumentLayoutBlock],
    ) -> Iterator[documentai.Document.DocumentLayout.DocumentLayoutBlock]:
        queue = collections.deque(blocks)

        while queue:
            block = queue.popleft()
            yield block
            # Add the nested blocks to the stack in the correct order
            if block.text_block and block.text_block.blocks:
                queue.extendleft(reversed(block.text_block.blocks))

    for shard in shards:
        yield from extract_blocks(shard.document_layout.blocks)


def _entities_from_shards(
    shards: List[documentai.Document],
) -> List[Entity]:
    r"""Returns a list of Entities and Properties from a list of documentai.Document shards.

    Args:
        shards (List[google.cloud.documentai.Document]):
            Required. List of document shards.

    Returns:
        List[Entity]:
            a list of Entities.
    """
    result = [
        Entity(
            documentai_object=item,
            # Needed to load the correct page index for sharded documents.
            page_offset=sum(len(shard.pages) for shard in shards[:i]),
        )
        for i, shard in enumerate(shards)
        for entity in shard.entities
        for item in (entity, *entity.properties)
    ]

    # https://github.com/googleapis/python-documentai-toolbox/issues/199
    # Only sort entities if the ids are all numeric.
    # Document AI Workbench labeling outputs hexadecimal ids which should not be sorted.
    # Sorting numeric ids is needed for backwards-compatible behavior.
    if len(result) > 1 and all(item.documentai_object.id.isdigit() for item in result):
        result.sort(key=lambda x: int(x.documentai_object.id))
    return result


def _pages_from_shards(shards: List[documentai.Document]) -> List[Page]:
    r"""Returns a list of Pages from a list of documentai.Document shards.

    Args:
        shards (List[google.cloud.documentai.Document]):
            Required. List of document shards.

    Returns:
        List[Page]:
            A list of Pages.
    """
    result = [
        Page(documentai_object=shard_page, _document_text=shard.text)
        for shard in shards
        for shard_page in shard.pages
    ]

    if len(result) > 1 and result[0].page_number:
        result.sort(key=lambda x: x.page_number)
    return result


def _get_shards(gcs_bucket_name: str, gcs_prefix: str) -> List[documentai.Document]:
    r"""Returns a list of `documentai.Document` shards from a Cloud Storage folder.

    Args:
        gcs_bucket_name (str):
            Required. The name of the gcs bucket.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_bucket_name=`bucket`.
        gcs_prefix (str):
            Required. The prefix of the json files in the target_folder.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_prefix=`{optional_folder}/{target_folder}`.
    Returns:
        List[google.cloud.documentai.Document]:
            A list of documentai.Documents.

    """
    file_check = re.match(constants.FILE_CHECK_REGEX, gcs_prefix)
    if file_check is not None:
        raise ValueError("gcs_prefix cannot contain file types")

    byte_array = gcs_utilities.get_bytes(gcs_bucket_name, gcs_prefix)
    shards = [
        documentai.Document.from_json(byte, ignore_unknown_fields=True)
        for byte in byte_array
    ]

    if not shards:
        raise ValueError("Incomplete Document - No JSON files found.")

    total_shards = len(shards)

    if total_shards > 1:
        shards.sort(key=lambda x: int(x.shard_info.shard_index))

        for shard in shards:
            if int(shard.shard_info.shard_count) != total_shards:
                raise ValueError(
                    f"Invalid Document - shardInfo.shardCount ({shard.shard_info.shard_count}) does not match number of shards ({total_shards})."
                )

    return shards


def _get_batch_process_metadata(
    operation_name: str,
    location: Optional[str] = None,
    timeout: Optional[float] = None,
) -> documentai.BatchProcessMetadata:
    r"""Get `BatchProcessMetadata` from a `batch_process_documents()` long-running operation.

    Args:
        operation_name (str):
            Required. The fully qualified operation name for a `batch_process_documents()` operation.

        location (str):
                Optional. The location of the processor used for `batch_process_documents()`.
                Deprecated. Maintained for backwards compatibility.

        timeout (float):
            Optional. Default None. Time in seconds to wait for operation to complete.
            If None, will wait indefinitely.
    Returns:
        documentai.BatchProcessMetadata:
            Metadata from batch process.
    """
    # Validate Operation Name
    match = re.search(
        r"projects\/\w+\/locations\/(\w+)\/operations\/\w+", operation_name
    )

    if not match:
        raise ValueError(
            f"Invalid Operation Name: {operation_name}\n"
            "Expected operation name in the format `projects/<project>/locations/<location>/operations/<operation>`"
        )

    location = location or match.group(1)

    client = documentai.DocumentProcessorServiceClient(
        client_info=gcs_utilities._get_client_info(module="get_batch_process_metadata"),
        client_options=ClientOptions(
            api_endpoint=f"{location}-documentai.googleapis.com"
        ),
    )

    # Poll Operation until complete.
    operation = operation_from_gapic(
        operation=client.get_operation(
            request=GetOperationRequest(name=operation_name),
        ),
        operations_client=client,
        result_type=documentai.BatchProcessResponse,
    )
    operation.result(timeout=timeout)

    operation_pb = operation.operation

    # Get Operation metadata.
    if not operation_pb.metadata:
        raise ValueError(f"Operation does not contain metadata: {operation}")

    metadata_type = (
        "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata"
    )

    if (
        not operation_pb.metadata.type_url
        or operation_pb.metadata.type_url != metadata_type
    ):
        raise ValueError(
            f"Operation metadata type is not `{metadata_type}`. Type is `{operation_pb.metadata.type_url}`."
        )

    metadata: documentai.BatchProcessMetadata = (
        documentai.BatchProcessMetadata.deserialize(operation_pb.metadata.value)
    )

    return metadata


def _insert_into_dictionary_with_list(
    dic: Dict[str, Union[str, List[str]]], key: str, value: str
) -> Dict[str, Union[str, List[str]]]:
    r"""Inserts value into a dictionary that can contain lists.

    Args:
        dic (Dict[str, Union[str, List[str]]]):
            Required. The dictionary to insert into.
        key (str):
            Required. The key to be created or inserted into.
        value (str):
            Required. The value to be inserted.

    Returns:
        Dict[str, Union[str, List[str]]]:
            The dictionary after adding the key-value pair.
    """
    existing_value = dic.get(key)

    if existing_value:
        # For duplicate keys.
        # Change type to a List if not already.
        if not isinstance(existing_value, list):
            existing_value = [existing_value]

        existing_value.append(value)
        dic[key] = existing_value
    else:
        dic[key] = value

    return dic


def _bigquery_column_name(input_string: str) -> str:
    r"""Converts a string into a BigQuery column name.
        https://cloud.google.com/bigquery/docs/schemas#column_names

    Args:
        input_string (str):
            Required: The string to convert.
    Returns:
        str
            The converted string.

    """
    char_map: Dict[str, str] = {
        r":|;|\(|\)|\[|\]|,|\.|\?|\!|\'|\n": "",
        r"/| ": "_",
        r"#": "num",
        r"@": "at",
    }

    for key, value in char_map.items():
        input_string = re.sub(key, value, input_string)

    return input_string.lower()


def _dict_to_bigquery(
    dic: Dict[str, Union[str, List[str]]],
    dataset_name: str,
    table_name: str,
    project_id: Optional[str],
) -> bigquery.job.LoadJob:
    r"""Loads dictionary to a BigQuery table.

    Args:
        dic (Dict[str, Union[str, List[str]]]):
            Required: The dictionary to insert.
        dataset_name (str):
            Required. Name of the BigQuery dataset.
        table_name (str):
            Required. Name of the BigQuery table.
        project_id (Optional[str]):
            Optional. Project ID containing the BigQuery table. If not passed, falls back to the default inferred from the environment.
    Returns:
        bigquery.job.LoadJob:
            The BigQuery LoadJob for adding the dictionary.

    """
    bq_client = bigquery.Client(
        project=project_id, client_info=gcs_utilities._get_client_info()
    )
    resolved_project_id = project_id or bq_client.project
    table_ref = bigquery.DatasetReference(
        project=resolved_project_id, dataset_id=dataset_name
    ).table(table_name)

    job_config = bigquery.LoadJobConfig(
        schema_update_options=[
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
            bigquery.SchemaUpdateOption.ALLOW_FIELD_RELAXATION,
        ],
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    )

    return bq_client.load_table_from_json(
        json_rows=[dic],
        destination=table_ref,
        job_config=job_config,
    )


def _apply_text_offset(
    documentai_object: Union[Dict[str, Any], List[Any]], text_offset: int
) -> None:
    r"""Applies a text offset to all text_segments in `documentai_object`.

    Args:
        documentai_object (object):
            Required. Document AI object to apply `text_offset` to.
        text_offset (int):
            Required. Text offset to apply. From `Document.shard_info.text_offset`.
    Returns:
        None

    """
    if isinstance(documentai_object, dict):
        for key, value in documentai_object.items():
            if key == "text_segments":
                documentai_object[key] = [
                    {
                        "start_index": int(text_segment.get("start_index", 0))
                        + text_offset,
                        "end_index": int(text_segment.get("end_index", 0))
                        + text_offset,
                    }
                    for text_segment in value
                ]
            else:
                _apply_text_offset(value, text_offset)
    elif isinstance(documentai_object, list):
        for item in documentai_object:
            _apply_text_offset(item, text_offset)


@dataclasses.dataclass
class Document:
    r"""Represents a wrapped `Document`.

    This class hides away the complexities of using the `Document` protobuf
    response outputted by `BatchProcessDocuments` or `ProcessDocument`
    methods and implements convenient methods for searching and
    extracting information within the `Document`.

    Attributes:
        shards (List[google.cloud.documentai.Document]):
            Required. A list of `documentai.Document` shards of the same `Document`.
            Each shard consists of a number of pages in the `Document`.
        gcs_bucket_name (Optional[str]):
            Optional. The name of the gcs bucket.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where `gcs_bucket_name=bucket`.
        gcs_prefix (Optional[str]):
            Optional. The prefix of the json files in the target_folder.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where `gcs_prefix={optional_folder}/{target_folder}`.

            For more information, refer to https://cloud.google.com/storage/docs/json_api/v1/objects/list
        gcs_input_uri (str):
            Optional. The gcs uri to the original input file.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/{file_name}.pdf`
        pages (List[Page]):
            A list of `Pages` in the `Document`.
        entities (List[Entity]):
            A list of un-nested `Entities` in the `Document`.
        chunks (Iterator[documentai.Document.ChunkedDocument.Chunk]):
            An iterator of document chunks extracted from a Layout Parser.
        document_layout_blocks (Iterator[documentai.Document.DocumentLayout.DocumentLayoutBlock]):
            An iterator of document layout blocks extracted from a Layout Parser.
        text (str):
            The full text of the `Document`.
    """

    shards: List[documentai.Document] = dataclasses.field(repr=False)
    gcs_bucket_name: Optional[str] = dataclasses.field(default=None, repr=False)
    gcs_prefix: Optional[str] = dataclasses.field(default=None, repr=False)
    gcs_uri: Optional[str] = dataclasses.field(default=None, repr=False)
    gcs_input_uri: Optional[str] = dataclasses.field(default=None, repr=False)

    @cached_property
    def pages(self):
        return _pages_from_shards(shards=self.shards)

    @cached_property
    def entities(self):
        return _entities_from_shards(shards=self.shards)

    @cached_property
    def chunks(self):
        return _chunks_from_shards(shards=self.shards)

    @cached_property
    def document_layout_blocks(self):
        return _document_layout_blocks_from_shards(shards=self.shards)

    @cached_property
    def text(self):
        return "".join(shard.text for shard in self.shards)

    @classmethod
    def from_document_path(
        cls: Type["Document"],
        document_path: str,
    ) -> "Document":
        r"""Loads `Document` from local `document_path`.

            .. code-block:: python

                from google.cloud.documentai_toolbox import document

                document_path = "/path/to/local/file.json"
                wrapped_document = document.Document.from_document_path(document_path)

        Args:
            document_path (str):
                Required. The path to the `document.json` file or directory containing sharded `document.json` files.
        Returns:
            Document:
                A document from local `document_path`.
        """
        document_paths = (
            glob.glob(os.path.join(document_path, f"*{constants.JSON_EXTENSION}"))
            if os.path.isdir(document_path)
            else [document_path]
        )

        documents: List[documentai.Document] = []
        for file_path in document_paths:
            with open(file_path, "r", encoding="utf-8") as file:
                json_content = file.read()
                document = documentai.Document.from_json(
                    json_content,
                    ignore_unknown_fields=True,
                )
                documents.append(document)

        return cls(shards=documents)

    @classmethod
    def from_documentai_document(
        cls: Type["Document"],
        documentai_document: documentai.Document,
    ) -> "Document":
        r"""Loads `Document` from local `documentai_document`.

            .. code-block:: python

                from google.cloud import documentai
                from google.cloud.documentai_toolbox import document

                documentai_document = client.process_documents(request).document
                wrapped_document = document.Document.from_documentai_document(documentai_document)

        Args:
            documentai_document (documentai.Document):
                Required. The `Document.proto` response.
        Returns:
            Document:
                A document from local `documentai_document`.
        """

        return cls(shards=[documentai_document])

    @classmethod
    def from_gcs(
        cls: Type["Document"],
        gcs_bucket_name: str,
        gcs_prefix: str,
        gcs_input_uri: Optional[str] = None,
    ) -> "Document":
        r"""Loads a Document from a Cloud Storage directory.

        Args:
            gcs_bucket_name (str):
                Required. The gcs bucket.

                Format: Given `gs://{bucket_name}/{optional_folder}/{operation_id}/` where `gcs_bucket_name={bucket_name}`.
            gcs_prefix (str):
                Required. The prefix to the location of the target folder.

                Format: Given `gs://{bucket_name}/{optional_folder}/{target_folder}` where `gcs_prefix={optional_folder}/{target_folder}`.
            gcs_input_uri (str):
                Optional. The gcs uri to the original input file.

                Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/{file_name}.pdf`
        Returns:
            Document:
                A document from gcs.
        """
        # Add trailing slash if not present.
        gcs_prefix = gcs_prefix.rstrip("/") + "/"
        shards = _get_shards(gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix)
        return cls(
            shards=shards,
            gcs_bucket_name=gcs_bucket_name,
            gcs_prefix=gcs_prefix,
            gcs_input_uri=gcs_input_uri,
        )

    @classmethod
    def from_gcs_uri(
        cls: Type["Document"],
        gcs_uri: str,
        gcs_input_uri: Optional[str] = None,
    ) -> "Document":
        r"""Loads a Document from a Cloud Storage uri.

        Args:
            gcs_uri (str):
                Required. The full GCS uri to a Document JSON file.

                Example: `gs://{bucket_name}/{optional_folder}/{target_file}.json`.
            gcs_input_uri (str):
                Optional. The gcs uri to the original input file.

                Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/{file_name}.pdf`
        Returns:
            Document:
                A document from gcs.
        """
        blob = gcs_utilities.get_blob(gcs_uri=gcs_uri, module="get-document")
        shards = [
            documentai.Document.from_json(
                blob.download_as_bytes(),
                ignore_unknown_fields=True,
            )
        ]
        return cls(
            shards=shards,
            gcs_uri=gcs_uri,
            gcs_input_uri=gcs_input_uri,
        )

    @classmethod
    def from_batch_process_metadata(
        cls: Type["Document"], metadata: documentai.BatchProcessMetadata
    ) -> List["Document"]:
        r"""Loads Documents from Cloud Storage, using the output from `BatchProcessMetadata`.

            .. code-block:: python

                from google.cloud import documentai
                from google.cloud.documentai_toolbox import document

                operation = client.batch_process_documents(request)
                operation.result(timeout=timeout)
                metadata = documentai.BatchProcessMetadata(operation.metadata)
                wrapped_document = document.Document.from_batch_process_metadata(metadata)

        Args:
            metadata (documentai.BatchProcessMetadata):
                Required. The operation metadata after a `batch_process_documents()` operation completes.

        Returns:
            List[Document]:
                A list of wrapped documents from gcs. Each document corresponds to an input file.
        """
        if metadata.state != documentai.BatchProcessMetadata.State.SUCCEEDED:
            raise ValueError(f"Batch Process Failed: {metadata.state_message}")

        return [
            Document.from_gcs(
                *gcs_utilities.split_gcs_uri(process.output_gcs_destination),
                gcs_input_uri=process.input_gcs_source,
            )
            for process in list(metadata.individual_process_statuses)
        ]

    @classmethod
    def from_batch_process_operation(
        cls: Type["Document"],
        location: str,  # pylint: disable=unused-argument
        operation_name: str,
        timeout: Optional[float] = None,
    ) -> List["Document"]:
        r"""Loads Documents from Cloud Storage, using the operation name returned from `batch_process_documents()`.

            .. code-block:: python

                from google.cloud import documentai
                from google.cloud.documentai_toolbox import document

                operation = client.batch_process_documents(request)
                operation_name = operation.operation.name
                wrapped_document = document.Document.from_batch_process_operation(operation_name)

        Args:
            location (str):
                Optional. The location of the processor used for `batch_process_documents()`.
                Deprecated. Maintained for backwards compatibility.

            operation_name (str):
                Required. The fully qualified operation name for a `batch_process_documents()` operation.

                Format: `projects/{project}/locations/{location}/operations/{operation}`

            timeout (float):
                Optional. Default None. Time in seconds to wait for operation to complete.
                If None, will wait indefinitely.

        Returns:
            List[Document]:
                A list of wrapped documents from gcs. Each document corresponds to an input file.
        """
        return cls.from_batch_process_metadata(
            metadata=_get_batch_process_metadata(
                operation_name=operation_name,
                location=location,
                timeout=timeout,
            )
        )

    def search_pages(
        self, target_string: Optional[str] = None, pattern: Optional[str] = None
    ) -> List[Page]:
        r"""Returns the list of Pages containing target_string or text matching pattern.

        Args:
            target_string (Optional[str]):
                Optional. target str.
            pattern (Optional[str]):
                Optional. regex str.

        Returns:
            List[Page]:
                A list of Pages.

        """
        if bool(target_string) == bool(pattern):
            raise ValueError(
                "Exactly one of target_string and pattern must be specified."
            )

        found_pages = [
            page
            for page in self.pages
            if (target_string and target_string in page.text)
            or (pattern and re.search(pattern, page.text))
        ]

        return found_pages

    def get_form_field_by_name(self, target_field: str) -> List[FormField]:
        r"""Returns the list of `FormFields` named `target_field`.

        Args:
            target_field (str):
                Required. Target field name.

        Returns:
            List[FormField]:
                A list of `FormField` matching `target_field`.

        """
        target_field = target_field.lower()
        return [
            form_field
            for p in self.pages
            for form_field in p.form_fields
            if target_field in form_field.field_name.lower()
        ]

    def form_fields_to_dict(self) -> Dict[str, Union[str, List[str]]]:
        r"""Returns dictionary of form fields in document.

        Returns:
            Dict[str, Union[str, List[str]]]:
                The Dict of the form fields indexed by type.

        """
        form_fields_dict: Dict[str, Union[str, List[str]]] = {}
        for p in self.pages:
            for form_field in p.form_fields:
                field_name = _bigquery_column_name(form_field.field_name)
                form_fields_dict = _insert_into_dictionary_with_list(
                    form_fields_dict, field_name, form_field.field_value
                )

        return form_fields_dict

    def form_fields_to_bigquery(
        self, dataset_name: str, table_name: str, project_id: Optional[str] = None
    ) -> bigquery.job.LoadJob:
        r"""Adds extracted form fields to a BigQuery table.

        Args:
            dataset_name (str):
                Required. Name of the BigQuery dataset.
            table_name (str):
                Required. Name of the BigQuery table.
            project_id (Optional[str]):
                Optional. Project ID containing the BigQuery table. If not passed, falls back to the default inferred from the environment.
        Returns:
            bigquery.job.LoadJob:
                The BigQuery `LoadJob` for adding the form fields.

        """

        return _dict_to_bigquery(
            self.form_fields_to_dict(),
            dataset_name,
            table_name,
            project_id,
        )

    def get_entity_by_type(self, target_type: str) -> List[Entity]:
        r"""Returns the list of `Entities` of `target_type`.

        Args:
            target_type (str):
                Required. Target entity type.

        Returns:
            List[Entity]:
                A list of `Entity` matching `target_type`.

        """
        return [entity for entity in self.entities if entity.type_ == target_type]

    def entities_to_dict(self) -> Dict[str, Union[str, List[str]]]:
        r"""Returns Dictionary of entities in document.

        Returns:
            Dict:
                The Dict of the entities indexed by type.

        """
        entities_dict: Dict[str, Union[str, List[str]]] = {}
        for entity in self.entities:
            entity_type = _bigquery_column_name(entity.type_)
            entities_dict = _insert_into_dictionary_with_list(
                entities_dict, entity_type, entity.mention_text
            )

        return entities_dict

    def entities_to_bigquery(
        self, dataset_name: str, table_name: str, project_id: Optional[str] = None
    ) -> bigquery.job.LoadJob:
        r"""Adds extracted entities to a BigQuery table.

        Args:
            dataset_name (str):
                Required. Name of the BigQuery dataset.
            table_name (str):
                Required. Name of the BigQuery table.
            project_id (Optional[str]):
                Optional. Project ID containing the BigQuery table. If not passed, falls back to the default inferred from the environment.
        Returns:
            bigquery.job.LoadJob:
                The BigQuery `LoadJob` for adding the entities.

        """

        return _dict_to_bigquery(
            self.entities_to_dict(),
            dataset_name,
            table_name,
            project_id,
        )

    def split_pdf(self, pdf_path: str, output_path: str) -> List[str]:
        r"""Splits local PDF file into multiple PDF files based on output from a Splitter processor.

        Args:
            pdf_path (str):
                Required. The path to the PDF file.
            output_path (str):
                Required. The path to the output directory.
        Returns:
            List[str]:
                A list of output pdf files.
        """
        if self.entities[0].start_page is None or self.entities[0].end_page is None:
            raise ValueError("Entities do not contain start or end pages.")
        output_files: List[str] = []
        input_filename, input_extension = os.path.splitext(os.path.basename(pdf_path))
        with Pdf.open(pdf_path) as pdf:
            for entity in self.entities:
                # Entity types come from the parsed Document and may contain
                # path separators (e.g. "vat/tax_amount") or traversal
                # sequences. Flatten them so the split file stays inside
                # output_path. ":" is also flattened since it is not a valid
                # filename character on Windows.
                subdoc_type = (
                    (entity.type_ or "subdoc")
                    .replace("/", "_")
                    .replace("\\", "_")
                    .replace(":", "_")
                )
                page_range = (
                    f"pg{entity.start_page + 1}"
                    if entity.start_page == entity.end_page
                    else f"pg{entity.start_page + 1}-{entity.end_page + 1}"
                )
                output_filename = (
                    f"{input_filename}_{page_range}_{subdoc_type}{input_extension}"
                )

                subdoc = Pdf.new()
                subdoc.pages.extend(pdf.pages[entity.start_page : entity.end_page + 1])
                subdoc.save(
                    os.path.join(output_path, output_filename),
                    min_version=pdf.pdf_version,
                )

                output_files.append(output_filename)
        return output_files

    def convert_document_to_annotate_file_response(self) -> AnnotateFileResponse:
        r"""Convert OCR data from `Document.proto` to `AnnotateFileResponse.proto` for Vision API.

        Args:
            None.
        Returns:
            AnnotateFileResponse:
                Proto with `TextAnnotations`.
        """
        return AnnotateFileResponse(
            responses=[
                vision_helpers.convert_page_to_annotate_image_response(
                    docai_page, self.text
                )
                for shard in self.shards
                for docai_page in shard.pages
            ]
        )

    def convert_document_to_annotate_file_json_response(self) -> str:
        r"""Convert OCR data from `Document.proto` to JSON str of `AnnotateFileResponse` for Vision API.

        Args:
            None.
        Returns:
            str:
                JSON string of `TextAnnotations`.
        """
        return AnnotateFileResponse.to_json(
            self.convert_document_to_annotate_file_response()
        )

    def export_images(
        self, output_path: str, output_file_prefix: str, output_file_extension: str
    ) -> List[str]:
        r"""Exports images from `Document.entities` to files. Only exports `Portrait` entities.

        Args:
            output_path (str):
                Required. The path to the output directory.
            output_file_prefix (str):
                Required. The output file name prefix.
            output_file_extension (str):
                Required. The output file extension.

                Format: `png`, `jpg`, etc.
        Returns:
            List[str]:
                A list of output image file names.
                Format: `{output_path}/{output_file_prefix}_{index}_{Entity.type_}.{output_file_extension}`
        """
        output_filenames: List[str] = []
        index = 0
        for entity in self.entities:
            if entity.type_ not in constants.IMAGE_ENTITIES or entity.mention_text:
                continue

            image = entity.crop_image(
                documentai_page=self.pages[entity.start_page].documentai_object
            )
            if not image:
                continue

            output_filename = (
                f"{output_file_prefix}_{index}_{entity.type_}.{output_file_extension}"
            )
            image.save(os.path.join(output_path, output_filename))
            output_filenames.append(output_filename)
            index += 1

        return output_filenames

    def export_hocr_str(self, title: str) -> str:
        r"""Exports a string hOCR version of the Document.

            The format for the id of the object follows as such:
                object_{page_index}_...

            For example words will have the following id format:
                word_{page_index}_{block_index}_{paragraph_index}_{line_index}_{word_index}

        Args:
            title (str):
                Required. The title for hocr_page and head.

        Returns:
            str:
                A string hOCR version of the Document
        """
        environment = Environment(
            loader=PackageLoader("google.cloud.documentai_toolbox", "templates"),
            autoescape=True,
        )
        template = environment.get_template("hocr_document_template.xml.j2")
        content = template.render(pages=self.pages, title=title)
        return content

    def to_merged_documentai_document(self) -> documentai.Document:
        r"""Exports a documentai.Document from the wrapped document with shards merged.

        Args:
            None.
        Returns:
            documentai.Document:
                Document with all shards merged and text offsets applied.
        """
        if len(self.shards) == 1:
            return self.shards[0]

        merged_document = documentai.Document(text=self.text, pages=[], entities=[])
        for shard in self.shards:
            modified_shard = copy.deepcopy(shard)

            _apply_text_offset(
                documentai_object=modified_shard,
                text_offset=int(modified_shard.shard_info.text_offset),
            )
            merged_document.pages.extend(modified_shard.pages)
            merged_document.entities.extend(modified_shard.entities)

        return merged_document
