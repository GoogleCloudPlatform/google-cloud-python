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
"""Wrappers for Document AI Page type."""

import dataclasses
from abc import ABC
from functools import cached_property
from typing import Iterable, List, Optional, Type, TypeVar

import pandas as pd

from google.cloud import documentai
from google.cloud.documentai_toolbox.constants import ElementWithLayout
from google.cloud.documentai_toolbox.utilities import docai_utilities

T = TypeVar("T", bound="_BasePageElement")


@dataclasses.dataclass
class Table:
    """Represents a wrapped documentai.Document.Page.Table.

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.Table):
            Required. The original object.
        body_rows (List[List[str]]):
            Required. A list of body rows.
        header_rows (List[List[str]]):
            Required. A list of header rows.
    """

    documentai_object: documentai.Document.Page.Table = dataclasses.field(repr=False)
    _page: "Page" = dataclasses.field(repr=False)

    @cached_property
    def body_rows(self) -> List[List[str]]:
        return self._extract_table_rows(self.documentai_object.body_rows)

    @cached_property
    def header_rows(self) -> List[List[str]]:
        return self._extract_table_rows(self.documentai_object.header_rows)

    def to_dataframe(self) -> pd.DataFrame:
        """Returns pd.DataFrame from documentai.table

        Returns:
            pd.DataFrame:
                The DataFrame of the table.
        """
        if not self.body_rows:
            return pd.DataFrame(columns=self.header_rows)

        columns = (
            pd.MultiIndex.from_arrays(self.header_rows)
            if self.header_rows
            else [None] * len(self.body_rows[0])
        )

        return pd.DataFrame(self.body_rows, columns=columns)

    def _extract_table_rows(
        self, table_rows: Iterable[documentai.Document.Page.Table.TableRow]
    ) -> List[List[str]]:
        """Returns a list of rows from table_rows.

        Args:
            table_rows (List[documentai.Document.Page.Table.TableRow]):
                Required. A documentai.Document.Page.Table.TableRow.

        Returns:
            List[List[str]]:
                A list of table rows.
        """
        return [
            [
                # Newlines removed to improve formatting for export formats.
                _text_from_layout(cell.layout, self._page._document_text).replace(
                    "\n", ""
                )
                for cell in row.cells
            ]
            for row in table_rows
        ]


@dataclasses.dataclass
class FormField:
    """Represents a wrapped documentai.Document.Page.FormField.

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.FormField):
            Required. The original object.
        field_name (str):
            Required. The form field name
        field_value (str):
            Required. The form field value
    """

    documentai_object: documentai.Document.Page.FormField = dataclasses.field(
        repr=False
    )
    _page: "Page" = dataclasses.field(repr=False)

    @cached_property
    def field_name(self) -> str:
        return _trim_text(
            _text_from_layout(
                self.documentai_object.field_name, self._page._document_text
            )
        )

    @cached_property
    def field_value(self) -> str:
        return _trim_text(
            _text_from_layout(
                self.documentai_object.field_value, self._page._document_text
            )
        )


def _trim_text(text: str) -> str:
    """Remove extra space characters from text (blank, newline, tab, etc.)

    Args:
        text (str):
            Required. UTF-8 encoded text in reading order
            from the document.

    Returns:
        str:
            Text without trailing spaces/newlines
    """
    # Newline replacement added to correct common
    # misshapen output from Form Parser.
    return text.strip().replace("\n", " ")


@dataclasses.dataclass
class _BasePageElement(ABC):
    """Base class for representing a wrapped Document AI Page element (Symbol, Token, Line, Paragraph, Block)."""

    documentai_object: ElementWithLayout = dataclasses.field(repr=False)
    _page: "Page" = dataclasses.field(repr=False)

    @cached_property
    def text(self) -> str:
        """
        Text of the page element.
        """
        return _text_from_layout(
            self.documentai_object.layout, self._page._document_text
        )

    @cached_property
    def hocr_bounding_box(self) -> Optional[str]:
        """
        hOCR bounding box of the page element.
        """
        return _get_hocr_bounding_box(
            self.documentai_object, self._page.documentai_object.dimension
        )

    # This field is a cached property to improve export times for hOCR
    # as outlined in https://github.com/googleapis/python-documentai-toolbox/issues/312
    @cached_property
    def _text_segment(self) -> documentai.Document.TextAnchor.TextSegment:
        """
        Page element text segment.
        """
        return self.documentai_object.layout.text_anchor.text_segments[0]

    def _get_children_of_element(self, potential_children: List[T]) -> List[T]:
        """
        Filters potential child elements to identify only those fully contained within this element.

        This method iterates through a list of potential child elements, checking if their
        start and end indices fall completely within the start and end indices of this element.
        Elements that are only partially contained or entirely outside this element's range are excluded.

        Args:
            potential_children (List[_BasePageElement]):
                Required. A list of wrapped page elements (e.g., words, lines, paragraphs)
                that could potentially be children of this element.

        Returns:
            List[_BasePageElement]:
                A new list containing only the wrapped page elements that are fully
                contained within this element, maintaining their original order.
        """
        start_index = self._text_segment.start_index
        end_index = self._text_segment.end_index

        children = []
        for child in potential_children:
            child_start_index = child._text_segment.start_index
            child_end_index = child._text_segment.end_index

            if child_start_index >= end_index:
                break  # Optimization: stop early if child is beyond the end of this element
            if (
                start_index <= child_start_index < end_index
                and start_index < child_end_index <= end_index
            ):
                children.append(child)
        return children


@dataclasses.dataclass
class Symbol(_BasePageElement):
    """Represents a wrapped documentai.Document.Page.Symbol.
    https://cloud.google.com/document-ai/docs/process-documents-ocr#enable_symbols

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.Symbol):
            Required. The original object.
        text (str):
            Required. The text of the Symbol.
    """

    @cached_property
    def hocr_bounding_box(self) -> Optional[str]:
        # Symbols are not represented in hOCR
        return None


@dataclasses.dataclass
class Token(_BasePageElement):
    """Represents a wrapped documentai.Document.Page.Token.

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.Token):
            Required. The original object.
        text (str):
            Required. The text of the Token.
        symbols (List[Symbol]):
            Optional. The Symbols contained within the Token.
    """

    @cached_property
    def symbols(self) -> List[Symbol]:
        return self._get_children_of_element(self._page.symbols)


@dataclasses.dataclass
class Line(_BasePageElement):
    """Represents a wrapped documentai.Document.Page.Line.

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.Line):
            Required. The original object.
        text (str):
            Required. The text of the Line.
        tokens (List[Token]):
            Optional. The Tokens contained within the Line.
    """

    @cached_property
    def tokens(self) -> List[Token]:
        return self._get_children_of_element(self._page.tokens)


@dataclasses.dataclass
class Paragraph(_BasePageElement):
    """Represents a wrapped documentai.Document.Page.Paragraph.

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.Paragraph):
            Required. The original object.
        text (str):
            Required. The text of the Paragraph.
        lines (List[Line]):
            Optional. The Lines contained within the Paragraph.
    """

    @cached_property
    def lines(self) -> List[Line]:
        return self._get_children_of_element(self._page.lines)


@dataclasses.dataclass
class Block(_BasePageElement):
    """Represents a wrapped documentai.Document.Page.Block.

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.Block):
            Required. The original object.
        text (str):
            Required. The text of the Block.
        paragraphs (List[Paragraph]):
            Optional. The Paragraphs contained within the Block.
    """

    @cached_property
    def paragraphs(self) -> List[Paragraph]:
        return self._get_children_of_element(self._page.paragraphs)


@dataclasses.dataclass
class MathFormula(_BasePageElement):
    """Represents a wrapped documentai.Document.Page.VisualElement with type `math_formula`.
    https://cloud.google.com/document-ai/docs/process-documents-ocr#math_ocr

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page.VisualElement):
            Required. The original object.
        text (str):
            Required. The text of the MathFormula.
    """

    @cached_property
    def hocr_bounding_box(self):
        # Math Formulas are not represented in hOCR
        return None


def _get_hocr_bounding_box(
    element_with_layout: ElementWithLayout,
    page_dimension: documentai.Document.Page.Dimension,
) -> Optional[str]:
    """Returns a hOCR bounding box string.

    Args:
        element_with_layout (ElementWithLayout):
            Required. an element with layout fields.
        dimension (documentai.Document.Page.Dimension):
            Required. Page dimension.

    Returns:
        Optional[str]:
            hOCR bounding box string.
    """
    if not element_with_layout.layout.bounding_poly:
        return None

    bbox = docai_utilities.get_bounding_box(
        bounding_poly=element_with_layout.layout.bounding_poly,
        page_dimension=page_dimension,
    )

    if not bbox:
        return None

    min_x, min_y, max_x, max_y = bbox
    return f"bbox {min_x} {min_y} {max_x} {max_y}"


def _text_from_layout(layout: documentai.Document.Page.Layout, text: str) -> str:
    r"""Returns a text from a single layout element.

    Args:
        layout (documentai.Document.Page.Layout):
            Required. An element with layout fields.
        text (str):
            Required. UTF-8 encoded text in reading order
            of the `documentai.Document` containing the layout element.

    Returns:
        str:
            Text from a single element.
    """
    if not layout.text_anchor or not layout.text_anchor.text_segments:
        return ""

    # Note: `layout.text_anchor.text_segments` are indexes into the full Document text.
    # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document#textsegment
    return "".join(
        text[int(segment.start_index) : int(segment.end_index)]
        for segment in layout.text_anchor.text_segments
    )


@dataclasses.dataclass
class Page:
    """Represents a wrapped documentai.Document.Page .

    Attributes:
        documentai_object (google.cloud.documentai.Document.Page):
            Required. The original object.
        text (str):
            Required. UTF-8 encoded text of the page.
        page_number (int):
            Required. The page number of the `Page`.
        hocr_bounding_box (str):
            Required. hOCR bounding box of the page element.
        symbols (List[Symbol]):
            Optional. A list of visually detected text symbols
            (characters/letters) on the page.
        tokens (List[Token]):
            Required. A list of visually detected text tokens (words) on the
            page.
        lines (List[Line]):
            Required. A list of visually detected text lines on the
            page. A collection of tokens that a human would
            perceive as a line.
        paragraphs (List[Paragraph]):
            Required. A list of visually detected text paragraphs
            on the page. A collection of lines that a human
            would perceive as a paragraph.
        blocks (List[Block]):
            Required. A list of visually detected text blocks
            on the page. A collection of lines that a human
            would perceive as a block.
        form_fields (List[FormField]):
            Optional. A list of visually detected form fields on the
            page.
        tables (List[Table]):
            Optional. A list of visually detected tables on the
            page.
        math_formulas (List[MathFormula]):
            Optional. A list of visually detected math formulas
            on the page.
    """

    documentai_object: documentai.Document.Page = dataclasses.field(repr=False)
    _document_text: str = dataclasses.field(repr=False)

    def _get_elements(self, element_type: Type, attribute_name: str) -> List:
        """
        Helper method to create elements based on specified type.
        """
        elements = getattr(self.documentai_object, attribute_name)
        return [
            element_type(documentai_object=element, _page=self) for element in elements
        ]

    @cached_property
    def text(self):
        return _text_from_layout(
            self.documentai_object.layout, text=self._document_text
        )

    @cached_property
    def page_number(self):
        return self.documentai_object.page_number

    @cached_property
    def tables(self):
        return self._get_elements(Table, "tables")

    @cached_property
    def form_fields(self):
        return self._get_elements(FormField, "form_fields")

    @cached_property
    def math_formulas(self):
        return [
            MathFormula(documentai_object=visual_element, _page=self)
            for visual_element in self.documentai_object.visual_elements
            if visual_element.type_ == "math_formula"
        ]

    @cached_property
    def symbols(self):
        return self._get_elements(Symbol, "symbols")

    @cached_property
    def tokens(self):
        return self._get_elements(Token, "tokens")

    @cached_property
    def lines(self):
        return self._get_elements(Line, "lines")

    @cached_property
    def paragraphs(self):
        return self._get_elements(Paragraph, "paragraphs")

    @cached_property
    def blocks(self):
        return self._get_elements(Block, "blocks")

    @cached_property
    def hocr_bounding_box(self):
        return _get_hocr_bounding_box(
            self.documentai_object, self.documentai_object.dimension
        )
