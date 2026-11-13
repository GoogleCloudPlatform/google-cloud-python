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

from gapic.schema import imp


def test_str():
    i = imp.Import(package=("foo", "bar"), module="baz")
    assert str(i) == "from foo.bar import baz"


def test_str_no_package():
    i = imp.Import(package=(), module="baz")
    assert str(i) == "import baz"


def test_str_alias():
    i = imp.Import(package=("foo", "bar"), module="baz", alias="bacon")
    assert str(i) == "from foo.bar import baz as bacon"


def test_str_untyped_pb2():
    i = imp.Import(package=("foo", "bar"), module="baz_pb2", alias="bacon")
    assert str(i) == "import foo.bar.baz_pb2 as bacon  # type: ignore"


def test_str_untyped_api_core():
    i = imp.Import(package=("foo", "api_core"), module="baz", alias="bacon")
    assert str(i) == "import foo.api_core.baz as bacon  # type: ignore"


def test_str_typed_resumable_transfer():
    # Verify that google.api_core.resumable_transfer is imported without "# type: ignore".
    i = imp.Import(package=("google", "api_core"), module="resumable_transfer")
    assert str(i) == "from google.api_core import resumable_transfer"


def test_str_eq():
    i1 = imp.Import(package=("foo", "bar"), module="baz")
    i2 = imp.Import(package=("foo", "bar"), module="baz")
    i3 = imp.Import(package=("foo", "bar"), module="baz", alias="bacon")
    j1 = imp.Import(package=("foo", "bar"), module="not_baz")
    k1 = imp.Import(package=("spam", "eggs"), module="baz")
    assert i1 == i2
    assert i1 == i3
    assert i2 == i3
    assert i1 != j1
    assert i1 != k1
