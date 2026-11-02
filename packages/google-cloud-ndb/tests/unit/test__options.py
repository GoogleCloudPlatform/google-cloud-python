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

from google.cloud.ndb import _datastore_api, _options, utils


class MyOptions(_options.Options):
    __slots__ = ["foo", "bar"]


class TestOptions:
    @staticmethod
    def test_constructor_w_bad_arg():
        with pytest.raises(TypeError):
            MyOptions(kind="test")

    @staticmethod
    def test_constructor_w_deadline():
        options = MyOptions(deadline=20)
        assert options.timeout == 20

    @staticmethod
    def test_constructor_w_deadline_and_timeout():
        with pytest.raises(TypeError):
            MyOptions(timeout=20, deadline=10)

    @staticmethod
    def test_constructor_w_use_memcache():
        options = MyOptions(use_memcache=True)
        assert options.use_global_cache is True

    @staticmethod
    def test_constructor_w_use_global_cache():
        options = MyOptions(use_global_cache=True)
        assert options.use_global_cache is True

    @staticmethod
    def test_constructor_w_use_memcache_and_global_cache():
        with pytest.raises(TypeError):
            MyOptions(use_global_cache=True, use_memcache=False)

    @staticmethod
    def test_constructor_w_use_datastore():
        options = MyOptions(use_datastore=False)
        assert options.use_datastore is False

    @staticmethod
    def test_constructor_w_use_cache():
        options = MyOptions(use_cache=20)
        assert options.use_cache == 20

    @staticmethod
    def test_constructor_w_memcache_timeout():
        options = MyOptions(memcache_timeout=20)
        assert options.global_cache_timeout == 20

    @staticmethod
    def test_constructor_w_global_cache_timeout():
        options = MyOptions(global_cache_timeout=20)
        assert options.global_cache_timeout == 20

    @staticmethod
    def test_constructor_w_memcache_and_global_cache_timeout():
        with pytest.raises(TypeError):
            MyOptions(memcache_timeout=20, global_cache_timeout=20)

    @staticmethod
    def test_constructor_w_max_memcache_items():
        with pytest.raises(NotImplementedError):
            MyOptions(max_memcache_items=20)

    @staticmethod
    def test_constructor_w_force_writes():
        with pytest.raises(NotImplementedError):
            MyOptions(force_writes=20)

    @staticmethod
    def test_constructor_w_propagation():
        with pytest.raises(NotImplementedError):
            MyOptions(propagation=20)

    @staticmethod
    def test_constructor_w_xg():
        options = MyOptions(xg=True)
        assert options == MyOptions()

    @staticmethod
    def test_constructor_with_config():
        config = MyOptions(retries=5, foo="config_test")
        options = MyOptions(config=config, retries=8, bar="app")
        assert options.retries == 8
        assert options.bar == "app"
        assert options.foo == "config_test"

    @staticmethod
    def test_constructor_with_bad_config():
        with pytest.raises(TypeError):
            MyOptions(config="bad")

    @staticmethod
    def test___repr__():
        representation = "MyOptions(foo='test', bar='app')"
        options = MyOptions(foo="test", bar="app")
        assert options.__repr__() == representation

    @staticmethod
    def test__eq__():
        options = MyOptions(foo="test", bar="app")
        other = MyOptions(foo="test", bar="app")
        otherother = MyOptions(foo="nope", bar="noway")

        assert options == other
        assert options != otherother
        assert options != "foo"

    @staticmethod
    def test_copy():
        options = MyOptions(retries=8, bar="app")
        options = options.copy(bar="app2", foo="foo")
        assert options.retries == 8
        assert options.bar == "app2"
        assert options.foo == "foo"

    @staticmethod
    def test_items():
        options = MyOptions(retries=8, bar="app")
        items = [(key, value) for key, value in options.items() if value is not None]
        assert items == [("bar", "app"), ("retries", 8)]

    @staticmethod
    def test_options():
        @MyOptions.options
        @utils.positional(4)
        def hi(mom, foo=None, retries=None, timeout=None, _options=None):
            return mom, _options

        assert hi("mom", "bar", 23, timeout=42) == (
            "mom",
            MyOptions(foo="bar", retries=23, timeout=42),
        )

    @staticmethod
    def test_options_bad_signature():
        @utils.positional(2)
        def hi(foo, mom):
            pass

        with pytest.raises(TypeError):
            MyOptions.options(hi)

        hi("mom", "!")  # coverage

    @staticmethod
    def test_options_delegated():
        @MyOptions.options
        @utils.positional(4)
        def hi(mom, foo=None, retries=None, timeout=None, _options=None):
            return mom, _options

        options = MyOptions(foo="bar", retries=23, timeout=42)
        assert hi("mom", "baz", 24, timeout=43, _options=options) == (
            "mom",
            options,
        )


class TestReadOptions:
    @staticmethod
    def test_constructor_w_read_policy():
        options = _options.ReadOptions(read_policy=_datastore_api.EVENTUAL_CONSISTENCY)
        assert options == _options.ReadOptions(read_consistency=_datastore_api.EVENTUAL)

    @staticmethod
    def test_constructor_w_read_policy_and_read_consistency():
        with pytest.raises(TypeError):
            _options.ReadOptions(
                read_policy=_datastore_api.EVENTUAL_CONSISTENCY,
                read_consistency=_datastore_api.EVENTUAL,
            )
