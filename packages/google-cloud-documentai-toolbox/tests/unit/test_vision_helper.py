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

from google.cloud.vision import Paragraph

from google.cloud import documentai
from google.cloud.documentai_toolbox.converters import vision_helpers


def test_get_text_anchor_substring():
    text = "Testing this function"
    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])
    actual = vision_helpers._get_text_anchor_substring(
        text=text, text_anchor=text_anchor
    )

    assert actual == "Testing"


def test_has_text_segment_true():
    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])
    layout = documentai.Document.Page.Layout(text_anchor=text_anchor)

    assert vision_helpers._has_text_segment(layout)


def test_has_text_segment_false():
    layout = documentai.Document.Page.Layout(text_anchor=None)

    assert not vision_helpers._has_text_segment(layout)


def test_convert_common_info_src_with_vertices():
    test_src = documentai.Document.Page.Paragraph()
    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])

    vertices = [
        documentai.Vertex(x=1, y=1),
        documentai.Vertex(x=2, y=1),
        documentai.Vertex(x=2, y=2),
        documentai.Vertex(x=1, y=2),
    ]

    bounding_poly = documentai.BoundingPoly(vertices=vertices)

    detected_language = documentai.Document.Page.DetectedLanguage(
        language_code="en-US", confidence=0.99
    )

    layout = documentai.Document.Page.Layout(
        text_anchor=text_anchor,
        bounding_poly=bounding_poly,
        confidence=0.98,
    )
    test_src.layout = layout
    test_src.detected_languages = [detected_language]

    page = documentai.Document.Page()
    page.dimension.width = 1000
    page.dimension.height = 2500

    test_dest = Paragraph()

    test_page_info = vision_helpers.PageInfo(page=page)

    vision_helpers._convert_common_info(
        src=test_src, dest=test_dest, page_info=test_page_info
    )

    assert test_dest.bounding_box != Paragraph().bounding_box


def test_convert_common_info_src_with_normalized_vertices():
    test_src = documentai.Document.Page.Paragraph()
    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])

    normalized = [
        documentai.NormalizedVertex(x=0.1, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.2),
        documentai.NormalizedVertex(x=0.1, y=0.2),
    ]

    bounding_poly = documentai.BoundingPoly(normalized_vertices=normalized)

    layout = documentai.Document.Page.Layout(
        text_anchor=text_anchor, bounding_poly=bounding_poly, confidence=0.98
    )
    test_src.layout = layout

    page = documentai.Document.Page()
    page.dimension.width = 1000
    page.dimension.height = 2500

    test_dest = Paragraph()

    test_page_info = vision_helpers.PageInfo(page=page)

    vision_helpers._convert_common_info(
        src=test_src, dest=test_dest, page_info=test_page_info
    )

    assert test_dest.bounding_box != Paragraph().bounding_box


def test_is_layout_included_return_true():
    in_text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=1, end_index=4
    )
    in_text_anchor = documentai.Document.TextAnchor(text_segments=[in_text_segment])
    in_layout = documentai.Document.Page.Layout(text_anchor=in_text_anchor)

    out_text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    out_text_anchor = documentai.Document.TextAnchor(text_segments=[out_text_segment])
    out_layout = documentai.Document.Page.Layout(text_anchor=out_text_anchor)

    assert vision_helpers._is_layout_included(inner=in_layout, outer=out_layout)


def test_is_layout_included_return_false():
    in_layout = documentai.Document.Page.Layout(text_anchor=None)
    out_layout = documentai.Document.Page.Layout(text_anchor=None)

    assert not vision_helpers._is_layout_included(inner=in_layout, outer=out_layout)


def test_convert_document_symbol():
    text = "Testing this function"

    vertices = [
        documentai.Vertex(x=1, y=1),
        documentai.Vertex(x=2, y=1),
        documentai.Vertex(x=2, y=2),
        documentai.Vertex(x=1, y=2),
    ]
    normalized = [
        documentai.NormalizedVertex(x=0.1, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.2),
        documentai.NormalizedVertex(x=0.1, y=0.2),
    ]

    bounding_poly = documentai.BoundingPoly(
        vertices=vertices, normalized_vertices=normalized
    )

    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])
    layout = documentai.Document.Page.Layout(
        text_anchor=text_anchor, bounding_poly=bounding_poly
    )

    symbol = documentai.Document.Page.Symbol(layout=layout)
    token = documentai.Document.Page.Token(layout=layout)

    page = documentai.Document.Page(symbols=[symbol], tokens=[token])
    page.dimension.width = 1000
    page.dimension.height = 2500

    page_info = vision_helpers.PageInfo(page=page, text=text)

    actual = vision_helpers._convert_document_symbol(
        page_info=page_info,
        break_type=documentai.Document.Page.Token.DetectedBreak.Type.SPACE,
    )

    assert len(actual) == 1
    assert actual[0].text == "Testing"
    assert len(actual[0].bounding_box.vertices) == 4
    assert len(actual[0].bounding_box.normalized_vertices) == 4


def test_convert_document_token():
    vertices = [
        documentai.Vertex(x=1, y=1),
        documentai.Vertex(x=2, y=1),
        documentai.Vertex(x=2, y=2),
        documentai.Vertex(x=1, y=2),
    ]
    normalized = [
        documentai.NormalizedVertex(x=0.1, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.2),
        documentai.NormalizedVertex(x=0.1, y=0.2),
    ]

    bounding_poly = documentai.BoundingPoly(
        vertices=vertices, normalized_vertices=normalized
    )

    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])
    layout = documentai.Document.Page.Layout(
        text_anchor=text_anchor, bounding_poly=bounding_poly
    )

    paragraph = documentai.Document.Page.Paragraph(layout=layout)
    token = documentai.Document.Page.Token(layout=layout)

    page = documentai.Document.Page(paragraphs=[paragraph], tokens=[token])
    page.dimension.width = 1000
    page.dimension.height = 2500

    page_info = vision_helpers.PageInfo(page=page)

    actual = vision_helpers._convert_document_token(page_info=page_info)

    assert len(actual) == 1
    assert len(actual[0].bounding_box.vertices) == 4
    assert len(actual[0].bounding_box.normalized_vertices) == 4


def test_convert_document_paragraph():
    vertices = [
        documentai.Vertex(x=1, y=1),
        documentai.Vertex(x=2, y=1),
        documentai.Vertex(x=2, y=2),
        documentai.Vertex(x=1, y=2),
    ]
    normalized = [
        documentai.NormalizedVertex(x=0.1, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.2),
        documentai.NormalizedVertex(x=0.1, y=0.2),
    ]

    bounding_poly = documentai.BoundingPoly(
        vertices=vertices, normalized_vertices=normalized
    )

    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])
    layout = documentai.Document.Page.Layout(
        text_anchor=text_anchor, bounding_poly=bounding_poly
    )

    paragraph = documentai.Document.Page.Paragraph(layout=layout)
    block = documentai.Document.Page.Block(layout=layout)

    page = documentai.Document.Page(paragraphs=[paragraph], blocks=[block])
    page.dimension.width = 1000
    page.dimension.height = 2500

    page_info = vision_helpers.PageInfo(page=page)

    actual = vision_helpers._convert_document_paragraph(page_info=page_info)

    assert len(actual) == 1
    assert len(actual[0].bounding_box.vertices) == 4
    assert len(actual[0].bounding_box.normalized_vertices) == 4


def test_convert_document_block():
    vertices = [
        documentai.Vertex(x=1, y=1),
        documentai.Vertex(x=2, y=1),
        documentai.Vertex(x=2, y=2),
        documentai.Vertex(x=1, y=2),
    ]
    normalized = [
        documentai.NormalizedVertex(x=0.1, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.1),
        documentai.NormalizedVertex(x=0.2, y=0.2),
        documentai.NormalizedVertex(x=0.1, y=0.2),
    ]

    bounding_poly = documentai.BoundingPoly(
        vertices=vertices, normalized_vertices=normalized
    )

    text_segment = documentai.Document.TextAnchor.TextSegment(
        start_index=0, end_index=7
    )
    text_anchor = documentai.Document.TextAnchor(text_segments=[text_segment])
    layout = documentai.Document.Page.Layout(
        text_anchor=text_anchor, bounding_poly=bounding_poly
    )

    block = documentai.Document.Page.Block(layout=layout)

    page = documentai.Document.Page(blocks=[block])
    page.dimension.width = 1000
    page.dimension.height = 2500

    page_info = vision_helpers.PageInfo(page=page)

    actual = vision_helpers._convert_document_block(page_info=page_info)

    assert len(actual) == 1
    assert len(actual[0].bounding_box.vertices) == 4
    assert len(actual[0].bounding_box.normalized_vertices) == 4
    assert actual[0].block_type == 1


def test_convert_document_page():
    detected_language = documentai.Document.Page.DetectedLanguage(
        language_code="en-us", confidence=1.0
    )
    page = documentai.Document.Page(detected_languages=[detected_language])

    page_info = vision_helpers.PageInfo(page=page)

    actual = vision_helpers._convert_document_page(page_info=page_info)

    assert actual.pages[0].property.detected_languages[0].language_code == "en-us"
    assert actual.pages[0].property.detected_languages[0].confidence == 1
