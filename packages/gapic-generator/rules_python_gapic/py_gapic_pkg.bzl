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

load("@rules_gapic//:gapic_pkg.bzl", "construct_package_dir_paths")

def _py_gapic_src_pkg_impl(ctx):
    srcjar_srcs = []
    dir_srcs = []
    py_srcs = []
    for dep in ctx.attr.deps:
        # Check if this is a `proto_library` dependency which has `ProtoInfo`
        # See https://bazel.build/versions/6.5.0/rules/lib/ProtoInfo
        if ProtoInfo in dep:
            # Add `*.proto` files to the output which exist in `direct_sources`
            # https://bazel.build/versions/6.5.0/rules/lib/ProtoInfo#direct_sources
            for source in dep[ProtoInfo].direct_sources:
                py_srcs.append(source)
        for f in dep.files.to_list():
            if f.is_directory:
                dir_srcs.append(f)
            elif f.extension in ("srcjar", "jar", "zip"):
                srcjar_srcs.append(f)
            # Exclude source files and files for external packages
            elif f.extension in ("py", "pyi") and not f.is_source and 'external' not in f.path:
                py_srcs.append(f)

    paths = construct_package_dir_paths(ctx.attr.package_dir, ctx.outputs.pkg, ctx.label.name)

    script = """
    mkdir -p {package_dir_path}
    for srcjar_src in {srcjar_srcs}; do
        unzip -q -o $srcjar_src -d {package_dir_path}
    done
    for dir_src in {dir_srcs}; do
        cp -rT -L $dir_src {package_dir_path}
    done
    for py_src in {py_srcs}; do
        cp $py_src {package_dir_path}
    done
    # Replace 555 (forced by Bazel) permissions with 644
    find {package_dir_path} -type f -exec chmod 644 {{}} \\;
    cd {package_dir_path}/..
    tar -zchpf {package_dir}/{package_dir}.tar.gz {package_dir}
    cd -
    mv {package_dir_path}/{package_dir}.tar.gz {pkg}
    rm -rf {package_dir_path}
    """.format(
        srcjar_srcs = " ".join(["'%s'" % f.path for f in srcjar_srcs]),
        dir_srcs = " ".join(["'%s'" % f.path for f in dir_srcs]),
        py_srcs =  " ".join(["'%s'" % f.path for f in py_srcs]),
        package_dir_path = paths.package_dir_path,
        package_dir = paths.package_dir,
        pkg = ctx.outputs.pkg.path,
        package_dir_expr = paths.package_dir_expr,
    )

    ctx.actions.run_shell(
        inputs = srcjar_srcs + dir_srcs + py_srcs,
        command = script,
        outputs = [ctx.outputs.pkg],
    )

_py_gapic_src_pkg = rule(
    attrs = {
        "deps": attr.label_list(allow_files = True, mandatory = True),
        "package_dir": attr.string(mandatory = True),
    },
    outputs = {"pkg": "%{name}.tar.gz"},
    implementation = _py_gapic_src_pkg_impl,
)

def py_gapic_assembly_pkg(name, deps, assembly_name = None, **kwargs):
    package_dir = name
    if assembly_name:
        package_dir = "%s-%s" % (assembly_name, name)
    _py_gapic_src_pkg(
        name = name,
        deps = deps,
        package_dir = package_dir,
        **kwargs
    )
