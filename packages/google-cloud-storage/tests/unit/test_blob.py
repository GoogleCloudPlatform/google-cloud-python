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

import base64
import datetime
import hashlib
import http.client
import io
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlencode

import mock
import pytest
from google.cloud.exceptions import NotFound

from google.cloud.storage import _helpers
from google.cloud.storage._helpers import (
    _DEFAULT_UNIVERSE_DOMAIN,
    _NOW,
    _UTC,
    _get_default_headers,
    _get_default_storage_base_url,
)
from google.cloud.storage.exceptions import DataCorruption, InvalidResponse
from google.cloud.storage.retry import (
    DEFAULT_RETRY,
    DEFAULT_RETRY_IF_ETAG_IN_JSON,
    DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
)
from tests.unit.test__helpers import GCCL_INVOCATION_TEST_CONST


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class Test_Blob(unittest.TestCase):
    @staticmethod
    def _make_one(*args, **kw):
        from google.cloud.storage.blob import Blob

        properties = kw.pop("properties", {})
        blob = Blob(*args, **kw)
        blob._properties.update(properties)
        return blob

    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    @staticmethod
    def _make_client(*args, **kw):
        from google.cloud.storage.client import Client

        kw["api_endpoint"] = kw.get("api_endpoint") or _get_default_storage_base_url()
        return mock.create_autospec(Client, instance=True, **kw)

    def test_ctor_wo_encryption_key(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {"key": "value"}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertIs(blob.bucket, bucket)
        self.assertEqual(blob.name, BLOB_NAME)
        self.assertEqual(blob._properties, properties)
        self.assertFalse(blob._acl.loaded)
        self.assertIs(blob._acl.blob, blob)
        self.assertEqual(blob._encryption_key, None)
        self.assertEqual(blob.kms_key_name, None)

    def test_ctor_with_encoded_unicode(self):
        blob_name = b"wet \xe2\x9b\xb5"
        blob = self._make_one(blob_name, bucket=None)
        unicode_name = "wet \N{SAILBOAT}"
        self.assertNotIsInstance(blob.name, bytes)
        self.assertIsInstance(blob.name, str)
        self.assertEqual(blob.name, unicode_name)

    def test_ctor_w_encryption_key(self):
        KEY = b"01234567890123456789012345678901"  # 32 bytes
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket, encryption_key=KEY)
        self.assertEqual(blob._encryption_key, KEY)
        self.assertEqual(blob.kms_key_name, None)

    def test_ctor_w_kms_key_name_and_encryption_key(self):
        KEY = b"01234567890123456789012345678901"  # 32 bytes
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        BLOB_NAME = "blob-name"
        bucket = _Bucket()

        with self.assertRaises(ValueError):
            self._make_one(
                BLOB_NAME, bucket=bucket, encryption_key=KEY, kms_key_name=KMS_RESOURCE
            )

    def test_ctor_w_kms_key_name(self):
        KMS_RESOURCE = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket, kms_key_name=KMS_RESOURCE)
        self.assertEqual(blob._encryption_key, None)
        self.assertEqual(blob.kms_key_name, KMS_RESOURCE)

    def test_ctor_with_generation(self):
        BLOB_NAME = "blob-name"
        GENERATION = 12345
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket, generation=GENERATION)
        self.assertEqual(blob.generation, GENERATION)

    def _set_properties_helper(self, kms_key_name=None):
        from google.cloud._helpers import _RFC3339_MICROS

        now = _NOW(_UTC)
        NOW = now.strftime(_RFC3339_MICROS)
        BLOB_NAME = "blob-name"
        GENERATION = 12345
        BLOB_ID = f"name/{BLOB_NAME}/{GENERATION}"
        SELF_LINK = "http://example.com/self/"
        METAGENERATION = 23456
        SIZE = 12345
        MD5_HASH = "DEADBEEF"
        MEDIA_LINK = "http://example.com/media/"
        ENTITY = "project-owner-12345"
        ENTITY_ID = "23456"
        CRC32C = "FACE0DAC"
        COMPONENT_COUNT = 2
        ETAG = "ETAG"
        resource = {
            "id": BLOB_ID,
            "selfLink": SELF_LINK,
            "generation": GENERATION,
            "metageneration": METAGENERATION,
            "contentType": "text/plain",
            "timeCreated": NOW,
            "updated": NOW,
            "timeDeleted": NOW,
            "storageClass": "NEARLINE",
            "timeStorageClassUpdated": NOW,
            "size": SIZE,
            "md5Hash": MD5_HASH,
            "mediaLink": MEDIA_LINK,
            "contentEncoding": "gzip",
            "contentDisposition": "inline",
            "contentLanguage": "en-US",
            "cacheControl": "private",
            "metadata": {"foo": "Foo"},
            "owner": {"entity": ENTITY, "entityId": ENTITY_ID},
            "crc32c": CRC32C,
            "componentCount": COMPONENT_COUNT,
            "etag": ETAG,
            "customTime": NOW,
        }

        if kms_key_name is not None:
            resource["kmsKeyName"] = kms_key_name

        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)

        blob._set_properties(resource)

        self.assertEqual(blob.id, BLOB_ID)
        self.assertEqual(blob.self_link, SELF_LINK)
        self.assertEqual(blob.generation, GENERATION)
        self.assertEqual(blob.metageneration, METAGENERATION)
        self.assertEqual(blob.content_type, "text/plain")
        self.assertEqual(blob.time_created, now)
        self.assertEqual(blob.updated, now)
        self.assertEqual(blob.time_deleted, now)
        self.assertEqual(blob.storage_class, "NEARLINE")
        self.assertEqual(blob.size, SIZE)
        self.assertEqual(blob.md5_hash, MD5_HASH)
        self.assertEqual(blob.media_link, MEDIA_LINK)
        self.assertEqual(blob.content_encoding, "gzip")
        self.assertEqual(blob.content_disposition, "inline")
        self.assertEqual(blob.content_language, "en-US")
        self.assertEqual(blob.cache_control, "private")
        self.assertEqual(blob.metadata, {"foo": "Foo"})
        self.assertEqual(blob.owner, {"entity": ENTITY, "entityId": ENTITY_ID})
        self.assertEqual(blob.crc32c, CRC32C)
        self.assertEqual(blob.component_count, COMPONENT_COUNT)
        self.assertEqual(blob.etag, ETAG)
        self.assertEqual(blob.custom_time, now)

        if kms_key_name is not None:
            self.assertEqual(blob.kms_key_name, kms_key_name)
        else:
            self.assertIsNone(blob.kms_key_name)

    def test__set_properties_wo_kms_key_name(self):
        self._set_properties_helper()

    def test__set_properties_w_kms_key_name(self):
        kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        self._set_properties_helper(kms_key_name=kms_resource)

    def test_finalized_time_property_is_none(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.finalized_time)

    def test_finalized_time_property_is_not_none(self):
        from google.cloud.storage import blob as blob_module

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)

        timestamp = "2024-07-29T12:34:56.123456Z"
        blob._properties["finalizedTime"] = timestamp

        mock_datetime = mock.Mock()
        with mock.patch.object(
            blob_module, "_rfc3339_nanos_to_datetime", return_value=mock_datetime
        ) as mocked:
            self.assertEqual(blob.finalized_time, mock_datetime)
            mocked.assert_called_once_with(timestamp)

    def test_chunk_size_ctor(self):
        from google.cloud.storage.blob import Blob

        BLOB_NAME = "blob-name"
        BUCKET = object()
        chunk_size = 10 * Blob._CHUNK_SIZE_MULTIPLE
        blob = self._make_one(BLOB_NAME, bucket=BUCKET, chunk_size=chunk_size)
        self.assertEqual(blob._chunk_size, chunk_size)

    def test_chunk_size_getter(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob.chunk_size)
        VALUE = object()
        blob._chunk_size = VALUE
        self.assertIs(blob.chunk_size, VALUE)

    def test_chunk_size_setter(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob._chunk_size)
        blob._CHUNK_SIZE_MULTIPLE = 10
        blob.chunk_size = 20
        self.assertEqual(blob._chunk_size, 20)

    def test_chunk_size_setter_bad_value(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob._chunk_size)
        blob._CHUNK_SIZE_MULTIPLE = 10
        with self.assertRaises(ValueError):
            blob.chunk_size = 11

    def test_acl_property(self):
        from google.cloud.storage.acl import ObjectACL

        fake_bucket = _Bucket()
        blob = self._make_one("name", bucket=fake_bucket)
        acl = blob.acl
        self.assertIsInstance(acl, ObjectACL)
        self.assertIs(acl, blob._acl)

    def test_encryption_key_getter(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob.encryption_key)
        VALUE = object()
        blob._encryption_key = VALUE
        self.assertIs(blob.encryption_key, VALUE)

    def test_encryption_key_setter(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob._encryption_key)
        key = b"12345678901234567890123456789012"
        blob.encryption_key = key
        self.assertEqual(blob._encryption_key, key)

    def test_kms_key_name_getter(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob.kms_key_name)
        VALUE = object()
        blob._patch_property("kmsKeyName", VALUE)
        self.assertIs(blob.kms_key_name, VALUE)

    def test_kms_key_name_setter(self):
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)
        self.assertIsNone(blob._properties.get("kmsKeyName"))
        kms_key_name = "cryptoKeys/test-key"
        blob.kms_key_name = kms_key_name
        self.assertEqual(blob._properties.get("kmsKeyName"), kms_key_name)

    def test_path_bad_bucket(self):
        fake_bucket = object()
        name = "blob-name"
        blob = self._make_one(name, bucket=fake_bucket)
        self.assertRaises(AttributeError, getattr, blob, "path")

    def test_path_no_name(self):
        bucket = _Bucket()
        blob = self._make_one("", bucket=bucket)
        self.assertRaises(ValueError, getattr, blob, "path")

    def test_path_normal(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(blob.path, f"/b/name/o/{BLOB_NAME}")

    def test_path_w_slash_in_name(self):
        BLOB_NAME = "parent/child"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(blob.path, "/b/name/o/parent%2Fchild")

    def test_path_with_non_ascii(self):
        blob_name = "Caf\xe9"
        bucket = _Bucket()
        blob = self._make_one(blob_name, bucket=bucket)
        self.assertEqual(blob.path, "/b/name/o/Caf%C3%A9")

    def test_bucket_readonly_property(self):
        blob_name = "BLOB"
        bucket = _Bucket()
        other = _Bucket()
        blob = self._make_one(blob_name, bucket=bucket)
        with self.assertRaises(AttributeError):
            blob.bucket = other

    def test_client(self):
        blob_name = "BLOB"
        bucket = _Bucket()
        blob = self._make_one(blob_name, bucket=bucket)
        self.assertIs(blob.client, bucket.client)

    def test_user_project(self):
        user_project = "user-project-123"
        blob_name = "BLOB"
        bucket = _Bucket(user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)
        self.assertEqual(blob.user_project, user_project)

    def test__encryption_headers_wo_encryption_key(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        expected = {}
        self.assertEqual(blob._encryption_headers(), expected)

    def test__encryption_headers_w_encryption_key(self):
        key = b"aa426195405adee2c8081bb9e7e74b19"
        header_key_value = "YWE0MjYxOTU0MDVhZGVlMmM4MDgxYmI5ZTdlNzRiMTk="
        header_key_hash_value = "V3Kwe46nKc3xLv96+iJ707YfZfFvlObta8TQcx2gpm0="
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket, encryption_key=key)
        expected = {
            "X-Goog-Encryption-Algorithm": "AES256",
            "X-Goog-Encryption-Key": header_key_value,
            "X-Goog-Encryption-Key-Sha256": header_key_hash_value,
        }
        self.assertEqual(blob._encryption_headers(), expected)

    def test__query_params_default(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(blob._query_params, {})

    def test__query_params_w_user_project(self):
        user_project = "user-project-123"
        BLOB_NAME = "BLOB"
        bucket = _Bucket(user_project=user_project)
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(blob._query_params, {"userProject": user_project})

    def test__query_params_w_generation(self):
        generation = 123456
        BLOB_NAME = "BLOB"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket, generation=generation)
        self.assertEqual(blob._query_params, {"generation": generation})

    def test_public_url(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(
            blob.public_url, f"https://storage.googleapis.com/name/{BLOB_NAME}"
        )

    def test_public_url_w_slash_in_name(self):
        BLOB_NAME = "parent/child"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(
            blob.public_url, "https://storage.googleapis.com/name/parent/child"
        )

    def test_public_url_w_tilde_in_name(self):
        BLOB_NAME = "foo~bar"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(blob.public_url, "https://storage.googleapis.com/name/foo~bar")

    def test_public_url_with_non_ascii(self):
        blob_name = "winter \N{SNOWMAN}"
        bucket = _Bucket()
        blob = self._make_one(blob_name, bucket=bucket)
        expected_url = "https://storage.googleapis.com/name/winter%20%E2%98%83"
        self.assertEqual(blob.public_url, expected_url)

    def test_public_url_without_client(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        bucket.client = None
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertEqual(
            blob.public_url, f"https://storage.googleapis.com/name/{BLOB_NAME}"
        )

    def test_generate_signed_url_w_invalid_version(self):
        BLOB_NAME = "blob-name"
        EXPIRATION = "2014-10-16T20:34:37.000Z"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(BLOB_NAME, bucket=bucket)

        with self.assertRaises(ValueError):
            blob.generate_signed_url(EXPIRATION, version="nonesuch")

    def _generate_signed_url_helper(
        self,
        version=None,
        blob_name="blob-name",
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
        encryption_key=None,
        access_token=None,
        service_account_email=None,
        virtual_hosted_style=False,
        bucket_bound_hostname=None,
        scheme="http",
    ):
        from urllib import parse

        from google.cloud.storage._helpers import (
            _bucket_bound_hostname_url,
            _get_default_storage_base_url,
        )
        from google.cloud.storage.blob import _get_encryption_headers

        delta = datetime.timedelta(hours=1)

        if expiration is None:
            expiration = _NOW(_UTC) + delta

        if credentials is None:
            expected_creds = _make_credentials()
            client = self._make_client(_credentials=expected_creds)
        else:
            expected_creds = credentials
            client = self._make_client(_credentials=object())

        expected_universe_domain = client.universe_domain

        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket, encryption_key=encryption_key)

        if version is None:
            effective_version = "v2"
        else:
            effective_version = version

        to_patch = f"google.cloud.storage.blob.generate_signed_url_{effective_version}"

        with mock.patch(to_patch) as signer:
            signed_uri = blob.generate_signed_url(
                expiration=expiration,
                api_access_endpoint=api_access_endpoint,
                method=method,
                credentials=credentials,
                content_md5=content_md5,
                content_type=content_type,
                response_type=response_type,
                response_disposition=response_disposition,
                generation=generation,
                headers=headers,
                query_parameters=query_parameters,
                version=version,
                access_token=access_token,
                service_account_email=service_account_email,
                virtual_hosted_style=virtual_hosted_style,
                bucket_bound_hostname=bucket_bound_hostname,
            )

        self.assertEqual(signed_uri, signer.return_value)

        encoded_name = blob_name.encode("utf-8")
        quoted_name = parse.quote(encoded_name, safe=b"/~")

        if virtual_hosted_style:
            expected_api_access_endpoint = "https://{}.storage.googleapis.com".format(
                bucket.name
            )
        elif bucket_bound_hostname:
            expected_api_access_endpoint = _bucket_bound_hostname_url(
                bucket_bound_hostname, scheme
            )
        else:
            expected_api_access_endpoint = (
                api_access_endpoint
                if api_access_endpoint
                else _get_default_storage_base_url()
            )
            expected_resource = f"/{bucket.name}/{quoted_name}"

        if virtual_hosted_style or bucket_bound_hostname:
            expected_resource = f"/{quoted_name}"

        if encryption_key is not None:
            expected_headers = headers or {}
            if effective_version == "v2":
                expected_headers["X-Goog-Encryption-Algorithm"] = "AES256"
            else:
                expected_headers.update(_get_encryption_headers(encryption_key))
        else:
            expected_headers = headers

        expected_kwargs = {
            "resource": expected_resource,
            "expiration": expiration,
            "api_access_endpoint": expected_api_access_endpoint,
            "method": method.upper(),
            "content_md5": content_md5,
            "content_type": content_type,
            "response_type": response_type,
            "response_disposition": response_disposition,
            "generation": generation,
            "headers": expected_headers,
            "query_parameters": query_parameters,
            "access_token": access_token,
            "service_account_email": service_account_email,
            "universe_domain": expected_universe_domain,
        }
        signer.assert_called_once_with(expected_creds, **expected_kwargs)

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

    def test_generate_signed_url_v2_w_non_ascii_name(self):
        BLOB_NAME = "\u0410\u043a\u043a\u043e\u0440\u0434\u044b.txt"
        self._generate_signed_url_v2_helper(blob_name=BLOB_NAME)

    def test_generate_signed_url_v2_w_slash_in_name(self):
        BLOB_NAME = "parent/child"
        self._generate_signed_url_v2_helper(blob_name=BLOB_NAME)

    def test_generate_signed_url_v2_w_tilde_in_name(self):
        BLOB_NAME = "foo~bar"
        self._generate_signed_url_v2_helper(blob_name=BLOB_NAME)

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

    def test_generate_signed_url_v2_w_csek(self):
        self._generate_signed_url_v2_helper(encryption_key=os.urandom(32))

    def test_generate_signed_url_v2_w_csek_and_headers(self):
        self._generate_signed_url_v2_helper(
            encryption_key=os.urandom(32), headers={"x-goog-foo": "bar"}
        )

    def test_generate_signed_url_v2_w_credentials(self):
        credentials = object()
        self._generate_signed_url_v2_helper(credentials=credentials)

    def _generate_signed_url_v4_helper(self, **kw):
        version = "v4"
        self._generate_signed_url_helper(version, **kw)

    def test_generate_signed_url_v4_w_defaults(self):
        self._generate_signed_url_v4_helper()

    def test_generate_signed_url_v4_w_non_ascii_name(self):
        BLOB_NAME = "\u0410\u043a\u043a\u043e\u0440\u0434\u044b.txt"
        self._generate_signed_url_v4_helper(blob_name=BLOB_NAME)

    def test_generate_signed_url_v4_w_slash_in_name(self):
        BLOB_NAME = "parent/child"
        self._generate_signed_url_v4_helper(blob_name=BLOB_NAME)

    def test_generate_signed_url_v4_w_tilde_in_name(self):
        BLOB_NAME = "foo~bar"
        self._generate_signed_url_v4_helper(blob_name=BLOB_NAME)

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

    def test_generate_signed_url_v4_w_csek(self):
        self._generate_signed_url_v4_helper(encryption_key=os.urandom(32))

    def test_generate_signed_url_v4_w_csek_and_headers(self):
        self._generate_signed_url_v4_helper(
            encryption_key=os.urandom(32), headers={"x-goog-foo": "bar"}
        )

    def test_generate_signed_url_v4_w_virtual_hostname(self):
        self._generate_signed_url_v4_helper(virtual_hosted_style=True)

    def test_generate_signed_url_v4_w_bucket_bound_hostname_w_scheme(self):
        self._generate_signed_url_v4_helper(
            bucket_bound_hostname="http://cdn.example.com"
        )

    def test_generate_signed_url_v4_w_bucket_bound_hostname_w_bare_hostname(self):
        self._generate_signed_url_v4_helper(bucket_bound_hostname="cdn.example.com")

    def test_generate_signed_url_v4_w_credentials(self):
        credentials = object()
        self._generate_signed_url_v4_helper(credentials=credentials)

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

    def test_exists_miss_w_defaults(self):
        from google.cloud.exceptions import NotFound

        blob_name = "nonesuch"
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.side_effect = NotFound("testing")
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertFalse(blob.exists())

        expected_query_params = {"fields": "name"}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            blob.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_exists_hit_w_user_project_w_timeout(self):
        blob_name = "blob-name"
        user_project = "user-project-123"
        timeout = 42
        api_response = {"name": blob_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client, user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertTrue(blob.exists(timeout=timeout))

        expected_query_params = {"fields": "name", "userProject": user_project}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            blob.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_exists_hit_w_generation_w_retry(self):
        blob_name = "blob-name"
        generation = 123456
        api_response = {"name": blob_name}
        retry = mock.Mock(spec=[])
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket, generation=generation)

        self.assertTrue(blob.exists(retry=retry))

        expected_query_params = {"fields": "name", "generation": generation}
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            blob.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=None,
        )

    def test_exists_hit_w_generation_w_soft_deleted(self):
        blob_name = "blob-name"
        generation = 123456
        api_response = {"name": blob_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket, generation=generation)

        self.assertTrue(blob.exists(retry=None, soft_deleted=True))

        expected_query_params = {
            "fields": "name",
            "generation": generation,
            "softDeleted": True,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            blob.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=None,
        )

    def test_exists_w_etag_match(self):
        blob_name = "blob-name"
        etag = "kittens"
        api_response = {"name": blob_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertTrue(
            blob.exists(
                if_etag_match=etag,
                retry=None,
            )
        )

        expected_query_params = {
            "fields": "name",
        }
        expected_headers = {
            "If-Match": etag,
        }
        client._get_resource.assert_called_once_with(
            blob.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=None,
        )

    def test_exists_w_generation_match(self):
        blob_name = "blob-name"
        generation_number = 123456
        metageneration_number = 6
        api_response = {"name": blob_name}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertTrue(
            blob.exists(
                if_generation_match=generation_number,
                if_metageneration_match=metageneration_number,
                retry=None,
            )
        )

        expected_query_params = {
            "fields": "name",
            "ifGenerationMatch": generation_number,
            "ifMetagenerationMatch": metageneration_number,
        }
        expected_headers = {}
        client._get_resource.assert_called_once_with(
            blob.path,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=None,
            _target_object=None,
        )

    def test_delete_wo_generation(self):
        BLOB_NAME = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        bucket._blobs[BLOB_NAME] = 1

        blob.delete()

        self.assertEqual(
            bucket._deleted,
            [
                (
                    BLOB_NAME,
                    None,
                    None,
                    self._get_default_timeout(),
                    None,
                    None,
                    None,
                    None,
                    DEFAULT_RETRY,
                )
            ],
        )

    def test_delete_w_generation(self):
        BLOB_NAME = "blob-name"
        GENERATION = 123456
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(BLOB_NAME, bucket=bucket, generation=GENERATION)
        bucket._blobs[BLOB_NAME] = 1

        blob.delete(timeout=42)

        self.assertEqual(
            bucket._deleted,
            [
                (
                    BLOB_NAME,
                    None,
                    GENERATION,
                    42,
                    None,
                    None,
                    None,
                    None,
                    DEFAULT_RETRY,
                )
            ],
        )

    def test_delete_w_generation_match(self):
        BLOB_NAME = "blob-name"
        GENERATION = 123456
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(BLOB_NAME, bucket=bucket, generation=GENERATION)
        bucket._blobs[BLOB_NAME] = 1

        blob.delete(timeout=42, if_generation_match=GENERATION)

        self.assertEqual(
            bucket._deleted,
            [
                (
                    BLOB_NAME,
                    None,
                    GENERATION,
                    42,
                    GENERATION,
                    None,
                    None,
                    None,
                    DEFAULT_RETRY,
                )
            ],
        )

    def test__get_transport(self):
        client = mock.Mock(spec=["_credentials", "_http"])
        client._http = mock.sentinel.transport
        blob = self._make_one("blob-name", bucket=None)

        transport = blob._get_transport(client)

        self.assertIs(transport, mock.sentinel.transport)

    def test__get_download_url_with_media_link(self):
        blob_name = "something.txt"
        bucket = _Bucket(name="IRRELEVANT")
        blob = self._make_one(blob_name, bucket=bucket)
        media_link = "http://test.invalid"
        # Set the media link on the blob
        blob._properties["mediaLink"] = media_link

        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(client)

        self.assertEqual(download_url, media_link)

    def test__get_download_url_with_generation_match(self):
        GENERATION_NUMBER = 6
        MEDIA_LINK = "http://test.invalid"

        blob = self._make_one("something.txt", bucket=_Bucket(name="IRRELEVANT"))
        # Set the media link on the blob
        blob._properties["mediaLink"] = MEDIA_LINK

        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(
            client, if_generation_match=GENERATION_NUMBER
        )
        self.assertEqual(
            download_url,
            f"{MEDIA_LINK}?ifGenerationMatch={GENERATION_NUMBER}",
        )

    def test__get_download_url_with_media_link_w_user_project(self):
        blob_name = "something.txt"
        user_project = "user-project-123"
        bucket = _Bucket(name="IRRELEVANT", user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)
        media_link = "http://test.invalid"
        # Set the media link on the blob
        blob._properties["mediaLink"] = media_link

        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(client)

        self.assertEqual(download_url, f"{media_link}?userProject={user_project}")

    def test__get_download_url_on_the_fly(self):
        blob_name = "bzzz-fly.txt"
        bucket = _Bucket(name="buhkit")
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertIsNone(blob.media_link)
        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(client)
        expected_url = (
            "https://storage.googleapis.com/download/storage/v1/b/"
            "buhkit/o/bzzz-fly.txt?alt=media"
        )
        self.assertEqual(download_url, expected_url)

    def test__get_download_url_mtls(self):
        blob_name = "bzzz-fly.txt"
        bucket = _Bucket(name="buhkit")
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertIsNone(blob.media_link)
        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._connection.get_api_base_url_for_mtls = mock.Mock(
            return_value="https://foo.mtls"
        )
        download_url = blob._get_download_url(client)
        del client._connection.get_api_base_url_for_mtls
        expected_url = (
            "https://foo.mtls/download/storage/v1/b/buhkit/o/bzzz-fly.txt?alt=media"
        )
        self.assertEqual(download_url, expected_url)

    def test__get_download_url_on_the_fly_with_generation(self):
        blob_name = "pretend.txt"
        bucket = _Bucket(name="fictional")
        blob = self._make_one(blob_name, bucket=bucket)
        generation = 1493058489532987
        # Set the media link on the blob
        blob._properties["generation"] = str(generation)

        self.assertIsNone(blob.media_link)
        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(client)
        expected_url = (
            "https://storage.googleapis.com/download/storage/v1/b/"
            "fictional/o/pretend.txt?alt=media&generation=1493058489532987"
        )
        self.assertEqual(download_url, expected_url)

    def test__get_download_url_on_the_fly_with_user_project(self):
        blob_name = "pretend.txt"
        user_project = "user-project-123"
        bucket = _Bucket(name="fictional", user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)

        self.assertIsNone(blob.media_link)
        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(client)
        expected_url = (
            "https://storage.googleapis.com/download/storage/v1/b/"
            "fictional/o/pretend.txt?alt=media&userProject={}".format(user_project)
        )
        self.assertEqual(download_url, expected_url)

    def test__get_download_url_on_the_fly_with_kms_key_name(self):
        kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        blob_name = "bzzz-fly.txt"
        bucket = _Bucket(name="buhkit")
        blob = self._make_one(blob_name, bucket=bucket, kms_key_name=kms_resource)

        self.assertIsNone(blob.media_link)
        client = mock.Mock(_connection=_Connection)
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        download_url = blob._get_download_url(client)
        expected_url = (
            "https://storage.googleapis.com/download/storage/v1/b/"
            "buhkit/o/bzzz-fly.txt?alt=media"
        )
        self.assertEqual(download_url, expected_url)

    @staticmethod
    def _mock_requests_response(status_code, headers, content=b""):
        import requests

        response = requests.Response()
        response.status_code = status_code
        response.headers.update(headers)
        response.raw = None
        response._content = content

        response.request = requests.Request("POST", "http://example.com").prepare()
        return response

    def test__extract_headers_from_download_gzipped(self):
        blob_name = "blob-name"
        client = mock.Mock(spec=["_http"])
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        response = self._mock_requests_response(
            http.client.OK,
            headers={
                "Content-Type": "application/json",
                "Content-Language": "ko-kr",
                "Cache-Control": "max-age=1337;public",
                "Content-Encoding": "gzip",
                "Etag": "kittens",
                "X-Goog-Storage-Class": "STANDARD",
                "X-Goog-Hash": "crc32c=4gcgLQ==,md5=CS9tHYTtyFntzj7B9nkkJQ==",
                "X-goog-generation": 42,
                "X-goog-metageneration": 4,
            },
            # { "x": 5 } gzipped
            content=b"\x1f\x8b\x08\x00\xcfo\x17_\x02\xff\xabVP\xaaP\xb2R0U\xa8\x05\x00\xa1\xcaQ\x93\n\x00\x00\x00",
        )
        blob._extract_headers_from_download(response)

        self.assertEqual(blob.content_type, "application/json")
        self.assertEqual(blob.content_language, "ko-kr")
        self.assertEqual(blob.content_encoding, "gzip")
        self.assertEqual(blob.cache_control, "max-age=1337;public")
        self.assertEqual(blob.storage_class, "STANDARD")
        self.assertEqual(blob.md5_hash, "CS9tHYTtyFntzj7B9nkkJQ==")
        self.assertEqual(blob.crc32c, "4gcgLQ==")
        self.assertEqual(blob.etag, "kittens")
        self.assertEqual(blob.generation, 42)
        self.assertEqual(blob.metageneration, 4)
        self.assertEqual(blob._changes, set())

    def test__extract_headers_from_download_empty(self):
        blob_name = "blob-name"
        client = mock.Mock(spec=["_http"])
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        response = self._mock_requests_response(
            http.client.OK,
            headers={
                "Content-Type": "application/octet-stream",
                "Content-Language": "en-US",
                "Cache-Control": "max-age=1337;public",
                "Content-Encoding": "gzip",
                "Etag": "kittens",
                "X-Goog-Storage-Class": "STANDARD",
                "X-Goog-Hash": "crc32c=4/c+LQ==,md5=CS9tHYTt/+ntzj7B9nkkJQ==",
                "X-goog-generation": 42,
                "X-goog-metageneration": 4,
            },
            content=b"",
        )
        blob._extract_headers_from_download(response)
        self.assertEqual(blob.content_type, "application/octet-stream")
        self.assertEqual(blob.content_language, "en-US")
        self.assertEqual(blob.md5_hash, "CS9tHYTt/+ntzj7B9nkkJQ==")
        self.assertEqual(blob.crc32c, "4/c+LQ==")
        self.assertEqual(blob.etag, "kittens")
        self.assertEqual(blob.generation, 42)
        self.assertEqual(blob.metageneration, 4)
        self.assertEqual(blob._changes, set())

    def test__extract_headers_from_download_w_hash_response_header_none(self):
        blob_name = "blob-name"
        md5_hash = "CS9tHYTtyFntzj7B9nkkJQ=="
        crc32c = "4gcgLQ=="
        client = mock.Mock(spec=["_http"])
        bucket = _Bucket(client)
        properties = {
            "md5Hash": md5_hash,
            "crc32c": crc32c,
        }
        blob = self._make_one(blob_name, bucket=bucket, properties=properties)

        response = self._mock_requests_response(
            http.client.OK,
            headers={"X-Goog-Hash": ""},
            # { "x": 5 } gzipped
            content=b"\x1f\x8b\x08\x00\xcfo\x17_\x02\xff\xabVP\xaaP\xb2R0U\xa8\x05\x00\xa1\xcaQ\x93\n\x00\x00\x00",
        )
        blob._extract_headers_from_download(response)

        self.assertEqual(blob.md5_hash, md5_hash)
        self.assertEqual(blob.crc32c, crc32c)

    def test__extract_headers_from_download_w_response_headers_not_match(self):
        blob_name = "blob-name"
        client = mock.Mock(spec=["_http"])
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        response = self._mock_requests_response(
            http.client.OK,
            headers={"X-Goog-Hash": "bogus=4gcgLQ==,"},
            # { "x": 5 } gzipped
            content=b"",
        )
        blob._extract_headers_from_download(response)

        self.assertIsNone(blob.md5_hash)
        self.assertIsNone(blob.crc32c)

    def _do_download_helper_wo_chunks(
        self, w_range, raw_download, timeout=None, **extra_kwargs
    ):
        blob_name = "blob-name"
        client = mock.Mock()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        self.assertIsNone(blob.chunk_size)

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"
        headers = extra_kwargs.pop("headers", {})

        if raw_download:
            patch = mock.patch("google.cloud.storage.blob.RawDownload")
        else:
            patch = mock.patch("google.cloud.storage.blob.Download")

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}

        extra_kwargs.update(timeout_kwarg)

        retry = extra_kwargs.get("retry", DEFAULT_RETRY)

        with patch as patched:
            if w_range:
                blob._do_download(
                    transport,
                    file_obj,
                    download_url,
                    headers,
                    start=1,
                    end=3,
                    raw_download=raw_download,
                    **extra_kwargs,
                )
            else:
                blob._do_download(
                    transport,
                    file_obj,
                    download_url,
                    headers,
                    raw_download=raw_download,
                    **extra_kwargs,
                )

        if w_range:
            patched.assert_called_once_with(
                download_url,
                stream=file_obj,
                headers=headers,
                start=1,
                end=3,
                checksum="auto",
                retry=retry,
                single_shot_download=False,
            )
        else:
            patched.assert_called_once_with(
                download_url,
                stream=file_obj,
                headers=headers,
                start=None,
                end=None,
                checksum="auto",
                retry=retry,
                single_shot_download=False,
            )

        patched.return_value.consume.assert_called_once_with(
            transport, timeout=expected_timeout
        )

    def test__do_download_wo_chunks_wo_range_wo_raw(self):
        self._do_download_helper_wo_chunks(w_range=False, raw_download=False)

    def test__do_download_wo_chunks_wo_range_wo_raw_w_headers(self):
        self._do_download_helper_wo_chunks(
            w_range=False, raw_download=False, headers={"If-Match": "kittens"}
        )

    def test__do_download_wo_chunks_wo_range_wo_raw_w_retry(self):
        self._do_download_helper_wo_chunks(
            w_range=False, raw_download=False, retry=DEFAULT_RETRY
        )

    def test__do_download_wo_chunks_wo_range_wo_raw_w_retry_w_headers(self):
        self._do_download_helper_wo_chunks(
            w_range=False,
            raw_download=False,
            retry=DEFAULT_RETRY,
            headers={"If-Match": "kittens"},
        )

    def test__do_download_wo_chunks_w_range_wo_raw(self):
        self._do_download_helper_wo_chunks(w_range=True, raw_download=False)

    def test__do_download_wo_chunks_w_range_wo_raw_w_headers(self):
        self._do_download_helper_wo_chunks(
            w_range=True, raw_download=False, headers={"If-Match": "kittens"}
        )

    def test__do_download_wo_chunks_wo_range_w_raw(self):
        self._do_download_helper_wo_chunks(w_range=False, raw_download=True)

    def test__do_download_wo_chunks_wo_range_w_raw_w_headers(self):
        self._do_download_helper_wo_chunks(
            w_range=False, raw_download=True, headers={"If-Match": "kittens"}
        )

    def test__do_download_wo_chunks_w_range_w_raw(self):
        self._do_download_helper_wo_chunks(w_range=True, raw_download=True)

    def test__do_download_wo_chunks_w_range_w_raw_w_headers(self):
        self._do_download_helper_wo_chunks(
            w_range=True, raw_download=True, headers={"If-Match": "kittens"}
        )

    @mock.patch("google.cloud.storage.blob._logger")
    def test__do_download_log_extra_bytes_singleshot(self, mock_logger):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.chunk_size = None

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"

        patch = mock.patch("google.cloud.storage.blob.Download")
        with patch as patched:
            download = patched.return_value
            download._bytes_downloaded = 10

            mock_response = mock.Mock()
            mock_response.headers = {}
            download.consume.return_value = mock_response
            download._get_headers.return_value = {}

            blob._do_download(
                transport,
                file_obj,
                download_url,
                {},
                start=0,
                end=4,
            )

        mock_logger.warning.assert_called_once_with(
            "storage: received %d more bytes than requested from GCS for bucket %r, object %r",
            5,
            "name",
            "blob-name",
        )

    @mock.patch("google.cloud.storage.blob._logger")
    def test__do_download_log_extra_bytes_chunked(self, mock_logger):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.chunk_size = 262144

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"

        patch = mock.patch("google.cloud.storage.blob.ChunkedDownload")
        with patch as patched:
            download = patched.return_value
            download._bytes_downloaded = 10
            type(download).finished = mock.PropertyMock(side_effect=[False, True])

            mock_response = mock.Mock()
            mock_response.headers = {}
            download.consume_next_chunk.return_value = mock_response
            download._get_headers.return_value = {}

            blob._do_download(
                transport,
                file_obj,
                download_url,
                {},
                start=0,
                end=4,
            )

        mock_logger.warning.assert_called_once_with(
            "storage: received %d more bytes than requested from GCS for bucket %r, object %r",
            5,
            "name",
            "blob-name",
        )

    @mock.patch("google.cloud.storage.blob._logger")
    def test__do_download_log_extra_bytes_positive_start(self, mock_logger):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.chunk_size = None

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"

        patch = mock.patch("google.cloud.storage.blob.Download")
        with patch as patched:
            download = patched.return_value
            download._bytes_downloaded = 310
            download.total_bytes = 500

            mock_response = mock.Mock()
            mock_response.headers = {}
            download.consume.return_value = mock_response
            download._get_headers.return_value = {}

            blob._do_download(
                transport,
                file_obj,
                download_url,
                {},
                start=200,
                end=None,
            )

        mock_logger.warning.assert_not_called()

    @mock.patch("google.cloud.storage.blob._logger")
    def test__do_download_log_extra_bytes_negative_start(self, mock_logger):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.chunk_size = None

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"

        patch = mock.patch("google.cloud.storage.blob.Download")
        with patch as patched:
            download = patched.return_value
            download._bytes_downloaded = 15

            mock_response = mock.Mock()
            mock_response.headers = {}
            download.consume.return_value = mock_response
            download._get_headers.return_value = {}

            blob._do_download(
                transport,
                file_obj,
                download_url,
                {},
                start=-10,
                end=None,
            )

        mock_logger.warning.assert_not_called()

    @mock.patch("google.cloud.storage.blob._logger")
    def test__do_download_log_extra_bytes_whole_file(self, mock_logger):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.chunk_size = None

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"

        patch = mock.patch("google.cloud.storage.blob.Download")
        with patch as patched:
            download = patched.return_value
            download._bytes_downloaded = 550
            download.total_bytes = 500

            mock_response = mock.Mock()
            mock_response.headers = {}
            download.consume.return_value = mock_response
            download._get_headers.return_value = {}

            blob._do_download(
                transport,
                file_obj,
                download_url,
                {},
                start=None,
                end=None,
            )

        mock_logger.warning.assert_not_called()

    @mock.patch("google.cloud.storage.blob._logger")
    def test__do_download_no_log_exact_bytes(self, mock_logger):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.chunk_size = None

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"

        patch = mock.patch("google.cloud.storage.blob.Download")
        with patch as patched:
            download = patched.return_value
            download._bytes_downloaded = 300
            download.total_bytes = 500

            mock_response = mock.Mock()
            mock_response.headers = {}
            download.consume.return_value = mock_response
            download._get_headers.return_value = {}

            blob._do_download(
                transport,
                file_obj,
                download_url,
                {},
                start=200,
                end=None,
            )

        mock_logger.warning.assert_not_called()

    def test__do_download_wo_chunks_w_custom_timeout(self):
        self._do_download_helper_wo_chunks(
            w_range=False, raw_download=False, timeout=9.58
        )

    def _do_download_helper_w_chunks(
        self, w_range, raw_download, timeout=None, checksum="md5"
    ):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob._CHUNK_SIZE_MULTIPLE = 1
        chunk_size = blob.chunk_size = 3

        transport = object()
        file_obj = io.BytesIO()
        download_url = "http://test.invalid"
        headers = {}

        download = mock.Mock(finished=False, spec=["finished", "consume_next_chunk"])

        def side_effect(*args, **kwargs):
            download.finished = True

        download.consume_next_chunk.side_effect = side_effect

        if raw_download:
            patch = mock.patch("google.cloud.storage.blob.RawChunkedDownload")
        else:
            patch = mock.patch("google.cloud.storage.blob.ChunkedDownload")

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}

        with patch as patched:
            patched.return_value = download
            if w_range:
                blob._do_download(
                    transport,
                    file_obj,
                    download_url,
                    headers,
                    start=1,
                    end=3,
                    raw_download=raw_download,
                    checksum=checksum,
                    **timeout_kwarg,
                )
            else:
                blob._do_download(
                    transport,
                    file_obj,
                    download_url,
                    headers,
                    raw_download=raw_download,
                    checksum=checksum,
                    **timeout_kwarg,
                )

        if w_range:
            patched.assert_called_once_with(
                download_url,
                chunk_size,
                file_obj,
                headers=headers,
                start=1,
                end=3,
                retry=DEFAULT_RETRY,
            )
        else:
            patched.assert_called_once_with(
                download_url,
                chunk_size,
                file_obj,
                headers=headers,
                start=0,
                end=None,
                retry=DEFAULT_RETRY,
            )
        download.consume_next_chunk.assert_called_once_with(
            transport, timeout=expected_timeout
        )

    def test__do_download_w_chunks_wo_range_wo_raw(self):
        self._do_download_helper_w_chunks(w_range=False, raw_download=False)

    def test__do_download_w_chunks_w_range_wo_raw(self):
        self._do_download_helper_w_chunks(w_range=True, raw_download=False)

    def test__do_download_w_chunks_wo_range_w_raw(self):
        self._do_download_helper_w_chunks(w_range=False, raw_download=True)

    def test__do_download_w_chunks_w_range_w_raw(self):
        self._do_download_helper_w_chunks(w_range=True, raw_download=True)

    def test__do_download_w_chunks_w_custom_timeout(self):
        self._do_download_helper_w_chunks(w_range=True, raw_download=True, timeout=9.58)

    def test__do_download_w_chunks_w_checksum(self):
        from google.cloud.storage import blob as blob_module

        with mock.patch.object(blob_module._logger, "info") as patch:
            self._do_download_helper_w_chunks(
                w_range=False, raw_download=False, checksum="md5"
            )
        patch.assert_called_once_with(
            blob_module._CHUNKED_DOWNLOAD_CHECKSUM_MESSAGE.format("md5")
        )

    def test__do_download_w_chunks_wo_checksum(self):
        from google.cloud.storage import blob as blob_module

        with mock.patch.object(blob_module._logger, "info") as patch:
            self._do_download_helper_w_chunks(
                w_range=False, raw_download=False, checksum=None
            )
        patch.assert_not_called()

    def test_download_to_file_with_failure(self):
        from google.cloud.exceptions import NotFound

        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        file_obj = io.BytesIO()

        with mock.patch.object(blob, "_prep_and_do_download"):
            blob._prep_and_do_download.side_effect = NotFound("testing")

            with self.assertRaises(NotFound):
                blob.download_to_file(file_obj)

            self.assertEqual(file_obj.tell(), 0)

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                file_obj,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )

    def test_download_to_file_wo_media_link(self):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)
        file_obj = io.BytesIO()

        with mock.patch.object(blob, "_prep_and_do_download"):
            blob.download_to_file(file_obj)

            # Make sure the media link is still unknown.
            self.assertIsNone(blob.media_link)

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                file_obj,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )

    def test_download_to_file_w_etag_match(self):
        etag = "kittens"
        client = self._make_client()
        blob = self._make_one("blob-name", bucket=_Bucket(client))
        file_obj = io.BytesIO()

        with mock.patch.object(blob, "_prep_and_do_download"):
            blob.download_to_file(file_obj, if_etag_not_match=etag)

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                file_obj,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=etag,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )

    def test_download_to_file_w_generation_match(self):
        generation_number = 6
        client = self._make_client()
        blob = self._make_one("blob-name", bucket=_Bucket(client))
        file_obj = io.BytesIO()

        with mock.patch.object(blob, "_prep_and_do_download"):
            blob.download_to_file(file_obj, if_generation_not_match=generation_number)

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                file_obj,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=generation_number,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )

    def _download_to_file_helper(
        self,
        use_chunks,
        raw_download,
        timeout=None,
        single_shot_download=False,
        **extra_kwargs,
    ):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        media_link = "http://example.com/media/"
        properties = {"mediaLink": media_link}
        blob = self._make_one(blob_name, bucket=bucket, properties=properties)
        if use_chunks:
            blob._CHUNK_SIZE_MULTIPLE = 1
            blob.chunk_size = 3

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}

        extra_kwargs.update(timeout_kwarg)

        file_obj = io.BytesIO()

        with mock.patch.object(blob, "_prep_and_do_download"):
            if raw_download:
                blob.download_to_file(
                    file_obj,
                    raw_download=True,
                    single_shot_download=single_shot_download,
                    **extra_kwargs,
                )
            else:
                blob.download_to_file(
                    file_obj, single_shot_download=single_shot_download, **extra_kwargs
                )

            expected_retry = extra_kwargs.get("retry", DEFAULT_RETRY)
            blob._prep_and_do_download.assert_called_once_with(
                file_obj,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=raw_download,
                timeout=expected_timeout,
                checksum="auto",
                retry=expected_retry,
                single_shot_download=single_shot_download,
            )

    def test_download_to_file_wo_chunks_wo_raw(self):
        self._download_to_file_helper(use_chunks=False, raw_download=False)

    def test_download_to_file_wo_chunks_no_retry(self):
        self._download_to_file_helper(use_chunks=False, raw_download=False, retry=None)

    def test_download_to_file_w_chunks_wo_raw(self):
        self._download_to_file_helper(use_chunks=True, raw_download=False)

    def test_download_to_file_wo_single_shot_download_wo_raw(self):
        self._download_to_file_helper(
            use_chunks=False, raw_download=False, single_shot_download=False
        )

    def test_download_to_file_w_single_shot_download_wo_raw(self):
        self._download_to_file_helper(
            use_chunks=False, raw_download=False, single_shot_download=True
        )

    def test_download_to_file_wo_single_shot_download_w_raw(self):
        self._download_to_file_helper(
            use_chunks=False, raw_download=True, single_shot_download=False
        )

    def test_download_to_file_w_single_shot_download_w_raw(self):
        self._download_to_file_helper(
            use_chunks=False, raw_download=True, single_shot_download=True
        )

    def test_download_to_file_wo_chunks_w_raw(self):
        self._download_to_file_helper(use_chunks=False, raw_download=True)

    def test_download_to_file_w_chunks_w_raw(self):
        self._download_to_file_helper(use_chunks=True, raw_download=True)

    def test_download_to_file_w_custom_timeout(self):
        self._download_to_file_helper(
            use_chunks=False, raw_download=False, timeout=9.58
        )

    def _download_to_filename_helper(
        self, updated, raw_download, timeout=None, **extra_kwargs
    ):
        import os

        from google.cloud._testing import _NamedTemporaryFile

        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        properties = {}
        if updated is not None:
            properties["updated"] = updated

        blob = self._make_one(blob_name, bucket=bucket, properties=properties)

        with mock.patch.object(blob, "_prep_and_do_download"):
            with _NamedTemporaryFile() as temp:
                if timeout is None:
                    blob.download_to_filename(
                        temp.name, raw_download=raw_download, **extra_kwargs
                    )
                else:
                    blob.download_to_filename(
                        temp.name,
                        raw_download=raw_download,
                        timeout=timeout,
                        **extra_kwargs,
                    )

                if updated is None:
                    self.assertIsNone(blob.updated)
                else:
                    mtime = os.path.getmtime(temp.name)
                    updated_time = blob.updated.timestamp()
                    self.assertEqual(mtime, updated_time)

            expected_timeout = (
                self._get_default_timeout() if timeout is None else timeout
            )

            expected_retry = extra_kwargs.get("retry", DEFAULT_RETRY)

            blob._prep_and_do_download.assert_called_once_with(
                mock.ANY,
                client=None,
                start=None,
                end=None,
                raw_download=raw_download,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                timeout=expected_timeout,
                checksum="auto",
                retry=expected_retry,
                single_shot_download=False,
            )
            stream = blob._prep_and_do_download.mock_calls[0].args[0]
            self.assertEqual(stream.name, temp.name)

    def test_download_to_filename_w_updated_wo_raw(self):
        updated = "2014-12-06T13:13:50.690Z"
        self._download_to_filename_helper(updated=updated, raw_download=False)

    def test_download_to_filename_w_updated_no_retry(self):
        updated = "2014-12-06T13:13:50.690Z"
        self._download_to_filename_helper(
            updated=updated, raw_download=False, retry=None
        )

    def test_download_to_filename_wo_updated_wo_raw(self):
        self._download_to_filename_helper(updated=None, raw_download=False)

    def test_download_to_filename_w_updated_w_raw(self):
        updated = "2014-12-06T13:13:50.690Z"
        self._download_to_filename_helper(updated=updated, raw_download=True)

    def test_download_to_filename_wo_updated_w_raw(self):
        self._download_to_filename_helper(updated=None, raw_download=True)

    def test_download_to_filename_w_custom_timeout(self):
        self._download_to_filename_helper(
            updated=None, raw_download=False, timeout=9.58
        )

    def test_download_to_filename_w_etag_match(self):
        from google.cloud._testing import _NamedTemporaryFile

        etag = "kittens"
        client = self._make_client()
        blob = self._make_one("blob-name", bucket=_Bucket(client))

        with mock.patch.object(blob, "_prep_and_do_download"):
            with _NamedTemporaryFile() as temp:
                blob.download_to_filename(temp.name, if_etag_match=etag)

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                mock.ANY,
                client=None,
                start=None,
                end=None,
                if_etag_match=etag,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )
            stream = blob._prep_and_do_download.mock_calls[0].args[0]
            self.assertEqual(stream.name, temp.name)

    def test_download_to_filename_w_generation_match(self):
        from google.cloud._testing import _NamedTemporaryFile

        generation_number = 6
        client = self._make_client()
        blob = self._make_one("blob-name", bucket=_Bucket(client))

        with mock.patch.object(blob, "_prep_and_do_download"):
            with _NamedTemporaryFile() as temp:
                blob.download_to_filename(
                    temp.name, if_generation_match=generation_number
                )

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                mock.ANY,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=generation_number,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )
            stream = blob._prep_and_do_download.mock_calls[0].args[0]
            self.assertEqual(stream.name, temp.name)

    def test_download_to_filename_corrupted(self):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        with mock.patch.object(blob, "_prep_and_do_download"):
            blob._prep_and_do_download.side_effect = DataCorruption("testing")

            # Try to download into a temporary file (don't use
            # `_NamedTemporaryFile` it will try to remove after the file is
            # already removed)
            filehandle, filename = tempfile.mkstemp()
            os.close(filehandle)
            self.assertTrue(os.path.exists(filename))

            with self.assertRaises(DataCorruption):
                blob.download_to_filename(filename)

            # Make sure the file was cleaned up.
            self.assertFalse(os.path.exists(filename))

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                mock.ANY,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )
            stream = blob._prep_and_do_download.mock_calls[0].args[0]
            self.assertEqual(stream.name, filename)

    def test_download_to_filename_notfound(self):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        with mock.patch.object(blob, "_prep_and_do_download"):
            blob._prep_and_do_download.side_effect = NotFound("testing")

            # Try to download into a temporary file (don't use
            # `_NamedTemporaryFile` it will try to remove after the file is
            # already removed)
            filehandle, filename = tempfile.mkstemp()
            os.close(filehandle)
            self.assertTrue(os.path.exists(filename))

            with self.assertRaises(NotFound):
                blob.download_to_filename(filename)

            # Make sure the file was cleaned up.
            self.assertFalse(os.path.exists(filename))

            expected_timeout = self._get_default_timeout()
            blob._prep_and_do_download.assert_called_once_with(
                mock.ANY,
                client=None,
                start=None,
                end=None,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                raw_download=False,
                timeout=expected_timeout,
                checksum="auto",
                retry=DEFAULT_RETRY,
                single_shot_download=False,
            )
            stream = blob._prep_and_do_download.mock_calls[0].args[0]
            self.assertEqual(stream.name, filename)

    def _download_as_bytes_helper(
        self, raw_download, timeout=None, single_shot_download=False, **extra_kwargs
    ):
        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        with mock.patch.object(blob, "_prep_and_do_download"):
            if timeout is None:
                expected_timeout = self._get_default_timeout()
                fetched = blob.download_as_bytes(
                    raw_download=raw_download,
                    single_shot_download=single_shot_download,
                    **extra_kwargs,
                )
            else:
                expected_timeout = timeout
                fetched = blob.download_as_bytes(
                    raw_download=raw_download,
                    timeout=timeout,
                    single_shot_download=single_shot_download,
                    **extra_kwargs,
                )
            self.assertEqual(fetched, b"")

            expected_retry = extra_kwargs.get("retry", DEFAULT_RETRY)

            blob._prep_and_do_download.assert_called_once_with(
                mock.ANY,
                client=None,
                start=None,
                end=None,
                raw_download=raw_download,
                if_etag_match=None,
                if_etag_not_match=None,
                if_generation_match=None,
                if_generation_not_match=None,
                if_metageneration_match=None,
                if_metageneration_not_match=None,
                timeout=expected_timeout,
                checksum="auto",
                retry=expected_retry,
                single_shot_download=single_shot_download,
            )
            stream = blob._prep_and_do_download.mock_calls[0].args[0]
            self.assertIsInstance(stream, io.BytesIO)

    def test_download_as_bytes_w_custom_timeout(self):
        self._download_as_bytes_helper(raw_download=False, timeout=9.58)

    def test_download_as_bytes_w_etag_match(self):
        ETAG = "kittens"
        MEDIA_LINK = "http://example.com/media/"

        client = self._make_client()
        blob = self._make_one(
            "blob-name", bucket=_Bucket(client), properties={"mediaLink": MEDIA_LINK}
        )
        blob._prep_and_do_download = mock.Mock()

        fetched = blob.download_as_bytes(if_etag_match=ETAG)
        self.assertEqual(fetched, b"")

        blob._prep_and_do_download.assert_called_once_with(
            mock.ANY,
            client=None,
            start=None,
            end=None,
            raw_download=False,
            if_etag_match=ETAG,
            if_etag_not_match=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            checksum="auto",
            retry=DEFAULT_RETRY,
            single_shot_download=False,
        )

    def test_download_as_bytes_w_generation_match(self):
        GENERATION_NUMBER = 6
        MEDIA_LINK = "http://example.com/media/"

        client = self._make_client()
        blob = self._make_one(
            "blob-name", bucket=_Bucket(client), properties={"mediaLink": MEDIA_LINK}
        )
        blob._prep_and_do_download = mock.Mock()

        fetched = blob.download_as_bytes(if_generation_match=GENERATION_NUMBER)
        self.assertEqual(fetched, b"")

        blob._prep_and_do_download.assert_called_once_with(
            mock.ANY,
            client=None,
            start=None,
            end=None,
            raw_download=False,
            if_etag_match=None,
            if_etag_not_match=None,
            if_generation_match=GENERATION_NUMBER,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            checksum="auto",
            retry=DEFAULT_RETRY,
            single_shot_download=False,
        )

    def test_download_as_bytes_wo_raw(self):
        self._download_as_bytes_helper(raw_download=False)

    def test_download_as_bytes_no_retry(self):
        self._download_as_bytes_helper(raw_download=False, retry=None)

    def test_download_as_bytes_w_raw(self):
        self._download_as_bytes_helper(raw_download=True)

    def test_download_as_byte_w_custom_timeout(self):
        self._download_as_bytes_helper(raw_download=False, timeout=9.58)

    def test_download_as_bytes_wo_single_shot_download(self):
        self._download_as_bytes_helper(
            raw_download=False, retry=None, single_shot_download=False
        )

    def test_download_as_bytes_w_single_shot_download(self):
        self._download_as_bytes_helper(
            raw_download=False, retry=None, single_shot_download=True
        )

    def _download_as_text_helper(
        self,
        raw_download,
        client=None,
        start=None,
        end=None,
        if_etag_match=None,
        if_etag_not_match=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=None,
        encoding=None,
        charset=None,
        no_charset=False,
        expected_value="DEADBEEF",
        payload=None,
        **extra_kwargs,
    ):
        if payload is None:
            if encoding is not None:
                payload = expected_value.encode(encoding)
            else:
                payload = expected_value.encode()

        blob_name = "blob-name"
        bucket_client = self._make_client()
        bucket = _Bucket(bucket_client)

        properties = {}
        if charset is not None:
            properties["contentType"] = f"text/plain; charset={charset}"  # noqa: E702
        elif no_charset:
            properties = {"contentType": "text/plain"}

        blob = self._make_one(blob_name, bucket=bucket, properties=properties)
        blob.download_as_bytes = mock.Mock(return_value=payload)

        kwargs = {"raw_download": raw_download}

        if client is not None:
            kwargs["client"] = client

        if start is not None:
            kwargs["start"] = start

        if end is not None:
            kwargs["end"] = end

        if encoding is not None:
            kwargs["encoding"] = encoding

        if if_etag_match is not None:
            kwargs["if_etag_match"] = if_etag_match

        if if_etag_not_match is not None:
            kwargs["if_etag_not_match"] = if_etag_not_match

        if if_generation_match is not None:
            kwargs["if_generation_match"] = if_generation_match

        if if_generation_not_match is not None:
            kwargs["if_generation_not_match"] = if_generation_not_match

        if if_metageneration_match is not None:
            kwargs["if_metageneration_match"] = if_metageneration_match

        if if_metageneration_not_match is not None:
            kwargs["if_metageneration_not_match"] = if_metageneration_not_match

        if timeout is None:
            expected_timeout = self._get_default_timeout()
        else:
            kwargs["timeout"] = expected_timeout = timeout

        kwargs.update(extra_kwargs)

        fetched = blob.download_as_text(**kwargs)

        self.assertEqual(fetched, expected_value)

        expected_retry = extra_kwargs.get("retry", DEFAULT_RETRY)

        blob.download_as_bytes.assert_called_once_with(
            client=client,
            start=start,
            end=end,
            raw_download=raw_download,
            timeout=expected_timeout,
            if_etag_match=if_etag_match,
            if_etag_not_match=if_etag_not_match,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            retry=expected_retry,
            single_shot_download=False,
        )

    def test_download_as_text_wo_raw(self):
        self._download_as_text_helper(raw_download=False)

    def test_download_as_text_w_no_retry(self):
        self._download_as_text_helper(raw_download=False, retry=None)

    def test_download_as_text_w_raw(self):
        self._download_as_text_helper(raw_download=True)

    def test_download_as_text_w_client(self):
        self._download_as_text_helper(raw_download=False, client=object())

    def test_download_as_text_w_start(self):
        self._download_as_text_helper(raw_download=False, start=123)

    def test_download_as_text_w_end(self):
        self._download_as_text_helper(raw_download=False, end=456)

    def test_download_as_text_w_custom_timeout(self):
        self._download_as_text_helper(raw_download=False, timeout=9.58)

    def test_download_as_text_w_if_etag_match_str(self):
        self._download_as_text_helper(
            raw_download=False,
            if_etag_match="kittens",
        )

    def test_download_as_text_w_if_etag_match_list(self):
        self._download_as_text_helper(
            raw_download=False,
            if_etag_match=["kittens", "fluffy"],
        )

    def test_download_as_text_w_if_etag_not_match_str(self):
        self._download_as_text_helper(
            raw_download=False,
            if_etag_not_match="kittens",
        )

    def test_download_as_text_w_if_etag_not_match_list(self):
        self._download_as_text_helper(
            raw_download=False,
            if_etag_not_match=["kittens", "fluffy"],
        )

    def test_download_as_text_w_if_generation_match(self):
        self._download_as_text_helper(raw_download=False, if_generation_match=6)

    def test_download_as_text_w_if_generation_not_match(self):
        self._download_as_text_helper(raw_download=False, if_generation_not_match=6)

    def test_download_as_text_w_if_metageneration_match(self):
        self._download_as_text_helper(raw_download=False, if_metageneration_match=6)

    def test_download_as_text_w_if_metageneration_not_match(self):
        self._download_as_text_helper(raw_download=False, if_metageneration_not_match=6)

    def test_download_as_text_w_encoding(self):
        encoding = "utf-16"
        self._download_as_text_helper(
            raw_download=False,
            encoding=encoding,
        )

    def test_download_as_text_w_no_charset(self):
        self._download_as_text_helper(
            raw_download=False,
            no_charset=True,
        )

    def test_download_as_text_w_non_ascii_w_explicit_encoding(self):
        expected_value = "\x0aFe"
        encoding = "utf-16"
        charset = "latin1"
        payload = expected_value.encode(encoding)
        self._download_as_text_helper(
            raw_download=False,
            expected_value=expected_value,
            payload=payload,
            encoding=encoding,
            charset=charset,
        )

    def test_download_as_text_w_non_ascii_wo_explicit_encoding_w_charset(self):
        expected_value = "\x0aFe"
        charset = "utf-16"
        payload = expected_value.encode(charset)
        self._download_as_text_helper(
            raw_download=False,
            expected_value=expected_value,
            payload=payload,
            charset=charset,
        )

    @mock.patch("warnings.warn")
    def test_download_as_string(self, mock_warn):
        from google.cloud.storage.blob import _DOWNLOAD_AS_STRING_DEPRECATED

        MEDIA_LINK = "http://example.com/media/"

        client = self._make_client()
        blob = self._make_one(
            "blob-name", bucket=_Bucket(client), properties={"mediaLink": MEDIA_LINK}
        )
        blob._prep_and_do_download = mock.Mock()

        fetched = blob.download_as_string()
        self.assertEqual(fetched, b"")

        blob._prep_and_do_download.assert_called_once_with(
            mock.ANY,
            client=None,
            start=None,
            end=None,
            raw_download=False,
            if_etag_match=None,
            if_etag_not_match=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            checksum="auto",
            retry=DEFAULT_RETRY,
            single_shot_download=False,
        )

        mock_warn.assert_any_call(
            _DOWNLOAD_AS_STRING_DEPRECATED,
            PendingDeprecationWarning,
            stacklevel=2,
        )

    @mock.patch("warnings.warn")
    def test_download_as_string_no_retry(self, mock_warn):
        from google.cloud.storage.blob import _DOWNLOAD_AS_STRING_DEPRECATED

        MEDIA_LINK = "http://example.com/media/"

        client = self._make_client()
        blob = self._make_one(
            "blob-name", bucket=_Bucket(client), properties={"mediaLink": MEDIA_LINK}
        )
        blob._prep_and_do_download = mock.Mock()

        fetched = blob.download_as_string(retry=None)
        self.assertEqual(fetched, b"")

        blob._prep_and_do_download.assert_called_once_with(
            mock.ANY,
            client=None,
            start=None,
            end=None,
            raw_download=False,
            if_etag_match=None,
            if_etag_not_match=None,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            checksum="auto",
            retry=None,
            single_shot_download=False,
        )

        mock_warn.assert_any_call(
            _DOWNLOAD_AS_STRING_DEPRECATED,
            PendingDeprecationWarning,
            stacklevel=2,
        )

    def test__get_content_type_explicit(self):
        blob = self._make_one("blob-name", bucket=None)

        content_type = "text/plain"
        return_value = blob._get_content_type(content_type)
        self.assertEqual(return_value, content_type)

    def test__get_content_type_from_blob(self):
        blob = self._make_one("blob-name", bucket=None)
        blob.content_type = "video/mp4"

        return_value = blob._get_content_type(None)
        self.assertEqual(return_value, blob.content_type)

    def test__get_content_type_from_filename(self):
        blob = self._make_one("blob-name", bucket=None)

        return_value = blob._get_content_type(None, filename="archive.tar")
        self.assertEqual(return_value, "application/x-tar")

    def test__get_content_type_default(self):
        blob = self._make_one("blob-name", bucket=None)

        return_value = blob._get_content_type(None)
        self.assertEqual(return_value, "application/octet-stream")

    def test__get_writable_metadata_no_changes(self):
        name = "blob-name"
        blob = self._make_one(name, bucket=None)

        object_metadata = blob._get_writable_metadata()
        expected = {"name": name}
        self.assertEqual(object_metadata, expected)

    def test__get_writable_metadata_with_changes(self):
        name = "blob-name"
        blob = self._make_one(name, bucket=None)
        blob.storage_class = "NEARLINE"
        blob.cache_control = "max-age=3600"
        blob.metadata = {"color": "red"}

        object_metadata = blob._get_writable_metadata()
        expected = {
            "cacheControl": blob.cache_control,
            "metadata": blob.metadata,
            "name": name,
            "storageClass": blob.storage_class,
        }
        self.assertEqual(object_metadata, expected)

    def test__get_writable_metadata_unwritable_field(self):
        name = "blob-name"
        properties = {"updated": "2016-10-16T18:18:18.181Z"}
        blob = self._make_one(name, bucket=None, properties=properties)
        # Fake that `updated` is in changes.
        blob._changes.add("updated")

        object_metadata = blob._get_writable_metadata()
        expected = {"name": name}
        self.assertEqual(object_metadata, expected)

    def test__set_metadata_to_none(self):
        name = "blob-name"
        blob = self._make_one(name, bucket=None)
        blob.storage_class = "NEARLINE"
        blob.cache_control = "max-age=3600"

        with mock.patch("google.cloud.storage.blob.Blob._patch_property") as patch_prop:
            blob.metadata = None
            patch_prop.assert_called_once_with("metadata", None)

    def test__get_upload_arguments(self):
        name = "blob-name"
        key = b"[pXw@,p@@AfBfrR3x-2b2SCHR,.?YwRO"
        custom_headers = {
            "x-goog-custom-audit-foo": "bar",
            "x-goog-custom-audit-user": "baz",
        }
        client = mock.Mock(_connection=_Connection)
        client._connection.user_agent = "testing 1.2.3"
        client._extra_headers = custom_headers
        blob = self._make_one(name, bucket=None, encryption_key=key)
        blob.content_disposition = "inline"

        COMMAND = "tm.upload_many"
        content_type = "image/jpeg"
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            info = blob._get_upload_arguments(client, content_type, command=COMMAND)

        headers, object_metadata, new_content_type = info
        header_key_value = "W3BYd0AscEBAQWZCZnJSM3gtMmIyU0NIUiwuP1l3Uk8="
        header_key_hash_value = "G0++dxF4q5rG4o9kE8gvEKn15RH6wLm0wXV1MgAlXOg="
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            expected_headers = {
                **_get_default_headers(
                    client._connection.user_agent, content_type, command=COMMAND
                ),
                "X-Goog-Encryption-Algorithm": "AES256",
                "X-Goog-Encryption-Key": header_key_value,
                "X-Goog-Encryption-Key-Sha256": header_key_hash_value,
                **custom_headers,
            }
        self.assertEqual(
            headers["x-goog-api-client"],
            f"{client._connection.user_agent} {GCCL_INVOCATION_TEST_CONST} gccl-gcs-cmd/{COMMAND}",
        )
        self.assertEqual(headers, expected_headers)
        expected_metadata = {
            "contentDisposition": blob.content_disposition,
            "name": name,
        }
        self.assertEqual(object_metadata, expected_metadata)
        self.assertEqual(new_content_type, content_type)

    def _mock_transport(self, status_code, headers, content=b""):
        fake_transport = mock.Mock(spec=["request"])
        fake_response = self._mock_requests_response(
            status_code, headers, content=content
        )
        fake_transport.request.return_value = fake_response
        return fake_transport

    def _do_multipart_success(
        self,
        mock_get_boundary,
        client=None,
        size=None,
        user_project=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        kms_key_name=None,
        timeout=None,
        metadata=None,
        mtls=False,
        retry=None,
    ):
        bucket = _Bucket(name="w00t", user_project=user_project)
        blob = self._make_one("blob-name", bucket=bucket, kms_key_name=kms_key_name)
        self.assertIsNone(blob.chunk_size)
        if metadata:
            self.assertIsNone(blob.metadata)
            blob._properties["metadata"] = metadata
            self.assertEqual(len(blob._changes), 0)

        # Create some mock arguments.
        if not client:
            # Create mocks to be checked for doing transport.
            transport = self._mock_transport(http.client.OK, {})

            client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
            client._connection.API_BASE_URL = "https://storage.googleapis.com"
            client._extra_headers = {}

        # Mock get_api_base_url_for_mtls function.
        mtls_url = "https://foo.mtls"
        if mtls:
            client._connection.get_api_base_url_for_mtls = mock.Mock(
                return_value=mtls_url
            )

        data = b"data here hear hier"
        stream = io.BytesIO(data)
        content_type = "application/xml"

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}

        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            response = blob._do_multipart_upload(
                client,
                stream,
                content_type,
                size,
                predefined_acl,
                if_generation_match,
                if_generation_not_match,
                if_metageneration_match,
                if_metageneration_not_match,
                checksum=None,
                retry=retry,
                **timeout_kwarg,
            )

        # Clean up the get_api_base_url_for_mtls mock.
        if mtls:
            del client._connection.get_api_base_url_for_mtls

        # Check the mocks and the returned value.
        self.assertIs(response, client._http.request.return_value)
        if size is None:
            data_read = data
            self.assertEqual(stream.tell(), len(data))
        else:
            data_read = data[:size]
            self.assertEqual(stream.tell(), size)

        mock_get_boundary.assert_called_once_with()

        upload_url = (
            "https://storage.googleapis.com/upload/storage/v1" + bucket.path + "/o"
        )
        if mtls:
            upload_url = mtls_url + "/upload/storage/v1" + bucket.path + "/o"

        qs_params = [("uploadType", "multipart")]

        if user_project is not None:
            qs_params.append(("userProject", user_project))

        if predefined_acl is not None:
            qs_params.append(("predefinedAcl", predefined_acl))

        if kms_key_name is not None and "cryptoKeyVersions" not in kms_key_name:
            qs_params.append(("kmsKeyName", kms_key_name))

        if if_generation_match is not None:
            qs_params.append(("ifGenerationMatch", if_generation_match))

        if if_generation_not_match is not None:
            qs_params.append(("ifGenerationNotMatch", if_generation_not_match))

        if if_metageneration_match is not None:
            qs_params.append(("ifMetagenerationMatch", if_metageneration_match))

        if if_metageneration_not_match is not None:
            qs_params.append(("ifMetaGenerationNotMatch", if_metageneration_not_match))

        upload_url += "?" + urlencode(qs_params)

        blob_data = {"name": "blob-name"}
        if metadata:
            blob_data["metadata"] = metadata
            self.assertEqual(blob._changes, set(["metadata"]))
        payload = (
            b"--==0==\r\n"
            + b"content-type: application/json; charset=UTF-8\r\n\r\n"
            + json.dumps(blob_data).encode("utf-8")
            + b"\r\n--==0==\r\n"
            + b"content-type: application/xml\r\n\r\n"
            + data_read
            + b"\r\n--==0==--"
        )
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            headers = {
                **_get_default_headers(
                    client._connection.user_agent,
                    b'multipart/related; boundary="==0=="',
                    "application/xml",
                ),
                **client._extra_headers,
            }
        client._http.request.assert_called_once_with(
            "POST", upload_url, data=payload, headers=headers, timeout=expected_timeout
        )

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_no_size(self, mock_get_boundary):
        self._do_multipart_success(mock_get_boundary, predefined_acl="private")

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_no_size_retry(self, mock_get_boundary):
        self._do_multipart_success(
            mock_get_boundary, predefined_acl="private", retry=DEFAULT_RETRY
        )

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_no_size_mtls(self, mock_get_boundary):
        self._do_multipart_success(
            mock_get_boundary, predefined_acl="private", mtls=True
        )

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_size(self, mock_get_boundary):
        self._do_multipart_success(mock_get_boundary, size=10)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_user_project(self, mock_get_boundary):
        user_project = "user-project-123"
        self._do_multipart_success(mock_get_boundary, user_project=user_project)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_kms(self, mock_get_boundary):
        kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        self._do_multipart_success(mock_get_boundary, kms_key_name=kms_resource)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_kms_with_version(self, mock_get_boundary):
        kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
            "cryptoKeyVersions/1"
        )
        self._do_multipart_success(mock_get_boundary, kms_key_name=kms_resource)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_retry(self, mock_get_boundary):
        self._do_multipart_success(mock_get_boundary, retry=DEFAULT_RETRY)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_generation_match(self, mock_get_boundary):
        self._do_multipart_success(
            mock_get_boundary, if_generation_match=4, if_metageneration_match=4
        )

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_custom_timeout(self, mock_get_boundary):
        self._do_multipart_success(mock_get_boundary, timeout=9.58)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_generation_not_match(self, mock_get_boundary):
        self._do_multipart_success(
            mock_get_boundary, if_generation_not_match=4, if_metageneration_not_match=4
        )

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_client(self, mock_get_boundary):
        transport = self._mock_transport(http.client.OK, {})
        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._extra_headers = {}
        self._do_multipart_success(mock_get_boundary, client=client)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_client_custom_headers(self, mock_get_boundary):
        custom_headers = {
            "x-goog-custom-audit-foo": "bar",
            "x-goog-custom-audit-user": "baz",
        }
        transport = self._mock_transport(http.client.OK, {})
        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._extra_headers = custom_headers
        self._do_multipart_success(mock_get_boundary, client=client)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==0=="
    )
    def test__do_multipart_upload_with_metadata(self, mock_get_boundary):
        self._do_multipart_success(mock_get_boundary, metadata={"test": "test"})

    def test__do_multipart_upload_bad_size(self):
        blob = self._make_one("blob-name", bucket=None)

        data = b"data here hear hier"
        stream = io.BytesIO(data)
        size = 50
        self.assertGreater(size, len(data))

        with self.assertRaises(ValueError) as exc_info:
            blob._do_multipart_upload(
                None, stream, None, size, None, None, None, None, None, None
            )

        exc_contents = str(exc_info.exception)
        self.assertIn("was specified but the file-like object only had", exc_contents)
        self.assertEqual(stream.tell(), len(data))

    def _initiate_resumable_helper(
        self,
        client=None,
        size=None,
        extra_headers=None,
        chunk_size=None,
        user_project=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        blob_chunk_size=786432,
        kms_key_name=None,
        timeout=None,
        metadata=None,
        mtls=False,
        retry=None,
        crc32c_checksum_value=None,
    ):
        from google.cloud.storage._media.requests import ResumableUpload
        from google.cloud.storage.blob import _DEFAULT_CHUNKSIZE

        bucket = _Bucket(name="whammy", user_project=user_project)
        blob = self._make_one("blob-name", bucket=bucket, kms_key_name=kms_key_name)
        if metadata:
            self.assertIsNone(blob.metadata)
            blob._properties["metadata"] = metadata
            self.assertEqual(len(blob._changes), 0)
        else:
            blob.metadata = {"rook": "takes knight"}
        blob.chunk_size = blob_chunk_size
        if blob_chunk_size is not None:
            self.assertIsNotNone(blob.chunk_size)
        else:
            self.assertIsNone(blob.chunk_size)

        # Need to make sure **same** dict is used because ``json.dumps()``
        # will depend on the hash order.
        if not metadata:
            object_metadata = blob._get_writable_metadata()
            blob._get_writable_metadata = mock.Mock(
                return_value=object_metadata, spec=[]
            )

        resumable_url = "http://test.invalid?upload_id=hey-you"
        if not client:
            # Create mocks to be checked for doing transport.
            response_headers = {"location": resumable_url}
            transport = self._mock_transport(http.client.OK, response_headers)

            # Create some mock arguments and call the method under test.
            client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
            client._connection.API_BASE_URL = "https://storage.googleapis.com"
            client._extra_headers = {}

        # Mock get_api_base_url_for_mtls function.
        mtls_url = "https://foo.mtls"
        if mtls:
            client._connection.get_api_base_url_for_mtls = mock.Mock(
                return_value=mtls_url
            )

        data = b"hello hallo halo hi-low"
        stream = io.BytesIO(data)
        content_type = "text/plain"

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            upload, transport = blob._initiate_resumable_upload(
                client,
                stream,
                content_type,
                size,
                extra_headers=extra_headers,
                chunk_size=chunk_size,
                predefined_acl=predefined_acl,
                if_generation_match=if_generation_match,
                if_generation_not_match=if_generation_not_match,
                if_metageneration_match=if_metageneration_match,
                if_metageneration_not_match=if_metageneration_not_match,
                retry=retry,
                crc32c_checksum_value=crc32c_checksum_value,
                **timeout_kwarg,
            )

        # Clean up the get_api_base_url_for_mtls mock.
        if mtls:
            del client._connection.get_api_base_url_for_mtls

        # Check the returned values.
        self.assertIsInstance(upload, ResumableUpload)

        upload_url = (
            "https://storage.googleapis.com/upload/storage/v1" + bucket.path + "/o"
        )
        if mtls:
            upload_url = mtls_url + "/upload/storage/v1" + bucket.path + "/o"
        qs_params = [("uploadType", "resumable")]

        if user_project is not None:
            qs_params.append(("userProject", user_project))

        if predefined_acl is not None:
            qs_params.append(("predefinedAcl", predefined_acl))

        if kms_key_name is not None and "cryptoKeyVersions" not in kms_key_name:
            qs_params.append(("kmsKeyName", kms_key_name))

        if if_generation_match is not None:
            qs_params.append(("ifGenerationMatch", if_generation_match))

        if if_generation_not_match is not None:
            qs_params.append(("ifGenerationNotMatch", if_generation_not_match))

        if if_metageneration_match is not None:
            qs_params.append(("ifMetagenerationMatch", if_metageneration_match))

        if if_metageneration_not_match is not None:
            qs_params.append(("ifMetaGenerationNotMatch", if_metageneration_not_match))

        upload_url += "?" + urlencode(qs_params)

        self.assertEqual(upload.upload_url, upload_url)
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            if extra_headers is None:
                expected_headers = {
                    **_get_default_headers(client._connection.user_agent, content_type),
                    **client._extra_headers,
                }
                self.assertEqual(upload._headers, expected_headers)
            else:
                expected_headers = {
                    **_get_default_headers(client._connection.user_agent, content_type),
                    **client._extra_headers,
                    **extra_headers,
                }
                self.assertEqual(upload._headers, expected_headers)
                self.assertIsNot(upload._headers, expected_headers)
        self.assertFalse(upload.finished)
        if chunk_size is None:
            if blob_chunk_size is None:
                self.assertEqual(upload._chunk_size, _DEFAULT_CHUNKSIZE)
            else:
                self.assertEqual(upload._chunk_size, blob.chunk_size)
        else:
            self.assertNotEqual(blob.chunk_size, chunk_size)
            self.assertEqual(upload._chunk_size, chunk_size)
        self.assertIs(upload._stream, stream)
        if metadata:
            self.assertEqual(blob._changes, set(["metadata"]))
        if size is None:
            self.assertIsNone(upload._total_bytes)
        else:
            self.assertEqual(upload._total_bytes, size)
        self.assertEqual(upload._content_type, content_type)
        self.assertEqual(upload.resumable_url, resumable_url)
        retry_strategy = upload._retry_strategy
        self.assertEqual(retry_strategy, retry)
        self.assertIs(client._http, transport)
        # Make sure we never read from the stream.
        self.assertEqual(stream.tell(), 0)

        if metadata:
            object_metadata = {"name": "blob-name", "metadata": metadata}
        else:
            # Check the mocks.
            blob._get_writable_metadata.assert_called_once_with()

        if crc32c_checksum_value is not None:
            object_metadata["crc32c"] = crc32c_checksum_value

        payload = json.dumps(object_metadata).encode("utf-8")

        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            expected_headers = {
                **_get_default_headers(
                    client._connection.user_agent, x_upload_content_type=content_type
                ),
                **client._extra_headers,
            }
        if size is not None:
            expected_headers["x-upload-content-length"] = str(size)
        if extra_headers is not None:
            expected_headers.update(extra_headers)
        transport.request.assert_called_once_with(
            "POST",
            upload_url,
            data=payload,
            headers=expected_headers,
            timeout=expected_timeout,
        )

    def test__initiate_resumable_upload_with_metadata(self):
        self._initiate_resumable_helper(metadata={"test": "test"})

    def test__initiate_resumable_upload_with_user_provided_checksum(self):
        self._initiate_resumable_helper(
            crc32c_checksum_value="this-is-a-fake-checksum-for-unit-tests",
        )

    def test__initiate_resumable_upload_w_metadata_and_user_provided_checksum(self):
        self._initiate_resumable_helper(
            crc32c_checksum_value="test-checksum",
            metadata={"my-fav-key": "my-fav-value"},
        )

    def test__initiate_resumable_upload_with_custom_timeout(self):
        self._initiate_resumable_helper(timeout=9.58)

    def test__initiate_resumable_upload_no_size(self):
        self._initiate_resumable_helper()

    def test__initiate_resumable_upload_no_size_mtls(self):
        self._initiate_resumable_helper(mtls=True)

    def test__initiate_resumable_upload_with_size(self):
        self._initiate_resumable_helper(size=10000)

    def test__initiate_resumable_upload_with_user_project(self):
        user_project = "user-project-123"
        self._initiate_resumable_helper(user_project=user_project)

    def test__initiate_resumable_upload_with_kms(self):
        kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        self._initiate_resumable_helper(kms_key_name=kms_resource)

    def test__initiate_resumable_upload_with_kms_with_version(self):
        kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
            "cryptoKeyVersions/1"
        )
        self._initiate_resumable_helper(kms_key_name=kms_resource)

    def test__initiate_resumable_upload_without_chunk_size(self):
        self._initiate_resumable_helper(blob_chunk_size=None)

    def test__initiate_resumable_upload_with_chunk_size(self):
        one_mb = 1048576
        self._initiate_resumable_helper(chunk_size=one_mb)

    def test__initiate_resumable_upload_with_extra_headers(self):
        extra_headers = {"origin": "http://not-in-kansas-anymore.invalid"}
        self._initiate_resumable_helper(extra_headers=extra_headers)

    def test__initiate_resumable_upload_with_retry(self):
        self._initiate_resumable_helper(retry=DEFAULT_RETRY)

    def test__initiate_resumable_upload_with_generation_match(self):
        self._initiate_resumable_helper(
            if_generation_match=4, if_metageneration_match=4
        )

    def test__initiate_resumable_upload_with_generation_not_match(self):
        self._initiate_resumable_helper(
            if_generation_not_match=4, if_metageneration_not_match=4
        )

    def test__initiate_resumable_upload_with_predefined_acl(self):
        self._initiate_resumable_helper(predefined_acl="private")

    def test__initiate_resumable_upload_with_client(self):
        resumable_url = "http://test.invalid?upload_id=hey-you"
        response_headers = {"location": resumable_url}
        transport = self._mock_transport(http.client.OK, response_headers)

        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._extra_headers = {}
        self._initiate_resumable_helper(client=client)

    def test__initiate_resumable_upload_with_client_custom_headers(self):
        custom_headers = {
            "x-goog-custom-audit-foo": "bar",
            "x-goog-custom-audit-user": "baz",
        }
        resumable_url = "http://test.invalid?upload_id=hey-you"
        response_headers = {"location": resumable_url}
        transport = self._mock_transport(http.client.OK, response_headers)

        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._extra_headers = custom_headers
        self._initiate_resumable_helper(client=client)

    def _make_resumable_transport(
        self,
        headers1,
        headers2,
        headers3,
        total_bytes,
        data_corruption=False,
        md5_checksum_value=None,
        crc32c_checksum_value=None,
    ):
        fake_transport = mock.Mock(spec=["request"])

        fake_response1 = self._mock_requests_response(http.client.OK, headers1)
        fake_response2 = self._mock_requests_response(
            http.client.PERMANENT_REDIRECT, headers2
        )
        json_body = json.dumps(
            {
                "size": str(total_bytes),
                "md5Hash": md5_checksum_value,
                "crc32c": crc32c_checksum_value,
            }
        )
        if data_corruption:
            fake_response3 = DataCorruption(None)
        else:
            fake_response3 = self._mock_requests_response(
                http.client.OK, headers3, content=json_body.encode("utf-8")
            )

        responses = [fake_response1, fake_response2, fake_response3]
        fake_transport.request.side_effect = responses
        return fake_transport, responses

    @staticmethod
    def _do_resumable_upload_call0(
        client,
        blob,
        content_type,
        size=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=None,
    ):
        # First mock transport.request() does initiates upload.
        upload_url = (
            "https://storage.googleapis.com/upload/storage/v1"
            + blob.bucket.path
            + "/o?uploadType=resumable"
        )
        if predefined_acl is not None:
            upload_url += f"&predefinedAcl={predefined_acl}"
        expected_headers = _get_default_headers(
            client._connection.user_agent, x_upload_content_type=content_type
        )
        if size is not None:
            expected_headers["x-upload-content-length"] = str(size)
        payload = json.dumps({"name": blob.name}).encode("utf-8")
        return mock.call(
            "POST", upload_url, data=payload, headers=expected_headers, timeout=timeout
        )

    @staticmethod
    def _do_resumable_upload_call1(
        client,
        blob,
        content_type,
        data,
        resumable_url,
        size=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=None,
    ):
        # Second mock transport.request() does sends first chunk.
        if size is None:
            content_range = f"bytes 0-{blob.chunk_size - 1:}/*"
        else:
            content_range = f"bytes 0-{blob.chunk_size - 1}/{size}"

        expected_headers = {
            **_get_default_headers(
                client._connection.user_agent, x_upload_content_type=content_type
            ),
            "content-type": content_type,
            "content-range": content_range,
        }
        payload = data[: blob.chunk_size]
        return mock.call(
            "PUT",
            resumable_url,
            data=payload,
            headers=expected_headers,
            timeout=timeout,
        )

    @staticmethod
    def _do_resumable_upload_call2(
        client,
        blob,
        content_type,
        data,
        resumable_url,
        total_bytes,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=None,
        checksum=None,
        crc32c_checksum_value=None,
        md5_checksum_value=None,
    ):
        # Third mock transport.request() does sends last chunk.
        content_range = f"bytes {blob.chunk_size:d}-{total_bytes - 1:d}/{total_bytes:d}"
        expected_headers = {
            **_get_default_headers(
                client._connection.user_agent, x_upload_content_type=content_type
            ),
            "content-type": content_type,
            "content-range": content_range,
        }
        if checksum == "crc32c":
            expected_headers["x-goog-hash"] = f"crc32c={crc32c_checksum_value}"
        elif checksum == "md5":
            expected_headers["x-goog-hash"] = f"md5={md5_checksum_value}"

        payload = data[blob.chunk_size :]
        return mock.call(
            "PUT",
            resumable_url,
            data=payload,
            headers=expected_headers,
            timeout=timeout,
        )

    def _do_resumable_helper(
        self,
        use_size=False,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        timeout=None,
        data_corruption=False,
        retry=None,
        checksum=None,  # None is also a valid value, when user decides to disable checksum validation.
    ):
        CHUNK_SIZE = 256 * 1024
        USER_AGENT = "testing 1.2.3"
        content_type = "text/html"
        # Data to be uploaded.
        data = b"<html>" + (b"A" * CHUNK_SIZE) + b"</html>"

        # Data calcuated offline and entered here. (Unit test best practice).
        crc32c_checksum_value = "mQ30hg=="
        md5_checksum_value = "wajHeg1f2Q2u9afI6fjPOw=="
        total_bytes = len(data)
        if use_size:
            size = total_bytes
        else:
            size = None

        # Create mocks to be checked for doing transport.
        resumable_url = "http://test.invalid?upload_id=and-then-there-was-1"
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            headers1 = {
                **_get_default_headers(USER_AGENT, content_type),
                "location": resumable_url,
            }
            headers2 = {
                **_get_default_headers(USER_AGENT, content_type),
                "range": f"bytes=0-{CHUNK_SIZE - 1:d}",
            }
            headers3 = _get_default_headers(USER_AGENT, content_type)
            transport, responses = self._make_resumable_transport(
                headers1,
                headers2,
                headers3,
                total_bytes,
                data_corruption=data_corruption,
                md5_checksum_value=md5_checksum_value,
                crc32c_checksum_value=crc32c_checksum_value,
            )

        # Create some mock arguments and call the method under test.
        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._connection.user_agent = USER_AGENT
        client._extra_headers = {}
        stream = io.BytesIO(data)

        bucket = _Bucket(name="yesterday")
        blob = self._make_one("blob-name", bucket=bucket)
        blob.chunk_size = blob._CHUNK_SIZE_MULTIPLE
        self.assertIsNotNone(blob.chunk_size)

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}

        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            response = blob._do_resumable_upload(
                client,
                stream,
                content_type,
                size,
                predefined_acl,
                if_generation_match,
                if_generation_not_match,
                if_metageneration_match,
                if_metageneration_not_match,
                checksum=checksum,
                retry=retry,
                **timeout_kwarg,
            )

            # Check the returned values.
            self.assertIs(response, responses[2])
            self.assertEqual(stream.tell(), total_bytes)

            # Check the mocks.
            call0 = self._do_resumable_upload_call0(
                client,
                blob,
                content_type,
                size=size,
                predefined_acl=predefined_acl,
                if_generation_match=if_generation_match,
                if_generation_not_match=if_generation_not_match,
                if_metageneration_match=if_metageneration_match,
                if_metageneration_not_match=if_metageneration_not_match,
                timeout=expected_timeout,
            )
            call1 = self._do_resumable_upload_call1(
                client,
                blob,
                content_type,
                data,
                resumable_url,
                size=size,
                predefined_acl=predefined_acl,
                if_generation_match=if_generation_match,
                if_generation_not_match=if_generation_not_match,
                if_metageneration_match=if_metageneration_match,
                if_metageneration_not_match=if_metageneration_not_match,
                timeout=expected_timeout,
            )
            call2 = self._do_resumable_upload_call2(
                client,
                blob,
                content_type,
                data,
                resumable_url,
                total_bytes,
                predefined_acl=predefined_acl,
                if_generation_match=if_generation_match,
                if_generation_not_match=if_generation_not_match,
                if_metageneration_match=if_metageneration_match,
                if_metageneration_not_match=if_metageneration_not_match,
                timeout=expected_timeout,
                checksum=checksum,
                crc32c_checksum_value=crc32c_checksum_value,
                md5_checksum_value=md5_checksum_value,
            )
        self.assertEqual(transport.request.mock_calls, [call0, call1, call2])

    def test__do_resumable_upload_with_custom_timeout(self):
        self._do_resumable_helper(timeout=9.58)

    def test__do_resumable_upload_no_size(self):
        self._do_resumable_helper()

    def test__do_resumable_upload_with_size(self):
        self._do_resumable_helper(use_size=True)

    def test__do_resumable_upload_with_size_with_crc32c_checksum(self):
        self._do_resumable_helper(use_size=True, checksum="crc32c")

    def test__do_resumable_upload_with_size_with_md5_checksum(self):
        self._do_resumable_helper(use_size=True, checksum="md5")

    def test__do_resumable_upload_with_retry(self):
        self._do_resumable_helper(retry=DEFAULT_RETRY)

    def test__do_resumable_upload_with_predefined_acl(self):
        self._do_resumable_helper(predefined_acl="private")

    def test__do_resumable_upload_with_data_corruption(self):
        with mock.patch("google.cloud.storage.blob.Blob.delete") as patch:
            try:
                self._do_resumable_helper(data_corruption=True)
            except Exception as e:
                self.assertTrue(patch.called)
                self.assertIsInstance(e, DataCorruption)

    def _do_upload_helper(
        self,
        chunk_size=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        size=None,
        timeout=None,
        retry=None,
    ):
        from google.cloud.storage.blob import _MAX_MULTIPART_SIZE

        blob = self._make_one("blob-name", bucket=None)

        # Create a fake response.
        response = mock.Mock(spec=["json"])
        response.json.return_value = mock.sentinel.json
        # Mock **both** helpers.
        blob._do_multipart_upload = mock.Mock(return_value=response, spec=[])
        blob._do_resumable_upload = mock.Mock(return_value=response, spec=[])

        if chunk_size is None:
            self.assertIsNone(blob.chunk_size)
        else:
            blob.chunk_size = chunk_size
            self.assertIsNotNone(blob.chunk_size)

        client = mock.sentinel.client
        stream = mock.sentinel.stream
        content_type = "video/mp4"
        if size is None:
            size = 12345654321

        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}

        # Make the request and check the mocks.
        created_json = blob._do_upload(
            client,
            stream,
            content_type,
            size,
            predefined_acl,
            if_generation_match,
            if_generation_not_match,
            if_metageneration_match,
            if_metageneration_not_match,
            checksum=None,
            retry=retry,
            **timeout_kwarg,
        )

        if retry is DEFAULT_RETRY_IF_GENERATION_SPECIFIED:
            retry = DEFAULT_RETRY if if_generation_match else None

        self.assertIs(created_json, mock.sentinel.json)
        response.json.assert_called_once_with()
        if size is not None and size <= _MAX_MULTIPART_SIZE:
            blob._do_multipart_upload.assert_called_once_with(
                client,
                stream,
                content_type,
                size,
                predefined_acl,
                if_generation_match,
                if_generation_not_match,
                if_metageneration_match,
                if_metageneration_not_match,
                timeout=expected_timeout,
                checksum=None,
                retry=retry,
                command=None,
            )
            blob._do_resumable_upload.assert_not_called()
        else:
            blob._do_multipart_upload.assert_not_called()
            blob._do_resumable_upload.assert_called_once_with(
                client,
                stream,
                content_type,
                size,
                predefined_acl,
                if_generation_match,
                if_generation_not_match,
                if_metageneration_match,
                if_metageneration_not_match,
                timeout=expected_timeout,
                checksum=None,
                retry=retry,
                command=None,
                crc32c_checksum_value=None,
            )

    def test__do_upload_uses_multipart(self):
        from google.cloud.storage.blob import _MAX_MULTIPART_SIZE

        self._do_upload_helper(size=_MAX_MULTIPART_SIZE)

    def test__do_upload_uses_multipart_w_custom_timeout(self):
        from google.cloud.storage.blob import _MAX_MULTIPART_SIZE

        self._do_upload_helper(size=_MAX_MULTIPART_SIZE, timeout=9.58)

    def test__do_upload_uses_resumable(self):
        from google.cloud.storage.blob import _MAX_MULTIPART_SIZE

        chunk_size = 256 * 1024  # 256KB
        self._do_upload_helper(chunk_size=chunk_size, size=_MAX_MULTIPART_SIZE + 1)

    def test__do_upload_uses_resumable_w_custom_timeout(self):
        from google.cloud.storage.blob import _MAX_MULTIPART_SIZE

        chunk_size = 256 * 1024  # 256KB
        self._do_upload_helper(
            chunk_size=chunk_size, size=_MAX_MULTIPART_SIZE + 1, timeout=9.58
        )

    def test__do_upload_with_retry(self):
        self._do_upload_helper(retry=DEFAULT_RETRY)

    def test__do_upload_with_conditional_retry_success(self):
        self._do_upload_helper(
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED, if_generation_match=123456
        )

    def test__do_upload_with_conditional_retry_failure(self):
        self._do_upload_helper(retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED)

    def _upload_from_file_helper(self, side_effect=None, **kwargs):
        blob = self._make_one("blob-name", bucket=None)
        # Mock low-level upload helper on blob (it is tested elsewhere).
        created_json = {"updated": "2017-01-01T09:09:09.081Z"}
        blob._do_upload = mock.Mock(return_value=created_json, spec=[])
        if side_effect is not None:
            blob._do_upload.side_effect = side_effect
        # Make sure `updated` is empty before the request.
        self.assertIsNone(blob.updated)

        data = b"data is here"
        stream = io.BytesIO(data)
        stream.seek(2)  # Not at zero.
        content_type = "font/woff"
        client = mock.sentinel.client
        predefined_acl = kwargs.get("predefined_acl", None)
        if_generation_match = kwargs.get("if_generation_match", None)
        if_generation_not_match = kwargs.get("if_generation_not_match", None)
        if_metageneration_match = kwargs.get("if_metageneration_match", None)
        if_metageneration_not_match = kwargs.get("if_metageneration_not_match", None)
        retry = kwargs.get("retry", DEFAULT_RETRY)
        ret_val = blob.upload_from_file(
            stream,
            size=len(data),
            content_type=content_type,
            client=client,
            checksum=None,
            **kwargs,
        )

        # Check the response and side-effects.
        self.assertIsNone(ret_val)
        new_updated = datetime.datetime(2017, 1, 1, 9, 9, 9, 81000, tzinfo=_UTC)
        self.assertEqual(blob.updated, new_updated)

        expected_timeout = kwargs.get("timeout", self._get_default_timeout())

        blob._do_upload.assert_called_once_with(
            client,
            stream,
            content_type,
            len(data),
            predefined_acl,
            if_generation_match,
            if_generation_not_match,
            if_metageneration_match,
            if_metageneration_not_match,
            timeout=expected_timeout,
            checksum=None,
            retry=retry,
            command=None,
            crc32c_checksum_value=None,
        )
        return stream

    def test_upload_from_file_success(self):
        stream = self._upload_from_file_helper(predefined_acl="private")
        assert stream.tell() == 2

    def test_upload_from_file_with_retry(self):
        self._upload_from_file_helper(retry=DEFAULT_RETRY)

    def test_upload_from_file_with_rewind(self):
        stream = self._upload_from_file_helper(rewind=True)
        assert stream.tell() == 0

    def test_upload_from_file_with_custom_timeout(self):
        self._upload_from_file_helper(timeout=9.58)

    def test_upload_from_file_failure(self):
        import requests

        from google.cloud import exceptions

        message = "Someone is already in this spot."
        response = requests.Response()
        response.status_code = http.client.CONFLICT
        response.request = requests.Request("POST", "http://example.com").prepare()
        side_effect = InvalidResponse(response, message)

        with self.assertRaises(exceptions.Conflict) as exc_info:
            self._upload_from_file_helper(side_effect=side_effect)

        self.assertIn(message, exc_info.exception.message)
        self.assertEqual(exc_info.exception.errors, [])

    def _do_upload_mock_call_helper(
        self,
        blob,
        client,
        content_type,
        size,
        timeout=None,
        retry=None,
    ):
        self.assertEqual(blob._do_upload.call_count, 1)
        mock_call = blob._do_upload.mock_calls[0]
        call_name, pos_args, kwargs = mock_call
        self.assertEqual(call_name, "")
        self.assertEqual(len(pos_args), 9)
        self.assertEqual(pos_args[0], client)
        self.assertEqual(pos_args[2], content_type)
        self.assertEqual(pos_args[3], size)
        self.assertIsNone(pos_args[4])  # predefined_acl
        self.assertIsNone(pos_args[5])  # if_generation_match
        self.assertIsNone(pos_args[6])  # if_generation_not_match
        self.assertIsNone(pos_args[7])  # if_metageneration_match
        self.assertIsNone(pos_args[8])  # if_metageneration_not_match

        expected_timeout = self._get_default_timeout() if timeout is None else timeout
        if not retry:
            retry = DEFAULT_RETRY
        self.assertEqual(
            kwargs,
            {
                "timeout": expected_timeout,
                "crc32c_checksum_value": None,
                "checksum": None,
                "retry": retry,
                "command": None,
            },
        )

        return pos_args[1]

    def test_upload_from_filename(self):
        from google.cloud._testing import _NamedTemporaryFile

        blob = self._make_one("blob-name", bucket=None)
        # Mock low-level upload helper on blob (it is tested elsewhere).
        created_json = {"metadata": {"mint": "ice-cream"}}
        blob._do_upload = mock.Mock(return_value=created_json, spec=[])
        # Make sure `metadata` is empty before the request.
        self.assertIsNone(blob.metadata)

        data = b"soooo much data"
        content_type = "image/svg+xml"
        client = mock.sentinel.client
        with _NamedTemporaryFile() as temp:
            with open(temp.name, "wb") as file_obj:
                file_obj.write(data)

            ret_val = blob.upload_from_filename(
                temp.name, content_type=content_type, client=client, checksum=None
            )

        # Check the response and side-effects.
        self.assertIsNone(ret_val)
        self.assertEqual(blob.metadata, created_json["metadata"])

        # Check the mock.
        stream = self._do_upload_mock_call_helper(blob, client, content_type, len(data))
        self.assertTrue(stream.closed)
        self.assertEqual(stream.mode, "rb")
        self.assertEqual(stream.name, temp.name)

    def test_upload_from_filename_with_retry(self):
        from google.cloud._testing import _NamedTemporaryFile

        blob = self._make_one("blob-name", bucket=None)
        # Mock low-level upload helper on blob (it is tested elsewhere).
        created_json = {"metadata": {"mint": "ice-cream"}}
        blob._do_upload = mock.Mock(return_value=created_json, spec=[])
        # Make sure `metadata` is empty before the request.
        self.assertIsNone(blob.metadata)

        data = b"soooo much data"
        content_type = "image/svg+xml"
        client = mock.sentinel.client
        with _NamedTemporaryFile() as temp:
            with open(temp.name, "wb") as file_obj:
                file_obj.write(data)

            ret_val = blob.upload_from_filename(
                temp.name,
                content_type=content_type,
                client=client,
                retry=DEFAULT_RETRY,
                checksum=None,
            )

        # Check the response and side-effects.
        self.assertIsNone(ret_val)
        self.assertEqual(blob.metadata, created_json["metadata"])

        # Check the mock.
        stream = self._do_upload_mock_call_helper(
            blob, client, content_type, len(data), retry=DEFAULT_RETRY
        )
        self.assertTrue(stream.closed)
        self.assertEqual(stream.mode, "rb")
        self.assertEqual(stream.name, temp.name)

    def test_upload_from_filename_w_custom_timeout(self):
        from google.cloud._testing import _NamedTemporaryFile

        blob = self._make_one("blob-name", bucket=None)
        # Mock low-level upload helper on blob (it is tested elsewhere).
        created_json = {"metadata": {"mint": "ice-cream"}}
        blob._do_upload = mock.Mock(return_value=created_json, spec=[])
        # Make sure `metadata` is empty before the request.
        self.assertIsNone(blob.metadata)

        data = b"soooo much data"
        content_type = "image/svg+xml"
        client = mock.sentinel.client
        with _NamedTemporaryFile() as temp:
            with open(temp.name, "wb") as file_obj:
                file_obj.write(data)

            blob.upload_from_filename(
                temp.name,
                content_type=content_type,
                client=client,
                timeout=9.58,
                checksum=None,
            )

        # Check the mock.
        self._do_upload_mock_call_helper(
            blob, client, content_type, len(data), timeout=9.58
        )

    def _upload_from_string_helper(self, data, **kwargs):
        from google.cloud._helpers import _to_bytes

        blob = self._make_one("blob-name", bucket=None)

        # Mock low-level upload helper on blob (it is tested elsewhere).
        created_json = {"componentCount": "5"}
        blob._do_upload = mock.Mock(return_value=created_json, spec=[])
        # Make sure `metadata` is empty before the request.
        self.assertIsNone(blob.component_count)

        client = mock.sentinel.client
        ret_val = blob.upload_from_string(data, client=client, checksum=None, **kwargs)

        # Check the response and side-effects.
        self.assertIsNone(ret_val)
        self.assertEqual(blob.component_count, 5)

        extra_kwargs = {}
        if "retry" in kwargs:
            extra_kwargs["retry"] = kwargs["retry"]
        else:
            extra_kwargs["retry"] = DEFAULT_RETRY
        # Check the mock.
        payload = _to_bytes(data, encoding="utf-8")
        stream = self._do_upload_mock_call_helper(
            blob,
            client,
            "text/plain",
            len(payload),
            kwargs.get("timeout", self._get_default_timeout()),
            **extra_kwargs,
        )
        self.assertIsInstance(stream, io.BytesIO)
        self.assertEqual(stream.getvalue(), payload)

    def test_upload_from_string_w_custom_timeout(self):
        data = b"XB]jb\xb8tad\xe0"
        self._upload_from_string_helper(data, timeout=9.58)

    def test_upload_from_string_w_bytes(self):
        data = b"XB]jb\xb8tad\xe0"
        self._upload_from_string_helper(data)

    def test_upload_from_string_w_text(self):
        data = "\N{SNOWMAN} \N{SAILBOAT}"
        self._upload_from_string_helper(data)

    def test_upload_from_string_w_text_w_retry(self):
        data = "\N{SNOWMAN} \N{SAILBOAT}"
        self._upload_from_string_helper(data, retry=DEFAULT_RETRY)

    def _create_resumable_upload_session_helper(
        self,
        origin=None,
        side_effect=None,
        timeout=None,
        predefined_acl=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        retry=None,
        client=None,
    ):
        bucket = _Bucket(name="alex-trebek")
        blob = self._make_one("blob-name", bucket=bucket)
        chunk_size = 99 * blob._CHUNK_SIZE_MULTIPLE
        blob.chunk_size = chunk_size
        resumable_url = "http://test.invalid?upload_id=clean-up-everybody"
        content_type = "text/plain"
        size = 10000
        transport = None

        if not client:
            # Create mocks to be checked for doing transport.
            response_headers = {"location": resumable_url}
            transport = self._mock_transport(http.client.OK, response_headers)

            # Create some mock arguments and call the method under test.
            client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
            client._connection.API_BASE_URL = "https://storage.googleapis.com"
            client._connection.user_agent = "testing 1.2.3"
            client._extra_headers = {}

        if transport is None:
            transport = client._http
        if side_effect is not None:
            transport.request.side_effect = side_effect
        if timeout is None:
            expected_timeout = self._get_default_timeout()
            timeout_kwarg = {}
        else:
            expected_timeout = timeout
            timeout_kwarg = {"timeout": timeout}
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            new_url = blob.create_resumable_upload_session(
                content_type=content_type,
                size=size,
                origin=origin,
                client=client,
                predefined_acl=predefined_acl,
                if_generation_match=if_generation_match,
                if_generation_not_match=if_generation_not_match,
                if_metageneration_match=if_metageneration_match,
                if_metageneration_not_match=if_metageneration_not_match,
                retry=retry,
                **timeout_kwarg,
            )

        # Check the returned value and (lack of) side-effect.
        self.assertEqual(new_url, resumable_url)
        self.assertEqual(blob.chunk_size, chunk_size)

        # Check the mocks.
        upload_url = (
            "https://storage.googleapis.com/upload/storage/v1" + bucket.path + "/o"
        )

        qs_params = [("uploadType", "resumable")]
        if predefined_acl is not None:
            qs_params.append(("predefinedAcl", predefined_acl))

        if if_generation_match is not None:
            qs_params.append(("ifGenerationMatch", if_generation_match))

        if if_generation_not_match is not None:
            qs_params.append(("ifGenerationNotMatch", if_generation_not_match))

        if if_metageneration_match is not None:
            qs_params.append(("ifMetagenerationMatch", if_metageneration_match))

        if if_metageneration_not_match is not None:
            qs_params.append(("ifMetaGenerationNotMatch", if_metageneration_not_match))

        upload_url += "?" + urlencode(qs_params)
        payload = b'{"name": "blob-name"}'
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            expected_headers = {
                **_get_default_headers(
                    client._connection.user_agent, x_upload_content_type=content_type
                ),
                **client._extra_headers,
                "x-upload-content-length": str(size),
                "x-upload-content-type": content_type,
            }
        if origin is not None:
            expected_headers["Origin"] = origin
        transport.request.assert_called_once_with(
            "POST",
            upload_url,
            data=payload,
            headers=expected_headers,
            timeout=expected_timeout,
        )

    def test_create_resumable_upload_session(self):
        self._create_resumable_upload_session_helper()

    def test_create_resumable_upload_session_with_custom_timeout(self):
        self._create_resumable_upload_session_helper(timeout=9.58)

    def test_create_resumable_upload_session_with_origin(self):
        self._create_resumable_upload_session_helper(origin="http://google.com")

    def test_create_resumable_upload_session_with_predefined_acl(self):
        self._create_resumable_upload_session_helper(predefined_acl="private")

    def test_create_resumable_upload_session_with_generation_match(self):
        self._create_resumable_upload_session_helper(
            if_generation_match=123456, if_metageneration_match=2
        )

    def test_create_resumable_upload_session_with_generation_not_match(self):
        self._create_resumable_upload_session_helper(
            if_generation_not_match=0, if_metageneration_not_match=3
        )

    def test_create_resumable_upload_session_with_conditional_retry_success(self):
        self._create_resumable_upload_session_helper(
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED, if_generation_match=123456
        )

    def test_create_resumable_upload_session_with_conditional_retry_failure(self):
        self._create_resumable_upload_session_helper(
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED
        )

    def test_create_resumable_upload_session_with_failure(self):
        from google.cloud import exceptions

        message = "5-oh-3 woe is me."
        response = self._mock_requests_response(
            status_code=http.client.SERVICE_UNAVAILABLE, headers={}
        )
        side_effect = InvalidResponse(response, message)

        with self.assertRaises(exceptions.ServiceUnavailable) as exc_info:
            self._create_resumable_upload_session_helper(side_effect=side_effect)

        self.assertIn(message, exc_info.exception.message)
        self.assertEqual(exc_info.exception.errors, [])

    def test_create_resumable_upload_session_with_client(self):
        resumable_url = "http://test.invalid?upload_id=clean-up-everybody"
        response_headers = {"location": resumable_url}
        transport = self._mock_transport(http.client.OK, response_headers)
        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._extra_headers = {}
        self._create_resumable_upload_session_helper(client=client)

    def test_create_resumable_upload_session_with_client_custom_headers(self):
        custom_headers = {
            "x-goog-custom-audit-foo": "bar",
            "x-goog-custom-audit-user": "baz",
        }
        resumable_url = "http://test.invalid?upload_id=clean-up-everybody"
        response_headers = {"location": resumable_url}
        transport = self._mock_transport(http.client.OK, response_headers)
        client = mock.Mock(_http=transport, _connection=_Connection, spec=["_http"])
        client._connection.API_BASE_URL = "https://storage.googleapis.com"
        client._extra_headers = custom_headers
        self._create_resumable_upload_session_helper(client=client)

    def test_get_iam_policy_defaults(self):
        from google.api_core.iam import Policy

        from google.cloud.storage.iam import (
            STORAGE_EDITOR_ROLE,
            STORAGE_OWNER_ROLE,
            STORAGE_VIEWER_ROLE,
        )

        blob_name = "blob-name"
        path = f"/b/name/o/{blob_name}"
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
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)

        policy = blob.get_iam_policy()

        self.assertIsInstance(policy, Policy)
        self.assertEqual(policy.etag, api_response["etag"])
        self.assertEqual(policy.version, api_response["version"])
        self.assertEqual(dict(policy), expected_policy)

        expected_path = f"{path}/iam"
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

        blob_name = "blob-name"
        user_project = "user-project-123"
        timeout = 42
        path = f"/b/name/o/{blob_name}"
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
        bucket = _Bucket(client=client, user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)

        policy = blob.get_iam_policy(timeout=42)

        self.assertIsInstance(policy, Policy)
        self.assertEqual(policy.etag, api_response["etag"])
        self.assertEqual(policy.version, api_response["version"])
        self.assertEqual(dict(policy), expected_policy)

        expected_path = f"{path}/iam"
        expected_query_params = {"userProject": user_project}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_get_iam_policy_w_requested_policy_version(self):
        from google.cloud.storage.iam import STORAGE_OWNER_ROLE

        blob_name = "blob-name"
        path = f"/b/name/o/{blob_name}"
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
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)

        policy = blob.get_iam_policy(requested_policy_version=version)

        self.assertEqual(policy.version, version)

        expected_path = f"{path}/iam"
        expected_query_params = {"optionsRequestedPolicyVersion": version}
        client._get_resource.assert_called_once_with(
            expected_path,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
            _target_object=None,
        )

    def test_set_iam_policy(self):
        import operator

        from google.api_core.iam import Policy

        from google.cloud.storage.iam import (
            STORAGE_EDITOR_ROLE,
            STORAGE_OWNER_ROLE,
            STORAGE_VIEWER_ROLE,
        )

        blob_name = "blob-name"
        path = f"/b/name/o/{blob_name}"
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
        api_response = {"etag": etag, "version": version, "bindings": bindings}
        policy = Policy()
        for binding in bindings:
            policy[binding["role"]] = binding["members"]

        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)

        returned = blob.set_iam_policy(policy)

        self.assertEqual(returned.etag, etag)
        self.assertEqual(returned.version, version)
        self.assertEqual(dict(returned), dict(policy))

        expected_path = f"{path}/iam"
        expected_data = {
            "resourceId": path,
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

    def test_set_iam_policy_w_user_project_w_explicit_client_w_timeout_retry(self):
        from google.api_core.iam import Policy

        blob_name = "blob-name"
        user_project = "user-project-123"
        path = f"/b/name/o/{blob_name}"
        etag = "DEADBEEF"
        version = 1
        bindings = []
        policy = Policy()

        api_response = {"etag": etag, "version": version, "bindings": bindings}
        client = mock.Mock(spec=["_put_resource"])
        client._put_resource.return_value = api_response
        bucket = _Bucket(client=None, user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)
        timeout = 42
        retry = mock.Mock(spec=[])

        returned = blob.set_iam_policy(
            policy,
            client=client,
            timeout=timeout,
            retry=retry,
        )

        self.assertEqual(returned.etag, etag)
        self.assertEqual(returned.version, version)
        self.assertEqual(dict(returned), dict(policy))

        expected_path = f"{path}/iam"
        expected_data = {  # bindings omitted
            "resourceId": path,
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

    def test_test_iam_permissions_defaults(self):
        from google.cloud.storage.iam import (
            STORAGE_BUCKETS_GET,
            STORAGE_BUCKETS_UPDATE,
            STORAGE_OBJECTS_LIST,
        )

        blob_name = "blob-name"
        permissions = [
            STORAGE_OBJECTS_LIST,
            STORAGE_BUCKETS_GET,
            STORAGE_BUCKETS_UPDATE,
        ]
        expected = permissions[1:]
        api_response = {"permissions": expected}
        client = mock.Mock(spec=["_get_resource"])
        client._get_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)

        found = blob.test_iam_permissions(permissions)

        self.assertEqual(found, expected)

        expected_path = f"/b/name/o/{blob_name}/iam/testPermissions"
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

        blob_name = "blob-name"
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
        bucket = _Bucket(client=client, user_project=user_project)
        blob = self._make_one(blob_name, bucket=bucket)

        found = blob.test_iam_permissions(permissions, timeout=timeout, retry=retry)

        self.assertEqual(found, expected)

        expected_path = f"/b/name/o/{blob_name}/iam/testPermissions"
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

    def test_make_public_w_defaults(self):
        from google.cloud.storage.acl import _ACLEntity

        blob_name = "blob-name"
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]
        api_response = {"acl": permissive}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.acl.loaded = True

        blob.make_public()

        self.assertEqual(list(blob.acl), permissive)

        expected_patch_data = {"acl": permissive}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            blob.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_make_public_w_timeout(self):
        from google.cloud.storage.acl import _ACLEntity

        blob_name = "blob-name"
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]
        api_response = {"acl": permissive}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.acl.loaded = True
        timeout = 42

        blob.make_public(timeout=timeout)

        self.assertEqual(list(blob.acl), permissive)

        expected_patch_data = {"acl": permissive}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            blob.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY,
        )

    def test_make_public_w_preconditions(self):
        from google.cloud.storage.acl import _ACLEntity

        blob_name = "blob-name"
        permissive = [{"entity": "allUsers", "role": _ACLEntity.READER_ROLE}]
        api_response = {"acl": permissive}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.acl.loaded = True

        blob.make_public(if_metageneration_match=2, if_metageneration_not_match=1)

        self.assertEqual(list(blob.acl), permissive)

        expected_patch_data = {"acl": permissive}
        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            blob.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_make_private_w_defaults(self):
        blob_name = "blob-name"
        no_permissions = []
        api_response = {"acl": no_permissions}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.acl.loaded = True

        blob.make_private()

        self.assertEqual(list(blob.acl), no_permissions)

        expected_patch_data = {"acl": no_permissions}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            blob.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_make_private_w_timeout(self):
        blob_name = "blob-name"
        no_permissions = []
        api_response = {"acl": no_permissions}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.acl.loaded = True
        timeout = 42

        blob.make_private(timeout=timeout)

        self.assertEqual(list(blob.acl), no_permissions)

        expected_patch_data = {"acl": no_permissions}
        expected_query_params = {"projection": "full"}
        client._patch_resource.assert_called_once_with(
            blob.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY,
        )

    def test_make_private_w_preconditions(self):
        blob_name = "blob-name"
        no_permissions = []
        api_response = {"acl": no_permissions}
        client = mock.Mock(spec=["_patch_resource"])
        client._patch_resource.return_value = api_response
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.acl.loaded = True

        blob.make_private(if_metageneration_match=2, if_metageneration_not_match=1)

        self.assertEqual(list(blob.acl), no_permissions)

        expected_patch_data = {"acl": no_permissions}
        expected_query_params = {
            "projection": "full",
            "ifMetagenerationMatch": 2,
            "ifMetagenerationNotMatch": 1,
        }
        client._patch_resource.assert_called_once_with(
            blob.path,
            expected_patch_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY,
        )

    def test_compose_wo_content_type_set(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)
        # no destination.content_type set

        destination.compose(sources=[source_1, source_2])

        self.assertIsNone(destination.content_type)

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {},
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_compose_minimal_w_user_project_w_timeout(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        api_response = {"etag": "DEADBEEF"}
        user_project = "user-project-123"
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client, user_project=user_project)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)
        destination.content_type = "text/plain"
        timeout = 42

        destination.compose(sources=[source_1, source_2], timeout=timeout)

        self.assertEqual(destination.etag, "DEADBEEF")

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {"contentType": "text/plain"},
        }
        expected_query_params = {"userProject": user_project}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_compose_w_additional_property_changes_w_retry(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        api_response = {"etag": "DEADBEEF"}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)
        destination.content_type = "text/plain"
        destination.content_language = "en-US"
        destination.metadata = {"my-key": "my-value"}
        retry = mock.Mock(spec=[])

        destination.compose(sources=[source_1, source_2], retry=retry)

        self.assertEqual(destination.etag, "DEADBEEF")

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {
                "contentType": "text/plain",
                "contentLanguage": "en-US",
                "metadata": {"my-key": "my-value"},
            },
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=destination,
        )

    def test_compose_w_source_generation_match(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        api_response = {}
        source_generation_numbers = [6, 9]

        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)

        destination = self._make_one(destination_name, bucket=bucket)
        destination.compose(
            sources=[source_1, source_2],
            if_source_generation_match=source_generation_numbers,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {
                    "name": source_1.name,
                    "generation": source_1.generation,
                    "objectPreconditions": {
                        "ifGenerationMatch": source_generation_numbers[0],
                    },
                },
                {
                    "name": source_2.name,
                    "generation": source_2.generation,
                    "objectPreconditions": {
                        "ifGenerationMatch": source_generation_numbers[1],
                    },
                },
            ],
            "destination": {},
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_compose_w_source_generation_match_bad_length(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        source_generation_numbers = [6]
        client = mock.Mock(spec=["_post_resource"])
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)

        destination = self._make_one(destination_name, bucket=bucket)

        with self.assertRaises(ValueError):
            destination.compose(
                sources=[source_1, source_2],
                if_source_generation_match=source_generation_numbers,
            )

        client._post_resource.assert_not_called()

    def test_compose_w_source_generation_match_nones(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        source_generation_numbers = [6, None]
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)

        destination.compose(
            sources=[source_1, source_2],
            if_source_generation_match=source_generation_numbers,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {
                    "name": source_1.name,
                    "generation": source_1.generation,
                    "objectPreconditions": {
                        "ifGenerationMatch": source_generation_numbers[0],
                    },
                },
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {},
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_compose_w_generation_match(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        generation_number = 1
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)

        destination.compose(
            sources=[source_1, source_2],
            if_generation_match=generation_number,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {},
        }
        expected_query_params = {"ifGenerationMatch": generation_number}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    @mock.patch("warnings.warn")
    def test_compose_w_if_generation_match_list_w_warning(self, mock_warn):
        from google.cloud.storage.blob import _COMPOSE_IF_GENERATION_LIST_DEPRECATED

        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        api_response = {}
        generation_numbers = [6, 9]

        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)

        destination = self._make_one(destination_name, bucket=bucket)
        destination.compose(
            sources=[source_1, source_2],
            if_generation_match=generation_numbers,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {
                    "name": source_1_name,
                    "generation": None,
                    "objectPreconditions": {
                        "ifGenerationMatch": generation_numbers[0],
                    },
                },
                {
                    "name": source_2_name,
                    "generation": None,
                    "objectPreconditions": {
                        "ifGenerationMatch": generation_numbers[1],
                    },
                },
            ],
            "destination": {},
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

        mock_warn.assert_any_call(
            _COMPOSE_IF_GENERATION_LIST_DEPRECATED,
            DeprecationWarning,
            stacklevel=2,
        )

    @mock.patch("warnings.warn")
    def test_compose_w_if_generation_match_and_if_s_generation_match(self, mock_warn):
        from google.cloud.storage.blob import _COMPOSE_IF_GENERATION_LIST_DEPRECATED

        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        source_generation_numbers = [6, 8]
        client = mock.Mock(spec=["_post_resource"])
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)

        destination = self._make_one(destination_name, bucket=bucket)

        with self.assertRaises(ValueError):
            destination.compose(
                sources=[source_1, source_2],
                if_generation_match=source_generation_numbers,
                if_source_generation_match=source_generation_numbers,
            )

        client._post_resource.assert_not_called()

        mock_warn.assert_any_call(
            _COMPOSE_IF_GENERATION_LIST_DEPRECATED,
            DeprecationWarning,
            stacklevel=2,
        )

    @mock.patch("warnings.warn")
    def test_compose_w_if_metageneration_match_list_w_warning(self, mock_warn):
        from google.cloud.storage.blob import _COMPOSE_IF_METAGENERATION_LIST_DEPRECATED

        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        metageneration_number = [6]
        client = mock.Mock(spec=["_post_resource"])
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)

        destination = self._make_one(destination_name, bucket=bucket)

        destination.compose(
            sources=[source_1, source_2],
            if_metageneration_match=metageneration_number,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1_name, "generation": None},
                {"name": source_2_name, "generation": None},
            ],
            "destination": {},
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

        mock_warn.assert_any_call(
            _COMPOSE_IF_METAGENERATION_LIST_DEPRECATED,
            DeprecationWarning,
            stacklevel=2,
        )

    def test_compose_w_metageneration_match(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        metageneration_number = 1
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)

        destination.compose(
            sources=[source_1, source_2],
            if_metageneration_match=metageneration_number,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {},
        }
        expected_query_params = {"ifMetagenerationMatch": metageneration_number}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_compose_w_delete_source_objects(self):
        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        delete_source_objects = True
        api_response = {}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)

        destination.compose(
            sources=[source_1, source_2],
            delete_source_objects=delete_source_objects,
        )

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {},
            "deleteSourceObjects": delete_source_objects,
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_compose_w_destination_contexts(self):
        from google.cloud.storage.blob import (
            ObjectContexts,
            ObjectCustomContextPayload,
        )

        source_1_name = "source-1"
        source_2_name = "source-2"
        destination_name = "destination"
        api_response = {"contexts": {"custom": {"foo": {"value": "bar"}}}}
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source_1 = self._make_one(source_1_name, bucket=bucket)
        source_2 = self._make_one(source_2_name, bucket=bucket)
        destination = self._make_one(destination_name, bucket=bucket)

        payload = ObjectCustomContextPayload(value="bar")
        contexts = ObjectContexts(None, custom={"foo": payload})

        destination.compose(
            sources=[source_1, source_2],
            destination_contexts=contexts,
        )

        self.assertEqual(destination.contexts.custom["foo"].value, "bar")

        expected_path = f"/b/name/o/{destination_name}/compose"
        expected_data = {
            "sourceObjects": [
                {"name": source_1.name, "generation": source_1.generation},
                {"name": source_2.name, "generation": source_2.generation},
            ],
            "destination": {"contexts": {"custom": {"foo": {"value": "bar"}}}},
        }
        expected_query_params = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=destination,
        )

    def test_rewrite_w_response_wo_resource(self):
        source_name = "source"
        dest_name = "dest"
        other_bucket_name = "other-bucket"
        bytes_rewritten = 33
        object_size = 52
        rewrite_token = "TOKEN"
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": False,
            "rewriteToken": rewrite_token,
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source_bucket = _Bucket(client=client)
        source_blob = self._make_one(source_name, bucket=source_bucket)
        dest_bucket = _Bucket(client=client, name=other_bucket_name)
        dest_blob = self._make_one(dest_name, bucket=dest_bucket)

        token, rewritten, size = dest_blob.rewrite(source_blob)

        self.assertEqual(token, rewrite_token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = "/b/%s/o/%s/rewriteTo/b/%s/o/%s" % (
            source_bucket.name,
            source_name,
            other_bucket_name,
            dest_name,
        )
        expected_data = {}
        expected_query_params = {}
        expected_headers = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest_blob,
        )

    def test_rewrite_w_generations_w_timeout(self):
        source_name = "source"
        source_generation = 22
        dest_name = "dest"
        other_bucket_name = "other-bucket"
        dest_generation = 23
        bytes_rewritten = 33
        object_size = 52
        rewrite_token = "TOKEN"
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": False,
            "rewriteToken": rewrite_token,
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source_bucket = _Bucket(client=client)
        source_blob = self._make_one(
            source_name, bucket=source_bucket, generation=source_generation
        )
        dest_bucket = _Bucket(client=client, name=other_bucket_name)
        dest_blob = self._make_one(
            dest_name, bucket=dest_bucket, generation=dest_generation
        )
        timeout = 42

        token, rewritten, size = dest_blob.rewrite(source_blob, timeout=timeout)

        self.assertEqual(token, rewrite_token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = "/b/%s/o/%s/rewriteTo/b/%s/o/%s" % (
            source_bucket.name,
            source_name,
            other_bucket_name,
            dest_name,
        )
        expected_data = {"generation": dest_generation}
        expected_query_params = {"sourceGeneration": source_generation}
        expected_headers = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=timeout,
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest_blob,
        )

    def test_rewrite_w_generation_match_w_retry(self):
        source_name = "source"
        source_generation = 42
        dest_name = "dest"
        other_bucket_name = "other-bucket"
        dest_generation = 16
        bytes_rewritten = 33
        object_size = 52
        rewrite_token = "TOKEN"
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": False,
            "rewriteToken": rewrite_token,
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source_bucket = _Bucket(client=client)
        source_blob = self._make_one(
            source_name, bucket=source_bucket, generation=source_generation
        )
        dest_bucket = _Bucket(client=client, name=other_bucket_name)
        dest_blob = self._make_one(
            dest_name, bucket=dest_bucket, generation=dest_generation
        )
        retry = mock.Mock(spec=[])

        token, rewritten, size = dest_blob.rewrite(
            source_blob,
            if_generation_match=dest_blob.generation,
            if_source_generation_match=source_blob.generation,
            retry=retry,
        )

        self.assertEqual(token, rewrite_token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = "/b/%s/o/%s/rewriteTo/b/%s/o/%s" % (
            source_bucket.name,
            source_name,
            other_bucket_name,
            dest_name,
        )
        expected_data = {"generation": dest_generation}
        expected_query_params = {
            "ifSourceGenerationMatch": source_generation,
            "ifGenerationMatch": dest_generation,
            "sourceGeneration": source_generation,
        }
        expected_headers = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=retry,
            _target_object=dest_blob,
        )

    def test_rewrite_other_bucket_other_name_no_encryption_partial(self):
        source_name = "source"
        dest_name = "dest"
        other_bucket_name = "other-bucket"
        bytes_rewritten = 33
        object_size = 52
        rewrite_token = "TOKEN"
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": False,
            "rewriteToken": rewrite_token,
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        source_bucket = _Bucket(client=client)
        source_blob = self._make_one(source_name, bucket=source_bucket)
        dest_bucket = _Bucket(client=client, name=other_bucket_name)
        dest_blob = self._make_one(dest_name, bucket=dest_bucket)

        token, rewritten, size = dest_blob.rewrite(source_blob)

        self.assertEqual(token, rewrite_token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = "/b/name/o/%s/rewriteTo/b/%s/o/%s" % (
            source_name,
            other_bucket_name,
            dest_name,
        )
        expected_query_params = {}
        expected_data = {}
        expected_headers = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest_blob,
        )

    def test_rewrite_same_name_no_old_key_new_key_done_w_user_project(self):
        blob_name = "blob"
        user_project = "user-project-123"
        key = b"01234567890123456789012345678901"  # 32 bytes
        key_b64 = base64.b64encode(key).rstrip().decode("ascii")
        key_hash = hashlib.sha256(key).digest()
        key_hash_b64 = base64.b64encode(key_hash).rstrip().decode("ascii")
        bytes_rewritten = object_size = 52
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": True,
            "resource": {"etag": "DEADBEEF"},
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client, user_project=user_project)
        plain = self._make_one(blob_name, bucket=bucket)
        encrypted = self._make_one(blob_name, bucket=bucket, encryption_key=key)

        token, rewritten, size = encrypted.rewrite(plain)

        self.assertIsNone(token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = f"/b/name/o/{blob_name}/rewriteTo/b/name/o/{blob_name}"
        expected_query_params = {"userProject": user_project}
        expected_data = {}
        expected_headers = {
            "X-Goog-Encryption-Algorithm": "AES256",
            "X-Goog-Encryption-Key": key_b64,
            "X-Goog-Encryption-Key-Sha256": key_hash_b64,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=encrypted,
        )

    def test_rewrite_same_name_no_key_new_key_w_token(self):
        blob_name = "blob"
        source_key = b"01234567890123456789012345678901"  # 32 bytes
        source_key_b64 = base64.b64encode(source_key).rstrip().decode("ascii")
        source_key_hash = hashlib.sha256(source_key).digest()
        source_key_hash_b64 = base64.b64encode(source_key_hash).rstrip().decode("ascii")
        dest_key = b"90123456789012345678901234567890"  # 32 bytes
        dest_key_b64 = base64.b64encode(dest_key).rstrip().decode("ascii")
        dest_key_hash = hashlib.sha256(dest_key).digest()
        dest_key_hash_b64 = base64.b64encode(dest_key_hash).rstrip().decode("ascii")
        previous_token = "TOKEN"
        bytes_rewritten = object_size = 52
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": True,
            "resource": {"etag": "DEADBEEF"},
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source = self._make_one(blob_name, bucket=bucket, encryption_key=source_key)
        dest = self._make_one(blob_name, bucket=bucket, encryption_key=dest_key)

        token, rewritten, size = dest.rewrite(source, token=previous_token)

        self.assertIsNone(token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = f"/b/name/o/{blob_name}/rewriteTo/b/name/o/{blob_name}"
        expected_data = {}
        expected_query_params = {"rewriteToken": previous_token}
        expected_headers = {
            "X-Goog-Copy-Source-Encryption-Algorithm": "AES256",
            "X-Goog-Copy-Source-Encryption-Key": source_key_b64,
            "X-Goog-Copy-Source-Encryption-Key-Sha256": source_key_hash_b64,
            "X-Goog-Encryption-Algorithm": "AES256",
            "X-Goog-Encryption-Key": dest_key_b64,
            "X-Goog-Encryption-Key-Sha256": dest_key_hash_b64,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest,
        )

    def test_rewrite_same_name_w_old_key_new_kms_key(self):
        blob_name = "blob"
        source_key = b"01234567890123456789012345678901"  # 32 bytes
        source_key_b64 = base64.b64encode(source_key).rstrip().decode("ascii")
        source_key_hash = hashlib.sha256(source_key).digest()
        source_key_hash_b64 = base64.b64encode(source_key_hash).rstrip().decode("ascii")
        dest_kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
        )
        bytes_rewritten = object_size = 42
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": True,
            "resource": {"etag": "DEADBEEF"},
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source = self._make_one(blob_name, bucket=bucket, encryption_key=source_key)
        dest = self._make_one(blob_name, bucket=bucket, kms_key_name=dest_kms_resource)

        token, rewritten, size = dest.rewrite(source)

        self.assertIsNone(token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = f"/b/name/o/{blob_name}/rewriteTo/b/name/o/{blob_name}"
        expected_data = {"kmsKeyName": dest_kms_resource}
        expected_query_params = {"destinationKmsKeyName": dest_kms_resource}
        expected_headers = {
            "X-Goog-Copy-Source-Encryption-Algorithm": "AES256",
            "X-Goog-Copy-Source-Encryption-Key": source_key_b64,
            "X-Goog-Copy-Source-Encryption-Key-Sha256": source_key_hash_b64,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest,
        )

    def test_rewrite_same_name_w_kms_key_w_version(self):
        blob_name = "blob"
        source_key = b"01234567890123456789012345678901"  # 32 bytes
        source_key_b64 = base64.b64encode(source_key).rstrip().decode("ascii")
        source_key_hash = hashlib.sha256(source_key).digest()
        source_key_hash_b64 = base64.b64encode(source_key_hash).rstrip().decode("ascii")
        dest_kms_resource = (
            "projects/test-project-123/"
            "locations/us/"
            "keyRings/test-ring/"
            "cryptoKeys/test-key"
            "cryptoKeyVersions/1"
        )
        bytes_rewritten = object_size = 42
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": True,
            "resource": {"etag": "DEADBEEF"},
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source = self._make_one(blob_name, bucket=bucket, encryption_key=source_key)
        dest = self._make_one(blob_name, bucket=bucket, kms_key_name=dest_kms_resource)

        token, rewritten, size = dest.rewrite(source)

        self.assertIsNone(token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)

        expected_path = f"/b/name/o/{blob_name}/rewriteTo/b/name/o/{blob_name}"
        expected_data = {"kmsKeyName": dest_kms_resource}
        # The kmsKeyName version value can't be used in the rewrite request,
        # so the client instead ignores it.
        expected_query_params = {}
        expected_headers = {
            "X-Goog-Copy-Source-Encryption-Algorithm": "AES256",
            "X-Goog-Copy-Source-Encryption-Key": source_key_b64,
            "X-Goog-Copy-Source-Encryption-Key-Sha256": source_key_hash_b64,
        }
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest,
        )

    def test_rewrite_w_destination_contexts(self):
        from google.cloud.storage.blob import (
            ObjectContexts,
            ObjectCustomContextPayload,
        )

        blob_name = "blob"
        bytes_rewritten = object_size = 42
        api_response = {
            "totalBytesRewritten": bytes_rewritten,
            "objectSize": object_size,
            "done": True,
            "resource": {
                "etag": "DEADBEEF",
                "contexts": {"custom": {"foo": {"value": "bar"}}},
            },
        }
        client = mock.Mock(spec=["_post_resource"])
        client._post_resource.return_value = api_response
        bucket = _Bucket(client=client)
        source = self._make_one(blob_name, bucket=bucket)
        dest = self._make_one(blob_name, bucket=bucket)

        payload = ObjectCustomContextPayload(value="bar")
        contexts = ObjectContexts(None, custom={"foo": payload})

        token, rewritten, size = dest.rewrite(
            source,
            destination_contexts=contexts,
        )

        self.assertIsNone(token)
        self.assertEqual(rewritten, bytes_rewritten)
        self.assertEqual(size, object_size)
        self.assertEqual(dest.contexts.custom["foo"].value, "bar")

        expected_path = f"/b/name/o/{blob_name}/rewriteTo/b/name/o/{blob_name}"
        expected_data = {"contexts": {"custom": {"foo": {"value": "bar"}}}}
        expected_query_params = {}
        expected_headers = {}
        client._post_resource.assert_called_once_with(
            expected_path,
            expected_data,
            query_params=expected_query_params,
            headers=expected_headers,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
            _target_object=dest,
        )

    def _update_storage_class_multi_pass_helper(self, **kw):
        blob_name = "blob-name"
        storage_class = "NEARLINE"
        rewrite_token = "TOKEN"
        bytes_rewritten = 42
        object_size = 84
        client = mock.Mock(spec=[])
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.rewrite = mock.Mock(spec=[])
        blob.rewrite.side_effect = [
            (rewrite_token, bytes_rewritten, object_size),
            (None, object_size, object_size),
        ]

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

        blob.update_storage_class(storage_class, **kw)

        self.assertEqual(blob.storage_class, storage_class)

        call1 = mock.call(
            blob,
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
        call2 = mock.call(
            blob,
            token=rewrite_token,
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
        blob.rewrite.assert_has_calls([call1, call2])

    def test_update_storage_class_multi_pass_w_defaults(self):
        self._update_storage_class_multi_pass_helper()

    def test_update_storage_class_multi_pass_w_i_g_m(self):
        generation = 16
        self._update_storage_class_multi_pass_helper(if_generation_match=generation)

    def test_update_storage_class_multi_pass_w_i_g_n_m(self):
        generation = 16
        self._update_storage_class_multi_pass_helper(if_generation_not_match=generation)

    def test_update_storage_class_multi_pass_w_i_m_m(self):
        metageneration = 16
        self._update_storage_class_multi_pass_helper(
            if_metageneration_match=metageneration,
        )

    def test_update_storage_class_multi_pass_w_i_m_n_m(self):
        metageneration = 16
        self._update_storage_class_multi_pass_helper(
            if_metageneration_not_match=metageneration,
        )

    def test_update_storage_class_multi_pass_w_i_s_g_m(self):
        generation = 16
        self._update_storage_class_multi_pass_helper(
            if_source_generation_match=generation
        )

    def test_update_storage_class_multi_pass_w_i_s_g_n_m(self):
        generation = 16
        self._update_storage_class_multi_pass_helper(
            if_source_generation_not_match=generation
        )

    def test_update_storage_class_multi_pass_w_i_s_m_m(self):
        metageneration = 16
        self._update_storage_class_multi_pass_helper(
            if_source_metageneration_match=metageneration,
        )

    def test_update_storage_class_multi_pass_w_i_s_m_n_m(self):
        metageneration = 16
        self._update_storage_class_multi_pass_helper(
            if_source_metageneration_not_match=metageneration,
        )

    def test_update_storage_class_multi_pass_w_timeout(self):
        timeout = 42
        self._update_storage_class_multi_pass_helper(timeout=timeout)

    def test_update_storage_class_multi_pass_w_retry(self):
        retry = mock.Mock(spec=[])
        self._update_storage_class_multi_pass_helper(retry=retry)

    def _update_storage_class_single_pass_helper(self, **kw):
        blob_name = "blob-name"
        storage_class = "NEARLINE"
        object_size = 84
        client = mock.Mock(spec=[])
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.rewrite = mock.Mock(spec=[])
        blob.rewrite.return_value = (None, object_size, object_size)

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

        blob.update_storage_class(storage_class, **kw)

        self.assertEqual(blob.storage_class, storage_class)

        blob.rewrite.assert_called_once_with(
            blob,
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

    def test_update_storage_class_single_pass_w_defaults(self):
        self._update_storage_class_single_pass_helper()

    def test_update_storage_class_single_pass_w_i_g_m(self):
        generation = 16
        self._update_storage_class_single_pass_helper(if_generation_match=generation)

    def test_update_storage_class_single_pass_w_i_g_n_m(self):
        generation = 16
        self._update_storage_class_single_pass_helper(
            if_generation_not_match=generation
        )

    def test_update_storage_class_single_pass_w_i_m_m(self):
        metageneration = 16
        self._update_storage_class_single_pass_helper(
            if_metageneration_match=metageneration,
        )

    def test_update_storage_class_single_pass_w_i_m_n_m(self):
        metageneration = 16
        self._update_storage_class_single_pass_helper(
            if_metageneration_not_match=metageneration,
        )

    def test_update_storage_class_single_pass_w_i_s_g_m(self):
        generation = 16
        self._update_storage_class_single_pass_helper(
            if_source_generation_match=generation
        )

    def test_update_storage_class_single_pass_w_i_s_g_n_m(self):
        generation = 16
        self._update_storage_class_single_pass_helper(
            if_source_generation_not_match=generation
        )

    def test_update_storage_class_single_pass_w_i_s_m_m(self):
        metageneration = 16
        self._update_storage_class_single_pass_helper(
            if_source_metageneration_match=metageneration,
        )

    def test_update_storage_class_single_pass_w_i_s_m_n_m(self):
        metageneration = 16
        self._update_storage_class_single_pass_helper(
            if_source_metageneration_not_match=metageneration,
        )

    def test_update_storage_class_single_pass_w_timeout(self):
        timeout = 42
        self._update_storage_class_single_pass_helper(timeout=timeout)

    def test_update_storage_class_single_pass_w_retry(self):
        retry = mock.Mock(spec=[])
        self._update_storage_class_single_pass_helper(retry=retry)

    def test_update_storage_class_invalid(self):
        from google.cloud.exceptions import BadRequest

        storage_class = "BOGUS"
        blob_name = "blob-name"
        client = mock.Mock(spec=[])
        bucket = _Bucket(client=client)
        blob = self._make_one(blob_name, bucket=bucket)
        blob.rewrite = mock.Mock(spec=[])
        blob.rewrite.side_effect = BadRequest("Invalid storage class")

        with self.assertRaises(BadRequest):
            blob.update_storage_class(storage_class)

        # Test that invalid classes are allowed without client side validation.
        # Fall back to server side validation and errors.
        self.assertEqual(blob.storage_class, storage_class)

        blob.rewrite.assert_called_once_with(
            blob,
            if_generation_match=None,
            if_generation_not_match=None,
            if_metageneration_match=None,
            if_metageneration_not_match=None,
            if_source_generation_match=None,
            if_source_generation_not_match=None,
            if_source_metageneration_match=None,
            if_source_metageneration_not_match=None,
            timeout=self._get_default_timeout(),
            retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
        )

    def test_cache_control_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        CACHE_CONTROL = "no-cache"
        properties = {"cacheControl": CACHE_CONTROL}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.cache_control, CACHE_CONTROL)

    def test_cache_control_setter(self):
        BLOB_NAME = "blob-name"
        CACHE_CONTROL = "no-cache"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.cache_control)
        blob.cache_control = CACHE_CONTROL
        self.assertEqual(blob.cache_control, CACHE_CONTROL)

    def test_component_count(self):
        BUCKET = object()
        COMPONENT_COUNT = 42
        blob = self._make_one(
            "blob-name", bucket=BUCKET, properties={"componentCount": COMPONENT_COUNT}
        )
        self.assertEqual(blob.component_count, COMPONENT_COUNT)

    def test_component_count_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.component_count)

    def test_component_count_string_val(self):
        BUCKET = object()
        COMPONENT_COUNT = 42
        blob = self._make_one(
            "blob-name",
            bucket=BUCKET,
            properties={"componentCount": str(COMPONENT_COUNT)},
        )
        self.assertEqual(blob.component_count, COMPONENT_COUNT)

    def test_content_disposition_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        CONTENT_DISPOSITION = "Attachment; filename=example.jpg"
        properties = {"contentDisposition": CONTENT_DISPOSITION}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.content_disposition, CONTENT_DISPOSITION)

    def test_content_disposition_setter(self):
        BLOB_NAME = "blob-name"
        CONTENT_DISPOSITION = "Attachment; filename=example.jpg"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.content_disposition)
        blob.content_disposition = CONTENT_DISPOSITION
        self.assertEqual(blob.content_disposition, CONTENT_DISPOSITION)

    def test_content_encoding_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        CONTENT_ENCODING = "gzip"
        properties = {"contentEncoding": CONTENT_ENCODING}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.content_encoding, CONTENT_ENCODING)

    def test_content_encoding_setter(self):
        BLOB_NAME = "blob-name"
        CONTENT_ENCODING = "gzip"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.content_encoding)
        blob.content_encoding = CONTENT_ENCODING
        self.assertEqual(blob.content_encoding, CONTENT_ENCODING)

    def test_content_language_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        CONTENT_LANGUAGE = "pt-BR"
        properties = {"contentLanguage": CONTENT_LANGUAGE}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.content_language, CONTENT_LANGUAGE)

    def test_content_language_setter(self):
        BLOB_NAME = "blob-name"
        CONTENT_LANGUAGE = "pt-BR"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.content_language)
        blob.content_language = CONTENT_LANGUAGE
        self.assertEqual(blob.content_language, CONTENT_LANGUAGE)

    def test_content_type_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        CONTENT_TYPE = "image/jpeg"
        properties = {"contentType": CONTENT_TYPE}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.content_type, CONTENT_TYPE)

    def test_content_type_setter(self):
        BLOB_NAME = "blob-name"
        CONTENT_TYPE = "image/jpeg"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.content_type)
        blob.content_type = CONTENT_TYPE
        self.assertEqual(blob.content_type, CONTENT_TYPE)

    def test_crc32c_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        CRC32C = "DEADBEEF"
        properties = {"crc32c": CRC32C}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.crc32c, CRC32C)

    def test_crc32c_setter(self):
        BLOB_NAME = "blob-name"
        CRC32C = "DEADBEEF"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.crc32c)
        blob.crc32c = CRC32C
        self.assertEqual(blob.crc32c, CRC32C)

    def test_etag(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        ETAG = "ETAG"
        properties = {"etag": ETAG}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.etag, ETAG)

    def test_event_based_hold_getter_missing(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertIsNone(blob.event_based_hold)

    def test_event_based_hold_getter_false(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {"eventBasedHold": False}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertFalse(blob.event_based_hold)

    def test_event_based_hold_getter_true(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {"eventBasedHold": True}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertTrue(blob.event_based_hold)

    def test_event_based_hold_setter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.event_based_hold)
        blob.event_based_hold = True
        self.assertEqual(blob.event_based_hold, True)

    def test_generation(self):
        BUCKET = object()
        GENERATION = 42
        blob = self._make_one(
            "blob-name", bucket=BUCKET, properties={"generation": GENERATION}
        )
        self.assertEqual(blob.generation, GENERATION)

    def test_generation_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.generation)

    def test_generation_string_val(self):
        BUCKET = object()
        GENERATION = 42
        blob = self._make_one(
            "blob-name", bucket=BUCKET, properties={"generation": str(GENERATION)}
        )
        self.assertEqual(blob.generation, GENERATION)

    def test_id(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        ID = "ID"
        properties = {"id": ID}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.id, ID)

    def test_md5_hash_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        MD5_HASH = "DEADBEEF"
        properties = {"md5Hash": MD5_HASH}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.md5_hash, MD5_HASH)

    def test_md5_hash_setter(self):
        BLOB_NAME = "blob-name"
        MD5_HASH = "DEADBEEF"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.md5_hash)
        blob.md5_hash = MD5_HASH
        self.assertEqual(blob.md5_hash, MD5_HASH)

    def test_media_link(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        MEDIA_LINK = "http://example.com/media/"
        properties = {"mediaLink": MEDIA_LINK}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.media_link, MEDIA_LINK)

    def test_metadata_getter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        METADATA = {"foo": "Foo"}
        properties = {"metadata": METADATA}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.metadata, METADATA)

    def test_metadata_setter(self):
        BLOB_NAME = "blob-name"
        METADATA = {"foo": "Foo"}
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.metadata)
        blob.metadata = METADATA
        self.assertEqual(blob.metadata, METADATA)
        self.assertIn("metadata", blob._changes)

    def test_metadata_setter_w_nan(self):
        BLOB_NAME = "blob-name"
        METADATA = {"foo": float("nan")}
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.metadata)
        blob.metadata = METADATA
        value = blob.metadata["foo"]
        self.assertIsInstance(value, str)
        self.assertIn("metadata", blob._changes)

    def test_metageneration(self):
        BUCKET = object()
        METAGENERATION = 42
        blob = self._make_one(
            "blob-name", bucket=BUCKET, properties={"metageneration": METAGENERATION}
        )
        self.assertEqual(blob.metageneration, METAGENERATION)

    def test_metageneration_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.metageneration)

    def test_metageneration_string_val(self):
        BUCKET = object()
        METAGENERATION = 42
        blob = self._make_one(
            "blob-name",
            bucket=BUCKET,
            properties={"metageneration": str(METAGENERATION)},
        )
        self.assertEqual(blob.metageneration, METAGENERATION)

    def test_owner(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        OWNER = {"entity": "project-owner-12345", "entityId": "23456"}
        properties = {"owner": OWNER}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        owner = blob.owner
        self.assertEqual(owner["entity"], "project-owner-12345")
        self.assertEqual(owner["entityId"], "23456")

    def test_retention_expiration_time(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        TIME_CREATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"retentionExpirationTime": TIME_CREATED}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.retention_expiration_time, TIMESTAMP)

    def test_retention_expiration_time_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.retention_expiration_time)

    def test_self_link(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        SELF_LINK = "http://example.com/self/"
        properties = {"selfLink": SELF_LINK}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.self_link, SELF_LINK)

    def test_size(self):
        BUCKET = object()
        SIZE = 42
        blob = self._make_one("blob-name", bucket=BUCKET, properties={"size": SIZE})
        self.assertEqual(blob.size, SIZE)

    def test_size_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.size)

    def test_size_string_val(self):
        BUCKET = object()
        SIZE = 42
        blob = self._make_one(
            "blob-name", bucket=BUCKET, properties={"size": str(SIZE)}
        )
        self.assertEqual(blob.size, SIZE)

    def test_storage_class_getter(self):
        blob_name = "blob-name"
        bucket = _Bucket()
        storage_class = "COLDLINE"
        properties = {"storageClass": storage_class}
        blob = self._make_one(blob_name, bucket=bucket, properties=properties)
        self.assertEqual(blob.storage_class, storage_class)

    def test_storage_class_setter(self):
        blob_name = "blob-name"
        bucket = _Bucket()
        storage_class = "COLDLINE"
        blob = self._make_one(blob_name, bucket=bucket)
        self.assertIsNone(blob.storage_class)
        blob.storage_class = storage_class
        self.assertEqual(blob.storage_class, storage_class)
        self.assertEqual(blob._properties, {"storageClass": storage_class})

    def test_temporary_hold_getter_missing(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertIsNone(blob.temporary_hold)

    def test_temporary_hold_getter_false(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {"temporaryHold": False}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertFalse(blob.temporary_hold)

    def test_temporary_hold_getter_true(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        properties = {"temporaryHold": True}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertTrue(blob.temporary_hold)

    def test_temporary_hold_setter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.temporary_hold)
        blob.temporary_hold = True
        self.assertEqual(blob.temporary_hold, True)

    def test_time_deleted(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        TIME_DELETED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"timeDeleted": TIME_DELETED}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.time_deleted, TIMESTAMP)

    def test_time_deleted_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.time_deleted)

    def test_time_created(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        TIME_CREATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"timeCreated": TIME_CREATED}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.time_created, TIMESTAMP)

    def test_time_created_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.time_created)

    def test_updated(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        UPDATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"updated": UPDATED}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.updated, TIMESTAMP)

    def test_updated_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.updated)

    def test_custom_time_getter(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        TIME_CREATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"customTime": TIME_CREATED}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.custom_time, TIMESTAMP)

    def test_custom_time_setter(self):
        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsNone(blob.custom_time)
        blob.custom_time = TIMESTAMP
        self.assertEqual(blob.custom_time, TIMESTAMP)
        self.assertIn("customTime", blob._changes)

    def test_custom_time_setter_none_value(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        TIMESTAMP = datetime.datetime(2014, 11, 5, 20, 34, 37, tzinfo=_UTC)
        TIME_CREATED = TIMESTAMP.strftime(_RFC3339_MICROS)
        properties = {"customTime": TIME_CREATED}
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.custom_time, TIMESTAMP)
        blob.custom_time = None
        self.assertIsNone(blob.custom_time)

    def test_custom_time_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.custom_time)

    def test_soft_hard_delete_time_getter(self):
        from google.cloud._helpers import _RFC3339_MICROS

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        soft_timstamp = datetime.datetime(2024, 1, 5, 20, 34, 37, tzinfo=_UTC)
        soft_delete = soft_timstamp.strftime(_RFC3339_MICROS)
        hard_timstamp = datetime.datetime(2024, 1, 15, 20, 34, 37, tzinfo=_UTC)
        hard_delete = hard_timstamp.strftime(_RFC3339_MICROS)
        properties = {
            "softDeleteTime": soft_delete,
            "hardDeleteTime": hard_delete,
        }
        blob = self._make_one(BLOB_NAME, bucket=bucket, properties=properties)
        self.assertEqual(blob.soft_delete_time, soft_timstamp)
        self.assertEqual(blob.hard_delete_time, hard_timstamp)

    def test_soft_hard_delte_time_unset(self):
        BUCKET = object()
        blob = self._make_one("blob-name", bucket=BUCKET)
        self.assertIsNone(blob.soft_delete_time)
        self.assertIsNone(blob.hard_delete_time)

    def test_from_uri_w_valid_uri(self):
        from google.cloud.storage.blob import Blob

        client = self._make_client()
        basic_uri = "gs://bucket_name/b"
        blob = Blob.from_uri(basic_uri, client)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.client, client)
        self.assertEqual(blob.name, "b")
        self.assertEqual(blob.bucket.name, "bucket_name")
        self.assertEqual(blob.uri, basic_uri)

        nested_uri = "gs://bucket_name/path1/path2/b#name"
        blob = Blob.from_uri(nested_uri, client)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.client, client)
        self.assertEqual(blob.name, "path1/path2/b#name")
        self.assertEqual(blob.bucket.name, "bucket_name")
        self.assertEqual(blob.uri, nested_uri)

    def test_from_uri_w_invalid_uri(self):
        from google.cloud.storage.blob import Blob

        client = self._make_client()

        with pytest.raises(ValueError):
            Blob.from_uri("http://bucket_name/b", client)

    def test_from_uri_w_domain_name_bucket(self):
        from google.cloud.storage.blob import Blob

        client = self._make_client()
        uri = "gs://buckets.example.com/b"
        blob = Blob.from_uri(uri, client)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.client, client)
        self.assertEqual(blob.name, "b")
        self.assertEqual(blob.bucket.name, "buckets.example.com")
        self.assertEqual(blob.uri, uri)

    def test_get_uri_from_blob_w_unset_bucket_name(self):
        blob = self._make_one(name="b", bucket=None)
        with pytest.raises(ValueError, match="Bucket must be set to generate a URI."):
            blob.uri

    @mock.patch("warnings.warn")
    def test_from_string(self, mock_warn):
        from google.cloud.storage.blob import _FROM_STRING_DEPRECATED, Blob

        client = self._make_client()
        basic_uri = "gs://bucket_name/b"
        blob = Blob.from_string(basic_uri, client)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.client, client)
        self.assertEqual(blob.name, "b")
        self.assertEqual(blob.bucket.name, "bucket_name")

        nested_uri = "gs://bucket_name/path1/path2/b#name"
        blob = Blob.from_string(nested_uri, client)

        self.assertIsInstance(blob, Blob)
        self.assertIs(blob.client, client)
        self.assertEqual(blob.name, "path1/path2/b#name")
        self.assertEqual(blob.bucket.name, "bucket_name")

        mock_warn.assert_any_call(
            _FROM_STRING_DEPRECATED,
            PendingDeprecationWarning,
            stacklevel=2,
        )

    def test_open(self):
        from io import TextIOWrapper

        from google.cloud.storage.fileio import BlobReader, BlobWriter

        blob_name = "blob-name"
        client = self._make_client()
        bucket = _Bucket(client)
        blob = self._make_one(blob_name, bucket=bucket)

        f = blob.open("r")
        self.assertEqual(type(f), TextIOWrapper)
        self.assertEqual(type(f.buffer), BlobReader)
        f = blob.open("rt")
        self.assertEqual(type(f), TextIOWrapper)
        self.assertEqual(type(f.buffer), BlobReader)
        f = blob.open("rb")
        self.assertEqual(type(f), BlobReader)
        f = blob.open("w")
        self.assertEqual(type(f), TextIOWrapper)
        self.assertEqual(type(f.buffer), BlobWriter)
        f = blob.open("wt")
        self.assertEqual(type(f), TextIOWrapper)
        self.assertEqual(type(f.buffer), BlobWriter)
        f = blob.open("wb")
        self.assertEqual(type(f), BlobWriter)
        f = blob.open("wb", ignore_flush=True)
        self.assertTrue(f._ignore_flush)

        with self.assertRaises(NotImplementedError):
            blob.open("a")
        with self.assertRaises(ValueError):
            blob.open("rb", encoding="utf-8")
        with self.assertRaises(ValueError):
            blob.open("wb", encoding="utf-8")
        with self.assertRaises(ValueError):
            blob.open("r", ignore_flush=True)
        with self.assertRaises(ValueError):
            blob.open("rb", ignore_flush=True)
        with self.assertRaises(ValueError):
            blob.open("w", ignore_flush=False)

    def test_downloads_w_client_custom_headers(self):
        import google.auth.credentials

        from google.cloud.storage import Client

        custom_headers = {
            "x-goog-custom-audit-foo": "bar",
            "x-goog-custom-audit-user": "baz",
        }
        credentials = mock.Mock(
            spec=google.auth.credentials.Credentials,
            universe_domain=_DEFAULT_UNIVERSE_DOMAIN,
        )
        client = Client(
            project="project", credentials=credentials, extra_headers=custom_headers
        )
        blob = self._make_one("blob-name", bucket=_Bucket(client))
        file_obj = io.BytesIO()

        downloads = {
            client.download_blob_to_file: (blob, file_obj),
            blob.download_to_file: (file_obj,),
            blob.download_as_bytes: (),
        }
        for method, args in downloads.items():
            with mock.patch.object(blob, "_do_download"):
                method(*args)
                blob._do_download.assert_called()
                called_headers = blob._do_download.call_args.args[-4]
                self.assertIsInstance(called_headers, dict)
                self.assertLessEqual(custom_headers.items(), called_headers.items())

    def test_object_lock_retention_configuration(self):
        from google.cloud.storage.blob import Retention

        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET)

        retention = blob.retention

        self.assertIsInstance(retention, Retention)
        self.assertIs(retention.blob, blob)
        self.assertIsNone(retention.mode)
        self.assertIsNone(retention.retain_until_time)
        self.assertIsNone(retention.retention_expiration_time)

    def test_object_lock_retention_configuration_w_entry(self):
        from google.cloud._helpers import _RFC3339_MICROS

        from google.cloud.storage.blob import Retention

        now = _NOW(_UTC)
        expiration_time = now + datetime.timedelta(hours=1)
        expiration = expiration_time.strftime(_RFC3339_MICROS)
        mode = "Locked"
        properties = {
            "retention": {
                "mode": mode,
                "retainUntilTime": expiration,
                "retentionExpirationTime": expiration,
            }
        }
        BLOB_NAME = "blob-name"
        BUCKET = object()
        blob = self._make_one(BLOB_NAME, bucket=BUCKET, properties=properties)
        retention_config = Retention(
            blob=blob,
            mode=mode,
            retain_until_time=expiration_time,
            retention_expiration_time=expiration_time,
        )

        retention = blob.retention

        self.assertIsInstance(retention, Retention)
        self.assertEqual(retention, retention_config)
        self.assertIs(retention.blob, blob)
        self.assertEqual(retention.mode, mode)
        self.assertEqual(retention.retain_until_time, expiration_time)
        self.assertEqual(retention.retention_expiration_time, expiration_time)

    def test_object_lock_retention_configuration_setter(self):
        from google.cloud.storage.blob import Retention

        BLOB_NAME = "blob-name"
        bucket = _Bucket()
        blob = self._make_one(BLOB_NAME, bucket=bucket)
        self.assertIsInstance(blob.retention, Retention)

        mode = "Locked"
        now = _NOW(_UTC)
        expiration_time = now + datetime.timedelta(hours=1)
        retention_config = Retention(
            blob=blob, mode=mode, retain_until_time=expiration_time
        )
        blob.retention.mode = mode
        blob.retention.retain_until_time = expiration_time
        self.assertEqual(blob.retention, retention_config)
        self.assertIn("retention", blob._changes)
        blob.retention.retain_until_time = None
        self.assertIsNone(blob.retention.retain_until_time)
        self.assertIn("retention", blob._changes)

    def test_object_contexts_payload_ctor(self):
        from google.cloud.storage.blob import ObjectCustomContextPayload

        payload = ObjectCustomContextPayload(value="foo")
        self.assertEqual(payload.value, "foo")

    def test_object_contexts_ctor(self):
        from google.cloud.storage.blob import (
            Blob,
            ObjectContexts,
            ObjectCustomContextPayload,
        )

        blob = mock.Mock(spec=Blob)
        custom = {"key": ObjectCustomContextPayload(value="val")}
        contexts = ObjectContexts(blob, custom=custom)
        self.assertIs(contexts.blob, blob)
        self.assertEqual(contexts.custom, custom)

    def test_object_contexts_from_api_repr(self):
        from google.cloud.storage.blob import Blob, ObjectContexts

        blob = mock.Mock(spec=Blob)
        resource = {
            "custom": {
                "key": {
                    "value": "val",
                    "createTime": "2025-01-01T00:00:00Z",
                    "updateTime": "2025-01-02T00:00:00Z",
                }
            }
        }
        contexts = ObjectContexts.from_api_repr(resource, blob)
        self.assertIs(contexts.blob, blob)
        self.assertIn("key", contexts.custom)
        payload = contexts.custom["key"]
        self.assertEqual(payload.value, "val")
        self.assertEqual(
            payload.create_time, datetime.datetime(2025, 1, 1, tzinfo=_UTC)
        )
        self.assertEqual(
            payload.update_time, datetime.datetime(2025, 1, 2, tzinfo=_UTC)
        )

    def test_object_contexts_property(self):
        from google.cloud.storage.blob import (
            Blob,
            ObjectContexts,
            ObjectCustomContextPayload,
        )

        bucket = mock.Mock()
        bucket.name = "b"
        bucket.__getitem__ = mock.Mock(
            side_effect=lambda x: "b" if x in (0, -1) else None
        )
        blob = Blob("blob-name", bucket=bucket)
        self.assertIsInstance(blob.contexts, ObjectContexts)
        self.assertEqual(blob.contexts.custom, {})

        custom = {"key": ObjectCustomContextPayload(value="val")}
        blob.contexts = ObjectContexts(blob, custom=custom)
        self.assertEqual(blob.contexts.custom, custom)

        blob.contexts = None
        self.assertIsNone(blob._properties["contexts"])

    def test_patch_contexts(self):
        from google.cloud.storage.blob import (
            Blob,
            ObjectContexts,
            ObjectCustomContextPayload,
        )
        from google.cloud.storage.bucket import Bucket

        client = self._make_client(project="p")
        bucket = Bucket(client, name="b")
        blob = Blob("blob-name", bucket=bucket)

        custom = {"key": ObjectCustomContextPayload(value="val")}
        blob.contexts = ObjectContexts(blob, custom=custom)

        with mock.patch.object(client, "_patch_resource") as mocked:
            blob.patch()
            mocked.assert_called_once()
            args, kwargs = mocked.call_args
            sent_resource = args[1]
            self.assertEqual(sent_resource["contexts"]["custom"]["key"]["value"], "val")

    def test_patch_contexts_none(self):
        from google.cloud.storage.blob import Blob
        from google.cloud.storage.bucket import Bucket

        client = self._make_client(project="p")
        bucket = Bucket(client, name="b")
        blob = Blob("blob-name", bucket=bucket)

        blob.contexts = None

        with mock.patch.object(client, "_patch_resource") as mocked:
            blob.patch()
            mocked.assert_called_once()
            args, kwargs = mocked.call_args
            sent_resource = args[1]
            self.assertIsNone(sent_resource["contexts"])


class Test__quote(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kw):
        from google.cloud.storage.blob import _quote

        return _quote(*args, **kw)

    def test_bytes(self):
        quoted = self._call_fut(b"\xde\xad\xbe\xef")
        self.assertEqual(quoted, "%DE%AD%BE%EF")

    def test_unicode(self):
        helicopter = "\U0001f681"
        quoted = self._call_fut(helicopter)
        self.assertEqual(quoted, "%F0%9F%9A%81")

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            self._call_fut(None)

    def test_w_slash_default(self):
        with_slash = "foo/bar/baz"
        quoted = self._call_fut(with_slash)
        self.assertEqual(quoted, "foo%2Fbar%2Fbaz")

    def test_w_slash_w_safe(self):
        with_slash = "foo/bar/baz"
        quoted_safe = self._call_fut(with_slash, safe=b"/")
        self.assertEqual(quoted_safe, with_slash)

    def test_w_tilde(self):
        with_tilde = "bam~qux"
        quoted = self._call_fut(with_tilde, safe=b"~")
        self.assertEqual(quoted, with_tilde)


class Test__maybe_rewind(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage.blob import _maybe_rewind

        return _maybe_rewind(*args, **kwargs)

    def test_default(self):
        stream = mock.Mock(spec=["seek"])
        ret_val = self._call_fut(stream)
        self.assertIsNone(ret_val)

        stream.seek.assert_not_called()

    def test_do_not_rewind(self):
        stream = mock.Mock(spec=["seek"])
        ret_val = self._call_fut(stream, rewind=False)
        self.assertIsNone(ret_val)

        stream.seek.assert_not_called()

    def test_do_rewind(self):
        stream = mock.Mock(spec=["seek"])
        ret_val = self._call_fut(stream, rewind=True)
        self.assertIsNone(ret_val)

        stream.seek.assert_called_once_with(0, os.SEEK_SET)


class Test__raise_from_invalid_response(unittest.TestCase):
    @staticmethod
    def _call_fut(error):
        from google.cloud.storage.blob import _raise_from_invalid_response

        return _raise_from_invalid_response(error)

    def _helper(self, message, code=http.client.BAD_REQUEST, reason=None, args=()):
        import requests
        from google.api_core import exceptions

        response = requests.Response()
        response.request = requests.Request("GET", "http://example.com").prepare()
        response._content = reason
        response.status_code = code
        error = InvalidResponse(response, message, *args)

        with self.assertRaises(exceptions.GoogleAPICallError) as exc_info:
            self._call_fut(error)

        return exc_info

    def test_default(self):
        message = "Failure"
        exc_info = self._helper(message)
        expected = f"GET http://example.com/: {message}"
        self.assertEqual(exc_info.exception.message, expected)
        self.assertEqual(exc_info.exception.errors, [])

    def test_w_206_and_args(self):
        message = "Failure"
        reason = b"Not available"
        args = ("one", "two")
        exc_info = self._helper(
            message, code=http.client.PARTIAL_CONTENT, reason=reason, args=args
        )
        expected = "GET http://example.com/: {}: {}".format(
            reason.decode("utf-8"), (message,) + args
        )
        self.assertEqual(exc_info.exception.message, expected)
        self.assertEqual(exc_info.exception.errors, [])


class Test__add_query_parameters(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage.blob import _add_query_parameters

        return _add_query_parameters(*args, **kwargs)

    def test_w_empty_list(self):
        BASE_URL = "https://test.example.com/base"
        self.assertEqual(self._call_fut(BASE_URL, []), BASE_URL)

    def test_wo_existing_qs(self):
        BASE_URL = "https://test.example.com/base"
        NV_LIST = [("one", "One"), ("two", "Two")]
        expected = "&".join([f"{name}={value}" for name, value in NV_LIST])
        self.assertEqual(self._call_fut(BASE_URL, NV_LIST), f"{BASE_URL}?{expected}")

    def test_w_existing_qs(self):
        BASE_URL = "https://test.example.com/base?one=Three"
        NV_LIST = [("one", "One"), ("two", "Two")]
        expected = "&".join([f"{name}={value}" for name, value in NV_LIST])
        self.assertEqual(self._call_fut(BASE_URL, NV_LIST), f"{BASE_URL}&{expected}")


class _Connection(object):
    API_BASE_URL = "http://example.com"
    USER_AGENT = "testing 1.2.3"
    user_agent = "testing 1.2.3"
    credentials = object()


class _Bucket(object):
    def __init__(self, client=None, name="name", user_project=None):
        if client is None:
            client = Test_Blob._make_client()

        self.client = client
        self._blobs = {}
        self._copied = []
        self._deleted = []
        self.name = name
        self.path = "/b/" + name
        self.user_project = user_project

    def delete_blob(
        self,
        blob_name,
        client=None,
        generation=None,
        timeout=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
    ):
        del self._blobs[blob_name]
        self._deleted.append(
            (
                blob_name,
                client,
                generation,
                timeout,
                if_generation_match,
                if_generation_not_match,
                if_metageneration_match,
                if_metageneration_not_match,
                retry,
            )
        )
