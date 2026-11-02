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
import io
import os
import re
import tempfile

import pytest
from test_utils.vpcsc_config import vpcsc_config

from google.cloud import exceptions

from . import _helpers

dual_data_loc_1 = os.getenv("DUAL_REGION_LOC_1", "US-EAST1")
dual_data_loc_2 = os.getenv("DUAL_REGION_LOC_2", "US-WEST1")
public_bucket = "gcp-public-data-landsat"


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Test does not yet support endpoint override",
)
@vpcsc_config.skip_if_inside_vpcsc
def test_anonymous_client_access_to_public_bucket():
    from google.cloud.storage.client import Client

    anonymous_client = Client.create_anonymous_client()
    bucket = anonymous_client.bucket(public_bucket)
    (blob,) = _helpers.retry_429_503(anonymous_client.list_blobs)(
        bucket,
        max_results=1,
    )
    with tempfile.TemporaryFile() as stream:
        _helpers.retry_429_503(blob.download_to_file)(stream)


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Test does not yet support endpoint override",
)
def test_get_service_account_email(storage_client, service_account):
    domain = "gs-project-accounts.iam.gserviceaccount.com"
    email = storage_client.get_service_account_email()

    new_style = re.compile(r"service-(?P<projnum>[^@]+)@{}".format(domain))
    old_style = re.compile(r"{}@{}".format(storage_client.project, domain))
    patterns = [new_style, old_style]
    matches = [pattern.match(email) for pattern in patterns]

    assert any(match for match in matches if match is not None)


def test_create_bucket_simple(storage_client, buckets_to_delete):
    new_bucket_name = _helpers.unique_name("a-new-bucket")

    with pytest.raises(exceptions.NotFound):
        storage_client.get_bucket(new_bucket_name)

    created = _helpers.retry_429_503(storage_client.create_bucket)(new_bucket_name)
    buckets_to_delete.append(created)

    assert created.name == new_bucket_name


def test_create_bucket_dual_region(storage_client, buckets_to_delete):
    from google.cloud.storage.constants import DUAL_REGION_LOCATION_TYPE

    new_bucket_name = _helpers.unique_name("dual-region-bucket")
    location = "US"

    data_locations = [dual_data_loc_1, dual_data_loc_2]

    with pytest.raises(exceptions.NotFound):
        storage_client.get_bucket(new_bucket_name)

    created = _helpers.retry_429_503(storage_client.create_bucket)(
        new_bucket_name, location=location, data_locations=data_locations
    )
    buckets_to_delete.append(created)

    assert created.name == new_bucket_name
    assert created.location == location
    assert created.location_type == DUAL_REGION_LOCATION_TYPE
    assert created.data_locations == data_locations


def test_list_buckets(storage_client, buckets_to_delete):
    buckets_to_create = [
        _helpers.unique_name("new"),
        _helpers.unique_name("newer"),
        _helpers.unique_name("newest"),
    ]
    created_buckets = []

    for bucket_name in buckets_to_create:
        bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
        buckets_to_delete.append(bucket)

    all_buckets = storage_client.list_buckets()

    created_buckets = [
        bucket.name for bucket in all_buckets if bucket.name in buckets_to_create
    ]

    assert sorted(created_buckets) == sorted(buckets_to_create)


def test_download_blob_to_file_w_uri(
    storage_client,
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    blob = shared_bucket.blob("MyBuffer")
    payload = b"Hello World"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    with tempfile.NamedTemporaryFile() as temp_f:
        with open(temp_f.name, "wb") as file_obj:
            storage_client.download_blob_to_file(
                "gs://" + shared_bucket.name + "/MyBuffer", file_obj
            )

        with open(temp_f.name, "rb") as file_obj:
            stored_contents = file_obj.read()

    assert stored_contents == payload


def test_download_blob_to_file_w_etag(
    storage_client,
    shared_bucket,
    blobs_to_delete,
    service_account,
):
    filename = "kittens"
    blob = shared_bucket.blob(filename)
    payload = b"fluffy"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    buffer = io.BytesIO()
    with pytest.raises(exceptions.NotModified):
        storage_client.download_blob_to_file(
            "gs://" + shared_bucket.name + "/" + filename,
            buffer,
            if_etag_not_match=blob.etag,
        )

    buffer = io.BytesIO()
    with pytest.raises(exceptions.PreconditionFailed):
        storage_client.download_blob_to_file(
            "gs://" + shared_bucket.name + "/" + filename,
            buffer,
            if_etag_match="kittens",
        )

    buffer = io.BytesIO()
    storage_client.download_blob_to_file(
        "gs://" + shared_bucket.name + "/" + filename,
        buffer,
        if_etag_not_match="kittens",
    )
    assert buffer.getvalue() == payload

    buffer = io.BytesIO()
    storage_client.download_blob_to_file(
        "gs://" + shared_bucket.name + "/" + filename,
        buffer,
        if_etag_match=blob.etag,
    )
    assert buffer.getvalue() == payload


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Credentials not yet supported in preprod testing.",
)
def test_client_universe_domain(
    universe_domain_client,
    test_universe_location,
    buckets_to_delete,
    blobs_to_delete,
):
    bucket_name = _helpers.unique_name("gcp-systest-ud")
    ud_bucket = universe_domain_client.create_bucket(
        bucket_name, location=test_universe_location
    )
    buckets_to_delete.append(ud_bucket)

    blob_name = _helpers.unique_name("gcp-systest-ud")
    blob = ud_bucket.blob(blob_name)
    payload = b"The quick brown fox jumps over the lazy dog"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    with tempfile.NamedTemporaryFile() as temp_f:
        with open(temp_f.name, "wb") as file_obj:
            universe_domain_client.download_blob_to_file(blob, file_obj)
        with open(temp_f.name, "rb") as file_obj:
            stored_contents = file_obj.read()

    assert stored_contents == payload


def test_restore_bucket(
    storage_client,
    buckets_to_delete,
):
    from google.cloud.storage.bucket import SoftDeletePolicy

    # Create a bucket with soft delete policy.
    duration_secs = 7 * 86400
    bucket = storage_client.bucket(_helpers.unique_name("w-soft-delete"))
    bucket.soft_delete_policy.retention_duration_seconds = duration_secs
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket)
    buckets_to_delete.append(bucket)

    policy = bucket.soft_delete_policy
    assert isinstance(policy, SoftDeletePolicy)
    assert policy.retention_duration_seconds == duration_secs
    assert isinstance(policy.effective_time, datetime.datetime)

    # Record the bucket's name and generation
    name = bucket.name
    generation = bucket.generation
    assert generation is not None

    # Delete the bucket, then use the generation to get a reference to it again.
    _helpers.retry_429_503(bucket.delete)()
    soft_deleted_bucket = _helpers.retry_429_503(storage_client.get_bucket)(
        name, generation=generation, soft_deleted=True
    )
    assert soft_deleted_bucket.name == name
    assert soft_deleted_bucket.generation == generation
    assert soft_deleted_bucket.soft_delete_time is not None
    assert soft_deleted_bucket.hard_delete_time is not None

    # Restore the bucket.
    restored_bucket = _helpers.retry_429_503(storage_client.restore_bucket)(
        name, generation=generation
    )
    assert restored_bucket.name == name
    assert restored_bucket.generation == generation
    assert restored_bucket.soft_delete_time is None
    assert restored_bucket.hard_delete_time is None
