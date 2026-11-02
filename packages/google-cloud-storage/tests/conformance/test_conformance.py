# Copyright 2021 Google LLC
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

"""Conformance tests for retry. Verifies correct behavior around retryable errors, idempotency and preconditions."""

import functools
import logging
import os
import subprocess
import tempfile
import time
import urllib
import uuid

import pytest
import requests
from google.auth.credentials import AnonymousCredentials

from google.cloud import storage
from google.cloud.storage.hmac_key import HMACKeyMetadata

from . import _read_local_json

_CONFORMANCE_TESTS = _read_local_json("retry_strategy_test_data.json")["retryTests"]

"""Environment variable or default host for Storage testbench emulator."""
_HOST = os.environ.get("STORAGE_EMULATOR_HOST", "http://localhost:9000")
_PORT = urllib.parse.urlsplit(_HOST).port

"""The storage testbench docker image info and commands."""
_DEFAULT_IMAGE_NAME = "gcr.io/cloud-devrel-public-resources/storage-testbench"
_DEFAULT_IMAGE_TAG = "latest"
_DOCKER_IMAGE = f"{_DEFAULT_IMAGE_NAME}:{_DEFAULT_IMAGE_TAG}"
_PULL_CMD = ["docker", "pull", _DOCKER_IMAGE]
_RUN_CMD = ["docker", "run", "--rm", "-d", "-p", f"{_PORT}:9000", _DOCKER_IMAGE]

_CONF_TEST_PROJECT_ID = "my-project-id"
_CONF_TEST_SERVICE_ACCOUNT_EMAIL = (
    "my-service-account@my-project-id.iam.gserviceaccount.com"
)
_CONF_TEST_PUBSUB_TOPIC_NAME = "my-topic-name"

_STRING_CONTENT = "hello world"
_BYTE_CONTENT = b"12345678"
_RESUMABLE_UPLOAD_CHUNK_SIZE = 2 * 1024 * 1024


########################################################################################################################################
### Library methods for mapping ########################################################################################################
########################################################################################################################################


def bucket_get_blob(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    bucket = client.bucket(bucket.name)
    bucket.get_blob(object.name)


def blob_exists(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    blob.exists()


def blob_download_as_bytes(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    # download the file and assert data integrity
    blob = client.bucket(bucket.name).blob(file.name)
    stored_contents = blob.download_as_bytes()
    assert stored_contents == data.encode("utf-8")


def blob_download_as_text(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(file.name)
    stored_contents = blob.download_as_text()
    assert stored_contents == data


def blob_download_to_filename(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(file.name)
    with tempfile.NamedTemporaryFile() as temp_f:
        blob.download_to_filename(temp_f.name)
        with open(temp_f.name, "r") as file_obj:
            stored_contents = file_obj.read()
    assert stored_contents == data


def blob_download_to_filename_chunked(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(file.name, chunk_size=40 * 1024 * 1024)
    with tempfile.NamedTemporaryFile() as temp_f:
        blob.download_to_filename(temp_f.name)
        with open(temp_f.name, "r") as file_obj:
            stored_contents = file_obj.read()
    assert stored_contents == data


def blob_download_to_filename_range(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(file.name)
    with tempfile.NamedTemporaryFile() as temp_f:
        blob.download_to_filename(temp_f.name, start=1024, end=512 * 1024)
        with open(temp_f.name, "r") as file_obj:
            stored_contents = file_obj.read()
    assert stored_contents == data[1024 : 512 * 1024 + 1]


def client_download_blob_to_file(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(file.name)
    with tempfile.NamedTemporaryFile() as temp_f:
        with open(temp_f.name, "wb") as file_obj:
            client.download_blob_to_file(blob, file_obj)
        with open(temp_f.name, "r") as to_read:
            stored_contents = to_read.read()
    assert stored_contents == data


def blobreader_read(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(file.name)
    with blob.open(mode="r") as reader:
        stored_contents = reader.read()
    assert stored_contents == data


def client_list_blobs(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    blobs = client.list_blobs(bucket.name)
    for b in blobs:
        pass


def bucket_list_blobs(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    blobs = client.bucket(bucket.name).list_blobs()
    for b in blobs:
        pass


def bucket_delete(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.delete(force=True)


def bucket_reload(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.reload()


def client_get_bucket(client, _preconditions, **resources):
    client.get_bucket(resources.get("bucket").name)


def client_lookup_bucket(client, _preconditions, **resources):
    client.lookup_bucket(resources.get("bucket").name)


def bucket_exists(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.exists()


def client_create_bucket(client, _preconditions, **_):
    bucket = client.bucket(uuid.uuid4().hex)
    client.create_bucket(bucket)


def bucket_create(client, _preconditions, **_):
    bucket = client.bucket(uuid.uuid4().hex)
    bucket.create()


def client_list_buckets(client, _preconditions, **_):
    buckets = client.list_buckets()
    for b in buckets:
        pass


def bucket_get_iam_policy(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.get_iam_policy()


def bucket_test_iam_permissions(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    permissions = ["storage.buckets.get", "storage.buckets.create"]
    bucket.test_iam_permissions(permissions)


def bucket_lock_retention_policy(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.retention_period = 60
    bucket.patch()
    bucket.lock_retention_policy()


def client_get_service_account_email(client, _preconditions, **_):
    client.get_service_account_email()


def notification_create(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    notification = bucket.notification(topic_name=_CONF_TEST_PUBSUB_TOPIC_NAME)
    notification.create()


def bucket_list_notifications(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    notifications = client.bucket(bucket.name).list_notifications()
    for n in notifications:
        pass


def bucket_get_notification(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    notification = resources.get("notification")
    client.bucket(bucket.name).get_notification(notification.notification_id)


def notification_reload(client, _preconditions, **resources):
    notification = client.bucket(resources.get("bucket").name).notification(
        notification_id=resources.get("notification").notification_id
    )
    notification.reload()


def notification_exists(client, _preconditions, **resources):
    notification = client.bucket(resources.get("bucket").name).notification(
        notification_id=resources.get("notification").notification_id
    )
    notification.exists()


def notification_delete(client, _preconditions, **resources):
    notification = client.bucket(resources.get("bucket").name).notification(
        notification_id=resources.get("notification").notification_id
    )
    notification.delete()


def client_list_hmac_keys(client, _preconditions, **_):
    hmac_keys = client.list_hmac_keys()
    for k in hmac_keys:
        pass


def client_get_hmac_key_metadata(client, _preconditions, **resources):
    access_id = resources.get("hmac_key").access_id
    client.get_hmac_key_metadata(access_id=access_id)


def hmac_key_exists(client, _preconditions, **resources):
    access_id = resources.get("hmac_key").access_id
    hmac_key = HMACKeyMetadata(client, access_id=access_id)
    hmac_key.exists()


def hmac_key_reload(client, _preconditions, **resources):
    access_id = resources.get("hmac_key").access_id
    hmac_key = HMACKeyMetadata(client, access_id=access_id)
    hmac_key.reload()


def hmac_key_delete(client, _preconditions, **resources):
    access_id = resources.get("hmac_key").access_id
    hmac_key = HMACKeyMetadata(client, access_id=access_id)
    hmac_key.state = "INACTIVE"
    hmac_key.update()
    hmac_key.delete()


def client_create_hmac_key(client, _preconditions, **_):
    client.create_hmac_key(service_account_email=_CONF_TEST_SERVICE_ACCOUNT_EMAIL)


def hmac_key_update(client, _preconditions, **resources):
    access_id = resources.get("hmac_key").access_id
    etag = resources.get("hmac_key").etag
    hmac_key = HMACKeyMetadata(client, access_id=access_id)
    if _preconditions:
        pytest.skip("Etag is not yet supported")
        hmac_key.etag = etag
    hmac_key.state = "INACTIVE"
    hmac_key.update()


def bucket_patch(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    metageneration = resources.get("bucket").metageneration
    bucket.storage_class = "COLDLINE"
    if _preconditions:
        bucket.patch(if_metageneration_match=metageneration)
    else:
        bucket.patch()


def bucket_update(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    metageneration = resources.get("bucket").metageneration
    bucket._properties = {"storageClass": "STANDARD"}
    if _preconditions:
        bucket.update(if_metageneration_match=metageneration)
    else:
        bucket.update()


def bucket_set_iam_policy(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    role = "roles/storage.objectViewer"
    member = _CONF_TEST_SERVICE_ACCOUNT_EMAIL

    policy = bucket.get_iam_policy(requested_policy_version=3)
    policy.bindings.append({"role": role, "members": {member}})
    if _preconditions:
        bucket.set_iam_policy(policy)
    else:
        # IAM policies have no metageneration:  clear ETag to avoid checking that it matches.
        policy.etag = None
        bucket.set_iam_policy(policy)


def bucket_delete_blob(client, _preconditions, **resources):
    object = resources.get("object")
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        generation = object.generation
        bucket.delete_blob(object.name, if_generation_match=generation)
    else:
        bucket.delete_blob(object.name)


def bucket_delete_blobs(client, _preconditions, **resources):
    object = resources.get("object")
    bucket = client.bucket(resources.get("bucket").name)
    sources = [object]
    source_generations = [object.generation]
    if _preconditions:
        bucket.delete_blobs(sources, if_generation_match=source_generations)
    else:
        bucket.delete_blobs(sources)


def blob_delete(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    if _preconditions:
        blob.delete(if_generation_match=object.generation)
    else:
        blob.delete()


def blob_patch(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    blob.metadata = {"foo": "bar"}
    if _preconditions:
        blob.patch(if_metageneration_match=object.metageneration)
    else:
        blob.patch()


def blob_update(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    blob.metadata = {"foo": "bar"}
    if _preconditions:
        blob.update(if_metageneration_match=object.metageneration)
    else:
        blob.update()


def bucket_copy_blob(client, _preconditions, **resources):
    object = resources.get("object")
    bucket = client.bucket(resources.get("bucket").name)
    destination = client.create_bucket(uuid.uuid4().hex)
    if _preconditions:
        bucket.copy_blob(
            object, destination, new_name=uuid.uuid4().hex, if_generation_match=0
        )
    else:
        bucket.copy_blob(object, destination)


def bucket_rename_blob(client, _preconditions, **resources):
    object = resources.get("object")
    bucket = client.bucket(resources.get("bucket").name)
    blob = bucket.blob(resources.get("object").name)
    new_name = uuid.uuid4().hex
    if _preconditions:
        bucket.rename_blob(
            blob,
            new_name,
            if_generation_match=0,
            if_source_generation_match=object.generation,
        )
    else:
        bucket.rename_blob(blob, new_name)


def blob_rewrite(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    new_blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    new_blob.metadata = {"foo": "bar"}
    if _preconditions:
        new_blob.rewrite(object, if_generation_match=0)
    else:
        new_blob.rewrite(object)


def blob_update_storage_class(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    storage_class = "STANDARD"
    if _preconditions:
        blob.update_storage_class(storage_class, if_generation_match=object.generation)
    else:
        blob.update_storage_class(storage_class)


def blob_compose(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    blob_2 = bucket.blob(uuid.uuid4().hex)
    blob_2.upload_from_string(_STRING_CONTENT)
    sources = [blob_2]
    if _preconditions:
        blob.compose(sources, if_generation_match=object.generation)
    else:
        blob.compose(sources)


def blob_upload_from_string(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    _, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    blob.chunk_size = _RESUMABLE_UPLOAD_CHUNK_SIZE
    if _preconditions:
        blob.upload_from_string(data, if_generation_match=0)
    else:
        blob.upload_from_string(data)
    assert blob.size == len(data)


def blob_upload_from_file(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    file_blob = client.bucket(bucket.name).blob(file.name)
    upload_blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    upload_blob.chunk_size = _RESUMABLE_UPLOAD_CHUNK_SIZE

    with tempfile.NamedTemporaryFile() as temp_f:
        # Create a named temporary file with payload.
        with open(temp_f.name, "wb") as file_obj:
            client.download_blob_to_file(file_blob, file_obj)
        # Upload the temporary file and assert data integrity.
        if _preconditions:
            upload_blob.upload_from_file(temp_f, if_generation_match=0)
        else:
            upload_blob.upload_from_file(temp_f)

    upload_blob.reload()
    assert upload_blob.size == len(data)


def blob_upload_from_filename(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    blob.chunk_size = _RESUMABLE_UPLOAD_CHUNK_SIZE

    bucket = resources.get("bucket")
    file, data = resources.get("file_data")
    file_blob = client.bucket(bucket.name).blob(file.name)
    upload_blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    upload_blob.chunk_size = _RESUMABLE_UPLOAD_CHUNK_SIZE

    with tempfile.NamedTemporaryFile() as temp_f:
        # Create a named temporary file with payload.
        with open(temp_f.name, "wb") as file_obj:
            client.download_blob_to_file(file_blob, file_obj)
        # Upload the temporary file and assert data integrity.
        if _preconditions:
            upload_blob.upload_from_filename(temp_f.name, if_generation_match=0)
        else:
            upload_blob.upload_from_filename(temp_f.name)

    upload_blob.reload()
    assert upload_blob.size == len(data)


def blobwriter_write(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    _, data = resources.get("file_data")
    blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    if _preconditions:
        with blob.open(
            "w", chunk_size=_RESUMABLE_UPLOAD_CHUNK_SIZE, if_generation_match=0
        ) as writer:
            writer.write(data)
    else:
        with blob.open("w", chunk_size=_RESUMABLE_UPLOAD_CHUNK_SIZE) as writer:
            writer.write(data)
    blob.reload()
    assert blob.size == len(data)


def blobwriter_write_multipart(client, _preconditions, **resources):
    chunk_size = 256 * 1024
    bucket = resources.get("bucket")
    blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    if _preconditions:
        with blob.open("wb", chunk_size=chunk_size, if_generation_match=0) as writer:
            writer.write(_BYTE_CONTENT)
    else:
        with blob.open("wb", chunk_size=chunk_size) as writer:
            writer.write(_BYTE_CONTENT)


def blob_upload_from_string_multipart(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    if _preconditions:
        blob.upload_from_string(_STRING_CONTENT, if_generation_match=0)
    else:
        blob.upload_from_string(_STRING_CONTENT)


def blob_create_resumable_upload_session(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    blob = client.bucket(bucket.name).blob(uuid.uuid4().hex)
    if _preconditions:
        blob.create_resumable_upload_session(if_generation_match=0)
    else:
        blob.create_resumable_upload_session()


def blob_make_private(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    if _preconditions:
        blob.make_private(if_metageneration_match=object.metageneration)
    else:
        blob.make_private()


def blob_make_public(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    if _preconditions:
        blob.make_public(if_metageneration_match=object.metageneration)
    else:
        blob.make_public()


def bucket_make_private(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        bucket.make_private(
            if_metageneration_match=resources.get("bucket").metageneration
        )
    else:
        bucket.make_private()


def bucket_make_public(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        bucket.make_public(
            if_metageneration_match=resources.get("bucket").metageneration
        )
    else:
        bucket.make_public()


def bucket_acl_reload(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.acl.reload()


def bucket_acl_save(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.acl.user(_CONF_TEST_SERVICE_ACCOUNT_EMAIL).grant_owner()
    if _preconditions:
        bucket.acl.save(if_metageneration_match=resources.get("bucket").metageneration)
    else:
        bucket.acl.save()


def bucket_acl_save_predefined(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        bucket.acl.save_predefined(
            "bucketOwnerFullControl",
            if_metageneration_match=resources.get("bucket").metageneration,
        )
    else:
        bucket.acl.save_predefined("bucketOwnerFullControl")


def bucket_acl_clear(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        bucket.acl.clear(if_metageneration_match=resources.get("bucket").metageneration)
    else:
        bucket.acl.clear()


def default_object_acl_reload(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.default_object_acl.reload()


def default_object_acl_save(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    bucket.default_object_acl.user(_CONF_TEST_SERVICE_ACCOUNT_EMAIL).grant_owner()
    if _preconditions:
        bucket.default_object_acl.save(
            if_metageneration_match=resources.get("bucket").metageneration
        )
    else:
        bucket.default_object_acl.save()


def default_object_acl_save_predefined(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        bucket.default_object_acl.save_predefined(
            "bucketOwnerFullControl",
            if_metageneration_match=resources.get("bucket").metageneration,
        )
    else:
        bucket.default_object_acl.save_predefined("bucketOwnerFullControl")


def default_object_acl_clear(client, _preconditions, **resources):
    bucket = client.bucket(resources.get("bucket").name)
    if _preconditions:
        bucket.default_object_acl.clear(
            if_metageneration_match=resources.get("bucket").metageneration
        )
    else:
        bucket.default_object_acl.clear()


def object_acl_reload(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    blob.acl.reload()


def object_acl_save(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    blob.acl.user(_CONF_TEST_SERVICE_ACCOUNT_EMAIL).grant_owner()
    if _preconditions:
        blob.acl.save(if_metageneration_match=object.metageneration)
    else:
        blob.acl.save()


def object_acl_save_predefined(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    if _preconditions:
        blob.acl.save_predefined(
            "bucketOwnerFullControl", if_metageneration_match=object.metageneration
        )
    else:
        blob.acl.save_predefined("bucketOwnerFullControl")


def object_acl_clear(client, _preconditions, **resources):
    bucket = resources.get("bucket")
    object = resources.get("object")
    blob = client.bucket(bucket.name).blob(object.name)
    if _preconditions:
        blob.acl.clear(if_metageneration_match=object.metageneration)
    else:
        blob.acl.clear()


########################################################################################################################################
### Method Invocation Mapping ##########################################################################################################
########################################################################################################################################

# Method invocation mapping is a map whose keys are a string describing a standard
# API call (e.g. storage.objects.get) and values are a list of functions which
# wrap library methods that implement these calls. There may be multiple values
# because multiple library methods may use the same call (e.g. get could be a
# read or just a metadata get).

method_mapping = {
    "storage.bucket_acl.list": [bucket_acl_reload],  # S1 start
    "storage.buckets.delete": [bucket_delete],
    "storage.buckets.get": [
        client_get_bucket,
        bucket_reload,
        client_lookup_bucket,
        bucket_exists,
    ],
    "storage.buckets.getIamPolicy": [bucket_get_iam_policy],
    "storage.buckets.insert": [client_create_bucket, bucket_create],
    "storage.buckets.list": [client_list_buckets],
    "storage.buckets.lockRetentionPolicy": [bucket_lock_retention_policy],
    "storage.buckets.testIamPermissions": [bucket_test_iam_permissions],
    "storage.default_object_acl.list": [default_object_acl_reload],
    "storage.hmacKey.delete": [hmac_key_delete],
    "storage.hmacKey.get": [
        client_get_hmac_key_metadata,
        hmac_key_exists,
        hmac_key_reload,
    ],
    "storage.hmacKey.list": [client_list_hmac_keys],
    "storage.notifications.delete": [notification_delete],
    "storage.notifications.get": [
        bucket_get_notification,
        notification_exists,
        notification_reload,
    ],
    "storage.notifications.list": [bucket_list_notifications],
    "storage.object_acl.list": [object_acl_reload],
    "storage.objects.get": [
        bucket_get_blob,
        blob_exists,
        client_download_blob_to_file,
        blob_download_to_filename,
        blob_download_to_filename_chunked,
        blob_download_to_filename_range,
        blob_download_as_bytes,
        blob_download_as_text,
        blobreader_read,
    ],
    "storage.objects.download": [
        client_download_blob_to_file,
        blob_download_to_filename,
        blob_download_to_filename_chunked,
        blob_download_to_filename_range,
        blob_download_as_bytes,
        blob_download_as_text,
        blobreader_read,
    ],
    "storage.objects.list": [client_list_blobs, bucket_list_blobs, bucket_delete],
    "storage.objects.delete": [
        bucket_delete_blob,
        bucket_delete_blobs,
        blob_delete,
    ],
    "storage.serviceaccount.get": [client_get_service_account_email],  # S1 end
    "storage.buckets.patch": [
        bucket_patch,
        bucket_make_public,
        bucket_make_private,
        bucket_acl_save,
        bucket_acl_save_predefined,
        bucket_acl_clear,
        default_object_acl_save,
        default_object_acl_save_predefined,
        default_object_acl_clear,
    ],  # S2/S3 start
    "storage.buckets.setIamPolicy": [bucket_set_iam_policy],
    "storage.buckets.update": [bucket_update],
    "storage.hmacKey.update": [hmac_key_update],
    "storage.objects.compose": [blob_compose],
    "storage.objects.copy": [bucket_copy_blob, bucket_rename_blob],
    "storage.objects.insert": [
        blob_upload_from_string_multipart,
        blobwriter_write_multipart,
        blob_create_resumable_upload_session,
    ],
    "storage.resumable.upload": [
        blob_upload_from_string,
        blob_upload_from_file,
        blob_upload_from_filename,
        blobwriter_write,
    ],
    "storage.objects.patch": [
        blob_patch,
        object_acl_save,
        object_acl_save_predefined,
        object_acl_clear,
        blob_make_private,
        blob_make_public,
    ],
    "storage.objects.rewrite": [blob_rewrite, blob_update_storage_class],
    "storage.objects.update": [blob_update],  # S2/S3 end
    "storage.hmacKey.create": [client_create_hmac_key],  # S4 start
    "storage.notifications.insert": [notification_create],
}


########################################################################################################################################
### Helper Methods for Testbench Retry Test API ########################################################################################
########################################################################################################################################


"""
The Retry Test API in the testbench is used to run the retry conformance tests. It offers a mechanism to describe more complex
retry scenarios while sending a single, constant header through all the HTTP requests from a test program. The Retry Test API
can be accessed by adding the path "/retry-test" to the host. See also: https://github.com/googleapis/storage-testbench
"""


def _create_retry_test(host, method_name, instructions):
    """
    For each test case, initialize a Retry Test resource by loading a set of
    instructions to the testbench host. The instructions include an API method
    and a list of errors. An unique id is created for each Retry Test resource.
    """
    import json

    retry_test_uri = host + "/retry_test"
    headers = {
        "Content-Type": "application/json",
    }
    data_dict = {"instructions": {method_name: instructions}}
    data = json.dumps(data_dict)
    r = requests.post(retry_test_uri, headers=headers, data=data)
    return r.json()


def _get_retry_test(host, id):
    """
    Retrieve the state of the Retry Test resource, including the unique id,
    instructions, and a boolean status "completed". This can be used to verify
    if all instructions were used as expected.
    """
    get_retry_test_uri = f"{host}/retry_test/{id}"
    r = requests.get(get_retry_test_uri)
    return r.json()


def _run_retry_test(
    host,
    id,
    lib_func,
    _preconditions,
    bucket,
    object,
    notification,
    hmac_key,
    file_data,
):
    """
    To execute tests against the list of instrucions sent to the Retry Test API,
    create a client to send the retry test ID using the x-retry-test-id header
    in each request. For incoming requests that match the test ID and API method,
    the testbench will pop off the next instruction from the list and force the
    listed failure case.
    """
    client = storage.Client(
        project=_CONF_TEST_PROJECT_ID,
        credentials=AnonymousCredentials(),
        client_options={"api_endpoint": host},
    )
    client._http.headers.update({"x-retry-test-id": id})
    lib_func(
        client,
        _preconditions,
        bucket=bucket,
        object=object,
        notification=notification,
        hmac_key=hmac_key,
        file_data=file_data,
    )


def _delete_retry_test(host, id):
    """
    Delete the Retry Test resource by id.
    """
    get_retry_test_uri = f"{host}/retry_test/{id}"
    requests.delete(get_retry_test_uri)


########################################################################################################################################
### Run Test Case for Retry Strategy ###################################################################################################
########################################################################################################################################


def run_test_case(
    scenario_id,
    method,
    case,
    lib_func,
    host,
    bucket,
    object,
    notification,
    hmac_key,
    file_data,
):
    scenario = _CONFORMANCE_TESTS[scenario_id - 1]
    expect_success = scenario["expectSuccess"]
    precondition_provided = scenario["preconditionProvided"]
    method_name = method["name"]
    instructions = case["instructions"]

    try:
        r = _create_retry_test(host, method_name, instructions)
        id = r["id"]
    except Exception as e:
        raise Exception(
            f"Error creating retry test for {method_name}: {e}"
        ).with_traceback(e.__traceback__)

    # Run retry tests on library methods.
    try:
        _run_retry_test(
            host,
            id,
            lib_func,
            precondition_provided,
            bucket,
            object,
            notification,
            hmac_key,
            file_data,
        )
    except Exception as e:
        logging.exception(f"Caught an exception while running retry instructions\n {e}")
        success_results = False
    else:
        success_results = True

    # Assert expected success for each scenario.
    assert expect_success == success_results, (
        "Retry API call expected_success was {}, should be {}".format(
            success_results, expect_success
        )
    )

    # Verify that all instructions were used up during the test
    # (indicates that the client sent the correct requests).
    status_response = _get_retry_test(host, id)
    assert status_response["completed"] is True, (
        "Retry test not completed; unused instructions:{}".format(
            status_response["instructions"]
        )
    )

    # Clean up and close out test in testbench.
    _delete_retry_test(host, id)


########################################################################################################################################
### Run Conformance Tests for Retry Strategy ###########################################################################################
########################################################################################################################################

# Pull storage-testbench docker image
subprocess.run(_PULL_CMD)
time.sleep(5)

# Run docker image to start storage-testbench
with subprocess.Popen(_RUN_CMD) as proc:
    # Run retry conformance tests
    for scenario in _CONFORMANCE_TESTS:
        id = scenario["id"]
        methods = scenario["methods"]
        cases = scenario["cases"]
        for i, c in enumerate(cases):
            for m in methods:
                method_name = m["name"]
                method_group = m["group"] if m.get("group", None) else m["name"]
                if method_group not in method_mapping:
                    logging.info(f"No tests for operation {method_name}")
                    continue

                for lib_func in method_mapping[method_group]:
                    test_name = f"test-S{id}-{method_name}-{lib_func.__name__}-{i}"
                    globals()[test_name] = functools.partial(
                        run_test_case, id, m, c, lib_func, _HOST
                    )
    time.sleep(5)
    proc.kill()
