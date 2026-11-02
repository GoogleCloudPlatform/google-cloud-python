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

import grpc
import pytest

from google.cloud.ndb import _remote, exceptions, tasklets


class TestRemoteCall:
    @staticmethod
    def test_constructor():
        future = tasklets.Future()
        call = _remote.RemoteCall(future, "info")
        assert call.future is future
        assert call.info == "info"

    @staticmethod
    def test_repr():
        future = tasklets.Future()
        call = _remote.RemoteCall(future, "a remote call")
        assert repr(call) == "a remote call"

    @staticmethod
    def test_exception():
        error = Exception("Spurious error")
        future = tasklets.Future()
        future.set_exception(error)
        call = _remote.RemoteCall(future, "testing")
        assert call.exception() is error

    @staticmethod
    def test_exception_FutureCancelledError():
        error = grpc.FutureCancelledError()
        future = tasklets.Future()
        future.exception = mock.Mock(side_effect=error)
        call = _remote.RemoteCall(future, "testing")
        assert isinstance(call.exception(), exceptions.Cancelled)

    @staticmethod
    def test_result():
        future = tasklets.Future()
        future.set_result("positive")
        call = _remote.RemoteCall(future, "testing")
        assert call.result() == "positive"

    @staticmethod
    def test_add_done_callback():
        future = tasklets.Future()
        call = _remote.RemoteCall(future, "testing")
        callback = mock.Mock(spec=())
        call.add_done_callback(callback)
        future.set_result(None)
        callback.assert_called_once_with(call)

    @staticmethod
    def test_add_done_callback_already_done():
        future = tasklets.Future()
        future.set_result(None)
        call = _remote.RemoteCall(future, "testing")
        callback = mock.Mock(spec=())
        call.add_done_callback(callback)
        callback.assert_called_once_with(call)

    @staticmethod
    def test_cancel():
        future = tasklets.Future()
        call = _remote.RemoteCall(future, "testing")
        call.cancel()
        assert future.cancelled()
        with pytest.raises(exceptions.Cancelled):
            call.result()
