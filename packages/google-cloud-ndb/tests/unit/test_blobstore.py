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

import pytest

from google.cloud.ndb import _datastore_types, blobstore, model

from . import utils


def test___all__():
    utils.verify___all__(blobstore)


def test_BlobKey():
    assert blobstore.BlobKey is _datastore_types.BlobKey


def test_BlobKeyProperty():
    assert blobstore.BlobKeyProperty is model.BlobKeyProperty


class TestBlobFetchSizeTooLargeError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.BlobFetchSizeTooLargeError()


class TestBlobInfo:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.BlobInfo()

    @staticmethod
    def test_get():
        with pytest.raises(NotImplementedError):
            blobstore.BlobInfo.get()

    @staticmethod
    def test_get_async():
        with pytest.raises(NotImplementedError):
            blobstore.BlobInfo.get_async()

    @staticmethod
    def test_get_multi():
        with pytest.raises(NotImplementedError):
            blobstore.BlobInfo.get_multi()

    @staticmethod
    def test_get_multi_async():
        with pytest.raises(NotImplementedError):
            blobstore.BlobInfo.get_multi_async()


class TestBlobInfoParseError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.BlobInfoParseError()


class TestBlobNotFoundError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.BlobNotFoundError()


class TestBlobReader:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.BlobReader()


def test_create_upload_url():
    with pytest.raises(NotImplementedError):
        blobstore.create_upload_url()


def test_create_upload_url_async():
    with pytest.raises(NotImplementedError):
        blobstore.create_upload_url_async()


class TestDataIndexOutOfRangeError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.DataIndexOutOfRangeError()


def test_delete():
    with pytest.raises(NotImplementedError):
        blobstore.delete()


def test_delete_async():
    with pytest.raises(NotImplementedError):
        blobstore.delete_async()


def test_delete_multi():
    with pytest.raises(NotImplementedError):
        blobstore.delete_multi()


def test_delete_multi_async():
    with pytest.raises(NotImplementedError):
        blobstore.delete_multi_async()


class TestError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.Error()


def test_fetch_data():
    with pytest.raises(NotImplementedError):
        blobstore.fetch_data()


def test_fetch_data_async():
    with pytest.raises(NotImplementedError):
        blobstore.fetch_data_async()


def test_get():
    # NOTE: `is` identity doesn't work for class methods
    assert blobstore.get == blobstore.BlobInfo.get


def test_get_async():
    # NOTE: `is` identity doesn't work for class methods
    assert blobstore.get_async == blobstore.BlobInfo.get_async


def test_get_multi():
    # NOTE: `is` identity doesn't work for class methods
    assert blobstore.get_multi == blobstore.BlobInfo.get_multi


def test_get_multi_async():
    # NOTE: `is` identity doesn't work for class methods
    assert blobstore.get_multi_async == blobstore.BlobInfo.get_multi_async


class TestInternalError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.InternalError()


def test_parse_blob_info():
    with pytest.raises(NotImplementedError):
        blobstore.parse_blob_info()


class TestPermissionDeniedError:
    @staticmethod
    def test_constructor():
        with pytest.raises(NotImplementedError):
            blobstore.PermissionDeniedError()
