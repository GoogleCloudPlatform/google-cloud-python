# Copyright 2014 Google LLC
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

import datetime
import unittest

import mock
import pytest

from google.cloud.storage._helpers import _NOW, _UTC, _get_default_storage_base_url
from google.cloud.storage.blob import _quote
from google.cloud.storage.constants import (
    PUBLIC_ACCESS_PREVENTION_ENFORCED,
    PUBLIC_ACCESS_PREVENTION_INHERITED,
    PUBLIC_ACCESS_PREVENTION_UNSPECIFIED,
    RPO_ASYNC_TURBO,
    RPO_DEFAULT,
)
from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_ETAG_IN_JSON,
    DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
    DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
)


def _create_signing_credentials():
    import google.auth.credentials

    class _SigningCredentials(
        google.auth.credentials.Credentials, google.auth.credentials.Signing
    ):
        pass

    credentials = mock.Mock(spec=_SigningCredentials)

    return credentials


class Test__blobs_page_start(unittest.TestCase):
    @staticmethod
    def _call_fut(iterator, page, response):
        from google.cloud.storage.bucket import _blobs_page_start

        return _blobs_page_start(iterator, page, response)

    def test_wo_any_prefixes(self):
        iterator = mock.Mock(spec=["prefixes"], prefixes=set())
        page = mock.Mock(spec=["prefixes"])
        response = {}

        self._call_fut(iterator, page, response)

        self.assertEqual(page.prefixes, ())
        self.assertEqual(iterator.prefixes, set())

    def test_w_prefixes(self):
        iterator_prefixes = set(["foo/", "qux/"])
        iterator = mock.Mock(spec=["prefixes"], prefixes=iterator_prefixes)
        page = mock.Mock(spec=["prefixes"])
        page_prefixes = ["foo/", "bar/", "baz/"]
        response = {"prefixes": page_prefixes}

        self._call_fut(iterator, page, response)

        self.assertEqual(page.prefixes, tuple(page_prefixes))
        self.assertEqual(iterator.prefixes, iterator_prefixes.union(page_prefixes))


class Test__item_to_blob(unittest.TestCase):
    @staticmethod
    def _call_fut(iterator, item):
        from google.cloud.storage.bucket import _item_to_blob

        return _item_to_blob(iterator, item)

    def test_wo_extra_properties(self):
        from google.cloud.storage.blob import Blob

        blob_name = "blob-name"
        bucket = mock.Mock(spec=[])
        iterator = mock.Mock(spec=["bucket"], bucket=bucket)
        item = {"name": blob_name}

        blob = self._call_fut(iterator, item)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob._properties, item)

    def test_w_extra_properties(self):
        from google.cloud.storage.blob import Blob

        blob_name = "blob-name"
        bucket = mock.Mock(spec=[])
        iterator = mock.Mock(spec=["bucket"], bucket=bucket)
        item = {
            "name": blob_name,
            "generation": 123,
            "contentType": "text/plain",
            "contentLanguage": "en-US",
        }

        blob = self._call_fut(iterator, item)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob._properties, item)


class Test_LifecycleRuleConditions(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import LifecycleRuleConditions

        return LifecycleRuleConditions

    def _make_one(self, **kw):
        return self._get_target_class()(**kw)

    def test_ctor_wo_conditions(self):
        with self.assertRaises(ValueError):
            self._make_one()

    def test_ctor_w_age_and_matches_storage_class(self):
        conditions = self._make_one(age=10, matches_storage_class=["COLDLINE"])
        expected = {"age": 10, "matchesStorageClass": ["COLDLINE"]}
        self.assertEqual(dict(conditions), expected)
        self.assertEqual(conditions.age, 10)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertEqual(conditions.matches_storage_class, ["COLDLINE"])
        self.assertIsNone(conditions.number_of_newer_versions)

    def test_ctor_w_created_before_and_is_live(self):
        import datetime

        before = datetime.date(2018, 8, 1)
        conditions = self._make_one(created_before=before, is_live=False)
        expected = {"createdBefore": "2018-08-01", "isLive": False}
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertEqual(conditions.created_before, before)
        self.assertEqual(conditions.is_live, False)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertIsNone(conditions.number_of_newer_versions)
        self.assertIsNone(conditions.days_since_custom_time)
        self.assertIsNone(conditions.custom_time_before)
        self.assertIsNone(conditions.noncurrent_time_before)

    def test_ctor_w_number_of_newer_versions(self):
        conditions = self._make_one(number_of_newer_versions=3)
        expected = {"numNewerVersions": 3}
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertEqual(conditions.number_of_newer_versions, 3)

    def test_ctor_w_days_since_custom_time(self):
        conditions = self._make_one(
            number_of_newer_versions=3, days_since_custom_time=2
        )
        expected = {"numNewerVersions": 3, "daysSinceCustomTime": 2}
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertEqual(conditions.number_of_newer_versions, 3)
        self.assertEqual(conditions.days_since_custom_time, 2)

    def test_ctor_w_days_since_noncurrent_time(self):
        conditions = self._make_one(
            number_of_newer_versions=3, days_since_noncurrent_time=2
        )
        expected = {"numNewerVersions": 3, "daysSinceNoncurrentTime": 2}
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertEqual(conditions.number_of_newer_versions, 3)
        self.assertEqual(conditions.days_since_noncurrent_time, 2)

    def test_ctor_w_custom_time_before(self):
        import datetime

        custom_time_before = datetime.date(2018, 8, 1)
        conditions = self._make_one(
            number_of_newer_versions=3, custom_time_before=custom_time_before
        )
        expected = {
            "numNewerVersions": 3,
            "customTimeBefore": custom_time_before.isoformat(),
        }
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertEqual(conditions.number_of_newer_versions, 3)
        self.assertEqual(conditions.custom_time_before, custom_time_before)

    def test_ctor_w_noncurrent_time_before(self):
        import datetime

        noncurrent_before = datetime.date(2018, 8, 1)
        conditions = self._make_one(
            number_of_newer_versions=3, noncurrent_time_before=noncurrent_before
        )

        expected = {
            "numNewerVersions": 3,
            "noncurrentTimeBefore": noncurrent_before.isoformat(),
        }
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertEqual(conditions.number_of_newer_versions, 3)
        self.assertEqual(conditions.noncurrent_time_before, noncurrent_before)

    def test_ctor_w_matches_prefix(self):
        conditions = self._make_one(matches_prefix=["test-prefix"])
        expected = {"matchesPrefix": ["test-prefix"]}
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertIsNone(conditions.matches_suffix)
        self.assertEqual(conditions.matches_prefix, ["test-prefix"])

    def test_ctor_w_matches_suffix(self):
        conditions = self._make_one(matches_suffix=["test-suffix"])
        expected = {"matchesSuffix": ["test-suffix"]}
        self.assertEqual(dict(conditions), expected)
        self.assertIsNone(conditions.age)
        self.assertIsNone(conditions.created_before)
        self.assertIsNone(conditions.is_live)
        self.assertIsNone(conditions.matches_storage_class)
        self.assertIsNone(conditions.matches_prefix)
        self.assertEqual(conditions.matches_suffix, ["test-suffix"])

    def test_from_api_repr(self):
        import datetime

        custom_time_before = datetime.date(2018, 8, 1)
        noncurrent_before = datetime.date(2018, 8, 1)
        before = datetime.date(2018, 8, 1)
        klass = self._get_target_class()
        resource = {
            "age": 10,
            "createdBefore": "2018-08-01",
            "isLive": True,
            "matchesStorageClass": ["COLDLINE"],
            "numNewerVersions": 3,
            "daysSinceCustomTime": 2,
            "customTimeBefore": custom_time_before.isoformat(),
            "daysSinceNoncurrentTime": 2,
            "noncurrentTimeBefore": noncurrent_before.isoformat(),
        }
        conditions = klass.from_api_repr(resource)
        self.assertEqual(conditions.age, 10)
        self.assertEqual(conditions.created_before, before)
        self.assertEqual(conditions.is_live, True)
        self.assertEqual(conditions.matches_storage_class, ["COLDLINE"])
        self.assertEqual(conditions.number_of_newer_versions, 3)
        self.assertEqual(conditions.days_since_custom_time, 2)
        self.assertEqual(conditions.custom_time_before, custom_time_before)
        self.assertEqual(conditions.days_since_noncurrent_time, 2)
        self.assertEqual(conditions.noncurrent_time_before, noncurrent_before)


class Test_LifecycleRuleDelete(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import LifecycleRuleDelete

        return LifecycleRuleDelete

    def _make_one(self, **kw):
        return self._get_target_class()(**kw)

    def test_ctor_wo_conditions(self):
        with self.assertRaises(ValueError):
            self._make_one()

    def test_ctor_w_condition(self):
        rule = self._make_one(age=10, matches_storage_class=["COLDLINE"])
        expected = {
            "action": {"type": "Delete"},
            "condition": {"age": 10, "matchesStorageClass": ["COLDLINE"]},
        }
        self.assertEqual(dict(rule), expected)

    def test_from_api_repr(self):
        klass = self._get_target_class()
        conditions = {
            "age": 10,
            "createdBefore": "2018-08-01",
            "isLive": True,
            "matchesStorageClass": ["COLDLINE"],
            "numNewerVersions": 3,
        }
        resource = {"action": {"type": "Delete"}, "condition": conditions}
        rule = klass.from_api_repr(resource)
        self.assertEqual(dict(rule), resource)


class Test_LifecycleRuleSetStorageClass(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import LifecycleRuleSetStorageClass

        return LifecycleRuleSetStorageClass

    def _make_one(self, **kw):
        return self._get_target_class()(**kw)

    def test_ctor_wo_conditions(self):
        with self.assertRaises(ValueError):
            self._make_one(storage_class="COLDLINE")

    def test_ctor_w_condition(self):
        rule = self._make_one(
            storage_class="COLDLINE", age=10, matches_storage_class=["NEARLINE"]
        )
        expected = {
            "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
            "condition": {"age": 10, "matchesStorageClass": ["NEARLINE"]},
        }
        self.assertEqual(dict(rule), expected)

    def test_from_api_repr(self):
        klass = self._get_target_class()
        conditions = {
            "age": 10,
            "createdBefore": "2018-08-01",
            "isLive": True,
            "matchesStorageClass": ["NEARLINE"],
            "numNewerVersions": 3,
        }
        resource = {
            "action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
            "condition": conditions,
        }
        rule = klass.from_api_repr(resource)
        self.assertEqual(dict(rule), resource)


class Test_LifecycleRuleAbortIncompleteMultipartUpload(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import (
            LifecycleRuleAbortIncompleteMultipartUpload,
        )

        return LifecycleRuleAbortIncompleteMultipartUpload

    def _make_one(self, **kw):
        return self._get_target_class()(**kw)

    def test_ctor_wo_conditions(self):
        with self.assertRaises(ValueError):
            self._make_one()

    def test_ctor_w_condition(self):
        rule = self._make_one(age=10)
        expected = {
            "action": {"type": "AbortIncompleteMultipartUpload"},
            "condition": {"age": 10},
        }
        self.assertEqual(dict(rule), expected)

    def test_from_api_repr(self):
        klass = self._get_target_class()
        conditions = {
            "age": 10,
        }
        resource = {
            "action": {"type": "AbortIncompleteMultipartUpload"},
            "condition": conditions,
        }
        rule = klass.from_api_repr(resource)
        self.assertEqual(dict(rule), resource)


class Test_IAMConfiguration(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import IAMConfiguration

        return IAMConfiguration

    def _make_one(self, bucket, **kw):
        return self._get_target_class()(bucket, **kw)

    @staticmethod
    def _make_bucket():
        from google.cloud.storage.bucket import Bucket

        return mock.create_autospec(Bucket, instance=True)

    def test_ctor_defaults(self):
        bucket = self._make_bucket()

        config = self._make_one(bucket)

        self.assertIs(config.bucket, bucket)
        self.assertFalse(config.uniform_bucket_level_access_enabled)
        self.assertIsNone(config.uniform_bucket_level_access_locked_time)
        # TODO: Remove unspecified after changeover is complete
        self.assertIn(
            config.public_access_prevention,
            [PUBLIC_ACCESS_PREVENTION_UNSPECIFIED, PUBLIC_ACCESS_PREVENTION_INHERITED],
        )
        self.assertFalse(config.bucket_policy_only_enabled)
        self.assertIsNone(config.bucket_policy_only_locked_time)

    def test_ctor_explicit_ubla(self):
        bucket = self._make_bucket()
        now = _NOW(_UTC)

        config = self._make_one(
            bucket,
            uniform_bucket_level_access_enabled=True,
            uniform_bucket_level_access_locked_time=now,
        )

        self.assertIs(config.bucket, bucket)
        self.assertTrue(config.uniform_bucket_level_access_enabled)
        self.assertEqual(config.uniform_bucket_level_access_locked_time, now)
        self.assertTrue(config.bucket_policy_only_enabled)
        self.assertEqual(config.bucket_policy_only_locked_time, now)

    def test_ctor_explicit_pap(self):
        bucket = self._make_bucket()

        config = self._make_one(
            bucket,
            public_access_prevention=PUBLIC_ACCESS_PREVENTION_ENFORCED,
        )

        self.assertIs(config.bucket, bucket)
        self.assertFalse(config.uniform_bucket_level_access_enabled)
        self.assertEqual(
            config.public_access_prevention, PUBLIC_ACCESS_PREVENTION_ENFORCED
        )

        config.public_access_prevention = PUBLIC_ACCESS_PREVENTION_INHERITED
        # TODO: Remove unspecified after changeover is complete
        self.assertIn(
            config.public_access_prevention,
            [PUBLIC_ACCESS_PREVENTION_UNSPECIFIED, PUBLIC_ACCESS_PREVENTION_INHERITED],
        )

    def test_ctor_explicit_bpo(self):
        bucket = self._make_bucket()
        now = _NOW(_UTC)

        config = pytest.deprecated_call(
            self._make_one,
            bucket,
            bucket_policy_only_enabled=True,
            bucket_policy_only_locked_time=now,
        )

        self.assertIs(config.bucket, bucket)
        self.assertTrue(config.uniform_bucket_level_access_enabled)
        self.assertEqual(config.uniform_bucket_level_access_locked_time, now)
        self.assertTrue(config.bucket_policy_only_enabled)
        self.assertEqual(config.bucket_policy_only_locked_time, now)

    def test_ctor_ubla_and_bpo_enabled(self):
        bucket = self._make_bucket()

        with self.assertRaises(ValueError):
            self._make_one(
                bucket,
                uniform_bucket_level_access_enabled=True,
                bucket_policy_only_enabled=True,
            )

    def test_ctor_ubla_and_bpo_time(self):
        bucket = self._make_bucket()
        now = _NOW(_UTC)

        with self.assertRaises(ValueError):
            self._make_one(
                bucket,
                uniform_bucket_level_access_enabled=True,
                uniform_bucket_level_access_locked_time=now,
                bucket_policy_only_locked_time=now,
            )

    def test_from_api_repr_w_empty_resource(self):
        klass = self._get_target_class()
        bucket = self._make_bucket()
        resource = {}

        config = klass.from_api_repr(resource, bucket)

        self.assertIs(config.bucket, bucket)
        self.assertFalse(config.bucket_policy_only_enabled)
        self.assertIsNone(config.bucket_policy_only_locked_time)

    def test_from_api_repr_w_empty_bpo(self):
        klass = self._get_target_class()
        bucket = self._make_bucket()
        resource = {"uniformBucketLevelAccess": {}}

        config = klass.from_api_repr(resource, bucket)

        self.assertIs(config.bucket, bucket)
        self.assertFalse(config.bucket_policy_only_enabled)
        self.assertIsNone(config.bucket_policy_only_locked_time)

    def test_from_api_repr_w_disabled(self):
        klass = self._get_target_class()
        bucket = self._make_bucket()
        resource = {"uniformBucketLevelAccess": {"enabled": False}}

        config = klass.from_api_repr(resource, bucket)

        self.assertIs(config.bucket, bucket)
        self.assertFalse(config.bucket_policy_only_enabled)
        self.assertIsNone(config.bucket_policy_only_locked_time)

    def test_from_api_repr_w_enabled(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        klass = self._get_target_class()
        bucket = self._make_bucket()
        now = _NOW(_UTC)
        resource = {
            "uniformBucketLevelAccess": {
                "enabled": True,
                "lockedTime": _datetime_to_rfc3339(now),
            }
        }

        config = klass.from_api_repr(resource, bucket)

        self.assertIs(config.bucket, bucket)
        self.assertTrue(config.uniform_bucket_level_access_enabled)
        self.assertEqual(config.uniform_bucket_level_access_locked_time, now)
        self.assertTrue(config.bucket_policy_only_enabled)
        self.assertEqual(config.bucket_policy_only_locked_time, now)

    def test_uniform_bucket_level_access_enabled_setter(self):
        bucket = self._make_bucket()
        config = self._make_one(bucket)

        config.uniform_bucket_level_access_enabled = True
        self.assertTrue(config.bucket_policy_only_enabled)

        self.assertTrue(config["uniformBucketLevelAccess"]["enabled"])
        bucket._patch_property.assert_called_once_with("iamConfiguration", config)

    def test_bucket_policy_only_enabled_setter(self):
        bucket = self._make_bucket()
        config = self._make_one(bucket)

        with pytest.deprecated_call():
            config.bucket_policy_only_enabled = True

        self.assertTrue(config.uniform_bucket_level_access_enabled)
        self.assertTrue(config["uniformBucketLevelAccess"]["enabled"])
        bucket._patch_property.assert_called_once_with("iamConfiguration", config)


class Test_Bucket(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import Bucket

        return Bucket

    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    @staticmethod
    def _make_client(**kw):
        from google.cloud.storage.client import Client

        kw["api_endpoint"] = kw.get("api_endpoint") or _get_default_storage_base_url()
        return mock.create_autospec(Client, instance=True, **kw)

    def _make_one(
        self,
        client=None,
        name=None,
        properties=None,
        user_project=None,
        generation=None,
    ):
        if client is None:
            client = self._make_client()
        if user_project is None:
            bucket = self._get_target_class()(client, name=name, generation=generation)
        else:
            bucket = self._get_target_class()(
                client, name=name, user_project=user_project, generation=generation
            )
        if properties:
            bucket._properties = {**bucket._properties, **properties}
        return bucket

    def test_ctor_w_invalid_name(self):
        NAME = "#invalid"
        with self.assertRaises(ValueError):
            self._make_one(name=NAME)

    def test_ctor(self):
        NAME = "name"
        properties = {"key": "value"}
        bucket = self._make_one(name=NAME, properties=properties)
        self.assertEqual(bucket.name, NAME)
        self.assertEqual(bucket._properties, properties)
        self.assertEqual(list(bucket._changes), [])
        self.assertFalse(bucket._acl.loaded)
        self.assertIs(bucket._acl.bucket, bucket)
        self.assertFalse(bucket._default_object_acl.loaded)
        self.assertIs(bucket._default_object_acl.bucket, bucket)
        self.assertEqual(list(bucket._label_removals), [])
        self.assertIsNone(bucket.user_project)
        self.assertEqual(bucket.generation, None)
        self.assertEqual(bucket.soft_delete_time, None)
        self.assertEqual(bucket.hard_delete_time, None)

    def test_ctor_w_user_project(self):
        NAME = "name"
        USER_PROJECT = "user-project-123"
        client = self._make_client()
        bucket = self._make_one(client, name=NAME, user_project=USER_PROJECT)
        self.assertEqual(bucket.name, NAME)
        self.assertEqual(bucket._properties, {})
        self.assertEqual(list(bucket._changes), [])
        self.assertFalse(bucket._acl.loaded)
        self.assertIs(bucket._acl.bucket, bucket)
        self.assertFalse(bucket._default_object_acl.loaded)
        self.assertIs(bucket._default_object_acl.bucket, bucket)
        self.assertEqual(list(bucket._label_removals), [])
        self.assertEqual(bucket.user_project, USER_PROJECT)

    def test_ctor_w_generation_and_soft_delete_info(self):
        from google.cloud._helpers import _RFC3339_MICROS

        NAME = "name"
        generation = 12345

        soft_timestamp = datetime.datetime(2024, 1, 5, 20, 34, 37, tzinfo=_UTC)
        soft_delete = soft_timestamp.strftime(_RFC3339_MICROS)
        hard_timestamp = datetime.datetime(2024, 1, 15, 20, 34, 37, tzinfo=_UTC)
        hard_delete = hard_timestamp.strftime(_RFC3339_MICROS)
        properties = {"softDeleteTime": soft_delete, "hardDeleteTime": hard_delete}

        bucket = self._make_one(name=NAME, generation=generation, properties=properties)
        self.assertEqual(bucket.name, NAME)
        self.assertEqual(list(bucket._changes), [])
        self.assertFalse(bucket._acl.loaded)
        self.assertIs(bucket._acl.bucket, bucket)
        self.assertFalse(bucket._default_object_acl.loaded)
        self.assertIs(bucket._default_object_acl.bucket, bucket)
        self.assertEqual(list(bucket._label_removals), [])
        self.assertIsNone(bucket.user_project)
        self.assertEqual(bucket.generation, generation)
        self.assertEqual(bucket.soft_delete_time, soft_timestamp)
        self.assertEqual(bucket.hard_delete_time, hard_timestamp)

    def test_blob_wo_keys(self):
        from google.cloud.storage.blob import Blob

        BUCKET_NAME = "BUCKET_NAME"
        BLOB_NAME = "BLOB_NAME"
        CHUNK_SIZE = 1024 * 1024

        bucket = self._make_one(name=BUCKET_NAME)
        blob = bucket.blob(BLOB_NAME, chunk_size=CHUNK_SIZE)
        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertIs(blob.client, bucket.client)
        self.assertEqual(blob.name, BLOB_NAME)
        self.assertEqual(blob.chunk_size, CHUNK_SIZE)
        self.assertIsNone(blob._encryption_key)
        self.assertIsNone(blob.kms_key_name)

    def test_blob_w_encryption_key(self):
        from google.cloud.storage.blob import Blob

        BUCKET_NAME = "BUCKET_NAME"
        BLOB_NAME = "BLOB_NAME"
        CHUNK_SIZE = 1024 * 1024
        KEY = b"01234567890123456789012345678901"  # 32 bytes

        bucket = self._make_one(name=BUCKET_NAME)
        blob = bucket.blob(BLOB_NAME, chunk_size=CHUNK_SIZE, encryption_key=KEY)
        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertIs(blob.client, bucket.client)
        self.assertEqual(blob.name, BLOB_NAME)
        self.assertEqual(blob.chunk_size, CHUNK_SIZE)
        self.assertEqual(blob._encryption_key, KEY)
        self.assertIsNone(blob.kms_key_name)

    def test_blob_w_generation(self):
        from google.cloud.storage.blob import Blob

        BUCKET_NAME = "BUCKET_NAME"
        BLOB_NAME = "BLOB_NAME"
        GENERATION = 123

        bucket = self._make_one(name=BUCKET_NAME)
        blob = bucket.blob(BLOB_NAME, generation=GENERATION)
        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertIs(blob.client, bucket.client)
        self.assertEqual(blob.name, BLOB_NAME)
        self.assertEqual(blob.generation, GENERATION)

    def test_blob_w_kms_key_name(self):
        from google.cloud.storage.blob import Blob

        BUCKET_NAME = "BUCKET_NAME"
        BLOB_NAME = "BLOB_NAME"
        CHUNK_SIZE = 1024 * 1024
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )

        bucket = self._make_one(name=BUCKET_NAME)
        blob = bucket.blob(BLOB_NAME, chunk_size=CHUNK_SIZE, kms_key_name=KMS_RESOURCE)
        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertIs(blob.client, bucket.client)
        self.assertEqual(blob.name, BLOB_NAME)
        self.assertEqual(blob.chunk_size, CHUNK_SIZE)
        self.assertIsNone(blob._encryption_key)
        self.assertEqual(blob.kms_key_name, KMS_RESOURCE)

    def test_notification_defaults(self):
        from google.cloud.storage.notification import (
            NONE_PAYLOAD_FORMAT,
            BucketNotification,
        )

        PROJECT = "PROJECT"
        BUCKET_NAME = "BUCKET_NAME"
        TOPIC_NAME = "TOPIC_NAME"
        client = self._make_client(project=PROJECT)
        bucket = self._make_one(client, name=BUCKET_NAME)

        notification = bucket.notification(TOPIC_NAME)

        self.assertIsInstance(notification, BucketNotification)
        self.assertIs(notification.bucket, bucket)
        self.assertEqual(notification.topic_project, PROJECT)
        self.assertIsNone(notification.custom_attributes)
        self.assertIsNone(notification.event_types)
        self.assertIsNone(notification.blob_name_prefix)
        self.assertEqual(notification.payload_format, NONE_PAYLOAD_FORMAT)

    def test_notification_explicit(self):
        from google.cloud.storage.notification import (
            JSON_API_V1_PAYLOAD_FORMAT,
            OBJECT_DELETE_EVENT_TYPE,
            OBJECT_FINALIZE_EVENT_TYPE,
            BucketNotification,
        )

        PROJECT = "PROJECT"
        BUCKET_NAME = "BUCKET_NAME"
        TOPIC_NAME = "TOPIC_NAME"
        TOPIC_ALT_PROJECT = "topic-project-456"
        CUSTOM_ATTRIBUTES = {"attr1": "value1", "attr2": "value2"}
        EVENT_TYPES = [OBJECT_FINALIZE_EVENT_TYPE, OBJECT_DELETE_EVENT_TYPE]
        BLOB_NAME_PREFIX = "blob-name-prefix/"
        client = self._make_client(project=PROJECT)
        bucket = self._make_one(client, name=BUCKET_NAME)

        notification = bucket.notification(
            TOPIC_NAME,
            topic_project=TOPIC_ALT_PROJECT,
            custom_attributes=CUSTOM_ATTRIBUTES,
            event_types=EVENT_TYPES,
            blob_name_prefix=BLOB_NAME_PREFIX,
            payload_format=JSON_API_V1_PAYLOAD_FORMAT,
        )

        self.assertIsInstance(notification, BucketNotification)
        self.assertIs(notification.bucket, bucket)
        self.assertEqual(notification.topic_project, TOPIC_ALT_PROJECT)
        self.assertEqual(notification.custom_attributes, CUSTOM_ATTRIBUTES)
        self.assertEqual(notification.event_types, EVENT_TYPES)
        self.assertEqual(notification.blob_name_prefix, BLOB_NAME_PREFIX)
        self.assertEqual(notification.payload_format, JSON_API_V1_PAYLOAD_FORMAT)

    def test_bucket_name_value(self):
        BUCKET_NAME = "bucket-name"
        self._make_one(name=BUCKET_NAME)

        bad_start_bucket_name = "/testing123"
        with self.assertRaises(ValueError):
            self._make_one(name=bad_start_bucket_name)

        bad_end_bucket_name = "testing123/"
        with self.assertRaises(ValueError):
            self._make_one(name=bad_end_bucket_name)

    def test_user_project(self):
        BUCKET_NAME = "name"
        USER_PROJECT = "user-project-123"
        bucket = self._make_one(name=BUCKET_NAME)
        bucket._user_project = USER_PROJECT
        self.assertEqual(bucket.user_project, USER_PROJECT)

    def test_exists_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        bucket_name = "bucket-name"
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.side_effect = NotFound("testing")
        bucket = self._make_one(client, name=bucket_name)

        self.assertFalse(bucket.exists())

        expected_query_params = {"fields": "name"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_exists_w_etag_match(self):
        bucket_name = "bucket-name"
        etag = "kittens"
        api_response = {"name": bucket_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=bucket_name)

        self.assertTrue(bucket.exists(if_etag_match=etag))

        expected_query_params = {
            "fields": "name",
        }
        expected_headers = {
            "If-Match": etag,
        }
        client._get_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_exists_w_metageneration_match_w_timeout(self):
        bucket_name = "bucket-name"
        metageneration_number = 6
        timeout = 42
        api_response = {"name": bucket_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=bucket_name)

        self.assertTrue(
            bucket.exists(timeout=42, if_metageneration_match=metageneration_number)
        )

        expected_query_params = {
            "fields": "name",
            "ifMetagenerationMatch": metageneration_number,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_exists_hit_w_user_project_w_retry_w_explicit_client(self):
        bucket_name = "bucket-name"
        user_project = "user-project-123"
        retry = mock.Mock(spec=[])
        api_response = {"name": bucket_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(name=bucket_name, user_project=user_project)

        self.assertTrue(bucket.exists(client=client, retry=retry))

        expected_query_params = {
            "fields": "name",
            "userProject": user_project,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=None,
        )

    def test_acl_property(self):
        from google.cloud.storage.acl import BucketACL

        bucket = self._make_one()
        acl = bucket.acl
        self.assertIsInstance(acl, BucketACL)
        self.assertIs(acl, bucket._acl)

    def test_default_object_acl_property(self):
        from google.cloud.storage.acl import DefaultObjectACL

        bucket = self._make_one()
        acl = bucket.default_object_acl
        self.assertIsInstance(acl, DefaultObjectACL)
        self.assertIs(acl, bucket._default_object_acl)

    def test_path_no_name(self):
        bucket = self._make_one()
        self.assertRaises(ValueError, getattr, bucket, "path")

    def test_path_w_name(self):
        NAME = "name"
        bucket = self._make_one(name=NAME)
        self.assertEqual(bucket.path, f"/b/{NAME}")

    def test_get_blob_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        from google.cloud.storage.blob import Blob

        name = "name"
        blob_name = "nonesuch"
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.side_effect = NotFound("testing")
        bucket = self._make_one(client, name=name)

        result = bucket.get_blob(blob_name)

        self.assertIsNone(result)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {"projection": "noAcl"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=mock.ANY,
        )

        target = client._get_resource.call_args[1]["_target_object"]
        self.assertIsInstance(target, Blob)
        self.assertIs(target.bucket, bucket)
        self.assertEqual(target.name, blob_name)

    def test_get_blob_hit_w_user_project(self):
        from google.cloud.storage.blob import Blob

        name = "name"
        blob_name = "blob-name"
        user_project = "user-project-123"
        api_response = {"name": blob_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name, user_project=user_project)

        blob = bucket.get_blob(blob_name, client=client)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "userProject": user_project,
            "projection": "noAcl",
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=blob,
        )

    def test_get_blob_hit_w_generation_w_soft_deleted(self):
        from google.cloud.storage.blob import Blob

        name = "name"
        blob_name = "blob-name"
        generation = 1512565576797178
        api_response = {"name": blob_name, "generation": generation}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name)

        blob = bucket.get_blob(blob_name, generation=generation, soft_deleted=True)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob.generation, generation)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "generation": generation,
            "projection": "noAcl",
            "softDeleted": True,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=blob,
        )

    def test_get_blob_hit_w_generation_w_timeout(self):
        from google.cloud.storage.blob import Blob

        name = "name"
        blob_name = "blob-name"
        generation = 1512565576797178
        timeout = 42
        api_response = {"name": blob_name, "generation": generation}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name)

        blob = bucket.get_blob(blob_name, generation=generation, timeout=timeout)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob.generation, generation)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "generation": generation,
            "projection": "noAcl",
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=blob,
        )

    def test_get_blob_w_etag_match_w_retry(self):
        from google.cloud.storage.blob import Blob

        name = "name"
        blob_name = "blob-name"
        etag = "kittens"
        retry = mock.Mock(spec=[])
        api_response = {"name": blob_name, "etag": etag}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name)

        blob = bucket.get_blob(blob_name, if_etag_match=etag, retry=retry)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob.etag, etag)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "projection": "noAcl",
        }
        expected_headers = {
            "If-Match": etag,
        }
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=blob,
        )

    def test_get_blob_w_generation_match_w_retry(self):
        from google.cloud.storage.blob import Blob

        name = "name"
        blob_name = "blob-name"
        generation = 1512565576797178
        retry = mock.Mock(spec=[])
        api_response = {"name": blob_name, "generation": generation}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name)

        blob = bucket.get_blob(blob_name, if_generation_match=generation, retry=retry)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob.generation, generation)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "ifGenerationMatch": generation,
            "projection": "noAcl",
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=blob,
        )

    def test_get_blob_hit_with_kwargs_w_explicit_client(self):
        from google.cloud.storage.blob import Blob, _get_encryption_headers

        name = "name"
        blob_name = "blob-name"
        chunk_size = 1024 * 1024
        key = b"01234567890123456789012345678901"  # 32 bytes
        api_response = {"name": blob_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(name=name)

        blob = bucket.get_blob(
            blob_name, client=client, encryption_key=key, chunk_size=chunk_size
        )

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, blob_name)
        self.assertEqual(blob.chunk_size, chunk_size)
        self.assertEqual(blob._encryption_key, key)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "projection": "noAcl",
        }
        expected_headers = _get_encryption_headers(key)
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=blob,
        )

    def test_list_blobs_w_defaults(self):
        name = "name"
        client = self._make_client()
        client.list_blobs = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=name)

        iterator = bucket.list_blobs()

        self.assertIs(iterator, client.list_blobs.return_value)

        expected_page_token = None
        expected_max_results = None
        expected_prefix = None
        expected_delimiter = None
        expected_match_glob = None
        expected_start_offset = None
        expected_end_offset = None
        expected_include_trailing_delimiter = None
        expected_versions = None
        expected_projection = "noAcl"
        expected_fields = None
        expected_include_folders_as_prefixes = None
        soft_deleted = None
        page_size = None
        filter_ = None
        client.list_blobs.assert_called_once_with(
            bucket,
            max_results=expected_max_results,
            page_token=expected_page_token,
            prefix=expected_prefix,
            delimiter=expected_delimiter,
            start_offset=expected_start_offset,
            end_offset=expected_end_offset,
            include_trailing_delimiter=expected_include_trailing_delimiter,
            versions=expected_versions,
            projection=expected_projection,
            fields=expected_fields,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            match_glob=expected_match_glob,
            include_folders_as_prefixes=expected_include_folders_as_prefixes,
            soft_deleted=soft_deleted,
            page_size=page_size,
            filter_=filter_,
        )

    def test_list_blobs_w_explicit(self):
        name = "name"
        max_results = 10
        page_token = "ABCD"
        prefix = "subfolder"
        delimiter = "/"
        match_glob = "**txt"
        start_offset = "c"
        end_offset = "g"
        include_trailing_delimiter = True
        include_folders_as_prefixes = True
        versions = True
        soft_deleted = True
        page_size = 2
        projection = "full"
        fields = "items/contentLanguage,nextPageToken"
        bucket = self._make_one(client=None, name=name)
        other_client = self._make_client()
        other_client.list_blobs = mock.Mock(spec=[])
        timeout = 42
        retry = mock.Mock(spec=[])

        iterator = bucket.list_blobs(
            max_results=max_results,
            page_token=page_token,
            prefix=prefix,
            delimiter=delimiter,
            start_offset=start_offset,
            end_offset=end_offset,
            include_trailing_delimiter=include_trailing_delimiter,
            versions=versions,
            projection=projection,
            fields=fields,
            client=other_client,
            timeout=timeout,
            retry=retry,
            match_glob=match_glob,
            include_folders_as_prefixes=include_folders_as_prefixes,
            soft_deleted=soft_deleted,
            page_size=page_size,
        )

        self.assertIs(iterator, other_client.list_blobs.return_value)

        expected_page_token = page_token
        expected_max_results = max_results
        expected_prefix = prefix
        expected_delimiter = delimiter
        expected_match_glob = match_glob
        expected_start_offset = start_offset
        expected_end_offset = end_offset
        expected_include_trailing_delimiter = include_trailing_delimiter
        expected_versions = versions
        expected_projection = projection
        expected_fields = fields
        expected_include_folders_as_prefixes = include_folders_as_prefixes
        expected_soft_deleted = soft_deleted
        expected_page_size = page_size
        expected_filter = None
        other_client.list_blobs.assert_called_once_with(
            bucket,
            max_results=expected_max_results,
            page_token=expected_page_token,
            prefix=expected_prefix,
            delimiter=expected_delimiter,
            start_offset=expected_start_offset,
            end_offset=expected_end_offset,
            include_trailing_delimiter=expected_include_trailing_delimiter,
            versions=expected_versions,
            projection=expected_projection,
            fields=expected_fields,
            timeout=timeout,
            retry=retry,
            match_glob=expected_match_glob,
            include_folders_as_prefixes=expected_include_folders_as_prefixes,
            soft_deleted=expected_soft_deleted,
            page_size=expected_page_size,
            filter_=expected_filter,
        )

    def test_list_blobs_w_filter(self):
        name = "name"
        filter_ = 'contexts."foo"="bar"'
        bucket = self._make_one(client=None, name=name)
        other_client = self._make_client()
        other_client.list_blobs = mock.Mock(spec=[])

        iterator = bucket.list_blobs(filter_=filter_, client=other_client)

        self.assertIs(iterator, other_client.list_blobs.return_value)

        expected_page_token = None
        expected_max_results = None
        expected_prefix = None
        expected_delimiter = None
        expected_match_glob = None
        expected_start_offset = None
        expected_end_offset = None
        expected_include_trailing_delimiter = None
        expected_versions = None
        expected_projection = "noAcl"
        expected_fields = None
        expected_include_folders_as_prefixes = None
        expected_soft_deleted = None
        expected_page_size = None
        expected_filter = filter_
        other_client.list_blobs.assert_called_once_with(
            bucket,
            max_results=expected_max_results,
            page_token=expected_page_token,
            prefix=expected_prefix,
            delimiter=expected_delimiter,
            start_offset=expected_start_offset,
            end_offset=expected_end_offset,
            include_trailing_delimiter=expected_include_trailing_delimiter,
            versions=expected_versions,
            projection=expected_projection,
            fields=expected_fields,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            match_glob=expected_match_glob,
            include_folders_as_prefixes=expected_include_folders_as_prefixes,
            soft_deleted=expected_soft_deleted,
            page_size=expected_page_size,
            filter_=expected_filter,
        )

    def test_list_notifications_w_defaults(self):
        from google.cloud.storage.bucket import _item_to_notification

        bucket_name = "name"
        client = self._make_client()
        client._list_resource = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=bucket_name)

        iterator = bucket.list_notifications()

        self.assertIs(iterator, client._list_resource.return_value)
        self.assertIs(iterator.bucket, bucket)

        expected_path = f"/b/{bucket_name}/notificationConfigs"
        expected_item_to_value = _item_to_notification
        client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_list_notifications_w_explicit(self):
        from google.cloud.storage.bucket import _item_to_notification

        bucket_name = "name"
        other_client = self._make_client()
        other_client._list_resource = mock.Mock(spec=[])
        bucket = self._make_one(client=None, name=bucket_name)
        timeout = 42
        retry = mock.Mock(spec=[])

        iterator = bucket.list_notifications(
            client=other_client,
            timeout=timeout,
            retry=retry,
        )

        self.assertIs(iterator, other_client._list_resource.return_value)
        self.assertIs(iterator.bucket, bucket)

        expected_path = f"/b/{bucket_name}/notificationConfigs"
        expected_item_to_value = _item_to_notification
        other_client._list_resource.assert_called_once_with(
            expected_path,
            expected_item_to_value,
            timeout=timeout,
            retry=retry,
        )

    def test_get_notification_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        project = "my-project-123"
        name = "name"
        notification_id = "1"

        client = mock.Mock(spec=["_get_resource", "project"])
        client._get_resource.side_effect = NotFound("testing")
        client.project = project
        bucket = self._make_one(client=client, name=name)

        with self.assertRaises(NotFound):
            bucket.get_notification(notification_id=notification_id)

        expected_path = f"/b/{name}/notificationConfigs/{notification_id}"
        expected_query_params = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_get_notification_hit_w_explicit_w_user_project(self):
        from google.cloud.storage.notification import (
            _TOPIC_REF_FMT,
            JSON_API_V1_PAYLOAD_FORMAT,
            BucketNotification,
        )

        project = "my-project-123"
        user_project = "user-project-456"
        name = "name"
        etag = "FACECABB"
        notification_id = "1"
        self_link = "https://example.com/notification/1"
        api_response = {
            "topic": _TOPIC_REF_FMT.format("my-project-123", "topic-1"),
            "id": notification_id,
            "etag": etag,
            "selfLink": self_link,
            "payload_format": JSON_API_V1_PAYLOAD_FORMAT,
        }
        timeout = 42
        retry = mock.Mock(spec=[])
        client = mock.Mock(spec=["_get_resource", "project"])
        client._get_resource.return_value = api_response
        client.project = project
        bucket = self._make_one(client=client, name=name, user_project=user_project)

        notification = bucket.get_notification(
            notification_id=notification_id,
            timeout=timeout,
            retry=retry,
        )

        self.assertIsInstance(notification, BucketNotification)
        self.assertEqual(notification.notification_id, notification_id)
        self.assertEqual(notification.etag, etag)
        self.assertEqual(notification.self_link, self_link)
        self.assertIsNone(notification.custom_attributes)
        self.assertIsNone(notification.event_types)
        self.assertIsNone(notification.blob_name_prefix)
        self.assertEqual(notification.payload_format, JSON_API_V1_PAYLOAD_FORMAT)

        expected_path = f"/b/{name}/notificationConfigs/{notification_id}"
        expected_query_params = {"userProject": user_project}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
        )

    def test_delete_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        name = "name"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.side_effect = NotFound("testing")
        bucket = self._make_one(client=client, name=name)

        with self.assertRaises(NotFound):
            bucket.delete()

        expected_query_params = {}
        client._delete_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_hit_w_metageneration_match_w_explicit_client(self):
        name = "name"
        metageneration_number = 6
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=None, name=name)

        result = bucket.delete(
            client=client,
            if_metageneration_match=metageneration_number,
        )

        self.assertIsNone(result)

        expected_query_params = {"ifMetagenerationMatch": metageneration_number}
        client._delete_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_hit_evicts_from_cache(self):
        name = "bucket-to-delete"
        client = mock.Mock(spec=["_delete_resource", "_bucket_metadata_cache"])
        cache = mock.Mock()
        client._bucket_metadata_cache = cache
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name)

        result = bucket.delete()

        self.assertIsNone(result)
        cache.evict.assert_called_once_with(name)

        client._delete_resource.assert_called_once_with(
            bucket.path,
            query_params={},
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_hit_w_force_w_user_project_w_explicit_timeout_retry(self):
        name = "name"
        user_project = "user-project-123"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name, user_project=user_project)
        bucket.list_blobs = mock.Mock(return_value=iter([]))
        bucket.delete_blobs = mock.Mock(return_value=None)
        timeout = 42
        retry = mock.Mock(spec=[])

        result = bucket.delete(force=True, timeout=timeout, retry=retry)

        self.assertIsNone(result)

        bucket.list_blobs.assert_called_once_with(
            max_results=bucket._MAX_OBJECTS_FOR_ITERATION + 1,
            client=client,
            timeout=timeout,
            retry=retry,
            versions=True,
        )

        bucket.delete_blobs.assert_called_once_with(
            [],
            on_error=mock.ANY,
            client=client,
            timeout=timeout,
            retry=retry,
            preserve_generation=True,
        )

        expected_query_params = {"userProject": user_project}
        client._delete_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
            _target_object=None,
        )

    def test_delete_hit_w_force_delete_blobs(self):
        name = "name"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name)
        blobs = [mock.Mock(spec=[]), mock.Mock(spec=[])]
        bucket.list_blobs = mock.Mock(return_value=iter(blobs))
        bucket.delete_blobs = mock.Mock(return_value=None)

        result = bucket.delete(force=True)

        self.assertIsNone(result)

        bucket.list_blobs.assert_called_once_with(
            max_results=bucket._MAX_OBJECTS_FOR_ITERATION + 1,
            client=client,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            versions=True,
        )

        bucket.delete_blobs.assert_called_once_with(
            blobs,
            on_error=mock.ANY,
            client=client,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            preserve_generation=True,
        )

        expected_query_params = {}
        client._delete_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_w_force_w_user_project_w_miss_on_blob(self):
        from google.cloud.exceptions import NotFound

        name = "name"
        blob_name = "blob-name"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name)
        blob = mock.Mock(spec=["name", "generation"])
        blob.name = blob_name
        GEN = 1234
        blob.generation = GEN
        blobs = [blob]
        bucket.list_blobs = mock.Mock(return_value=iter(blobs))
        bucket.delete_blob = mock.Mock(side_effect=NotFound("testing"))

        result = bucket.delete(force=True)

        self.assertIsNone(result)

        bucket.delete_blob.assert_called_once_with(
            blob_name,
            client=client,
            generation=GEN,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

        expected_query_params = {}
        client._delete_resource.assert_called_once_with(
            bucket.path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_w_too_many(self):
        name = "name"
        blob_name1 = "blob-name1"
        blob_name2 = "blob-name2"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name)
        blob1 = mock.Mock(spec=["name"])
        blob1.name = blob_name1
        blob2 = mock.Mock(spec=["name"])
        blob2.name = blob_name2
        blobs = [blob1, blob2]
        bucket.list_blobs = mock.Mock(return_value=iter(blobs))
        bucket.delete_blobs = mock.Mock()
        # Make the Bucket refuse to delete with 2 objects.
        bucket._MAX_OBJECTS_FOR_ITERATION = 1

        with self.assertRaises(ValueError):
            bucket.delete(force=True)

        bucket.delete_blobs.assert_not_called()

    def test_delete_blob_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        name = "name"
        blob_name = "nonesuch"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.side_effect = NotFound("testing")
        bucket = self._make_one(client=client, name=name)

        with self.assertRaises(NotFound):
            bucket.delete_blob(blob_name)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {}
        client._delete_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_blob_hit_w_user_project_w_timeout(self):
        name = "name"
        blob_name = "blob-name"
        user_project = "user-project-123"
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name, user_project=user_project)
        timeout = 42

        result = bucket.delete_blob(blob_name, timeout=timeout)

        self.assertIsNone(result)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {"userProject": user_project}
        client._delete_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_blob_hit_w_generation_w_retry(self):
        name = "name"
        blob_name = "blob-name"
        generation = 1512565576797178
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name)
        retry = mock.Mock(spec=[])

        result = bucket.delete_blob(blob_name, generation=generation, retry=retry)

        self.assertIsNone(result)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {"generation": generation}
        client._delete_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=None,
        )

    def test_delete_blob_hit_w_generation_match(self):
        name = "name"
        blob_name = "blob-name"
        generation = 6
        metageneration = 9
        client = mock.Mock(spec=["_delete_resource"])
        client._delete_resource.return_value = None
        bucket = self._make_one(client=client, name=name)

        result = bucket.delete_blob(
            blob_name,
            if_generation_match=generation,
            if_metageneration_match=metageneration,
        )

        self.assertIsNone(result)

        expected_path = f"/b/{name}/o/{blob_name}"
        expected_query_params = {
            "ifGenerationMatch": generation,
            "ifMetagenerationMatch": metageneration,
        }
        client._delete_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_delete_blobs_empty(self):
        name = "name"
        bucket = self._make_one(client=None, name=name)
        bucket.delete_blob = mock.Mock()

        bucket.delete_blobs([])

        bucket.delete_blob.assert_not_called()

    def test_delete_blobs_hit_w_explicit_client_w_timeout(self):
        name = "name"
        blob_name = "blob-name"
        client = mock.Mock(spec=[])
        bucket = self._make_one(client=None, name=name)
        bucket.delete_blob = mock.Mock()
        timeout = 42

        bucket.delete_blobs([blob_name], client=client, timeout=timeout)

        bucket.delete_blob.assert_called_once_with(
            blob_name,
            client=client,
            generation=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=timeout,
            retry=DEFAULT_RETRY,
        )

    def test_delete_blobs_w_generation_match_wrong_len(self):
        name = "name"
        blob_name = "blob-name"
        blob_name2 = "blob-name2"
        generation_number = 6
        bucket = self._make_one(client=None, name=name)
        bucket.delete_blob = mock.Mock()

        with self.assertRaises(ValueError):
            bucket.delete_blobs(
                [blob_name, blob_name2],
                if_generation_not_match=[generation_number],
            )

        bucket.delete_blob.assert_not_called()

    def test_delete_blobs_w_generation_match_w_retry(self):
        name = "name"
        blob_name = "blob-name"
        blob_name2 = "blob-name2"
        generation_number = 6
        generation_number2 = 9
        client = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=name)
        bucket.delete_blob = mock.Mock()
        retry = mock.Mock(spec=[])

        bucket.delete_blobs(
            [blob_name, blob_name2],
            if_generation_match=[generation_number, generation_number2],
            retry=retry,
        )

        call_1 = mock.call(
            blob_name,
            client=None,
            generation=None,
            if_generation_match=generation_number,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=retry,
        )
        call_2 = mock.call(
            blob_name2,
            client=None,
            generation=None,
            if_generation_match=generation_number2,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=retry,
        )
        bucket.delete_blob.assert_has_calls([call_1, call_2])

    def test_delete_blobs_w_generation_match_none(self):
        name = "name"
        blob_name = "blob-name"
        blob_name2 = "blob-name2"
        generation_number = 6
        generation_number2 = None
        client = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=name)
        bucket.delete_blob = mock.Mock()

        bucket.delete_blobs(
            [blob_name, blob_name2],
            if_generation_match=[generation_number, generation_number2],
        )

        call_1 = mock.call(
            blob_name,
            client=None,
            generation=None,
            if_generation_match=generation_number,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )
        call_2 = mock.call(
            blob_name2,
            client=None,
            generation=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )
        bucket.delete_blob.assert_has_calls([call_1, call_2])

    def test_delete_blobs_w_preserve_generation(self):
        name = "name"
        blob_name = "blob-name"
        blob_name2 = "blob-name2"
        generation_number = 1234567890
        generation_number2 = 7890123456
        client = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=name)
        blob = self._make_blob(bucket.name, blob_name)
        blob.generation = generation_number
        blob2 = self._make_blob(bucket.name, blob_name2)
        blob2.generation = generation_number2
        bucket.delete_blob = mock.Mock()
        retry = mock.Mock(spec=[])

        # Test generation is propagated from list of blob instances
        bucket.delete_blobs(
            [blob, blob2],
            preserve_generation=True,
            retry=retry,
        )

        call_1 = mock.call(
            blob_name,
            client=None,
            generation=generation_number,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=retry,
        )
        call_2 = mock.call(
            blob_name2,
            client=None,
            generation=generation_number2,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=retry,
        )
        bucket.delete_blob.assert_has_calls([call_1, call_2])

    def test_delete_blobs_miss_wo_on_error(self):
        from google.cloud.exceptions import NotFound

        name = "name"
        blob_name = "blob-name"
        blob_name2 = "nonesuch"
        client = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=name)
        bucket.delete_blob = mock.Mock()
        bucket.delete_blob.side_effect = [None, NotFound("testing")]

        with self.assertRaises(NotFound):
            bucket.delete_blobs([blob_name, blob_name2])

        call_1 = mock.call(
            blob_name,
            client=None,
            generation=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )
        call_2 = mock.call(
            blob_name2,
            client=None,
            generation=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )
        bucket.delete_blob.assert_has_calls([call_1, call_2])

    def test_delete_blobs_miss_w_on_error(self):
        from google.cloud.exceptions import NotFound

        name = "name"
        blob_name = "blob-name"
        blob_name2 = "nonesuch"
        client = mock.Mock(spec=[])
        bucket = self._make_one(client=client, name=name)
        bucket.delete_blob = mock.Mock()
        bucket.delete_blob.side_effect = [None, NotFound("testing")]

        errors = []
        bucket.delete_blobs([blob_name, blob_name2], on_error=errors.append)

        self.assertEqual(errors, [blob_name2])

        call_1 = mock.call(
            blob_name,
            client=None,
            generation=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )
        call_2 = mock.call(
            blob_name2,
            client=None,
            generation=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )
        bucket.delete_blob.assert_has_calls([call_1, call_2])

    def test_reload_w_etag_match(self):
        name = "name"
        etag = "kittens"
        api_response = {"name": name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name)

        bucket.reload(if_etag_match=etag)

        expected_path = f"/b/{name}"
        expected_query_params = {
            "projection": "noAcl",
        }
        expected_headers = {
            "If-Match": etag,
        }
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_reload_forbidden_sync_cache_fallback(self):
        from google.api_core.exceptions import Forbidden

        from google.cloud.storage._bucket_metadata_cache import BucketMetadataCache

        name = "forbidden-bucket"
        client = mock.Mock(spec=["_get_resource", "_bucket_metadata_cache"])
        client._bucket_metadata_cache = BucketMetadataCache(client)
        client._get_resource.side_effect = Forbidden("forbidden")
        bucket = self._make_one(client, name=name)

        # Ensure cache is clear
        client._bucket_metadata_cache.clear()

        with self.assertRaises(Forbidden):
            bucket.reload()

        # Assert cache was synchronously populated with fallback
        cached = client._bucket_metadata_cache.get(name)
        self.assertIsNotNone(cached)
        dest_id, loc = cached
        self.assertEqual(dest_id, f"//storage.googleapis.com/projects/_/buckets/{name}")
        self.assertEqual(loc, "global")

    def test_reload_w_metageneration_match(self):
        name = "name"
        metageneration_number = 9
        api_response = {"name": name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name)

        bucket.reload(if_metageneration_match=metageneration_number)

        expected_path = f"/b/{name}"
        expected_query_params = {
            "projection": "noAcl",
            "ifMetagenerationMatch": metageneration_number,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_reload_w_generation_match(self):
        client = self._make_client()
        bucket = self._make_one(client=client, name="name")

        with self.assertRaises(TypeError):
            bucket.reload(if_generation_match=6)

    def test_reload_w_soft_deleted(self):
        name = "name"
        api_response = {"name": name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client, name=name, generation=12345)

        bucket.reload(soft_deleted=True)

        expected_path = f"/b/{name}"
        expected_query_params = {
            "projection": "noAcl",
            "softDeleted": True,
            "generation": 12345,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_update_w_metageneration_match(self):
        name = "name"
        metageneration_number = 9
        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = {}
        bucket = self._make_one(client=client, name=name)

        bucket.update(if_metageneration_match=metageneration_number)

        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": metageneration_number,
        }
        client._put_resource.assert_called_once_with(
            bucket.path,
            bucket._properties,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
            _target_object=bucket,
        )

    def test_update_w_generation_match(self):
        name = "name"
        generation_number = 6
        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = {}
        bucket = self._make_one(client=client, name=name)

        with self.assertRaises(TypeError):
            bucket.update(if_generation_match=generation_number)

        client._put_resource.assert_not_called()

    @staticmethod
    def _make_blob(bucket_name, blob_name):
        from google.cloud.storage.blob import Blob

        blob = mock.create_autospec(Blob)
        blob.name = blob_name
        blob.path = f"/b/{bucket_name}/o/{blob_name}"
        return blob

    def test_copy_blobs_wo_name(self):
        source_name = "source"
        dest_name = "dest"
        blob_name = "blob-name"
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(client=client, name=source_name)
        dest = self._make_one(client=client, name=dest_name)
        blob = self._make_blob(source_name, blob_name)

        new_blob = source.copy_blob(blob, dest)

        self.assertIs(new_blob.bucket, dest)
        self.assertEqual(new_blob.name, blob_name)

        expected_path = "/b/{}/o/{}/copyTo/b/{}/o/{}".format(
            source_name, blob_name, dest_name, blob_name
        )
        expected_data = None
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=new_blob,
        )

    def test_copy_blob_w_source_generation_w_timeout(self):
        source_name = "source"
        dest_name = "dest"
        blob_name = "blob-name"
        generation = 1512565576797178
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(client=client, name=source_name)
        dest = self._make_one(client=client, name=dest_name)
        blob = self._make_blob(source_name, blob_name)
        timeout = 42

        new_blob = source.copy_blob(
            blob,
            dest,
            source_generation=generation,
            timeout=timeout,
        )

        self.assertIs(new_blob.bucket, dest)
        self.assertEqual(new_blob.name, blob_name)

        expected_path = "/b/{}/o/{}/copyTo/b/{}/o/{}".format(
            source_name, blob_name, dest_name, blob_name
        )
        expected_data = None
        expected_query_params = {"sourceGeneration": generation}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=new_blob,
        )

    def test_copy_blob_w_generation_match_w_retry(self):
        source_name = "source"
        dest_name = "dest"
        blob_name = "blob-name"
        generation_number = 6
        source_generation_number = 9
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(client=client, name=source_name)
        dest = self._make_one(client=client, name=dest_name)
        blob = self._make_blob(source_name, blob_name)
        retry = mock.Mock(spec=[])

        new_blob = source.copy_blob(
            blob,
            dest,
            if_generation_match=generation_number,
            if_source_generation_match=source_generation_number,
            retry=retry,
        )
        self.assertIs(new_blob.bucket, dest)
        self.assertEqual(new_blob.name, blob_name)

        expected_path = "/b/{}/o/{}/copyTo/b/{}/o/{}".format(
            source_name, blob_name, dest_name, blob_name
        )
        expected_data = None
        expected_query_params = {
            "ifGenerationMatch": generation_number,
            "ifSourceGenerationMatch": source_generation_number,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=new_blob,
        )

    def test_copy_blob_w_preserve_acl_false_w_explicit_client(self):
        from google.cloud.storage.acl import ObjectACL

        source_name = "source"
        dest_name = "dest"
        blob_name = "blob-name"
        new_name = "new_name"
        post_api_response = {}
        patch_api_response = {}
        client = mock.Mock(spec=["_post_resource", "_patch_resource"])
        client._post_resource.return_value = post_api_response
        client._patch_resource.return_value = patch_api_response
        source = self._make_one(client=None, name=source_name)
        dest = self._make_one(client=None, name=dest_name)
        blob = self._make_blob(source_name, blob_name)

        new_blob = source.copy_blob(
            blob, dest, new_name, client=client, preserve_acl=False
        )

        self.assertIs(new_blob.bucket, dest)
        self.assertEqual(new_blob.name, new_name)
        self.assertIsInstance(new_blob.acl, ObjectACL)

        expected_copy_path = "/b/{}/o/{}/copyTo/b/{}/o/{}".format(
            source_name, blob_name, dest_name, new_name
        )
        expected_copy_data = None
        expected_copy_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_copy_path,
            expected_copy_data,
            query_params=expected_copy_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=new_blob,
        )

        expected_patch_path = f"/b/{dest_name}/o/{new_name}"
        expected_patch_data = {"acl": []}
        expected_patch_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            expected_patch_path,
            expected_patch_data,
            query_params=expected_patch_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_copy_blob_w_name_and_user_project(self):
        source_name = "source"
        dest_name = "dest"
        blob_name = "blob-name"
        new_name = "new_name"
        user_project = "user-project-123"
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(
            client=client, name=source_name, user_project=user_project
        )
        dest = self._make_one(client=client, name=dest_name)
        blob = self._make_blob(source_name, blob_name)

        new_blob = source.copy_blob(blob, dest, new_name)

        self.assertIs(new_blob.bucket, dest)
        self.assertEqual(new_blob.name, new_name)

        expected_path = "/b/{}/o/{}/copyTo/b/{}/o/{}".format(
            source_name, blob_name, dest_name, new_name
        )
        expected_data = None
        expected_query_params = {"userProject": user_project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=new_blob,
        )

    def test_copy_blob_w_destination_contexts(self):
        from google.cloud.storage.blob import (
            ObjectContexts,
            ObjectCustomContextPayload,
        )

        source_name = "source"
        dest_name = "dest"
        blob_name = "blob-name"
        new_name = "new_name"
        api_response = {"contexts": {"custom": {"foo": {"value": "bar"}}}}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(client=client, name=source_name)
        dest = self._make_one(client=client, name=dest_name)
        blob = self._make_blob(source_name, blob_name)

        payload = ObjectCustomContextPayload(value="bar")
        contexts = ObjectContexts(None, custom={"foo": payload})

        new_blob = source.copy_blob(
            blob,
            dest,
            new_name,
            destination_contexts=contexts,
        )

        self.assertIs(new_blob.bucket, dest)
        self.assertEqual(new_blob.name, new_name)
        self.assertEqual(new_blob.contexts.custom["foo"].value, "bar")

        expected_path = "/b/{}/o/{}/copyTo/b/{}/o/{}".format(
            source_name, blob_name, dest_name, new_name
        )
        expected_data = {"contexts": {"custom": {"foo": {"value": "bar"}}}}
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=new_blob,
        )

    def test_move_blob_w_no_retry_timeout_and_generation_match(self):
        source_name = "source"
        blob_name = "blob-name"
        new_name = "new_name"
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(client=client, name=source_name)
        blob = self._make_blob(source_name, blob_name)

        new_blob = source.move_blob(
            blob, new_name, if_generation_match=0, retry=None, timeout=30
        )

        self.assertIs(new_blob.bucket, source)
        self.assertEqual(new_blob.name, new_name)

        expected_path = "/b/{}/o/{}/moveTo/o/{}".format(
            source_name, blob_name, new_name
        )
        expected_data = None
        expected_query_params = {"ifGenerationMatch": 0}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=30,
            retry=None,
            _target_object=new_blob,
        )

    def test_move_blob_needs_url_encoding(self):
        source_name = "source"
        blob_name = "blob-name"
        new_name = "new/name"
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(client=client, name=source_name)
        blob = self._make_blob(source_name, blob_name)

        new_blob = source.move_blob(
            blob, new_name, if_generation_match=0, retry=None, timeout=30
        )

        self.assertIs(new_blob.bucket, source)
        self.assertEqual(new_blob.name, new_name)

        expected_path = "/b/{}/o/{}/moveTo/o/{}".format(
            source_name, blob_name, _quote(new_name)
        )
        expected_data = None
        expected_query_params = {"ifGenerationMatch": 0}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=30,
            retry=None,
            _target_object=new_blob,
        )

    def test_move_blob_w_user_project(self):
        source_name = "source"
        blob_name = "blob-name"
        new_name = "new_name"
        user_project = "user-project-123"
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source = self._make_one(
            client=client, name=source_name, user_project=user_project
        )
        blob = self._make_blob(source_name, blob_name)

        new_blob = source.move_blob(blob, new_name)

        self.assertIs(new_blob.bucket, source)
        self.assertEqual(new_blob.name, new_name)

        expected_path = "/b/{}/o/{}/moveTo/o/{}".format(
            source_name, blob_name, new_name
        )
        expected_data = None
        expected_query_params = {"userProject": user_project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=new_blob,
        )

    def _rename_blob_helper(self, explicit_client=False, same_name=False, **kw):
        bucket_name = "BUCKET_NAME"
        blob_name = "blob-name"

        if same_name:
            new_blob_name = blob_name
        else:
            new_blob_name = "new-blob-name"

        client = mock.Mock(spec=[])
        kw = kw.copy()

        if explicit_client:
            bucket = self._make_one(client=None, name=bucket_name)
            expected_client = kw["client"] = client
        else:
            bucket = self._make_one(client=client, name=bucket_name)
            expected_client = None

        expected_i_g_m = kw.get("if_generation_match")
        expected_i_g_n_m = kw.get("if_generation_not_match")
        expected_i_m_m = kw.get("if_metageneration_match")
        expected_i_m_n_m = kw.get("if_metageneration_not_match")
        expected_i_s_g_m = kw.get("if_source_generation_match")
        expected_i_s_g_n_m = kw.get("if_source_generation_not_match")
        expected_i_s_m_m = kw.get("if_source_metageneration_match")
        expected_i_s_m_n_m = kw.get("if_source_metageneration_not_match")
        expected_timeout = kw.get("timeout", self._get_default_timeout())
        expected_retry = kw.get("retry", DEFAULT_RETRY_IF_GENERATION_SPECIFIED)

        bucket.copy_blob = mock.Mock(spec=[])
        blob = self._make_blob(bucket_name, blob_name)

        renamed_blob = bucket.rename_blob(blob, new_blob_name, **kw)

        self.assertIs(renamed_blob, bucket.copy_blob.return_value)

        bucket.copy_blob.assert_called_once_with(
            blob,
            bucket,
            new_blob_name,
            client=expected_client,
            if_generation_match=expected_i_g_m,
            if_generation_not_match=expected_i_g_n_m,
            if_metageneration_match=expected_i_m_m,
            if_metageneration_not_match=expected_i_m_n_m,
            if_source_generation_match=expected_i_s_g_m,
            if_source_generation_not_match=expected_i_s_g_n_m,
            if_source_metageneration_match=expected_i_s_m_m,
            if_source_metageneration_not_match=expected_i_s_m_n_m,
            timeout=expected_timeout,
            retry=expected_retry,
        )

        if same_name:
            blob.delete.assert_not_called()
        else:
            blob.delete.assert_called_once_with(
                client=expected_client,
                if_generation_match=expected_i_s_g_m,
                if_generation_not_match=expected_i_s_g_n_m,
                if_metageneration_match=expected_i_s_m_m,
                if_metageneration_not_match=expected_i_s_m_n_m,
                timeout=expected_timeout,
                retry=expected_retry,
            )

    def test_rename_blob_w_defaults(self):
        self._rename_blob_helper()

    def test_rename_blob_w_explicit_client(self):
        self._rename_blob_helper(explicit_client=True)

    def test_rename_blob_w_generation_match(self):
        generation_number = 6
        source_generation_number = 7
        source_metageneration_number = 9

        self._rename_blob_helper(
            if_generation_match=generation_number,
            if_source_generation_match=source_generation_number,
            if_source_metageneration_not_match=source_metageneration_number,
        )

    def test_rename_blob_w_timeout(self):
        timeout = 42
        self._rename_blob_helper(timeout=timeout)

    def test_rename_blob_w_retry(self):
        retry = mock.Mock(spec={})
        self._rename_blob_helper(retry=retry)

    def test_rename_blob_to_itself(self):
        self._rename_blob_helper(same_name=True)

    def test_etag(self):
        ETAG = "ETAG"
        properties = {"etag": ETAG}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.etag, ETAG)

    def test_id(self):
        ID = "ID"
        properties = {"id": ID}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.id, ID)

    def test_location_getter(self):
        NAME = "name"
        before = {"location": "AS"}
        bucket = self._make_one(name=NAME, properties=before)
        self.assertEqual(bucket.location, "AS")

    @mock.patch("warnings.warn")
    def test_location_setter(self, mock_warn):
        from google.cloud.storage import bucket as bucket_module

        NAME = "name"
        bucket = self._make_one(name=NAME)
        self.assertIsNone(bucket.location)
        bucket.location = "AS"
        self.assertEqual(bucket.location, "AS")
        self.assertTrue("location" in bucket._changes)
        mock_warn.assert_called_once_with(
            bucket_module._LOCATION_SETTER_MESSAGE, DeprecationWarning, stacklevel=2
        )

    def test_iam_configuration_policy_missing(self):
        from google.cloud.storage.bucket import IAMConfiguration

        NAME = "name"
        bucket = self._make_one(name=NAME)

        config = bucket.iam_configuration

        self.assertIsInstance(config, IAMConfiguration)
        self.assertIs(config.bucket, bucket)
        self.assertFalse(config.bucket_policy_only_enabled)
        self.assertIsNone(config.bucket_policy_only_locked_time)

    def test_iam_configuration_policy_w_entry(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        from google.cloud.storage.bucket import IAMConfiguration

        now = _NOW(_UTC)
        NAME = "name"
        properties = {
            "iamConfiguration": {
                "uniformBucketLevelAccess": {
                    "enabled": True,
                    "lockedTime": _datetime_to_rfc3339(now),
                }
            }
        }
        bucket = self._make_one(name=NAME, properties=properties)

        config = bucket.iam_configuration

        self.assertIsInstance(config, IAMConfiguration)
        self.assertIs(config.bucket, bucket)
        self.assertTrue(config.uniform_bucket_level_access_enabled)
        self.assertEqual(config.uniform_bucket_level_access_locked_time, now)

    @mock.patch("warnings.warn")
    def test_lifecycle_rules_getter_unknown_action_type(self, mock_warn):
        NAME = "name"
        BOGUS_RULE = {"action": {"type": "Bogus"}, "condition": {"age": 42}}
        rules = [BOGUS_RULE]
        properties = {"lifecycle": {"rule": rules}}
        bucket = self._make_one(name=NAME, properties=properties)

        list(bucket.lifecycle_rules)
        mock_warn.assert_called_with(
            "Unknown lifecycle rule type received: {}. Please upgrade to the latest version of google-cloud-storage.".format(
                BOGUS_RULE
            ),
            UserWarning,
            stacklevel=1,
        )

    def test_lifecycle_rules_getter(self):
        from google.cloud.storage.bucket import (
            LifecycleRuleAbortIncompleteMultipartUpload,
            LifecycleRuleDelete,
            LifecycleRuleSetStorageClass,
        )

        NAME = "name"
        DELETE_RULE = {"action": {"type": "Delete"}, "condition": {"age": 42}}
        SSC_RULE = {
            "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
            "condition": {"isLive": False},
        }
        MULTIPART_RULE = {
            "action": {"type": "AbortIncompleteMultipartUpload"},
            "condition": {"age": 42},
        }
        rules = [DELETE_RULE, SSC_RULE, MULTIPART_RULE]
        properties = {"lifecycle": {"rule": rules}}
        bucket = self._make_one(name=NAME, properties=properties)

        found = list(bucket.lifecycle_rules)

        delete_rule = found[0]
        self.assertIsInstance(delete_rule, LifecycleRuleDelete)
        self.assertEqual(dict(delete_rule), DELETE_RULE)

        ssc_rule = found[1]
        self.assertIsInstance(ssc_rule, LifecycleRuleSetStorageClass)
        self.assertEqual(dict(ssc_rule), SSC_RULE)

        multipart_rule = found[2]
        self.assertIsInstance(
            multipart_rule, LifecycleRuleAbortIncompleteMultipartUpload
        )
        self.assertEqual(dict(multipart_rule), MULTIPART_RULE)

    def test_lifecycle_rules_setter_w_dicts(self):
        NAME = "name"
        DELETE_RULE = {"action": {"type": "Delete"}, "condition": {"age": 42}}
        SSC_RULE = {
            "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
            "condition": {"isLive": False},
        }
        rules = [DELETE_RULE, SSC_RULE]
        bucket = self._make_one(name=NAME)
        self.assertEqual(list(bucket.lifecycle_rules), [])

        bucket.lifecycle_rules = rules

        self.assertEqual([dict(rule) for rule in bucket.lifecycle_rules], rules)
        self.assertTrue("lifecycle" in bucket._changes)

    def test_lifecycle_rules_setter_w_helpers(self):
        from google.cloud.storage.bucket import (
            LifecycleRuleDelete,
            LifecycleRuleSetStorageClass,
        )

        NAME = "name"
        DELETE_RULE = {"action": {"type": "Delete"}, "condition": {"age": 42}}
        SSC_RULE = {
            "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
            "condition": {"isLive": False},
        }
        rules = [DELETE_RULE, SSC_RULE]
        bucket = self._make_one(name=NAME)
        self.assertEqual(list(bucket.lifecycle_rules), [])

        bucket.lifecycle_rules = [
            LifecycleRuleDelete(age=42),
            LifecycleRuleSetStorageClass("NEARLINE", is_live=False),
        ]

        self.assertEqual([dict(rule) for rule in bucket.lifecycle_rules], rules)
        self.assertTrue("lifecycle" in bucket._changes)

    def test_clear_lifecycle_rules(self):
        NAME = "name"
        DELETE_RULE = {"action": {"type": "Delete"}, "condition": {"age": 42}}
        SSC_RULE = {
            "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
            "condition": {"isLive": False},
        }
        rules = [DELETE_RULE, SSC_RULE]
        bucket = self._make_one(name=NAME)
        bucket._properties["lifecycle"] = {"rule": rules}
        self.assertEqual(list(bucket.lifecycle_rules), rules)

        # This is a deprecated alias and will test both methods
        bucket.clear_lifecyle_rules()

        self.assertEqual(list(bucket.lifecycle_rules), [])
        self.assertTrue("lifecycle" in bucket._changes)

    def test_add_lifecycle_delete_rule(self):
        NAME = "name"
        DELETE_RULE = {"action": {"type": "Delete"}, "condition": {"age": 42}}
        rules = [DELETE_RULE]
        bucket = self._make_one(name=NAME)
        self.assertEqual(list(bucket.lifecycle_rules), [])

        bucket.add_lifecycle_delete_rule(age=42)

        self.assertEqual([dict(rule) for rule in bucket.lifecycle_rules], rules)
        self.assertTrue("lifecycle" in bucket._changes)

    def test_add_lifecycle_set_storage_class_rule(self):
        NAME = "name"
        SSC_RULE = {
            "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
            "condition": {"isLive": False},
        }
        rules = [SSC_RULE]
        bucket = self._make_one(name=NAME)
        self.assertEqual(list(bucket.lifecycle_rules), [])

        bucket.add_lifecycle_set_storage_class_rule("NEARLINE", is_live=False)

        self.assertEqual([dict(rule) for rule in bucket.lifecycle_rules], rules)
        self.assertTrue("lifecycle" in bucket._changes)

    def test_add_lifecycle_abort_incomplete_multipart_upload_rule(self):
        NAME = "name"
        AIMPU_RULE = {
            "action": {"type": "AbortIncompleteMultipartUpload"},
            "condition": {"age": 42},
        }
        rules = [AIMPU_RULE]
        bucket = self._make_one(name=NAME)
        self.assertEqual(list(bucket.lifecycle_rules), [])

        bucket.add_lifecycle_abort_incomplete_multipart_upload_rule(age=42)

        self.assertEqual([dict(rule) for rule in bucket.lifecycle_rules], rules)
        self.assertTrue("lifecycle" in bucket._changes)

    def test_cors_getter(self):
        NAME = "name"
        CORS_ENTRY = {
            "maxAgeSeconds": 1234,
            "method": ["OPTIONS", "GET"],
            "origin": ["127.0.0.1"],
            "responseHeader": ["Content-Type"],
        }
        properties = {"cors": [CORS_ENTRY, {}]}
        bucket = self._make_one(name=NAME, properties=properties)
        entries = bucket.cors
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0], CORS_ENTRY)
        self.assertEqual(entries[1], {})
        # Make sure it was a copy, not the same object.
        self.assertIsNot(entries[0], CORS_ENTRY)

    def test_cors_setter(self):
        NAME = "name"
        CORS_ENTRY = {
            "maxAgeSeconds": 1234,
            "method": ["OPTIONS", "GET"],
            "origin": ["127.0.0.1"],
            "responseHeader": ["Content-Type"],
        }
        bucket = self._make_one(name=NAME)

        self.assertEqual(bucket.cors, [])
        bucket.cors = [CORS_ENTRY]
        self.assertEqual(bucket.cors, [CORS_ENTRY])
        self.assertTrue("cors" in bucket._changes)

    def test_encryption_getter(self):
        from google.cloud.storage.bucket import BucketEncryption

        NAME = "name"
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        ENCRYPTION_CONFIG = {"defaultKmsKeyName": KMS_RESOURCE}
        bucket = self._make_one(name=NAME)
        self.assertIsNone(bucket.encryption.default_kms_key_name)
        bucket._properties["encryption"] = ENCRYPTION_CONFIG
        encryption = bucket.encryption
        self.assertIsInstance(encryption, BucketEncryption)
        self.assertEqual(encryption.default_kms_key_name, KMS_RESOURCE)

    def test_encryption_setter(self):
        from google.cloud.storage.bucket import BucketEncryption

        NAME = "name"
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        ENCRYPTION_CONFIG = {"defaultKmsKeyName": KMS_RESOURCE}
        bucket = self._make_one(name=NAME)
        encryption = BucketEncryption(bucket, default_kms_key_name=KMS_RESOURCE)
        bucket.encryption = encryption
        self.assertEqual(bucket._properties["encryption"], ENCRYPTION_CONFIG)
        self.assertTrue("encryption" in bucket._changes)

    def test_default_kms_key_name_getter(self):
        NAME = "name"
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        ENCRYPTION_CONFIG = {"defaultKmsKeyName": KMS_RESOURCE}
        bucket = self._make_one(name=NAME)
        self.assertIsNone(bucket.default_kms_key_name)
        bucket._properties["encryption"] = ENCRYPTION_CONFIG
        self.assertEqual(bucket.default_kms_key_name, KMS_RESOURCE)

    def test_default_kms_key_name_setter(self):
        NAME = "name"
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        ENCRYPTION_CONFIG = {"defaultKmsKeyName": KMS_RESOURCE}
        bucket = self._make_one(name=NAME)
        bucket.default_kms_key_name = KMS_RESOURCE
        self.assertEqual(bucket._properties["encryption"], ENCRYPTION_CONFIG)
        self.assertTrue("encryption" in bucket._changes)

    def test_labels_getter(self):
        NAME = "name"
        LABELS = {"color": "red", "flavor": "cherry"}
        properties = {"labels": LABELS}
        bucket = self._make_one(name=NAME, properties=properties)
        labels = bucket.labels
        self.assertEqual(labels, LABELS)
        # Make sure it was a copy, not the same object.
        self.assertIsNot(labels, LABELS)

    def test_labels_setter(self):
        NAME = "name"
        LABELS = {"color": "red", "flavor": "cherry"}
        bucket = self._make_one(name=NAME)

        self.assertEqual(bucket.labels, {})
        bucket.labels = LABELS
        self.assertEqual(bucket.labels, LABELS)
        self.assertIsNot(bucket._properties["labels"], LABELS)
        self.assertIn("labels", bucket._changes)

    def test_labels_setter_with_nan(self):
        NAME = "name"
        LABELS = {"color": "red", "foo": float("nan")}
        bucket = self._make_one(name=NAME)

        self.assertEqual(bucket.labels, {})
        bucket.labels = LABELS
        value = bucket.labels["foo"]
        self.assertIsInstance(value, str)

    def test_labels_setter_with_removal(self):
        # Make sure the bucket labels look correct and follow the expected
        # public structure.
        bucket = self._make_one(name="name")
        self.assertEqual(bucket.labels, {})
        bucket.labels = {"color": "red", "flavor": "cherry"}
        self.assertEqual(bucket.labels, {"color": "red", "flavor": "cherry"})
        bucket.labels = {"color": "red"}
        self.assertEqual(bucket.labels, {"color": "red"})

        # Make sure that a patch call correctly removes the flavor label.
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = {}

        bucket.patch(client=client)

        expected_patch_data = {
            "labels": {"color": "red", "flavor": None},
        }
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            bucket.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
            _target_object=bucket,
        )

        # A second patch call should be a no-op for labels.
        client._patch_resource.reset_mock()

        bucket.patch(client=client, timeout=42)

        expected_patch_data = {}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            bucket.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=42,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
            _target_object=bucket,
        )

    def test_location_type_getter_unset(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.location_type)

    def test_location_type_getter_set(self):
        from google.cloud.storage.constants import REGION_LOCATION_TYPE

        properties = {"locationType": REGION_LOCATION_TYPE}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.location_type, REGION_LOCATION_TYPE)

    def test_rpo_getter_and_setter(self):
        bucket = self._make_one()
        bucket.rpo = RPO_ASYNC_TURBO
        self.assertEqual(bucket.rpo, RPO_ASYNC_TURBO)
        bucket.rpo = RPO_DEFAULT
        self.assertIn("rpo", bucket._changes)
        self.assertEqual(bucket.rpo, RPO_DEFAULT)

    def test_autoclass_enabled_getter_and_setter(self):
        properties = {"autoclass": {"enabled": True}}
        bucket = self._make_one(properties=properties)
        self.assertTrue(bucket.autoclass_enabled)
        bucket.autoclass_enabled = False
        self.assertIn("autoclass", bucket._changes)
        self.assertFalse(bucket.autoclass_enabled)

    def test_autoclass_config_unset(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.autoclass_toggle_time)
        self.assertIsNone(bucket.autoclass_terminal_storage_class)
        self.assertIsNone(bucket.autoclass_terminal_storage_class_update_time)

        properties = {"autoclass": {}}
        bucket = self._make_one(properties=properties)
        self.assertIsNone(bucket.autoclass_toggle_time)
        self.assertIsNone(bucket.autoclass_terminal_storage_class)
        self.assertIsNone(bucket.autoclass_terminal_storage_class_update_time)

    def test_autoclass_toggle_and_tsc_update_time(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        effective_time = _NOW(_UTC)
        properties = {
            "autoclass": {
                "enabled": True,
                "toggleTime": _datetime_to_rfc3339(effective_time),
                "terminalStorageClass": "NEARLINE",
                "terminalStorageClassUpdateTime": _datetime_to_rfc3339(effective_time),
            }
        }
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.autoclass_toggle_time, effective_time)
        self.assertEqual(
            bucket.autoclass_terminal_storage_class_update_time, effective_time
        )

    def test_autoclass_tsc_getter_and_setter(self):
        from google.cloud.storage import constants

        properties = {
            "autoclass": {"terminalStorageClass": constants.ARCHIVE_STORAGE_CLASS}
        }
        bucket = self._make_one(properties=properties)
        self.assertEqual(
            bucket.autoclass_terminal_storage_class, constants.ARCHIVE_STORAGE_CLASS
        )
        bucket.autoclass_terminal_storage_class = constants.NEARLINE_STORAGE_CLASS
        self.assertIn("autoclass", bucket._changes)
        self.assertEqual(
            bucket.autoclass_terminal_storage_class, constants.NEARLINE_STORAGE_CLASS
        )

    def test_get_logging_w_prefix(self):
        NAME = "name"
        LOG_BUCKET = "logs"
        LOG_PREFIX = "pfx"
        before = {"logging": {"logBucket": LOG_BUCKET, "logObjectPrefix": LOG_PREFIX}}
        bucket = self._make_one(name=NAME, properties=before)
        info = bucket.get_logging()
        self.assertEqual(info["logBucket"], LOG_BUCKET)
        self.assertEqual(info["logObjectPrefix"], LOG_PREFIX)

    def test_enable_logging_defaults(self):
        NAME = "name"
        LOG_BUCKET = "logs"
        before = {"logging": None}
        bucket = self._make_one(name=NAME, properties=before)
        self.assertIsNone(bucket.get_logging())
        bucket.enable_logging(LOG_BUCKET)
        info = bucket.get_logging()
        self.assertEqual(info["logBucket"], LOG_BUCKET)
        self.assertEqual(info["logObjectPrefix"], "")

    def test_enable_logging(self):
        NAME = "name"
        LOG_BUCKET = "logs"
        LOG_PFX = "pfx"
        before = {"logging": None}
        bucket = self._make_one(name=NAME, properties=before)
        self.assertIsNone(bucket.get_logging())
        bucket.enable_logging(LOG_BUCKET, LOG_PFX)
        info = bucket.get_logging()
        self.assertEqual(info["logBucket"], LOG_BUCKET)
        self.assertEqual(info["logObjectPrefix"], LOG_PFX)

    def test_disable_logging(self):
        NAME = "name"
        before = {"logging": {"logBucket": "logs", "logObjectPrefix": "pfx"}}
        bucket = self._make_one(name=NAME, properties=before)
        self.assertIsNotNone(bucket.get_logging())
        bucket.disable_logging()
        self.assertIsNone(bucket.get_logging())

    def test_metageneration(self):
        METAGENERATION = 42
        properties = {"metageneration": METAGENERATION}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.metageneration, METAGENERATION)

    def test_metageneration_unset(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.metageneration)

    def test_metageneration_string_val(self):
        METAGENERATION = 42
        properties = {"metageneration": str(METAGENERATION)}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.metageneration, METAGENERATION)

    def test_owner(self):
        OWNER = {"entity": "project-owner-12345", "entityId": "23456"}
        properties = {"owner": OWNER}
        bucket = self._make_one(properties=properties)
        owner = bucket.owner
        self.assertEqual(owner["entity"], "project-owner-12345")
        self.assertEqual(owner["entityId"], "23456")

    def test_project_number(self):
        PROJECT_NUMBER = 12345
        properties = {"projectNumber": PROJECT_NUMBER}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.project_number, PROJECT_NUMBER)

    def test_project_number_unset(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.project_number)

    def test_project_number_string_val(self):
        PROJECT_NUMBER = 12345
        properties = {"projectNumber": str(PROJECT_NUMBER)}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.project_number, PROJECT_NUMBER)

    def test_retention_policy_effective_time_policy_missing(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.retention_policy_effective_time)

    def test_retention_policy_effective_time_et_missing(self):
        properties = {"retentionPolicy": {}}
        bucket = self._make_one(properties=properties)

        self.assertIsNone(bucket.retention_policy_effective_time)

    def test_retention_policy_effective_time(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        effective_time = _NOW(_UTC)
        properties = {
            "retentionPolicy": {"effectiveTime": _datetime_to_rfc3339(effective_time)}
        }
        bucket = self._make_one(properties=properties)

        self.assertEqual(bucket.retention_policy_effective_time, effective_time)

    def test_retention_policy_locked_missing(self):
        bucket = self._make_one()
        self.assertFalse(bucket.retention_policy_locked)

    def test_retention_policy_locked_false(self):
        properties = {"retentionPolicy": {"isLocked": False}}
        bucket = self._make_one(properties=properties)
        self.assertFalse(bucket.retention_policy_locked)

    def test_retention_policy_locked_true(self):
        properties = {"retentionPolicy": {"isLocked": True}}
        bucket = self._make_one(properties=properties)
        self.assertTrue(bucket.retention_policy_locked)

    def test_retention_period_getter_policymissing(self):
        bucket = self._make_one()

        self.assertIsNone(bucket.retention_period)

    def test_retention_period_getter_pr_missing(self):
        properties = {"retentionPolicy": {}}
        bucket = self._make_one(properties=properties)

        self.assertIsNone(bucket.retention_period)

    def test_retention_period_getter(self):
        period = 86400 * 100  # 100 days
        properties = {"retentionPolicy": {"retentionPeriod": str(period)}}
        bucket = self._make_one(properties=properties)

        self.assertEqual(bucket.retention_period, period)

    def test_retention_period_setter_w_none(self):
        period = 86400 * 100  # 100 days
        bucket = self._make_one()
        bucket._properties["retentionPolicy"] = {"retentionPeriod": period}

        bucket.retention_period = None

        self.assertIsNone(bucket._properties["retentionPolicy"])

    def test_retention_period_setter_w_int(self):
        period = 86400 * 100  # 100 days
        bucket = self._make_one()

        bucket.retention_period = period

        self.assertEqual(
            bucket._properties["retentionPolicy"]["retentionPeriod"], str(period)
        )

    def test_self_link(self):
        SELF_LINK = "http://example.com/self/"
        properties = {"selfLink": SELF_LINK}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.self_link, SELF_LINK)

    def test_storage_class_getter(self):
        from google.cloud.storage.constants import NEARLINE_STORAGE_CLASS

        properties = {"storageClass": NEARLINE_STORAGE_CLASS}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.storage_class, NEARLINE_STORAGE_CLASS)

    def test_storage_class_setter_invalid(self):
        invalid_class = "BOGUS"
        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = invalid_class

        # Test that invalid classes are allowed without client side validation.
        # Fall back to server side validation and errors.
        self.assertEqual(bucket.storage_class, invalid_class)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_STANDARD(self):
        from google.cloud.storage.constants import STANDARD_STORAGE_CLASS

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = STANDARD_STORAGE_CLASS
        self.assertEqual(bucket.storage_class, STANDARD_STORAGE_CLASS)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_NEARLINE(self):
        from google.cloud.storage.constants import NEARLINE_STORAGE_CLASS

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = NEARLINE_STORAGE_CLASS
        self.assertEqual(bucket.storage_class, NEARLINE_STORAGE_CLASS)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_COLDLINE(self):
        from google.cloud.storage.constants import COLDLINE_STORAGE_CLASS

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = COLDLINE_STORAGE_CLASS
        self.assertEqual(bucket.storage_class, COLDLINE_STORAGE_CLASS)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_ARCHIVE(self):
        from google.cloud.storage.constants import ARCHIVE_STORAGE_CLASS

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = ARCHIVE_STORAGE_CLASS
        self.assertEqual(bucket.storage_class, ARCHIVE_STORAGE_CLASS)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_MULTI_REGIONAL(self):
        from google.cloud.storage.constants import MULTI_REGIONAL_LEGACY_STORAGE_CLASS

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = MULTI_REGIONAL_LEGACY_STORAGE_CLASS
        self.assertEqual(bucket.storage_class, MULTI_REGIONAL_LEGACY_STORAGE_CLASS)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_REGIONAL(self):
        from google.cloud.storage.constants import REGIONAL_LEGACY_STORAGE_CLASS

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = REGIONAL_LEGACY_STORAGE_CLASS
        self.assertEqual(bucket.storage_class, REGIONAL_LEGACY_STORAGE_CLASS)
        self.assertTrue("storageClass" in bucket._changes)

    def test_storage_class_setter_DURABLE_REDUCED_AVAILABILITY(self):
        from google.cloud.storage.constants import (
            DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS,
        )

        NAME = "name"
        bucket = self._make_one(name=NAME)
        bucket.storage_class = DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS
        self.assertEqual(
            bucket.storage_class, DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS
        )
        self.assertTrue("storageClass" in bucket._changes)

    def test_time_created(self):
        from google.cloud._helpers import _RFC3339_MICROS

        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        TIME_CREATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"timeCreated": TIME_CREATED}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.time_created, TIMESTAMP)

    def test_time_created_unset(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.time_created)

    def test_updated(self):
        from google.cloud._helpers import _RFC3339_MICROS

        TIMESTAMP = datetime.datetime(2023, 11, 5, 20, 34, 37, tzinfo=_UTC)
        UPDATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"updated": UPDATED}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.updated, TIMESTAMP)

    def test_updated_unset(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.updated)

    def test_versioning_enabled_getter_missing(self):
        NAME = "name"
        bucket = self._make_one(name=NAME)
        self.assertEqual(bucket.versioning_enabled, False)

    def test_versioning_enabled_getter(self):
        NAME = "name"
        before = {"versioning": {"enabled": True}}
        bucket = self._make_one(name=NAME, properties=before)
        self.assertEqual(bucket.versioning_enabled, True)

    def test_create_w_defaults(self):
        bucket_name = "bucket-name"
        api_response = {"name": bucket_name}
        client = mock.Mock(spec=["create_bucket"])
        client.create_bucket.return_value = api_response
        bucket = self._make_one(client=client, name=bucket_name)

        bucket.create()

        client.create_bucket.assert_called_once_with(
            bucket_or_name=bucket,
            project=None,
            user_project=None,
            location=None,
            predefined_acl=None,
            predefined_default_object_acl=None,
            enable_object_retention=False,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_create_w_explicit(self):
        project = "PROJECT"
        location = "eu"
        user_project = "USER_PROJECT"
        bucket_name = "bucket-name"
        predefined_acl = "authenticatedRead"
        predefined_default_object_acl = "bucketOwnerFullControl"
        enable_object_retention = True
        api_response = {"name": bucket_name}
        client = mock.Mock(spec=["create_bucket"])
        client.create_bucket.return_value = api_response
        bucket = self._make_one(client=None, name=bucket_name)
        bucket._user_project = user_project
        timeout = 42
        retry = mock.Mock(spec=[])

        bucket.create(
            client=client,
            project=project,
            location=location,
            predefined_acl=predefined_acl,
            predefined_default_object_acl=predefined_default_object_acl,
            enable_object_retention=enable_object_retention,
            timeout=timeout,
            retry=retry,
        )

        client.create_bucket.assert_called_once_with(
            bucket_or_name=bucket,
            project=project,
            user_project=user_project,
            location=location,
            predefined_acl=predefined_acl,
            predefined_default_object_acl=predefined_default_object_acl,
            enable_object_retention=enable_object_retention,
            timeout=timeout,
            retry=retry,
        )

    def test_versioning_enabled_setter(self):
        NAME = "name"
        bucket = self._make_one(name=NAME)
        self.assertFalse(bucket.versioning_enabled)
        bucket.versioning_enabled = True
        self.assertTrue(bucket.versioning_enabled)

    def test_requester_pays_getter_missing(self):
        NAME = "name"
        bucket = self._make_one(name=NAME)
        self.assertEqual(bucket.requester_pays, False)

    def test_requester_pays_getter(self):
        NAME = "name"
        before = {"billing": {"requesterPays": True}}
        bucket = self._make_one(name=NAME, properties=before)
        self.assertEqual(bucket.requester_pays, True)

    def test_requester_pays_setter(self):
        NAME = "name"
        bucket = self._make_one(name=NAME)
        self.assertFalse(bucket.requester_pays)
        bucket.requester_pays = True
        self.assertTrue(bucket.requester_pays)

    def test_object_retention_mode_getter(self):
        bucket = self._make_one()
        self.assertIsNone(bucket.object_retention_mode)
        mode = "Enabled"
        properties = {"objectRetention": {"mode": mode}}
        bucket = self._make_one(properties=properties)
        self.assertEqual(bucket.object_retention_mode, mode)

    def test_soft_delete_policy_getter_w_entry(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        from google.cloud.storage.bucket import SoftDeletePolicy

        seconds = 86400 * 10  # 10 days
        effective_time = _NOW(_UTC)
        properties = {
            "softDeletePolicy": {
                "retentionDurationSeconds": seconds,
                "effectiveTime": _datetime_to_rfc3339(effective_time),
            }
        }
        bucket = self._make_one(properties=properties)

        policy = SoftDeletePolicy(
            bucket=bucket,
            retention_duration_seconds=seconds,
            effective_time=effective_time,
        )
        self.assertIsInstance(bucket.soft_delete_policy, SoftDeletePolicy)
        self.assertEqual(bucket.soft_delete_policy, policy)
        self.assertEqual(bucket.soft_delete_policy.retention_duration_seconds, seconds)
        self.assertEqual(bucket.soft_delete_policy.effective_time, effective_time)

    def test_soft_delete_policy_setter(self):
        bucket = self._make_one()
        policy = bucket.soft_delete_policy
        self.assertIsNone(policy.retention_duration_seconds)
        self.assertIsNone(policy.effective_time)

        seconds = 86400 * 10  # 10 days
        bucket.soft_delete_policy.retention_duration_seconds = seconds
        self.assertTrue("softDeletePolicy" in bucket._changes)
        self.assertEqual(bucket.soft_delete_policy.retention_duration_seconds, seconds)

    def test_hierarchical_namespace_enabled_getter_and_setter(self):
        # Test hierarchical_namespace configuration unset
        bucket = self._make_one()
        self.assertIsNone(bucket.hierarchical_namespace_enabled)

        # Test hierarchical_namespace configuration explicitly set
        properties = {"hierarchicalNamespace": {"enabled": True}}
        bucket = self._make_one(properties=properties)
        self.assertTrue(bucket.hierarchical_namespace_enabled)
        bucket.hierarchical_namespace_enabled = False
        self.assertIn("hierarchicalNamespace", bucket._changes)
        self.assertFalse(bucket.hierarchical_namespace_enabled)

    def test_configure_website_defaults(self):
        NAME = "name"
        UNSET = {"website": {"mainPageSuffix": None, "notFoundPage": None}}
        bucket = self._make_one(name=NAME)
        bucket.configure_website()
        self.assertEqual(bucket._properties, UNSET)

    def test_configure_website(self):
        NAME = "name"
        WEBSITE_VAL = {
            "website": {"mainPageSuffix": "html", "notFoundPage": "404.html"}
        }
        bucket = self._make_one(name=NAME)
        bucket.configure_website("html", "404.html")
        self.assertEqual(bucket._properties, WEBSITE_VAL)

    def test_disable_website(self):
        NAME = "name"
        UNSET = {"website": {"mainPageSuffix": None, "notFoundPage": None}}
        bucket = self._make_one(name=NAME)
        bucket.disable_website()
        self.assertEqual(bucket._properties, UNSET)

    def test_get_iam_policy_defaults(self):
        from google.api_core.iam import Policy

        from google.cloud.storage.iam import (
            STORAGE_EDITOR_ROLE,
            STORAGE_OWNER_ROLE,
            STORAGE_VIEWER_ROLE,
        )

        bucket_name = "name"
        path = f"/b/{bucket_name}"
        etag = "DEADBEEF"
        version = 1
        owner1 = "user:phred@example.com"
        owner2 = "group:cloud-logs@google.com"
        editor1 = "domain:google.com"
        editor2 = "user:phred@example.com"
        viewer1 = "serviceAccount:1234-abcdef@service.example.com"
        viewer2 = "user:phred@example.com"
        api_response = {
            "resourceId": path,
            "etag": etag,
            "version": version,
            "bindings": [
                {"role": STORAGE_OWNER_ROLE, "members": [owner1, owner2]},
                {"role": STORAGE_EDITOR_ROLE, "members": [editor1, editor2]},
                {"role": STORAGE_VIEWER_ROLE, "members": [viewer1, viewer2]},
            ],
        }
        expected_policy = {
            binding["role"]: set(binding["members"])
            for binding in api_response["bindings"]
        }
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client=client, name=bucket_name)

        policy = bucket.get_iam_policy()

        self.assertIsInstance(policy, Policy)
        self.assertEqual(policy.etag, api_response["etag"])
        self.assertEqual(policy.version, api_response["version"])
        self.assertEqual(dict(policy), expected_policy)

        expected_path = f"/b/{bucket_name}/iam"
        expected_query_params = {}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_get_iam_policy_w_user_project_w_timeout(self):
        from google.api_core.iam import Policy

        bucket_name = "name"
        timeout = 42
        user_project = "user-project-123"
        path = f"/b/{bucket_name}"
        etag = "DEADBEEF"
        version = 1
        api_response = {
            "resourceId": path,
            "etag": etag,
            "version": version,
            "bindings": [],
        }
        expected_policy = {}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(
            client=client, name=bucket_name, user_project=user_project
        )

        policy = bucket.get_iam_policy(timeout=timeout)

        self.assertIsInstance(policy, Policy)
        self.assertEqual(policy.etag, api_response["etag"])
        self.assertEqual(policy.version, api_response["version"])
        self.assertEqual(dict(policy), expected_policy)

        expected_path = f"/b/{bucket_name}/iam"
        expected_query_params = {"userProject": user_project}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_get_iam_policy_w_requested_policy_version_w_retry(self):
        from google.cloud.storage.iam import STORAGE_OWNER_ROLE

        bucket_name = "name"
        path = f"/b/{bucket_name}"
        etag = "DEADBEEF"
        version = 3
        owner1 = "user:phred@example.com"
        owner2 = "group:cloud-logs@google.com"
        api_response = {
            "resourceId": path,
            "etag": etag,
            "version": version,
            "bindings": [{"role": STORAGE_OWNER_ROLE, "members": [owner1, owner2]}],
        }
        retry = mock.Mock(spec=[])
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client=client, name=bucket_name)

        policy = bucket.get_iam_policy(requested_policy_version=3, retry=retry)

        self.assertEqual(policy.version, version)

        expected_path = f"/b/{bucket_name}/iam"
        expected_query_params = {"optionsRequestedPolicyVersion": version}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=None,
        )

    def test_set_iam_policy_w_defaults(self):
        import operator

        from google.api_core.iam import Policy

        from google.cloud.storage.iam import (
            STORAGE_EDITOR_ROLE,
            STORAGE_OWNER_ROLE,
            STORAGE_VIEWER_ROLE,
        )

        name = "name"
        etag = "DEADBEEF"
        version = 1
        owner1 = "user:phred@example.com"
        owner2 = "group:cloud-logs@google.com"
        editor1 = "domain:google.com"
        editor2 = "user:phred@example.com"
        viewer1 = "serviceAccount:1234-abcdef@service.example.com"
        viewer2 = "user:phred@example.com"
        bindings = [
            {"role": STORAGE_OWNER_ROLE, "members": [owner1, owner2]},
            {"role": STORAGE_EDITOR_ROLE, "members": [editor1, editor2]},
            {"role": STORAGE_VIEWER_ROLE, "members": [viewer1, viewer2]},
        ]
        policy = Policy()
        for binding in bindings:
            policy[binding["role"]] = binding["members"]

        api_response = {"etag": etag, "version": version, "bindings": bindings}
        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)

        returned = bucket.set_iam_policy(policy)

        self.assertEqual(returned.etag, etag)
        self.assertEqual(returned.version, version)
        self.assertEqual(dict(returned), dict(policy))

        expected_path = f"{bucket.path}/iam"
        expected_data = {
            "resourceId": bucket.path,
            "bindings": mock.ANY,
        }
        expected_query_params = {}
        client._put_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_ETAG_IN_JSON,
            _target_object=None,
        )

        sent_bindings = client._put_resource.call_args.args[1]["bindings"]
        key = operator.itemgetter("role")
        for found, expected in zip(
            sorted(sent_bindings, key=key), sorted(bindings, key=key)
        ):
            self.assertEqual(found["role"], expected["role"])
            self.assertEqual(sorted(found["members"]), sorted(expected["members"]))

    def test_set_iam_policy_w_user_project_w_expl_client_w_timeout_retry(self):
        import operator

        from google.api_core.iam import Policy

        from google.cloud.storage.iam import (
            STORAGE_EDITOR_ROLE,
            STORAGE_OWNER_ROLE,
            STORAGE_VIEWER_ROLE,
        )

        name = "name"
        user_project = "user-project-123"
        etag = "DEADBEEF"
        version = 1
        owner1 = "user:phred@example.com"
        owner2 = "group:cloud-logs@google.com"
        editor1 = "domain:google.com"
        editor2 = "user:phred@example.com"
        viewer1 = "serviceAccount:1234-abcdef@service.example.com"
        viewer2 = "user:phred@example.com"
        bindings = [
            {"role": STORAGE_OWNER_ROLE, "members": [owner1, owner2]},
            {"role": STORAGE_EDITOR_ROLE, "members": [editor1, editor2]},
            {"role": STORAGE_VIEWER_ROLE, "members": [viewer1, viewer2]},
        ]
        policy = Policy()
        for binding in bindings:
            policy[binding["role"]] = binding["members"]

        api_response = {"etag": etag, "version": version, "bindings": bindings}
        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        bucket = self._make_one(client=None, name=name, user_project=user_project)
        timeout = 42
        retry = mock.Mock(spec=[])

        returned = bucket.set_iam_policy(
            policy, client=client, timeout=timeout, retry=retry
        )

        self.assertEqual(returned.etag, etag)
        self.assertEqual(returned.version, version)
        self.assertEqual(dict(returned), dict(policy))

        expected_path = f"{bucket.path}/iam"
        expected_data = {
            "resourceId": bucket.path,
            "bindings": mock.ANY,
        }
        expected_query_params = {"userProject": user_project}
        client._put_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
            _target_object=None,
        )

        sent_bindings = client._put_resource.call_args.args[1]["bindings"]
        key = operator.itemgetter("role")
        for found, expected in zip(
            sorted(sent_bindings, key=key), sorted(bindings, key=key)
        ):
            self.assertEqual(found["role"], expected["role"])
            self.assertEqual(sorted(found["members"]), sorted(expected["members"]))

    def test_test_iam_permissions_defaults(self):
        from google.cloud.storage.iam import (
            STORAGE_BUCKETS_GET,
            STORAGE_BUCKETS_UPDATE,
            STORAGE_OBJECTS_LIST,
        )

        name = "name"
        permissions = [
            STORAGE_OBJECTS_LIST,
            STORAGE_BUCKETS_GET,
            STORAGE_BUCKETS_UPDATE,
        ]
        expected = permissions[1:]
        api_response = {"permissions": expected}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)

        found = bucket.test_iam_permissions(permissions)

        self.assertEqual(found, expected)

        expected_path = f"/b/{name}/iam/testPermissions"
        expected_query_params = {}
        expected_query_params = {"permissions": permissions}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_test_iam_permissions_w_user_project_w_timeout_w_retry(self):
        from google.cloud.storage.iam import (
            STORAGE_BUCKETS_GET,
            STORAGE_BUCKETS_UPDATE,
            STORAGE_OBJECTS_LIST,
        )

        name = "name"
        user_project = "user-project-123"
        timeout = 42
        retry = mock.Mock(spec=[])
        permissions = [
            STORAGE_OBJECTS_LIST,
            STORAGE_BUCKETS_GET,
            STORAGE_BUCKETS_UPDATE,
        ]
        expected = permissions[1:]
        api_response = {"permissions": expected}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name, user_project=user_project)

        found = bucket.test_iam_permissions(permissions, timeout=timeout, retry=retry)

        self.assertEqual(found, expected)

        expected_path = f"/b/{name}/iam/testPermissions"
        expected_query_params = {
            "permissions": permissions,
            "userProject": user_project,
        }
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
            _target_object=None,
        )

    def test_make_public_defaults(self):
        from google.cloud.storage.acl import _ACLEntity

        name = "name"
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]
        api_response = {"acl": permissive, "defaultObjectAcl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        bucket.make_public()

        self.assertEqual(list(bucket.acl), permissive)
        self.assertEqual(list(bucket.default_object_acl), [])

        expected_path = bucket.path
        expected_data = {"acl": permissive}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_make_public_w_preconditions(self):
        from google.cloud.storage.acl import _ACLEntity

        name = "name"
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]
        api_response = {"acl": permissive, "defaultObjectAcl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        bucket.make_public(if_metageneration_match=2, if_metageneration_not_match=1)

        self.assertEqual(list(bucket.acl), permissive)
        self.assertEqual(list(bucket.default_object_acl), [])

        expected_path = bucket.path
        expected_data = {"acl": permissive}
        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def _make_public_w_future_helper(self, default_object_acl_loaded=True):
        from google.cloud.storage.acl import _ACLEntity

        name = "name"
        get_api_response = {"items": []}
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]
        acl_patched_response = {"acl": permissive, "defaultObjectAcl": []}
        dac_patched_response = {"acl": permissive, "defaultObjectAcl": permissive}
        client = mock.Mock(spec=["_get_resource", "_patch_resource"])
        client._get_resource.return_value = get_api_response
        client._patch_resource.side_effect = [
            acl_patched_response,
            dac_patched_response,
        ]

        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = default_object_acl_loaded

        bucket.make_public(future=True)

        self.assertEqual(list(bucket.acl), permissive)
        self.assertEqual(list(bucket.default_object_acl), permissive)

        self.assertEqual(len(client._patch_resource.call_args_list), 2)
        expected_acl_data = {"acl": permissive}
        expected_dac_data = {"defaultObjectAcl": permissive}
        expected_kw = {
            "query_params": {"projection": "full"},
            "timeout": self._get_default_timeout(),
            "retry": DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        }
        client._patch_resource.assert_has_calls(
            [
                ((bucket.path, expected_acl_data), expected_kw),
                ((bucket.path, expected_dac_data), expected_kw),
            ]
        )

        if not default_object_acl_loaded:
            expected_path = f"/b/{name}/defaultObjectAcl"
            expected_query_params = {}
            client._get_resource.assert_called_once_with(
                expected_path,
                query_params=expected_query_params,
                timeout=self._get_default_timeout(),
                retry=DEFAULT_RETRY,
            )
        else:
            client._get_resource.assert_not_called()

    def test_make_public_w_future(self):
        self._make_public_w_future_helper(default_object_acl_loaded=True)

    def test_make_public_w_future_reload_default(self):
        self._make_public_w_future_helper(default_object_acl_loaded=False)

    def test_make_public_recursive(self):
        from google.cloud.storage.acl import _ACLEntity

        _saved = []

        class _Blob(object):
            _granted = False

            def __init__(self, bucket, name):
                self._bucket = bucket
                self._name = name

            @property
            def acl(self):
                return self

            # Faux ACL methods
            def all(self):
                return self

            def grant_read(self):
                self._granted = True

            def save(self, client=None, timeout=None):
                _saved.append(
                    (self._bucket, self._name, self._granted, client, timeout)
                )

        name = "name"
        blob_name = "blob-name"
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]

        patch_acl_response = {"acl": permissive, "defaultObjectAcl": []}
        client = mock.Mock(spec=["list_blobs", "_patch_resource"])
        client._patch_resource.return_value = patch_acl_response

        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        list_blobs_response = iter([_Blob(bucket, blob_name)])
        client.list_blobs.return_value = list_blobs_response

        timeout = 42

        bucket.make_public(recursive=True, timeout=timeout)

        self.assertEqual(list(bucket.acl), permissive)
        self.assertEqual(list(bucket.default_object_acl), [])
        self.assertEqual(_saved, [(bucket, blob_name, True, None, timeout)])

        expected_patch_data = {"acl": permissive}
        expected_patch_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            bucket.path,
            expected_patch_data,
            query_params=expected_patch_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )
        client.list_blobs.assert_called_once()

    def test_make_public_recursive_too_many(self):
        from google.cloud.storage.acl import _ACLEntity

        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]

        name = "name"
        blob1 = mock.Mock(spec=[])
        blob2 = mock.Mock(spec=[])
        patch_acl_response = {"acl": permissive, "defaultObjectAcl": []}
        list_blobs_response = iter([blob1, blob2])
        client = mock.Mock(spec=["list_blobs", "_patch_resource"])
        client.list_blobs.return_value = list_blobs_response
        client._patch_resource.return_value = patch_acl_response
        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        # Make the Bucket refuse to make_public with 2 objects.
        bucket._MAX_OBJECTS_FOR_ITERATION = 1

        with self.assertRaises(ValueError):
            bucket.make_public(recursive=True)

        expected_path = bucket.path
        expected_data = {"acl": permissive}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

        client.list_blobs.assert_called_once()

    def test_make_private_defaults(self):
        name = "name"
        no_permissions = []
        api_response = {"acl": no_permissions, "defaultObjectAcl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        bucket.make_private()

        self.assertEqual(list(bucket.acl), no_permissions)
        self.assertEqual(list(bucket.default_object_acl), [])

        expected_path = bucket.path
        expected_data = {"acl": no_permissions}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def test_make_private_w_preconditions(self):
        name = "name"
        no_permissions = []
        api_response = {"acl": no_permissions, "defaultObjectAcl": []}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        bucket.make_private(if_metageneration_match=2, if_metageneration_not_match=1)

        self.assertEqual(list(bucket.acl), no_permissions)
        self.assertEqual(list(bucket.default_object_acl), [])

        expected_path = bucket.path
        expected_data = {"acl": no_permissions}
        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

    def _make_private_w_future_helper(self, default_object_acl_loaded=True):
        name = "name"
        no_permissions = []
        get_api_response = {"items": []}
        acl_patched_response = {"acl": no_permissions, "defaultObjectAcl": []}
        dac_patched_response = {
            "acl": no_permissions,
            "defaultObjectAcl": no_permissions,
        }
        client = mock.Mock(spec=["_get_resource", "_patch_resource"])
        client._get_resource.return_value = get_api_response
        client._patch_resource.side_effect = [
            acl_patched_response,
            dac_patched_response,
        ]

        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = default_object_acl_loaded

        bucket.make_private(future=True)

        self.assertEqual(list(bucket.acl), no_permissions)
        self.assertEqual(list(bucket.default_object_acl), no_permissions)

        self.assertEqual(len(client._patch_resource.call_args_list), 2)
        expected_acl_data = {"acl": no_permissions}
        expected_dac_data = {"defaultObjectAcl": no_permissions}
        expected_kw = {
            "query_params": {"projection": "full"},
            "timeout": self._get_default_timeout(),
            "retry": DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        }
        client._patch_resource.assert_has_calls(
            [
                ((bucket.path, expected_acl_data), expected_kw),
                ((bucket.path, expected_dac_data), expected_kw),
            ]
        )

        if not default_object_acl_loaded:
            expected_path = f"/b/{name}/defaultObjectAcl"
            expected_query_params = {}
            client._get_resource.assert_called_once_with(
                expected_path,
                query_params=expected_query_params,
                timeout=self._get_default_timeout(),
                retry=DEFAULT_RETRY,
            )
        else:
            client._get_resource.assert_not_called()

    def test_make_private_w_future(self):
        self._make_private_w_future_helper(default_object_acl_loaded=True)

    def test_make_private_w_future_reload_default(self):
        self._make_private_w_future_helper(default_object_acl_loaded=False)

    def test_make_private_recursive(self):
        _saved = []

        class _Blob(object):
            _granted = True

            def __init__(self, bucket, name):
                self._bucket = bucket
                self._name = name

            @property
            def acl(self):
                return self

            # Faux ACL methods
            def all(self):
                return self

            def revoke_read(self):
                self._granted = False

            def save(self, client=None, timeout=None):
                _saved.append(
                    (self._bucket, self._name, self._granted, client, timeout)
                )

        name = "name"
        blob_name = "blob-name"
        no_permissions = []

        patch_acl_response = {"acl": no_permissions, "defaultObjectAcl": []}
        client = mock.Mock(spec=["list_blobs", "_patch_resource"])
        client._patch_resource.return_value = patch_acl_response

        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        list_blobs_response = iter([_Blob(bucket, blob_name)])
        client.list_blobs.return_value = list_blobs_response

        timeout = 42

        bucket.make_private(recursive=True, timeout=42)

        self.assertEqual(list(bucket.acl), no_permissions)
        self.assertEqual(list(bucket.default_object_acl), [])
        self.assertEqual(_saved, [(bucket, blob_name, False, None, timeout)])

        expected_patch_data = {"acl": no_permissions}
        expected_patch_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            bucket.path,
            expected_patch_data,
            query_params=expected_patch_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

        client.list_blobs.assert_called_once()

    def test_make_private_recursive_too_many(self):
        no_permissions = []

        name = "name"
        blob1 = mock.Mock(spec=[])
        blob2 = mock.Mock(spec=[])
        patch_acl_response = {"acl": no_permissions, "defaultObjectAcl": []}
        list_blobs_response = iter([blob1, blob2])
        client = mock.Mock(spec=["list_blobs", "_patch_resource"])
        client.list_blobs.return_value = list_blobs_response
        client._patch_resource.return_value = patch_acl_response
        bucket = self._make_one(client=client, name=name)
        bucket.acl.loaded = True
        bucket.default_object_acl.loaded = True

        # Make the Bucket refuse to make_private with 2 objects.
        bucket._MAX_OBJECTS_FOR_ITERATION = 1

        with self.assertRaises(ValueError):
            bucket.make_private(recursive=True)

        expected_path = bucket.path
        expected_data = {"acl": no_permissions}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED,
        )

        client.list_blobs.assert_called_once()

    def _generate_upload_policy_helper(self, **kwargs):
        import base64
        import json

        credentials = _create_signing_credentials()
        credentials.signer_email = mock.sentinel.signer_email
        credentials.sign_bytes.return_value = b"DEADBEEF"
        client = self._make_client(_credentials=credentials)
        name = "name"
        bucket = self._make_one(client=client, name=name)

        conditions = [["starts-with", "$key", ""]]

        policy_fields = bucket.generate_upload_policy(conditions, **kwargs)

        self.assertEqual(policy_fields["bucket"], bucket.name)
        self.assertEqual(policy_fields["GoogleAccessId"], mock.sentinel.signer_email)
        self.assertEqual(
            policy_fields["signature"], base64.b64encode(b"DEADBEEF").decode("utf-8")
        )

        policy = json.loads(base64.b64decode(policy_fields["policy"]).decode("utf-8"))

        policy_conditions = policy["conditions"]
        expected_conditions = [{"bucket": bucket.name}] + conditions
        for expected_condition in expected_conditions:
            for condition in policy_conditions:
                if condition == expected_condition:
                    break
            else:  # pragma: NO COVER
                self.fail(
                    f"Condition {expected_condition} not found in {policy_conditions}"  # noqa: E713
                )

        return policy_fields, policy

    @mock.patch(
        "google.cloud.storage.bucket._NOW", return_value=datetime.datetime(1990, 1, 1)
    )
    def test_generate_upload_policy(self, now):
        from google.cloud._helpers import _datetime_to_rfc3339

        _, policy = self._generate_upload_policy_helper()

        self.assertEqual(
            policy["expiration"],
            _datetime_to_rfc3339(now() + datetime.timedelta(hours=1)),
        )

    def test_generate_upload_policy_args(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        expiration = datetime.datetime(1990, 5, 29)

        _, policy = self._generate_upload_policy_helper(expiration=expiration)

        self.assertEqual(policy["expiration"], _datetime_to_rfc3339(expiration))

    def test_generate_upload_policy_bad_credentials(self):
        credentials = object()
        client = self._make_client(_credentials=credentials)
        name = "name"
        bucket = self._make_one(client=client, name=name)

        with self.assertRaises(AttributeError):
            bucket.generate_upload_policy([])

    def test_lock_retention_policy_no_policy_set(self):
        client = mock.Mock(spec=["_post_resource"])
        name = "name"
        bucket = self._make_one(client=client, name=name)
        bucket._properties["metageneration"] = 1234

        with self.assertRaises(ValueError):
            bucket.lock_retention_policy()

        client._post_resource.assert_not_called()

    def test_lock_retention_policy_no_metageneration(self):
        client = mock.Mock(spec=["_post_resource"])
        name = "name"
        bucket = self._make_one(client=client, name=name)
        bucket._properties["retentionPolicy"] = {
            "effectiveTime": "2018-03-01T16:46:27.123456Z",
            "retentionPeriod": 86400 * 100,  # 100 days
        }

        with self.assertRaises(ValueError):
            bucket.lock_retention_policy()

        client._post_resource.assert_not_called()

    def test_lock_retention_policy_already_locked(self):
        client = mock.Mock(spec=["_post_resource"])
        name = "name"
        bucket = self._make_one(client=client, name=name)
        bucket._properties["metageneration"] = 1234
        bucket._properties["retentionPolicy"] = {
            "effectiveTime": "2018-03-01T16:46:27.123456Z",
            "isLocked": True,
            "retentionPeriod": 86400 * 100,  # 100 days
        }

        with self.assertRaises(ValueError):
            bucket.lock_retention_policy()

        client._post_resource.assert_not_called()

    def test_lock_retention_policy_ok_w_timeout_w_retry(self):
        name = "name"
        effective_time = "2018-03-01T16:46:27.123456Z"
        one_hundred_days = 86400 * 100  # seconds in 100 days
        metageneration = 1234
        api_response = {
            "name": name,
            "metageneration": metageneration + 1,
            "retentionPolicy": {
                "effectiveTime": effective_time,
                "isLocked": True,
                "retentionPeriod": one_hundred_days,
            },
        }
        metageneration = 1234
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name)
        bucket._properties["metageneration"] = metageneration
        bucket._properties["retentionPolicy"] = {
            "effectiveTime": effective_time,
            "retentionPeriod": one_hundred_days,
        }
        timeout = 42
        retry = mock.Mock(spec=[])

        bucket.lock_retention_policy(timeout=timeout, retry=retry)

        expected_path = f"/b/{name}/lockRetentionPolicy"
        expected_data = None
        expected_query_params = {"ifMetagenerationMatch": metageneration}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=retry,
            _target_object=bucket,
        )

    def test_lock_retention_policy_w_user_project(self):
        name = "name"
        user_project = "user-project-123"
        metageneration = 1234
        effective_time = "2018-03-01T16:46:27.123456Z"
        one_hundred_days = 86400 * 100  # seconds in 100 days
        api_response = {
            "name": name,
            "metageneration": metageneration + 1,
            "retentionPolicy": {
                "effectiveTime": effective_time,
                "isLocked": True,
                "retentionPeriod": one_hundred_days,
            },
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = self._make_one(client=client, name=name, user_project=user_project)
        bucket._properties["metageneration"] = 1234
        bucket._properties["retentionPolicy"] = {
            "effectiveTime": effective_time,
            "retentionPeriod": one_hundred_days,
        }

        bucket.lock_retention_policy()

        expected_path = f"/b/{name}/lockRetentionPolicy"
        expected_data = None
        expected_query_params = {
            "ifMetagenerationMatch": metageneration,
            "userProject": user_project,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=bucket,
        )

    def test_restore_blob_w_defaults(self):
        bucket_name = "restore_bucket"
        blob_name = "restore_blob"
        generation = 123456
        api_response = {"name": blob_name, "generation": generation}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = self._make_one(client=client, name=bucket_name)

        restored_blob = bucket.restore_blob(blob_name)

        self.assertIs(restored_blob.bucket, bucket)
        self.assertEqual(restored_blob.name, blob_name)
        expected_path = f"/b/{bucket_name}/o/{blob_name}/restore"
        expected_data = None
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
        )

    def test_restore_blob_w_explicit(self):
        user_project = "user-project-123"
        bucket_name = "restore_bucket"
        blob_name = "restore_blob"
        generation = 123456
        api_response = {"name": blob_name, "generation": generation}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = self._make_one(
            client=client, name=bucket_name, user_project=user_project
        )
        if_generation_match = 123456
        if_generation_not_match = 654321
        if_metageneration_match = 1
        if_metageneration_not_match = 2
        projection = "noAcl"

        restored_blob = bucket.restore_blob(
            blob_name,
            client=client,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            projection=projection,
        )

        self.assertEqual(restored_blob.name, blob_name)
        self.assertEqual(restored_blob.bucket, bucket)
        expected_path = f"/b/{bucket_name}/o/{blob_name}/restore"
        expected_data = None
        expected_query_params = {
            "userProject": user_project,
            "projection": projection,
            "ifGenerationMatch": if_generation_match,
            "ifGenerationNotMatch": if_generation_not_match,
            "ifMetagenerationMatch": if_metageneration_match,
            "ifMetagenerationNotMatch": if_metageneration_not_match,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
        )

    def test_restore_blob_explicit_copy_source_acl(self):
        bucket_name = "restore_bucket"
        blob_name = "restore"
        generation = 123456
        api_response = {"name": blob_name, "generation": generation}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = self._make_one(client=client, name=bucket_name)
        copy_source_acl = False

        restored_blob = bucket.restore_blob(
            blob_name,
            copy_source_acl=copy_source_acl,
            generation=generation,
        )

        self.assertEqual(restored_blob.name, blob_name)
        self.assertEqual(restored_blob.bucket, bucket)
        expected_path = f"/b/{bucket_name}/o/{blob_name}/restore"
        expected_data = None
        expected_query_params = {
            "copySourceAcl": False,
            "generation": generation,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
        )

    def test_generate_signed_url_w_invalid_version(self):
        expiration = "2014-10-16T20:34:37.000Z"
        client = self._make_client()
        bucket = self._make_one(name="bucket_name", client=client)
        with self.assertRaises(ValueError):
            bucket.generate_signed_url(expiration, version="nonesuch")

    def _generate_signed_url_helper(
        self,
        version=None,
        bucket_name="bucket-name",
        api_access_endpoint=None,
        method="GET",
        content_md5=None,
        content_type=None,
        response_type=None,
        response_disposition=None,
        generation=None,
        headers=None,
        query_parameters=None,
        credentials=None,
        expiration=None,
        virtual_hosted_style=False,
        bucket_bound_hostname=None,
        scheme="http",
    ):
        from urllib import parse

        from google.cloud.storage._helpers import (
            _bucket_bound_hostname_url,
            _get_default_storage_base_url,
        )

        delta = datetime.timedelta(hours=1)

        if expiration is None:
            expiration = _NOW(_UTC) + delta

        client = self._make_client(_credentials=credentials)
        bucket = self._make_one(name=bucket_name, client=client)

        if version is None:
            effective_version = "v2"
        else:
            effective_version = version

        to_patch = "google.cloud.storage.bucket.generate_signed_url_{}".format(
            effective_version
        )

        with mock.patch(to_patch) as signer:
            signed_uri = bucket.generate_signed_url(
                expiration=expiration,
                api_access_endpoint=api_access_endpoint,
                method=method,
                credentials=credentials,
                headers=headers,
                query_parameters=query_parameters,
                version=version,
                virtual_hosted_style=virtual_hosted_style,
                bucket_bound_hostname=bucket_bound_hostname,
            )

        self.assertEqual(signed_uri, signer.return_value)

        if credentials is None:
            expected_creds = client._credentials
        else:
            expected_creds = credentials

        if virtual_hosted_style:
            expected_api_access_endpoint = "https://{}.storage.googleapis.com".format(
                bucket_name
            )
        elif bucket_bound_hostname:
            expected_api_access_endpoint = _bucket_bound_hostname_url(
                bucket_bound_hostname, scheme
            )
        else:
            expected_api_access_endpoint = (
                api_access_endpoint or _get_default_storage_base_url()
            )
            expected_resource = f"/{parse.quote(bucket_name)}"

        if virtual_hosted_style or bucket_bound_hostname:
            expected_resource = "/"

        expected_kwargs = {
            "resource": expected_resource,
            "expiration": expiration,
            "api_access_endpoint": expected_api_access_endpoint,
            "method": method.upper(),
            "headers": headers,
            "query_parameters": query_parameters,
        }
        signer.assert_called_once_with(expected_creds, **expected_kwargs)

    def test_get_bucket_from_uri_w_valid_uri(self):
        from google.cloud.storage.bucket import Bucket

        client = self._make_client()
        BUCKET_NAME = "BUCKET_NAME"
        uri = "gs://" + BUCKET_NAME

        bucket = Bucket.from_uri(uri, client)

        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, client)
        self.assertEqual(bucket.name, BUCKET_NAME)

    def test_get_bucket_from_uri_w_invalid_uri(self):
        from google.cloud.storage.bucket import Bucket

        client = self._make_client()

        with pytest.raises(ValueError, match="URI scheme must be gs"):
            Bucket.from_uri("http://bucket_name", client)

    def test_get_bucket_from_uri_w_domain_name_bucket(self):
        from google.cloud.storage.bucket import Bucket

        client = self._make_client()
        BUCKET_NAME = "buckets.example.com"
        uri = "gs://" + BUCKET_NAME

        bucket = Bucket.from_uri(uri, client)

        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, client)
        self.assertEqual(bucket.name, BUCKET_NAME)

    @mock.patch("warnings.warn")
    def test_get_bucket_from_string(self, mock_warn):
        from google.cloud.storage.bucket import _FROM_STRING_MESSAGE, Bucket

        client = self._make_client()
        BUCKET_NAME = "BUCKET_NAME"
        uri = "gs://" + BUCKET_NAME

        bucket = Bucket.from_string(uri, client)

        self.assertIsInstance(bucket, Bucket)
        self.assertIs(bucket.client, client)
        self.assertEqual(bucket.name, BUCKET_NAME)
        mock_warn.assert_any_call(
            _FROM_STRING_MESSAGE,
            PendingDeprecationWarning,
            stacklevel=2,
        )

    def test_generate_signed_url_no_version_passed_warning(self):
        self._generate_signed_url_helper()

    def _generate_signed_url_v2_helper(self, **kw):
        version = "v2"
        self._generate_signed_url_helper(version, **kw)

    def test_generate_signed_url_v2_w_defaults(self):
        self._generate_signed_url_v2_helper()

    def test_generate_signed_url_v2_w_expiration(self):
        expiration = _NOW(_UTC)
        self._generate_signed_url_v2_helper(expiration=expiration)

    def test_generate_signed_url_v2_w_endpoint(self):
        self._generate_signed_url_v2_helper(
            api_access_endpoint="https://api.example.com/v1"
        )

    def test_generate_signed_url_v2_w_method(self):
        self._generate_signed_url_v2_helper(method="POST")

    def test_generate_signed_url_v2_w_lowercase_method(self):
        self._generate_signed_url_v2_helper(method="get")

    def test_generate_signed_url_v2_w_content_md5(self):
        self._generate_signed_url_v2_helper(content_md5="FACEDACE")

    def test_generate_signed_url_v2_w_content_type(self):
        self._generate_signed_url_v2_helper(content_type="text.html")

    def test_generate_signed_url_v2_w_response_type(self):
        self._generate_signed_url_v2_helper(response_type="text.html")

    def test_generate_signed_url_v2_w_response_disposition(self):
        self._generate_signed_url_v2_helper(response_disposition="inline")

    def test_generate_signed_url_v2_w_generation(self):
        self._generate_signed_url_v2_helper(generation=12345)

    def test_generate_signed_url_v2_w_headers(self):
        self._generate_signed_url_v2_helper(headers={"x-goog-foo": "bar"})

    def test_generate_signed_url_v2_w_credentials(self):
        credentials = object()
        self._generate_signed_url_v2_helper(credentials=credentials)

    def _generate_signed_url_v4_helper(self, **kw):
        version = "v4"
        self._generate_signed_url_helper(version, **kw)

    def test_generate_signed_url_v4_w_defaults(self):
        self._generate_signed_url_v2_helper()

    def test_generate_signed_url_v4_w_endpoint(self):
        self._generate_signed_url_v4_helper(
            api_access_endpoint="https://api.example.com/v1"
        )

    def test_generate_signed_url_v4_w_method(self):
        self._generate_signed_url_v4_helper(method="POST")

    def test_generate_signed_url_v4_w_lowercase_method(self):
        self._generate_signed_url_v4_helper(method="get")

    def test_generate_signed_url_v4_w_content_md5(self):
        self._generate_signed_url_v4_helper(content_md5="FACEDACE")

    def test_generate_signed_url_v4_w_content_type(self):
        self._generate_signed_url_v4_helper(content_type="text.html")

    def test_generate_signed_url_v4_w_response_type(self):
        self._generate_signed_url_v4_helper(response_type="text.html")

    def test_generate_signed_url_v4_w_response_disposition(self):
        self._generate_signed_url_v4_helper(response_disposition="inline")

    def test_generate_signed_url_v4_w_generation(self):
        self._generate_signed_url_v4_helper(generation=12345)

    def test_generate_signed_url_v4_w_headers(self):
        self._generate_signed_url_v4_helper(headers={"x-goog-foo": "bar"})

    def test_generate_signed_url_v4_w_credentials(self):
        credentials = object()
        self._generate_signed_url_v4_helper(credentials=credentials)

    def test_generate_signed_url_v4_w_virtual_hostname(self):
        self._generate_signed_url_v4_helper(virtual_hosted_style=True)

    def test_generate_signed_url_v4_w_bucket_bound_hostname_w_scheme(self):
        self._generate_signed_url_v4_helper(
            bucket_bound_hostname="http://cdn.example.com"
        )

    def test_generate_signed_url_v4_w_bucket_bound_hostname_w_bare_hostname(self):
        self._generate_signed_url_v4_helper(bucket_bound_hostname="cdn.example.com")

    def test_generate_signed_url_v4_w_incompatible_params(self):
        with self.assertRaises(ValueError):
            self._generate_signed_url_v4_helper(
                api_access_endpoint="example.com",
                bucket_bound_hostname="cdn.example.com",
            )
        with self.assertRaises(ValueError):
            self._generate_signed_url_v4_helper(
                virtual_hosted_style=True, bucket_bound_hostname="cdn.example.com"
            )

    def test_ip_filter_getter_unset(self):
        """Test that ip_filter is None when not set."""
        bucket = self._make_one()
        self.assertIsNone(bucket.ip_filter)

    def test_ip_filter_getter_w_value(self):
        """Test getting an existing ip_filter configuration."""
        from google.cloud.storage.ip_filter import IPFilter

        ipf_property = {"mode": "Enabled"}
        properties = {"ipFilter": ipf_property}
        bucket = self._make_one(properties=properties)

        ip_filter = bucket.ip_filter
        self.assertIsInstance(ip_filter, IPFilter)
        self.assertEqual(ip_filter.mode, "Enabled")

    def test_ip_filter_setter(self):
        """Test setting the ip_filter with a helper class."""
        from google.cloud.storage.bucket import _IP_FILTER_PROPERTY
        from google.cloud.storage.ip_filter import IPFilter

        bucket = self._make_one()
        ip_filter = IPFilter()
        ip_filter.mode = "Enabled"

        bucket.ip_filter = ip_filter

        self.assertIn(_IP_FILTER_PROPERTY, bucket._changes)
        self.assertEqual(
            bucket._properties[_IP_FILTER_PROPERTY],
            {
                "mode": "Enabled",
                "vpcNetworkSources": [],
                "allowAllServiceAgentAccess": None,
            },
        )

    def test_ip_filter_setter_w_none(self):
        """Test clearing the ip_filter by setting it to None."""
        from google.cloud.storage.bucket import _IP_FILTER_PROPERTY

        bucket = self._make_one(properties={"ipFilter": {"mode": "Enabled"}})
        bucket.ip_filter = None

        self.assertIn(_IP_FILTER_PROPERTY, bucket._changes)
        self.assertIsNone(bucket._properties.get(_IP_FILTER_PROPERTY))


class Test__item_to_notification(unittest.TestCase):
    def _call_fut(self, iterator, item):
        from google.cloud.storage.bucket import _item_to_notification

        return _item_to_notification(iterator, item)

    def test_it(self):
        from google.cloud.storage.notification import (
            _TOPIC_REF_FMT,
            NONE_PAYLOAD_FORMAT,
            BucketNotification,
        )

        iterator = mock.Mock(spec=["bucket"])
        project = "my-project-123"
        topic = "topic-1"
        item = {
            "topic": _TOPIC_REF_FMT.format(project, topic),
            "id": "1",
            "etag": "DEADBEEF",
            "selfLink": "https://example.com/notification/1",
            "payload_format": NONE_PAYLOAD_FORMAT,
        }

        notification = self._call_fut(iterator, item)

        self.assertIsInstance(notification, BucketNotification)
        self.assertIs(notification._bucket, iterator.bucket)
        self.assertEqual(notification._topic_name, topic)
        self.assertEqual(notification._topic_project, project)
        self.assertEqual(notification._properties, item)


class Test_EncryptionEnforcementConfig(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import EncryptionEnforcementConfig

        return EncryptionEnforcementConfig

    def _make_one(self, **kw):
        return self._get_target_class()(**kw)

    def test_ctor(self):
        from google.cloud.storage.constants import ENFORCEMENT_MODE_FULLY_RESTRICTED

        config = self._make_one(restriction_mode=ENFORCEMENT_MODE_FULLY_RESTRICTED)

        self.assertEqual(config.restriction_mode, ENFORCEMENT_MODE_FULLY_RESTRICTED)
        self.assertIsNone(config.effective_time)

    def test_from_api_repr(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        from google.cloud.storage.constants import ENFORCEMENT_MODE_NOT_RESTRICTED

        now = _NOW(_UTC)
        resource = {
            "restrictionMode": ENFORCEMENT_MODE_NOT_RESTRICTED,
            "effectiveTime": _datetime_to_rfc3339(now),
        }
        klass = self._get_target_class()
        config = klass.from_api_repr(resource)
        self.assertEqual(config.restriction_mode, ENFORCEMENT_MODE_NOT_RESTRICTED)
        self.assertEqual(config.effective_time, now)

    def test_restriction_mode_setter(self):
        config = self._make_one()
        self.assertIsNone(config.restriction_mode)
        config.restriction_mode = "FULLY_RESTRICTED"
        self.assertEqual(config.restriction_mode, "FULLY_RESTRICTED")
        self.assertEqual(config["restrictionMode"], "FULLY_RESTRICTED")


class Test_BucketEncryption(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.bucket import BucketEncryption

        return BucketEncryption

    def _make_one(self, bucket, **kw):
        return self._get_target_class()(bucket, **kw)

    @staticmethod
    def _make_bucket():
        from google.cloud.storage.bucket import Bucket

        return mock.create_autospec(Bucket, instance=True)

    def test_ctor_defaults(self):
        bucket = self._make_bucket()
        encryption = self._make_one(bucket)
        self.assertIs(encryption.bucket, bucket)
        self.assertIsNone(encryption.default_kms_key_name)
        # Check that the config itself is None, not its sub-property
        self.assertIsNone(encryption.google_managed_encryption_enforcement_config)
        self.assertIsNone(encryption.customer_managed_encryption_enforcement_config)
        self.assertIsNone(encryption.customer_supplied_encryption_enforcement_config)

    def test_ctor_explicit(self):
        from google.cloud.storage.bucket import EncryptionEnforcementConfig

        bucket = self._make_bucket()
        kms_key = "key"
        google_config = EncryptionEnforcementConfig("FullyRestricted")
        encryption = self._make_one(
            bucket,
            default_kms_key_name=kms_key,
            google_managed_encryption_enforcement_config=google_config,
        )
        self.assertEqual(encryption.default_kms_key_name, kms_key)
        self.assertEqual(
            encryption.google_managed_encryption_enforcement_config.restriction_mode,
            "FullyRestricted",
        )

    def test_from_api_repr(self):
        klass = self._get_target_class()
        bucket = self._make_bucket()
        resource = {
            "defaultKmsKeyName": "key",
            "googleManagedEncryptionEnforcementConfig": {
                "restrictionMode": "FullyRestricted"
            },
        }
        encryption = klass.from_api_repr(resource, bucket)
        self.assertEqual(encryption.default_kms_key_name, "key")
        self.assertEqual(
            encryption.google_managed_encryption_enforcement_config.restriction_mode,
            "FullyRestricted",
        )

    def test_setters_trigger_patch(self):
        from google.cloud.storage.bucket import EncryptionEnforcementConfig

        bucket = self._make_bucket()
        encryption = self._make_one(bucket)

        encryption.default_kms_key_name = "new-key"
        config = EncryptionEnforcementConfig("NotRestricted")
        encryption.google_managed_encryption_enforcement_config = config
        encryption.customer_managed_encryption_enforcement_config = config
        encryption.customer_supplied_encryption_enforcement_config = config

        self.assertEqual(bucket._patch_property.call_count, 4)
        bucket._patch_property.assert_called_with("encryption", encryption)

    def test_bucket_encryption_getters_handle_none(self):
        bucket = self._make_bucket()
        encryption = self._get_target_class()(bucket)
        encryption["googleManagedEncryptionEnforcementConfig"] = None

        config = encryption.google_managed_encryption_enforcement_config
        self.assertIsNone(config)
