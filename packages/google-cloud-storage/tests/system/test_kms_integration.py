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

import os

from . import _helpers

keyring_name = "gcs-test"
default_key_name = "gcs-test"
alt_key_name = "gcs-test-alternate"


def test_blob_w_explicit_kms_key_name(
    kms_bucket, blobs_to_delete, kms_key_name, file_data
):
    blob_name = "explicit-kms-key-name"
    info = file_data["simple"]
    blob = kms_bucket.blob(blob_name, kms_key_name=kms_key_name)
    blob.upload_from_filename(info["path"])
    blobs_to_delete.append(blob)

    with open(info["path"], "rb") as file_obj:
        assert blob.download_as_bytes() == file_obj.read()

    # We don't know the current version of the key.
    assert blob.kms_key_name.startswith(kms_key_name)

    (listed,) = list(kms_bucket.list_blobs())
    assert listed.kms_key_name.startswith(kms_key_name)


@_helpers.retry_failures
def test_bucket_w_default_kms_key_name(
    kms_bucket,
    blobs_to_delete,
    kms_key_name,
    alt_kms_key_name,
    file_data,
):
    blob_name = "default-kms-key-name"
    info = file_data["simple"]

    with open(info["path"], "rb") as file_obj:
        payload = file_obj.read()

    kms_bucket.default_kms_key_name = kms_key_name
    kms_bucket.patch()
    assert kms_bucket.default_kms_key_name == kms_key_name

    # Changes to the bucket will be readable immediately after writing,
    # but configuration changes may take time to propagate.
    _helpers.await_config_changes_propagate()

    defaulted_blob = kms_bucket.blob(blob_name)
    defaulted_blob.upload_from_filename(info["path"])
    blobs_to_delete.append(defaulted_blob)

    assert defaulted_blob.download_as_bytes() == payload
    _helpers.retry_429_harder(_helpers.retry_has_kms_key_name(defaulted_blob.reload))()
    # We don't know the current version of the key.
    assert defaulted_blob.kms_key_name.startswith(kms_key_name)

    # Test changing the default KMS key.
    kms_bucket.default_kms_key_name = alt_kms_key_name
    kms_bucket.patch()
    assert kms_bucket.default_kms_key_name == alt_kms_key_name

    # Test removing the default KMS key.
    kms_bucket.default_kms_key_name = None
    kms_bucket.patch()
    assert kms_bucket.default_kms_key_name is None


def test_blob_rewrite_rotate_csek_to_cmek(
    kms_bucket,
    blobs_to_delete,
    kms_key_name,
    file_data,
):
    blob_name = "rotating-keys"
    source_key = os.urandom(32)
    info = file_data["simple"]

    source = kms_bucket.blob(blob_name, encryption_key=source_key)
    source.upload_from_filename(info["path"])
    blobs_to_delete.append(source)
    source_data = source.download_as_bytes()

    # We can't verify it, but ideally we would check that the following
    # URL was resolvable with our credentials
    # KEY_URL = 'https://cloudkms.googleapis.com/v1/{}'.format(
    #     kms_key_name)

    dest = kms_bucket.blob(blob_name, kms_key_name=kms_key_name)
    token, rewritten, total = dest.rewrite(source)

    while token is not None:
        token, rewritten, total = dest.rewrite(source, token=token)

    # Not adding 'dest' to 'self.case_blobs_to_delete':  it is the
    # same object as 'source'.

    assert token is None
    assert rewritten == len(source_data)
    assert total == len(source_data)

    assert dest.download_as_bytes() == source_data

    # Test existing kmsKeyName version is ignored in the rewrite request
    dest = kms_bucket.get_blob(blob_name)
    source = kms_bucket.get_blob(blob_name)
    token, rewritten, total = dest.rewrite(source)

    while token is not None:
        token, rewritten, total = dest.rewrite(source, token=token)

    assert rewritten == len(source_data)
    assert dest.download_as_bytes() == source_data


def test_blob_upload_w_bucket_cmek_enabled(
    kms_bucket,
    blobs_to_delete,
    kms_key_name,
    alt_kms_key_name,
):
    blob_name = "test-blob"
    override_blob_name = "override-default-kms-key-name"
    payload = b"DEADBEEF"
    alt_payload = b"NEWDEADBEEF"

    kms_bucket.default_kms_key_name = kms_key_name
    kms_bucket.patch()
    assert kms_bucket.default_kms_key_name == kms_key_name

    # Changes to the bucket will be readable immediately after writing,
    # but configuration changes may take time to propagate.
    _helpers.await_config_changes_propagate()

    blob = kms_bucket.blob(blob_name)
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    _helpers.retry_429_harder(_helpers.retry_has_kms_key_name(blob.reload))()
    assert blob.kms_key_name.startswith(kms_key_name)

    blob.upload_from_string(alt_payload, if_generation_match=blob.generation)
    assert blob.download_as_bytes() == alt_payload

    # Test the specific key is used to encrypt the object if you have both
    # a default KMS key set on your bucket and a specific key included in your request.
    override_blob = kms_bucket.blob(override_blob_name, kms_key_name=alt_kms_key_name)
    override_blob.upload_from_string(payload)
    blobs_to_delete.append(override_blob)

    assert override_blob.download_as_bytes() == payload
    assert override_blob.kms_key_name.startswith(alt_kms_key_name)

    kms_bucket.default_kms_key_name = None
    _helpers.retry_429_harder(kms_bucket.patch)()
    assert kms_bucket.default_kms_key_name is None
