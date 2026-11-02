# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
"""Helper functions for docproto to vision conversion."""

import dataclasses
from typing import List

import immutabledict
from google.cloud.documentai import Document
from google.cloud.vision import (
    AnnotateImageResponse,
    Block,
    EntityAnnotation,
    ImageAnnotationContext,
    Page,
    Paragraph,
    Symbol,
    TextAnnotation,
    Word,
)

from google.cloud import vision
from google.cloud.documentai_toolbox.constants import ElementWithLayout

_BREAK_TYPE_MAP = immutabledict.immutabledict(
    {
        Document.Page.Token.DetectedBreak.Type.SPACE: (
            TextAnnotation.DetectedBreak.BreakType.SPACE
        ),
        Document.Page.Token.DetectedBreak.Type.WIDE_SPACE: (
            TextAnnotation.DetectedBreak.BreakType.LINE_BREAK
        ),
        Document.Page.Token.DetectedBreak.Type.HYPHEN: (
            TextAnnotation.DetectedBreak.BreakType.HYPHEN
        ),
    }
)


@dataclasses.dataclass
class PageInfo:
    page: Document.Page
    text: str = ""
    page_idx: int = 0
    block_idx: int = 0
    paragraph_idx: int = 0
    token_idx: int = 0
    symbol_idx: int = 0


def _get_text_anchor_substring(text: str, text_anchor: Document.TextAnchor) -> str:
    """Gets text corresponding to the TextAnchor."""
    return "".join(
        [
            text[text_segment.start_index : text_segment.end_index]
            for text_segment in text_anchor.text_segments
        ]
    )


def _has_text_segment(layout: Document.Page.Layout) -> bool:
    """Checks if the layout has not empty text_segments."""
    if layout.text_anchor.text_segments:
        return True
    return False


def _convert_common_info(
    src: ElementWithLayout, dest: ElementWithLayout, page_info: PageInfo
):
    """Copy common data such as languages and bounding poly from src to dest.

    Args:
      src:
        source message that contains common data such as languages and bounding
        poly.
      dest:
        destination message that common data converts to.
      page_info (PageInfo):
        provides dimension information to help convert between vertices
        and normalized vertices.
    """
    dest.confidence = src.layout.confidence
    for language in src.detected_languages:
        dest.property.detected_languages.append(
            TextAnnotation.DetectedLanguage(
                language_code=language.language_code, confidence=language.confidence
            )
        )

    if src.layout.bounding_poly.vertices:
        for scr_vertex in src.layout.bounding_poly.vertices:
            dest.bounding_box.vertices.append(
                {"x": int(scr_vertex.x), "y": int(scr_vertex.y)}
            )
    else:
        for scr_normalized_vertex in src.layout.bounding_poly.normalized_vertices:
            dest.bounding_box.vertices.append(
                {
                    "x": int(scr_normalized_vertex.x * page_info.page.dimension.width),
                    "y": int(scr_normalized_vertex.y * page_info.page.dimension.height),
                }
            )
    for scr_normalized_vertex in src.layout.bounding_poly.normalized_vertices:
        dest.bounding_box.normalized_vertices.append(
            {"x": scr_normalized_vertex.x, "y": scr_normalized_vertex.y}
        )


def _is_layout_included(
    inner: Document.Page.Layout,
    outer: Document.Page.Layout,
) -> bool:
    """Checks if the inner layout is within the scope of the outer layout."""
    if not _has_text_segment(inner) or not _has_text_segment(outer):
        return False
    return (
        inner.text_anchor.text_segments[0].start_index
        >= outer.text_anchor.text_segments[0].start_index
        and inner.text_anchor.text_segments[0].end_index
        <= outer.text_anchor.text_segments[0].end_index
    )


def _convert_document_symbol(
    page_info: PageInfo,
    break_type: Document.Page.Token.DetectedBreak.Type,
) -> List[Symbol]:
    """Converts document symbols to vision symbols.

    Args:
      page_info (PageInfo):
        Current page information, including document page to be converted,
        its text, and the position of reading cursor.
      break_type (Document.Page.Token.DetectedBreak.Type):
        The break type of the current word that needs to be added to the
        last vision symbol.

    Returns:
        List[Symbol]:
            Symbols filled with OCR data that are within
            current document token.
    """
    vision_symbols = []
    doc_symbols = page_info.page.symbols
    cur_doc_token = page_info.page.tokens[page_info.token_idx]
    while page_info.symbol_idx < len(doc_symbols) and _is_layout_included(
        doc_symbols[page_info.symbol_idx].layout, cur_doc_token.layout
    ):
        vision_symbols.append(
            Symbol(
                text=_get_text_anchor_substring(
                    page_info.text,
                    doc_symbols[page_info.symbol_idx].layout.text_anchor,
                )
            )
        )
        _convert_common_info(
            doc_symbols[page_info.symbol_idx], vision_symbols[-1], page_info
        )

        page_info.symbol_idx += 1
    # Add the break_type to the last symbol.
    if (
        vision_symbols
        and break_type != Document.Page.Token.DetectedBreak.Type.TYPE_UNSPECIFIED
    ):
        vision_symbols[-1].property.detected_break.type = (
            _BREAK_TYPE_MAP[break_type]
            if break_type in _BREAK_TYPE_MAP
            else TextAnnotation.DetectedBreak.BreakType.UNKNOWN
        )
    return vision_symbols


def _convert_document_token(
    page_info: PageInfo,
) -> List[Word]:
    """Converts document tokens to vision words.

    Args:
      page_info (PageInfo):
        Current page information, including document page to be converted,
        its text, and the position of reading cursor.

    Returns:
        List[Word]:
            Word filled with OCR data that are within
            current document paragraph.
    """
    vision_words = []
    doc_tokens = page_info.page.tokens
    cur_doc_paragraph = page_info.page.paragraphs[page_info.paragraph_idx]
    while page_info.token_idx < len(doc_tokens) and _is_layout_included(
        doc_tokens[page_info.token_idx].layout, cur_doc_paragraph.layout
    ):
        doc_break_type = doc_tokens[page_info.token_idx].detected_break.type
        vision_break_type = (
            _BREAK_TYPE_MAP[doc_break_type]
            if doc_break_type in _BREAK_TYPE_MAP
            else TextAnnotation.DetectedBreak.BreakType.UNKNOWN
        )
        vision_words.append(
            Word(
                symbols=_convert_document_symbol(page_info, doc_break_type),
                property=TextAnnotation.TextProperty(
                    detected_break=TextAnnotation.DetectedBreak(type=vision_break_type)
                ),
            )
        )
        _convert_common_info(
            doc_tokens[page_info.token_idx], vision_words[-1], page_info
        )
        page_info.token_idx += 1
    return vision_words


def _generate_entity_annotations(
    page_info: PageInfo,
) -> List[EntityAnnotation]:
    """Generate a list of EntityAnnotations from Document.

    Args:
      page_info: Current page information, including document page to be converted
        , its text, and the position of reading cursor.

    Returns:
      A list of EntityAnnotations with descriptions and bounding box populated. A
      EntityAnnotation has a word level information.
    """
    entity_annotations: List[EntityAnnotation] = []
    for token in page_info.page.tokens:
        v: list[vision.Vertex] = []
        if token.layout.bounding_poly.vertices:
            for vertex in token.layout.bounding_poly.vertices:
                v.append(vision.Vertex(x=int(vertex.x), y=int(vertex.y)))
        else:
            for normalized_vertex in token.layout.bounding_poly.normalized_vertices:
                v.append(
                    vision.Vertex(
                        x=int(normalized_vertex.x * page_info.page.dimension.width),
                        y=int(normalized_vertex.y * page_info.page.dimension.height),
                    )
                )

        text_start_index = token.layout.text_anchor.text_segments[0].start_index
        text_end_index = token.layout.text_anchor.text_segments[0].end_index
        # The word in docai response contains the break text. Remove the break text.
        if (
            token.detected_break
            != Document.Page.Token.DetectedBreak.Type.TYPE_UNSPECIFIED
        ):
            text_end_index -= 1

        e = EntityAnnotation(
            description=page_info.text[text_start_index:text_end_index]
        )

        e.bounding_poly.vertices = v

        entity_annotations.append(e)
    return entity_annotations


def _convert_document_paragraph(
    page_info: PageInfo,
) -> List[Paragraph]:
    """Converts document paragraphs to vision paragraphs.

    Args:
      page_info (PageInfo):
        Current page information, including document page to be converted,
        its text, and the position of reading cursor.

    Returns:
        List[Paragraph]:
            Paragraph filled with OCR data that are within
            current document block.
    """
    vision_paragraphs = []
    doc_paragraphs = page_info.page.paragraphs
    cur_doc_block = page_info.page.blocks[page_info.block_idx]
    while page_info.paragraph_idx < len(doc_paragraphs) and _is_layout_included(
        doc_paragraphs[page_info.paragraph_idx].layout, cur_doc_block.layout
    ):
        vision_paragraphs.append(Paragraph(words=_convert_document_token(page_info)))
        _convert_common_info(
            doc_paragraphs[page_info.paragraph_idx],
            vision_paragraphs[-1],
            page_info,
        )

        page_info.paragraph_idx += 1
    return vision_paragraphs


def _convert_document_block(
    page_info: PageInfo,
) -> List[Block]:
    """Converts document blocks to vision blocks.

    Args:
      page_info (PageInfo): Current page information, including document page to be converted,
      its text, and the position of reading cursor.

    Returns:
        List[Block]:
            Block filled with OCR data that are within the
            current document page.
    """
    vision_blocks = []
    while page_info.block_idx < len(page_info.page.blocks):
        vision_blocks.append(
            Block(
                block_type=Block.BlockType.TEXT,
                paragraphs=_convert_document_paragraph(page_info),
            )
        )
        _convert_common_info(
            page_info.page.blocks[page_info.block_idx], vision_blocks[-1], page_info
        )

        page_info.block_idx += 1
    return vision_blocks


def _convert_document_page(
    page_info: PageInfo,
) -> TextAnnotation:
    """Extracts OCR related data in `page` and converts it to TextAnnotation.

    Args:
      page_info (PageInfo): Current page information, including document page to be converted,
      its text, and the position of reading cursor.

    Returns:
        TextAnnotation:
            Proto that only contains one page OCR data.
    """
    detected_languages = []
    for language in page_info.page.detected_languages:
        detected_languages.append(
            vision.TextAnnotation.DetectedLanguage(
                language_code=language.language_code, confidence=language.confidence
            )
        )

    text_property = TextAnnotation.TextProperty(detected_languages=detected_languages)

    page = Page(
        width=int(page_info.page.dimension.width),
        height=int(page_info.page.dimension.height),
        confidence=page_info.page.layout.confidence,
        blocks=_convert_document_block(page_info),
        property=text_property,
    )

    text_annotation = TextAnnotation(
        pages=[page],
        text=_get_text_anchor_substring(
            page_info.text, page_info.page.layout.text_anchor
        ),
    )

    return text_annotation


def convert_page_to_annotate_image_response(
    docai_page: Document.Page, document_text: str
) -> AnnotateImageResponse:
    r"""Convert OCR data from `Document.proto` to `AnnotateImageResponse.proto` for Vision API.

    Args:
        docai_page (documentai.Document.Page): Document page to be converted.
        document_text (str): Full text of the document to convert.
    Returns:
        AnnotateImageResponse:
            Proto with `TextAnnotations`.
    """
    page_info = PageInfo(page=docai_page, text=document_text)

    page_vision_annotation = _convert_document_page(page_info)
    text_annotations = _generate_entity_annotations(page_info)
    return AnnotateImageResponse(
        full_text_annotation=page_vision_annotation,
        text_annotations=text_annotations,
        context=ImageAnnotationContext(page_number=docai_page.page_number),
    )
