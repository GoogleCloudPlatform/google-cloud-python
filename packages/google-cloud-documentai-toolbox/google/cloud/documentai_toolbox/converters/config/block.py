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

import dataclasses
import json
from types import SimpleNamespace
from typing import Any, List, Optional, Type, Union

from google.cloud import documentai


def _get_target_object(json_data: Any, target_object: str) -> Any:
    r"""Returns SimpleNamespace of target_object.

    Args:
        json_data (str):
            Required. data from JSON.loads .
        target_object (str):
            Required. The path to the target object.

    Returns:
        Optional[SimpleNamespace].

    """
    json_data_s = SimpleNamespace(**json_data)

    target_object_parts = target_object.split(".")

    if not hasattr(json_data_s, target_object_parts[0]):
        return None

    for part in target_object_parts:
        if type(json_data_s) is dict:
            json_data_s = SimpleNamespace(**json_data_s)
        elif type(json_data_s) is list and part.isnumeric():
            json_data_s = json_data_s[int(part)]
            continue
        json_data_s = getattr(json_data_s, part)
    return json_data_s


@dataclasses.dataclass
class Block:
    r"""Represents a Block from OCR data.

    Attributes:
        bounding_box (str):
            Required.
        block_references:
            Optional.
        block_id:
            Optional.
        confidence:
            Optional.
        type_:
            Required.
        text:
            Required.
        page_number:
            Optional.
    """

    type_: Any = dataclasses.field(init=True, repr=False)
    text: str = dataclasses.field(init=True, repr=False)
    bounding_box: Optional[Union[SimpleNamespace, List[Any]]] = dataclasses.field(
        init=True, repr=False, default=None
    )
    block_references: Any = dataclasses.field(init=True, repr=False, default=None)
    block_id: Optional[str] = dataclasses.field(init=False, repr=False, default=None)
    confidence: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    page_number: Optional[int] = dataclasses.field(init=False, repr=False, default=None)
    page_width: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    page_height: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    bounding_width: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    bounding_height: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    bounding_type: Optional[str] = dataclasses.field(
        init=False, repr=False, default=None
    )
    bounding_unit: Optional[str] = dataclasses.field(
        init=False, repr=False, default=None
    )
    bounding_x: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    bounding_y: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    docproto_width: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )
    docproto_height: Optional[float] = dataclasses.field(
        init=False, repr=False, default=None
    )

    @classmethod
    def load_blocks_from_schema(
        cls: Type["Block"],
        input_data: bytes,
        input_config: bytes,
        base_docproto: documentai.Document,
    ) -> List["Block"]:
        r"""Loads Blocks from original annotation data and provided config.

        Args:
            input_data (bytes):
                Required.The bytes of the annotated data.
            input_config (bytes):
                Required.The bytes of config data.
            base_docproto (bytes):
                Required. The bytes of the original pdf.

        Returns:
            List[Block]:
                From original annotation data and provided config.

        """
        objects = json.loads(input_data)
        schema_json = json.loads(
            input_config, object_hook=lambda d: SimpleNamespace(**d)
        )

        entities = schema_json.entity_object
        type_ = schema_json.entity.type_

        mention_text = schema_json.entity.mention_text

        id_ = getattr(schema_json.entity, "id", None)
        document_height = (
            getattr(schema_json.page, "height", None)
            if hasattr(schema_json, "page")
            else None
        )
        document_width = (
            getattr(schema_json.page, "width", None)
            if hasattr(schema_json, "page")
            else None
        )

        confidence = getattr(schema_json.entity, "confidence", None)
        page_number = getattr(schema_json.entity, "page_number", None)
        normalized_vertices = getattr(
            schema_json.entity.normalized_vertices, "base", None
        )
        bounding_width = getattr(schema_json.entity.normalized_vertices, "width", None)
        bounding_height = getattr(
            schema_json.entity.normalized_vertices, "height", None
        )
        bounding_type = getattr(schema_json.entity.normalized_vertices, "type", None)
        bounding_unit = getattr(schema_json.entity.normalized_vertices, "unit", None)
        bounding_x = getattr(schema_json.entity.normalized_vertices, "x", None)
        bounding_y = getattr(schema_json.entity.normalized_vertices, "y", None)

        blocks: List[Block] = []
        ens = _get_target_object(objects, entities)
        if not isinstance(ens, (list, dict)):
            raise TypeError("Expected list or dict for entities")
        for i in ens:
            entity = i

            block_text = ""

            if type_ == f"{entities}:self":
                block_type = i
                entity = _get_target_object(objects, f"{entities}.{i}")
            else:
                block_type = _get_target_object(entity, type_)

            if "||" in mention_text:
                text_commands = mention_text.split("||")
                for command in text_commands:
                    if command in entity:
                        block_text = _get_target_object(entity, command)
                        continue
            else:
                block_text = _get_target_object(entity, mention_text)

            b = Block(
                type_=block_type,
                text=block_text,
                bounding_box=_get_target_object(entity, normalized_vertices)
                if normalized_vertices is not None
                else None,
            )

            if id_:
                b.block_id = _get_target_object(entity, id_)
            if confidence:
                b.confidence = _get_target_object(entity, confidence)
            if page_number and page_number in entity:
                b.page_number = _get_target_object(entity, page_number)
            if bounding_width:
                b.bounding_width = _get_target_object(b.bounding_box, bounding_width)
            if bounding_height:
                b.bounding_height = _get_target_object(b.bounding_box, bounding_height)
            if document_height:
                b.page_height = _get_target_object(objects, document_height)
            if document_width:
                b.page_width = _get_target_object(objects, document_width)
            if bounding_type:
                b.bounding_type = bounding_type
            if bounding_unit:
                b.bounding_unit = bounding_unit
            if bounding_x:
                b.bounding_x = bounding_x
            if bounding_y:
                b.bounding_y = bounding_y

            if b.page_number is None:
                b.page_number = 0

            b.docproto_width = base_docproto.pages[int(b.page_number)].dimension.width
            b.docproto_height = base_docproto.pages[int(b.page_number)].dimension.height

            blocks.append(b)
        return blocks
