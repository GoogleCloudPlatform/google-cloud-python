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
"""Document.proto converters."""

import os
import time
from concurrent import futures
from typing import Dict, List, Optional, Set, Tuple

from google.api_core.client_options import ClientOptions

from google.cloud import documentai
from google.cloud.documentai_toolbox import constants
from google.cloud.documentai_toolbox.converters.config import bbox_conversion
from google.cloud.documentai_toolbox.converters.config.block import Block
from google.cloud.documentai_toolbox.utilities import gcs_utilities


def _get_base_ocr(
    project_id: str,
    location: str,
    processor_id: str,
    file_bytes: bytes,
    mime_type: str,
    field_mask: Optional[str] = None,
    processor_version_id: Optional[str] = None,
) -> documentai.Document:
    r"""Returns `documentai.Document` from OCR processor.

    Args:
        project_id (str):
            Required.
        location (str):
            Required.
        processor_id (str):
            Required.
        file_bytes (bytes):
            Required. The bytes of the original pdf.
        mime_type (str):
            Required. Usually `application/pdf`.
        field_mask (Optional[str]):
            Optional.  Specifies which fields to include in the `Document` output.
        processor_version_id (Optional[str]):
            Optional. Specifies the processor version to use.

    Returns:
        documentai.Document:
            A documentai.Document from OCR processor.

    """
    client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(
            api_endpoint=f"{location}-documentai.googleapis.com"
        ),
        client_info=gcs_utilities._get_client_info(),
    )

    name = (
        client.processor_version_path(
            project_id, location, processor_id, processor_version_id
        )
        if processor_version_id
        else client.processor_path(project_id, location, processor_id)
    )

    result = client.process_document(
        request=documentai.ProcessRequest(
            name=name,
            raw_document=documentai.RawDocument(
                content=file_bytes, mime_type=mime_type
            ),
            field_mask=field_mask,
        )
    )
    return result.document


def _get_entity_content(
    blocks: List[Block], docproto: documentai.Document
) -> List[documentai.Document.Entity]:
    r"""Returns a list of documentai.Document entities.

    Args:
        blocks (List[Block]):
            Required.List of blocks from original annotation.
        docproto (documentai.Document):
            Required.The ocr docproto.
    Returns:
        List[documentai.Document.Entity]:
            A list of documentai.Document entities.
    """
    entities: List[documentai.Document.Entity] = []

    for entity_id, block in enumerate(blocks):
        docai_entity = documentai.Document.Entity(
            type=block.type_,
            mention_text=block.text,
            id=str(entity_id),
            confidence=block.confidence if block.confidence else None,
        )

        if block.bounding_box:
            bounding_box = bbox_conversion.convert_bbox_to_docproto_bbox(block)
            page_number = int(block.page_number) - 1 if block.page_number else 0
            page = docproto.pages[page_number]

            docai_entity.text_anchor = bbox_conversion.get_text_anchor_in_bbox(
                bounding_box, page
            )
            docai_entity.text_anchor.content = block.text
            docai_entity.page_anchor = documentai.Document.PageAnchor(
                page_refs=[
                    documentai.Document.PageAnchor.PageRef(bounding_poly=bounding_box)
                ]
            )

        entities.append(docai_entity)

    return entities


def _convert_to_docproto_with_config(
    annotated_bytes: bytes,
    config_bytes: bytes,
    document_bytes: bytes,
    project_id: str,
    location: str,
    processor_id: str,
    wait_time: int = 1,
    max_retries: int = 6,
    name: str = "",
) -> Optional[documentai.Document]:
    r"""Converts a single document to docproto.

    Args:
        annotated_bytes (bytes):
            Required.The bytes of the annotated data.
        config_bytes (bytes):
            Required.The bytes of config data.
        document_bytes (bytes):
            Required. The bytes of the original pdf.
        project_id (str):
            Required.
        location (str):
            Required.
        processor_id (str):
            Required.
        wait_time (str):
            Optional. The number of seconds needed to wait if an error occured.
        max_retries (str):
            Optional. Maximum times to retry before stopping.
        name (str):
            Optional. Name of the document to be converted. This is used for logging.

    Returns:
        Optional[documentai.Document]:
            documentai.Document object. Returns None if the conversion fails.

    TODO: Depending on input type you will need to modify load_blocks.
          Depending on input format, if your annotated data is not separate from the base OCR data you will need to modify _get_entity_content
          Depending on input BoundingBox, if the input BoundingBox object is like https://cloud.google.com/document-ai/docs/reference/rest/v1/Document#BoundingPoly then you will need to
            modify bbox_conversion.convert_bbox_to_docproto_bbox since the objects are different.
    """
    for i in range(max_retries):
        try:
            base_docproto = _get_base_ocr(
                project_id=project_id,
                location=location,
                processor_id=processor_id,
                file_bytes=document_bytes,
                mime_type=constants.PDF_MIMETYPE,
            )

            blocks = Block.load_blocks_from_schema(
                input_data=annotated_bytes,
                input_config=config_bytes,
                base_docproto=base_docproto,
            )

            base_docproto.entities = _get_entity_content(blocks, base_docproto)

            print(f"Converted: {name}", end="\r")
            return base_docproto

        except Exception as e:
            print(e)
            print(f"Could Not Convert {name}\nretrying")
            time.sleep(wait_time + i)

    return None


def _get_bytes(
    gcs_uri: str,
    annotation_file_prefix: str,
    config_file_prefix: str,
    config_path: Optional[str] = None,
) -> Tuple[bytes, bytes, bytes, str]:
    r"""Downloads documents and returns them as bytes.

    Args:
        gcs_uri (str):
            Required: The fully-qualified Google Cloud Storage URI.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}`
        annotation_file_prefix (str):
            Required. The prefix to search for annotation file.
        config_file_prefix (str):
            Required. The prefix to search for config file.
        config_path (str):
            Optional. The gcs path to a config file. This should be used when there is a single config file.

    Returns:
        Tuple[bytes, bytes, bytes, str].
        Annotation, Document PDF, Config File, Directory Name.

    """
    blobs = gcs_utilities.get_blobs(gcs_uri=gcs_uri)

    try:
        for blob in blobs:
            if blob.name.endswith("/"):
                continue
            file_name = os.path.basename(blob.name)
            if annotation_file_prefix in file_name:
                annotation_blob = blob
            elif config_file_prefix in file_name:
                metadata_blob = blob
            elif constants.PDF_EXTENSION in file_name:
                doc_blob = blob

        if config_path:
            metadata_blob = gcs_utilities.get_blob(config_path)

        directory_name = os.path.basename(gcs_uri)
        print(f"Downloaded: {directory_name}", end="\r")

        return (
            annotation_blob.download_as_bytes(),
            doc_blob.download_as_bytes(),
            metadata_blob.download_as_bytes(),
            directory_name,
        )
    except Exception as e:
        raise e


def _get_files(
    blob_list: List, config_path: Optional[str] = None
) -> List[futures.Future]:
    r"""Returns a list of Futures of documents as bytes.

    Args:
        blob_list (List[storage.blob.Blob]):
            Required. The list of Futures from _get_files.
        config_path (Optional[str]):
            Optional. The configuration path.
    Returns:
        List[futures.Future]:
            A list of Futures.

    """

    download_pool = futures.ThreadPoolExecutor(max_workers=10)

    dirs = {
        gcs_utilities.create_gcs_uri(blob.bucket.name, os.path.dirname(blob.name))
        for blob in blob_list
    }

    print("-------- Downloading Started --------")
    return [
        download_pool.submit(
            _get_bytes,
            dir,
            "annotation",
            "config",
            config_path,
        )
        for dir in dirs
    ]


def _get_docproto_files(
    futures_list: List[futures.Future],
    project_id: str,
    location: str,
    processor_id: str,
) -> Tuple[Dict[str, str], Set[str], List[str]]:
    r"""Returns converted document.proto, unique entity types, and documents that were not converted.

    Args:
        futures_list (List[futures.Future]):
            Required. The list of Futures from _get_files.
        project_id (str):
            Required. The project ID.
        location (str):
            Required. The location.
        processor_id (str):
            Required. The processor ID.

    Returns:
        Tuple[dict, set, list]:
            Converted document.proto, unique entity types, and documents that were not converted.

    """
    files: Dict[str, str] = {}
    unique_types: Set[str] = set()
    did_not_convert: List[str] = []

    for future in futures_list:
        annotated_bytes, document_bytes, config_bytes, name = future.result()
        docproto = _convert_to_docproto_with_config(
            annotated_bytes=annotated_bytes,
            document_bytes=document_bytes,
            config_bytes=config_bytes,
            project_id=project_id,
            location=location,
            processor_id=processor_id,
            name=name,
        )

        if docproto is None:
            did_not_convert.append(name)
            continue

        unique_types.update(entity.type_ for entity in docproto.entities)
        files[name] = documentai.Document.to_json(docproto)

    return files, unique_types, did_not_convert


def _upload(
    files: dict,
    gcs_output_path: str,
) -> None:
    r"""Upload converted document.proto to gcs location.

    Args:
        files (dict):
            Required. The document.proto files to upload.
        gcs_output_path (str):
            Required. The gcs path to the folder to upload the converted docproto documents to.

            Format: `gs://{bucket}/{optional_folder}`
    Returns:
        None.

    """
    upload_pool = futures.ThreadPoolExecutor(max_workers=10)

    print("-------- Uploading Started --------")
    uploads = [
        upload_pool.submit(
            gcs_utilities.upload_file,
            gcs_output_path,
            f"{name}{constants.JSON_EXTENSION}",
            content,
        )
        for name, content in files.items()
        if "config" not in name and "annotations" not in name
    ]

    futures.wait(uploads)


def convert_from_config(
    project_id: str,
    location: str,
    processor_id: str,
    gcs_input_path: str,
    gcs_output_path: str,
    config_path: Optional[str] = None,
) -> None:
    r"""Converts all documents in gcs_input_path to docproto using configs.

    Args:
        project_id (str):
            Required.
        location (str):
            Required.
        processor_id (str):
            Required.
        gcs_input_path (str):
            Required. The gcs path to the folder containing all non docproto documents.

            Format: `gs://{bucket}/{optional_folder}`
        gcs_output_path (str):
            Required. The gcs path to the folder to upload the converted docproto documents to.

            Format: `gs://{bucket}/{optional_folder}`
        config_path:
            Optional. The gcs path to a single config file. This will work if all the documents in gcs_input_path are of the same config type.

            Format: `gs://{bucket}/{optional_folder}/config.json`
    Returns:
        None.

    """
    blob_list = gcs_utilities.get_blobs(
        gcs_uri=gcs_input_path, module="config-converter"
    )
    downloads = _get_files(
        blob_list=blob_list,
        config_path=config_path,
    )

    futures_list, _ = futures.wait(downloads)

    print("-------- Finished Downloading --------")

    print("-------- Converting Started --------")
    files, labels, did_not_convert = _get_docproto_files(
        list(futures_list), project_id, location, processor_id
    )

    print("-------- Finished Converting --------")
    if did_not_convert:
        print(f"Did not convert {len(did_not_convert)} documents")
        print(did_not_convert)

    _upload(files, gcs_output_path)

    print("-------- Finished Uploading --------")
    print("-------- Schema Information --------")
    print(f"Unique Entity Types: {labels}")
