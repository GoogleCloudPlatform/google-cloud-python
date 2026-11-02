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

import copy

from gapic.schema import metadata
from gapic.schema import wrappers


def test_python_eq():
    meta = metadata.Metadata(
        address=metadata.Address(
            name="Foo",
            module="bar",
            package=("google", "api"),
        )
    )
    assert wrappers.PythonType(meta=meta) == wrappers.PythonType(
        meta=copy.copy(meta),
    )
    assert wrappers.PythonType(
        meta=metadata.Metadata(
            address=metadata.Address(name="Baz", module="bar", package=()),
        )
    ) != wrappers.PythonType(meta=meta)


def test_primitive_eq():
    assert wrappers.PrimitiveType.build(None) == None  # noqa: E711
    assert wrappers.PrimitiveType.build(int) == int
    assert wrappers.PrimitiveType.build(str) == str
    assert wrappers.PrimitiveType.build(bytes) == bytes
    assert wrappers.PrimitiveType.build(str) != bytes
    assert wrappers.PrimitiveType.build(int) == wrappers.PrimitiveType.build(
        int,
    )


def test_primitive_name():
    assert wrappers.PrimitiveType.build(int).name == "int"
