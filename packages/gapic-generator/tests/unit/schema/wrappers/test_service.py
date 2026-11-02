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

import collections
import itertools
import pytest
import typing

from google.api import resource_pb2
from google.cloud import extended_operations_pb2 as ex_ops_pb2
from google.protobuf import descriptor_pb2

from gapic.schema import imp
from gapic.schema.wrappers import CommonResource, MessageType
from gapic.schema import wrappers

from test_utils.test_utils import (
    get_method,
    make_enum,
    make_field,
    make_message,
    make_method,
    make_service,
    make_service_with_method_options,
)

################################
# Helper Functions
################################


def make_resource_opts(*args):
    # Resources are labeled via an options extension
    opts = descriptor_pb2.MessageOptions()
    opts.Extensions[resource_pb2.resource].pattern.append(
        "/".join(f"{arg}/{{{arg}}}" for arg in args)
    )
    opts.Extensions[resource_pb2.resource].type = "/".join(
        f"{arg}/{{{arg}}}" for arg in args
    )
    return opts


################################
# End Helper Functions
################################


def test_service_properties():
    service = make_service(name="ThingDoer")
    assert service.name == "ThingDoer"
    assert service.client_name == "ThingDoerClient"
    assert service.client_package_version == ""
    assert service.async_client_name == "ThingDoerAsyncClient"
    assert service.transport_name == "ThingDoerTransport"
    assert service.grpc_transport_name == "ThingDoerGrpcTransport"
    assert service.grpc_asyncio_transport_name == "ThingDoerGrpcAsyncIOTransport"
    assert service.rest_transport_name == "ThingDoerRestTransport"


def test_service_host():
    service = make_service(host="thingdoer.googleapis.com")
    assert service.host == "thingdoer.googleapis.com"


def test_service_api_version_not_specified():
    service = make_service(host="thingdoer.googleapis.com")
    assert not service.version


def test_service_api_version_exists():
    service = make_service(host="thingdoer.googleapis.com", version="goose")
    assert service.version == "goose"


def test_service_no_host():
    service = make_service()
    assert not service.host


def test_service_scopes():
    service = make_service(scopes=("https://foo/user/", "https://foo/admin/"))
    assert "https://foo/user/" in service.oauth_scopes
    assert "https://foo/admin/" in service.oauth_scopes


def test_service_shortname():
    service = make_service(host="thingdoer")
    assert service.shortname == "thingdoer"

    service = make_service(host="thingdoer:12345")
    assert service.shortname == "thingdoer"


def test_service_names():
    service = make_service(
        name="ThingDoer",
        methods=(
            get_method("DoThing", "foo.bar.ThingRequest", "foo.baz.ThingResponse"),
            get_method("Jump", "foo.bacon.JumpRequest", "foo.bacon.JumpResponse"),
            get_method("Yawn", "a.b.v1.c.YawnRequest", "x.y.v1.z.YawnResponse"),
        ),
    )
    expected_names = {
        "ThingDoer",
        "ThingDoerClient",
        "ThingDoerAsyncClient",
        "do_thing",
        "jump",
        "yawn",
    }
    assert service.names == expected_names


def test_service_name_colliding_modules():
    service = make_service(
        name="ThingDoer",
        methods=(
            get_method("DoThing", "foo.bar.ThingRequest", "foo.bar.ThingResponse"),
            get_method("Jump", "bacon.bar.JumpRequest", "bacon.bar.JumpResponse"),
            get_method("Yawn", "a.b.v1.c.YawnRequest", "a.b.v1.c.YawnResponse"),
        ),
    )
    expected_names = {
        "ThingDoer",
        "ThingDoerClient",
        "ThingDoerAsyncClient",
        "do_thing",
        "jump",
        "yawn",
        "bar",
    }
    assert service.names == expected_names


def test_service_no_scopes():
    service = make_service()
    assert len(service.oauth_scopes) == 0


def test_service_python_modules():
    service = make_service(
        methods=(
            get_method("DoThing", "foo.bar.ThingRequest", "foo.baz.ThingResponse"),
            get_method("Jump", "foo.bacon.JumpRequest", "foo.bacon.JumpResponse"),
            get_method("Yawn", "a.b.v1.c.YawnRequest", "x.y.v1.z.YawnResponse"),
        )
    )
    imports = {
        i.ident.python_import for m in service.methods.values() for i in m.ref_types
    }
    assert imports == {
        imp.Import(package=("a", "b", "v1"), module="c"),
        imp.Import(package=("foo",), module="bacon"),
        imp.Import(package=("foo",), module="bar"),
        imp.Import(package=("foo",), module="baz"),
        imp.Import(package=("x", "y", "v1"), module="z"),
    }


def test_service_python_modules_lro():
    service = make_service_with_method_options()
    method = service.methods["DoBigThing"]
    imports = {i.ident.python_import for i in method.ref_types}
    assert imports == {
        imp.Import(package=("foo",), module="bar"),
        imp.Import(package=("foo",), module="baz"),
        imp.Import(package=("foo",), module="qux"),
        imp.Import(package=("google", "api_core"), module="operation"),
        imp.Import(package=("google", "api_core"), module="operation_async"),
    }


def test_service_python_modules_signature():
    service = make_service_with_method_options(
        in_fields=(
            # type=5 is int, so nothing is added.
            descriptor_pb2.FieldDescriptorProto(name="secs", type=5),
            descriptor_pb2.FieldDescriptorProto(
                name="d",
                type=14,  # enum
                type_name="a.b.c.v2.D",
            ),
        ),
        method_signature="secs,d",
    )

    # Ensure that the service will have the expected imports.
    method = service.methods["DoBigThing"]
    imports = {i.ident.python_import for i in method.ref_types}
    assert imports == {
        imp.Import(package=("a", "b", "c"), module="v2"),
        imp.Import(package=("foo",), module="bar"),
        imp.Import(package=("foo",), module="baz"),
        imp.Import(package=("foo",), module="qux"),
        imp.Import(package=("google", "api_core"), module="operation"),
        imp.Import(package=("google", "api_core"), module="operation_async"),
    }


def test_service_no_lro():
    service = make_service()
    assert service.has_lro is False


def test_service_has_lro():
    service = make_service_with_method_options()
    assert service.has_lro


def test_module_name():
    service = make_service(name="MyService")
    assert service.module_name == "my_service"


def test_resource_messages():
    # Regular, top level resource
    squid_resource = make_message("Squid", options=make_resource_opts("squid"))
    squid_request = make_message(
        "CreateSquid",
        fields=(make_field("squid", message=squid_resource),),
    )

    # Nested resource
    squamosa_message = make_message(
        "Squamosa",
        options=make_resource_opts("clam", "squamosa"),
    )
    clam_resource = make_message(
        "Clam",
        options=make_resource_opts("clam"),
        fields=(make_field("squamosa", message=squamosa_message),),
    )
    clam_request = make_message(
        "CreateClam",
        fields=(
            make_field("clam", message=clam_resource),
            # Red herring, not resources :)
            make_field("zone", 2, enum=make_enum("Zone")),
            make_field("pearls", 3, True, message=make_message("Pearl")),
        ),
    )

    # Some special APIs have request messages that _are_ resources.
    whelk_resource = make_message("Whelk", options=make_resource_opts("whelk"))

    # Not a resource
    octopus_request = make_message(
        "CreateOctopus",
        fields=(make_field("Octopus", message=make_message("Octopus")),),
    )

    service = make_service(
        "Molluscs",
        methods=(
            make_method(
                f"{message.name}",
                input_message=message,
            )
            for message in (
                squid_request,
                clam_request,
                whelk_resource,
                octopus_request,
            )
        ),
    )

    expected = (
        clam_resource,
        squamosa_message,
        squid_resource,
        whelk_resource,
    )
    actual = service.resource_messages
    assert expected == actual


def test_resource_messages_dict():
    # Regular, top level resource
    squid_resource = make_message("Squid", options=make_resource_opts("squid"))
    squid_request = make_message(
        "CreateSquid",
        fields=(make_field("squid", message=squid_resource),),
    )

    # Nested resource
    squamosa_message = make_message(
        "Squamosa",
        options=make_resource_opts("clam", "squamosa"),
    )
    clam_resource = make_message(
        "Clam",
        options=make_resource_opts("clam"),
        fields=(make_field("squamosa", message=squamosa_message),),
    )
    clam_request = make_message(
        "CreateClam",
        fields=(
            make_field("clam", message=clam_resource),
            # Red herring, not resources :)
            make_field("zone", 2, enum=make_enum("Zone")),
            make_field("pearls", 3, True, message=make_message("Pearl")),
        ),
    )

    # Some special APIs have request messages that _are_ resources.
    whelk_resource = make_message("Whelk", options=make_resource_opts("whelk"))

    # Not a resource
    octopus_request = make_message(
        "CreateOctopus",
        fields=(make_field("Octopus", message=make_message("Octopus")),),
    )

    service = make_service(
        "Molluscs",
        methods=(
            make_method(
                f"{message.name}",
                input_message=message,
            )
            for message in (
                squid_request,
                clam_request,
                whelk_resource,
                octopus_request,
            )
        ),
    )

    expected = {
        # Service specific
        "squid/{squid}": squid_resource,
        "clam/{clam}": clam_resource,
        "whelk/{whelk}": whelk_resource,
        "clam/{clam}/squamosa/{squamosa}": squamosa_message,
        # Common resources
        "cloudresourcemanager.googleapis.com/Project": service.common_resources[
            "cloudresourcemanager.googleapis.com/Project"
        ].message_type,
        "cloudresourcemanager.googleapis.com/Organization": service.common_resources[
            "cloudresourcemanager.googleapis.com/Organization"
        ].message_type,
        "cloudresourcemanager.googleapis.com/Folder": service.common_resources[
            "cloudresourcemanager.googleapis.com/Folder"
        ].message_type,
        "cloudbilling.googleapis.com/BillingAccount": service.common_resources[
            "cloudbilling.googleapis.com/BillingAccount"
        ].message_type,
        "locations.googleapis.com/Location": service.common_resources[
            "locations.googleapis.com/Location"
        ].message_type,
    }
    actual = service.resource_messages_dict
    assert expected == actual


def test_service_unknown_resource_reference():
    # This happens occasionally.
    opts = descriptor_pb2.FieldOptions()
    res_ref = opts.Extensions[resource_pb2.resource_reference]
    res_ref.type = "*"
    squid_request = make_message(
        "CreateSquid",
        fields=(
            make_field(
                "parent",
                type="TYPE_STRING",
                options=opts,
            ),
        ),
    )
    squid_service = make_service(
        "SquidService",
        methods=(
            make_method(
                "CreateSquid",
                input_message=squid_request,
            ),
        ),
    )

    assert not squid_service.resource_messages


def test_service_any_streaming():
    for client, server in itertools.product((True, False), (True, False)):
        service = make_service(
            f"ClientStream{client}:ServerStream{server}",
            methods=(
                (
                    make_method(
                        f"GetMollusc",
                        input_message=make_message(
                            "GetMolluscRequest",
                        ),
                        output_message=make_message(
                            "GetMolluscResponse",
                        ),
                        client_streaming=client,
                        server_streaming=server,
                    ),
                )
            ),
        )

        assert service.any_client_streaming == client
        assert service.any_server_streaming == server


def test_service_any_deprecated():
    service = make_service(
        name="Service",
        methods=(
            (
                make_method(
                    f"GetMollusc",
                    input_message=make_message(
                        "GetMolluscRequest",
                    ),
                    output_message=make_message(
                        "GetMolluscResponse",
                    ),
                ),
            )
        ),
    )

    assert service.any_deprecated == False

    deprecated_service = make_service(
        name="ServiceWithDeprecatedMethod",
        methods=(
            (
                make_method(
                    f"GetMollusc",
                    input_message=make_message(
                        "GetMolluscRequest",
                    ),
                    output_message=make_message(
                        "GetMolluscResponse",
                    ),
                    is_deprecated=True,
                ),
            )
        ),
    )

    assert deprecated_service.any_deprecated == True


def test_has_pagers():
    paged = make_field(name="foos", message=make_message("Foo"), repeated=True)
    input_msg = make_message(
        name="ListFoosRequest",
        fields=(
            make_field(name="parent", type=9),  # str
            make_field(name="page_size", type=5),  # int
            make_field(name="page_token", type=9),  # str
        ),
    )
    output_msg = make_message(
        name="ListFoosResponse",
        fields=(
            paged,
            make_field(name="next_page_token", type=9),  # str
        ),
    )
    method = make_method(
        "ListFoos",
        input_message=input_msg,
        output_message=output_msg,
    )

    service = make_service(
        name="Fooer",
        methods=(method,),
    )
    assert service.has_pagers

    other_service = make_service(
        name="Unfooer",
        methods=(get_method("Unfoo", "foo.bar.UnfooReq", "foo.bar.UnFooResp"),),
    )
    assert not other_service.has_pagers


def test_default_common_resources():
    service = make_service(name="MolluscMaker")

    assert service.common_resources == {
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
    }


def test_common_resource_patterns():
    species = CommonResource(
        "nomenclature.linnaen.com/Species",
        "families/{family}/genera/{genus}/species/{species}",
    )
    species_msg = species.message_type

    assert (
        species_msg.resource_path
        == "families/{family}/genera/{genus}/species/{species}"
    )
    assert species_msg.resource_type == "Species"
    assert species_msg.resource_path_args == ["family", "genus", "species"]
    assert (
        species_msg.path_regex_str
        == "^families/(?P<family>.+?)/genera/(?P<genus>.+?)/species/(?P<species>.+?)$"
    )


def test_resource_response():
    # Top level response resource
    squid_resource = make_message("Squid", options=make_resource_opts("squid"))
    squid_request = make_message("CreateSquidRequest")

    # Nested response resource
    clam_resource = make_message("Clam", options=make_resource_opts("clam"))
    clam_response = make_message(
        "CreateClamResponse",
        fields=(make_field("clam", message=clam_resource),),
    )
    clam_request = make_message("CreateClamRequest")

    mollusc_service = make_service(
        "MolluscService",
        methods=(
            make_method(f"{request.name}", request, response)
            for request, response in (
                (squid_request, squid_resource),
                (clam_request, clam_response),
            )
        ),
    )

    expected = (clam_resource, squid_resource)
    actual = mollusc_service.resource_messages
    assert expected == actual


def test_operation_polling_method():
    T = descriptor_pb2.FieldDescriptorProto.Type

    operation = make_message(
        name="Operation",
        fields=[
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(
                ("name", "status", "error_code", "error_message"), start=1
            )
        ],
    )
    for f in operation.fields.values():
        options = descriptor_pb2.FieldOptions()
        # Note: The field numbers were carefully chosen to be the corresponding enum values.
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    request = make_message(
        name="GetOperation",
        fields=[make_field(name="name", type=T.Value("TYPE_STRING"), number=1)],
    )

    options = descriptor_pb2.MethodOptions()
    options.Extensions[ex_ops_pb2.operation_polling_method] = True
    polling_method = make_method(
        name="Get",
        input_message=request,
        output_message=operation,
        options=options,
    )

    # Even though polling_method returns an Operation, it isn't an LRO
    ops_service = make_service(
        name="CustomOperations",
        methods=[
            polling_method,
            make_method(
                name="Delete",
                input_message=make_message(name="Input"),
                output_message=make_message("Output"),
            ),
        ],
    )

    assert ops_service.operation_polling_method == polling_method

    # Methods are LROs, so they are not polling methods
    user_service = make_service(
        name="ComputationStarter",
        methods=[
            make_method(
                name="Start",
                input_message=make_message(name="StartRequest"),
                output_message=operation,
            ),
        ],
    )

    assert not user_service.operation_polling_method


def test_extended_operations_lro_detection():
    T = descriptor_pb2.FieldDescriptorProto.Type

    operation = make_message(
        name="Operation",
        fields=[
            make_field(name=name, type=T.Value("TYPE_STRING"), number=i)
            for i, name in enumerate(
                ("name", "status", "error_code", "error_message"), start=1
            )
        ],
    )
    for f in operation.fields.values():
        options = descriptor_pb2.FieldOptions()
        # Note: The field numbers were carefully chosen to be the corresponding enum values.
        options.Extensions[ex_ops_pb2.operation_field] = f.number
        f.options.MergeFrom(options)

    request = make_message(
        name="GetOperation",
        fields=[make_field(name="name", type=T.Value("TYPE_STRING"), number=1)],
    )

    options = descriptor_pb2.MethodOptions()
    options.Extensions[ex_ops_pb2.operation_polling_method] = True
    polling_method = make_method(
        name="Get",
        input_message=request,
        output_message=operation,
        options=options,
    )

    ops_service = make_service(
        name="CustomOperations",
        methods=[
            polling_method,
            make_method(
                name="Delete",
                input_message=make_message(name="Input"),
                output_message=make_message("Output"),
            ),
        ],
    )

    assert not ops_service.has_extended_lro
    assert not ops_service.any_extended_operations_methods
    assert not polling_method.operation_service

    # Methods are LROs, so they are not polling methods
    lro_opts = descriptor_pb2.MethodOptions()
    lro_opts.Extensions[ex_ops_pb2.operation_service] = "CustomOperations"
    lro = make_method(
        name="Start",
        input_message=make_message(name="StartRequest"),
        output_message=operation,
        options=lro_opts,
    )
    user_service = make_service(
        name="ComputationStarter",
        methods=[
            lro,
        ],
    )

    assert user_service.any_extended_operations_methods
    # Note: we can't have the operation_service property point to the actual operation service
    # because Service objects can't perform the lookup.
    # Instead we kick that can to the API object and make it do the lookup and verification.
    assert lro.operation_service == "CustomOperations"


def test_resource_messages_throws_informative_collision_error():
    # 1. Create options with explicit colliding resource types AND valid patterns
    opts_1 = descriptor_pb2.MessageOptions()
    opts_1.Extensions[resource_pb2.resource].type = "ces.googleapis.com/Tool"
    opts_1.Extensions[resource_pb2.resource].pattern.append("ces/{ces}/tool")
    
    opts_2 = descriptor_pb2.MessageOptions()
    opts_2.Extensions[resource_pb2.resource].type = "workspace.googleapis.com/Tool"
    opts_2.Extensions[resource_pb2.resource].pattern.append("workspaces/{workspace}/tool")
    
    # 2. Use the test helpers to build the messages
    msg_1 = make_message("MessageOne", options=opts_1)
    msg_2 = make_message("MessageTwo", options=opts_2)

    # 3. Build the service with BOTH methods (so the property loops) 
    # AND visible_resources (so the internal lookups succeed).
    service = make_service(
        name="MyService",
        methods=(
            make_method("GetToolOne", input_message=msg_1),
            make_method("GetToolTwo", input_message=msg_2),
        ),
        visible_resources={
            "ces.googleapis.com/Tool": msg_1,
            "workspace.googleapis.com/Tool": msg_2,
        }
    )

    # 4. Assert that asking the service for its resources throws the custom error
    expected_error_regex = r"(?s)Namespace collision detected.*--resource-name-alias"
    
    with pytest.raises(ValueError, match=expected_error_regex):
        _ = service.resource_messages


def test_resource_messages_raises_on_malformed_typeless_resource():
    # 1. Create a malformed resource: it has a pattern, but no type!
    opts = descriptor_pb2.MessageOptions()
    opts.Extensions[resource_pb2.resource].pattern.append("workspaces/{workspace}")
    
    malformed_msg = make_message("MalformedMessage", options=opts)
    
    service = make_service(
        name="MyService",
        methods=(
            make_method("DoThing", input_message=malformed_msg),
        )
    )
    
    # 2. Trigger the property and expect it to fail fast with the AIP-123 URL
    with pytest.raises(ValueError, match="https://google.aip.dev/123"):
        _ = service.resource_messages


def test_service_has_resumable_upload_methods():
    # Verify that a service containing a resumable upload method reports
    # has_resumable_upload_methods as True.
    m_upload = make_method("UploadMedia")
    m_status = make_method("GetStatus")

    service_with_resumable = make_service(
        name="ResumableService",
        methods=(m_upload, m_status),
    )
    assert service_with_resumable.has_resumable_upload_methods

    # Verify that a service with only standard methods reports
    # has_resumable_upload_methods as False.
    m_other = make_method("DoThing")
    service_without_resumable = make_service(
        name="StandardService",
        methods=(m_other,),
    )
    assert not service_without_resumable.has_resumable_upload_methods

