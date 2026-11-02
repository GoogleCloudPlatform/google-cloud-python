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

from . import _helpers

custom_attributes = {"attr1": "value1", "attr2": "value2"}
blob_name_prefix = "blob-name-prefix/"


@pytest.fixture(scope="session")
def event_types():
    from google.cloud.storage.notification import (
        OBJECT_DELETE_EVENT_TYPE,
        OBJECT_FINALIZE_EVENT_TYPE,
    )

    return [OBJECT_FINALIZE_EVENT_TYPE, OBJECT_DELETE_EVENT_TYPE]


@pytest.fixture(scope="session")
def payload_format():
    from google.cloud.storage.notification import JSON_API_V1_PAYLOAD_FORMAT

    return JSON_API_V1_PAYLOAD_FORMAT


@pytest.fixture(scope="session")
def publisher_client():
    try:
        from google.cloud.pubsub_v1 import PublisherClient
    except ImportError:
        pytest.skip("Cannot import pubsub")

    return PublisherClient()


@pytest.fixture(scope="session")
def topic_name():
    return _helpers.unique_name("notification")


@pytest.fixture(scope="session")
def topic_path(storage_client, topic_name):
    return f"projects/{storage_client.project}/topics/{topic_name}"


@pytest.fixture(scope="session")
def notification_topic(storage_client, publisher_client, topic_path, no_mtls):
    _helpers.retry_429(publisher_client.create_topic)(request={"name": topic_path})
    try:
        policy = publisher_client.get_iam_policy(request={"resource": topic_path})
        binding = policy.bindings.add()
        binding.role = "roles/pubsub.publisher"
        binding.members.append(
            f"serviceAccount:{storage_client.get_service_account_email()}"
        )
        publisher_client.set_iam_policy(
            request={"resource": topic_path, "policy": policy}
        )
        yield topic_path
    finally:
        publisher_client.delete_topic(request={"topic": topic_path})


def test_notification_create_minimal(
    storage_client,
    buckets_to_delete,
    topic_name,
    notification_topic,
):
    bucket_name = _helpers.unique_name("notification-minimal")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    assert list(bucket.list_notifications()) == []

    notification = bucket.notification(topic_name)
    _helpers.retry_429_503(notification.create)()

    try:
        assert notification.exists()
        assert notification.notification_id is not None
        notifications = list(bucket.list_notifications())
        assert len(notifications) == 1
        assert notifications[0].topic_name == topic_name
    finally:
        notification.delete()


def test_notification_create_explicit(
    storage_client,
    buckets_to_delete,
    topic_name,
    notification_topic,
    event_types,
    payload_format,
):
    bucket_name = _helpers.unique_name("notification-explicit")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    assert list(bucket.list_notifications()) == []

    notification = bucket.notification(
        topic_name=topic_name,
        custom_attributes=custom_attributes,
        event_types=event_types,
        blob_name_prefix=blob_name_prefix,
        payload_format=payload_format,
    )
    _helpers.retry_429_503(notification.create)()

    try:
        assert notification.exists()
        assert notification.notification_id is not None
        assert notification.custom_attributes == custom_attributes
        assert notification.event_types == event_types
        assert notification.blob_name_prefix == blob_name_prefix
        assert notification.payload_format == payload_format
    finally:
        notification.delete()


def test_notification_create_w_user_project(
    storage_client,
    buckets_to_delete,
    topic_name,
    notification_topic,
    user_project,
):
    bucket_name = _helpers.unique_name("notification-w-up")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    with_user_project = storage_client.bucket(bucket_name, user_project=user_project)

    assert list(with_user_project.list_notifications()) == []

    notification = with_user_project.notification(topic_name)
    _helpers.retry_429_503(notification.create)()

    try:
        assert notification.exists()
        assert notification.notification_id is not None
        notifications = list(bucket.list_notifications())
        assert len(notifications) == 1
        assert notifications[0].topic_name == topic_name
    finally:
        notification.delete()


def test_notification_create_wo_topic_name(
    storage_client,
    buckets_to_delete,
    topic_name,
    notification_topic,
    event_types,
    payload_format,
):
    from google.cloud.exceptions import BadRequest

    bucket_name = _helpers.unique_name("notification-wo-name")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    assert list(bucket.list_notifications()) == []

    notification = bucket.notification(
        topic_name=None,
        custom_attributes=custom_attributes,
        event_types=event_types,
        blob_name_prefix=blob_name_prefix,
        payload_format=payload_format,
    )

    with pytest.raises(BadRequest):
        notification.create()


def test_bucket_get_notification(
    storage_client,
    buckets_to_delete,
    topic_name,
    notification_topic,
    event_types,
    payload_format,
):
    bucket_name = _helpers.unique_name("notification-get")
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(bucket_name)
    buckets_to_delete.append(bucket)

    notification = bucket.notification(
        topic_name=topic_name,
        custom_attributes=custom_attributes,
        payload_format=payload_format,
    )
    _helpers.retry_429_503(notification.create)()
    try:
        assert notification.exists()
        assert notification.notification_id is not None

        fetched = bucket.get_notification(notification.notification_id)

        assert fetched.notification_id == notification.notification_id
        assert fetched.custom_attributes == custom_attributes
        assert fetched.payload_format == payload_format
    finally:
        notification.delete()
