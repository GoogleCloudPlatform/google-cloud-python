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

import pytest
from google.api_core import exceptions

from google.cloud.storage.bucket import EncryptionEnforcementConfig
from google.cloud.storage.constants import (
    ENFORCEMENT_MODE_FULLY_RESTRICTED,
    ENFORCEMENT_MODE_NOT_RESTRICTED,
)
from google.cloud.storage.ip_filter import (
    IPFilter,
    PublicNetworkSource,
    VpcNetworkSource,
)

from . import _helpers


def test_bucket_create_w_alt_storage_class(storage_client, buckets_to_delete):
    from google.cloud.storage import constants

    bucket_name = _helpers.unique_name("bucket-w-archive")

    with pytest.raises(exceptions.NotFound):
        storage_client.get_bucket(bucket_name)

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = constants.ARCHIVE_STORAGE_CLASS

    _helpers.retry_429_503(bucket.create)()
    buckets_to_delete.append(bucket)

    created = storage_client.get_bucket(bucket_name)
    assert created.storage_class == constants.ARCHIVE_STORAGE_CLASS


def test_bucket_lifecycle_rules(storage_client, buckets_to_delete):
    from google.cloud.storage import constants
    from google.cloud.storage.bucket import (
        LifecycleRuleAbortIncompleteMultipartUpload,
        LifecycleRuleDelete,
        LifecycleRuleSetStorageClass,
    )

    bucket_name = _helpers.unique_name("w-lifcycle-rules")
    custom_time_before = datetime.date(2018, 8, 1)
    noncurrent_before = datetime.date(2018, 8, 1)
    matches_prefix = ["storage-sys-test", "gcs-sys-test"]
    matches_suffix = ["suffix-test"]

    with pytest.raises(exceptions.NotFound):
        storage_client.get_bucket(bucket_name)

    bucket = storage_client.bucket(bucket_name)
    bucket.add_lifecycle_delete_rule(
        age=42,
        number_of_newer_versions=3,
        days_since_custom_time=2,
        custom_time_before=custom_time_before,
        days_since_noncurrent_time=2,
        noncurrent_time_before=noncurrent_before,
        matches_prefix=matches_prefix,
        matches_suffix=matches_suffix,
    )
    bucket.add_lifecycle_set_storage_class_rule(
        constants.COLDLINE_STORAGE_CLASS,
        is_live=False,
        matches_storage_class=[constants.NEARLINE_STORAGE_CLASS],
    )
    bucket.add_lifecycle_abort_incomplete_multipart_upload_rule(
        age=42,
    )

    expected_rules = [
        LifecycleRuleDelete(
            age=42,
            number_of_newer_versions=3,
            days_since_custom_time=2,
            custom_time_before=custom_time_before,
            days_since_noncurrent_time=2,
            noncurrent_time_before=noncurrent_before,
            matches_prefix=matches_prefix,
            matches_suffix=matches_suffix,
        ),
        LifecycleRuleSetStorageClass(
            constants.COLDLINE_STORAGE_CLASS,
            is_live=False,
            matches_storage_class=[constants.NEARLINE_STORAGE_CLASS],
        ),
        LifecycleRuleAbortIncompleteMultipartUpload(
            age=42,
        ),
    ]

    _helpers.retry_429_503(bucket.create)(location="us")
    buckets_to_delete.append(bucket)

    assert bucket.name == bucket_name
    assert list(bucket.lifecycle_rules) == expected_rules

    # Test modifying lifecycle rules
    expected_rules[0] = LifecycleRuleDelete(
        age=30,
        matches_prefix=["new-prefix"],
        matches_suffix=["new-suffix"],
    )
    rules = list(bucket.lifecycle_rules)
    rules[0]["condition"] = {
        "age": 30,
        "matchesPrefix": ["new-prefix"],
        "matchesSuffix": ["new-suffix"],
    }
    bucket.lifecycle_rules = rules
    bucket.patch()

    assert list(bucket.lifecycle_rules) == expected_rules

    # Test clearing lifecycle rules
    bucket.clear_lifecyle_rules()
    bucket.patch()

    assert list(bucket.lifecycle_rules) == []


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Test does not yet support endpoint override",
)
def test_bucket_update_labels(storage_client, buckets_to_delete):
    bucket_name = _helpers.unique_name("update-labels")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)
    assert bucket.exists()

    updated_labels = {"test-label": "label-value"}
    bucket.labels = updated_labels
    bucket.update()
    assert bucket.labels == updated_labels

    new_labels = {"another-label": "another-value"}
    bucket.labels = new_labels
    bucket.patch()
    assert bucket.labels == new_labels

    bucket.labels = {}
    # See https://github.com/googleapis/python-storage/issues/541
    retry_400 = _helpers.RetryErrors(exceptions.BadRequest)
    retry_400(bucket.update)()
    assert bucket.labels == {}


def test_bucket_get_set_iam_policy(
    storage_client,
    buckets_to_delete,
    service_account,
):
    from google.api_core.exceptions import BadRequest, PreconditionFailed

    from google.cloud.storage.iam import STORAGE_OBJECT_VIEWER_ROLE

    bucket_name = _helpers.unique_name("iam-policy")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)
    assert bucket.exists()

    policy_no_version = bucket.get_iam_policy()
    assert policy_no_version.version == 1

    policy = bucket.get_iam_policy(requested_policy_version=3)
    assert policy == policy_no_version

    member = f"serviceAccount:{storage_client.get_service_account_email()}"

    binding_w_condition = {
        "role": STORAGE_OBJECT_VIEWER_ROLE,
        "members": {member},
        "condition": {
            "title": "always-true",
            "description": "test condition always-true",
            "expression": "true",
        },
    }
    policy.bindings.append(binding_w_condition)

    with pytest.raises(PreconditionFailed, match="enable uniform bucket-level access"):
        bucket.set_iam_policy(policy)

    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket.patch()

    policy = bucket.get_iam_policy(requested_policy_version=3)
    policy.bindings.append(binding_w_condition)

    with pytest.raises(BadRequest, match="at least 3"):
        bucket.set_iam_policy(policy)

    policy.version = 3
    returned_policy = bucket.set_iam_policy(policy)
    assert returned_policy.version == 3
    assert returned_policy.bindings == policy.bindings

    fetched_policy = bucket.get_iam_policy(requested_policy_version=3)
    assert fetched_policy.bindings == returned_policy.bindings


def test_bucket_crud_w_requester_pays(storage_client, buckets_to_delete, user_project):
    bucket_name = _helpers.unique_name("w-requester-pays")
    created = _helpers.retry_429_503(storage_client.create_bucket)(
        bucket_name, requester_pays=True
    )
    buckets_to_delete.append(created)
    assert created.name == bucket_name
    assert created.requester_pays

    with_user_project = storage_client.bucket(
        bucket_name,
        user_project=user_project,
    )

    try:
        # Exercise 'buckets.get' w/ userProject.
        assert with_user_project.exists()
        with_user_project.reload()
        assert with_user_project.requester_pays

        # Exercise 'buckets.patch' w/ userProject.
        with_user_project.configure_website(
            main_page_suffix="index.html", not_found_page="404.html"
        )
        with_user_project.patch()
        expected_website = {"mainPageSuffix": "index.html", "notFoundPage": "404.html"}
        assert with_user_project._properties["website"] == expected_website

        # Exercise 'buckets.update' w/ userProject.
        new_labels = {"another-label": "another-value"}
        with_user_project.labels = new_labels
        with_user_project.update()
        assert with_user_project.labels == new_labels

    finally:
        # Exercise 'buckets.delete' w/ userProject.
        with_user_project.delete()
        buckets_to_delete.remove(created)


def test_bucket_acls_iam_w_user_project(
    storage_client, buckets_to_delete, user_project
):
    bucket_name = _helpers.unique_name("acl-w-user-project")
    created = _helpers.retry_429_503(storage_client.create_bucket)(
        bucket_name,
        requester_pays=True,
    )
    buckets_to_delete.append(created)

    with_user_project = storage_client.bucket(bucket_name, user_project=user_project)

    # Exercise bucket ACL w/ userProject
    acl = with_user_project.acl
    acl.reload()
    acl.all().grant_read()
    acl.save()
    assert "READER" in acl.all().get_roles()

    del acl.entities["allUsers"]
    acl.save()
    assert not acl.has_entity("allUsers")

    # Exercise default object ACL w/ userProject
    doa = with_user_project.default_object_acl
    doa.reload()
    doa.all().grant_read()
    doa.save()
    assert "READER" in doa.all().get_roles()

    # Exercise IAM w/ userProject
    test_permissions = ["storage.buckets.get"]
    found = with_user_project.test_iam_permissions(test_permissions)
    assert found == test_permissions

    policy = with_user_project.get_iam_policy()
    viewers = policy.setdefault("roles/storage.objectViewer", set())
    viewers.add(policy.all_users())
    with_user_project.set_iam_policy(policy)


def test_bucket_acls_w_metageneration_match(storage_client, buckets_to_delete):
    wrong_metageneration_number = 9
    bucket_name = _helpers.unique_name("acl-w-metageneration-match")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    # Exercise bucket ACL with metageneration match
    acl = bucket.acl
    acl.group("cloud-developer-relations@google.com").grant_read()
    bucket.reload()

    with pytest.raises(exceptions.PreconditionFailed):
        acl.save(if_metageneration_match=wrong_metageneration_number)
        assert (
            "READER"
            not in acl.group("cloud-developer-relations@google.com").get_roles()
        )

    acl.save(if_metageneration_match=bucket.metageneration)
    assert "READER" in acl.group("cloud-developer-relations@google.com").get_roles()

    # Exercise default object ACL w/ metageneration match
    doa = bucket.default_object_acl
    doa.group("cloud-developer-relations@google.com").grant_owner()
    bucket.reload()

    with pytest.raises(exceptions.PreconditionFailed):
        doa.save(if_metageneration_match=wrong_metageneration_number)
        assert (
            "OWNER" not in doa.group("cloud-developer-relations@google.com").get_roles()
        )

    doa.save(if_metageneration_match=bucket.metageneration)
    assert "OWNER" in doa.group("cloud-developer-relations@google.com").get_roles()


def test_bucket_copy_blob(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
    user_project,
):
    payload = b"DEADBEEF"
    bucket_name = _helpers.unique_name("copy-blob")
    created = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(created)
    assert created.name == bucket_name

    blob = created.blob("CloudLogo")
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    new_blob = _helpers.retry_bad_copy(created.copy_blob)(
        blob, created, "CloudLogoCopy"
    )
    blobs_to_delete.append(new_blob)

    copied_contents = new_blob.download_as_bytes()
    assert copied_contents == payload


def test_bucket_copy_blob_w_destination_contexts(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    from google.cloud.storage.blob import ObjectContexts, ObjectCustomContextPayload

    payload = b"DEADBEEF"
    bucket_name = _helpers.unique_name("copy-blob-contexts")
    created = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(created)
    assert created.name == bucket_name

    blob = created.blob("CloudLogo")
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    context_payload = ObjectCustomContextPayload(value="bar")
    contexts = ObjectContexts(None, custom={"foo": context_payload})

    new_blob = _helpers.retry_bad_copy(created.copy_blob)(
        blob, created, "CloudLogoCopy", destination_contexts=contexts
    )
    blobs_to_delete.append(new_blob)

    copied_contents = new_blob.download_as_bytes()
    assert copied_contents == payload
    new_blob.reload()
    assert new_blob.contexts.custom["foo"].value == "bar"


def test_bucket_copy_blob_w_user_project(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
    user_project,
):
    payload = b"DEADBEEF"
    bucket_name = _helpers.unique_name("copy-w-requester-pays")
    created = _helpers.retry_429_503(storage_client.create_bucket)(
        bucket_name, requester_pays=True
    )
    buckets_to_delete.append(created)
    assert created.name == bucket_name
    assert created.requester_pays

    blob = created.blob("simple")
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    with_user_project = storage_client.bucket(bucket_name, user_project=user_project)

    new_blob = _helpers.retry_bad_copy(with_user_project.copy_blob)(
        blob, with_user_project, "simple-copy"
    )
    blobs_to_delete.append(new_blob)

    assert new_blob.download_as_bytes() == payload


def test_bucket_copy_blob_w_generation_match(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    payload = b"DEADBEEF"
    bucket_name = _helpers.unique_name("generation-match")
    created = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(created)
    assert created.name == bucket_name

    blob = created.blob("simple")
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    dest_bucket = storage_client.bucket(bucket_name)

    new_blob = dest_bucket.copy_blob(
        blob,
        dest_bucket,
        "simple-copy",
        if_source_generation_match=blob.generation,
    )
    blobs_to_delete.append(new_blob)

    assert new_blob.download_as_bytes() == payload


def test_bucket_copy_blob_w_metageneration_match(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    payload = b"DEADBEEF"
    bucket_name = _helpers.unique_name("generation-match")
    bucket = storage_client.bucket(bucket_name)
    bucket.requester_pays = True
    created = _helpers.retry_429_503(storage_client.create_bucket)(bucket)
    buckets_to_delete.append(created)
    assert created.name == bucket_name

    blob = created.blob("simple")
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    dest_bucket = storage_client.bucket(bucket_name)

    new_blob = dest_bucket.copy_blob(
        blob,
        dest_bucket,
        "simple-copy",
        if_source_metageneration_match=blob.metageneration,
    )
    blobs_to_delete.append(new_blob)

    assert new_blob.download_as_bytes() == payload


def test_bucket_move_blob_hns(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    payload = b"move_blob_test"

    # Feature currently only works on HNS buckets, so create one here
    bucket_name = _helpers.unique_name("move-blob-hns-enabled")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket_obj.hierarchical_namespace_enabled = True
    bucket_obj.iam_configuration.uniform_bucket_level_access_enabled = True
    created = _helpers.retry_429_503(storage_client.create_bucket)(bucket_obj)
    buckets_to_delete.append(created)
    assert created.hierarchical_namespace_enabled is True

    source = created.blob("source")
    source_gen = source.generation
    source.upload_from_string(payload)
    blobs_to_delete.append(source)

    dest = created.move_blob(
        source,
        "dest",
        if_source_generation_match=source.generation,
        if_source_metageneration_match=source.metageneration,
    )
    blobs_to_delete.append(dest)

    assert dest.download_as_bytes() == payload
    assert dest.generation is not None
    assert source_gen != dest.generation


def test_bucket_move_blob_with_name_needs_encoding(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    payload = b"move_blob_with_name_which_has_a_char_that_needs_url_encoding"

    bucket_name = _helpers.unique_name("move-blob")
    bucket_obj = storage_client.bucket(bucket_name)
    created = _helpers.retry_429_503(storage_client.create_bucket)(bucket_obj)
    buckets_to_delete.append(created)

    source = created.blob("source")
    source_gen = source.generation
    source.upload_from_string(payload)
    blobs_to_delete.append(source)

    dest = created.move_blob(
        source,
        "dest/dest_file.txt",
        if_source_generation_match=source.generation,
        if_source_metageneration_match=source.metageneration,
    )
    blobs_to_delete.append(dest)

    assert dest.download_as_bytes() == payload
    assert dest.generation is not None
    assert source_gen != dest.generation


def test_bucket_get_blob_with_user_project(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
    user_project,
):
    blob_name = "blob-name"
    payload = b"DEADBEEF"
    bucket_name = _helpers.unique_name("w-requester-pays")
    created = _helpers.retry_429_503(storage_client.create_bucket)(
        bucket_name, requester_pays=True
    )
    buckets_to_delete.append(created)
    assert created.name == bucket_name
    assert created.requester_pays

    with_user_project = storage_client.bucket(bucket_name, user_project=user_project)

    assert with_user_project.get_blob("nonesuch") is None

    to_add = created.blob(blob_name)
    to_add.upload_from_string(payload)
    blobs_to_delete.append(to_add)

    found = with_user_project.get_blob(blob_name)
    assert found.download_as_bytes() == payload


@_helpers.retry_failures
def test_bucket_list_blobs(listable_bucket, listable_filenames):
    all_blobs = list(listable_bucket.list_blobs())
    assert sorted(blob.name for blob in all_blobs) == sorted(listable_filenames)


@_helpers.retry_failures
def test_bucket_list_blobs_w_user_project(
    storage_client,
    listable_bucket,
    listable_filenames,
    user_project,
):
    with_user_project = storage_client.bucket(
        listable_bucket.name, user_project=user_project
    )
    all_blobs = list(with_user_project.list_blobs())
    assert sorted(blob.name for blob in all_blobs) == sorted(listable_filenames)


@_helpers.retry_failures
def test_bucket_list_blobs_paginated(listable_bucket, listable_filenames):
    truncation_size = 1
    count = len(listable_filenames) - truncation_size
    iterator = listable_bucket.list_blobs(max_results=count)
    page_iter = iterator.pages

    page1 = next(page_iter)
    blobs = list(page1)
    assert len(blobs) == count
    assert iterator.next_page_token is not None
    # Technically the iterator is exhausted.
    assert iterator.num_results == iterator.max_results
    # But we modify the iterator to continue paging after
    # artificially stopping after ``count`` items.
    iterator.max_results = None

    page2 = next(page_iter)
    last_blobs = list(page2)
    assert len(last_blobs) == truncation_size


@_helpers.retry_failures
def test_bucket_list_blobs_paginated_w_offset(listable_bucket, listable_filenames):
    truncation_size = 1
    inclusive_start_offset = listable_filenames[1]
    exclusive_end_offset = listable_filenames[-1]
    desired_files = listable_filenames[1:-1]
    count = len(desired_files) - truncation_size
    iterator = listable_bucket.list_blobs(
        max_results=count,
        start_offset=inclusive_start_offset,
        end_offset=exclusive_end_offset,
    )
    page_iter = iterator.pages

    page1 = next(page_iter)
    blobs = list(page1)
    assert len(blobs) == count
    assert blobs[0].name == desired_files[0]
    assert iterator.next_page_token is not None
    # Technically the iterator is exhausted.
    assert iterator.num_results == iterator.max_results
    # But we modify the iterator to continue paging after
    # artificially stopping after ``count`` items.
    iterator.max_results = None

    page2 = next(page_iter)
    last_blobs = list(page2)
    assert len(last_blobs) == truncation_size
    assert last_blobs[-1].name == desired_files[-1]


@_helpers.retry_failures
def test_blob_exists_hierarchy(hierarchy_bucket, hierarchy_filenames):
    for filename in hierarchy_filenames:
        blob = hierarchy_bucket.blob(filename)
        assert blob.exists()


@_helpers.retry_failures
def test_bucket_list_blobs_hierarchy_root_level(hierarchy_bucket, hierarchy_filenames):
    expected_names = ["file01.txt"]
    expected_prefixes = set(["parent/"])

    iterator = hierarchy_bucket.list_blobs(delimiter="/")
    page = next(iterator.pages)
    blobs = list(page)

    assert [blob.name for blob in blobs] == expected_names
    assert iterator.next_page_token is None
    assert iterator.prefixes == expected_prefixes


@_helpers.retry_failures
def test_bucket_list_blobs_hierarchy_first_level(hierarchy_bucket, hierarchy_filenames):
    expected_names = ["parent/", "parent/file11.txt"]
    expected_prefixes = set(["parent/child/"])

    iterator = hierarchy_bucket.list_blobs(delimiter="/", prefix="parent/")
    page = next(iterator.pages)
    blobs = list(page)

    assert [blob.name for blob in blobs] == expected_names
    assert iterator.next_page_token is None
    assert iterator.prefixes == expected_prefixes


@_helpers.retry_failures
def test_bucket_list_blobs_hierarchy_second_level(
    hierarchy_bucket, hierarchy_filenames
):
    expected_names = ["parent/child/file21.txt", "parent/child/file22.txt"]
    expected_prefixes = set(["parent/child/grand/", "parent/child/other/"])

    iterator = hierarchy_bucket.list_blobs(delimiter="/", prefix="parent/child/")
    page = next(iterator.pages)
    blobs = list(page)
    assert [blob.name for blob in blobs] == expected_names
    assert iterator.next_page_token is None
    assert iterator.prefixes == expected_prefixes


@_helpers.retry_failures
def test_bucket_list_blobs_hierarchy_third_level(hierarchy_bucket, hierarchy_filenames):
    # Pseudo-hierarchy can be arbitrarily deep, subject to the limit
    # of 1024 characters in the UTF-8 encoded name:
    # https://cloud.google.com/storage/docs/bucketnaming#objectnames
    # Exercise a layer deeper to illustrate this.
    expected_names = ["parent/child/grand/file31.txt"]
    expected_prefixes = set()

    iterator = hierarchy_bucket.list_blobs(delimiter="/", prefix="parent/child/grand/")
    page = next(iterator.pages)
    blobs = list(page)

    assert [blob.name for blob in blobs] == expected_names
    assert iterator.next_page_token is None
    assert iterator.prefixes == expected_prefixes


@_helpers.retry_failures
def test_bucket_list_blobs_hierarchy_w_include_trailing_delimiter(
    hierarchy_bucket,
    hierarchy_filenames,
):
    expected_names = ["file01.txt", "parent/"]
    expected_prefixes = set(["parent/"])

    iterator = hierarchy_bucket.list_blobs(
        delimiter="/", include_trailing_delimiter=True
    )
    page = next(iterator.pages)
    blobs = list(page)

    assert [blob.name for blob in blobs] == expected_names
    assert iterator.next_page_token is None
    assert iterator.prefixes == expected_prefixes


@_helpers.retry_failures
def test_bucket_list_blobs_w_match_glob(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    bucket_name = _helpers.unique_name("w-matchglob")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    payload = b"helloworld"
    blob_names = ["foo/bar", "foo/baz", "foo/foobar", "foobar"]
    for name in blob_names:
        blob = bucket.blob(name)
        blob.upload_from_string(payload)
        blobs_to_delete.append(blob)

    match_glob_results = {
        "foo*bar": ["foobar"],
        "foo**bar": ["foo/bar", "foo/foobar", "foobar"],
        "**/foobar": ["foo/foobar", "foobar"],
        "*/ba[rz]": ["foo/bar", "foo/baz"],
        "*/ba[!a-y]": ["foo/baz"],
        "**/{foobar,baz}": ["foo/baz", "foo/foobar", "foobar"],
        "foo/{foo*,*baz}": ["foo/baz", "foo/foobar"],
    }
    for match_glob, expected_names in match_glob_results.items():
        blob_iter = bucket.list_blobs(match_glob=match_glob)
        blobs = list(blob_iter)
        assert [blob.name for blob in blobs] == expected_names


@_helpers.retry_failures
def test_bucket_list_blobs_w_filter(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    from google.cloud.storage.blob import ObjectContexts, ObjectCustomContextPayload

    bucket_name = _helpers.unique_name("w-filter")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    payload = b"helloworld"
    blob_names = ["foo", "bar", "baz", "qux"]
    for name in blob_names:
        blob = bucket.blob(name)
        blob.upload_from_string(payload)
        if name == "bar":
            custom = {"target": ObjectCustomContextPayload(value="match")}
            blob.contexts = ObjectContexts(blob, custom=custom)
            blob.patch()
        if name == "qux":
            custom = {"target": ObjectCustomContextPayload(value="nomatch")}
            blob.contexts = ObjectContexts(blob, custom=custom)
            blob.patch()
        blobs_to_delete.append(blob)

    # List with filter matching only 'bar'
    blob_iter = bucket.list_blobs(filter_='contexts."target"="match"')
    blobs = list(blob_iter)
    assert [blob.name for blob in blobs] == ["bar"]

    # List with filter matching bar and qux
    blob_iter = bucket.list_blobs(filter_='contexts."target":*')
    blobs = list(blob_iter)
    assert sorted([blob.name for blob in blobs]) == ["bar", "qux"]

    # List with filter matching all except 'bar'
    blob_iter = bucket.list_blobs(filter_='-contexts."target"="match"')
    blobs = list(blob_iter)
    assert sorted([blob.name for blob in blobs]) == ["baz", "foo", "qux"]

    # List with filter matching 'foo' and 'baz' (those without target context)
    blob_iter = bucket.list_blobs(filter_='-contexts."target":*')
    blobs = list(blob_iter)
    assert sorted([blob.name for blob in blobs]) == ["baz", "foo"]


def test_bucket_list_blobs_include_managed_folders(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
    hierarchy_filenames,
):
    bucket_name = _helpers.unique_name("ubla-mf")
    bucket = storage_client.bucket(bucket_name)
    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    _helpers.retry_429_503(bucket.create)()
    buckets_to_delete.append(bucket)

    payload = b"helloworld"
    for filename in hierarchy_filenames:
        blob = bucket.blob(filename)
        blob.upload_from_string(payload)
        blobs_to_delete.append(blob)

    # Make API call to create a managed folder.
    # TODO: change to use storage control client once available.
    path = f"/b/{bucket_name}/managedFolders"
    properties = {"name": "managedfolder1"}
    storage_client._post_resource(path, properties)

    expected_prefixes = set(["parent/"])
    blob_iter = bucket.list_blobs(delimiter="/")
    list(blob_iter)
    assert blob_iter.prefixes == expected_prefixes

    # Test that managed folders are only included when IncludeFoldersAsPrefixes is set.
    expected_prefixes = set(["parent/", "managedfolder1/"])
    blob_iter = bucket.list_blobs(delimiter="/", include_folders_as_prefixes=True)
    list(blob_iter)
    assert blob_iter.prefixes == expected_prefixes

    # Cleanup: API call to delete a managed folder.
    # TODO: change to use storage control client once available.
    path = f"/b/{bucket_name}/managedFolders/managedfolder1"
    storage_client._delete_resource(path)


def test_bucket_update_retention_period(
    storage_client,
    buckets_to_delete,
):
    period_secs = 3
    bucket_name = _helpers.unique_name("w-retention-period")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    bucket.retention_period = period_secs
    bucket.default_event_based_hold = False
    bucket.patch()

    # Changes to the bucket will be readable immediately after writing,
    # but configuration changes may take time to propagate.
    _helpers.retry_has_retention_period(bucket.reload)()

    assert bucket.retention_period == period_secs
    assert isinstance(bucket.retention_policy_effective_time, datetime.datetime)
    assert not bucket.default_event_based_hold
    assert not bucket.retention_policy_locked

    bucket.retention_period = None
    bucket.patch()

    # Changes to the bucket will be readable immediately after writing,
    # but configuration changes may take time to propagate.
    _helpers.retry_no_retention_period(bucket.reload)()

    assert bucket.retention_period is None
    assert bucket.retention_policy_effective_time is None
    assert not bucket.default_event_based_hold
    assert not bucket.retention_policy_locked


def test_delete_object_bucket_w_retention_period(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    # Create a bucket with retention period.
    period_secs = 12
    bucket = storage_client.bucket(_helpers.unique_name("w-retention-period"))
    bucket.retention_period = period_secs
    bucket.default_event_based_hold = False
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket)
    buckets_to_delete.append(bucket)

    _helpers.retry_has_retention_period(bucket.reload)()
    assert bucket.retention_period == period_secs
    assert isinstance(bucket.retention_policy_effective_time, datetime.datetime)

    payload = b"DEADBEEF"
    blob = bucket.blob(_helpers.unique_name("w-retention"))
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    _helpers.retry_has_retention_expiration(blob.reload)()
    assert isinstance(blob.retention_expiration_time, datetime.datetime)
    assert not blob.event_based_hold
    assert not blob.temporary_hold

    # Attempts to delete objects whose age is less than the retention period should fail.
    with pytest.raises(exceptions.Forbidden):
        blob.delete()

    # Object can be deleted once it reaches the age defined in the retention policy.
    _helpers.await_config_changes_propagate(sec=period_secs)
    blob.delete()
    blobs_to_delete.pop()


def test_bucket_w_default_event_based_hold(
    storage_client,
    blobs_to_delete,
    default_ebh_bucket,
):
    bucket = storage_client.get_bucket(default_ebh_bucket)
    assert bucket.default_event_based_hold
    assert bucket.retention_period is None
    assert bucket.retention_policy_effective_time is None
    assert not bucket.retention_policy_locked

    blob_name = "test-blob"
    payload = b"DEADBEEF"
    blob = bucket.blob(blob_name)
    blob.upload_from_string(payload)

    blobs_to_delete.append(blob)

    other = bucket.get_blob(blob_name)

    assert other.event_based_hold
    assert not other.temporary_hold
    assert other.retention_expiration_time is None

    with pytest.raises(exceptions.Forbidden):
        other.delete()

    other.event_based_hold = False
    other.patch()
    other.delete()

    bucket.default_event_based_hold = False
    bucket.patch()

    assert not bucket.default_event_based_hold
    assert bucket.retention_period is None
    assert bucket.retention_policy_effective_time is None
    assert not bucket.retention_policy_locked

    # Changes to the bucket will be readable immediately after writing,
    # but configuration changes may take time to propagate.
    _helpers.await_config_changes_propagate()

    blob.upload_from_string(payload)

    # https://github.com/googleapis/python-storage/issues/435
    _helpers.retry_no_event_based_hold(blob.reload)()

    assert not blob.event_based_hold
    assert not blob.temporary_hold
    assert blob.retention_expiration_time is None

    blob.delete()
    blobs_to_delete.pop()


def test_blob_w_temporary_hold(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    bucket_name = _helpers.unique_name("w-tmp-hold")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    blob_name = "test-blob"
    payload = b"DEADBEEF"
    blob = bucket.blob(blob_name)
    blob.upload_from_string(payload)

    blobs_to_delete.append(blob)

    other = bucket.get_blob(blob_name)
    other.temporary_hold = True
    other.patch()

    assert other.temporary_hold
    assert not other.event_based_hold
    assert other.retention_expiration_time is None

    with pytest.raises(exceptions.Forbidden):
        other.delete()

    other.temporary_hold = False
    other.patch()

    other.delete()
    blobs_to_delete.pop()


def test_bucket_lock_retention_policy(
    storage_client,
    buckets_to_delete,
):
    period_secs = 10
    bucket_name = _helpers.unique_name("loc-ret-policy")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    bucket.retention_period = period_secs
    bucket.patch()

    assert bucket.retention_period == period_secs
    assert isinstance(bucket.retention_policy_effective_time, datetime.datetime)
    assert not bucket.default_event_based_hold
    assert not bucket.retention_policy_locked

    bucket.lock_retention_policy()

    bucket.reload()
    assert bucket.retention_policy_locked

    bucket.retention_period = None
    with pytest.raises(exceptions.Forbidden):
        bucket.patch()


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Test does not yet support endpoint override",
)
def test_new_bucket_w_ubla(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    bucket_name = _helpers.unique_name("new-w-ubla")
    bucket = storage_client.bucket(bucket_name)
    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    _helpers.retry_429_503(bucket.create)()
    buckets_to_delete.append(bucket)

    bucket_acl = bucket.acl
    with pytest.raises(exceptions.BadRequest):
        bucket_acl.reload()

    bucket_acl.loaded = True  # Fake that we somehow loaded the ACL
    bucket_acl.group("cloud-developer-relations@google.com").grant_read()
    with pytest.raises(exceptions.BadRequest):
        bucket_acl.save()

    blob_name = "my-blob.txt"
    blob = bucket.blob(blob_name)
    payload = b"DEADBEEF"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    found = bucket.get_blob(blob_name)
    assert found.download_as_bytes() == payload

    blob_acl = blob.acl
    with pytest.raises(exceptions.BadRequest):
        blob_acl.reload()

    blob_acl.loaded = True  # Fake that we somehow loaded the ACL
    blob_acl.group("cloud-developer-relations@google.com").grant_read()
    with pytest.raises(exceptions.BadRequest):
        blob_acl.save()


def test_ubla_set_unset_preserves_acls(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    bucket_name = _helpers.unique_name("ubla-acls")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    blob_name = "my-blob.txt"
    blob = bucket.blob(blob_name)
    payload = b"DEADBEEF"
    blob.upload_from_string(payload)
    blobs_to_delete.append(blob)

    # Preserve ACLs before setting UBLA
    bucket_acl_before = list(bucket.acl)
    blob_acl_before = list(bucket.acl)

    # Set UBLA
    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket.patch()

    assert bucket.iam_configuration.uniform_bucket_level_access_enabled

    # While UBLA is set, cannot get / set ACLs
    with pytest.raises(exceptions.BadRequest):
        bucket.acl.reload()

    # Clear UBLA
    bucket.iam_configuration.uniform_bucket_level_access_enabled = False
    bucket.patch()
    _helpers.await_config_changes_propagate()

    # Query ACLs after clearing UBLA
    bucket.acl.reload()
    bucket_acl_after = list(bucket.acl)
    blob.acl.reload()
    blob_acl_after = list(bucket.acl)

    assert bucket_acl_before == bucket_acl_after
    assert blob_acl_before == blob_acl_after


def test_new_bucket_created_w_inherited_pap(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    from google.cloud.storage import constants

    bucket_name = _helpers.unique_name("new-w-pap-inherited")
    bucket = storage_client.bucket(bucket_name)
    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket.create()
    buckets_to_delete.append(bucket)

    # TODO: Remove unspecified after changeover is complete
    assert bucket.iam_configuration.public_access_prevention in [
        constants.PUBLIC_ACCESS_PREVENTION_UNSPECIFIED,
        constants.PUBLIC_ACCESS_PREVENTION_INHERITED,
    ]

    bucket.iam_configuration.public_access_prevention = (
        constants.PUBLIC_ACCESS_PREVENTION_ENFORCED
    )
    bucket.patch()
    assert (
        bucket.iam_configuration.public_access_prevention
        == constants.PUBLIC_ACCESS_PREVENTION_ENFORCED
    )
    assert bucket.iam_configuration.uniform_bucket_level_access_enabled

    bucket.iam_configuration.uniform_bucket_level_access_enabled = False
    bucket.patch()

    _helpers.await_config_changes_propagate()

    assert (
        bucket.iam_configuration.public_access_prevention
        == constants.PUBLIC_ACCESS_PREVENTION_ENFORCED
    )

    with pytest.raises(exceptions.BadRequest):
        bucket.iam_configuration.public_access_prevention = "unexpected value"
        bucket.patch()

    with pytest.raises(exceptions.PreconditionFailed):
        bucket.make_public()

    blob_name = "my-blob.txt"
    blob = bucket.blob(blob_name)
    payload = b"DEADBEEF"
    blob.upload_from_string(payload)

    with pytest.raises(exceptions.PreconditionFailed):
        blob.make_public()


@pytest.mark.skip(reason="Unspecified PAP is changing to inherited")
def test_new_bucket_created_w_enforced_pap(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    from google.cloud.storage import constants

    bucket_name = _helpers.unique_name("new-w-pap-enforced")
    bucket = storage_client.bucket(bucket_name)
    bucket.iam_configuration.public_access_prevention = (
        constants.PUBLIC_ACCESS_PREVENTION_ENFORCED
    )
    bucket.create()
    buckets_to_delete.append(bucket)

    assert (
        bucket.iam_configuration.public_access_prevention
        == constants.PUBLIC_ACCESS_PREVENTION_ENFORCED
    )

    bucket.iam_configuration.public_access_prevention = (
        constants.PUBLIC_ACCESS_PREVENTION_INHERITED
    )
    bucket.patch()

    # TODO: Remove unspecified after changeover is complete
    assert bucket.iam_configuration.public_access_prevention in [
        constants.PUBLIC_ACCESS_PREVENTION_UNSPECIFIED,
        constants.PUBLIC_ACCESS_PREVENTION_INHERITED,
    ]
    assert not bucket.iam_configuration.uniform_bucket_level_access_enabled


@pytest.mark.skipif(
    _helpers.is_api_endpoint_override,
    reason="Test does not yet support endpoint override",
)
def test_new_bucket_with_rpo(
    storage_client,
    buckets_to_delete,
    blobs_to_delete,
):
    from google.cloud.storage import constants

    bucket_name = _helpers.unique_name("new-w-turbo-replication")
    bucket = storage_client.create_bucket(bucket_name, location="NAM4")
    buckets_to_delete.append(bucket)

    assert bucket.rpo == constants.RPO_DEFAULT

    bucket.rpo = constants.RPO_ASYNC_TURBO
    bucket.patch()

    bucket_from_server = storage_client.get_bucket(bucket_name)

    assert bucket_from_server.rpo == constants.RPO_ASYNC_TURBO


def test_new_bucket_with_autoclass(
    storage_client,
    buckets_to_delete,
):
    from google.cloud.storage import constants

    # Autoclass can be enabled via bucket create
    bucket_name = _helpers.unique_name("new-w-autoclass")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket_obj.autoclass_enabled = True
    bucket = storage_client.create_bucket(bucket_obj)
    previous_toggle_time = bucket.autoclass_toggle_time
    buckets_to_delete.append(bucket)

    # Autoclass terminal_storage_class is defaulted to NEARLINE if not specified
    assert bucket.autoclass_enabled is True
    assert bucket.autoclass_terminal_storage_class == constants.NEARLINE_STORAGE_CLASS

    # Autoclass can be enabled/disabled via bucket patch
    bucket.autoclass_enabled = False
    bucket.patch(if_metageneration_match=bucket.metageneration)

    assert bucket.autoclass_enabled is False
    assert bucket.autoclass_toggle_time != previous_toggle_time


def test_bucket_delete_force(storage_client):
    bucket_name = _helpers.unique_name("version-disabled")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket = storage_client.create_bucket(bucket_obj)

    BLOB_NAME = "my_object"
    blob = bucket.blob(BLOB_NAME)
    blob.upload_from_string("abcd")
    blob.upload_from_string("efgh")

    blobs = bucket.list_blobs(versions=True)
    counter = 0
    for blob in blobs:
        counter += 1
        assert blob.name == BLOB_NAME
    assert counter == 1

    bucket.delete(force=True)  # Will fail with 409 if blobs aren't deleted


def test_bucket_delete_force_works_with_versions(storage_client):
    bucket_name = _helpers.unique_name("version-enabled")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket_obj.versioning_enabled = True
    bucket = storage_client.create_bucket(bucket_obj)
    assert bucket.versioning_enabled

    BLOB_NAME = "my_versioned_object"
    blob = bucket.blob(BLOB_NAME)
    blob.upload_from_string("abcd")
    blob.upload_from_string("efgh")

    blobs = bucket.list_blobs(versions=True)
    counter = 0
    for blob in blobs:
        counter += 1
        assert blob.name == BLOB_NAME
    assert counter == 2

    bucket.delete(force=True)  # Will fail with 409 if versions aren't deleted


def test_config_autoclass_w_existing_bucket(
    storage_client,
    buckets_to_delete,
):
    from google.cloud.storage import constants

    bucket_name = _helpers.unique_name("for-autoclass")
    bucket = storage_client.create_bucket(bucket_name)
    buckets_to_delete.append(bucket)
    assert bucket.autoclass_enabled is False
    assert bucket.autoclass_toggle_time is None
    assert bucket.autoclass_terminal_storage_class is None
    assert bucket.autoclass_terminal_storage_class_update_time is None

    # Enable Autoclass on existing buckets with terminal_storage_class set to ARCHIVE
    bucket.autoclass_enabled = True
    bucket.autoclass_terminal_storage_class = constants.ARCHIVE_STORAGE_CLASS
    bucket.patch(if_metageneration_match=bucket.metageneration)
    previous_tsc_update_time = bucket.autoclass_terminal_storage_class_update_time
    assert bucket.autoclass_enabled is True
    assert bucket.autoclass_terminal_storage_class == constants.ARCHIVE_STORAGE_CLASS

    # Configure Autoclass terminal_storage_class to NEARLINE
    bucket.autoclass_terminal_storage_class = constants.NEARLINE_STORAGE_CLASS
    bucket.patch(if_metageneration_match=bucket.metageneration)
    assert bucket.autoclass_enabled is True
    assert bucket.autoclass_terminal_storage_class == constants.NEARLINE_STORAGE_CLASS
    assert (
        bucket.autoclass_terminal_storage_class_update_time != previous_tsc_update_time
    )


def test_soft_delete_policy(
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

    # Insert an object and get object metadata prior soft-deleted.
    payload = b"DEADBEEF"
    blob_name = _helpers.unique_name("soft-delete")
    blob = bucket.blob(blob_name)
    blob.upload_from_string(payload)

    blob = bucket.get_blob(blob_name)
    gen = blob.generation
    assert blob.soft_delete_time is None
    assert blob.hard_delete_time is None

    # Delete the object to enter soft-deleted state.
    blob.delete()

    iter_default = bucket.list_blobs()
    assert len(list(iter_default)) == 0
    iter_w_soft_delete = bucket.list_blobs(soft_deleted=True)
    assert len(list(iter_w_soft_delete)) > 0

    # Get the soft-deleted object.
    soft_deleted_blob = bucket.get_blob(blob_name, generation=gen, soft_deleted=True)
    assert soft_deleted_blob.soft_delete_time is not None
    assert soft_deleted_blob.hard_delete_time is not None

    # Restore the soft-deleted object.
    restored_blob = bucket.restore_blob(blob_name, generation=gen)
    assert restored_blob.exists() is True
    assert restored_blob.generation != gen

    # Patch the soft delete policy on an existing bucket.
    new_duration_secs = 10 * 86400
    bucket.soft_delete_policy.retention_duration_seconds = new_duration_secs
    bucket.patch()
    assert bucket.soft_delete_policy.retention_duration_seconds == new_duration_secs


def test_new_bucket_with_hierarchical_namespace(
    storage_client,
    buckets_to_delete,
):
    # Test new bucket without specifying hierarchical namespace
    bucket_name = _helpers.unique_name("new-wo-hns")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket = storage_client.create_bucket(bucket_obj)
    buckets_to_delete.append(bucket)
    assert bucket.hierarchical_namespace_enabled is None

    # Test new bucket with hierarchical namespace disabled
    bucket_name = _helpers.unique_name("new-hns-disabled")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket_obj.hierarchical_namespace_enabled = False
    bucket = storage_client.create_bucket(bucket_obj)
    buckets_to_delete.append(bucket)
    assert bucket.hierarchical_namespace_enabled is False

    # Test new bucket with hierarchical namespace enabled
    bucket_name = _helpers.unique_name("new-hns-enabled")
    bucket_obj = storage_client.bucket(bucket_name)
    bucket_obj.hierarchical_namespace_enabled = True
    bucket_obj.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket = storage_client.create_bucket(bucket_obj)
    buckets_to_delete.append(bucket)
    assert bucket.hierarchical_namespace_enabled is True


def test_bucket_ip_filter_patch(storage_client, buckets_to_delete):
    """Test setting and clearing IP filter configuration without enabling enforcement."""
    bucket_name = _helpers.unique_name("ip-filter-control")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    ip_filter = IPFilter()
    ip_filter.mode = "Disabled"
    ip_filter.allow_all_service_agent_access = True
    ip_filter.public_network_source = PublicNetworkSource(
        allowed_ip_cidr_ranges=["203.0.113.10/32"]
    )
    ip_filter.vpc_network_sources.append(
        VpcNetworkSource(
            network=f"projects/{storage_client.project}/global/networks/default",
            allowed_ip_cidr_ranges=["10.0.0.0/8"],
        )
    )
    bucket.ip_filter = ip_filter
    bucket.patch()

    # Reload and verify the full configuration was set correctly.
    bucket.reload()
    reloaded_filter = bucket.ip_filter
    assert reloaded_filter is not None
    assert reloaded_filter.mode == "Disabled"
    assert reloaded_filter.allow_all_service_agent_access is True
    assert reloaded_filter.public_network_source.allowed_ip_cidr_ranges == [
        "203.0.113.10/32"
    ]
    assert len(reloaded_filter.vpc_network_sources) == 1


@pytest.mark.skip(reason="[https://github.com/googleapis/python-storage/issues/1611]")
def test_list_buckets_with_ip_filter(storage_client, buckets_to_delete):
    """Test that listing buckets returns a summarized IP filter."""
    bucket_name = _helpers.unique_name("ip-filter-list")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    ip_filter = IPFilter()
    ip_filter.mode = "Disabled"
    ip_filter.allow_all_service_agent_access = True
    ip_filter.public_network_source = PublicNetworkSource(
        allowed_ip_cidr_ranges=["203.0.113.10/32"]
    )
    bucket.ip_filter = ip_filter
    bucket.patch()

    buckets_list = list(storage_client.list_buckets(prefix=bucket_name))
    found_bucket = next((b for b in buckets_list if b.name == bucket_name), None)

    assert found_bucket is not None
    summarized_filter = found_bucket.ip_filter

    assert summarized_filter is not None
    assert summarized_filter.mode == "Disabled"
    assert summarized_filter.allow_all_service_agent_access is True

    # Check that the summarized filter does not include full details.
    assert summarized_filter.public_network_source is None
    assert summarized_filter.vpc_network_sources == []


def test_create_bucket_with_encryption_enforcement(storage_client, buckets_to_delete):
    bucket_name = _helpers.unique_name("enforce-on-create")

    # Initialize the bucket object locally
    bucket = storage_client.bucket(bucket_name)

    # Define and set the enforcement config
    enforcement = EncryptionEnforcementConfig(
        restriction_mode=ENFORCEMENT_MODE_FULLY_RESTRICTED
    )
    # Set the config on the local object
    bucket.encryption.google_managed_encryption_enforcement_config = enforcement

    # storage_client.create_bucket(bucket) sends the config in the initial POST
    created_bucket = storage_client.create_bucket(bucket)
    buckets_to_delete.append(created_bucket)

    # Verify backend persistence and server-generated effective_time
    config = created_bucket.encryption.google_managed_encryption_enforcement_config
    assert config.restriction_mode == ENFORCEMENT_MODE_FULLY_RESTRICTED
    assert isinstance(config.effective_time, datetime.datetime)


def test_bucket_encryption_enforcement_config(storage_client, buckets_to_delete):
    bucket_name = _helpers.unique_name("encryption-enforcement")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    # 1. Set initial enforcement configuration
    # Testing both Google-managed and Customer-managed configurations
    google_config = EncryptionEnforcementConfig(
        restriction_mode=ENFORCEMENT_MODE_FULLY_RESTRICTED
    )
    customer_config = EncryptionEnforcementConfig(
        restriction_mode=ENFORCEMENT_MODE_NOT_RESTRICTED
    )

    bucket.encryption.google_managed_encryption_enforcement_config = google_config
    bucket.encryption.customer_managed_encryption_enforcement_config = customer_config

    # Patch sends the 'encryption' dict to the server
    bucket.patch()

    # 2. Reload and Verify backend persistence
    bucket.reload()

    # Verify Google Managed Config and the presence of effective_time
    reloaded_google = bucket.encryption.google_managed_encryption_enforcement_config
    assert reloaded_google.restriction_mode == ENFORCEMENT_MODE_FULLY_RESTRICTED
    assert isinstance(reloaded_google.effective_time, datetime.datetime)

    # Verify Customer Managed Config
    reloaded_customer = bucket.encryption.customer_managed_encryption_enforcement_config
    assert reloaded_customer.restriction_mode == ENFORCEMENT_MODE_NOT_RESTRICTED
    assert reloaded_customer.effective_time is None

    # 3. Test updating an existing config
    update_google_config = EncryptionEnforcementConfig(
        restriction_mode=ENFORCEMENT_MODE_NOT_RESTRICTED
    )
    bucket.encryption.google_managed_encryption_enforcement_config = (
        update_google_config
    )
    bucket.patch()
    assert (
        bucket.encryption.google_managed_encryption_enforcement_config.restriction_mode
        == ENFORCEMENT_MODE_NOT_RESTRICTED
    )


def test_delete_bucket_encryption_enforcement_config(storage_client, buckets_to_delete):
    bucket_name = _helpers.unique_name("delete-encryption-config")

    # Create a bucket with an initial restricted config
    enforcement = EncryptionEnforcementConfig(
        restriction_mode=ENFORCEMENT_MODE_FULLY_RESTRICTED
    )
    bucket = storage_client.bucket(bucket_name)
    bucket.encryption.google_managed_encryption_enforcement_config = enforcement
    bucket = storage_client.create_bucket(bucket)
    buckets_to_delete.append(bucket)

    # Verify it exists first
    assert bucket.encryption.google_managed_encryption_enforcement_config is not None

    # DELETE: Set the specific enforcement config to None
    bucket.encryption.google_managed_encryption_enforcement_config = None

    # patch() sends the null value to the server to clear the field
    bucket.patch()

    # Reload and verify the field is gone
    bucket.reload()
    assert bucket.encryption.google_managed_encryption_enforcement_config is None
