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
import jinja2
import json
import keyword
import os
import re
import time
import yaml

from gapic import utils

from gapic.samplegen_utils import types, snippet_metadata_pb2  # type: ignore
from gapic.samplegen_utils.utils import is_valid_sample_cfg
from gapic.schema import api
from gapic.schema import wrappers

from collections import defaultdict, namedtuple, ChainMap as chainmap
from typing import (
    Any,
    ChainMap,
    Dict,
    FrozenSet,
    Generator,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
)

# There is no library stub file for this module, so ignore it.
from google.api import resource_pb2  # type: ignore
from google.protobuf import descriptor_pb2

# Outstanding issues:
# * In real sample configs, many variables are
#   defined with an _implicit_ $resp variable.


RESERVED_WORDS = frozenset(
    itertools.chain(
        keyword.kwlist,
        dir(__builtins__),
        {
            "client",
            "f",  # parameter used in file I/O statements
            "operation",  # temporary used in LROs
            "page",  # used in paginated responses
            "page_result",  # used in paginated responses
            "response",  # basic 'response'
            "stream",  # used in server and bidi streaming
        },
    )
)

DEFAULT_TEMPLATE_NAME = "sample.py.j2"


@dataclasses.dataclass(frozen=True)
class AttributeRequestSetup:
    """A single request-field setup description.

    If 'field' is not set, this is a top level attribute, in which case the 'base'
    parameter of the owning TransformedRequest is the attribute name.

    A True 'value_is_file' indicates that 'value' is a file path,
    and that the value of the attribute is the contents of that file.

    A non-empty 'input_parameter' indicates a formal parameter to the sample function
    that contains the value for the attribute.

    """

    value: str
    field: Optional[str] = None
    value_is_file: bool = False
    input_parameter: Optional[str] = None
    comment: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class TransformedRequest:
    """Class representing a single field in a method call.

    A request block, as read in from the sample config, is a list of dicts that
    describe field setup for the API method request.

    Fields with subfields are treated as dictionaries, with subfields as keys
    and passed, read, or hardcoded subfield values as the mapped values.
    These field dictionaries are passed into the client method as positional arguments.

    Fields _without_ subfields, aka top-level-fields, are passed into the method call
    as keyword parameters, with their associated values assigned directly.

    A TransformedRequest describes a subfield of the API request.
    It is either a top level request, in which case the 'single' attribute is filled,
    or it has assigned-to subfields, in which case 'body' lists assignment setups.

    The Optional[single]/Optional[body] is workaround for not having tagged unions.
    """

    base: str
    single: Optional[AttributeRequestSetup]
    body: Optional[List[AttributeRequestSetup]]
    pattern: Optional[str] = None

    # Resource patterns look something like
    # kingdom/{kingdom}/phylum/{phylum}/class/{class}
    RESOURCE_RE = wrappers.MessageType.PATH_ARG_RE

    @classmethod
    def build(
        cls,
        request_type: wrappers.MessageType,
        api_schema: api.API,
        base: str,
        attrs: List[AttributeRequestSetup],
        is_resource_request: bool,
    ):
        """Build a TransformedRequest based on parsed input.

        Acts as a factory to hide complicated logic for resource-based requests.

        Args:
            request_type (wrappers.MessageType): The method's request message type.
            api_schema (api.API): The API schema (used for looking up other messages)
            base (str): the name of the base field being set.
            attrs List[str]: All the attributes (or fields) being set
                                           for the base field.
            is_resource_request (bool): Indicates whether the request describes a
                                        constructed resource name path.

        Returns:
            TransformedRequest

        Raises:
            NoSuchResource: If the base parameter field for a resource-name
                            request statement lists a resource_type for which
                            there is no message with the same resource type.
            NoSuchResourcePattern: If all the request setup statements for a
                                   resource name parameter do not combine to
                                   match a valid path pattern for that resource.
        """

        # Attrs is guaranteed to be non-empty because of the construction of
        # the base_param_to_attrs map in validate_and_transform_request.
        # Each non-error lookup results in an append to the corresponding attrs
        # list, and then the key/val pairs are passed into this factory.
        if not attrs[0].field:
            return cls(base=base, body=None, single=attrs[0])
        elif not is_resource_request:
            return cls(base=base, body=attrs, single=None)
        else:
            # This is the tricky one.
            # We need to determine whether the field is describing a valid resource,
            # and if so, what its corresponding message type is.
            # Then we need to find the pattern with parameters
            # that exactly matches the attrs, if one exists.
            #
            # It's a precondition that the base field is
            # a valid field of the request message type.
            resource_reference = request_type.fields[base].options.Extensions[
                resource_pb2.resource_reference
            ]
            resource_typestr = resource_reference.type or resource_reference.child_type

            resource_message = None
            for service in api_schema.services.values():
                resource_message = service.resource_messages_dict.get(resource_typestr)
                if resource_message is not None:
                    break

            if resource_message is None:
                raise types.NoSuchResource(
                    f"No message exists for resource: {resource_typestr}",
                )
            resource_message_descriptor = resource_message.options.Extensions[
                resource_pb2.resource
            ]

            # The field is only ever empty for singleton attributes.
            attr_names: List[str] = [a.field for a in attrs]  # type: ignore

            # A single resource may be found under multiple paths and have many patterns.
            # We want to find an _exact_ match, if one exists.
            pattern = next(
                (
                    p
                    for p in resource_message_descriptor.pattern
                    if cls.RESOURCE_RE.findall(p) == attr_names
                ),
                None,
            )
            if not pattern:
                attr_name_str = ", ".join(attr_names)
                raise types.NoSuchResourcePattern(
                    f"Resource {resource_typestr} has no pattern with params: {attr_name_str}"
                )
            # This re-writes
            # patterns like: 'projects/{project}/metricDescriptors/{metric_descriptor=**}'
            # to 'projects/{project}/metricDescriptors/{metric_descriptor}
            # so it can be used in sample code as an f-string.
            pattern = cls.RESOURCE_RE.sub(r"{\g<1>}", pattern)

            return cls(
                base=base,
                body=attrs,
                single=None,
                pattern=pattern,
            )


@dataclasses.dataclass
class RequestEntry:
    """Throwaway data type used in validating and transforming requests.

    Deliberatly NOT frozen: is_resource_request is mutable on purpose."""

    is_resource_request: bool = False
    attrs: List[AttributeRequestSetup] = dataclasses.field(default_factory=list)


@dataclasses.dataclass(frozen=True)
class FullRequest:
    request_list: List[TransformedRequest]
    flattenable: bool = False


class Validator:
    """Class that validates a sample.

    Contains methods that validate different segments of a sample and maintains
    state that's relevant to validation across different segments.
    """

    COLL_KWORD = "collection"
    VAR_KWORD = "variable"
    MAP_KWORD = "map"
    KEY_KWORD = "key"
    VAL_KWORD = "value"
    BODY_KWORD = "body"

    # This regex matches each variable or attribute in the following example
    # expression and indicates whether the lookup is indexed, mapped, or neither
    #
    # cephalopoda.coleoidea[0].suborder{"incirrina"}
    EXPRESSION_ATTR_RE = re.compile(
        r"""
        (?P<attr_name>\$?\w+)(?:\[(?P<index>\d+)\]|\{["'](?P<key>[^"']+)["']\})?$
        """.strip()
    )

    VALID_REQUEST_KWORDS = frozenset(
        ("value", "field", "value_is_file", "input_parameter", "comment")
    )

    def __init__(self, method: wrappers.Method, api_schema: api.API):
        # The response ($resp) variable is special and guaranteed to exist.
        self.method = method
        self.request_type_ = method.input
        response_type = method.output
        if method.paged_result_field:
            response_type = method.paged_result_field.message
        elif method.lro:
            response_type = method.lro.response_type

        self.api_schema_ = api_schema

        # This is a shameless hack to work around the design of wrappers.Field
        MockField = namedtuple("MockField", ["message", "repeated"])

        # TODO: pass var_defs_ around during response verification
        #       instead of assigning/restoring.
        self.var_defs_: ChainMap[str, wrappers.Field] = chainmap(
            # When validating expressions we need to store the Field,
            # not just the message type, because there are additional data we need:
            # whether a name refers to a repeated value (or a map),
            # and whether it's an enum or a message or a primitive type.
            # The method call response isn't a field, so construct an artificial
            # field that wraps the response.
            {"$resp": MockField(response_type, False)}  # type: ignore
        )

    @staticmethod
    def preprocess_sample(sample, api_schema: api.API, rpc: wrappers.Method):
        """Modify a sample to set default or missing fields.

        Args:
           sample (Any): A definition for a single sample generated from parsed yaml.
           api_schema (api.API): The schema that defines the API to which the sample belongs.
           rpc (wrappers.Method): The rpc method used in the sample.
        """
        sample["package_name"] = api_schema.naming.warehouse_package_name
        sample["module_name"] = api_schema.naming.versioned_module_name
        sample["module_namespace"] = api_schema.naming.module_namespace

        service = api_schema.services[sample["service"]]

        # Assume the gRPC transport if the transport is not specified
        transport = sample.setdefault("transport", api.TRANSPORT_GRPC)

        is_async = transport == api.TRANSPORT_GRPC_ASYNC
        sample["client_name"] = (
            service.async_client_name if is_async else service.client_name
        )
        sample["client_method_name"] = rpc.client_method_name

        # the MessageType of the request object passed to the rpc e.g., `ListRequest`
        sample["request_type"] = rpc.input

        # We check if the request object is part of the service proto package.
        # If not, it comes from a different module.
        address = rpc.input.meta.address
        if address.proto_package.startswith(address.api_naming.proto_package):
            sample["request_module_name"] = sample["module_name"]
        else:
            sample["request_module_name"] = address.python_import.module

        # If no request was specified in the config
        # Add reasonable default values as placeholders
        if "request" not in sample:
            sample["request"] = generate_request_object(api_schema, service, rpc.input)

        # If no response was specified in the config
        # Add reasonable defaults depending on the type of the sample
        if not rpc.void:
            sample.setdefault("response", [{"print": ["%s", "$resp"]}])
        else:
            sample.setdefault("response", [])

    @utils.cached_property
    def flattenable_fields(self) -> FrozenSet[str]:
        return frozenset(field.name for field in self.method.flattened_fields.values())

    def var_field(self, var_name: str) -> Optional[wrappers.Field]:
        return self.var_defs_.get(var_name)

    def _normal_request_setup(self, base_param_to_attrs, val, request, field):
        """validates and transforms non-resource-based request entries.

        Private method, lifted out to make validate_and_transform_request cleaner.

        Args:
            base_param_to_attrs ({str:RequestEntry}):
            val (str): The value to which the terminal field will be set
                       (only used if the terminus is an enum)
            request (str:str): The request dictionary read in from the config.
            field (str): The value of the "field" parameter in the request entry.

        Returns:
                Tuple[str, AttributeRequestSetup]
        """
        base = self.request_type_
        attr_chain = field.split(".")
        for i, attr_name in enumerate(attr_chain):
            attr = base.fields.get(attr_name)
            if not attr:
                raise types.BadAttributeLookup(
                    "Method request type {} has no attribute: '{}'".format(
                        self.request_type_, attr_name
                    )
                )

            if attr.message:
                base = attr.message
            elif attr.enum:
                # A little bit hacky, but 'values' is a list, and this is the easiest
                # way to verify that the value is a valid enum variant.
                # Here val could be a list of a single enum value name.
                witness = any(e.name in val for e in attr.enum.values)
                if not witness:
                    raise types.InvalidEnumVariant(
                        "Invalid variant for enum {}: '{}'".format(attr, val)
                    )
                break
            elif attr.is_primitive:
                # Only valid if this is the last attribute in the chain.
                break
            else:
                raise TypeError(
                    f"Could not handle attribute '{attr_name}' of type: {attr.type}"
                )

        if i != len(attr_chain) - 1:
            # We broke out of the loop after processing an enum or a primitive.
            extra_attrs = ".".join(attr_chain[i:])
            raise types.NonTerminalPrimitiveOrEnum(
                f"Attempted to reference attributes of enum value or primitive type: '{extra_attrs}'"
            )

        if len(attr_chain) > 1:
            request["field"] = ".".join(attr_chain[1:])
        else:
            # Because of the way top level attrs get rendered,
            # there can't be duplicates.
            # This is admittedly a bit of a hack.
            if attr_chain[0] in base_param_to_attrs:
                raise types.InvalidRequestSetup(
                    "Duplicated top level field in request block: '{}'".format(
                        attr_chain[0]
                    )
                )
            del request["field"]

        if isinstance(request["value"], str):
            # Passing value through json is a safe and simple way of
            # making sure strings are properly wrapped and quotes escaped.
            # This statement both wraps enums in quotes and escapes quotes
            # in string values passed as parameters.
            #
            # Python code can set protobuf enums from strings.
            # This is preferable to adding the necessary import statement
            # and requires less munging of the assigned value
            request["value"] = json.dumps(request["value"])

        # Mypy isn't smart enough to handle dictionary unpacking,
        # so disable it for the AttributeRequestSetup ctor call.
        return attr_chain[0], AttributeRequestSetup(**request)  # type: ignore

    def validate_and_transform_request(
        self, calling_form: types.CallingForm, request: List[Mapping[str, str]]
    ) -> FullRequest:
        """Validates and transforms the "request" block from a sample config.

           In the initial request, each dict has a "field" key that maps to a dotted
           variable name, e.g. clam.shell.

           The only required keys in each dict are "field" and value".
           Optional keys are "input_parameter", "value_is_file". and "comment".
           All values in the initial request are strings except for the value
           for "value_is_file", which is a bool.

           The TransformedRequest structure of the return value has four fields:
           "base", "body", "single", and "pattern",
           where "base" maps to the top level attribute name,
           "body" maps to a list of subfield assignment definitions, "single"
           maps to a singleton attribute assignment structure with no "field" value,
           and "pattern" is a resource name pattern string if the request describes
           resource name construction.
           The "field" attribute in the requests in a "body" list have their prefix stripped;
           the request in a "single" attribute has no "field" attribute.

           Note: gRPC API methods only take one parameter (ignoring client-side streaming).
                 The reason that GAPIC client library API methods may take multiple parameters
                 is a workaround to provide idiomatic protobuf support within python.
                 The different 'bases' are really attributes for the singular request parameter.

           TODO: properly handle subfields, indexing, and so forth.
           TODO: Add/transform to list repeated element fields.
                 Requires proto/method/message descriptors.

           E.g. [{"field": "clam.shell", "value": "10 kg", "input_parameter": "shell"},
                 {"field": "clam.pearls", "value": "3"},
                 {"field": "squid.mantle", "value": "100 kg"},
                 {"field": "whelk", "value": "speckled"}]
                  ->
                [TransformedRequest(
                     base="clam",
                     body=[AttributeRequestSetup(field="shell",
                                                 value="10 kg",
                                                 input_parameter="shell"),
                           AttributeRequestSetup(field="pearls", value="3")],
                     single=None),
                 TransformedRequest(base="squid",
                                    body=[AttributeRequestSetup(field="mantle",
                                                                value="100 kg")],
                                    single=None),
                 TransformedRequest(base="whelk",
                                    body=None,
                                    single=AttributeRequestSetup(value="speckled))]

           The transformation makes it easier to set up request parameters in jinja
           because it doesn't have to engage in prefix detection, validation,
           or aggregation logic.


        Args:
            request (list[dict{str:str}]): The request body from the sample config

        Returns:
            List[TransformedRequest]: The transformed request block.

        Raises:
            InvalidRequestSetup: If a dict in the request lacks a "field" key,
                                 a "value" key or if there is an unexpected keyword.
            BadAttributeLookup: If a request field refers to a non-existent field
                                in the request message type.
            ResourceRequestMismatch: If a request attempts to describe both
                                     attribute manipulation and resource name
                                     construction.

        """
        base_param_to_attrs: Dict[str, RequestEntry] = defaultdict(RequestEntry)
        for r in request:
            r_dup = dict(r)
            val = r_dup.get("value")
            if not val:
                raise types.InvalidRequestSetup(
                    "Missing keyword in request entry: 'value'"
                )

            field = r_dup.get("field")
            if not field:
                raise types.InvalidRequestSetup(
                    "Missing keyword in request entry: 'field'"
                )

            spurious_kwords = set(r_dup.keys()) - self.VALID_REQUEST_KWORDS
            if spurious_kwords:
                raise types.InvalidRequestSetup(
                    "Spurious keyword(s) in request entry: {}".format(
                        ", ".join(f"'{kword}'" for kword in spurious_kwords)
                    )
                )

            input_parameter = r_dup.get("input_parameter")
            if input_parameter:
                self._handle_lvalue(
                    input_parameter,
                    wrappers.Field(field_pb=descriptor_pb2.FieldDescriptorProto()),
                )

            # The percentage sign is used for setting up resource based requests
            percent_idx = field.find("%")
            if percent_idx == -1:
                base_param, attr = self._normal_request_setup(
                    base_param_to_attrs, val, r_dup, field
                )

                request_entry = base_param_to_attrs.get(base_param)
                if request_entry and request_entry.is_resource_request:
                    raise types.ResourceRequestMismatch(
                        f"Request setup mismatch for base: {base_param}"
                    )

                base_param_to_attrs[base_param].attrs.append(attr)
            else:
                # It's a resource based request.
                base_param, resource_attr = (
                    field[:percent_idx],
                    field[percent_idx + 1 :],
                )
                request_entry = base_param_to_attrs.get(base_param)
                if request_entry and not request_entry.is_resource_request:
                    raise types.ResourceRequestMismatch(
                        f"Request setup mismatch for base: {base_param}"
                    )

                if not self.request_type_.fields.get(base_param):
                    raise types.BadAttributeLookup(
                        "Method request type {} has no attribute: '{}'".format(
                            self.request_type_, base_param
                        )
                    )

                r_dup["field"] = resource_attr
                request_entry = base_param_to_attrs[base_param]
                request_entry.is_resource_request = True
                request_entry.attrs.append(
                    AttributeRequestSetup(**r_dup)  # type: ignore
                )

        # We can only flatten a collection of request parameters if they're a
        # subset of the flattened fields of the method.
        flattenable = self.flattenable_fields >= set(base_param_to_attrs)
        return FullRequest(
            request_list=[
                TransformedRequest.build(
                    self.request_type_,
                    self.api_schema_,
                    key,
                    val.attrs,
                    val.is_resource_request,
                )
                for key, val in base_param_to_attrs.items()
            ],
            flattenable=False,
        )

    def validate_response(self, response):
        """Validates a "response" block from a sample config.

        A full description of the response block is outside the scope of this code;
        refer to the samplegen documentation.

        Dispatches statements to sub-validators.

        Args:
            response: list[dict{str:Any}]: The structured data representing
                                           the sample's response.

        Raises:
            InvalidStatement: If an unexpected key is found in a statement dict
                              or a statement dict has more than or less than one key.
        """

        for statement in response:
            if len(statement) != 1:
                raise types.InvalidStatement("Invalid statement: {}".format(statement))

            keyword, body = next(iter(statement.items()))
            validater = self.STATEMENT_DISPATCH_TABLE.get(keyword)
            if not validater:
                raise types.InvalidStatement(
                    "Invalid statement keyword: {}".format(keyword)
                )

            validater(self, body)

    def validate_expression(self, exp: str) -> wrappers.Field:
        """Validate an attribute chain expression.

        Given a lookup expression, e.g. squid.clam.whelk,
        recursively validate that each base has an attr with the name of the
        next lookup lower down and repeated attributes are indexed.

        Args:
            expr: str: The attribute expression.

        Raises:
            UndefinedVariableReference: If the root of the expression is not
                                        a previously defined lvalue.
            BadAttributeLookup: If an attribute other than the final is repeated OR
                                if an attribute in the chain is not a field of its parent.

        Returns:
            wrappers.Field: The final field in the chain.
        """

        def validate_recursively(expression, scope, depth=0):
            first_dot = expression.find(".")
            base = expression[:first_dot] if first_dot > 0 else expression
            match = self.EXPRESSION_ATTR_RE.match(base)
            if not match:
                raise types.BadAttributeLookup(
                    f"Badly formed attribute expression: {expression}"
                )

            name, idxed, mapped = (
                match.groupdict()["attr_name"],
                bool(match.groupdict()["index"]),
                bool(match.groupdict()["key"]),
            )
            field = scope.get(name)

            if not field:
                exception_class = (
                    types.BadAttributeLookup
                    if depth
                    else types.UndefinedVariableReference
                )
                raise exception_class(f"No such variable or attribute: {name}")

            # Invalid input
            if (idxed or mapped) and not field.repeated:
                raise types.BadAttributeLookup(
                    f"Collection lookup on non-repeated field: {base}"
                )

            # Can only ignore indexing or mapping in an indexed (or mapped) field
            # if it is the terminal point in the expression.
            if field.repeated and not (idxed or mapped) and first_dot != -1:
                raise types.BadAttributeLookup(
                    (
                        "Accessing attribute on a non-terminal collection without"
                        f"indexing into the collection: {base}"
                    )
                )

            message = field.message
            scope = dict(message.fields) if message else {}
            # Can only map message types, not enums
            if mapped:
                # See https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/descriptor.proto#L496
                # for a better understanding of how map attributes are handled in protobuf
                if not message or not message.options.map_field:
                    raise types.BadAttributeLookup(f"Badly formed mapped field: {base}")

                value_field = message.fields.get("value")
                if not value_field:
                    raise types.BadAttributeLookup(
                        f"Mapped attribute has no value field: {base}"
                    )

                value_message = value_field.message
                if not value_message:
                    raise types.BadAttributeLookup(
                        f"Mapped value field is not a message: {base}"
                    )

                if first_dot != -1:
                    scope = value_message.fields

            # Terminus of the expression.
            if first_dot == -1:
                return field

            # Enums and primitives are only allowed at the tail of an expression.
            if not message:
                raise types.BadAttributeLookup(
                    f"Non-terminal attribute is not a message: {base}"
                )

            return validate_recursively(expression[first_dot + 1 :], scope, depth + 1)

        return validate_recursively(exp, self.var_defs_)

    def _handle_lvalue(self, lval: str, type_: wrappers.Field):
        """Conducts safety checks on an lvalue and adds it to the lexical scope.

        Raises:
            ReservedVariableName: If an attempted lvalue is a reserved keyword.
        """
        if lval in RESERVED_WORDS:
            raise types.ReservedVariableName(
                "Tried to define a variable with reserved name: {}".format(lval)
            )

        # Even though it's valid python to reassign variables to any rvalue,
        # the samplegen spec prohibits this.
        if lval in self.var_defs_:
            raise types.RedefinedVariable("Tried to redefine variable: {}".format(lval))

        self.var_defs_[lval] = type_

    def _validate_format(self, body: List[str]):
        """Validates a format string and corresponding arguments.

        The number of format tokens in the string must equal the
        number of arguments, and each argument must be a defined variable.

        Raises:
            MismatchedFormatSpecifier: If the number of format string segments ("%s") in
                                       a "print" or "comment" block does not equal the
                                       size number of strings in the block minus 1.
            UndefinedVariableReference: If the base lvalue in an expression chain
                                        is not a previously defined lvalue.
        """
        fmt_str = body[0]
        num_prints = fmt_str.count("%s")
        if num_prints != len(body) - 1:
            raise types.MismatchedFormatSpecifier(
                "Expected {} expressions in format string '{}' but found {}".format(
                    num_prints, fmt_str, len(body) - 1
                )
            )

        for expression in body[1:]:
            self.validate_expression(expression)

    def _validate_define(self, body: str):
        """ "Validates 'define' statements.

        Adds the defined lvalue to the lexical scope.
        Other statements can reference it.

         Raises:
             BadAssignment: If a "define" statement is badly formed lexically.
             UndefinedVariableReference: If an attempted rvalue base is a previously
                                         undeclared variable.
        """
        # Note: really checking for safety would be equivalent to
        #       re-implementing the python interpreter.
        m = re.match(r"^([a-zA-Z_]\w*) *= *([^=]+)$", body)
        if not m:
            raise types.BadAssignment(f"Bad assignment statement: {body}")

        lval, rval = m.groups()

        rval_type = self.validate_expression(rval)
        self._handle_lvalue(lval, rval_type)

    def _validate_write_file(self, body):
        """Validate 'write_file' statements.

        The body of a 'write_file' statement is a two-element dict
        with known keys: 'filename' and 'contents'.
        'filename' maps to a list of strings which constitute a format string
        and variable-based rvalues defining the fields.
        'contents' maps to a single variable-based rvalue.

        Raises:
            MismatchedFormatSpecifier: If the filename formatstring is badly formed.
            UndefinedVariableReference: If any of the formatstring variables
                                        or the file contents variable are undefined.
            InvalidStatement: If either 'filename' or 'contents' are absent keys.
        """

        fname_fmt = body.get("filename")
        if not fname_fmt:
            raise types.InvalidStatement(
                "Missing key in 'write_file' statement: 'filename'"
            )

        self._validate_format(fname_fmt)

        contents_var = body.get("contents")
        if not contents_var:
            raise types.InvalidStatement(
                "Missing key in 'write_file' statement: 'contents'"
            )

        self.validate_expression(contents_var)

    @dataclasses.dataclass(frozen=True)
    class LoopParameterField(wrappers.Field):
        # This class is a hack for assigning the iteration variable in a collection loop.
        # In protobuf, the concept of collection<T> is manifested as a repeated
        # field of message type T. Therefore, in order to assign the correct type
        # to a loop iteration parameter, we copy the field that is the collection
        # but remove 'repeated'.
        repeated: bool = False

    def _validate_loop(self, loop):
        """Validates loop headers and statement bodies.

        Checks for correctly defined loop constructs,
        either 'collection' loops with a collection and iteration variable,
        or 'map' loops with a map and at least one of 'key' or 'value'.
        Loops also have a 'body', which contains statements that may
        use the variables from the header.

        The body statements are validated recursively.
        The iteration variable(s) is/are added to the lexical scope
        before validating the statements in the loop body.

        Raises:
            UndefinedVariableReference: If an attempted rvalue base is a previously
                                        undeclared variable.
            BadLoop: If a "loop" segments has unexpected keywords
                     or keyword combinatations.

        """
        segments = set(loop.keys())
        map_args = {self.MAP_KWORD, self.BODY_KWORD}

        # Even though it's valid python to use a variable outside of the lexical
        # scope it was defined in,
        #
        # i.e.
        #   for m in molluscs:
        #     handle(m)
        #   print("Last mollusc: {}".format(m))
        #
        # is allowed, the samplegen spec requires that errors are raised
        # if strict lexical scoping is violated.
        self.var_defs_ = self.var_defs_.new_child()

        if {self.COLL_KWORD, self.VAR_KWORD, self.BODY_KWORD} == segments:
            tokens = loop[self.COLL_KWORD].split(".")

            # TODO: resolve the implicit $resp dilemma
            # if collection_name.startswith("."):
            #     collection_name = "$resp" + collection_name
            collection_field = self.validate_expression(loop[self.COLL_KWORD])

            if not collection_field.repeated:
                raise types.BadLoop(
                    "Tried to use a non-repeated field as a collection: {}".format(
                        tokens[-1]
                    )
                )

            var = loop[self.VAR_KWORD]
            # The collection_field is repeated,
            # but the iteration parameter should not be.
            self._handle_lvalue(
                var,
                self.LoopParameterField(
                    field_pb=collection_field.field_pb,
                    message=collection_field.message,
                    enum=collection_field.enum,
                    meta=collection_field.meta,
                ),
            )

        elif map_args <= segments:
            segments -= map_args
            segments -= {self.KEY_KWORD, self.VAL_KWORD}
            if segments:
                raise types.BadLoop(
                    "Unexpected keywords in loop statement: {}".format(segments)
                )

            map_field = self.validate_expression(loop[self.MAP_KWORD])

            key = loop.get(self.KEY_KWORD)
            if key:
                self._handle_lvalue(key, map_field.message.fields["key"])

            val = loop.get(self.VAL_KWORD)
            if val:
                self._handle_lvalue(val, map_field.message.fields["value"])

            if not (key or val):
                raise types.BadLoop(
                    "Need at least one of 'key' or 'value' in a map loop"
                )

        else:
            raise types.BadLoop("Unexpected loop form: {}".format(segments))

        self.validate_response(loop[self.BODY_KWORD])
        # Restore the previous lexical scope.
        # This is stricter than python scope rules
        # because the samplegen spec mandates it.
        self.var_defs_ = self.var_defs_.parents

    # Add new statement keywords to this table.
    STATEMENT_DISPATCH_TABLE = {
        "define": _validate_define,
        "print": _validate_format,
        "comment": _validate_format,
        "write_file": _validate_write_file,
        "loop": _validate_loop,
    }


def parse_handwritten_specs(
    sample_configs: Sequence[str],
) -> Generator[Dict[str, Any], None, None]:
    """Parse a handwritten sample spec"""

    for config_fpath in sample_configs:
        with open(config_fpath) as f:
            configs = yaml.safe_load_all(f.read())

            for cfg in configs:
                valid = is_valid_sample_cfg(cfg)
                if not valid:
                    raise types.InvalidConfig(
                        "Sample config in '{}' is invalid\n\n{}".format(
                            config_fpath, cfg
                        ),
                        valid,
                    )
                for spec in cfg.get("samples", []):
                    yield spec


def generate_request_object(
    api_schema: api.API,
    service: wrappers.Service,
    message: wrappers.MessageType,
    field_name_prefix: str = "",
):
    """Generate dummy input for a given message.

    Args:
        api_schema (api.API): The schema that defines the API.
        service (wrappers.Service): The service object the message belongs to.
        message (wrappers.MessageType): The message to generate a request object for.
        field_name_prefix (str): A prefix to attach to the field name in the request.

    Returns:
        List[Dict[str, Any]]: A list of dicts that can be turned into TransformedRequests.
    """
    request: List[Dict[str, Any]] = []

    request_fields: List[wrappers.Field] = []

    # There is no standard syntax to mark a oneof as "required" in protos.
    # Assume every oneof is required and pick the first option
    # in each oneof.
    selected_oneofs: List[wrappers.Field] = [
        oneof_fields[0] for oneof_fields in message.oneof_fields().values()
    ]

    # Don't add required fields if they're also marked as oneof
    required_fields = [field for field in message.required_fields if not field.oneof]
    request_fields = selected_oneofs + required_fields

    for field in request_fields:
        # TransformedRequest expects nested fields to be referenced like
        # `destination.input_config.name`
        field_name = ".".join([field_name_prefix, field.name]).lstrip(".")

        # TODO(busunkim): Properly handle map fields
        if field.is_primitive:
            request.append(
                {"field": field_name, "value": field.mock_value_original_type}
            )
        elif field.enum:
            # Choose the last enum value in the list since index 0 is often "unspecified"
            enum_value = field.enum.values[-1].name
            if field.repeated:
                field_value = [enum_value]
            else:
                field_value = enum_value

            request.append({"field": field_name, "value": field_value})
        else:
            # This is a message type, recurse
            # TODO(busunkim):  Some real world APIs have
            # request objects are recursive.
            # Reference `Field.mock_value` to ensure
            # this always terminates.
            request += generate_request_object(
                api_schema,
                service,
                field.type,
                field_name_prefix=field_name,
            )

    return request


def _sync_or_async_from_transport(transport: str) -> str:
    if transport in (api.TRANSPORT_GRPC, api.TRANSPORT_REST):
        return "sync"
    else:  # transport is api.TRANSPORT_GRPC_ASYNC
        # Currently the REST transport does not support async.
        return "async"


def _supports_grpc(service) -> bool:
    return api.TRANSPORT_GRPC in service.clients.keys()


def generate_sample_specs(
    api_schema: api.API, *, opts
) -> Generator[Dict[str, Any], None, None]:
    """Given an API, generate basic sample specs for each method.

    If a service supports gRPC transport, we do not generate
    spec for REST even if it also supports REST transport.

    Args:
        api_schema (api.API): The schema that defines the API.

    Yields:
        Dict[str, Any]: A sample spec.
    """

    gapic_metadata = api_schema.gapic_metadata(opts)

    for service_name, service in gapic_metadata.services.items():
        api_short_name = api_schema.services[
            f"{api_schema.naming.proto_package}.{service_name}"
        ].shortname
        api_version = api_schema.naming.version
        supports_grpc = _supports_grpc(service)
        for transport, client in service.clients.items():
            if supports_grpc and transport == api.TRANSPORT_REST:
                continue
            sync_or_async = _sync_or_async_from_transport(transport)
            for rpc_name, method_list in client.rpcs.items():
                # Region Tag Format:
                # [{START|END} ${apishortname}_${apiVersion}_generated_${serviceName}_${rpcName}_{sync|async|rest}]
                region_tag = f"{api_short_name}_{api_version}_generated_{service_name}_{rpc_name}_{sync_or_async}"

                is_internal = api_schema.all_methods[
                    f"{api_schema.naming.proto_package}.{service_name}.{rpc_name}"
                ].is_internal
                if is_internal:
                    region_tag += "_internal"

                spec = {
                    "rpc": rpc_name,
                    "transport": transport,
                    # `request` and `response` are populated in `preprocess_sample`
                    "service": f"{api_schema.naming.proto_package}.{service_name}",
                    "region_tag": region_tag,
                    "description": f"Snippet for {utils.to_snake_case(rpc_name)}",
                }

                yield spec


def _fill_sample_metadata(sample: dict, api_schema: api.API):
    """Returns snippet metadata for the sample."""

    # Snippet Metadata can't be fully filled out in any one function
    # In this function we add information from
    # the API schema and sample dictionary.
    # See `snippet_metadata.proto` for documentation on the fields

    service = api_schema.services[sample["service"]]
    method = service.methods[sample["rpc"]]
    async_ = sample["transport"] == api.TRANSPORT_GRPC_ASYNC

    snippet_metadata = snippet_metadata_pb2.Snippet()  # type: ignore
    snippet_metadata.region_tag = sample["region_tag"]
    snippet_metadata.description = f"Sample for {sample['rpc']}"
    snippet_metadata.language = snippet_metadata_pb2.Language.PYTHON  # type: ignore
    snippet_metadata.canonical = True
    snippet_metadata.origin = snippet_metadata_pb2.Snippet.Origin.API_DEFINITION  # type: ignore

    # Service Client
    snippet_metadata.client_method.client.short_name = (
        service.async_client_name if async_ else service.client_name
    )
    snippet_metadata.client_method.client.full_name = f"{'.'.join(sample['module_namespace'])}.{sample['module_name']}.{snippet_metadata.client_method.client.short_name}"

    # Service
    snippet_metadata.client_method.method.service.short_name = service.name
    snippet_metadata.client_method.method.service.full_name = (
        f"{api_schema.naming.proto_package}.{service.name}"
    )

    # RPC
    snippet_metadata.client_method.method.short_name = method.name
    snippet_metadata.client_method.method.full_name = (
        f"{api_schema.naming.proto_package}.{service.name}.{method.name}"
    )

    # Client Method
    setattr(snippet_metadata.client_method, "async", async_)
    snippet_metadata.client_method.short_name = utils.to_snake_case(
        method.client_method_name
    )
    snippet_metadata.client_method.full_name = f"{snippet_metadata.client_method.client.full_name}.{snippet_metadata.client_method.short_name}"

    if not method.void:
        snippet_metadata.client_method.result_type = (
            method.client_output_async.ident.sphinx
            if async_
            else method.client_output.ident.sphinx
        )
        if method.server_streaming:
            snippet_metadata.client_method.result_type = (
                f"Iterable[{snippet_metadata.client_method.result_type}]"
            )

    # Client Method Parameters
    parameters = snippet_metadata.client_method.parameters
    if not method.client_streaming:
        parameters.append(
            snippet_metadata_pb2.ClientMethod.Parameter(  # type: ignore
                type=method.input.ident.sphinx, name="request"
            )
        )
        for field in method.flattened_fields.values():
            parameters.append(
                snippet_metadata_pb2.ClientMethod.Parameter(  # type: ignore
                    type=field.ident.sphinx, name=field.name
                )
            )
    else:
        parameters.append(
            snippet_metadata_pb2.ClientMethod.Parameter(  # type: ignore
                type=f"Iterator[{method.input.ident.sphinx}]", name="requests"
            )
        )

    parameters.append(
        snippet_metadata_pb2.ClientMethod.Parameter(  # type: ignore
            name="retry", type="google.api_core.retry.Retry"
        )
    )
    parameters.append(
        snippet_metadata_pb2.ClientMethod.Parameter(  # type: ignore
            name="timeout", type="float"
        )
    )
    parameters.append(
        snippet_metadata_pb2.ClientMethod.Parameter(  # type: ignore
            name="metadata", type="Sequence[Tuple[str, Union[str, bytes]]]"
        )
    )

    return snippet_metadata


def _get_sample_imports(sample: Dict, rpc: wrappers.Method) -> List[str]:
    """Returns sorted sample import statements."""
    module_namespace = ".".join(sample["module_namespace"])
    module_name = sample["module_name"]
    module_import = f"from {module_namespace} import {module_name}"

    imports = [module_import]
    address = rpc.input.meta.address
    # This checks if the request message is part of the service proto package.
    # If not, we should try to include a separate import statement.
    if not address.proto_package.startswith(address.api_naming.proto_package):
        imports.append(str(address.python_import))

    if rpc.is_resumable_upload:
        imports.append(
            "from google.api_core.resumable_transfer import ResumableUploadConfig"
        )
        imports.append("import io")

    return sorted(imports)


def generate_sample(
    sample, api_schema, sample_template: jinja2.Template
) -> Tuple[str, Any]:
    """Generate a standalone, runnable sample.

    Writing the rendered output is left for the caller.

    Args:
        sample (Any): A definition for a single sample.
        api_schema (api.API): The schema that defines the API to which the sample belongs.
        sample_template (jinja2.Template): The template representing a generic sample.

    Returns:
        Tuple(str, snippet_metadata_pb2.Snippet): The rendered sample.
    """
    service_name = sample["service"]
    service = api_schema.services.get(service_name)
    if not service:
        raise types.UnknownService("Unknown service: {}", service_name)

    rpc_name = sample["rpc"]
    rpc = service.methods.get(rpc_name)
    if not rpc:
        raise types.RpcMethodNotFound(
            "Could not find rpc in service {}: {}".format(service_name, rpc_name)
        )

    calling_form = types.CallingForm.method_default(rpc)
    sample["is_internal"] = rpc.is_internal
    sample["is_resumable_upload"] = rpc.is_resumable_upload

    v = Validator(rpc, api_schema)
    # Tweak some small aspects of the sample to set defaults for optional
    # fields, add fields that are required for the template, and so forth.
    v.preprocess_sample(sample, api_schema, rpc)
    sample["request"] = v.validate_and_transform_request(
        calling_form, sample["request"]
    )

    v.validate_response(sample["response"])

    snippet_metadata = _fill_sample_metadata(sample, api_schema)

    # The sample must be preprocessed before calling _get_sample_imports.
    imports = _get_sample_imports(sample, rpc)

    return (
        sample_template.render(
            sample=sample,
            imports=imports,
            calling_form=calling_form,
            calling_form_enum=types.CallingForm,
            trim_blocks=True,
            lstrip_blocks=True,
        ),
        snippet_metadata,
    )
