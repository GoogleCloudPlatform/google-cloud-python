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

from unittest import mock

import pypandoc

from gapic import utils


def test_rst_unformatted():
    with mock.patch.object(pypandoc, "convert_text") as convert_text:
        assert utils.rst("The hail in Wales") == "The hail in Wales"
        assert convert_text.call_count == 0


def test_rst_formatted():
    with mock.patch.object(pypandoc, "convert_text") as convert_text:
        convert_text.side_effect = lambda *a, **kw: a[0].replace("`", "``")
        assert utils.rst("The hail in `Wales`") == "The hail in ``Wales``"
        assert convert_text.call_count == 1
        assert convert_text.mock_calls[0][1][1] == "rst"
        assert convert_text.mock_calls[0][2]["format"] == "commonmark"


def test_rst_add_newline():
    with mock.patch.object(pypandoc, "convert_text") as convert_text:
        s = "The hail in Wales\nfalls mainly on the snails."
        assert utils.rst(s) == s + "\n"
        assert convert_text.call_count == 0


def test_rst_force_add_newline():
    with mock.patch.object(pypandoc, "convert_text") as convert_text:
        s = "The hail in Wales"
        assert utils.rst(s, nl=True) == s + "\n"
        assert convert_text.call_count == 0


def test_rst_disable_add_newline():
    with mock.patch.object(pypandoc, "convert_text") as convert_text:
        s = "The hail in Wales\nfalls mainly on the snails."
        assert utils.rst(s, nl=False) == s
        assert convert_text.call_count == 0


def test_rst_pad_close_quote():
    with mock.patch.object(pypandoc, "convert_text") as convert_text:
        s = 'A value, as in "foo"'
        assert utils.rst(s) == s + "."
        assert convert_text.call_count == 0
