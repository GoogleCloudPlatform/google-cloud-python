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


from typing import Callable, List, Optional

from intervaltree import intervaltree

from google.cloud import documentai
from google.cloud.documentai_toolbox.converters.config.block import Block

PIXEL_CONVERSION_RATES = {
    "pxl": 1,
    "inch": 96,
    "cm": 37.795,
}


def _midpoint_in_bpoly(
    box_a: documentai.BoundingPoly, box_b: documentai.BoundingPoly
) -> bool:
    """Returns whether the midpoint in box_a is inside box_b."""

    # Calculate the midpoint of box_a.
    mid_x_a = (_get_norm_x_max(box_a) + _get_norm_x_min(box_a)) / 2.0
    mid_y_a = (_get_norm_y_max(box_a) + _get_norm_y_min(box_a)) / 2.0

    max_x_b = _get_norm_x_max(box_b)
    min_x_b = _get_norm_x_min(box_b)
    max_y_b = _get_norm_y_max(box_b)
    min_y_b = _get_norm_y_min(box_b)

    return min_x_b < mid_x_a < max_x_b and min_y_b < mid_y_a < max_y_b


def _merge_text_anchors(
    text_anchor_1: documentai.Document.TextAnchor,
    text_anchor_2: documentai.Document.TextAnchor,
) -> documentai.Document.TextAnchor:
    """Merges two TextAnchor objects into one ascending sorted TextAnchor."""
    intervals = []
    for text_segment in text_anchor_1.text_segments:
        intervals.append(
            intervaltree.Interval(text_segment.start_index, text_segment.end_index)
        )
    for text_segment in text_anchor_2.text_segments:
        intervals.append(
            intervaltree.Interval(text_segment.start_index, text_segment.end_index)
        )

    merged_tree = intervaltree.IntervalTree(intervals)
    merged_tree.merge_overlaps(strict=False)

    merged_text_segments = [
        documentai.Document.TextAnchor.TextSegment(
            start_index=iv.begin, end_index=iv.end
        )
        for iv in sorted(merged_tree)
    ]

    return documentai.Document.TextAnchor(text_segments=merged_text_segments)


def get_text_anchor_in_bbox(
    bbox: documentai.BoundingPoly,
    page: documentai.Document.Page,
    token_in_bounding_box_function: Callable[
        [documentai.BoundingPoly, documentai.BoundingPoly], bool
    ] = _midpoint_in_bpoly,
) -> documentai.Document.TextAnchor:
    """Gets mergedTextAnchor of Tokens in `page` that fall inside the `bbox`."""

    text_anchor = documentai.Document.TextAnchor()
    for token in page.tokens:
        if token_in_bounding_box_function(token.layout.bounding_poly, bbox):
            text_anchor = _merge_text_anchors(text_anchor, token.layout.text_anchor)
    return text_anchor


def _get_norm_x_max(bbox: documentai.BoundingPoly) -> float:
    return max([vertex.x for vertex in bbox.normalized_vertices])


def _get_norm_x_min(bbox: documentai.BoundingPoly) -> float:
    return min([vertex.x for vertex in bbox.normalized_vertices])


def _get_norm_y_max(bbox: documentai.BoundingPoly) -> float:
    return max([vertex.y for vertex in bbox.normalized_vertices])


def _get_norm_y_min(bbox: documentai.BoundingPoly) -> float:
    return min([vertex.y for vertex in bbox.normalized_vertices])


def _normalize_coordinates(x, y) -> float:
    return round(float(x / y), 9)


def _convert_to_pixels(x: float, conversion_rate: float) -> float:
    return x * conversion_rate


def _convert_bbox_units(
    coordinate: float,
    input_bbox_units: str,
    width: Optional[float] = None,
    height: Optional[float] = None,
    multiplier: float = 1.0,
) -> float:
    r"""Returns a converted coordinate.

    Args:
        coordinate (float):
            Required.The coordinate from document.proto
        input_bbox_units (str):
            Required. The bounding box units.
        width (float):
            Optional.
        height (float):
            Optional.
        multiplier (float):
            Optional.

    Returns:
        float:
            A converted coordinate.

    """

    if input_bbox_units == "normalized":
        return coordinate * multiplier

    x = _convert_to_pixels(coordinate, PIXEL_CONVERSION_RATES.get(input_bbox_units, 1))
    y = width or height

    return _normalize_coordinates(x, y) * multiplier


def _get_multiplier(
    docproto_coordinate: float, external_coordinate: float, input_bbox_units: str
) -> float:
    r"""Returns a multiplier to use when converting bounding boxes.

    Args:
        docproto_coordinate (float):
            Required.The coordinate from document.proto
        external_coordinate (float):
            Required.The coordinate from external annotations.
        input_bbox_units (str):
            Required. The bounding box units.
    Returns:
        float:
            multiplier to use when converting bounding boxes.

    """
    converted_coordinate = _convert_to_pixels(
        external_coordinate, PIXEL_CONVERSION_RATES.get(input_bbox_units, 1)
    )
    return docproto_coordinate / converted_coordinate


def convert_bbox_to_docproto_bbox(block: Block) -> documentai.BoundingPoly:
    r"""Returns a converted bounding box from Block.

    Args:
        block (Block):
            Required.
    Returns:
        documentai.BoundingPoly:
            A documentai.BoundingPoly from bounding box.

    """
    if block.bounding_box == []:
        return documentai.BoundingPoly()

    x_multiplier = 1.0
    y_multiplier = 1.0
    normalized_vertices: List[documentai.NormalizedVertex] = []

    if (
        block.page_width
        and block.page_height
        and block.docproto_width is not None
        and block.docproto_height is not None
    ):
        x_multiplier = _get_multiplier(
            docproto_coordinate=block.docproto_width,
            external_coordinate=block.page_width,
            input_bbox_units=block.bounding_unit or "normalized",
        )
        y_multiplier = _get_multiplier(
            docproto_coordinate=block.docproto_height,
            external_coordinate=block.page_height,
            input_bbox_units=block.bounding_unit or "normalized",
        )

    if block.bounding_type == "1":
        # Type 1 : bounding box has 4 (x,y) coordinates
        if isinstance(block.bounding_box, list):
            for coordinate in block.bounding_box:
                x = _convert_bbox_units(
                    coordinate[f"{block.bounding_x}"],
                    input_bbox_units=block.bounding_unit or "normalized",
                    width=block.docproto_width,
                    multiplier=x_multiplier,
                )
                y = _convert_bbox_units(
                    coordinate[f"{block.bounding_y}"],
                    input_bbox_units=block.bounding_unit or "normalized",
                    height=block.docproto_height,
                    multiplier=y_multiplier,
                )

                normalized_vertices.append(documentai.NormalizedVertex(x=x, y=y))

    elif block.bounding_type == "2":
        # Type 2 : bounding box has 1 (x,y) coordinates for the top left corner
        #          and (width, height)
        if not isinstance(block.bounding_box, dict):
            raise TypeError("Expected dict for bounding_box in Type 2")
        x_min = _convert_bbox_units(
            block.bounding_box[f"{block.bounding_x}"],
            input_bbox_units=block.bounding_unit or "normalized",
            width=block.page_width,
            multiplier=x_multiplier,
        )
        y_min = _convert_bbox_units(
            block.bounding_box[f"{block.bounding_y}"],
            input_bbox_units=block.bounding_unit or "normalized",
            width=block.page_height,
            multiplier=y_multiplier,
        )
        if block.bounding_width is None or block.bounding_height is None:
            raise ValueError(
                "bounding_width and bounding_height must be set for Type 2"
            )
        x_max = x_min + block.bounding_width
        y_max = y_min + block.bounding_height
        normalized_vertices.extend(
            [
                documentai.NormalizedVertex(x=x_min, y=y_min),
                documentai.NormalizedVertex(x=x_max, y=y_min),
                documentai.NormalizedVertex(x=x_max, y=y_max),
                documentai.NormalizedVertex(x=x_min, y=y_max),
            ]
        )

    elif block.bounding_type == "3":
        #   Type 3 : bounding_box: [x1, y1, x2, y2, x3, y3, x4, y4]
        if not isinstance(block.bounding_box, list):
            raise TypeError("Expected list for bounding_box in Type 3")
        for idx in range(0, len(block.bounding_box), 2):
            x = _convert_bbox_units(
                block.bounding_box[idx],
                input_bbox_units=block.bounding_unit or "normalized",
                width=block.docproto_width,
                multiplier=x_multiplier,
            )
            y = _convert_bbox_units(
                block.bounding_box[idx + 1],
                input_bbox_units=block.bounding_unit or "normalized",
                width=block.docproto_height,
                multiplier=y_multiplier,
            )
            normalized_vertices.append(documentai.NormalizedVertex(x=x, y=y))

    return documentai.BoundingPoly(normalized_vertices=normalized_vertices)
