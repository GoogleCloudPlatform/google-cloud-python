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

import datetime
import gzip
import io
import os
import tempfile
import uuid
import warnings

import mock
import pytest
from google.api_core import exceptions

from google.cloud.storage._helpers import _base64_md5hash
from google.cloud.storage.exceptions import DataCorruption

from . import _helpers

encryption_key = "b23ff11bba187db8c37077e6af3b25b8"


def _check_blob_hash(blob, info):
    md5_hash = blob.md5_hash
    if not isinstance(md5_hash, bytes):
        md5_hash = md5_hash.encode("utf-8")

    assert md5_hash == info["hash"]


def test_large_file_write_from_stream_w_user_provided_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")

    info = file_data["big_9MiB"]
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(file_obj, crc32c_checksum_value="20tD7w==")
        blobs_to_delete.append(blob)


def test_large_file_write_from_stream_w_user_provided_wrong_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")

    info = file_data["big_9MiB"]
    with pytest.raises(exceptions.BadRequest) as excep_info:
        with open(info["path"], "rb") as file_obj:
            blob.upload_from_file(file_obj, crc32c_checksum_value="A0tD7w==")
            blobs_to_delete.append(blob)
    assert excep_info.value.code == 400


def test_touch_and_write_large_file_w_user_provided_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")
    blob.upload_from_string(b"")
    blob.reload()

    info = file_data["big_9MiB"]
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(file_obj, crc32c_checksum_value="20tD7w==")
        blobs_to_delete.append(blob)


def test_large_file_write_from_stream(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")

    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(file_obj)
        blobs_to_delete.append(blob)

    _check_blob_hash(blob, info)


def test_large_file_write_from_stream_w_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")

    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(file_obj, checksum="crc32c")
        blobs_to_delete.append(blob)

    _check_blob_hash(blob, info)


def test_large_file_write_from_stream_w_failed_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")

    # Intercept the digest processing at the last stage and replace it
    # with garbage.  This is done with a patch to monkey-patch the
    # resumable media library's checksum # processing;
    # it does not mock a remote interface like a unit test would.
    # The # remote API is still exercised.
    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        with mock.patch(
            "google.cloud.storage._media._helpers.prepare_checksum_digest",
            return_value="FFFFFF==",
        ):
            with pytest.raises((DataCorruption, exceptions.BadRequest)):
                blob.upload_from_file(file_obj, checksum="crc32c")

    assert not blob.exists()


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Test does not yet support endpoint override",
)
def test_large_file_write_from_stream_w_encryption_key(
    storage_client,
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob("LargeFile", encryption_key=encryption_key)

    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(file_obj)
        blobs_to_delete.append(blob)

    _check_blob_hash(blob, info)

    blob_without_key = shared_bucket.blob("LargeFile")
    with tempfile.TemporaryFile() as tmp:
        with pytest.raises(exceptions.BadRequest):
            storage_client.download_blob_to_file(blob_without_key, tmp)

    with tempfile.NamedTemporaryFile() as temp_f:
        with open(temp_f.name, "wb") as file_obj:
            storage_client.download_blob_to_file(blob, file_obj)

        with open(temp_f.name, "rb") as file_obj:
            md5_temp_hash = _base64_md5hash(file_obj)

    assert md5_temp_hash == info["hash"]


def test_small_file_write_from_filename(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"SmallFile{uuid.uuid4().hex}")

    info = file_data["simple"]
    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)

    _check_blob_hash(blob, info)


def test_small_file_write_from_filename_with_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"SmallFile{uuid.uuid4().hex}")

    info = file_data["simple"]
    blob.upload_from_filename(info["path"], checksum="crc32c")
    blobs_to_delete.append(blob)

    _check_blob_hash(blob, info)


def test_small_file_write_from_filename_with_failed_checksum(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"SmallFile{uuid.uuid4().hex}")

    info = file_data["simple"]
    # Intercept the digest processing at the last stage and replace
    # it with garbage
    with mock.patch(
        "google.cloud.storage._media._helpers.prepare_checksum_digest",
        return_value="FFFFFF==",
    ):
        with pytest.raises(exceptions.BadRequest):
            blob.upload_from_filename(info["path"], checksum="crc32c")

    assert not blob.exists()


def test_blob_crud_w_user_project(
    storage_client,
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
    user_project,
):
    gen1_payload = b"gen1"
    with_user_project = storage_client.bucket(
        shared_bucket.name, user_project=user_project
    )
    blob = with_user_project.blob("SmallFile")

    info = file_data["simple"]
    with open(info["path"], mode="rb") as to_read:
        gen0_payload = to_read.read()

    # Exercise 'objects.insert' w/ userProject.
    blob.upload_from_filename(info["path"])
    gen0 = blob.generation
    etag0 = blob.etag

    # Upload a second generation of the blob
    blob.upload_from_string(gen1_payload)
    gen1 = blob.generation
    etag1 = blob.etag

    blob0 = with_user_project.blob("SmallFile", generation=gen0)
    blob1 = with_user_project.blob("SmallFile", generation=gen1)

    # Exercise 'objects.get' w/ generation
    blob1 = with_user_project.get_blob(blob.name)
    assert blob1.generation == gen1
    assert blob1.etag == etag1
    blob0 = with_user_project.get_blob(blob.name, generation=gen0)
    assert blob0.generation == gen0
    assert blob0.etag == etag0

    try:
        # Exercise 'objects.get' (metadata) w/ userProject.
        assert blob.exists()
        blob.reload()

        # Exercise 'objects.get' (media) w/ userProject.
        blob0 = with_user_project.blob("SmallFile", generation=gen0)
        blob1 = with_user_project.blob("SmallFile", generation=gen1)
        assert blob0.etag is None
        assert blob1.etag is None
        assert blob0.download_as_bytes() == gen0_payload
        assert blob1.download_as_bytes() == gen1_payload
        assert blob0.etag == etag0
        assert blob1.etag == etag1

        # Exercise 'objects.patch' w/ userProject.
        blob0.content_language = "en"
        blob0.patch()
        assert blob0.content_language == "en"
        assert blob1.content_language is None

        # Exercise 'objects.update' w/ userProject.
        metadata = {"foo": "Foo", "bar": "Bar"}
        blob0.metadata = metadata
        blob0.update()
        assert blob0.metadata == metadata
        assert blob1.metadata is None

    finally:
        # Exercise 'objects.delete' (metadata) w/ userProject.
        blobs = storage_client.list_blobs(
            with_user_project, prefix=blob.name, versions=True
        )
        assert [each.generation for each in blobs] == [gen0, gen1]

        blob0.delete()
        blobs = storage_client.list_blobs(
            with_user_project, prefix=blob.name, versions=True
        )
        assert [each.generation for each in blobs] == [gen1]

        blob1.delete()


def test_blob_crud_w_etag_match(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    wrong_etag = "kittens"

    blob = shared_bucket.blob("SmallFile")

    info = file_data["simple"]
    with open(info["path"], mode="rb") as to_read:
        payload = to_read.read()

    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)
    etag = blob.etag

    fresh_blob = shared_bucket.blob("SmallFile")

    # Exercise 'objects.get' (metadata) w/ etag match.
    with pytest.raises(exceptions.PreconditionFailed):
        fresh_blob.exists(if_etag_match=wrong_etag)

    with pytest.raises(exceptions.NotModified):
        fresh_blob.exists(if_etag_not_match=etag)

    assert fresh_blob.exists(if_etag_match=etag)
    assert fresh_blob.exists(if_etag_not_match=wrong_etag)

    with pytest.raises(exceptions.PreconditionFailed):
        fresh_blob.reload(if_etag_match=wrong_etag)

    with pytest.raises(exceptions.NotModified):
        fresh_blob.reload(if_etag_not_match=etag)

    fresh_blob.reload(if_etag_match=etag)  # no raise
    fresh_blob.reload(if_etag_not_match=wrong_etag)  # no raise

    # Exercise 'objects.get' (media) w/ etag match.
    assert fresh_blob.download_as_bytes(if_etag_match=etag) == payload

    with pytest.raises(exceptions.PreconditionFailed):
        fresh_blob.download_as_bytes(if_etag_match=wrong_etag)

    with pytest.raises(exceptions.NotModified):
        fresh_blob.download_as_bytes(if_etag_not_match=etag)


def test_blob_crud_w_generation_match(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    wrong_generation_number = 6
    wrong_metageneration_number = 9
    gen1_payload = b"gen1"

    blob = shared_bucket.blob("SmallFile")

    info = file_data["simple"]
    with open(info["path"], mode="rb") as to_read:
        gen0_payload = to_read.read()

    blob.upload_from_filename(info["path"])
    gen0 = blob.generation

    # Upload a second generation of the blob
    blob.upload_from_string(gen1_payload)
    gen1 = blob.generation

    blob0 = shared_bucket.blob("SmallFile", generation=gen0)
    blob1 = shared_bucket.blob("SmallFile", generation=gen1)

    try:
        # Exercise 'objects.get' (metadata) w/ generation match.
        with pytest.raises(exceptions.PreconditionFailed):
            blob.exists(if_generation_match=wrong_generation_number)

        assert blob.exists(if_generation_match=gen1)

        with pytest.raises(exceptions.PreconditionFailed):
            blob.reload(if_metageneration_match=wrong_metageneration_number)

        blob.reload(if_generation_match=gen1)

        # Exercise 'objects.get' (media) w/ generation match.
        assert blob0.download_as_bytes(if_generation_match=gen0) == gen0_payload
        assert blob1.download_as_bytes(if_generation_not_match=gen0) == gen1_payload

        # Exercise 'objects.patch' w/ generation match.
        blob0.content_language = "en"
        blob0.patch(if_generation_match=gen0)

        assert blob0.content_language == "en"
        assert blob1.content_language is None

        # Exercise 'objects.update' w/ generation match.
        metadata = {"foo": "Foo", "bar": "Bar"}
        blob0.metadata = metadata
        blob0.update(if_generation_match=gen0)

        assert blob0.metadata == metadata
        assert blob1.metadata is None
    finally:
        # Exercise 'objects.delete' (metadata) w/ generation match.
        with pytest.raises(exceptions.PreconditionFailed):
            blob0.delete(if_metageneration_match=wrong_metageneration_number)

        blob0.delete(if_generation_match=gen0)
        blob1.delete(if_metageneration_not_match=wrong_metageneration_number)


def test_blob_acl_w_user_project(
    storage_client,
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
    user_project,
):
    with_user_project = storage_client.bucket(
        shared_bucket.name, user_project=user_project
    )
    blob = with_user_project.blob(f"SmallFile{uuid.uuid4().hex}")

    info = file_data["simple"]

    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)

    # Exercise blob ACL w/ userProject
    acl = blob.acl
    acl.reload()
    acl.all().grant_read()
    acl.save()
    assert "READER" in acl.all().get_roles()

    del acl.entities["allUsers"]
    acl.save()
    assert not acl.has_entity("allUsers")


def test_blob_acl_w_metageneration_match(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    wrong_metageneration_number = 9
    wrong_generation_number = 6

    blob = shared_bucket.blob("FilePatchACL")
    info = file_data["simple"]
    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)

    # Exercise blob ACL with metageneration/generation match
    acl = blob.acl
    acl.domain("google.com").grant_read()

    with pytest.raises(exceptions.PreconditionFailed):
        acl.save(if_metageneration_match=wrong_metageneration_number)
        assert "READER" not in acl.domain("google.com").get_roles()

    acl.save(if_metageneration_match=blob.metageneration)

    assert "READER" in acl.domain("google.com").get_roles()
    acl.domain("google.com").revoke_read()

    with pytest.raises(exceptions.PreconditionFailed):
        acl.save(if_generation_match=wrong_generation_number)
        assert "READER" in acl.domain("google.com").get_roles()

    acl.save(if_generation_match=blob.generation)
    assert "READER" not in acl.domain("google.com").get_roles()


def test_blob_acl_upload_predefined(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    control_blob = shared_bucket.blob(f"logo{uuid.uuid4().hex}")
    control_blob_info = file_data["logo"]

    blob = shared_bucket.blob(f"SmallFile{uuid.uuid4().hex}")
    info = file_data["simple"]

    try:
        control_blob.upload_from_filename(control_blob_info["path"])
    finally:
        blobs_to_delete.append(control_blob)
    try:
        blob.upload_from_filename(info["path"], predefined_acl="private")
    finally:
        blobs_to_delete.append(blob)

    control_blob_acl = control_blob.acl

    acl = blob.acl
    count = 0
    for entry in acl:
        count += 1
        entity = entry["entity"]
    assert count == 1
    assert entity.lstrip("user-") == service_account.service_account_email

    assert sum(1 for _ in control_blob_acl) > 1


def test_blob_patch_metadata(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    filename = file_data["logo"]["path"]
    blob_name = os.path.basename(filename)

    blob = shared_bucket.blob(blob_name)
    blob.upload_from_filename(filename)
    blobs_to_delete.append(blob)

    # NOTE: This should not be necessary. We should be able to pass
    #       it in to upload_file and also to upload_from_string.
    blob.content_type = "image/png"
    assert blob.content_type == "image/png"

    metadata = {"foo": "Foo", "bar": "Bar"}
    blob.metadata = metadata
    blob.patch()
    blob.reload()
    assert blob.metadata == metadata

    # Ensure that metadata keys can be deleted by setting equal to None.
    new_metadata = {"foo": "Foo", "bar": None}
    blob.metadata = new_metadata
    blob.patch()
    blob.reload()
    assert blob.metadata == {"foo": "Foo"}


def test_blob_direct_write_and_read_into_file(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    payload = b"Hello World"
    blob = shared_bucket.blob("MyBuffer")
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    same_blob = shared_bucket.blob("MyBuffer")
    same_blob.reload()  # Initialize properties.

    with tempfile.NamedTemporaryFile() as temp_f:
        with open(temp_f.name, "wb") as file_obj:
            same_blob.download_to_file(file_obj)

        with open(temp_f.name, "rb") as file_obj:
            stored_contents = file_obj.read()

    assert stored_contents == payload


def test_blob_download_w_generation_match(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    wrong_generation_number = 6

    blob = shared_bucket.blob("MyBuffer")
    payload = b"Hello World"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    same_blob = shared_bucket.blob("MyBuffer")
    same_blob.reload()  # Initialize properties.

    with tempfile.NamedTemporaryFile() as temp_f:
        with open(temp_f.name, "wb") as file_obj:
            with pytest.raises(exceptions.PreconditionFailed):
                same_blob.download_to_file(
                    file_obj, if_generation_match=wrong_generation_number
                )

            same_blob.download_to_file(
                file_obj,
                if_generation_match=blob.generation,
                if_metageneration_match=blob.metageneration,
            )

        with open(temp_f.name, "rb") as file_obj:
            stored_contents = file_obj.read()

    assert stored_contents == payload


def test_blob_download_w_failed_crc32c_checksum(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    blob = shared_bucket.blob("FailedChecksumBlob")
    payload = b"Hello World"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    with tempfile.NamedTemporaryFile() as temp_f:
        # Intercept the digest processing at the last stage and replace
        # it with garbage.  This is done with a patch to monkey-patch
        # the resumable media library's checksum processing; it does not
        # mock a remote interface like a unit test would.
        # The remote API is still exercised.
        with mock.patch(
            "google.cloud.storage._media._helpers.prepare_checksum_digest",
            return_value="FFFFFF==",
        ):
            with pytest.raises(DataCorruption):
                blob.download_to_filename(temp_f.name, checksum="crc32c")

            # Confirm the file was deleted on failure
            assert not os.path.isfile(temp_f.name)

            # Now download with checksumming turned off
            blob.download_to_filename(temp_f.name, checksum=None)

        with open(temp_f.name, "rb") as file_obj:
            stored_contents = file_obj.read()

        assert stored_contents == payload


def test_blob_download_as_text(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    blob = shared_bucket.blob("MyBuffer")
    payload = "Hello World"
    blob.upload_from_string(payload)
    etag = blob.etag
    blobs_to_delete.append(blob)

    blob = shared_bucket.blob("MyBuffer")
    assert blob.etag is None
    stored_contents = blob.download_as_text()
    assert stored_contents == payload
    assert blob.etag == etag

    # Test download with byte range
    end_byte = 5
    stored_contents = blob.download_as_text(start=0, end=end_byte - 1)
    assert stored_contents == payload[0:end_byte]


def test_blob_upload_w_gzip_encoded_download_raw(
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    payload = b"DEADBEEF" * 1000
    raw_stream = io.BytesIO()
    with gzip.GzipFile(fileobj=raw_stream, mode="wb") as gzip_stream:
        gzip_stream.write(payload)
    zipped = raw_stream.getvalue()

    blob = shared_bucket.blob("test_gzipped.gz")
    blob.content_encoding = "gzip"
    blob.upload_from_file(raw_stream, rewind=True)
    blobs_to_delete.append(blob)

    expanded = blob.download_as_bytes()
    assert expanded == payload

    raw = blob.download_as_bytes(raw_download=True)
    assert raw == zipped


def test_blob_upload_from_file_resumable_with_generation(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob(f"LargeFile{uuid.uuid4().hex}")
    wrong_generation = 3
    wrong_meta_generation = 3

    # uploading the file
    info = file_data["big"]
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(file_obj)
        blobs_to_delete.append(blob)

    # reuploading with correct generations numbers
    with open(info["path"], "rb") as file_obj:
        blob.upload_from_file(
            file_obj,
            if_generation_match=blob.generation,
            if_metageneration_match=blob.metageneration,
        )

    # reuploading with generations numbers that doesn't match original
    with pytest.raises(exceptions.PreconditionFailed):
        with open(info["path"], "rb") as file_obj:
            blob.upload_from_file(
                file_obj,
                if_generation_match=wrong_generation,
            )

    with pytest.raises(exceptions.PreconditionFailed):
        with open(info["path"], "rb") as file_obj:
            blob.upload_from_file(
                file_obj,
                if_metageneration_match=wrong_meta_generation,
            )


def test_blob_upload_from_string_w_owner(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob("MyBuffer")
    payload = b"Hello World"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    same_blob = shared_bucket.blob("MyBuffer")
    same_blob.reload(projection="full")  # Initialize properties.
    user_email = service_account.service_account_email
    owner = same_blob.owner
    assert user_email in owner["entity"]


def test_blob_upload_from_string_w_custom_time(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob("CustomTimeBlob")
    payload = b"Hello World"
    current_time = datetime.datetime.now()
    blob.custom_time = current_time
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    same_blob = shared_bucket.blob("CustomTimeBlob")
    same_blob.reload(projection="full")
    custom_time = same_blob.custom_time.replace(tzinfo=None)
    assert custom_time == current_time


def test_blob_upload_from_string_w_custom_time_no_micros(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    # Test that timestamps without microseconds are treated correctly by
    # custom_time encoding/decoding.
    blob = shared_bucket.blob("CustomTimeNoMicrosBlob")
    payload = b"Hello World"
    time_without_micros = datetime.datetime(2021, 2, 10, 12, 30)
    blob.custom_time = time_without_micros
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    same_blob = shared_bucket.blob(("CustomTimeNoMicrosBlob"))
    same_blob.reload(projection="full")
    custom_time = same_blob.custom_time.replace(tzinfo=None)
    assert custom_time == time_without_micros


def test_blob_upload_download_crc32_md5_hash(
    shared_bucket,
    blobs_to_delete,
    file_data,
    service_account,
):
    blob = shared_bucket.blob("MyBuffer")
    payload = b"Hello World"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    download_blob = shared_bucket.blob("MyBuffer")

    assert download_blob.download_as_bytes() == payload
    assert download_blob.crc32c == blob.crc32c
    assert download_blob.md5_hash == blob.md5_hash


@pytest.mark.parametrize(
    "blob_name,payload",
    [
        ("Caf\u00e9", b"Normalization Form C"),
        ("Cafe\u0301", b"Normalization Form D"),
    ],
)
def test_blob_w_unicode_names(blob_name, payload, shared_bucket, blobs_to_delete):
    # Historical note: This test when originally written accessed public
    # files with Unicode names. These files are no longer available, so it
    # was rewritten to upload them first.

    # Normalization form C: a single character for e-acute;
    # URL should end with Cafe%CC%81
    # Normalization Form D: an ASCII e followed by U+0301 combining
    # character; URL should end with Caf%C3%A9

    blob = shared_bucket.blob(blob_name)
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    same_blob = shared_bucket.blob(blob_name)
    assert same_blob.download_as_bytes() == payload
    assert same_blob.name == blob_name


def test_blob_compose_new_blob(shared_bucket, blobs_to_delete):
    payload_1 = b"AAA\n"
    source_1 = shared_bucket.blob("source-1")
    source_1.upload_from_string(payload_1)
    blobs_to_delete.append(source_1)

    payload_2 = b"BBB\n"
    source_2 = shared_bucket.blob("source-2")
    source_2.upload_from_string(payload_2)
    blobs_to_delete.append(source_2)

    destination = shared_bucket.blob("destination")
    destination.content_type = "text/plain"
    destination.compose([source_1, source_2])
    blobs_to_delete.append(destination)

    assert destination.download_as_bytes() == payload_1 + payload_2


def test_blob_compose_w_destination_contexts(shared_bucket, blobs_to_delete):
    from google.cloud.storage.blob import ObjectContexts, ObjectCustomContextPayload

    payload_1 = b"AAA\n"
    source_1 = shared_bucket.blob("source-1-contexts")
    source_1.upload_from_string(payload_1)
    blobs_to_delete.append(source_1)

    payload_2 = b"BBB\n"
    source_2 = shared_bucket.blob("source-2-contexts")
    source_2.upload_from_string(payload_2)
    blobs_to_delete.append(source_2)

    destination = shared_bucket.blob("destination-contexts")
    destination.content_type = "text/plain"

    context_payload = ObjectCustomContextPayload(value="bar")
    contexts = ObjectContexts(None, custom={"foo": context_payload})

    destination.compose([source_1, source_2], destination_contexts=contexts)
    blobs_to_delete.append(destination)

    assert destination.download_as_bytes() == payload_1 + payload_2
    destination.reload()
    assert destination.contexts.custom["foo"].value == "bar"


def test_blob_compose_new_blob_wo_content_type(shared_bucket, blobs_to_delete):
    payload_1 = b"AAA\n"
    source_1 = shared_bucket.blob("source-1")
    source_1.upload_from_string(payload_1)
    blobs_to_delete.append(source_1)

    payload_2 = b"BBB\n"
    source_2 = shared_bucket.blob("source-2")
    source_2.upload_from_string(payload_2)
    blobs_to_delete.append(source_2)

    destination = shared_bucket.blob("destination")

    destination.compose([source_1, source_2])
    blobs_to_delete.append(destination)

    assert destination.content_type is None
    assert destination.download_as_bytes() == payload_1 + payload_2


def test_blob_compose_replace_existing_blob(shared_bucket, blobs_to_delete):
    payload_before = b"AAA\n"
    original = shared_bucket.blob(uuid.uuid4().hex)
    original.content_type = "text/plain"
    original.upload_from_string(payload_before)
    blobs_to_delete.append(original)

    payload_to_append = b"BBB\n"
    to_append = shared_bucket.blob(uuid.uuid4().hex)
    to_append.upload_from_string(payload_to_append)
    blobs_to_delete.append(to_append)

    original.compose([original, to_append])

    assert original.download_as_bytes() == payload_before + payload_to_append


def test_blob_compose_w_generation_match_list(shared_bucket, blobs_to_delete):
    payload_before = b"AAA\n"
    original = shared_bucket.blob(uuid.uuid4().hex)
    original.content_type = "text/plain"
    original.upload_from_string(payload_before)
    blobs_to_delete.append(original)
    wrong_generations = [6, 7]
    wrong_metagenerations = [8, 9]

    payload_to_append = b"BBB\n"
    to_append = shared_bucket.blob(uuid.uuid4().hex)
    to_append.upload_from_string(payload_to_append)
    blobs_to_delete.append(to_append)

    with warnings.catch_warnings(record=True) as log:
        with pytest.raises(exceptions.PreconditionFailed):
            original.compose(
                [original, to_append],
                if_generation_match=wrong_generations,
                if_metageneration_match=wrong_metagenerations,
            )
    assert len(log) == 2

    with warnings.catch_warnings(record=True) as log:
        original.compose(
            [original, to_append],
            if_generation_match=[original.generation, to_append.generation],
            if_metageneration_match=[original.metageneration, to_append.metageneration],
        )
    assert len(log) == 2

    assert original.download_as_bytes() == payload_before + payload_to_append


def test_blob_compose_w_generation_match_long(shared_bucket, blobs_to_delete):
    payload_before = b"AAA\n"
    original = shared_bucket.blob(uuid.uuid4().hex)
    original.content_type = "text/plain"
    original.upload_from_string(payload_before)
    blobs_to_delete.append(original)

    payload_to_append = b"BBB\n"
    to_append = shared_bucket.blob(uuid.uuid4().hex)
    to_append.upload_from_string(payload_to_append)
    blobs_to_delete.append(to_append)

    with pytest.raises(exceptions.PreconditionFailed):
        original.compose([original, to_append], if_generation_match=0)

    original.compose([original, to_append], if_generation_match=original.generation)

    assert original.download_as_bytes() == payload_before + payload_to_append


def test_blob_compose_w_source_generation_match(shared_bucket, blobs_to_delete):
    payload_before = b"AAA\n"
    original = shared_bucket.blob(uuid.uuid4().hex)
    original.content_type = "text/plain"
    original.upload_from_string(payload_before)
    blobs_to_delete.append(original)
    wrong_source_generations = [6, 7]

    payload_to_append = b"BBB\n"
    to_append = shared_bucket.blob(uuid.uuid4().hex)
    to_append.upload_from_string(payload_to_append)
    blobs_to_delete.append(to_append)

    with pytest.raises(exceptions.PreconditionFailed):
        original.compose(
            [original, to_append],
            if_source_generation_match=wrong_source_generations,
        )

    original.compose(
        [original, to_append],
        if_source_generation_match=[original.generation, to_append.generation],
    )

    assert original.download_as_bytes() == payload_before + payload_to_append


def test_blob_compose_w_user_project(storage_client, buckets_to_delete, user_project):
    new_bucket_name = _helpers.unique_name("compose-user-project")
    created = _helpers.retry_429_503(storage_client.create_bucket)(new_bucket_name)
    buckets_to_delete.append(created)
    created.requester_pays = True

    payload_1 = b"AAA\n"
    source_1 = created.blob(uuid.uuid4().hex)
    source_1.upload_from_string(payload_1)

    payload_2 = b"BBB\n"
    source_2 = created.blob(uuid.uuid4().hex)
    source_2.upload_from_string(payload_2)

    with_user_project = storage_client.bucket(
        new_bucket_name, user_project=user_project
    )

    destination = with_user_project.blob(uuid.uuid4().hex)
    destination.content_type = "text/plain"
    destination.compose([source_1, source_2])

    assert destination.download_as_bytes() == payload_1 + payload_2


def test_blob_rewrite_new_blob_add_key(shared_bucket, blobs_to_delete, file_data):
    info = file_data["simple"]
    source = shared_bucket.blob(uuid.uuid4().hex)
    source.upload_from_filename(info["path"])
    blobs_to_delete.append(source)
    source_data = source.download_as_bytes()

    key = os.urandom(32)
    dest = shared_bucket.blob(uuid.uuid4().hex, encryption_key=key)
    token, rewritten, total = dest.rewrite(source)
    blobs_to_delete.append(dest)

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)
    assert dest.download_as_bytes() == source_data


def test_blob_rewrite_w_destination_contexts(shared_bucket, blobs_to_delete, file_data):
    from google.cloud.storage.blob import ObjectContexts, ObjectCustomContextPayload

    info = file_data["simple"]
    source = shared_bucket.blob(uuid.uuid4().hex)
    source.upload_from_filename(info["path"])
    blobs_to_delete.append(source)
    source_data = source.download_as_bytes()

    dest = shared_bucket.blob(uuid.uuid4().hex)
    context_payload = ObjectCustomContextPayload(value="bar")
    contexts = ObjectContexts(None, custom={"foo": context_payload})

    token, rewritten, total = dest.rewrite(source, destination_contexts=contexts)
    blobs_to_delete.append(dest)

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)
    assert dest.download_as_bytes() == source_data
    dest.reload()
    assert dest.contexts.custom["foo"].value == "bar"


def test_blob_rewrite_rotate_key(shared_bucket, blobs_to_delete, file_data):
    blob_name = "rotating-keys"
    info = file_data["simple"]

    source_key = os.urandom(32)
    source = shared_bucket.blob(blob_name, encryption_key=source_key)
    source.upload_from_filename(info["path"])
    blobs_to_delete.append(source)
    source_data = source.download_as_bytes()

    dest_key = os.urandom(32)
    dest = shared_bucket.blob(blob_name, encryption_key=dest_key)
    token, rewritten, total = dest.rewrite(source)
    # Not adding 'dest' to 'blobs_to_delete':  it is the
    # same object as 'source'.

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)
    assert dest.download_as_bytes() == source_data


def test_blob_rewrite_add_key_w_user_project(
    storage_client, buckets_to_delete, user_project, file_data
):
    info = file_data["simple"]
    new_bucket_name = _helpers.unique_name("rewrite-key-up")
    created = _helpers.retry_429_503(storage_client.create_bucket)(new_bucket_name)
    buckets_to_delete.append(created)
    created.requester_pays = True

    with_user_project = storage_client.bucket(
        new_bucket_name, user_project=user_project
    )

    source = with_user_project.blob("source")
    source.upload_from_filename(info["path"])
    source_data = source.download_as_bytes()

    key = os.urandom(32)
    dest = with_user_project.blob("dest", encryption_key=key)
    token, rewritten, total = dest.rewrite(source)

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)
    assert dest.download_as_bytes() == source_data


def test_blob_rewrite_rotate_key_w_user_project(
    storage_client, buckets_to_delete, user_project, file_data
):
    blob_name = "rotating-keys"
    info = file_data["simple"]
    new_bucket_name = _helpers.unique_name("rewrite-key-up")
    created = _helpers.retry_429_503(storage_client.create_bucket)(new_bucket_name)
    buckets_to_delete.append(created)
    created.requester_pays = True

    with_user_project = storage_client.bucket(
        new_bucket_name, user_project=user_project
    )

    source_key = os.urandom(32)
    source = with_user_project.blob(blob_name, encryption_key=source_key)
    source.upload_from_filename(info["path"])
    source_data = source.download_as_bytes()

    dest_key = os.urandom(32)
    dest = with_user_project.blob(blob_name, encryption_key=dest_key)
    token, rewritten, total = dest.rewrite(source)

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)
    assert dest.download_as_bytes() == source_data


def test_blob_rewrite_w_generation_match(shared_bucket, blobs_to_delete, file_data):
    wrong_generation_number = 6
    blob_name = "generation-match"
    info = file_data["simple"]

    source = shared_bucket.blob(blob_name)
    source.upload_from_filename(info["path"])
    source_data = source.download_as_bytes()
    blobs_to_delete.append(source)

    dest = shared_bucket.blob(blob_name)
    dest.reload()

    with pytest.raises(exceptions.PreconditionFailed):
        dest.rewrite(source, if_generation_match=wrong_generation_number)

    token, rewritten, total = dest.rewrite(
        source,
        if_generation_match=dest.generation,
        if_source_generation_match=source.generation,
        if_source_metageneration_match=source.metageneration,
    )

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)
    assert dest.download_as_bytes() == source_data


def test_blob_update_storage_class_small_file(
    shared_bucket, blobs_to_delete, file_data
):
    from google.cloud.storage import constants

    blob = shared_bucket.blob("SmallFile")

    info = file_data["simple"]
    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)

    blob.update_storage_class(constants.NEARLINE_STORAGE_CLASS)
    blob.reload()
    assert blob.storage_class == constants.NEARLINE_STORAGE_CLASS

    blob.update_storage_class(constants.COLDLINE_STORAGE_CLASS)
    blob.reload()
    assert blob.storage_class == constants.COLDLINE_STORAGE_CLASS


def test_blob_update_storage_class_large_file(
    shared_bucket, blobs_to_delete, file_data
):
    from google.cloud.storage import constants

    blob = shared_bucket.blob(f"BigFile{uuid.uuid4().hex}")

    info = file_data["big"]
    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)

    blob.update_storage_class(constants.NEARLINE_STORAGE_CLASS)
    blob.reload()
    assert blob.storage_class == constants.NEARLINE_STORAGE_CLASS

    blob.update_storage_class(constants.COLDLINE_STORAGE_CLASS)
    blob.reload()
    assert blob.storage_class == constants.COLDLINE_STORAGE_CLASS


def test_object_retention_lock(storage_client, buckets_to_delete, blobs_to_delete):
    from google.cloud.storage._helpers import _NOW, _UTC

    # Test bucket created with object retention enabled
    new_bucket_name = _helpers.unique_name("object-retention")
    created_bucket = _helpers.retry_429_503(storage_client.create_bucket)(
        new_bucket_name, enable_object_retention=True
    )
    buckets_to_delete.append(created_bucket)
    assert created_bucket.object_retention_mode == "Enabled"

    # Test create object with object retention enabled
    payload = b"Hello World"
    mode = "Unlocked"
    current_time = _NOW(_UTC).replace(tzinfo=None)
    expiration_time = current_time + datetime.timedelta(seconds=10)
    blob = created_bucket.blob("object-retention-lock")
    blob.retention.mode = mode
    blob.retention.retain_until_time = expiration_time
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)
    blob.reload()
    assert blob.retention.mode == mode

    # Test patch object to disable object retention
    blob.retention.mode = None
    blob.retention.retain_until_time = None
    blob.patch(override_unlocked_retention=True)
    assert blob.retention.mode is None


def test_blob_download_as_bytes_single_shot_download(
    shared_bucket, blobs_to_delete, file_data, service_account
):
    blob_name = f"download-single-shot-{uuid.uuid4().hex}"
    info = file_data["simple"]
    with open(info["path"], "rb") as f:
        payload = f.read()

    blob = shared_bucket.blob(blob_name)
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    result_regular_download = blob.download_as_bytes(single_shot_download=False)
    assert result_regular_download == payload

    result_single_shot_download = blob.download_as_bytes(single_shot_download=True)
    assert result_single_shot_download == payload


def test_blob_compose_delete_source_objects(shared_bucket, blobs_to_delete):
    payload_1 = b"AAA\n"
    source_1 = shared_bucket.blob("source-1-delete")
    source_1.upload_from_string(payload_1)
    blobs_to_delete.append(source_1)

    payload_2 = b"BBB\n"
    source_2 = shared_bucket.blob("source-2-delete")
    source_2.upload_from_string(payload_2)
    blobs_to_delete.append(source_2)

    destination = shared_bucket.blob("destination-delete")
    destination.compose([source_1, source_2], delete_source_objects=True)
    blobs_to_delete.append(destination)

    assert destination.download_as_bytes() == payload_1 + payload_2
    assert not source_1.exists()
    assert not source_2.exists()


def test_blob_contexts(shared_bucket, blobs_to_delete):
    from google.cloud.storage.blob import ObjectContexts, ObjectCustomContextPayload

    blob_name = f"ObjectContexts-{uuid.uuid4().hex}"
    blob = shared_bucket.blob(blob_name)

    # 1. Create with contexts
    custom = {
        "k1": ObjectCustomContextPayload(value="v1"),
        "k2": ObjectCustomContextPayload(value="v2"),
    }
    blob.contexts = ObjectContexts(blob, custom=custom)
    blob.upload_from_string(b"foo")
    blobs_to_delete.append(blob)

    blob.reload()
    assert blob.contexts.custom["k1"].value == "v1"
    assert blob.contexts.custom["k2"].value == "v2"

    # 2. Patch: update one, delete one
    blob.contexts.custom["k1"].value = "v1-updated"
    blob.contexts.custom["k2"].value = None
    blob.patch()

    blob.reload()
    assert blob.contexts.custom["k1"].value == "v1-updated"
    assert "k2" not in blob.contexts.custom

    # 3. Clear all
    blob.contexts = None
    blob.patch()

    blob.reload()
    assert not blob.contexts.custom


def test_blob_contexts_custom_setter(shared_bucket, blobs_to_delete):
    from google.cloud.storage.blob import ObjectCustomContextPayload

    blob_name = f"ObjectContextsCustomSetter-{uuid.uuid4().hex}"
    blob = shared_bucket.blob(blob_name)
    blob.upload_from_string(b"foo")
    blobs_to_delete.append(blob)

    # 1. Use custom setter to assign dictionary of payloads
    custom = {
        "k1": ObjectCustomContextPayload(value="v1"),
        "k2": ObjectCustomContextPayload(value="v2"),
    }
    blob.contexts.custom = custom
    blob.patch()

    blob.reload()
    assert blob.contexts.custom["k1"].value == "v1"
    assert blob.contexts.custom["k2"].value == "v2"

    # 2. Update one key.value and patch
    blob.contexts.custom["k1"].value = "v1-updated"
    blob.patch()

    blob.reload()
    assert blob.contexts.custom["k1"].value == "v1-updated"
    assert blob.contexts.custom["k2"].value == "v2"


def test_upload_from_file_streaming_with_trailing_checksum_validation(
    shared_bucket, blobs_to_delete
):
    import base64
    import io
    import os

    import google_crc32c

    blob_name = f"StreamingTrailingChecksum-{uuid.uuid4().hex}"
    blob = shared_bucket.blob(blob_name)
    blobs_to_delete.append(blob)

    # Payload > 8 MiB to trigger chunked resumable upload
    payload = os.urandom(8 * 1024 * 1024 + 1024)
    io_stream = io.BytesIO(payload)

    # Calculate expected CRC32C base64 hash
    expected_crc32c_int = google_crc32c.value(payload)
    expected_crc32c_b64 = base64.b64encode(
        expected_crc32c_int.to_bytes(4, "big")
    ).decode("utf-8")

    # Upload from stream WITHOUT passing size parameter
    # (routes to resumable upload with total_bytes=None)
    blob.upload_from_file(io_stream, checksum="crc32c")

    blob.reload()
    assert blob.size == len(payload)
    assert blob.crc32c == expected_crc32c_b64


def test_upload_from_file_streaming_corrupted_checksum_rejection(
    shared_bucket, blobs_to_delete
):
    import io
    import os

    import pytest
    from google.api_core.exceptions import BadRequest

    blob_name = f"StreamingCorruptedChecksum-{uuid.uuid4().hex}"
    blob = shared_bucket.blob(blob_name)
    blobs_to_delete.append(blob)

    payload = os.urandom(8 * 1024 * 1024 + 1024)
    io_stream = io.BytesIO(payload)

    # Supply an intentionally corrupted/mismatched checksum
    bad_crc32c_b64 = "AAAAAA=="

    with pytest.raises(BadRequest):
        blob.upload_from_file(
            io_stream,
            checksum="crc32c",
            crc32c_checksum_value=bad_crc32c_b64,
        )
