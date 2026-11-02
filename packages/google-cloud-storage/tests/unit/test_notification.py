# Copyright 2017 Google LLC
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

import unittest

import mock

from google.cloud.storage.retry import DEFAULT_RETRY


class TestBucketNotification(unittest.TestCase):
    BUCKET_NAME = "test-bucket"
    BUCKET_PROJECT = "bucket-project-123"
    TOPIC_NAME = "test-topic"
    TOPIC_ALT_PROJECT = "topic-project-456"
    TOPIC_REF_FMT = "//pubsub.googleapis.com/projects/{}/topics/{}"
    TOPIC_REF = TOPIC_REF_FMT.format(BUCKET_PROJECT, TOPIC_NAME)
    TOPIC_ALT_REF = TOPIC_REF_FMT.format(TOPIC_ALT_PROJECT, TOPIC_NAME)
    CUSTOM_ATTRIBUTES = {"attr1": "value1", "attr2": "value2"}
    BLOB_NAME_PREFIX = "blob-name-prefix/"
    NOTIFICATION_ID = "123"
    SELF_LINK = "https://example.com/notification/123"
    ETAG = "DEADBEEF"
    CREATE_PATH = f"/b/{BUCKET_NAME}/notificationConfigs"
    NOTIFICATION_PATH = f"/b/{BUCKET_NAME}/notificationConfigs/{NOTIFICATION_ID}"

    @staticmethod
    def event_types():
        from google.cloud.storage.notification import (
            OBJECT_DELETE_EVENT_TYPE,
            OBJECT_FINALIZE_EVENT_TYPE,
        )

        return [OBJECT_FINALIZE_EVENT_TYPE, OBJECT_DELETE_EVENT_TYPE]

    @staticmethod
    def payload_format():
        from google.cloud.storage.notification import JSON_API_V1_PAYLOAD_FORMAT

        return JSON_API_V1_PAYLOAD_FORMAT

    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    @staticmethod
    def _get_target_class():
        from google.cloud.storage.notification import BucketNotification

        return BucketNotification

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _make_client(self, project=BUCKET_PROJECT):
        from google.cloud.storage.client import Client

        return mock.Mock(project=project, spec=Client)

    def _make_bucket(self, client, name=BUCKET_NAME, user_project=None):
        bucket = mock.Mock(spec=["client", "name", "user_project"])
        bucket.client = client
        bucket.name = name
        bucket.user_project = user_project
        return bucket

    def test_ctor_w_missing_project(self):
        client = self._make_client(project=None)
        bucket = self._make_bucket(client)

        with self.assertRaises(ValueError):
            self._make_one(bucket, self.TOPIC_NAME)

    def test_ctor_defaults(self):
        from google.cloud.storage.notification import NONE_PAYLOAD_FORMAT

        client = self._make_client()
        bucket = self._make_bucket(client)

        notification = self._make_one(bucket, self.TOPIC_NAME)

        self.assertIs(notification.bucket, bucket)
        self.assertEqual(notification.topic_name, self.TOPIC_NAME)
        self.assertEqual(notification.topic_project, self.BUCKET_PROJECT)
        self.assertIsNone(notification.custom_attributes)
        self.assertIsNone(notification.event_types)
        self.assertIsNone(notification.blob_name_prefix)
        self.assertEqual(notification.payload_format, NONE_PAYLOAD_FORMAT)

    def test_ctor_explicit(self):
        client = self._make_client()
        bucket = self._make_bucket(client)

        notification = self._make_one(
            bucket,
            self.TOPIC_NAME,
            topic_project=self.TOPIC_ALT_PROJECT,
            custom_attributes=self.CUSTOM_ATTRIBUTES,
            event_types=self.event_types(),
            blob_name_prefix=self.BLOB_NAME_PREFIX,
            payload_format=self.payload_format(),
        )

        self.assertIs(notification.bucket, bucket)
        self.assertEqual(notification.topic_name, self.TOPIC_NAME)
        self.assertEqual(notification.topic_project, self.TOPIC_ALT_PROJECT)
        self.assertEqual(notification.custom_attributes, self.CUSTOM_ATTRIBUTES)
        self.assertEqual(notification.event_types, self.event_types())
        self.assertEqual(notification.blob_name_prefix, self.BLOB_NAME_PREFIX)
        self.assertEqual(notification.payload_format, self.payload_format())

    def test_from_api_repr_no_topic(self):
        klass = self._get_target_class()
        client = self._make_client()
        bucket = self._make_bucket(client)
        resource = {}

        with self.assertRaises(ValueError):
            klass.from_api_repr(resource, bucket=bucket)

    def test_from_api_repr_invalid_topic(self):
        klass = self._get_target_class()
        client = self._make_client()
        bucket = self._make_bucket(client)
        resource = {"topic": "@#$%"}

        with self.assertRaises(ValueError):
            klass.from_api_repr(resource, bucket=bucket)

    def test_from_api_repr_minimal(self):
        from google.cloud.storage.notification import NONE_PAYLOAD_FORMAT

        klass = self._get_target_class()
        client = self._make_client()
        bucket = self._make_bucket(client)
        resource = {
            "topic": self.TOPIC_REF,
            "id": self.NOTIFICATION_ID,
            "etag": self.ETAG,
            "selfLink": self.SELF_LINK,
            "payload_format": NONE_PAYLOAD_FORMAT,
        }

        notification = klass.from_api_repr(resource, bucket=bucket)

        self.assertIs(notification.bucket, bucket)
        self.assertEqual(notification.topic_name, self.TOPIC_NAME)
        self.assertEqual(notification.topic_project, self.BUCKET_PROJECT)
        self.assertIsNone(notification.custom_attributes)
        self.assertIsNone(notification.event_types)
        self.assertIsNone(notification.blob_name_prefix)
        self.assertEqual(notification.payload_format, NONE_PAYLOAD_FORMAT)
        self.assertEqual(notification.etag, self.ETAG)
        self.assertEqual(notification.self_link, self.SELF_LINK)

    def test_from_api_repr_explicit(self):
        klass = self._get_target_class()
        client = self._make_client()
        bucket = self._make_bucket(client)
        resource = {
            "topic": self.TOPIC_ALT_REF,
            "custom_attributes": self.CUSTOM_ATTRIBUTES,
            "event_types": self.event_types(),
            "object_name_prefix": self.BLOB_NAME_PREFIX,
            "payload_format": self.payload_format(),
            "id": self.NOTIFICATION_ID,
            "etag": self.ETAG,
            "selfLink": self.SELF_LINK,
        }

        notification = klass.from_api_repr(resource, bucket=bucket)

        self.assertIs(notification.bucket, bucket)
        self.assertEqual(notification.topic_name, self.TOPIC_NAME)
        self.assertEqual(notification.topic_project, self.TOPIC_ALT_PROJECT)
        self.assertEqual(notification.custom_attributes, self.CUSTOM_ATTRIBUTES)
        self.assertEqual(notification.event_types, self.event_types())
        self.assertEqual(notification.blob_name_prefix, self.BLOB_NAME_PREFIX)
        self.assertEqual(notification.payload_format, self.payload_format())
        self.assertEqual(notification.notification_id, self.NOTIFICATION_ID)
        self.assertEqual(notification.etag, self.ETAG)
        self.assertEqual(notification.self_link, self.SELF_LINK)

    def test_notification_id(self):
        client = self._make_client()
        bucket = self._make_bucket(client)

        notification = self._make_one(bucket, self.TOPIC_NAME)

        self.assertIsNone(notification.notification_id)

        notification._properties["id"] = self.NOTIFICATION_ID
        self.assertEqual(notification.notification_id, self.NOTIFICATION_ID)

    def test_etag(self):
        client = self._make_client()
        bucket = self._make_bucket(client)

        notification = self._make_one(bucket, self.TOPIC_NAME)

        self.assertIsNone(notification.etag)

        notification._properties["etag"] = self.ETAG
        self.assertEqual(notification.etag, self.ETAG)

    def test_self_link(self):
        client = self._make_client()
        bucket = self._make_bucket(client)

        notification = self._make_one(bucket, self.TOPIC_NAME)

        self.assertIsNone(notification.self_link)

        notification._properties["selfLink"] = self.SELF_LINK
        self.assertEqual(notification.self_link, self.SELF_LINK)

    def test_create_w_existing_notification_id(self):
        client = mock.Mock(spec=["_post_resource", "project"])
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID

        with self.assertRaises(ValueError):
            notification.create()

        client._post_resource.assert_not_called()

    def test_create_wo_topic_name(self):
        from google.cloud.exceptions import BadRequest

        from google.cloud.storage.notification import NONE_PAYLOAD_FORMAT

        client = mock.Mock(spec=["_post_resource", "project"])
        client.project = self.BUCKET_PROJECT
        client._post_resource.side_effect = BadRequest(
            "Invalid Google Cloud Pub/Sub topic."
        )
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, None)

        with self.assertRaises(BadRequest):
            notification.create()

        expected_topic = self.TOPIC_REF_FMT.format(self.BUCKET_PROJECT, "")
        expected_data = {
            "topic": expected_topic,
            "payload_format": NONE_PAYLOAD_FORMAT,
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            self.CREATE_PATH,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=None,
        )

    def test_create_w_defaults(self):
        from google.cloud.storage.notification import NONE_PAYLOAD_FORMAT

        api_response = {
            "topic": self.TOPIC_REF,
            "id": self.NOTIFICATION_ID,
            "etag": self.ETAG,
            "selfLink": self.SELF_LINK,
            "payload_format": NONE_PAYLOAD_FORMAT,
        }
        client = mock.Mock(spec=["_post_resource", "project"])
        client.project = self.BUCKET_PROJECT
        client._post_resource.return_value = api_response
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)

        notification.create()

        self.assertEqual(notification.notification_id, self.NOTIFICATION_ID)
        self.assertEqual(notification.etag, self.ETAG)
        self.assertEqual(notification.self_link, self.SELF_LINK)
        self.assertIsNone(notification.custom_attributes)
        self.assertIsNone(notification.event_types)
        self.assertIsNone(notification.blob_name_prefix)
        self.assertEqual(notification.payload_format, NONE_PAYLOAD_FORMAT)

        expected_data = {
            "topic": self.TOPIC_REF,
            "payload_format": NONE_PAYLOAD_FORMAT,
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            self.CREATE_PATH,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=None,
        )

    def test_create_w_explicit_client_w_timeout_w_retry(self):
        user_project = "user-project-123"
        api_response = {
            "topic": self.TOPIC_ALT_REF,
            "custom_attributes": self.CUSTOM_ATTRIBUTES,
            "event_types": self.event_types(),
            "object_name_prefix": self.BLOB_NAME_PREFIX,
            "payload_format": self.payload_format(),
            "id": self.NOTIFICATION_ID,
            "etag": self.ETAG,
            "selfLink": self.SELF_LINK,
        }
        bucket = self._make_bucket(client=None, user_project=user_project)
        notification = self._make_one(
            bucket,
            self.TOPIC_NAME,
            topic_project=self.TOPIC_ALT_PROJECT,
            custom_attributes=self.CUSTOM_ATTRIBUTES,
            event_types=self.event_types(),
            blob_name_prefix=self.BLOB_NAME_PREFIX,
            payload_format=self.payload_format(),
        )
        client = mock.Mock(spec=["_post_resource", "project"])
        client.project = self.BUCKET_PROJECT
        client._post_resource.return_value = api_response
        timeout = 42
        retry = mock.Mock(spec=[])

        notification.create(client=client, timeout=timeout, retry=retry)

        self.assertEqual(notification.custom_attributes, self.CUSTOM_ATTRIBUTES)
        self.assertEqual(notification.event_types, self.event_types())
        self.assertEqual(notification.blob_name_prefix, self.BLOB_NAME_PREFIX)
        self.assertEqual(notification.payload_format, self.payload_format())
        self.assertEqual(notification.notification_id, self.NOTIFICATION_ID)
        self.assertEqual(notification.etag, self.ETAG)
        self.assertEqual(notification.self_link, self.SELF_LINK)

        expected_data = {
            "topic": self.TOPIC_ALT_REF,
            "custom_attributes": self.CUSTOM_ATTRIBUTES,
            "event_types": self.event_types(),
            "object_name_prefix": self.BLOB_NAME_PREFIX,
            "payload_format": self.payload_format(),
        }
        expected_query_params = {"userProject": user_project}
        client._post_resource.assert_called_once_with(
            self.CREATE_PATH,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
        )

    def test_exists_wo_notification_id(self):
        client = mock.Mock(spec=["_get_resource", "project"])
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)

        with self.assertRaises(ValueError):
            notification.exists()

        client._get_resource.assert_not_called()

    def test_exists_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        client = mock.Mock(spec=["_get_resource", "project"])
        client._get_resource.side_effect = NotFound("testing")
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID

        self.assertFalse(notification.exists())

        expected_query_params = {}
        client._get_resource.assert_called_once_with(
            self.NOTIFICATION_PATH,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_exists_hit_w_explicit_w_user_project(self):
        user_project = "user-project-123"
        api_response = {
            "topic": self.TOPIC_REF,
            "id": self.NOTIFICATION_ID,
            "etag": self.ETAG,
            "selfLink": self.SELF_LINK,
        }
        client = mock.Mock(spec=["_get_resource", "project"])
        client._get_resource.return_vale = api_response
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client, user_project=user_project)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID
        timeout = 42
        retry = mock.Mock(spec=[])

        self.assertTrue(
            notification.exists(client=client, timeout=timeout, retry=retry)
        )

        expected_query_params = {"userProject": user_project}
        client._get_resource.assert_called_once_with(
            self.NOTIFICATION_PATH,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
        )

    def test_reload_wo_notification_id(self):
        client = mock.Mock(spec=["_get_resource", "project"])
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)

        with self.assertRaises(ValueError):
            notification.reload()

        client._get_resource.assert_not_called()

    def test_reload_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        client = mock.Mock(spec=["_get_resource", "project"])
        client._get_resource.side_effect = NotFound("testing")
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID

        with self.assertRaises(NotFound):
            notification.reload()

        expected_query_params = {}
        client._get_resource.assert_called_once_with(
            self.NOTIFICATION_PATH,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_reload_hit_w_explicit_w_user_project(self):
        from google.cloud.storage.notification import NONE_PAYLOAD_FORMAT

        user_project = "user-project-123"
        api_response = {
            "topic": self.TOPIC_REF,
            "id": self.NOTIFICATION_ID,
            "etag": self.ETAG,
            "selfLink": self.SELF_LINK,
            "payload_format": NONE_PAYLOAD_FORMAT,
        }
        client = mock.Mock(spec=["_get_resource", "project"])
        client._get_resource.return_value = api_response
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client, user_project=user_project)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID
        timeout = 42
        retry = mock.Mock(spec=[])

        notification.reload(client=client, timeout=timeout, retry=retry)

        self.assertEqual(notification.etag, self.ETAG)
        self.assertEqual(notification.self_link, self.SELF_LINK)
        self.assertIsNone(notification.custom_attributes)
        self.assertIsNone(notification.event_types)
        self.assertIsNone(notification.blob_name_prefix)
        self.assertEqual(notification.payload_format, NONE_PAYLOAD_FORMAT)

        expected_query_params = {"userProject": user_project}
        client._get_resource.assert_called_once_with(
            self.NOTIFICATION_PATH,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
        )

    def test_delete_wo_notification_id(self):
        client = mock.Mock(spec=["_delete_resource", "project"])
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)

        with self.assertRaises(ValueError):
            notification.delete()

        client._delete_resource.assert_not_called()

    def test_delete_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        client = mock.Mock(spec=["_delete_resource", "project"])
        client._delete_resource.side_effect = NotFound("testing")
        client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(client)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID

        with self.assertRaises(NotFound):
            notification.delete()

        client._delete_resource.assert_called_once_with(
            self.NOTIFICATION_PATH,
            query_params={},
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_delete_hit_w_explicit_client_timeout_retry(self):
        user_project = "user-project-123"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket_client = mock.Mock(spec=["project"])
        bucket_client.project = self.BUCKET_PROJECT
        bucket = self._make_bucket(bucket_client, user_project=user_project)
        notification = self._make_one(bucket, self.TOPIC_NAME)
        notification._properties["id"] = self.NOTIFICATION_ID
        timeout = 42
        retry = mock.Mock(spec=[])

        notification.delete(client=client, timeout=timeout, retry=retry)

        client._delete_resource.assert_called_once_with(
            self.NOTIFICATION_PATH,
            query_params={"userProject": user_project},
            timeout=timeout,
            retry=retry,
        )


class Test__parse_topic_path(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage import notification

        return notification._parse_topic_path(*args, **kwargs)

    @staticmethod
    def _make_topic_path(project, topic_name):
        from google.cloud.storage import notification

        return notification._TOPIC_REF_FMT.format(project, topic_name)

    def test_project_name_too_long(self):
        project = "a" * 31
        topic_path = self._make_topic_path(project, "topic-name")
        with self.assertRaises(ValueError):
            self._call_fut(topic_path)

    def test_project_name_uppercase(self):
        project = "aaaAaa"
        topic_path = self._make_topic_path(project, "topic-name")
        with self.assertRaises(ValueError):
            self._call_fut(topic_path)

    def test_leading_digit(self):
        project = "1aaaaa"
        topic_path = self._make_topic_path(project, "topic-name")
        with self.assertRaises(ValueError):
            self._call_fut(topic_path)

    def test_leading_hyphen(self):
        project = "-aaaaa"
        topic_path = self._make_topic_path(project, "topic-name")
        with self.assertRaises(ValueError):
            self._call_fut(topic_path)

    def test_trailing_hyphen(self):
        project = "aaaaa-"
        topic_path = self._make_topic_path(project, "topic-name")
        with self.assertRaises(ValueError):
            self._call_fut(topic_path)

    def test_invalid_format(self):
        topic_path = "@#$%"
        with self.assertRaises(ValueError):
            self._call_fut(topic_path)

    def test_success(self):
        topic_name = "tah-pic-nehm"
        project_choices = (
            "a" * 30,  # Max length.
            "a-b--c---d",  # Valid hyphen usage.
            "abcdefghijklmnopqrstuvwxyz",  # Valid letters.
            "z0123456789",  # Valid digits (non-leading).
            "a-bcdefghijklmn12opqrstuv0wxyz",
        )
        for project in project_choices:
            topic_path = self._make_topic_path(project, topic_name)
            result = self._call_fut(topic_path)
            self.assertEqual(result, (topic_name, project))
