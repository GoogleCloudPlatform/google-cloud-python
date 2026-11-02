# Copyright 2021 Google LLC
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


def _make_status_pb(**kwargs):
    from google.rpc.status_pb2 import Status

    return Status(**kwargs)


def _make_status(status_pb):
    from google.cloud.bigtable.error import Status

    return Status(status_pb)


def test_status_ctor():
    status_pb = _make_status_pb()
    status = _make_status(status_pb)
    assert status.status_pb is status_pb


def test_status_code():
    code = 123
    status_pb = _make_status_pb(code=code)
    status = _make_status(status_pb)
    assert status.code == code


def test_status_message():
    message = "message"
    status_pb = _make_status_pb(message=message)
    status = _make_status(status_pb)
    assert status.message == message


def test_status___eq___self():
    status_pb = _make_status_pb()
    status = _make_status(status_pb)
    assert status == status


def test_status___eq___other_hit():
    status_pb = _make_status_pb(code=123, message="message")
    status = _make_status(status_pb)
    other = _make_status(status_pb)
    assert status == other


def test_status___eq___other_miss():
    status_pb = _make_status_pb(code=123, message="message")
    other_status_pb = _make_status_pb(code=456, message="oops")
    status = _make_status(status_pb)
    other = _make_status(other_status_pb)
    assert not (status == other)


def test_status___eq___wrong_type():
    status_pb = _make_status_pb(code=123, message="message")
    status = _make_status(status_pb)
    other = object()
    assert not (status == other)


def test_status___ne___self():
    status_pb = _make_status_pb()
    status = _make_status(status_pb)
    assert not (status != status)


def test_status___ne___other_hit():
    status_pb = _make_status_pb(code=123, message="message")
    status = _make_status(status_pb)
    other = _make_status(status_pb)
    assert not (status != other)


def test_status___ne___other_miss():
    status_pb = _make_status_pb(code=123, message="message")
    other_status_pb = _make_status_pb(code=456, message="oops")
    status = _make_status(status_pb)
    other = _make_status(other_status_pb)
    assert status != other


def test_status___ne___wrong_type():
    status_pb = _make_status_pb(code=123, message="message")
    status = _make_status(status_pb)
    other = object()
    assert status != other
