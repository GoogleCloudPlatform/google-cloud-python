# Copyright 2021 Google LLC All rights reserved.
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

import mock

from google.cloud.bigtable import enums

EncryptionType = enums.EncryptionInfo.EncryptionType
_STATUS_CODE = 123
_STATUS_MESSAGE = "message"
_KMS_KEY_VERSION = 345


def _make_status_pb(code=_STATUS_CODE, message=_STATUS_MESSAGE):
    from google.rpc.status_pb2 import Status

    return Status(code=code, message=message)


def _make_status(code=_STATUS_CODE, message=_STATUS_MESSAGE):
    from google.cloud.bigtable.error import Status

    status_pb = _make_status_pb(code=code, message=message)
    return Status(status_pb)


def _make_info_pb(
    encryption_type=EncryptionType.GOOGLE_DEFAULT_ENCRYPTION,
    code=_STATUS_CODE,
    message=_STATUS_MESSAGE,
    kms_key_version=_KMS_KEY_VERSION,
):
    encryption_status = _make_status_pb(code=code, message=message)

    spec = ["encryption_type", "encryption_status", "kms_key_version"]
    return mock.Mock(
        spec=spec,
        encryption_type=encryption_type,
        encryption_status=encryption_status,
        kms_key_version=kms_key_version,
    )


def _make_encryption_info(*args, **kwargs):
    from google.cloud.bigtable.encryption_info import EncryptionInfo

    return EncryptionInfo(*args, **kwargs)


def _make_encryption_info_defaults(
    encryption_type=EncryptionType.GOOGLE_DEFAULT_ENCRYPTION,
    code=_STATUS_CODE,
    message=_STATUS_MESSAGE,
    kms_key_version=_KMS_KEY_VERSION,
):
    encryption_status = _make_status(code=code, message=message)
    return _make_encryption_info(encryption_type, encryption_status, kms_key_version)


def test_encryption_info__from_pb():
    from google.cloud.bigtable.encryption_info import EncryptionInfo

    info_pb = _make_info_pb()

    info = EncryptionInfo._from_pb(info_pb)

    assert info.encryption_type == EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    assert info.encryption_status.code == _STATUS_CODE
    assert info.encryption_status.message == _STATUS_MESSAGE
    assert info.kms_key_version == _KMS_KEY_VERSION


def test_encryption_info_ctor():
    encryption_type = EncryptionType.GOOGLE_DEFAULT_ENCRYPTION
    encryption_status = _make_status()

    info = _make_encryption_info(
        encryption_type=encryption_type,
        encryption_status=encryption_status,
        kms_key_version=_KMS_KEY_VERSION,
    )

    assert info.encryption_type == encryption_type
    assert info.encryption_status == encryption_status
    assert info.kms_key_version == _KMS_KEY_VERSION


def test_encryption_info___eq___identity():
    info = _make_encryption_info_defaults()
    assert info == info


def test_encryption_info___eq___wrong_type():
    info = _make_encryption_info_defaults()
    other = object()
    assert not (info == other)


def test_encryption_info___eq___same_values():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults()
    assert info == other


def test_encryption_info___eq___different_encryption_type():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults(
        encryption_type=EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
    )
    assert not (info == other)


def test_encryption_info___eq___different_encryption_status():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults(code=456)
    assert not (info == other)


def test_encryption_info___eq___different_kms_key_version():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults(kms_key_version=789)
    assert not (info == other)


def test_encryption_info___ne___identity():
    info = _make_encryption_info_defaults()
    assert not (info != info)


def test_encryption_info___ne___wrong_type():
    info = _make_encryption_info_defaults()
    other = object()
    assert info != other


def test_encryption_info___ne___same_values():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults()
    assert not (info != other)


def test_encryption_info___ne___different_encryption_type():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults(
        encryption_type=EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
    )
    assert info != other


def test_encryption_info___ne___different_encryption_status():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults(code=456)
    assert info != other


def test_encryption_info___ne___different_kms_key_version():
    info = _make_encryption_info_defaults()
    other = _make_encryption_info_defaults(kms_key_version=789)
    assert info != other
