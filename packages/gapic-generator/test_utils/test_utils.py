# Copyright 2020 Google LLC
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

import collections
import typing

from gapic.schema import metadata
from gapic.schema import naming
from gapic.schema import wrappers
from google.api import annotations_pb2, routing_pb2
from google.api import client_pb2
from google.api import http_pb2
from google.protobuf import descriptor_pb2 as desc


def make_service(
    name: str = "Placeholder",
    host: str = "",
    methods: typing.Tuple[wrappers.Method] = (),
    scopes: typing.Tuple[str] = (),
    visible_resources: typing.Optional[
        typing.Mapping[str, wrappers.CommonResource]
    ] = None,
    version: str = "",
) -> wrappers.Service:
    visible_resources = visible_resources or {}
    # Define a service descriptor, and set a host and oauth scopes if
    # appropriate.
    service_pb = desc.ServiceDescriptorProto(name=name)
    if host:
        service_pb.options.Extensions[client_pb2.default_host] = host
    service_pb.options.Extensions[client_pb2.oauth_scopes] = ",".join(scopes)
    if version:
        service_pb.options.Extensions[client_pb2.api_version] = version

    # Return a service object to test.
    return wrappers.Service(
        service_pb=service_pb,
        methods={m.name: m for m in methods},
        visible_resources=visible_resources,
    )


# FIXME (lukesneeringer): This test method is convoluted and it makes these
#                         tests difficult to understand and maintain.
def make_service_with_method_options(
    *,
    http_rule: http_pb2.HttpRule = None,
    method_signature: str = "",
    in_fields: typing.Tuple[desc.FieldDescriptorProto] = (),
    visible_resources: typing.Optional[
        typing.Mapping[str, wrappers.CommonResource]
    ] = None,
) -> wrappers.Service:
    # Declare a method with options enabled for long-running operations and
    # field headers.
    method = get_method(
        "DoBigThing",
        "foo.bar.ThingRequest",
        "google.longrunning.operations_pb2.Operation",
        lro_response_type="foo.baz.ThingResponse",
        lro_metadata_type="foo.qux.ThingMetadata",
        in_fields=in_fields,
        http_rule=http_rule,
        method_signature=method_signature,
    )

    # Define a service descriptor.
    service_pb = desc.ServiceDescriptorProto(name="ThingDoer")

    # Return a service object to test.
    return wrappers.Service(
        service_pb=service_pb,
        methods={method.name: method},
        visible_resources=visible_resources or {},
    )


def get_method(
    name: str,
    in_type: str,
    out_type: str,
    lro_response_type: str = "",
    lro_metadata_type: str = "",
    *,
    in_fields: typing.Tuple[desc.FieldDescriptorProto] = (),
    http_rule: http_pb2.HttpRule = None,
    method_signature: str = "",
) -> wrappers.Method:
    input_ = get_message(in_type, fields=in_fields)
    output = get_message(out_type)
    lro = None

    # Define a method descriptor. Set the field headers if appropriate.
    method_pb = desc.MethodDescriptorProto(
        name=name,
        input_type=input_.ident.proto,
        output_type=output.ident.proto,
    )
    if lro_response_type:
        lro = wrappers.OperationInfo(
            response_type=get_message(lro_response_type),
            metadata_type=get_message(lro_metadata_type),
        )
    if http_rule:
        ext_key = annotations_pb2.http
        method_pb.options.Extensions[ext_key].MergeFrom(http_rule)
    if method_signature:
        ext_key = client_pb2.method_signature
        method_pb.options.Extensions[ext_key].append(method_signature)

    return wrappers.Method(
        method_pb=method_pb,
        input=input_,
        output=output,
        lro=lro,
        meta=input_.meta,
    )


def get_message(
    dot_path: str,
    *,
    fields: typing.Tuple[desc.FieldDescriptorProto] = (),
) -> wrappers.MessageType:
    # Pass explicit None through (for lro_metadata).
    if dot_path is None:
        return None

    # Note: The `dot_path` here is distinct from the canonical proto path
    # because it includes the module, which the proto path does not.
    #
    # So, if trying to test the DescriptorProto message here, the path
    # would be google.protobuf.descriptor.DescriptorProto (whereas the proto
    # path is just google.protobuf.DescriptorProto).
    pieces = dot_path.split(".")
    pkg, module, name = pieces[:-2], pieces[-2], pieces[-1]

    return wrappers.MessageType(
        fields={
            i.name: wrappers.Field(
                field_pb=i,
                enum=get_enum(i.type_name) if i.type_name else None,
            )
            for i in fields
        },
        nested_messages={},
        nested_enums={},
        message_pb=desc.DescriptorProto(name=name, field=fields),
        meta=metadata.Metadata(
            address=metadata.Address(
                name=name,
                package=tuple(pkg),
                module=module,
            )
        ),
    )


def make_method(
    name: str,
    input_message: wrappers.MessageType = None,
    output_message: wrappers.MessageType = None,
    package: typing.Union[typing.Tuple[str], str] = "foo.bar.v1",
    module: str = "baz",
    http_rule: http_pb2.HttpRule = None,
    signatures: typing.Sequence[str] = (),
    is_deprecated: bool = False,
    routing_rule: routing_pb2.RoutingRule = None,
    is_internal: bool = False,
    **kwargs,
) -> wrappers.Method:
    # Use default input and output messages if they are not provided.
    input_message = input_message or make_message("MethodInput")
    output_message = output_message or make_message("MethodOutput")

    # Create the method pb2.
    method_pb = desc.MethodDescriptorProto(
        name=name,
        input_type=str(input_message.meta.address),
        output_type=str(output_message.meta.address),
        **kwargs,
    )

    if routing_rule:
        ext_key = routing_pb2.routing
        method_pb.options.Extensions[ext_key].MergeFrom(routing_rule)

    # If there is an HTTP rule, process it.
    if http_rule:
        ext_key = annotations_pb2.http
        method_pb.options.Extensions[ext_key].MergeFrom(http_rule)

    # If there are signatures, include them.
    for sig in signatures:
        ext_key = client_pb2.method_signature
        method_pb.options.Extensions[ext_key].append(sig)

    if isinstance(package, str):
        package = tuple(package.split("."))

    if is_deprecated:
        method_pb.options.deprecated = True

    # Instantiate the wrapper class.
    return wrappers.Method(
        method_pb=method_pb,
        input=input_message,
        output=output_message,
        meta=metadata.Metadata(
            address=metadata.Address(
                name=name,
                package=package,
                module=module,
                parent=(f"{name}Service",),
            )
        ),
        is_internal=is_internal,
    )


def make_field(
    name: str = "my_field",
    number: int = 1,
    repeated: bool = False,
    message: wrappers.MessageType = None,
    enum: wrappers.EnumType = None,
    meta: metadata.Metadata = None,
    oneof: str = None,
    **kwargs,
) -> wrappers.Field:
    T = desc.FieldDescriptorProto.Type

    if message:
        kwargs.setdefault("type_name", str(message.meta.address))
        kwargs["type"] = "TYPE_MESSAGE"
    elif enum:
        kwargs.setdefault("type_name", str(enum.meta.address))
        kwargs["type"] = "TYPE_ENUM"
    else:
        kwargs.setdefault("type", T.Value("TYPE_BOOL"))

    if isinstance(kwargs["type"], str):
        kwargs["type"] = T.Value(kwargs["type"])

    label = kwargs.pop("label", 3 if repeated else 1)
    field_pb = desc.FieldDescriptorProto(
        name=name, label=label, number=number, **kwargs
    )

    return wrappers.Field(
        field_pb=field_pb,
        enum=enum,
        message=message,
        meta=meta or metadata.Metadata(),
        oneof=oneof,
    )


def make_message(
    name: str,
    package: str = "foo.bar.v1",
    module: str = "baz",
    fields: typing.Sequence[wrappers.Field] = (),
    meta: metadata.Metadata = None,
    options: desc.MethodOptions = None,
) -> wrappers.MessageType:
    message_pb = desc.DescriptorProto(
        name=name,
        field=[i.field_pb for i in fields],
        options=options,
    )
    return wrappers.MessageType(
        message_pb=message_pb,
        fields=collections.OrderedDict((i.name, i) for i in fields),
        nested_messages={},
        nested_enums={},
        meta=meta
        or metadata.Metadata(
            address=metadata.Address(
                name=name,
                package=tuple(package.split(".")),
                module=module,
            )
        ),
    )


def get_enum(dot_path: str) -> wrappers.EnumType:
    pieces = dot_path.split(".")
    pkg, module, name = pieces[:-2], pieces[-2], pieces[-1]
    return wrappers.EnumType(
        enum_pb=desc.EnumDescriptorProto(name=name),
        meta=metadata.Metadata(
            address=metadata.Address(
                name=name,
                package=tuple(pkg),
                module=module,
            )
        ),
        values=[],
    )


def make_enum(
    name: str,
    package: str = "foo.bar.v1",
    module: str = "baz",
    values: typing.Sequence[typing.Tuple[str, int]] = (),
    meta: metadata.Metadata = None,
    options: desc.EnumOptions = None,
) -> wrappers.EnumType:
    enum_value_pbs = [
        desc.EnumValueDescriptorProto(name=i[0], number=i[1]) for i in values
    ]
    enum_pb = desc.EnumDescriptorProto(
        name=name,
        value=enum_value_pbs,
        options=options,
    )
    return wrappers.EnumType(
        enum_pb=enum_pb,
        values=[wrappers.EnumValueType(enum_value_pb=evpb) for evpb in enum_value_pbs],
        meta=meta
        or metadata.Metadata(
            address=metadata.Address(
                name=name,
                package=tuple(package.split(".")),
                module=module,
            )
        ),
    )


def make_naming(**kwargs) -> naming.Naming:
    kwargs.setdefault("name", "Hatstand")
    kwargs.setdefault("namespace", ("Google", "Cloud"))
    kwargs.setdefault("version", "v1")
    kwargs.setdefault("product_name", "Hatstand")
    return naming.NewNaming(**kwargs)


def make_enum_pb2(
    name: str, *values: typing.Sequence[str], **kwargs
) -> desc.EnumDescriptorProto:
    enum_value_pbs = [
        desc.EnumValueDescriptorProto(name=n, number=i) for i, n in enumerate(values)
    ]
    enum_pb = desc.EnumDescriptorProto(name=name, value=enum_value_pbs, **kwargs)
    return enum_pb


def make_message_pb2(
    name: str, fields: tuple = (), oneof_decl: tuple = (), **kwargs
) -> desc.DescriptorProto:
    return desc.DescriptorProto(
        name=name, field=fields, oneof_decl=oneof_decl, **kwargs
    )


def make_field_pb2(
    name: str,
    number: int,
    type: int = 11,  # 11 == message
    type_name: str = None,
    oneof_index: int = None,
    **kwargs,
) -> desc.FieldDescriptorProto:
    return desc.FieldDescriptorProto(
        name=name,
        number=number,
        type=type,
        type_name=type_name,
        oneof_index=oneof_index,
        **kwargs,
    )


def make_oneof_pb2(name: str) -> desc.OneofDescriptorProto:
    return desc.OneofDescriptorProto(
        name=name,
    )


def make_file_pb2(
    name: str = "my_proto.proto",
    package: str = "example.v1",
    *,
    messages: typing.Sequence[desc.DescriptorProto] = (),
    enums: typing.Sequence[desc.EnumDescriptorProto] = (),
    services: typing.Sequence[desc.ServiceDescriptorProto] = (),
    locations: typing.Sequence[desc.SourceCodeInfo.Location] = (),
) -> desc.FileDescriptorProto:
    return desc.FileDescriptorProto(
        name=name,
        package=package,
        message_type=messages,
        enum_type=enums,
        service=services,
        source_code_info=desc.SourceCodeInfo(location=locations),
    )


def make_doc_meta(
    *,
    leading: str = "",
    trailing: str = "",
    detached: typing.List[str] = [],
) -> desc.SourceCodeInfo.Location:
    return metadata.Metadata(
        documentation=desc.SourceCodeInfo.Location(
            leading_comments=leading,
            trailing_comments=trailing,
            leading_detached_comments=detached,
        ),
    )
