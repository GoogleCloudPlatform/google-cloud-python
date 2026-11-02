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

import threading
from unittest import mock

import pytest

from google.cloud.ndb import utils


class Test_asbool:
    @staticmethod
    def test_None():
        assert utils.asbool(None) is False

    @staticmethod
    def test_bool():
        assert utils.asbool(True) is True
        assert utils.asbool(False) is False

    @staticmethod
    def test_truthy_int():
        assert utils.asbool(0) is False
        assert utils.asbool(1) is True

    @staticmethod
    def test_truthy_string():
        assert utils.asbool("Y") is True
        assert utils.asbool("f") is False


def test_code_info():
    with pytest.raises(NotImplementedError):
        utils.code_info()


def test_decorator():
    with pytest.raises(NotImplementedError):
        utils.decorator()


def test_frame_info():
    with pytest.raises(NotImplementedError):
        utils.frame_info()


def test_func_info():
    with pytest.raises(NotImplementedError):
        utils.func_info()


def test_gen_info():
    with pytest.raises(NotImplementedError):
        utils.gen_info()


def test_get_stack():
    with pytest.raises(NotImplementedError):
        utils.get_stack()


class Test_logging_debug:
    @staticmethod
    @mock.patch("google.cloud.ndb.utils.DEBUG", False)
    def test_noop():
        log = mock.Mock(spec=("debug",))
        utils.logging_debug(log, "hello dad! {} {where}", "I'm", where="in jail")
        log.debug.assert_not_called()

    @staticmethod
    @mock.patch("google.cloud.ndb.utils.DEBUG", True)
    def test_log_it():
        log = mock.Mock(spec=("debug",))
        utils.logging_debug(log, "hello dad! {} {where}", "I'm", where="in jail")
        log.debug.assert_called_once_with("hello dad! I'm in jail")


def test_positional():
    @utils.positional(2)
    def test_func(a=1, b=2, **kwargs):
        return a, b

    @utils.positional(1)
    def test_func2(a=3, **kwargs):
        return a

    with pytest.raises(TypeError):
        test_func(1, 2, 3)

    with pytest.raises(TypeError):
        test_func2(1, 2)

    assert test_func(4, 5, x=0) == (4, 5)
    assert test_func(6) == (6, 2)

    assert test_func2(6) == 6


def test_keyword_only():
    @utils.keyword_only(foo=1, bar=2, baz=3)
    def test_kwonly(**kwargs):
        return kwargs["foo"], kwargs["bar"], kwargs["baz"]

    with pytest.raises(TypeError):
        test_kwonly(faz=4)

    assert test_kwonly() == (1, 2, 3)
    assert test_kwonly(foo=3, bar=5, baz=7) == (3, 5, 7)
    assert test_kwonly(baz=7) == (1, 2, 7)


def test_threading_local():
    assert utils.threading_local is threading.local


def test_tweak_logging():
    with pytest.raises(NotImplementedError):
        utils.tweak_logging()


def test_wrapping():
    with pytest.raises(NotImplementedError):
        utils.wrapping()
