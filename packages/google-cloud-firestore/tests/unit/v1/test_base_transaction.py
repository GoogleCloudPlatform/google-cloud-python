# Copyright 2017 Google LLC All rights reserved.
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
import pytest


def _make_base_transaction(*args, **kwargs):
    from google.cloud.firestore_v1.base_transaction import BaseTransaction

    return BaseTransaction(*args, **kwargs)


def test_basetransaction_constructor_defaults():
    from google.cloud.firestore_v1.transaction import MAX_ATTEMPTS

    transaction = _make_base_transaction()
    assert transaction._max_attempts == MAX_ATTEMPTS
    assert not transaction._read_only
    assert transaction._id is None


def test_basetransaction_constructor_explicit():
    transaction = _make_base_transaction(max_attempts=10, read_only=True)
    assert transaction._max_attempts == 10
    assert transaction._read_only
    assert transaction._id is None


def test_basetransaction__options_protobuf_read_only():
    from google.cloud.firestore_v1.types import common

    transaction = _make_base_transaction(read_only=True)
    options_pb = transaction._options_protobuf(None)
    expected_pb = common.TransactionOptions(
        read_only=common.TransactionOptions.ReadOnly()
    )
    assert options_pb == expected_pb


def test_basetransaction__options_protobuf_read_only_retry():
    from google.cloud.firestore_v1.base_transaction import _CANT_RETRY_READ_ONLY

    transaction = _make_base_transaction(read_only=True)
    retry_id = b"illuminate"

    with pytest.raises(ValueError) as exc_info:
        transaction._options_protobuf(retry_id)

    assert exc_info.value.args == (_CANT_RETRY_READ_ONLY,)


def test_basetransaction__options_protobuf_read_write():
    transaction = _make_base_transaction()
    options_pb = transaction._options_protobuf(None)
    assert options_pb is None


def test_basetransaction__options_protobuf_on_retry():
    from google.cloud.firestore_v1.types import common

    transaction = _make_base_transaction()
    retry_id = b"hocus-pocus"
    options_pb = transaction._options_protobuf(retry_id)
    expected_pb = common.TransactionOptions(
        read_write=common.TransactionOptions.ReadWrite(retry_transaction=retry_id)
    )
    assert options_pb == expected_pb


def test_basetransaction_in_progress_property():
    transaction = _make_base_transaction()
    assert not transaction.in_progress
    transaction._id = b"not-none-bites"
    assert transaction.in_progress


def test_basetransaction_id_property():
    transaction = _make_base_transaction()
    transaction._id = mock.sentinel.eye_dee
    assert transaction.id is mock.sentinel.eye_dee


def _make_base_transactional(*args, **kwargs):
    from google.cloud.firestore_v1.base_transaction import _BaseTransactional

    return _BaseTransactional(*args, **kwargs)


def test_basetransactional_constructor():
    wrapped = _make_base_transactional(mock.sentinel.callable_)
    assert wrapped.to_wrap is mock.sentinel.callable_
    assert wrapped.current_id is None
    assert wrapped.retry_id is None


def test__basetransactional_reset():
    wrapped = _make_base_transactional(mock.sentinel.callable_)
    wrapped.current_id = b"not-none"
    wrapped.retry_id = b"also-not"

    ret_val = wrapped._reset()
    assert ret_val is None

    assert wrapped.current_id is None
    assert wrapped.retry_id is None
