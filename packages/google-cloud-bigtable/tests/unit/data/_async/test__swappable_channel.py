# Copyright 2025 Google LLC
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

import pytest
from grpc import ChannelConnectivity

from google.cloud.bigtable.data._cross_sync import CrossSync

if CrossSync.is_async:
    from google.cloud.bigtable.data._async._swappable_channel import (
        AsyncSwappableChannel as TargetType,
    )
else:
    from google.cloud.bigtable.data._sync_autogen._swappable_channel import (
        SwappableChannel as TargetType,
    )


__CROSS_SYNC_OUTPUT__ = "tests.unit.data._sync_autogen.test__swappable_channel"


@CrossSync.convert_class(sync_name="TestSwappableChannel")
class TestAsyncSwappableChannel:
    @staticmethod
    @CrossSync.convert
    def _get_target_class():
        return TargetType

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_ctor(self):
        channel_fn = mock.Mock()
        instance = self._make_one(channel_fn)
        assert instance._channel_fn == channel_fn
        channel_fn.assert_called_once_with()
        assert instance._channel == channel_fn.return_value

    def test_swap_channel(self):
        channel_fn = mock.Mock()
        instance = self._make_one(channel_fn)
        old_channel = instance._channel
        new_channel = object()
        result = instance.swap_channel(new_channel)
        assert result == old_channel
        assert instance._channel == new_channel

    def test_create_channel(self):
        channel_fn = mock.Mock()
        instance = self._make_one(channel_fn)
        # reset mock from ctor call
        channel_fn.reset_mock()
        new_channel = instance.create_channel()
        channel_fn.assert_called_once_with()
        assert new_channel == channel_fn.return_value

    @CrossSync.drop
    def test_create_channel_async_interceptors_copied(self):
        channel_fn = mock.Mock()
        instance = self._make_one(channel_fn)
        # reset mock from ctor call
        channel_fn.reset_mock()
        # mock out interceptors on original channel
        instance._channel._unary_unary_interceptors = ["unary_unary"]
        instance._channel._unary_stream_interceptors = ["unary_stream"]
        instance._channel._stream_unary_interceptors = ["stream_unary"]
        instance._channel._stream_stream_interceptors = ["stream_stream"]

        new_channel = instance.create_channel()
        channel_fn.assert_called_once_with()
        assert new_channel == channel_fn.return_value
        assert new_channel._unary_unary_interceptors == ["unary_unary"]
        assert new_channel._unary_stream_interceptors == ["unary_stream"]
        assert new_channel._stream_unary_interceptors == ["stream_unary"]
        assert new_channel._stream_stream_interceptors == ["stream_stream"]

    @pytest.mark.parametrize(
        "method_name,args,kwargs",
        [
            ("unary_unary", (1,), {"kw": 2}),
            ("unary_stream", (3,), {"kw": 4}),
            ("stream_unary", (5,), {"kw": 6}),
            ("stream_stream", (7,), {"kw": 8}),
            ("get_state", (), {"try_to_connect": True}),
        ],
    )
    def test_forwarded_methods(self, method_name, args, kwargs):
        channel_fn = mock.Mock()
        instance = self._make_one(channel_fn)
        method = getattr(instance, method_name)
        result = method(*args, **kwargs)
        mock_method = getattr(channel_fn.return_value, method_name)
        mock_method.assert_called_once_with(*args, **kwargs)
        assert result == mock_method.return_value

    @pytest.mark.parametrize(
        "method_name,args,kwargs",
        [
            ("channel_ready", (), {}),
            ("wait_for_state_change", (ChannelConnectivity.READY,), {}),
        ],
    )
    @CrossSync.pytest
    async def test_forwarded_async_methods(self, method_name, args, kwargs):
        async def dummy_coro(*a, **k):
            return mock.sentinel.result

        channel = mock.Mock()
        mock_method = getattr(channel, method_name)
        mock_method.side_effect = dummy_coro

        channel_fn = mock.Mock(return_value=channel)
        instance = self._make_one(channel_fn)
        method = getattr(instance, method_name)
        result = await method(*args, **kwargs)

        mock_method.assert_called_once_with(*args, **kwargs)
        assert result == mock.sentinel.result
