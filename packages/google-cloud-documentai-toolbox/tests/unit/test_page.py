# pylint: disable=protected-access
# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#


import pytest

from google.cloud import documentai
from google.cloud.documentai_toolbox import page


@pytest.fixture
def docproto():
    with open(
        "tests/unit/resources/0/toolbox_invoice_test-0.json", "r", encoding="utf-8"
    ) as f:
        return documentai.Document.from_json(f.read())


@pytest.fixture
def large_docproto():
    with open(
        "tests/unit/resources/multi_page/pretrained-ocr-v1.0-2020-09-23_output.json",
        "r",
        encoding="utf-8",
    ) as f:
        return documentai.Document.from_json(f.read())


@pytest.fixture
def docproto_with_symbols():
    with open(
        "tests/unit/resources/toolbox_invoice_test-with-symbols.json",
        "r",
        encoding="utf-8",
    ) as f:
        return documentai.Document.from_json(f.read())


@pytest.fixture
def docproto_with_math():
    with open(
        "tests/unit/resources/pretrained-ocr-v2.0-2023-06-02_math_output.json",
        "r",
        encoding="utf-8",
    ) as f:
        return documentai.Document.from_json(f.read())


@pytest.fixture
def docproto_form_parser():
    with open(
        "tests/unit/resources/form_parser/pretrained-form-parser-v1.0-2020-09-23_full-output.json",
        "r",
        encoding="utf-8",
    ) as f:
        return documentai.Document.from_json(f.read())


@pytest.fixture
def docproto_blank_document():
    with open("tests/unit/resources/blank_document.json", "r", encoding="utf-8") as f:
        return documentai.Document.from_json(f.read())


def test_table_to_csv(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    table = wrapped_page.tables[0]

    contents = table.to_dataframe().to_csv(index=False)

    assert (
        contents
        == """Item Description,Quantity,Price,Amount
Tool A,500,$1.00,$500.00
Service B,1,$900.00,$900.00
Resource C,50,$12.00,$600.00
,,Subtotal,$2000.00
,,Tax,$140.00
,,BALANCE DUE,$2140.00
"""
    )


def test_table_to_csv_with_empty_body_rows(docproto):
    docproto.pages[0].tables[0].body_rows = None
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    table = wrapped_page.tables[0]

    contents = table.to_dataframe().to_csv(index=False)

    assert (
        contents
        == """Item Description,Quantity,Price,Amount
"""
    )


def test_table_to_csv_with_empty_header_rows(docproto):
    docproto.pages[0].tables[0].header_rows = None
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    table = wrapped_page.tables[0]

    contents = table.to_dataframe().to_csv(index=False)

    assert (
        contents
        == """,,,
Tool A,500,$1.00,$500.00
Service B,1,$900.00,$900.00
Resource C,50,$12.00,$600.00
,,Subtotal,$2000.00
,,Tax,$140.00
,,BALANCE DUE,$2140.00
"""
    )


def test_table_to_csv_with_empty_header_rows_and_single_body(docproto):
    docproto.pages[0].tables[0].header_rows = None
    docproto.pages[0].tables[0].body_rows[0].cells = [
        docproto.pages[0].tables[0].body_rows[0].cells[0]
    ]
    docproto.pages[0].tables[0].body_rows = [docproto.pages[0].tables[0].body_rows[0]]
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    table = wrapped_page.tables[0]

    contents = table.to_dataframe().to_csv(index=False)
    assert (
        contents
        == """""
Tool A
"""
    )


def test_table_to_dataframe(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    table = wrapped_page.tables[0]
    contents = table.to_dataframe()

    assert len(contents.columns) == 4
    assert len(contents.values) == 6


def test_trim_text():
    input_text = "Sally\nWalker\n"
    output_text = page._trim_text(input_text)

    assert output_text == "Sally Walker"


def test_text_from_element_with_layout(docproto):
    docproto_page = docproto.pages[0]

    text = page._text_from_layout(
        layout=docproto_page.paragraphs[0].layout, text=docproto.text
    )

    assert text == "Invoice\n"


def test_get_hocr_bounding_box(docproto):
    hocr_bounding_box_normalized = page._get_hocr_bounding_box(
        element_with_layout=docproto.pages[0],
        page_dimension=docproto.pages[0].dimension,
    )

    assert hocr_bounding_box_normalized == "bbox 0 0 1758 2275"

    hocr_bounding_box_with_vertices = page._get_hocr_bounding_box(
        element_with_layout=docproto.pages[0].blocks[0],
        page_dimension=docproto.pages[0].dimension,
    )

    assert hocr_bounding_box_with_vertices == "bbox 1310 220 1534 282"


def test_get_hocr_bounding_box_with_blank_document(docproto_blank_document):
    hocr_bounding_box_normalized = page._get_hocr_bounding_box(
        element_with_layout=docproto_blank_document.pages[0],
        page_dimension=docproto_blank_document.pages[0].dimension,
    )

    assert hocr_bounding_box_normalized is None


# Class init Tests


def test_Table(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    docai_table = docproto.pages[0].tables[0]
    table = page.Table(documentai_object=docai_table, _page=wrapped_page)

    assert len(table.body_rows) == 6
    assert len(table.header_rows[0]) == 4


def test_FormField(docproto_form_parser):
    wrapped_page = page.Page(
        documentai_object=docproto_form_parser.pages[0],
        _document_text=docproto_form_parser.text,
    )
    docai_formfield = docproto_form_parser.pages[0].form_fields[4]
    form_field = page.FormField(documentai_object=docai_formfield, _page=wrapped_page)

    assert form_field.field_name == "Occupation:"
    assert form_field.field_value == "Software Engineer"
    # checking cached value
    assert form_field.field_name == "Occupation:"
    assert form_field.field_value == "Software Engineer"


def test_Block(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    docai_block = docproto.pages[0].blocks[0]
    block = page.Block(documentai_object=docai_block, _page=wrapped_page)

    assert block.text == "Invoice\n"
    assert block.hocr_bounding_box == "bbox 1310 220 1534 282"
    # checking cached value
    assert block.text == "Invoice\n"
    assert block.hocr_bounding_box == "bbox 1310 220 1534 282"

    assert block.paragraphs


def test_Paragraph(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    docai_paragraph = docproto.pages[0].paragraphs[0]
    paragraph = page.Paragraph(documentai_object=docai_paragraph, _page=wrapped_page)

    assert paragraph.text == "Invoice\n"
    assert paragraph.hocr_bounding_box == "bbox 1310 220 1534 282"
    # checking cached value
    assert paragraph.text == "Invoice\n"
    assert paragraph.hocr_bounding_box == "bbox 1310 220 1534 282"

    assert paragraph.lines


def test_Line(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    docai_line = docproto.pages[0].lines[36]
    line = page.Line(documentai_object=docai_line, _page=wrapped_page)

    assert line.text == "Supplies used for Project Q.\n"
    assert line.hocr_bounding_box == "bbox 223 1781 620 1818"
    # checking cached value
    assert line.text == "Supplies used for Project Q.\n"
    assert line.hocr_bounding_box == "bbox 223 1781 620 1818"

    assert line.tokens


def test_Token(docproto):
    wrapped_page = page.Page(
        documentai_object=docproto.pages[0], _document_text=docproto.text
    )
    docai_token = docproto.pages[0].tokens[85]
    token = page.Token(documentai_object=docai_token, _page=wrapped_page)

    assert token.text == "Q.\n"
    assert token.hocr_bounding_box == "bbox 585 1781 620 1818"
    # checking cached value
    assert token.text == "Q.\n"
    assert token.hocr_bounding_box == "bbox 585 1781 620 1818"

    assert token.symbols == []


def test_Symbol(docproto_with_symbols):
    wrapped_page = page.Page(
        documentai_object=docproto_with_symbols.pages[0],
        _document_text=docproto_with_symbols.text,
    )
    docai_symbol = docproto_with_symbols.pages[0].symbols[1]
    symbol = page.Symbol(documentai_object=docai_symbol, _page=wrapped_page)

    assert symbol.text == "n"
    assert symbol.hocr_bounding_box is None
    # checking cached value
    assert symbol.text == "n"
    assert symbol.hocr_bounding_box is None

    assert len(wrapped_page.symbols) > 0
    assert len(wrapped_page.tokens[0].symbols) > 0


def test_MathFormula(docproto_with_math):
    wrapped_page = page.Page(
        documentai_object=docproto_with_math.pages[0],
        _document_text=docproto_with_math.text,
    )

    docai_visual_element = docproto_with_math.pages[0].visual_elements[0]
    math_formula = page.MathFormula(
        documentai_object=docai_visual_element, _page=wrapped_page
    )

    assert math_formula
    assert math_formula.text == "\\int_{-\\infty}^{\\infty}e^{-x^{2}}dx=\\sqrt{x}.\n"
    assert math_formula.hocr_bounding_box is None
    # checking cached value
    assert math_formula.text == "\\int_{-\\infty}^{\\infty}e^{-x^{2}}dx=\\sqrt{x}.\n"
    assert math_formula.hocr_bounding_box is None

    assert len(wrapped_page.math_formulas) == 1
    assert (
        wrapped_page.math_formulas[0].text
        == "\\int_{-\\infty}^{\\infty}e^{-x^{2}}dx=\\sqrt{x}.\n"
    )


def test_Page(docproto):
    docproto_page = docproto.pages[0]

    wrapped_page = page.Page(
        documentai_object=docproto_page, _document_text=docproto.text
    )

    assert "Invoice" in wrapped_page._document_text
    assert "Invoice" in wrapped_page.text
    assert len(wrapped_page.text) > 0

    assert wrapped_page.page_number == 1

    assert len(wrapped_page.lines) == 37
    assert len(wrapped_page.paragraphs) == 31
    assert len(wrapped_page.blocks) == 31
    assert len(wrapped_page.tokens) == 86
    assert len(wrapped_page.form_fields) == 13
    assert len(wrapped_page.tables) == 1

    assert wrapped_page.lines[0].text == "Invoice\n"
    assert wrapped_page.lines[0].tokens[0].text == "Invoice\n"
    assert len(wrapped_page.lines[0].tokens) == 1

    assert wrapped_page.paragraphs[30].text == "Supplies used for Project Q.\n"
    assert len(wrapped_page.paragraphs[30].lines) == 1
    assert wrapped_page.paragraphs[30].lines[0].text == "Supplies used for Project Q.\n"
    assert wrapped_page.paragraphs[30].lines[0].tokens[0].text == "Supplies "

    assert wrapped_page.blocks[30].text == "Supplies used for Project Q.\n"

    assert (
        wrapped_page.blocks[30].paragraphs[0].text == "Supplies used for Project Q.\n"
    )
    assert (
        wrapped_page.blocks[30].paragraphs[0].lines[0].text
        == "Supplies used for Project Q.\n"
    )
    assert wrapped_page.blocks[30].paragraphs[0].lines[0].tokens[0].text == "Supplies "
    assert wrapped_page.tokens[85].text == "Q.\n"

    assert wrapped_page.symbols == []

    assert wrapped_page.hocr_bounding_box == "bbox 0 0 1758 2275"
    # checking cached value
    assert wrapped_page.hocr_bounding_box == "bbox 0 0 1758 2275"

    assert wrapped_page.form_fields[0].field_name == "BALANCE DUE"
    assert wrapped_page.form_fields[0].field_value == "$2140.00"

    assert wrapped_page.tables[0].header_rows[0][0] == "Item Description"
    assert wrapped_page.tables[0].body_rows[0][0] == "Tool A"


def test_page_elements_large_document(large_docproto):
    for pg in large_docproto.pages:
        wrapped_page = page.Page(
            documentai_object=pg, _document_text=large_docproto.text
        )
        for block in wrapped_page.blocks:
            assert block.text != ""
        for paragraph in wrapped_page.paragraphs:
            assert paragraph.text != ""
        for line in wrapped_page.lines:
            assert line.text != ""
        for token in wrapped_page.tokens:
            assert token.text != ""
