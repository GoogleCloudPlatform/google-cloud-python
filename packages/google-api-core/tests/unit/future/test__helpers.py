# Copyright 2017, Google LLC
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

from unittest import mock

from google.api_core.future import _helpers


@mock.patch("threading.Thread", autospec=True)
def test_start_deamon_thread(unused_thread):
    deamon_thread = _helpers.start_daemon_thread(target=mock.sentinel.target)
    assert deamon_thread.daemon is True


def test_safe_invoke_callback():
    callback = mock.Mock(spec=["__call__"], return_value=42)
    result = _helpers.safe_invoke_callback(callback, "a", b="c")
    assert result == 42
    callback.assert_called_once_with("a", b="c")


def test_safe_invoke_callback_exception():
    callback = mock.Mock(spec=["__call__"], side_effect=ValueError())
    result = _helpers.safe_invoke_callback(callback, "a", b="c")
    assert result is None
    callback.assert_called_once_with("a", b="c")
