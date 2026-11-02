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


from gapic.utils import code


def test_empty_empty():
    assert code.empty("")


def test_empty_comments():
    assert code.empty("# The rain in Wales...\n# falls mainly...")


def test_empty_whitespace():
    assert code.empty("    ")


def test_empty_whitespace_comments():
    assert code.empty("    # The rain in Wales...")


def test_empty_code():
    assert not code.empty("import this")


def test_nth():
    # list
    assert code.nth([i * i for i in range(20)], 4) == 16
    # generator
    assert code.nth((i * i for i in range(20)), 4) == 16
    # default
    assert code.nth((i * i for i in range(20)), 30, 2112) == 2112


def test_make_private():
    # Regular case
    assert code.make_private("private_func") == "_private_func"

    # Starts with underscore
    assert code.make_private("_no_dunder_plz") == "_no_dunder_plz"
