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
"""Utilities for Document AI"""

from typing import Optional, Tuple

from google.cloud import documentai


def get_bounding_box(
    bounding_poly: documentai.BoundingPoly,
    page_dimension: documentai.Document.Page.Dimension,
) -> Optional[Tuple[int, int, int, int]]:
    r"""Returns the bounding box of an element from the element bounding_poly and page dimensions.

    Args:
        bounding_poly (documentai.BoundingPoly):
            Required. The bounding polygon of the element.
        dimension (documentai.Document.Page.Dimension):
            Required. Page dimension.

    Returns:
        Tuple[int, int, int, int]:
            Bounding box coordinates in order (top, left, bottom, right).
            Returns `None` if `bounding_poly` or `bounding_poly.normalized_vertices` is empty.
    """
    if not bounding_poly or not bounding_poly.normalized_vertices:
        return None

    vertices = [
        (
            int(vertex.x * page_dimension.width + 0.5),
            int(vertex.y * page_dimension.height + 0.5),
        )
        for vertex in bounding_poly.normalized_vertices
    ]

    top, left = vertices[0]
    bottom, right = vertices[2]
    return top, left, bottom, right
