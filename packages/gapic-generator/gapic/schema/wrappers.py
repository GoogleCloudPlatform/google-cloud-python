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

"""Module containing wrapper classes around meta-descriptors.

This module contains dataclasses which wrap the descriptor protos
defined in google/protobuf/descriptor.proto (which are descriptors that
describe descriptors).

These wrappers exist in order to provide useful helper methods and
generally ease access to things in templates (in particular, documentation,
certain aggregate views of things, etc.)

Reading of underlying descriptor properties in templates *is* okay, a
``__getattr__`` method which consistently routes in this way is provided.
Documentation is consistently at ``{thing}.meta.doc``.
"""

import collections
import copy
import dataclasses
import json
import keyword
import re
from itertools import chain
from typing import (
    Any,
    ClassVar,
    Dict,
    FrozenSet,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Pattern,
    Sequence,
    Set,
    Tuple,
    Union,
    cast,
)

from google.api import (
    annotations_pb2,  # type: ignore
    client_pb2,
    field_behavior_pb2,
    field_info_pb2,
    http_pb2,
    resource_pb2,
    routing_pb2,
)
from google.api_core import exceptions, path_template
from google.cloud import extended_operations_pb2 as ex_ops_pb2  # type: ignore
from google.protobuf import descriptor_pb2  # type: ignore
from google.protobuf.json_format import MessageToDict  # type: ignore

from gapic import utils
from gapic.schema import metadata
from gapic.utils import cached_proto_context, make_private, uri_sample


@dataclasses.dataclass(frozen=True)
class Field:
    """Description of a field."""

    field_pb: descriptor_pb2.FieldDescriptorProto
    message: Optional["MessageType"] = None
    enum: Optional["EnumType"] = None
    meta: metadata.Metadata = dataclasses.field(
        default_factory=metadata.Metadata,
    )
    oneof: Optional[str] = None

    def __getattr__(self, name):
        return getattr(self.field_pb, name)

    def __hash__(self):
        # The only sense in which it is meaningful to say a field is equal to
        # another field is if they are the same, i.e. they live in the same
        # message type under the same moniker, i.e. they have the same id.
        return id(self)

    @property
    def name(self) -> str:
        """Used to prevent collisions with python keywords"""
        name = self.field_pb.name
        return (
            name + "_"
            if name in utils.RESERVED_NAMES and self.meta.address.is_proto_plus_type
            else name
        )

    @utils.cached_property
    def ident(self) -> metadata.FieldIdentifier:
        """Return the identifier to be used in templates."""
        mapping: Optional[Tuple[Field, Field]] = None
        if self.map:
            mapping = (self.type.fields["key"], self.type.fields["value"])
        return metadata.FieldIdentifier(
            ident=self.type.ident,
            repeated=self.repeated,
            mapping=mapping,
        )

    @property
    def is_primitive(self) -> bool:
        """Return True if the field is a primitive, False otherwise."""
        return isinstance(self.type, PrimitiveType)

    @property
    def map(self) -> bool:
        """Return True if this field is a map, False otherwise."""
        return bool(self.repeated and self.message and self.message.map)

    @property
    def operation_field(self) -> Optional[str]:
        return self.options.Extensions[ex_ops_pb2.operation_field]

    @property
    def operation_request_field(self) -> Optional[str]:
        return self.options.Extensions[ex_ops_pb2.operation_request_field]

    @property
    def operation_response_field(self) -> Optional[str]:
        return self.options.Extensions[ex_ops_pb2.operation_response_field]

    @utils.cached_property
    def mock_value_original_type(
        self,
    ) -> Union[bool, str, bytes, int, float, Dict[str, Any], List[Any], None]:
        visited_messages = set()

        def recursive_mock_original_type(field):
            if field.message:
                # Return messages as dicts and let the message ctor handle the conversion.
                if field.message in visited_messages:
                    return {}

                visited_messages.add(field.message)
                if field.map:
                    # Not worth the hassle, just return an empty map.
                    return {}

                adr = field.type.meta.address
                if adr.name == "Any" and adr.package == ("google", "protobuf"):
                    # If it is Any type pack a random but validly encoded type,
                    # Duration in this specific case.
                    msg_dict = {
                        "type_url": "type.googleapis.com/google.protobuf.Duration",
                        "value": b"\x08\x0c\x10\xdb\x07",
                    }
                else:
                    msg_dict = {
                        f.name: recursive_mock_original_type(f)
                        for f in field.message.fields.values()
                    }

                return [msg_dict] if field.repeated else msg_dict

            if field.enum:
                # First Truthy value, fallback to the first value
                answer = next(
                    (v for v in field.type.values if v.number), field.type.values[0]
                ).number
                if field.repeated:
                    answer = [answer]
                return answer

            answer = field.primitive_mock() or None

            # If this is a repeated field, then the mock answer should
            # be a list.
            if field.repeated:
                first_item = field.primitive_mock(suffix=1) or None
                second_item = field.primitive_mock(suffix=2) or None
                answer = [first_item, second_item]

            return answer

        return recursive_mock_original_type(self)

    def merged_mock_value(self, other_mock: Dict[Any, Any]):
        mock = self.mock_value_original_type
        if isinstance(mock, dict) and isinstance(other_mock, dict):
            mock = copy.deepcopy(mock)
            mock.update(other_mock)
        return mock

    @utils.cached_property
    def mock_value(self) -> str:
        visited_fields: Set["Field"] = set()
        stack = [self]
        answer = "{}"
        while stack:
            expr = stack.pop()
            answer = answer.format(expr.inner_mock(stack, visited_fields))

        return answer

    def inner_mock(self, stack, visited_fields) -> str:
        """Return a repr of a valid, usually truthy mock value."""
        # For primitives, send a truthy value computed from the
        # field name.
        answer = "None"
        if isinstance(self.type, PrimitiveType):
            answer = self.primitive_mock_as_str()

        # If this is an enum, select the first truthy value (or the zero
        # value if nothing else exists).
        if isinstance(self.type, EnumType):
            # Note: The slightly-goofy [:2][-1] lets us gracefully fall
            # back to index 0 if there is only one element.
            mock_value = self.type.values[:2][-1]
            answer = f"{self.type.ident}.{mock_value.name}"

        # If this is another message, set one value on the message.
        if (
            not self.map  # Maps are handled separately
            and isinstance(self.type, MessageType)
            and len(self.type.fields)
            # Nested message types need to terminate eventually
            and self not in visited_fields
        ):
            sub = next(iter(self.type.fields.values()))
            stack.append(sub)
            visited_fields.add(self)
            # Don't do the recursive rendering here, just set up
            # where the nested value should go with the double {}.
            answer = f"{self.type.ident}({sub.name}={{}})"

        if self.map:
            # Maps are a special case because they're represented internally as
            # a list of a generated type with two fields: 'key' and 'value'.
            answer = "{{{}: {}}}".format(
                self.type.fields["key"].mock_value,
                self.type.fields["value"].mock_value,
            )
        elif self.repeated:
            # If this is a repeated field, then the mock answer should
            # be a list.
            answer = f"[{answer}]"

        # Done; return the mock value.
        return answer

    def primitive_mock(
        self, suffix: int = 0
    ) -> Union[bool, str, bytes, int, float, List[Any], None]:
        """Generate a valid mock for a primitive type. This function
        returns the original (Python) type.

        If a suffix is provided, generate a slightly different mock
        using the provided integer.
        """
        answer: Union[bool, str, bytes, int, float, List[Any], None] = None

        if not isinstance(self.type, PrimitiveType):
            raise TypeError(
                f"'primitive_mock' can only be used for "
                f"PrimitiveType, but type is {self.type}"
            )

        else:
            if self.type.python_type == bool:
                answer = True
            elif self.type.python_type == str:
                if self.name == "type_url":
                    # It is most likely a mock for Any type. We don't really care
                    # which mock value to put, so lets put a value which makes
                    # Any deserializer happy, which will wtill work even if it
                    # is not Any.
                    answer = "type.googleapis.com/google.protobuf.Empty"
                else:
                    answer = (
                        f"{self.name}_value{suffix}" if suffix else f"{self.name}_value"
                    )
            elif self.type.python_type == bytes:
                answer_str = (
                    f"{self.name}_blob{suffix}" if suffix else f"{self.name}_blob"
                )
                answer = bytes(answer_str, encoding="utf-8")
            elif self.type.python_type == int:
                answer = sum([ord(i) for i in self.name]) + suffix
            elif self.type.python_type == float:
                name_sum = sum([ord(i) for i in self.name]) + suffix
                answer = name_sum * pow(10, -1 * len(str(name_sum)))
            else:  # Impossible; skip coverage checks.
                raise TypeError(
                    "Unrecognized PrimitiveType. This should "
                    "never happen; please file an issue."
                )

        return answer

    def primitive_mock_as_str(self) -> str:
        """Like primitive mock, but return the mock as a string."""
        answer = self.primitive_mock()

        if isinstance(answer, str):
            answer = f"'{answer}'"
        else:
            answer = str(answer)

        return answer

    @property
    def proto_type(self) -> str:
        """Return the proto type constant to be used in templates."""
        return cast(
            str,
            descriptor_pb2.FieldDescriptorProto.Type.Name(
                self.field_pb.type,
            ),
        )[len("TYPE_") :]

    @property
    def repeated(self) -> bool:
        """Return True if this is a repeated field, False otherwise.

        Returns:
            bool: Whether this field is repeated.
        """
        return self.label == descriptor_pb2.FieldDescriptorProto.Label.Value(
            "LABEL_REPEATED"
        )  # type: ignore

    @property
    def required(self) -> bool:
        """Return True if this is a required field, False otherwise.

        Returns:
            bool: Whether this field is required.
        """
        return (
            field_behavior_pb2.FieldBehavior.Value("REQUIRED")
            in self.options.Extensions[field_behavior_pb2.field_behavior]
        )

    @property
    def uuid4(self) -> bool:
        """
        Return True if the format of this field is a Universally
        Unique Identifier, version 4 field, False otherwise.

        Returns:
            bool: Whether this field is UUID4.
        """
        return self.options.Extensions[
            field_info_pb2.field_info
        ].format == field_info_pb2.FieldInfo.Format.Value("UUID4")

    @property
    def resource_reference(self) -> Optional[str]:
        """Return a resource reference type if it exists.

        This is only applicable for string fields.
        Example: "translate.googleapis.com/Glossary"
        """
        return (
            self.options.Extensions[resource_pb2.resource_reference].type
            or self.options.Extensions[resource_pb2.resource_reference].child_type
            or None
        )

    @utils.cached_property
    def type(self) -> Union["MessageType", "EnumType", "PrimitiveType"]:
        """Return the type of this field."""
        # If this is a message or enum, return the appropriate thing.
        if self.type_name and self.message:
            return self.message
        if self.type_name and self.enum:
            return self.enum

        # This is a primitive. Return the corresponding Python type.
        # The enum values used here are defined in:
        #   Repository: https://github.com/google/protobuf/
        #   Path: src/google/protobuf/descriptor.proto
        #
        # The values are used here because the code would be excessively
        # verbose otherwise, and this is guaranteed never to change.
        #
        # 10, 11, and 14 are intentionally missing. They correspond to
        # group (unused), message (covered above), and enum (covered above).
        if self.field_pb.type in (1, 2):
            return PrimitiveType.build(float)
        if self.field_pb.type in (3, 4, 5, 6, 7, 13, 15, 16, 17, 18):
            return PrimitiveType.build(int)
        if self.field_pb.type == 8:
            return PrimitiveType.build(bool)
        if self.field_pb.type == 9:
            return PrimitiveType.build(str)
        if self.field_pb.type == 12:
            return PrimitiveType.build(bytes)

        # This should never happen.
        raise TypeError(
            f"Unrecognized protobuf type: {self.field_pb.type}. "
            "This code should not be reachable; please file a bug."
        )

    @cached_proto_context
    def with_context(
        self,
        *,
        collisions: Set[str],
        visited_messages: Optional[Set["MessageType"]] = None,
    ) -> "Field":
        """Return a derivative of this field with the provided context.

        This method is used to address naming collisions. The returned
        ``Field`` object aliases module names to avoid naming collisions
        in the file being written.
        """
        return dataclasses.replace(
            self,
            message=(
                self.message.with_context(
                    collisions=collisions,
                    skip_fields=(
                        self.message in visited_messages if visited_messages else False
                    ),
                    visited_messages=visited_messages,
                )
                if self.message
                else None
            ),
            enum=self.enum.with_context(collisions=collisions) if self.enum else None,
            meta=self.meta.with_context(collisions=collisions),
        )

    def add_to_address_allowlist(
        self,
        *,
        address_allowlist: Set["metadata.Address"],
        resource_messages: Dict[str, "MessageType"],
    ) -> None:
        """Adds to the set of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
            resource_messages (Dict[str, wrappers.MessageType]): A dictionary mapping the unified
                resource type name of a resource message to the corresponding MessageType object
                representing that resource message. Only resources with a message representation
                should be included in the dictionary.
        Returns:
            None
        """
        if self.message:
            self.message.add_to_address_allowlist(
                address_allowlist=address_allowlist,
                resource_messages=resource_messages,
            )

        if self.enum:
            self.enum.add_to_address_allowlist(
                address_allowlist=address_allowlist,
            )

        if self.resource_reference and self.resource_reference in resource_messages:
            # The message types in resource_message are different objects, but should be
            # defined the same as the MessageTypes we're traversing here.
            resource_messages[self.resource_reference].add_to_address_allowlist(
                address_allowlist=address_allowlist,
                resource_messages=resource_messages,
            )


@dataclasses.dataclass(frozen=True)
class FieldHeader:
    raw: str

    @property
    def disambiguated(self) -> str:
        return self.raw + "_" if self.raw in utils.RESERVED_NAMES else self.raw


@dataclasses.dataclass(frozen=True)
class Oneof:
    """Description of a field."""

    oneof_pb: descriptor_pb2.OneofDescriptorProto

    def __getattr__(self, name):
        return getattr(self.oneof_pb, name)


@dataclasses.dataclass(frozen=True)
class MessageType:
    """Description of a message (defined with the ``message`` keyword)."""

    # Class attributes
    # https://google.aip.dev/122
    PATH_ARG_RE = re.compile(r"\{([a-zA-Z0-9_\-]+)(?:=\*\*)?\}")

    # Instance attributes
    message_pb: descriptor_pb2.DescriptorProto
    fields: Mapping[str, Field]
    nested_enums: Mapping[str, "EnumType"]
    nested_messages: Mapping[str, "MessageType"]
    meta: metadata.Metadata = dataclasses.field(
        default_factory=metadata.Metadata,
    )
    oneofs: Optional[Mapping[str, "Oneof"]] = None
    resource_name_aliases: Mapping[str, str] = dataclasses.field(default_factory=dict)

    def __getattr__(self, name):
        return getattr(self.message_pb, name)

    def __hash__(self):
        # Identity is sufficiently unambiguous.
        return hash(self.ident)

    def oneof_fields(self, include_optional=False):
        oneof_fields = collections.defaultdict(list)
        for field in self.fields.values():
            # Only include proto3 optional oneofs if explicitly looked for.
            if field.oneof and not field.proto3_optional or include_optional:
                oneof_fields[field.oneof].append(field)

        return oneof_fields

    @utils.cached_property
    def extended_operation_request_fields(self) -> Sequence[Field]:
        """
        If this message is the request for a method that uses extended operations,
        return the fields that correspond to operation request fields in the operation message.
        """
        return tuple(f for f in self.fields.values() if f.operation_request_field)

    @utils.cached_property
    def extended_operation_response_fields(self) -> Sequence[Field]:
        """
        If this message is the request for a method that uses extended operations,
        return the fields that correspond to operation response fields in the polling message.
        """
        return tuple(f for f in self.fields.values() if f.operation_response_field)

    @utils.cached_property
    def differently_named_extended_operation_fields(self) -> Optional[Dict[str, Field]]:
        if not self.is_extended_operation:
            return None

        def canonical_name(field):
            return OperationResponseMapping.Name(field.operation_field).lower()

        OperationResponseMapping = ex_ops_pb2.OperationResponseMapping
        default_field_names = [
            k.lower()
            # The first variant is UNKNOWN
            for k in ex_ops_pb2.OperationResponseMapping.keys()[1:]
        ]

        return {
            canonical_name(f): f
            for f in self.fields.values()
            if f.operation_field and f.name not in default_field_names
        }

    @utils.cached_property
    def is_extended_operation(self) -> bool:
        if not self.name == "Operation":
            return False

        name, status, error_code, error_message = False, False, False, False
        duplicate_msg = f"Message '{self.name}' has multiple fields with the same operation response mapping: {{}}"
        for f in self.fields.values():
            maybe_op_mapping = f.options.Extensions[ex_ops_pb2.operation_field]
            OperationResponseMapping = ex_ops_pb2.OperationResponseMapping

            if maybe_op_mapping == OperationResponseMapping.NAME:
                if name:
                    raise TypeError(duplicate_msg.format("name"))
                name = True

            if maybe_op_mapping == OperationResponseMapping.STATUS:
                if status:
                    raise TypeError(duplicate_msg.format("status"))
                status = True

            if maybe_op_mapping == OperationResponseMapping.ERROR_CODE:
                if error_code:
                    raise TypeError(duplicate_msg.format("error_code"))
                error_code = True

            if maybe_op_mapping == OperationResponseMapping.ERROR_MESSAGE:
                if error_message:
                    raise TypeError(duplicate_msg.format("error_message"))
                error_message = True

        return name and status and error_code and error_message

    @utils.cached_property
    def extended_operation_status_field(self) -> Optional[Field]:
        STATUS = ex_ops_pb2.OperationResponseMapping.STATUS
        return next(
            (
                f
                for f in self.fields.values()
                if f.options.Extensions[ex_ops_pb2.operation_field] == STATUS
            ),
            None,
        )

    @utils.cached_property
    def required_fields(self) -> Sequence["Field"]:
        required_fields = [field for field in self.fields.values() if field.required]

        return required_fields

    @utils.cached_property
    def field_types(self) -> Sequence[Union["MessageType", "EnumType"]]:
        answer = tuple(
            field.type for field in self.fields.values() if field.message or field.enum
        )

        return answer

    @utils.cached_property
    def recursive_field_types(self) -> Sequence[Union["MessageType", "EnumType"]]:
        """Return all composite fields used in this proto's messages."""
        types: Set[Union["MessageType", "EnumType"]] = set()

        stack = [iter(self.fields.values())]
        while stack:
            fields_iter = stack.pop()
            for field in fields_iter:
                if field.message and field.type not in types:
                    stack.append(iter(field.message.fields.values()))
                if not field.is_primitive:
                    types.add(field.type)

        return tuple(types)

    @utils.cached_property
    def recursive_resource_fields(self) -> FrozenSet[Field]:
        all_fields = chain(
            self.fields.values(),
            (
                field
                for t in self.recursive_field_types
                if isinstance(t, MessageType)
                for field in t.fields.values()
            ),
        )
        return frozenset(
            f
            for f in all_fields
            if (
                f.options.Extensions[resource_pb2.resource_reference].type
                or f.options.Extensions[resource_pb2.resource_reference].child_type
            )
        )

    @property
    def map(self) -> bool:
        """Return True if the given message is a map, False otherwise."""
        return self.message_pb.options.map_entry

    @property
    def ident(self) -> metadata.Address:
        """Return the identifier data to be used in templates."""
        return self.meta.address

    @property
    def resource_path(self) -> Optional[str]:
        """If this message describes a resource, return the path to the resource.
        If there are multiple paths, returns the first one."""
        return next(iter(self.options.Extensions[resource_pb2.resource].pattern), None)

    @property
    def resource_type(self) -> Optional[str]:
        resource = self.options.Extensions[resource_pb2.resource]
        if not resource.type:
            return None

        default_type = resource.type[resource.type.find("/") + 1 :]

        return self.resource_name_aliases.get(resource.type, default_type)

    @property
    def resource_type_full_path(self) -> Optional[str]:
        resource = self.options.Extensions[resource_pb2.resource]
        return resource.type if resource else None

    @property
    def resource_path_args(self) -> Sequence[str]:
        return self.PATH_ARG_RE.findall(self.resource_path or "")

    @property
    def resource_path_formatted(self) -> str:
        """
        Returns a formatted version of `resource_path`. This re-writes
        patterns like: 'projects/{project}/metricDescriptors/{metric_descriptor=**}'
        to 'projects/{project}/metricDescriptors/{metric_descriptor}
        so it can be used in an f-string.
        """
        return self.PATH_ARG_RE.sub(r"{\g<1>}", self.resource_path or "")

    @utils.cached_property
    def path_regex_str(self) -> str:
        # The indirection here is a little confusing:
        # we're using the resource path template as the base of a regex,
        # with each resource ID segment being captured by a regex.
        # E.g., the path schema
        # kingdoms/{kingdom}/phyla/{phylum}
        # becomes the regex
        # ^kingdoms/(?P<kingdom>.+?)/phyla/(?P<phylum>.+?)$
        parsing_regex_str = (
            "^"
            + self.PATH_ARG_RE.sub(
                # We can't just use (?P<name>[^/]+) because segments may be
                # separated by delimiters other than '/'.
                # Multiple delimiter characters within one schema are allowed,
                # e.g.
                # as/{a}-{b}/cs/{c}%{d}_{e}
                # This is discouraged but permitted by AIP4231
                lambda m: "(?P<{name}>.+?)".format(name=m.groups()[0]),
                self.resource_path or "",
            )
            + "$"
        )
        # Special case for wildcard resource names
        if parsing_regex_str == "^*$":
            parsing_regex_str = "^.*$"

        return parsing_regex_str

    def get_field(
        self, *field_path: str, collisions: Optional[Set[str]] = None
    ) -> Field:
        """Return a field arbitrarily deep in this message's structure.

        This method recursively traverses the message tree to return the
        requested inner-field.

        Traversing through repeated fields is not supported; a repeated field
        may be specified if and only if it is the last field in the path.

        Args:
            field_path (Sequence[str]): The field path.

        Returns:
            ~.Field: A field object.

        Raises:
            KeyError: If a repeated field is used in the non-terminal position
                in the path.
        """
        # This covers the case when field_path is a string path.
        if len(field_path) == 1 and "." in field_path[0]:
            field_path = tuple(field_path[0].split("."))

        # If collisions are not explicitly specified, retrieve them
        # from this message's address.
        # This ensures that calls to `get_field` will return a field with
        # the same context, regardless of the number of levels through the
        # chain (in order to avoid infinite recursion on circular references,
        # we only shallowly bind message references held by fields; this
        # binds deeply in the one spot where that might be a problem).
        collisions = collisions or self.meta.address.collisions

        # Get the first field in the path.
        first_field = field_path[0]
        cursor = self.fields[
            first_field + ("_" if first_field in utils.RESERVED_NAMES else "")
        ]

        # Base case: If this is the last field in the path, return it outright.
        if len(field_path) == 1:
            return cursor.with_context(
                collisions=collisions,
                visited_messages=set({self}),
            )

        # Quick check: If cursor is a repeated field, then raise an exception.
        # Repeated fields are only permitted in the terminal position.
        if cursor.repeated:
            raise KeyError(
                f"The {cursor.name} field is repeated; unable to use "
                "`get_field` to retrieve its children.\n"
                "This exception usually indicates that a "
                "google.api.method_signature annotation uses a repeated field "
                "in the fields list in a position other than the end.",
            )

        # Quick check: If this cursor has no message, there is a problem.
        if not cursor.message:
            raise KeyError(
                f"Field {'.'.join(field_path)} could not be resolved from "
                f"{cursor.name}.",
            )

        # Recursion case: Pass the remainder of the path to the sub-field's
        # message.
        return cursor.message.get_field(*field_path[1:], collisions=collisions)

    @cached_proto_context
    def with_context(
        self,
        *,
        collisions: Set[str],
        skip_fields: bool = False,
        visited_messages: Optional[Set["MessageType"]] = None,
    ) -> "MessageType":
        """Return a derivative of this message with the provided context.

        This method is used to address naming collisions. The returned
        ``MessageType`` object aliases module names to avoid naming collisions
        in the file being written.

        The ``skip_fields`` argument will omit applying the context to the
        underlying fields. This provides for an "exit" in the case of circular
        references.
        """
        visited_messages = visited_messages or set()
        visited_messages = visited_messages | {self}
        return dataclasses.replace(
            self,
            fields=(
                {
                    k: v.with_context(
                        collisions=collisions, visited_messages=visited_messages
                    )
                    for k, v in self.fields.items()
                }
                if not skip_fields
                else self.fields
            ),
            nested_enums={
                k: v.with_context(collisions=collisions)
                for k, v in self.nested_enums.items()
            },
            nested_messages={
                k: v.with_context(
                    collisions=collisions,
                    skip_fields=skip_fields,
                    visited_messages=visited_messages,
                )
                for k, v in self.nested_messages.items()
            },
            meta=self.meta.with_context(collisions=collisions),
        )

    def add_to_address_allowlist(
        self,
        *,
        address_allowlist: Set["metadata.Address"],
        resource_messages: Dict[str, "MessageType"],
    ) -> None:
        """Adds to the set of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
            resource_messages (Dict[str, wrappers.MessageType]): A dictionary mapping the unified
                resource type name of a resource message to the corresponding MessageType object
                representing that resource message. Only resources with a message representation
                should be included in the dictionary.
        Returns:
            None
        """
        if self.ident not in address_allowlist:
            address_allowlist.add(self.ident)

            for field in self.fields.values():
                field.add_to_address_allowlist(
                    address_allowlist=address_allowlist,
                    resource_messages=resource_messages,
                )

            for enum in self.nested_enums.values():
                enum.add_to_address_allowlist(
                    address_allowlist=address_allowlist,
                )

            for message in self.nested_messages.values():
                message.add_to_address_allowlist(
                    address_allowlist=address_allowlist,
                    resource_messages=resource_messages,
                )


@dataclasses.dataclass(frozen=True)
class EnumValueType:
    """Description of an enum value."""

    enum_value_pb: descriptor_pb2.EnumValueDescriptorProto
    meta: metadata.Metadata = dataclasses.field(
        default_factory=metadata.Metadata,
    )

    def __getattr__(self, name):
        return getattr(self.enum_value_pb, name)


@dataclasses.dataclass(frozen=True)
class EnumType:
    """Description of an enum (defined with the ``enum`` keyword.)"""

    enum_pb: descriptor_pb2.EnumDescriptorProto
    values: List[EnumValueType]
    meta: metadata.Metadata = dataclasses.field(
        default_factory=metadata.Metadata,
    )

    def __hash__(self):
        # Identity is sufficiently unambiguous.
        return hash(self.ident)

    def __getattr__(self, name):
        return getattr(self.enum_pb, name)

    @property
    def resource_path(self) -> Optional[str]:
        # This is a minor duck-typing workaround for the resource_messages
        # property in the Service class: we need to check fields recursively
        # to see if they're resources, and recursive_field_types includes enums
        return None

    @property
    def ident(self) -> metadata.Address:
        """Return the identifier data to be used in templates."""
        return self.meta.address

    @cached_proto_context
    def with_context(self, *, collisions: Set[str]) -> "EnumType":
        """Return a derivative of this enum with the provided context.

        This method is used to address naming collisions. The returned
        ``EnumType`` object aliases module names to avoid naming collisions in
        the file being written.
        """
        return (
            dataclasses.replace(
                self,
                meta=self.meta.with_context(collisions=collisions),
            )
            if collisions
            else self
        )

    def add_to_address_allowlist(
        self, *, address_allowlist: Set["metadata.Address"]
    ) -> None:
        """Adds to the set of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
        Returns:
            None
        """
        address_allowlist.add(self.ident)

    @property
    def options_dict(self) -> Dict:
        """Return the EnumOptions (if present) as a dict.

        This is a hack to support a pythonic structure representation for
        the generator templates.
        """
        return MessageToDict(self.enum_pb.options, preserving_proto_field_name=True)


@dataclasses.dataclass(frozen=True)
class PythonType:
    """Wrapper class for Python types.

    This exists for interface consistency, so that methods like
    :meth:`Field.type` can return an object and the caller can be confident
    that a ``name`` property will be present.
    """

    meta: metadata.Metadata

    def __eq__(self, other):
        return self.meta == other.meta

    def __ne__(self, other):
        return not self == other

    @utils.cached_property
    def ident(self) -> metadata.Address:
        """Return the identifier to be used in templates."""
        return self.meta.address

    @property
    def name(self) -> str:
        return self.ident.name

    @property
    def field_types(self) -> Sequence[Union["MessageType", "EnumType"]]:
        return tuple()


@dataclasses.dataclass(frozen=True)
class PrimitiveType(PythonType):
    """A representation of a Python primitive type."""

    python_type: Optional[type]

    @classmethod
    def build(cls, primitive_type: Optional[type]):
        """Return a PrimitiveType object for the given Python primitive type.

        Args:
            primitive_type (cls): A Python primitive type, such as
                :class:`int` or :class:`str`. Despite not being a type,
                ``None`` is also accepted here.

        Returns:
            ~.PrimitiveType: The instantiated PrimitiveType object.
        """
        # Primitives have no import, and no module to reference, so the
        # address just uses the name of the class (e.g. "int", "str").
        return cls(
            meta=metadata.Metadata(
                address=metadata.Address(
                    name="None" if primitive_type is None else primitive_type.__name__,
                )
            ),
            python_type=primitive_type,
        )

    def __eq__(self, other):
        # If we are sent the actual Python type (not the PrimitiveType object),
        # claim to be equal to that.
        if not hasattr(other, "meta"):
            return self.python_type is other
        return super().__eq__(other)


@dataclasses.dataclass(frozen=True)
class ExtendedOperationInfo:
    """A handle to the request type of the extended operation polling method
    and the underlying operation type.
    """

    request_type: MessageType
    operation_type: MessageType

    @cached_proto_context
    def with_context(
        self,
        *,
        collisions: Set[str],
        visited_messages: Optional[Set["MessageType"]] = None,
    ) -> "ExtendedOperationInfo":
        """Return a derivative of this OperationInfo with the provided context.

        This method is used to address naming collisions. The returned
        ``OperationInfo`` object aliases module names to avoid naming collisions
        in the file being written.
        """
        return (
            self
            if not collisions
            else dataclasses.replace(
                self,
                request_type=self.request_type.with_context(
                    collisions=collisions,
                    visited_messages=visited_messages,
                ),
                operation_type=self.operation_type.with_context(
                    collisions=collisions,
                    visited_messages=visited_messages,
                ),
            )
        )

    def add_to_address_allowlist(
        self,
        *,
        address_allowlist: Set["metadata.Address"],
        resource_messages: Dict[str, "MessageType"],
    ) -> None:
        """Adds to the set of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
            resource_messages (Dict[str, wrappers.MessageType]): A dictionary mapping the unified
                resource type name of a resource message to the corresponding MessageType object
                representing that resource message. Only resources with a message representation
                should be included in the dictionary.
        Returns:
            None
        """

        self.request_type.add_to_address_allowlist(
            address_allowlist=address_allowlist,
            resource_messages=resource_messages,
        )
        self.operation_type.add_to_address_allowlist(
            address_allowlist=address_allowlist,
            resource_messages=resource_messages,
        )


@dataclasses.dataclass(frozen=True)
class OperationInfo:
    """Representation of long-running operation info."""

    response_type: MessageType
    metadata_type: MessageType

    @cached_proto_context
    def with_context(
        self,
        *,
        collisions: Set[str],
        visited_messages: Optional[Set["MessageType"]] = None,
    ) -> "OperationInfo":
        """Return a derivative of this OperationInfo with the provided context.

        This method is used to address naming collisions. The returned
        ``OperationInfo`` object aliases module names to avoid naming collisions
        in the file being written.
        """
        return dataclasses.replace(
            self,
            response_type=self.response_type.with_context(
                collisions=collisions,
                visited_messages=visited_messages,
            ),
            metadata_type=self.metadata_type.with_context(
                collisions=collisions,
                visited_messages=visited_messages,
            ),
        )

    def add_to_address_allowlist(
        self,
        *,
        address_allowlist: Set["metadata.Address"],
        resource_messages: Dict[str, "MessageType"],
    ) -> None:
        """Adds to the set of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
            resource_messages (Dict[str, wrappers.MessageType]): A dictionary mapping the unified
                resource type name of a resource message to the corresponding MessageType object
                representing that resource message. Only resources with a message representation
                should be included in the dictionary.
        Returns:
            None
        """
        self.response_type.add_to_address_allowlist(
            address_allowlist=address_allowlist,
            resource_messages=resource_messages,
        )

        self.metadata_type.add_to_address_allowlist(
            address_allowlist=address_allowlist, resource_messages=resource_messages
        )


@dataclasses.dataclass(frozen=True)
class RetryInfo:
    """Representation of the method's retry behavior."""

    max_attempts: int
    initial_backoff: float
    max_backoff: float
    backoff_multiplier: float
    retryable_exceptions: FrozenSet[exceptions.GoogleAPICallError]


@dataclasses.dataclass(frozen=True)
class RoutingParameter:
    field: str
    path_template: str

    def _split_into_segments(self, path_template):
        segments = path_template.split("/")
        named_segment_ids = [i for i, x in enumerate(segments) if "{" in x or "}" in x]
        # bar/{foo}/baz, bar/{foo=one/two/three}/baz.
        assert len(named_segment_ids) <= 2
        if len(named_segment_ids) == 2:
            # Need to merge a named segment.
            i, j = named_segment_ids
            segments = (
                segments[:i]
                + [self._merge_segments(segments[i : j + 1])]
                + segments[j + 1 :]
            )
        return segments

    def _convert_segment_to_regex(self, segment):
        # Named segment
        if "{" in segment:
            assert "}" in segment
            # Strip "{" and "}"
            segment = segment[1:-1]
            if "=" not in segment:
                # e.g. {foo} should be {foo=*}
                return self._convert_segment_to_regex("{" + f"{segment}=*" + "}")
            key, sub_path_template = segment.split("=")
            group_name = f"?P<{key}>"
            sub_regex = self._convert_to_regex(sub_path_template)
            return f"({group_name}{sub_regex})"
        # Wildcards
        if "**" in segment:
            # ?: nameless capture
            return ".*"
        if "*" in segment:
            return "[^/]+"
        # Otherwise it's collection ID segment: transformed identically.
        return segment

    def _merge_segments(self, segments):
        acc = segments[0]
        for x in segments[1:]:
            # Don't add "/" if it's followed by a "**"
            # because "**" will eat it.
            if x == ".*":
                acc += "(?:/.*)?"
            else:
                acc += "/"
                acc += x
        return acc

    def _how_many_named_segments(self, path_template):
        return path_template.count("{")

    def _convert_to_regex(self, path_template):
        if self._how_many_named_segments(path_template) > 1:
            # This also takes care of complex patterns (i.e. {foo}~{bar})
            raise ValueError(
                "There must be exactly one named segment. {} has {}.".format(
                    path_template, self._how_many_named_segments(path_template)
                )
            )
        segments = self._split_into_segments(path_template)
        segment_regexes = [self._convert_segment_to_regex(x) for x in segments]
        final_regex = self._merge_segments(segment_regexes)
        return final_regex

    def _to_regex(self, path_template: str) -> Pattern:
        """Converts path_template into a Python regular expression string.
        Args:
            path_template (str): A path template corresponding to a resource name.
                It can only have 0 or 1 named segments. It can not contain complex resource ID path segments.
                See https://google.aip.dev/122, https://google.aip.dev/4222
                 and https://google.aip.dev/client-libraries/4231 for more details.
        Returns:
            Pattern: A Pattern object that matches strings conforming to the path_template.
        """
        return re.compile(f"^{self._convert_to_regex(path_template)}$")

    @utils.cached_property
    def _regex(self) -> Pattern:
        return self._to_regex(self.path_template)

    def to_regex(self) -> Pattern:
        return self._regex

    @utils.cached_property
    def key(self) -> Union[str, None]:
        if self.path_template == "":
            return self.field
        regex = self.to_regex()
        group_names = list(regex.groupindex)
        # Only 1 named segment is allowed and so only 1 key.
        return group_names[0] if group_names else self.field

    @property
    def sample_request(self) -> str:
        """return json dict for sample request matching the uri template."""
        sample = uri_sample.sample_from_path_template(self.field, self.path_template)
        return json.dumps(sample)


@dataclasses.dataclass(frozen=True)
class RoutingRule:
    routing_parameters: List[RoutingParameter]

    @classmethod
    def try_parse_routing_rule(
        cls, routing_rule: routing_pb2.RoutingRule
    ) -> Optional["RoutingRule"]:
        params = getattr(routing_rule, "routing_parameters")
        if not params:
            return None
        params = [RoutingParameter(x.field, x.path_template) for x in params]
        return cls(params)

    @classmethod
    def resolve(
        cls, routing_rule: routing_pb2.RoutingRule, request: Union[dict, str]
    ) -> dict:
        """Resolves the routing header which should be sent along with the request.
        The routing header is determined based on the given routing rule and request.
        See the following link for more information on explicit routing headers:
        https://google.aip.dev/client-libraries/4222#explicit-routing-headers-googleapirouting

        Args:
            routing_rule(routing_pb2.RoutingRule): A collection of Routing Parameter specifications
                defined by `routing_pb2.RoutingRule`.
                See https://github.com/googleapis/googleapis/blob/cb39bdd75da491466f6c92bc73cd46b0fbd6ba9a/google/api/routing.proto#L391
            request(Union[dict, str]): The request for which the routine rule should be resolved.
                The format can be either a dictionary or json string representing the request.

        Returns(dict):
            A dictionary containing the resolved routing header to the sent along with the given request.
        """

        def _get_field(request, field_path: str):
            segments = field_path.split(".")

            # Either json string or dictionary is supported
            if isinstance(request, str):
                current = json.loads(request)
            else:
                current = request

            # This is to cater for the case where the `field_path` contains a
            # dot-separated path of field names leading to a field in a sub-message.
            for x in segments:
                current = current.get(x, None)
                # Break if the sub-message does not exist
                if current is None:
                    break
            return current

        header_params = {}
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2160): Move this logic to
        # `google-api-core` so that the shared code can be used in both `wrappers.py` and GAPIC clients
        # via Jinja templates.
        for routing_param in routing_rule.routing_parameters:
            request_field_value = _get_field(request, routing_param.field)
            # Only resolve the header for routing parameter fields which are populated in the request
            if request_field_value is not None:
                # If there is a path_template for a given routing parameter field, the value of the field must match
                # If multiple `routing_param`s describe the same key
                # (via the `path_template` field or via the `field` field when
                # `path_template` is not provided), the "last one wins" rule
                # determines which parameter gets used. See https://google.aip.dev/client-libraries/4222.
                routing_parameter_key = routing_param.key
                if routing_param.path_template:
                    routing_param_regex = routing_param.to_regex()
                    regex_match = routing_param_regex.match(request_field_value)
                    if regex_match:
                        header_params[routing_parameter_key] = regex_match.group(
                            routing_parameter_key
                        )
                else:  # No need to match
                    header_params[routing_parameter_key] = request_field_value
        return header_params


@dataclasses.dataclass(frozen=True)
class HttpRule:
    """Representation of the method's http bindings."""

    method: str
    uri: str
    body: Optional[str]

    def path_fields(self, method: "Method") -> List[Tuple[Field, str, str]]:
        """return list of (name, template) tuples extracted from uri."""
        input = method.input
        return [
            (
                input.get_field(*match.group("name").split(".")),
                match.group("name"),
                match.group("template"),
            )
            for match in path_template._VARIABLE_RE.finditer(self.uri)
            if match.group("name")
        ]

    def sample_request(self, method: "Method") -> Dict[str, Any]:
        """return json dict for sample request matching the uri template."""

        def sample_from_path_fields(
            paths: List[Tuple[Field, str, str]],
        ) -> Dict[str, Any]:
            """Construct a dict for a sample request object from a list of fields
               and template patterns.

            Args:
                  paths: a list of tuples, each with a (segmented) name and a pattern.
            Returns:
                  A new nested dict with the templates instantiated.
            """
            request: Dict[str, Any] = {}

            sample_names_ = uri_sample.sample_names()
            for field, path, template in paths:
                sample_value = (
                    re.sub(r"(\*\*|\*)", lambda n: next(sample_names_), template or "*")
                    if field.type == PrimitiveType.build(str)
                    else field.mock_value_original_type
                )
                uri_sample.add_field(request, path, sample_value)

            return request

        sample = sample_from_path_fields(self.path_fields(method))
        return sample

    @classmethod
    def try_parse_http_rule(cls, http_rule) -> Optional["HttpRule"]:
        method = http_rule.WhichOneof("pattern")
        if method is None or method == "custom":
            return None

        uri = getattr(http_rule, method)
        if not uri:
            return None
        uri = utils.convert_uri_fieldnames(uri)

        body = http_rule.body or None
        # Ensure body doesn't conflict with reserved names.
        if body in utils.RESERVED_NAMES and not body.endswith("_"):
            body += "_"
        return cls(method, uri, body)


@dataclasses.dataclass(frozen=True)
class MixinMethod:
    name: str
    request_type: str
    response_type: str
    rpc_name: str = ""


@dataclasses.dataclass(frozen=True)
class MixinHttpRule(HttpRule):
    def path_fields(self, uri):
        """return list of (name, template) tuples extracted from uri."""
        return [
            (match.group("name"), match.group("template"))
            for match in path_template._VARIABLE_RE.finditer(uri)
            if match.group("name")
        ]

    @property
    def sample_request(self):
        req = uri_sample.sample_from_path_fields(self.path_fields(self.uri))
        if not self.body or self.body == "" or self.body == "*":
            return req
        req[self.body] = {}  # just an empty json.
        return req


@dataclasses.dataclass(frozen=True)
class Method:
    """Description of a method (defined with the ``rpc`` keyword)."""

    method_pb: descriptor_pb2.MethodDescriptorProto
    input: MessageType
    output: MessageType
    is_internal: bool = False
    lro: Optional[OperationInfo] = dataclasses.field(default=None)
    extended_lro: Optional[ExtendedOperationInfo] = dataclasses.field(default=None)
    retry: Optional[RetryInfo] = dataclasses.field(default=None)
    timeout: Optional[float] = None
    meta: metadata.Metadata = dataclasses.field(
        default_factory=metadata.Metadata,
    )
    resumable_upload_prefix: str = "resumable/upload"

    def __getattr__(self, name):
        return getattr(self.method_pb, name)

    @property
    def client_method_name(self) -> str:
        """Returns the name of the generated method name.

        This is used to prevent collisions with Python keywords at the
        client level, as well as prefix internal method names with underscore.
        """
        name = self.name + "_" if self.name.lower() in keyword.kwlist else self.name
        return make_private(name) if self.is_internal else name

    @property
    def transport_safe_name(self) -> str:
        # These names conflict with other methods in the transport.
        # We don't want to disambiguate the names at the client level
        # because the disambiguated name is less convenient and user friendly.
        #
        # Note: this should really be a class variable,
        # but python 3.6 can't handle that.
        TRANSPORT_UNSAFE_NAMES = chain(
            {
                "createchannel",
                "grpcchannel",
                "operationsclient",
            },
            keyword.kwlist,
        )
        return (
            f"{self.name}_"
            if self.name.lower() in TRANSPORT_UNSAFE_NAMES
            else self.name
        )

    @property
    def is_operation_polling_method(self):
        return (
            self.output.is_extended_operation
            and self.options.Extensions[ex_ops_pb2.operation_polling_method]
        )

    @utils.cached_property
    def client_output(self):
        return self._client_output(enable_asyncio=False)

    @utils.cached_property
    def client_output_async(self):
        return self._client_output(enable_asyncio=True)

    def flattened_oneof_fields(self, include_optional=False):
        oneof_fields = collections.defaultdict(list)
        for field in self.flattened_fields.values():
            # Only include proto3 optional oneofs if explicitly looked for.
            if field.oneof and not field.proto3_optional or include_optional:
                oneof_fields[field.oneof].append(field)

        return oneof_fields

    def _client_output(self, enable_asyncio: bool):
        """Return the output from the client layer.

        This takes into account transformations made by the outer GAPIC
        client to transform the output from the transport.

        Returns:
            Union[~.MessageType, ~.PythonType]:
                A description of the return type.
        """
        # Void messages ultimately return None.
        if self.void:
            return PrimitiveType.build(None)

        # If this method is an LRO, return a PythonType instance representing
        # that.
        if self.lro:
            return PythonType(
                meta=metadata.Metadata(
                    address=metadata.Address(
                        name="AsyncOperation" if enable_asyncio else "Operation",
                        module="operation_async" if enable_asyncio else "operation",
                        package=("google", "api_core"),
                        collisions=self.lro.response_type.ident.collisions,
                    ),
                    documentation=utils.doc(
                        "An object representing a long-running operation. \n\n"
                        "The result type for the operation will be "
                        ":class:`{ident}` {doc}".format(
                            doc=self.lro.response_type.meta.doc,
                            ident=self.lro.response_type.ident.sphinx,
                        ),
                    ),
                )
            )

        if self.extended_lro:
            return PythonType(
                meta=metadata.Metadata(
                    address=metadata.Address(
                        name="ExtendedOperation",
                        module="extended_operation",
                        package=("google", "api_core"),
                        collisions=self.extended_lro.operation_type.ident.collisions,
                    ),
                    documentation=utils.doc(
                        "An object representing a extended long-running operation."
                    ),
                ),
            )

        # If this method is paginated, return that method's pager class.
        if self.paged_result_field:
            return PythonType(
                meta=metadata.Metadata(
                    address=metadata.Address(
                        name=(
                            f"{self.name}AsyncPager"
                            if enable_asyncio
                            else f"{self.name}Pager"
                        ),
                        package=self.ident.api_naming.module_namespace
                        + (self.ident.api_naming.versioned_module_name,)
                        + self.ident.subpackage
                        + (
                            "services",
                            utils.to_snake_case(self.ident.parent[-1]),
                        ),
                        module="pagers",
                        collisions=self.input.ident.collisions,
                    ),
                    documentation=utils.doc(
                        f"{self.output.meta.doc}\n\n"
                        "Iterating over this object will yield results and "
                        "resolve additional pages automatically.",
                    ),
                )
            )

        # If this method is a resumable upload, return a PythonType instance
        # representing the resumable upload session (while self.output remains
        # the underlying protobuf response message for final deserialization).
        if self.is_resumable_upload:
            return PythonType(
                meta=metadata.Metadata(
                    address=metadata.Address(
                        name=(
                            "AsyncResumableUploadSession"
                            if enable_asyncio
                            else "ResumableUploadSession"
                        ),
                        module="resumable_transfer",
                        package=("google", "api_core"),
                        collisions=self.input.ident.collisions,
                    ),
                    documentation=utils.doc(
                        "An object representing a resumable upload session."
                    ),
                ),
            )

        # Return the usual output.
        return self.output

    @property
    def operation_service(self) -> Optional[str]:
        return self.options.Extensions[ex_ops_pb2.operation_service]

    @property
    def is_deprecated(self) -> bool:
        """Returns true if the method is deprecated, false otherwise."""
        return descriptor_pb2.MethodOptions.HasField(self.options, "deprecated")

    # TODO(yon-mg): remove or rewrite: don't think it performs as intended
    #               e.g. doesn't work with basic case of gRPC transcoding

    @property
    def field_headers(self) -> Sequence[FieldHeader]:
        """Return the field headers defined for this method."""

        http = self.options.Extensions[annotations_pb2.http]

        # Copied from Node generator.
        # https://github.com/googleapis/gapic-generator-typescript/blob/3ab47f04678d72171ddf25b439d50f6dfb44584c/typescript/src/schema/proto.ts#L587
        pattern = re.compile(r"{(.*?)[=}]")

        potential_verbs = [
            http.get,
            http.put,
            http.post,
            http.delete,
            http.patch,
            http.custom.path,
        ]
        field_headers = (
            tuple(FieldHeader(field_header) for field_header in pattern.findall(verb))
            for verb in potential_verbs
            if verb
        )
        return next(field_headers, ())

    @property
    def explicit_routing(self):
        return routing_pb2.routing in self.options.Extensions

    @property
    def routing_rule(self):
        if self.explicit_routing:
            routing_ext = self.options.Extensions[routing_pb2.routing]
            routing_rule = RoutingRule.try_parse_routing_rule(routing_ext)
            return routing_rule
        return None

    @property
    def http_options(self) -> List[HttpRule]:
        """Return a list of the http bindings for this method."""
        http = self.options.Extensions[annotations_pb2.http]
        http_options = [http] + list(http.additional_bindings)
        opt_gen = (
            HttpRule.try_parse_http_rule(http_rule) for http_rule in http_options
        )
        return [rule for rule in opt_gen if rule]

    @property
    def http_opt(self) -> Optional[Dict[str, str]]:
        """Return the (main) http option for this method.

        e.g. {'verb': 'post'
              'url': '/some/path'
              'body': '*'}

        """
        http: List[Tuple[descriptor_pb2.FieldDescriptorProto, str]]
        http = self.options.Extensions[annotations_pb2.http].ListFields()

        if len(http) < 1:
            return None

        http_method = http[0]
        answer: Dict[str, str] = {
            "verb": http_method[0].name,
            "url": http_method[1],
        }
        if len(http) > 1:
            body_spec = http[1]
            answer[body_spec[0].name] = body_spec[1]

        # TODO(yon-mg): handle nested fields & fields past body i.e. 'additional bindings'
        # TODO(yon-mg): enums for http verbs?
        return answer

    @property
    def is_resumable_upload(self) -> bool:
        """Return True if this method is a resumable upload method."""
        # Resumable upload method names are temporarily hardcoded here until
        # the resumable upload proto annotation exists and is published.
        return self.name in ("UploadMedia", "CreateYouTubeVideoUpload")

    @property
    def path_params(self) -> Sequence[str]:
        """Return the path parameters found in the http annotation path template"""
        # TODO(yon-mg): fully implement grpc transcoding (currently only handles basic case)
        if self.http_opt is None:
            return []

        pattern = r"\{(\w+)(?:=.+?)?\}"
        return re.findall(pattern, self.http_opt["url"])

    @property
    def query_params(self) -> Set[str]:
        """Return query parameters for API call as determined by http annotation and grpc transcoding"""
        # TODO(yon-mg): fully implement grpc transcoding (currently only handles basic case)
        # TODO(yon-mg): remove this method and move logic to generated client
        if self.http_opt is None:
            return set()

        params = set(self.path_params)
        body = self.http_opt.get("body")
        if body:
            if body == "*":
                # The entire request is the REST body.
                return set()
            else:
                params.add(body)

        return set(self.input.fields) - params

    @property
    def body_fields(self) -> Mapping[str, Field]:
        bindings = self.http_options
        if bindings and bindings[0].body and bindings[0].body != "*":
            return self._fields_mapping([bindings[0].body])
        return {}

    # TODO(yon-mg): refactor as there may be more than one method signature
    @utils.cached_property
    def flattened_fields(self) -> Mapping[str, Field]:
        signatures = self.options.Extensions[client_pb2.method_signature]
        return self._fields_mapping(signatures)

    # TODO(yon-mg): refactor as there may be more than one method signature
    def _fields_mapping(self, signatures) -> Mapping[str, Field]:
        """Return the signature defined for this method."""
        cross_pkg_request = self.input.ident.package != self.ident.package

        def filter_fields(sig: str) -> Iterable[Tuple[str, Field]]:
            for f in sig.split(","):
                if not f:
                    # Special case for an empty signature
                    continue
                name = f.strip()
                field = self.input.get_field(*name.split("."))
                name += "_" if field.field_pb.name in utils.RESERVED_NAMES else ""
                if cross_pkg_request and not field.is_primitive:
                    # This is not a proto-plus wrapped message type,
                    # and setting a non-primitive field directly is verboten.
                    continue

                yield name, field

        answer: Dict[str, Field] = collections.OrderedDict(
            name_and_field
            for sig in signatures
            for name_and_field in filter_fields(sig)
        )

        return answer

    @utils.cached_property
    def flattened_field_to_key(self):
        return {field.name: key for key, field in self.flattened_fields.items()}

    @utils.cached_property
    def legacy_flattened_fields(self) -> Mapping[str, Field]:
        """Return the legacy flattening interface: top level fields only,
        required fields first"""
        required, optional = utils.partition(
            lambda f: f.required, self.input.fields.values()
        )
        return collections.OrderedDict((f.name, f) for f in chain(required, optional))

    @property
    def grpc_stub_type(self) -> str:
        """Return the type of gRPC stub to use."""
        return "{client}_{server}".format(
            client="stream" if self.client_streaming else "unary",
            server="stream" if self.server_streaming else "unary",
        )

    # TODO(yon-mg): figure out why idempotent is reliant on http annotation
    @utils.cached_property
    def idempotent(self) -> bool:
        """Return True if we know this method is idempotent, False otherwise.

        Note: We are intentionally conservative here. It is far less bad
        to falsely believe an idempotent method is non-idempotent than
        the converse.
        """
        return bool(self.options.Extensions[annotations_pb2.http].get)

    @property
    def ident(self) -> metadata.Address:
        """Return the identifier data to be used in templates."""
        return self.meta.address

    def _validate_paged_field_size_type(self, page_field_size) -> bool:
        """Validates allowed paged_field_size type(s).

        Confirms whether the paged_field_size.type is an allowed wrapper type:
        The norm is for type to be int, but an additional check is included to
        account for BigQuery legacy APIs which allowed UInt32Value and
        Int32Value.
        """

        pb_type = page_field_size.type

        return pb_type == int or (
            isinstance(pb_type, MessageType)
            and pb_type.message_pb.name in {"UInt32Value", "Int32Value"}
        )

    @utils.cached_property
    def paged_result_field(self) -> Optional[Field]:
        """Return the response pagination field if the method is paginated.

        The request field must have a page_token field and a page_size field (or
        for legacy APIs, a max_results field) and the response field
        must have a next_token_field and a repeated field.

        For the purposes of supporting legacy APIs, additional wrapper types are
        allowed.
        """

        for source, source_type, name in (
            (self.input, str, "page_token"),
            (self.output, str, "next_page_token"),
        ):
            field = source.fields.get(name, None)
            if not field or field.type != source_type:
                return None

        # The request must have page_size (or max_results if legacy API)
        page_fields = (
            self.input.fields.get("max_results", None),
            self.input.fields.get("page_size", None),
        )
        page_field_size = next((field for field in page_fields if field), None)

        if not page_field_size:
            return None

        # Confirm whether the paged_field_size is an allowed type.
        if not self._validate_paged_field_size_type(page_field_size=page_field_size):
            return None

        # Return the first repeated field.
        for field in self.output.fields.values():
            if field.repeated:
                return field

        # We found no repeated fields. Return None.
        return None

    @utils.cached_property
    def ref_types(self) -> Sequence[Union[MessageType, EnumType]]:
        return self._ref_types(True)

    @utils.cached_property
    def flat_ref_types(self) -> Sequence[Union[MessageType, EnumType]]:
        return self._ref_types(False)

    def _ref_types(self, recursive: bool) -> Sequence[Union[MessageType, EnumType]]:
        """Return types referenced by this method."""
        # Begin with the input (request) and output (response) messages.
        answer: List[Union[MessageType, EnumType]] = [self.input]
        types: Iterable[Union[MessageType, EnumType]] = (
            self.input.recursive_field_types
            if recursive
            else (f.type for f in self.flattened_fields.values() if f.message or f.enum)
        )
        answer.extend(types)

        if not self.void:
            answer.append(self.client_output)
            answer.extend(self.client_output.field_types)
            answer.append(self.client_output_async)
            answer.extend(self.client_output_async.field_types)

        # If this method has LRO, it is possible (albeit unlikely) that
        # the LRO messages reside in a different module.
        if self.lro:
            answer.append(self.lro.response_type)
            answer.append(self.lro.metadata_type)

        # Extended operation
        if self.extended_lro:
            answer.append(self.extended_lro.request_type)
            answer.append(self.extended_lro.operation_type)

        # If this message paginates its responses, it is possible
        # that the individual result messages reside in a different module.
        if self.paged_result_field and self.paged_result_field.message:
            answer.append(self.paged_result_field.message)

        # If this method is a resumable upload, client_output is ResumableUploadSession,
        # so explicitly include self.output to ensure the underlying response message is imported.
        if self.is_resumable_upload:
            answer.append(self.output)

        # Done; return the answer.
        return tuple(answer)

    @property
    def void(self) -> bool:
        """Return True if this method has no return value, False otherwise."""
        return self.output.ident.proto == "google.protobuf.Empty"

    @cached_proto_context
    def with_context(
        self,
        *,
        collisions: Set[str],
        visited_messages: Optional[Set["MessageType"]] = None,
    ) -> "Method":
        """Return a derivative of this method with the provided context.

        This method is used to address naming collisions. The returned
        ``Method`` object aliases module names to avoid naming collisions
        in the file being written.
        """
        maybe_lro = None
        if self.lro:
            maybe_lro = (
                self.lro.with_context(
                    collisions=collisions,
                    visited_messages=visited_messages,
                )
                if collisions
                else self.lro
            )

        maybe_extended_lro = (
            self.extended_lro.with_context(
                collisions=collisions,
                visited_messages=visited_messages,
            )
            if self.extended_lro
            else None
        )

        return dataclasses.replace(
            self,
            lro=maybe_lro,
            extended_lro=maybe_extended_lro,
            input=self.input.with_context(
                collisions=collisions,
                visited_messages=visited_messages,
            ),
            output=self.output.with_context(
                collisions=collisions,
                visited_messages=visited_messages,
            ),
            meta=self.meta.with_context(collisions=collisions),
        )

    def add_to_address_allowlist(
        self,
        *,
        address_allowlist: Set["metadata.Address"],
        resource_messages: Dict[str, "MessageType"],
        services_in_proto: Dict[str, "Service"],
    ) -> None:
        """Adds to the allowlist of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
            method_allowlist (Set[str]): An allowlist of fully-qualified method names.
            resource_messages (Dict[str, wrappers.MessageType]): A dictionary mapping the unified
                resource type name of a resource message to the corresponding MessageType object
                representing that resource message. Only resources with a message representation
                should be included in the dictionary.
            services_in_proto (Dict[str, wrappers.Service]): A dictionary mapping the names of Service
                objects in the proto containing this method to the Service objects. This is necessary
                for traversing the operation service in the case of extended LROs.
        Returns:
            None
        """

        address_allowlist.add(self.ident)

        if self.lro:
            self.lro.add_to_address_allowlist(
                address_allowlist=address_allowlist, resource_messages=resource_messages
            )

        if self.extended_lro and self.operation_service:
            # We need to add the service/method pointed to by self.operation_service to
            # the allowlist, as it might not have been specified by
            # the methods under selective_gapic_generation.
            # We assume that the operation service lives in the same proto file as this one.
            operation_service = services_in_proto[
                self.meta.address.resolve(self.operation_service)
            ]
            address_allowlist.add(operation_service.meta.address)
            operation_service.operation_polling_method.add_to_address_allowlist(
                address_allowlist=address_allowlist,
                resource_messages=resource_messages,
                services_in_proto=services_in_proto,
            )

            self.extended_lro.add_to_address_allowlist(
                address_allowlist=address_allowlist,
                resource_messages=resource_messages,
            )

        self.input.add_to_address_allowlist(
            address_allowlist=address_allowlist,
            resource_messages=resource_messages,
        )

        self.output.add_to_address_allowlist(
            address_allowlist=address_allowlist,
            resource_messages=resource_messages,
        )

    def with_selective_generation(
        self,
        *,
        generate_omitted_as_internal: bool,
        public_methods: Set[str],
        excluded_addresses: Set["metadata.Address"],
    ) -> Optional["Method"]:
        """Returns a version of this Method for selective generation.

        Args:
            generate_omitted_as_internal (bool): Whether to mark omitted methods as internal.
            public_methods (Set[str]): The set of fully-qualified method names to keep as public.
            excluded_addresses (Set[metadata.Address]): The set of addresses to exclude from generation.

        Returns:
            Optional[Method]: The method, possibly marked as internal, or None if it should be removed.
        """
        if self.ident.proto in public_methods:
            return self

        # Not public.
        # We mark it as internal if either:
        #   1. generate_omitted_as_internal is set in selective_gapic_generation.
        #   2. The method is NOT in excluded_addresses, which means it is reachable
        #      from some public method (e.g. as a polling method for an extended LRO).
        if generate_omitted_as_internal or self.meta.address not in excluded_addresses:
            return dataclasses.replace(
                self,
                is_internal=True,
            )
        else:
            return None


@dataclasses.dataclass(frozen=True)
class CommonResource:
    type_name: str
    pattern: str
    resource_name_aliases: Mapping[str, str] = dataclasses.field(default_factory=dict)

    @classmethod
    def build(
        cls,
        resource: resource_pb2.ResourceDescriptor,
        aliases: Optional[Mapping[str, str]] = None,
    ):
        return cls(
            type_name=resource.type,
            pattern=next(iter(resource.pattern)),
            resource_name_aliases=aliases or {},
        )

    @utils.cached_property
    def message_type(self):
        message_pb = descriptor_pb2.DescriptorProto()
        res_pb = message_pb.options.Extensions[resource_pb2.resource]
        res_pb.type = self.type_name
        res_pb.pattern.append(self.pattern)

        return MessageType(
            message_pb=message_pb,
            fields={},
            nested_enums={},
            nested_messages={},
            resource_name_aliases=self.resource_name_aliases,
        )


@dataclasses.dataclass(frozen=True)
class Service:
    """Description of a service (defined with the ``service`` keyword)."""

    service_pb: descriptor_pb2.ServiceDescriptorProto
    methods: Mapping[str, Method]
    # N.B.: visible_resources is intended to be a read-only view
    # whose backing store is owned by the API.
    # This is represented by a types.MappingProxyType instance.
    visible_resources: Mapping[str, MessageType]
    meta: metadata.Metadata = dataclasses.field(
        default_factory=metadata.Metadata,
    )

    common_resources: ClassVar[Mapping[str, CommonResource]] = dataclasses.field(
        default={
            "cloudresourcemanager.googleapis.com/Project": CommonResource(
                "cloudresourcemanager.googleapis.com/Project",
                "projects/{project}",
            ),
            "cloudresourcemanager.googleapis.com/Organization": CommonResource(
                "cloudresourcemanager.googleapis.com/Organization",
                "organizations/{organization}",
            ),
            "cloudresourcemanager.googleapis.com/Folder": CommonResource(
                "cloudresourcemanager.googleapis.com/Folder",
                "folders/{folder}",
            ),
            "cloudbilling.googleapis.com/BillingAccount": CommonResource(
                "cloudbilling.googleapis.com/BillingAccount",
                "billingAccounts/{billing_account}",
            ),
            "locations.googleapis.com/Location": CommonResource(
                "locations.googleapis.com/Location",
                "projects/{project}/locations/{location}",
            ),
        },
        init=False,
        compare=False,
    )

    def __hash__(self):
        return hash(f"{self.meta.address.api_naming.module_name}.{self.name}")

    def __getattr__(self, name):
        return getattr(self.service_pb, name)

    @property
    def client_name(self) -> str:
        """Returns the name of the generated client class"""
        return ("Base" if self.is_internal else "") + self.name + "Client"

    @property
    def client_package_version(self) -> str:
        return self.meta.address.package[-1] if self.meta.address.package else ""

    @property
    def async_client_name(self) -> str:
        """Returns the name of the generated AsyncIO client class"""
        return ("Base" if self.is_internal else "") + self.name + "AsyncClient"

    @property
    def transport_name(self):
        return self.name + "Transport"

    @property
    def grpc_transport_name(self):
        return self.name + "GrpcTransport"

    @property
    def grpc_asyncio_transport_name(self):
        return self.name + "GrpcAsyncIOTransport"

    @property
    def rest_transport_name(self):
        return self.name + "RestTransport"

    @property
    def has_lro(self) -> bool:
        """Return whether the service has a long-running method."""
        return any(m.lro for m in self.methods.values())

    @property
    def has_extended_lro(self) -> bool:
        return any(m.extended_lro for m in self.methods.values())

    @property
    def has_pagers(self) -> bool:
        """Return whether the service has paged methods."""
        return any(m.paged_result_field for m in self.methods.values())

    @property
    def has_resumable_upload_methods(self) -> bool:
        """Return whether this specific service has resumable upload methods.

        Used during per-service file generation and in service-level templates
        to conditionally emit resumable upload imports, transports, and client
        methods only for services that define resumable upload RPCs.
        """
        return any(m.is_resumable_upload for m in self.methods.values())

    @property
    def host(self) -> str:
        """Return the hostname for this service, if specified.

        Returns:
            str: The hostname, with no protocol and no trailing ``/``.
        """
        if self.options.Extensions[client_pb2.default_host]:
            return self.options.Extensions[client_pb2.default_host]
        return ""

    @property
    def version(self) -> str:
        """Return the API version for this service, if specified.

        Returns:
            str: The API version for this service.
        """
        if self.options.Extensions[client_pb2.api_version]:
            return self.options.Extensions[client_pb2.api_version]
        return ""

    @property
    def shortname(self) -> str:
        """Return the API short name. DRIFT uses this to identify
        APIs.

        Returns:
            str: The api shortname.
        """
        # Get the shortname from the host
        # Real APIs are expected to have format:
        # "{api_shortname}.googleapis.com"
        return self.host.split(".")[0].split(":")[0]

    @property
    def oauth_scopes(self) -> Sequence[str]:
        """Return a sequence of oauth scopes, if applicable.

        Returns:
            Sequence[str]: A sequence of OAuth scopes.
        """
        # Return the OAuth scopes, split on comma.
        return tuple(
            i.strip()
            for i in self.options.Extensions[client_pb2.oauth_scopes].split(",")
            if i
        )

    @property
    def module_name(self) -> str:
        """Return the appropriate module name for this service.

        Returns:
            str: The service name, in snake case.
        """
        return utils.to_snake_case(self.name)

    @utils.cached_property
    def names(self) -> FrozenSet[str]:
        """Return a set of names used in this service.

        This is used for detecting naming collisions in the module names
        used for imports.
        """
        # Put together a set of the service and method names.
        answer = {self.name, self.client_name, self.async_client_name}
        answer.update(utils.to_snake_case(i.name) for i in self.methods.values())

        # Identify any import module names where the same module name is used
        # from distinct packages.
        modules: Dict[str, Set[str]] = collections.defaultdict(set)
        for m in self.methods.values():
            for t in m.ref_types:
                modules[t.ident.module].add(t.ident.package)

        answer.update(
            module_name
            for module_name, packages in modules.items()
            if len(packages) > 1
        )

        # Done; return the answer.
        return frozenset(answer)

    @utils.cached_property
    def resource_messages(self) -> Sequence["MessageType"]:
        """Returns all the resource message types used in all
        request and response fields in the service."""

        def gen_resources(message):
            if message.resource_path:
                yield message

            for type_ in message.recursive_field_types:
                if type_.resource_path:
                    yield type_

        def gen_indirect_resources_used(message):
            for field in message.recursive_resource_fields:
                resource = field.options.Extensions[resource_pb2.resource_reference]
                resource_type = resource.type or resource.child_type
                # The resource may not be visible if the resource type is one of
                # the common_resources (see the class var in class definition)
                # or if it's something unhelpful like '*'.
                resource = self.visible_resources.get(resource_type)
                if resource:
                    yield resource

        unique_messages = frozenset(
            msg
            for method in self.methods.values()
            for msg in chain(
                gen_resources(method.input),
                gen_resources(
                    method.lro.response_type if method.lro else method.output
                ),
                gen_indirect_resources_used(method.input),
                gen_indirect_resources_used(
                    method.lro.response_type if method.lro else method.output
                ),
            )
        )

        # Convert the set to a sorted tuple using the resource path or message name.
        # This is needed to prevent non-deterministic code generation.
        sorted_messages = sorted(
            unique_messages, key=lambda m: m.resource_type_full_path or m.name
        )

        # Fail-fast collision detection
        seen_types: Dict[str, "MessageType"] = {}
        for msg in sorted_messages:
            res_type = msg.resource_type
            if not res_type:
                # Fail fast if a resource is missing type
                raise ValueError(
                    f"\n\nFatal: Message '{msg.name}' defines a resource pattern but is missing a resource type. "
                    f"This violates AIP-123 (https://google.aip.dev/123). Please define a 'type' in the google.api.resource option."
                )

            if res_type in seen_types:
                incumbent = seen_types[res_type]
                raise ValueError(
                    f"\n\nFatal: Namespace collision detected for resource type '{res_type}'.\n"
                    f"Resources '{incumbent.resource_type_full_path}' and '{msg.resource_type_full_path}' "
                    f"both flatten to the exact same method name.\n"
                    f"To protect backward compatibility, explicitly alias one of these using "
                    f"the `--resource-name-alias` CLI parameter.\n"
                    f"Example: --resource-name-alias={msg.resource_type_full_path}:CustomName\n"
                )
            seen_types[res_type] = msg

        return tuple(sorted_messages)

    @utils.cached_property
    def resource_messages_dict(self) -> Dict[str, MessageType]:
        """Returns a dict from resource reference to
        the message type. This *includes* the common resource messages.

        Returns:
            Dict[str, MessageType]: A mapping from resource path
                string to the corresponding MessageType.
                `{"locations.googleapis.com/Location": MessageType(...)}`
        """
        service_resource_messages = {
            r.resource_type_full_path: r for r in self.resource_messages
        }

        # Add common resources
        service_resource_messages.update(
            (resource_path, resource.message_type)
            for resource_path, resource in self.common_resources.items()
        )

        return service_resource_messages

    @utils.cached_property
    def any_client_streaming(self) -> bool:
        return any(m.client_streaming for m in self.methods.values())

    @utils.cached_property
    def any_server_streaming(self) -> bool:
        return any(m.server_streaming for m in self.methods.values())

    @utils.cached_property
    def any_deprecated(self) -> bool:
        return any(m.is_deprecated for m in self.methods.values())

    @utils.cached_property
    def any_extended_operations_methods(self) -> bool:
        return any(m.operation_service for m in self.methods.values())

    @utils.cached_property
    def operation_polling_method(self) -> Optional[Method]:
        return next(
            (m for m in self.methods.values() if m.is_operation_polling_method), None
        )

    @utils.cached_property
    def is_internal(self) -> bool:
        return any(m.is_internal for m in self.methods.values())

    @cached_proto_context
    def with_context(
        self,
        *,
        collisions: Set[str],
        visited_messages: Optional[Set["MessageType"]] = None,
    ) -> "Service":
        """Return a derivative of this service with the provided context.

        This method is used to address naming collisions. The returned
        ``Service`` object aliases module names to avoid naming collisions
        in the file being written.
        """
        return dataclasses.replace(
            self,
            methods={
                k: v.with_context(
                    # A method's flattened fields create additional names
                    # that may conflict with module imports.
                    collisions=collisions | set(v.flattened_fields.keys()),
                    visited_messages=visited_messages,
                )
                for k, v in self.methods.items()
            },
            meta=self.meta.with_context(collisions=collisions),
        )

    def add_to_address_allowlist(
        self,
        *,
        address_allowlist: Set["metadata.Address"],
        method_allowlist: Set[str],
        resource_messages: Dict[str, "MessageType"],
        services_in_proto: Dict[str, "Service"],
    ) -> None:
        """Adds to the allowlist of Addresses of wrapper objects to be included in selective GAPIC generation.

        This method is used to create an allowlist of addresses to be used to filter out unneeded
        services, methods, messages, and enums at a later step.

        Args:
            address_allowlist (Set[metadata.Address]): A set of allowlisted metadata.Address
                objects to add to. Only the addresses of the allowlisted methods, the services
                containing these methods, and messages/enums those methods use will be part of the
                final address_allowlist. The set may be modified during this call.
            method_allowlist (Set[str]): An allowlist of fully-qualified method names.
            resource_messages (Dict[str, wrappers.MessageType]): A dictionary mapping the unified
                resource type name of a resource message to the corresponding MessageType object
                representing that resource message. Only resources with a message representation
                should be included in the dictionary.
            services_in_proto (Dict[str, Service]):
        Returns:
            None
        """

        for method in self.methods.values():
            if method.ident.proto in method_allowlist:
                # Include this service if there are any types/methods in selective gapic for this service.
                address_allowlist.add(self.meta.address)
                method.add_to_address_allowlist(
                    address_allowlist=address_allowlist,
                    resource_messages=resource_messages,
                    services_in_proto=services_in_proto,
                )

    def with_selective_generation(
        self,
        *,
        generate_omitted_as_internal: bool,
        public_methods: Set[str],
        excluded_addresses: Set["metadata.Address"],
    ) -> Optional["Service"]:
        """Returns a version of this Service for selective generation.

        Args:
            generate_omitted_as_internal (bool): Whether to mark omitted methods as internal.
            public_methods (Set[str]): The set of fully-qualified method names to keep as public.
            excluded_addresses (Set[metadata.Address]): The set of addresses to exclude from generation.

        Returns:
            Optional[Service]: The service with filtered methods, or None if it should be removed.
        """
        methods = {}
        for k, v in self.methods.items():
            new_v = v.with_selective_generation(
                generate_omitted_as_internal=generate_omitted_as_internal,
                public_methods=public_methods,
                excluded_addresses=excluded_addresses,
            )
            if new_v:
                methods[k] = new_v

        if not generate_omitted_as_internal and not methods:
            return None

        return dataclasses.replace(self, methods=methods)
