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

from gapic.utils import case


def test_pascal_to_snake():
    assert case.to_snake_case("PascalCaseThing") == "pascal_case_thing"


def test_camel_to_snake():
    assert case.to_snake_case("camelCaseThing") == "camel_case_thing"


def test_constant_to_snake():
    assert case.to_snake_case("CONSTANT_CASE_THING") == "constant_case_thing"


def test_pascal_to_camel():
    assert case.to_camel_case("PascalCaseThing") == "pascalCaseThing"


def test_snake_to_camel():
    assert case.to_camel_case("snake_case_thing") == "snakeCaseThing"


def test_constant_to_camel():
    assert case.to_camel_case("CONSTANT_CASE_THING") == "constantCaseThing"


def test_kebab_to_camel():
    assert case.to_camel_case("kebab-case-thing") == "kebabCaseThing"
