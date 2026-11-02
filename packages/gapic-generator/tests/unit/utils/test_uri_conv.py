# Copyright 2021 Google LLC
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


import pypandoc

from gapic import utils


def test_convert_uri_fieldname():
    uri = "abc/*/license/{license}/{xyz.class=class/*}"
    expected_uri = "abc/*/license/{license_}/{xyz.class_=class/*}"
    assert utils.convert_uri_fieldnames(uri) == expected_uri


def test_convert_uri_fieldname_no_fields():
    uri = "abc/license"
    assert utils.convert_uri_fieldnames(uri) == uri


def test_convert_uri_fieldname_no_reserved_names():
    uri = "abc/*/books/{book}/{xyz.chapter=page/*}"
    assert utils.convert_uri_fieldnames(uri) == uri
