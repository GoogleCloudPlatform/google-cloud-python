# Copyright 2018 Google LLC
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

from unittest import mock

import pytest

from google.cloud.ndb import _datastore_types, exceptions


class TestBlobKey:
    @staticmethod
    def test_constructor_bytes():
        value = b"abc"
        blob_key = _datastore_types.BlobKey(value)
        assert blob_key._blob_key is value

    @staticmethod
    def test_constructor_none():
        blob_key = _datastore_types.BlobKey(None)
        assert blob_key._blob_key is None

    @staticmethod
    def test_constructor_too_long():
        value = b"a" * 2000
        with pytest.raises(exceptions.BadValueError):
            _datastore_types.BlobKey(value)

    @staticmethod
    def test_constructor_bad_type():
        value = {"a": "b"}
        with pytest.raises(exceptions.BadValueError):
            _datastore_types.BlobKey(value)

    @staticmethod
    def test___eq__():
        blob_key1 = _datastore_types.BlobKey(b"abc")
        blob_key2 = _datastore_types.BlobKey(b"def")
        blob_key3 = _datastore_types.BlobKey(None)
        blob_key4 = b"ghi"
        blob_key5 = mock.sentinel.blob_key
        assert blob_key1 == blob_key1
        assert not blob_key1 == blob_key2
        assert not blob_key1 == blob_key3
        assert not blob_key1 == blob_key4
        assert not blob_key1 == blob_key5

    @staticmethod
    def test___lt__():
        blob_key1 = _datastore_types.BlobKey(b"abc")
        blob_key2 = _datastore_types.BlobKey(b"def")
        blob_key3 = _datastore_types.BlobKey(None)
        blob_key4 = b"ghi"
        blob_key5 = mock.sentinel.blob_key
        assert not blob_key1 < blob_key1
        assert blob_key1 < blob_key2
        with pytest.raises(TypeError):
            blob_key1 < blob_key3
        assert blob_key1 < blob_key4
        with pytest.raises(TypeError):
            blob_key1 < blob_key5

    @staticmethod
    def test___hash__():
        value = b"289399038904ndkjndjnd02mx"
        blob_key = _datastore_types.BlobKey(value)
        assert hash(blob_key) == hash(value)
