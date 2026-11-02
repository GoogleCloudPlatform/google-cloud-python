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


import jinja2
import os.path as path
import gapic.samplegen.samplegen as samplegen
import gapic.samplegen_utils.utils as sample_utils
import gapic.utils as utils

from gapic.samplegen_utils.types import CallingForm
from textwrap import dedent
from .. import common_types


def check_template(template_fragment, expected_output, **kwargs):
    # Making a new environment for every unit test seems wasteful,
    # but the obvious alternative (make env an instance attribute
    # and passing a FunctionLoader whose load function returns
    # a constantly reassigned string attribute) isn't any faster
    # and is less clear.
    expected_output = dedent(expected_output)
    env = jinja2.Environment(
        loader=jinja2.ChoiceLoader(
            [
                jinja2.FileSystemLoader(
                    searchpath=path.realpath(
                        path.join(
                            path.dirname(__file__),
                            "..",
                            "..",
                            "..",
                            "gapic",
                            "templates",
                            "examples",
                        )
                    )
                ),
                jinja2.DictLoader({"template_fragment": dedent(template_fragment)}),
            ]
        ),
        undefined=jinja2.StrictUndefined,
        extensions=["jinja2.ext.do"],
        trim_blocks=True,
        lstrip_blocks=True,
    )

    env.filters["snake_case"] = utils.to_snake_case
    env.filters["coerce_response_name"] = sample_utils.coerce_response_name
    env.filters["render_format_string"] = sample_utils.render_format_string

    template = env.get_template("template_fragment")
    text = template.render(**kwargs)
    expected_output = dedent(expected_output)

    assert text == expected_output


def test_render_attr_value():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_attr("mollusc", request) }}
        """,
        """
        mollusc.order = Molluscs.Cephalopoda.Coleoidea
        """,
        request=samplegen.AttributeRequestSetup(
            field="order", value="Molluscs.Cephalopoda.Coleoidea"
        ),
    )


def test_render_attr_input_parameter():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_attr("squid", request) }}
        """,
        """

        # species = 'Humboldt'
        squid.species = species
        """,
        request=samplegen.AttributeRequestSetup(
            field="species", value="'Humboldt'", input_parameter="species"
        ),
    )


def test_render_attr_file():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_attr("classify_mollusc_request", request) }}
        """,
        """

        # mollusc_video_path = 'path/to/mollusc/video.mkv'
        with open(mollusc_video_path, "rb") as f:
            classify_mollusc_request.mollusc_video = f.read()
        """,
        request=samplegen.AttributeRequestSetup(
            field="mollusc_video",
            value="'path/to/mollusc/video.mkv'",
            input_parameter="mollusc_video_path",
            value_is_file=True,
        ),
    )


def test_render_request_basic():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_setup(request, module_name, request_type) }}
        """,
        """
        # Initialize request argument(s)
        cephalopod = mollusca.Cephalopod()

        # cephalopod_mass = '10 kg'
        cephalopod.mantle_mass = cephalopod_mass

        # photo_path = 'path/to/cephalopod/photo.jpg'
        with open(photo_path, "rb") as f:
            cephalopod.photo = f.read()
        cephalopod.order = Molluscs.Cephalopoda.Coleoidea

        gastropod = mollusca.Gastropod()

        # gastropod_mass = '1 kg'
        gastropod.mantle_mass = gastropod_mass
        gastropod.order = Molluscs.Gastropoda.Pulmonata

        # movie_path = 'path/to/gastropod/movie.mkv'
        with open(movie_path, "rb") as f:
            gastropod.movie = f.read()

        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(
                    base="cephalopod",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="mantle_mass",
                            value="'10 kg'",
                            input_parameter="cephalopod_mass",
                        ),
                        samplegen.AttributeRequestSetup(
                            field="photo",
                            value="'path/to/cephalopod/photo.jpg'",
                            input_parameter="photo_path",
                            value_is_file=True,
                        ),
                        samplegen.AttributeRequestSetup(
                            field="order", value="Molluscs.Cephalopoda.Coleoidea"
                        ),
                    ],
                    single=None,
                ),
                samplegen.TransformedRequest(
                    base="gastropod",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="mantle_mass",
                            value="'1 kg'",
                            input_parameter="gastropod_mass",
                        ),
                        samplegen.AttributeRequestSetup(
                            field="order", value="Molluscs.Gastropoda.Pulmonata"
                        ),
                        samplegen.AttributeRequestSetup(
                            field="movie",
                            value="'path/to/gastropod/movie.mkv'",
                            input_parameter="movie_path",
                            value_is_file=True,
                        ),
                    ],
                    single=None,
                ),
            ],
            flattenable=True,
        ),
        module_name="mollusca",
        request_type=common_types.DummyMessage(
            fields={
                "cephalopod": common_types.DummyField(
                    name="cephalopod",
                    type=common_types.DummyMessageTypePB(name="Cephalopod"),
                ),
                "gastropod": common_types.DummyField(
                    name="gastropod",
                    type=common_types.DummyMessageTypePB(name="Gastropod"),
                ),
            }
        ),
    )


def test_render_request_unflattened():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_setup(request, module_name, request_type, calling_form, calling_form_enum) }}
        """,
        """
        # Initialize request argument(s)
        cephalopod = mollusca.Cephalopod()

        # cephalopod_mass = '10 kg'
        cephalopod.mantle_mass = cephalopod_mass

        # photo_path = 'path/to/cephalopod/photo.jpg'
        with open(photo_path, "rb") as f:
            cephalopod.photo = f.read()
        cephalopod.order = Molluscs.Cephalopoda.Coleoidea

        gastropod = mollusca.Gastropod()

        # gastropod_mass = '1 kg'
        gastropod.mantle_mass = gastropod_mass
        gastropod.order = Molluscs.Gastropoda.Pulmonata

        # movie_path = 'path/to/gastropod/movie.mkv'
        with open(movie_path, "rb") as f:
            gastropod.movie = f.read()

        request = mollusca.CreateMolluscRequest(
            cephalopod=cephalopod,
            gastropod=gastropod,
            bivalve="humboldt",
        )
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(
                    base="cephalopod",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="mantle_mass",
                            value="'10 kg'",
                            input_parameter="cephalopod_mass",
                        ),
                        samplegen.AttributeRequestSetup(
                            field="photo",
                            value="'path/to/cephalopod/photo.jpg'",
                            input_parameter="photo_path",
                            value_is_file=True,
                        ),
                        samplegen.AttributeRequestSetup(
                            field="order", value="Molluscs.Cephalopoda.Coleoidea"
                        ),
                    ],
                    single=None,
                ),
                samplegen.TransformedRequest(
                    base="gastropod",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="mantle_mass",
                            value="'1 kg'",
                            input_parameter="gastropod_mass",
                        ),
                        samplegen.AttributeRequestSetup(
                            field="order", value="Molluscs.Gastropoda.Pulmonata"
                        ),
                        samplegen.AttributeRequestSetup(
                            field="movie",
                            value="'path/to/gastropod/movie.mkv'",
                            input_parameter="movie_path",
                            value_is_file=True,
                        ),
                    ],
                    single=None,
                ),
                samplegen.TransformedRequest(
                    base="bivalve",
                    body=None,
                    single=samplegen.AttributeRequestSetup(
                        value='"humboldt"',
                    ),
                ),
            ]
        ),
        module_name="mollusca",
        request_type=common_types.DummyMessage(
            fields={
                "cephalopod": common_types.DummyField(
                    name="cephalopod",
                    type=common_types.DummyMessageTypePB(name="Cephalopod"),
                ),
                "gastropod": common_types.DummyField(
                    name="gastropod",
                    type=common_types.DummyMessageTypePB(name="Gastropod"),
                ),
            },
            ident=common_types.DummyIdent(name="CreateMolluscRequest"),
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
    )


def test_render_request_resource_name():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_setup(request) }}
        """,
        """
        # Initialize request argument(s)
        kingdom = "animalia"
        phylum = mollusca
        taxon = f"kingdom/{kingdom}/phylum/{phylum}"

        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(
                    base="taxon",
                    single=None,
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="kingdom",
                            value='"animalia"',
                        ),
                        samplegen.AttributeRequestSetup(
                            field="phylum",
                            value="mollusca",
                            input_parameter="mollusca",
                        ),
                    ],
                    pattern="kingdom/{kingdom}/phylum/{phylum}",
                ),
            ],
            flattenable=True,
        ),
    )


def test_render_print():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_print(["Mollusc"]) }}
        """,
        """
        print("Mollusc")
        """,
    )


def test_render_print_args():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_print(["$resp %s %s", "$resp.squids", "$resp.clams"]) }}
        """,
        """
        print(f"$resp {response.squids} {response.clams}")
        """,
    )


def test_render_comment():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_comment(["Mollusc"]) }}
        """,
        """
        # Mollusc
        """,
    )


def test_render_comment_args():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_comment(["$resp %s %s", "$resp.squids", "$resp.clams"]) }}
        """,
        """
        # $resp response.squids response.clams
        """,
    )


def test_define():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_define("squid=humboldt") }}
        """,
        """
        squid = humboldt
        """,
    )


def test_define_resp():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_define("squid=$resp.squid") }}
        """,
        """
        squid = response.squid
        """,
    )


def test_dispatch_print():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement({"print" : ["Squid"] }) }}
        """,
        """
        print("Squid")

        """,
    )


def test_dispatch_define():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement({"define": "squid=humboldt"})}}
        """,
        """
        squid = humboldt

        """,
    )


def test_dispatch_comment():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement({"comment" : ["Squid"] }) }}
        """,
        """
        # Squid

        """,
    )


def test_write_file():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_write_file({"filename": ["specimen-%s",
                                                 "$resp.species"],
                                    "contents": "$resp.photo"}) }}
        """,
        """
        with open(f"specimen-{response.species}", "wb") as f:
            f.write(response.photo)
        """,
    )


def test_dispatch_write_file():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement({"write_file":
                                       {"filename": ["specimen-%s",
                                                     "$resp.species"],
                                        "contents": "$resp.photo"}})}}
        """,
        """
        with open(f"specimen-{response.species}", "wb") as f:
            f.write(response.photo)

        """,
    )


def test_collection_loop():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_collection_loop(collection) }}
        """,
        """
        for m in response.molluscs:
            print(f"Mollusc: {m}")


        """,
        collection={
            "collection": "$resp.molluscs",
            "variable": "m",
            "body": [{"print": ["Mollusc: %s", "m"]}],
        },
    )


def test_dispatch_collection_loop():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement(statement) }}""",
        """
        for m in molluscs:
            print(f"Mollusc: {m}")



        """,
        statement={
            "loop": {
                "collection": "molluscs",
                "variable": "m",
                "body": [{"print": ["Mollusc: %s", "m"]}],
            }
        },
    )


def test_map_loop():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_map_loop(map_loop)
        }}""",
        """
        for cls, example in response.molluscs.items():
            print(f"A {example} is a {cls}")


        """,
        map_loop={
            "map": "$resp.molluscs",
            "key": "cls",
            "value": "example",
            "body": [{"print": ["A %s is a %s", "example", "cls"]}],
        },
    )


def test_map_loop_no_key():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_map_loop(map_loop)
        }}
        """,
        """
        for example in response.molluscs.values():
            print(f"A {example} is a mollusc")


        """,
        map_loop={
            "map": "$resp.molluscs",
            "value": "example",
            "body": [{"print": ["A %s is a mollusc", "example"]}],
        },
    )


def test_map_loop_no_value():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_map_loop(map_loop)
        }}
        """,
        """
        for cls in response.molluscs.keys():
            print(f"A {cls} is a mollusc")


        """,
        map_loop={
            "map": "$resp.molluscs",
            "key": "cls",
            "body": [{"print": ["A %s is a mollusc", "cls"]}],
        },
    )


def test_dispatch_map_loop():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement(statement) }}
        """,
        """
        for cls, example in molluscs.items():
            print(f"A {example} is a {cls}")



        """,
        statement={
            "loop": {
                "map": "molluscs",
                "key": "cls",
                "value": "example",
                "body": [{"print": ["A %s is a %s", "example", "cls"]}],
            }
        },
    )


def test_render_nested_loop_collection():
    # Note: the vast quantity of extraneous tailing whitespace is an artifact of the
    # recursive dispatch and indentation.
    # The calling form macros are responsible for trimming it out.
    statement = {
        "loop": {
            "collection": "$resp.molluscs",
            "variable": "m",
            "body": [
                {
                    "loop": {
                        "collection": "m.tentacles",
                        "variable": "t",
                        "body": [
                            {
                                "loop": {
                                    "collection": "t.suckers",
                                    "variable": "s",
                                    "body": [{"print": ["Sucker: %s", "s"]}],
                                }
                            }
                        ],
                    }
                }
            ],
        }
    }
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement(statement) }}
        """,
        """
        for m in response.molluscs:
            for t in m.tentacles:
                for s in t.suckers:
                    print(f"Sucker: {s}")







        """,
        statement=statement,
    )


def test_render_nested_loop_map():
    # Note: the vast quantity of extraneous tailing whitespace is an artifact of the
    # recursive dispatch and indentation.
    # The calling form macros are responsible for trimming it out.
    statement = {
        "loop": {
            "map": "$resp.molluscs",
            "key": "klass",
            "value": "orders",
            "body": [
                {
                    "loop": {
                        "map": "orders",
                        "key": "order",
                        "value": "families",
                        "body": [
                            {
                                "loop": {
                                    "map": "families",
                                    "key": "family",
                                    "value": "ex",
                                    "body": [{"print": ["Example: %s", "ex"]}],
                                }
                            }
                        ],
                    }
                }
            ],
        }
    }

    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.dispatch_statement(statement) }}
        """,
        """
        for klass, orders in response.molluscs.items():
            for order, families in orders.items():
                for family, ex in families.items():
                    print(f"Example: {ex}")







        """,
        statement=statement,
    )


def test_print_input_params():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.print_input_params(request) }}

        """,
        """
        mass, length, color
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(
                    base="squid",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="mass", value="10 kg", input_parameter="mass"
                        ),
                        samplegen.AttributeRequestSetup(
                            field="length", value="20 m", input_parameter="length"
                        ),
                    ],
                    single=None,
                ),
                samplegen.TransformedRequest(
                    base="diameter",
                    single=samplegen.AttributeRequestSetup(value="10 cm"),
                    body=None,
                ),
                samplegen.TransformedRequest(
                    base="color",
                    single=samplegen.AttributeRequestSetup(
                        value="red", input_parameter="color"
                    ),
                    body=None,
                ),
            ]
        ),
    )


CALLING_FORM_TEMPLATE_TEST_STR = """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_calling_form("TEST_INVOCATION_TXT", calling_form,
                                   calling_form_enum, transport,
                                   [{"print": ["Test print statement"]}]) }}
        """


def test_render_calling_form_request():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   response = TEST_INVOCATION_TXT

                   # Handle the response
                   print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc",
    )


def test_render_calling_form_paged_all():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   page_result = TEST_INVOCATION_TXT

                   # Handle the response
                   for response in page_result:
                       print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestPagedAll,
        transport="grpc",
    )


def test_render_calling_form_paged_all_async():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   page_result = TEST_INVOCATION_TXT

                   # Handle the response
                   async for response in page_result:
                       print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestPagedAll,
        transport="grpc-async",
    )


def test_render_calling_form_paged():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                    # Make the request
                    page_result = TEST_INVOCATION_TXT

                    # Handle the response
                    for page in page_result.pages():
                        for response in page:
                            print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestPaged,
        transport="grpc",
    )


def test_render_calling_form_paged_async():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                    # Make the request
                    page_result = TEST_INVOCATION_TXT

                    # Handle the response
                    async for page in page_result.pages():
                        for response in page:
                            print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestPaged,
        transport="grpc-async",
    )


def test_render_calling_form_streaming_server():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   stream = TEST_INVOCATION_TXT

                   # Handle the response
                   for response in stream:
                       print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingServer,
        transport="grpc",
    )


def test_render_calling_form_streaming_server_async():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   stream = TEST_INVOCATION_TXT

                   # Handle the response
                   async for response in stream:
                       print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingServer,
        transport="grpc-async",
    )


def test_render_calling_form_streaming_bidi():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   stream = TEST_INVOCATION_TXT

                   # Handle the response
                   for response in stream:
                       print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingBidi,
        transport="grpc",
    )


def test_render_calling_form_streaming_bidi_async():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   stream = TEST_INVOCATION_TXT

                   # Handle the response
                   async for response in stream:
                       print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingBidi,
        transport="grpc-async",
    )


def test_render_calling_form_longrunning():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   operation = TEST_INVOCATION_TXT

                   print("Waiting for operation to complete...")

                   response = operation.result()

                   # Handle the response
                   print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.LongRunningRequestPromise,
        transport="grpc",
    )


def test_render_calling_form_longrunning_async():
    check_template(
        CALLING_FORM_TEMPLATE_TEST_STR,
        """
                   # Make the request
                   operation = TEST_INVOCATION_TXT

                   print("Waiting for operation to complete...")

                   response = await operation.result()

                   # Handle the response
                   print("Test print statement")
                   """,
        calling_form_enum=CallingForm,
        calling_form=CallingForm.LongRunningRequestPromise,
        transport="grpc-async",
    )


def test_render_method_call_basic():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client.categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc",
    )


def test_render_method_call_basic_async():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        await client.categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc-async",
    )


def test_render_method_call_lro_async():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        await client.categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.LongRunningRequestPromise,
        transport="grpc-async",
    )


def test_render_method_call_paged_async():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client.categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestPaged,
        transport="grpc-async",
    )


def test_render_method_call_paged_all_async():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client.categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestPagedAll,
        transport="grpc-async",
    )


def test_render_method_call_basic_flattenable():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client.categorize_mollusc(video=video, audio=audio, guess=guess)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
            flattenable=True,
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc",
    )


def test_render_method_call_bidi():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client.categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingBidi,
        transport="grpc",
    )


def test_render_method_call_bidi_async():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        await client.categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingBidi,
        transport="grpc-async",
    )


def test_render_method_call_client():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
        calling_form, calling_form_enum, transport) }}
        """,
        """
        client.categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingClient,
        transport="grpc",
    )


def test_render_method_call_client_async():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": False,
                                    },
        calling_form, calling_form_enum, transport) }}
        """,
        """
        await client.categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingClient,
        transport="grpc-async",
    )


def test_render_method_call_basic_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client._categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc",
    )


def test_render_method_call_basic_async_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        await client._categorize_mollusc(request=request)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc-async",
    )


def test_render_method_call_basic_flattenable_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client._categorize_mollusc(video=video, audio=audio, guess=guess)
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None),
                samplegen.TransformedRequest(base="audio", body=True, single=None),
                samplegen.TransformedRequest(base="guess", body=True, single=None),
            ],
            flattenable=True,
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.Request,
        transport="grpc",
    )


def test_render_method_call_bidi_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        client._categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingBidi,
        transport="grpc",
    )


def test_render_method_call_bidi_async_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
                                  calling_form, calling_form_enum, transport) }}
        """,
        """
        await client._categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingBidi,
        transport="grpc-async",
    )


def test_render_method_call_client_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
        calling_form, calling_form_enum, transport) }}
        """,
        """
        client._categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingClient,
        transport="grpc",
    )


def test_render_method_call_client_async_internal():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_method_call({"rpc": "CategorizeMollusc",
                                     "request": request,
                                     "is_internal": True,
                                    },
        calling_form, calling_form_enum, transport) }}
        """,
        """
        await client._categorize_mollusc(requests=request_generator())
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(base="video", body=True, single=None)
            ]
        ),
        calling_form_enum=CallingForm,
        calling_form=CallingForm.RequestStreamingClient,
        transport="grpc-async",
    )


def test_render_request_params():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_request_params(request) }}

        """,
        """
        mollusc, length_meters=16, order='TEUTHIDA'
        """,
        request=[
            samplegen.TransformedRequest(
                base="length_meters",
                body=None,
                single=samplegen.AttributeRequestSetup(value="16"),
            ),
            samplegen.TransformedRequest(
                base="mollusc",
                body=[
                    samplegen.AttributeRequestSetup(
                        field="video", value="path/to/video.mkv"
                    ),
                    samplegen.AttributeRequestSetup(
                        field="audio", value="path/to/audio.ogg"
                    ),
                ],
                single=None,
            ),
            samplegen.TransformedRequest(
                base="order",
                body=None,
                single=samplegen.AttributeRequestSetup(value="'TEUTHIDA'"),
            ),
        ],
    )


def test_main_block():
    check_template(
        """
        {% import "feature_fragments.j2" as frags %}
        {{ frags.render_main_block({"rpc": "ListMolluscs", "is_internal": False},
                                   request) }}
        """,
        """
        def main():
            import argparse

            parser = argparse.ArgumentParser()
            parser.add_argument("--order",
                                type=str,
                                default='coleoidea')
            parser.add_argument("--mass",
                                type=str,
                                default='60kg')
            args = parser.parse_args()

            sample_list_molluscs(args.order, args.mass)


        if __name__ == "__main__":
            main()
        """,
        request=samplegen.FullRequest(
            request_list=[
                samplegen.TransformedRequest(
                    base="input_params",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="list_molluscs.order",
                            value="'coleoidea'",
                            input_parameter="order",
                        ),
                        samplegen.AttributeRequestSetup(
                            field="list_molluscs.mass",
                            value="'60kg'",
                            input_parameter="mass",
                        ),
                    ],
                    single=None,
                ),
                samplegen.TransformedRequest(
                    base="enum_param",
                    body=[
                        samplegen.AttributeRequestSetup(
                            field="list_molluscs.zone", value="MESOPELAGIC"
                        )
                    ],
                    single=None,
                ),
            ]
        ),
    )
