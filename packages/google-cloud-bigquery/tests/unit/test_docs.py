# Copyright 2026 Google LLC
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

import pathlib
import runpy
import sys
import types
from unittest import mock

import pytest


def test_docs_conf_executes_successfully():
    docs_dir = pathlib.Path(__file__).parent.parent.parent / "docs"
    conf_path = docs_dir / "conf.py"
    if not conf_path.exists():
        pytest.skip("docs/conf.py not found")

    res = runpy.run_path(str(conf_path))

    assert res.get("project") == "google-cloud-bigquery"


@pytest.fixture
def fake_translator_and_mock():
    docs_dir = pathlib.Path(__file__).parent.parent.parent / "docs"
    conf_path = docs_dir / "conf.py"
    if not conf_path.exists():
        pytest.skip("docs/conf.py not found")

    mock_orig_depart = mock.MagicMock(return_value="original_output")

    class FakeTranslator:
        depart_paragraph = mock_orig_depart
        depart_compact_paragraph = mock_orig_depart

    fake_module = types.ModuleType("sphinx_markdown_builder.markdown_writer")
    fake_module.MarkdownTranslator = FakeTranslator

    with mock.patch.dict(
        sys.modules,
        {
            "sphinx_markdown_builder": types.ModuleType("sphinx_markdown_builder"),
            "sphinx_markdown_builder.markdown_writer": fake_module,
        },
    ):
        runpy.run_path(str(conf_path))

    return FakeTranslator, mock_orig_depart


def test_depart_paragraph_suppresses_newlines_inside_table_cells(
    fake_translator_and_mock,
):
    FakeTranslator, mock_orig_depart = fake_translator_and_mock
    translator = FakeTranslator()
    translator.table_entries = ["cell"]
    node = mock.MagicMock()

    res_paragraph = FakeTranslator.depart_paragraph(translator, node)
    res_compact = FakeTranslator.depart_compact_paragraph(translator, node)

    assert res_paragraph is None
    assert res_compact is None
    mock_orig_depart.assert_not_called()


def test_depart_paragraph_delegates_outside_table_cells(
    fake_translator_and_mock,
):
    FakeTranslator, mock_orig_depart = fake_translator_and_mock
    translator = FakeTranslator()
    node = mock.MagicMock()

    res_paragraph = FakeTranslator.depart_paragraph(translator, node)
    res_compact = FakeTranslator.depart_compact_paragraph(translator, node)

    assert res_paragraph == "original_output"
    assert res_compact == "original_output"
    assert mock_orig_depart.call_count == 2
    mock_orig_depart.assert_has_calls(
        [
            mock.call(translator, node),
            mock.call(translator, node),
        ]
    )
