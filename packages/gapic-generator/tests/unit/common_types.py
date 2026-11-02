# Copyright (C) 2019  Google LLC
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

import dataclasses
import itertools

from collections import namedtuple
from typing import Any, Dict, Iterable, Optional

from google.protobuf import descriptor_pb2

from gapic.schema import metadata
from gapic.schema import wrappers

from test_utils.test_utils import make_method

# Injected dummy test types


@dataclasses.dataclass(frozen=True)
class DummyMethod:
    name: bool = False
    input: bool = False
    output: bool = False
    lro: bool = False
    void: bool = False
    paged_result_field: bool = False
    client_streaming: bool = False
    server_streaming: bool = False
    flattened_fields: Dict[str, Any] = dataclasses.field(default_factory=dict)
    client_output: bool = False
    client_output_async: bool = False
    is_internal: bool = False
    is_resumable_upload: bool = False

    @property
    def client_method_name(self):
        name = self.name if isinstance(self.name, str) else ""
        method_wrapper = make_method(name=name, is_internal=self.is_internal)
        return method_wrapper.client_method_name


DummyIdent = namedtuple("DummyIdent", ["name", "sphinx"])
DummyIdent.__new__.__defaults__ = (False,) * len(DummyIdent._fields)

DummyMessageTypePB = namedtuple("DummyMessageTypePB", ["name"])

# DummyMessageBase = namedtuple(
#     "DummyMessage", ["fields", "type", "options", "ident",])
# DummyMessageBase.__new__.__defaults__ = (False,) * len(DummyMessageBase._fields)


DummyFieldBase = namedtuple(
    "DummyField",
    [
        "message",
        "enum",
        "name",
        "repeated",
        "required",
        "resource_reference",
        "oneof",
        "field_pb",
        "meta",
        "is_primitive",
        "ident",
        "type",
    ],
)
DummyFieldBase.__new__.__defaults__ = (False,) * len(DummyFieldBase._fields)


class DummyField(DummyFieldBase):
    @property
    def mock_value_original_type(self):
        return "mock_value"


class DummyMessage:
    def __init__(
        self,
        *,
        fields={},
        type="",
        options=False,
        ident=False,
        resource_path=False,
        meta=None,
    ):
        self.fields = fields
        self.type = type
        self.options = options
        self.ident = ident
        self.resource_path = resource_path
        self.meta = meta or metadata.Metadata()

    def get_field(self, field_name: str):
        return self.fields[field_name]

    def oneof_fields(self):
        return dict(
            (field.oneof, field) for field in self.fields.values() if field.oneof
        )

    @property
    def required_fields(self):
        return [field for field in self.fields.values() if field.required]

    @property
    def resource_path_args(self):
        return wrappers.MessageType.PATH_ARG_RE.findall(self.resource_path or "")


DummyService = namedtuple(
    "DummyService",
    ["name", "methods", "client_name", "async_client_name", "resource_messages_dict"],
)
DummyService.__new__.__defaults__ = (False,) * len(DummyService._fields)

DummyApiSchema = namedtuple(
    "DummyApiSchema", ["services", "naming", "messages", "gapic_version"]
)
DummyApiSchema.__new__.__defaults__ = (False, False, False, "0.0.0")

DummyNaming = namedtuple(
    "DummyNaming",
    [
        "warehouse_package_name",
        "name",
        "version",
        "versioned_module_name",
        "module_namespace",
        "proto_package",
    ],
)
DummyNaming.__new__.__defaults__ = (False,) * len(DummyNaming._fields)


def message_factory(
    exp: str,
    repeated_iter=itertools.repeat(False),
    enum: Optional[wrappers.EnumType] = None,
) -> DummyMessage:
    # This mimics the structure of MessageType in the wrappers module:
    # A MessageType has a map from field names to Fields,
    # and a Field has an (optional) MessageType.
    # The 'exp' parameter is a dotted attribute expression
    # used to describe the field and type hierarchy,
    # e.g. "mollusc.cephalopod.coleoid"
    toks = exp.split(".")
    messages = [DummyMessage(fields={}, type=tok.upper() + "_TYPE") for tok in toks]
    if enum:
        messages[-1] = enum

    for base, field, attr_name, repeated_field in zip(
        messages, messages[1:], toks[1:], repeated_iter
    ):
        base.fields[attr_name] = (
            DummyField(message=field, repeated=repeated_field)
            if isinstance(field, DummyMessage)
            else DummyField(enum=field)
        )
    return messages[0]


def enum_factory(name: str, variants: Iterable[str]) -> wrappers.EnumType:
    enum_pb = descriptor_pb2.EnumDescriptorProto(
        name=name,
        value=tuple(
            descriptor_pb2.EnumValueDescriptorProto(name=v, number=i)
            for i, v in enumerate(variants)
        ),
    )

    enum = wrappers.EnumType(
        enum_pb=enum_pb,
        values=[wrappers.EnumValueType(enum_value_pb=v) for v in enum_pb.value],
    )

    return enum
