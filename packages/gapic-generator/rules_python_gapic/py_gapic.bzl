# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load("@rules_gapic//:gapic.bzl", "proto_custom_library", "unzipped_srcjar", "CustomProtoInfo")
load("@rules_python//python:defs.bzl", "py_library")
load("@gapic_generator_python_pip_deps//:requirements.bzl", "requirement")

# Load modern rules_proto Starlark ProtoInfo provider.
# Needed because modern rules_proto targets output Starlark ProtoInfo, whereas
# rules_gapic's proto_custom_library expects rules_gapic's CustomProtoInfo provider.
load("@rules_proto//proto:defs.bzl", StarlarkProtoInfo = "ProtoInfo")

# Compatibility adapter rule to convert modern rules_proto Starlark ProtoInfo
# into rules_gapic CustomProtoInfo provider required by proto_custom_library.
def _gapic_compat_proto_library_impl(ctx):
    dep = ctx.attr.dep
    if CustomProtoInfo in dep:
        return [
            dep[DefaultInfo],
            dep[CustomProtoInfo],
        ]
    starlark_proto = dep[StarlarkProtoInfo]
    return [
        dep[DefaultInfo],
        # Construct CustomProtoInfo provider needed by rules_gapic's proto_custom_library.
        # Must not return ProtoInfo here so proto_custom_library selects CustomProtoInfo (which has transitive_imports).
        CustomProtoInfo(
            direct_sources = starlark_proto.direct_sources,
            check_deps_sources = starlark_proto.check_deps_sources,
            # Map modern transitive_sources to CustomProtoInfo's transitive_imports field
            transitive_imports = starlark_proto.transitive_sources,
        ),
    ]

gapic_compat_proto_library = rule(
    implementation = _gapic_compat_proto_library_impl,
    attrs = {
        "dep": attr.label(mandatory = True, providers = [[StarlarkProtoInfo], [CustomProtoInfo]]),
    }
)

def _gapic_test_file_impl(ctx):
    generated_test_file = ctx.actions.declare_file(ctx.label.name)

    ctx.actions.expand_template(
        template = ctx.attr.template.files.to_list()[0],
        output = generated_test_file,
        substitutions = {},
    )

    return [DefaultInfo(files = depset(direct = [generated_test_file]))]

gapic_test_file = rule(
    _gapic_test_file_impl,
    attrs = {
        "template": attr.label(allow_files = True),
    },
)

def py_gapic_library(
        name,
        srcs,
        grpc_service_config = None,
        plugin_args = None,
        opt_args = None,
        metadata = True,
        service_yaml = None,
        transport = None,
        rest_numeric_enums = False,
        deps = [],
        **kwargs):

    # We extract and propagate 'testonly' and 'tags' from kwargs to prevent Bazel dependency analysis
    # errors and ensure wildcard builds (e.g. manual tags) behave correctly.
    testonly = kwargs.get("testonly", False)
    tags = kwargs.get("tags", [])
    compat_srcs = []
    for i, src in enumerate(srcs):
        compat_name = "%s_compat_src_%d" % (name, i)
        gapic_compat_proto_library(
            name = compat_name,
            dep = src,
            testonly = testonly,
            tags = tags,
        )
        compat_srcs.append(":%s" % compat_name)

    srcjar_target_name = "%s_srcjar" % name
    srcjar_output_suffix = ".srcjar"

    plugin_args = plugin_args or []
    opt_args = opt_args or []

    if metadata:
        plugin_args.append("metadata")

    file_args = {}
    if grpc_service_config:
        file_args[grpc_service_config] = "retry-config"
    if service_yaml:
        file_args[service_yaml] = "service-yaml"

    if transport:
        opt_args = opt_args + ["transport=%s" % transport]

    if rest_numeric_enums:
        opt_args = opt_args + ["rest-numeric-enums"]

    # Point deps to compat_srcs so proto_custom_library receives targets providing
    # the CustomProtoInfo provider instead of raw Starlark ProtoInfo targets.
    proto_custom_library(
        name = srcjar_target_name,
        deps = compat_srcs,
        plugin = Label("@gapic_generator_python//:gapic_plugin"),
        plugin_args = plugin_args,
        plugin_file_args = file_args,
        opt_args = opt_args,
        output_type = "python_gapic",
        output_suffix = srcjar_output_suffix,
        **kwargs
    )

    main_file = "%s" % srcjar_target_name + srcjar_output_suffix
    main_dir = "%s.py" % srcjar_target_name

    unzipped_srcjar(
        name = main_dir,
        srcjar = ":%s" % main_file,
    )

    actual_deps = deps + [
        "@com_github_grpc_grpc//src/python/grpcio/grpc:grpcio",
        requirement("protobuf"),
        requirement("proto-plus"),
        requirement("google-api-core"),
        requirement("googleapis-common-protos"),
        requirement("pytest-asyncio"),
        requirement("aiohttp")
    ]

    py_library(
        name = name,
        srcs = [":%s" % main_dir],
        deps = actual_deps,
    )

    test_file_target_name = "%s_test.py" % name

    gapic_test_file(
        name = test_file_target_name,
        template = Label("//rules_python_gapic:test.py"),
    )

    test_runner_file_target_name = "%s_pytest.py" % name

    gapic_test_file(
        name = test_runner_file_target_name,
        template = Label("//rules_python_gapic:pytest.py"),
    )
