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
"""Google Cloud Storage utilities."""

import os
import re
from typing import Dict, List, Optional, Tuple

from google.api_core.gapic_v1 import client_info

from google.cloud import (  # type: ignore[attr-defined]
    documentai,
    documentai_toolbox,
    storage,
)
from google.cloud.documentai_toolbox import constants


def _get_client_info(module: Optional[str] = None) -> client_info.ClientInfo:
    r"""Returns a custom user agent header.

    Returns:
        client_info.ClientInfo.

    """
    client_library_version = documentai_toolbox.__version__

    if module:
        client_library_version = f"{client_library_version}-{module}"

    return client_info.ClientInfo(
        client_library_version=client_library_version,
        user_agent=f"{constants.USER_AGENT_PRODUCT}/{client_library_version}",
    )


def _get_storage_client(module: Optional[str] = None) -> storage.Client:
    r"""Returns a Storage client with custom user agent header.

    Returns:
        storage.Client.

    """
    return storage.Client(client_info=_get_client_info(module))


def get_blobs(
    gcs_uri: Optional[str] = None,
    gcs_bucket_name: Optional[str] = None,
    gcs_prefix: Optional[str] = "/",
    module: Optional[str] = "get-bytes",
) -> List[storage.blob.Blob]:
    r"""Returns a list of blobs from Cloud Storage.

    Args:
        gcs_uri (Optional[str]):
            Optional: The fully-qualified Google Cloud Storage URI.
            You must provide either `gcs_uri` or both `gcs_bucket_name` and `gcs_prefix`.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/`
        gcs_bucket_name (Optional[str]):
            Optional. The name of the gcs bucket.
            You must provide either `gcs_uri` or both `gcs_bucket_name` and `gcs_prefix`.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_bucket_name=`bucket`.
        gcs_prefix (Optional[str]):
            Optional. The prefix of the files in the target_folder.
            You must provide either `gcs_uri` or both `gcs_bucket_name` and `gcs_prefix`.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_prefix=`{optional_folder}/{target_folder}`.
        module (Optional[str]):
            Optional. The module for a custom user agent header.
    Returns:
        List[storage.blob.Blob]:
            A list of the blobs in the Cloud Storage path.

    """
    if bool(gcs_uri) == (bool(gcs_bucket_name) and bool(gcs_prefix)):
        raise ValueError(
            "You must provide either `gcs_uri` or both `gcs_bucket_name` and `gcs_prefix`."
        )

    if gcs_uri:
        gcs_bucket_name, gcs_prefix = split_gcs_uri(gcs_uri)

    if gcs_prefix is None:
        raise TypeError("gcs_prefix cannot be None")
    if re.match(constants.FILE_CHECK_REGEX, gcs_prefix):
        raise ValueError("gcs_prefix cannot contain file types")

    storage_client = _get_storage_client(module=module)
    return storage_client.list_blobs(gcs_bucket_name, prefix=gcs_prefix)


def get_bytes(gcs_bucket_name: str, gcs_prefix: str) -> List[bytes]:
    r"""Returns a list of bytes of json files from Cloud Storage.

    Args:
        gcs_bucket_name (str):
            Required. The name of the gcs bucket.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_bucket_name=`bucket`.
        gcs_prefix (str):
            Required. The prefix of the json files in the target_folder

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_prefix=`{optional_folder}/{target_folder}`.
    Returns:
        List[bytes]:
            A list of bytes.
    """
    return [
        blob.download_as_bytes()
        for blob in get_blobs(gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix)
        if blob.name.endswith(constants.JSON_EXTENSION)
        or blob.content_type == constants.JSON_MIMETYPE
    ]


def get_blob(
    gcs_uri: str,
    module: Optional[str] = "get-bytes",
) -> storage.blob.Blob:
    r"""Returns a blob from Cloud Storage.

    Args:
        gcs_uri (str):
            Required: The fully-qualified Google Cloud Storage URI.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/{target_file}.{ext}`
        module (Optional[str]):
            Optional. The module for a custom user agent header.
    Returns:
        storage.blob.Blob:
            The blob in the Cloud Storage path.
    """
    if not re.match(constants.FILE_CHECK_REGEX, gcs_uri):
        raise ValueError("gcs_uri must link to a single file.")

    # google-cloud-storage >= 3.0.0
    if hasattr(storage.Blob, "from_uri"):
        return storage.Blob.from_uri(gcs_uri, _get_storage_client(module=module))

    return storage.Blob.from_string(gcs_uri, _get_storage_client(module=module))


def split_gcs_uri(gcs_uri: str) -> Tuple[str, str]:
    r"""Splits a Cloud Storage uri into the bucket_name and prefix.

    Args:
        gcs_uri (str):
            Required. The full Cloud Storage URI.

            Format: `gs://{bucket_name}/{gcs_prefix}`.
    Returns:
        Tuple[str, str]:
            The Cloud Storage Bucket and Prefix.

    """
    matches = re.match("gs://(.*?)/(.*)", gcs_uri)

    if not matches:
        raise ValueError(
            "gcs_uri must follow format 'gs://{bucket_name}/{gcs_prefix}'."
        )

    bucket, prefix = matches.groups()
    return bucket, prefix


def create_gcs_uri(gcs_bucket_name: str, gcs_prefix: str) -> str:
    r"""Creates a Cloud Storage uri from the bucket_name and prefix.

    Args:
        gcs_bucket_name (str):
            Required. The name of the gcs bucket.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_bucket_name=`bucket`.
        gcs_prefix (str):
            Required. The prefix of the files in the target_folder.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_prefix=`{optional_folder}/{target_folder}`.
    Returns:
        str
            The full Cloud Storage uri.
            Format: `gs://{gcs_bucket_name}/{gcs_prefix}`

    """
    return f"gs://{gcs_bucket_name}/{gcs_prefix}"


def list_gcs_document_tree(
    gcs_bucket_name: str, gcs_prefix: str
) -> Dict[str, List[str]]:
    r"""Returns a list path to files in Cloud Storage folder.

    Args:
        gcs_bucket_name (str):
            Required. The name of the gcs bucket.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_bucket_name=`bucket`.
        gcs_prefix (str):
            Required. The prefix of the json files in the target_folder.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_prefix=`{optional_folder}/{target_folder}`.
    Returns:
        Dict[str, List[str]]:
            The paths to documents in `gs://{gcs_bucket_name}/{gcs_prefix}`.

    """
    file_check = re.match(constants.FILE_CHECK_REGEX, gcs_prefix)

    if file_check is not None:
        raise ValueError("gcs_prefix cannot contain file types")

    storage_client = _get_storage_client(module="list-document")
    blob_list = storage_client.list_blobs(gcs_bucket_name, prefix=gcs_prefix)

    path_list: Dict[str, List[str]] = {}

    for blob in blob_list:
        directory, file_name = os.path.split(blob.name)
        path_list.setdefault(directory, []).append(file_name)

    return path_list


def print_gcs_document_tree(
    gcs_bucket_name: str, gcs_prefix: str, files_to_display: int = 4
) -> None:
    r"""Prints a tree of filenames in a Cloud Storage folder.

    Args:
        gcs_bucket_name (str):
            Required. The name of the gcs bucket.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_bucket_name=`bucket`.
        gcs_prefix (str):
            Required. The prefix of the json files in the target_folder.

            Format: `gs://{bucket_name}/{optional_folder}/{target_folder}/` where gcs_prefix=`{optional_folder}/{target_folder}`.
        files_to_display (int):
            Optional. The amount of files to display. Default is `4`.
    Returns:
        None.
    """
    FILENAME_TREE_MIDDLE = "├──"
    FILENAME_TREE_LAST = "└──"

    path_list = list_gcs_document_tree(
        gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix
    )

    for directory, files in path_list.items():
        print(directory)
        dir_size = len(files)
        for idx, file_name in enumerate(files):
            if idx == dir_size - 1:
                if dir_size > files_to_display:
                    print("│  ....")
                print(f"{FILENAME_TREE_LAST}{file_name}\n")
                break
            if idx <= files_to_display:
                print(f"{FILENAME_TREE_MIDDLE}{file_name}")


def create_batches(
    gcs_bucket_name: str, gcs_prefix: str, batch_size: int = constants.BATCH_MAX_FILES
) -> List[documentai.BatchDocumentsInputConfig]:
    """Create batches of documents in Cloud Storage to process with `batch_process_documents()`.

    Args:
        gcs_bucket_name (str):
            Required. The name of the gcs bucket.

            Format: `gs://bucket/optional_folder/target_folder/` where gcs_bucket_name=`bucket`.
        gcs_prefix (str):
            Required. The prefix of the json files in the `target_folder`

            Format: `gs://bucket/optional_folder/target_folder/` where gcs_prefix=`optional_folder/target_folder`.
        batch_size (int):
            Optional. Size of each batch of documents. Default is `50`.

    Returns:
        List[documentai.BatchDocumentsInputConfig]:
            A list of `BatchDocumentsInputConfig`, each corresponding to one batch.
    """
    if batch_size > constants.BATCH_MAX_FILES:
        raise ValueError(
            f"Batch size must be less than {constants.BATCH_MAX_FILES}. You provided {batch_size}."
        )

    storage_client = _get_storage_client(module="create-batches")
    blob_list = storage_client.list_blobs(gcs_bucket_name, prefix=gcs_prefix)

    batches: List[documentai.BatchDocumentsInputConfig] = []
    batch: List[documentai.GcsDocument] = []

    for blob in blob_list:
        # Skip Directories
        if blob.name.endswith("/"):
            continue

        if blob.content_type not in constants.VALID_MIME_TYPES:
            print(f"Skipping file {blob.name}. Invalid Mime Type {blob.content_type}.")
            continue

        if int(blob.size) > constants.BATCH_MAX_FILE_SIZE:
            print(
                f"Skipping file {blob.name}. File size must be less than {constants.BATCH_MAX_FILE_SIZE} bytes. File size is {blob.size} bytes."
            )
            continue

        batch.append(
            documentai.GcsDocument(
                gcs_uri=create_gcs_uri(gcs_bucket_name, blob.name),
                mime_type=blob.content_type,
            )
        )

        if len(batch) == batch_size:
            batches.append(
                documentai.BatchDocumentsInputConfig(
                    gcs_documents=documentai.GcsDocuments(documents=batch)
                )
            )
            batch = []

    if batch:
        # Append the last batch, which could be less than `batch_size`
        batches.append(
            documentai.BatchDocumentsInputConfig(
                gcs_documents=documentai.GcsDocuments(documents=batch)
            )
        )

    return batches


def upload_file(
    gcs_output_directory: str,
    file_name: str,
    file_content: str,
    content_type: str = constants.JSON_MIMETYPE,
    module: Optional[str] = "upload-file",
) -> None:
    r"""Uploads the converted docproto to gcs.

    Args:
        gcs_output_directory (str):
            Required: The Google Cloud Storage directory to output the file.

            Format: `gs://{bucket}/{optional_folder}`
        file_name (str):
            Required. The name of the file with extension.
        file_content (str):
            Required. The docproto file in string format.
        content_type (str):
            Optional. The Media Type (MIME Type) of the file to upload.
            Default: `application/json`

    Returns:
        None.

    """
    gcs_bucket_name, gcs_prefix = split_gcs_uri(gcs_output_directory)

    if re.match(constants.FILE_CHECK_REGEX, gcs_prefix):
        raise ValueError("gcs_prefix cannot contain file types")

    storage_client = _get_storage_client(module=module)

    bucket = storage_client.bucket(gcs_bucket_name)
    blob = bucket.blob(os.path.join(gcs_prefix, file_name))
    blob.upload_from_string(data=file_content, content_type=content_type)

    print(f"Uploaded: {blob.name}", end="\r")
