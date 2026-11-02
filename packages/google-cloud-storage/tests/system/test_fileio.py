# coding=utf-8
# Copyright 2021 Google LLC
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


import pytest

from google.cloud.storage.fileio import CHUNK_SIZE_MULTIPLE

from .test_blob import _check_blob_hash


def test_blobwriter_and_blobreader(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob("LargeFile")

    # Test BlobWriter works.
    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        with blob.open("wb", chunk_size=256 * 1024, if_generation_match=0) as writer:
            writer.write(file_obj.read(100))
            writer.write(file_obj.read(256 * 1024))
            writer.write(file_obj.read())
        blobs_to_delete.append(blob)

    blob.reload()
    _check_blob_hash(blob, info)

    # Test BlobReader read and seek behave identically to filesystem file.
    with open(info["path"], "rb") as file_obj:
        with blob.open("rb", chunk_size=256 * 1024) as reader:
            assert file_obj.read(100) == reader.read(100)
            assert file_obj.read(256 * 1024) == reader.read(256 * 1024)
            reader.seek(20)
            file_obj.seek(20)
            assert file_obj.read(256 * 1024 * 2) == reader.read(256 * 1024 * 2)
            assert file_obj.read() == reader.read()
            # End of file reached; further reads should be blank but not
            # raise an error.
            assert reader.read() == b""


def test_blobwriter_and_blobreader_text_mode(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    blob = shared_bucket.blob("MultibyteTextFile")

    # Construct a multibyte text_data sample file.
    base_multibyte_text_string = "abcde あいうえお line: "
    text_data = "\n".join([base_multibyte_text_string + str(x) for x in range(100)])

    # Test text BlobWriter works.
    with blob.open("wt", if_generation_match=0) as writer:
        writer.write(text_data[:100])
        writer.write(text_data[100:])
    blobs_to_delete.append(blob)

    # Test text BlobReader read and seek to 0. Seeking to an non-0 byte on a
    # multibyte text stream is not safe in Python but the API expects
    # seek() to work regadless.
    with blob.open("rt") as reader:
        # This should produce 100 characters, not 100 bytes.
        assert text_data[:100] == reader.read(100)
        assert 0 == reader.seek(0)
        assert reader.read() == text_data


def test_blobwriter_exit(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    blob = shared_bucket.blob("NeverUploaded")

    # no-op when nothing was uploaded yet
    with pytest.raises(ValueError, match="SIGTERM received"):
        with blob.open("wb") as writer:
            writer.write(b"first chunk")  # not yet uploaded
            raise ValueError("SIGTERM received")  # no upload to cancel in __exit__
    # blob should not exist
    assert not blob.exists()

    # unhandled exceptions should cancel the upload
    with pytest.raises(ValueError, match="SIGTERM received"):
        with blob.open("wb", chunk_size=CHUNK_SIZE_MULTIPLE) as writer:
            writer.write(b"first chunk")  # not yet uploaded
            writer.write(bytes(CHUNK_SIZE_MULTIPLE))  # uploaded
            raise ValueError("SIGTERM received")  # upload is cancelled in __exit__
    # blob should not exist
    assert not blob.exists()

    # handled exceptions should not cancel the upload
    with blob.open("wb", chunk_size=CHUNK_SIZE_MULTIPLE) as writer:
        writer.write(b"first chunk")  # not yet uploaded
        writer.write(bytes(CHUNK_SIZE_MULTIPLE))  # uploaded
        try:
            raise ValueError("This is fine")
        except ValueError:
            pass  # no exception context passed to __exit__
    blobs_to_delete.append(blob)
    # blob should have been uploaded
    assert blob.exists()


def test_blobreader_w_raw_download(
    shared_bucket,
    blobs_to_delete,
    file_data,
):
    blob = shared_bucket.blob("LargeFile")
    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        with blob.open("wb", chunk_size=256 * 1024, if_generation_match=0) as writer:
            writer.write(file_obj.read())
        blobs_to_delete.append(blob)

    # Test BlobReader read and seek handles raw downloads.
    with open(info["path"], "rb") as file_obj:
        with blob.open("rb", chunk_size=256 * 1024, raw_download=True) as reader:
            reader.seek(0)
            file_obj.seek(0)
            assert file_obj.read() == reader.read()
            # End of file reached; further reads should be blank but not
            # raise an error.
            assert reader.read() == b""
