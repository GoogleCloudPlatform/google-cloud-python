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

from gapic.utils import filename


def test_to_valid_filename():
    assert filename.to_valid_filename("foo bar.py") == "foo-bar.py"
    assert filename.to_valid_filename("FOO") == "foo"
    assert filename.to_valid_filename("nom%&nom@nom.py") == "nom-nom-nom.py"
    assert filename.to_valid_filename("num_bear.py") == "num_bear.py"


def test_to_valid_module_name():
    assert filename.to_valid_module_name("foo bar.py") == "foo_bar.py"
    assert filename.to_valid_module_name("FOO") == "foo"
    assert filename.to_valid_module_name("nom%&nom.py") == "nom_nom.py"
    assert filename.to_valid_module_name("num_bear.py") == "num_bear.py"
