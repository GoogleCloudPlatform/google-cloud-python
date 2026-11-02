def _pandoc_binary_impl(ctx):
    toolchain = ctx.toolchains["@gapic_generator_python//:pandoc_toolchain_type"]
    output = ctx.actions.declare_file(ctx.attr.binary_name)

    script = """
    cp {input} {output}
    chmod +x {output}
    """.format(
        input = toolchain.pandoc.files.to_list()[0].path,
        output = output.path,
    )
    ctx.actions.run_shell(
        command = script,
        inputs = toolchain.pandoc.files,
        outputs = [output],
    )
    return [DefaultInfo(files = depset(direct = [output]), executable = output)]

pandoc_binary = rule(
    attrs = {
        "binary_name": attr.string(default = "pandoc")
    },
    executable = True,
    toolchains = ["@gapic_generator_python//:pandoc_toolchain_type"],
    implementation = _pandoc_binary_impl,
)

#
# Toolchains
#
def _pandoc_toolchain_info_impl(ctx):
    return [
        platform_common.ToolchainInfo(
            pandoc = ctx.attr.pandoc,
        ),
    ]

_pandoc_toolchain_info = rule(
    attrs = {
        "pandoc": attr.label(
            allow_single_file = True,
            cfg = "host",
            executable = True,
        ),
    },
    implementation = _pandoc_toolchain_info_impl,
)

def pandoc_toolchain(platform, exec_compatible_with):
    toolchain_info_name = "pandoc_toolchain_info_%s" % platform
    _pandoc_toolchain_info(
        name = toolchain_info_name,
        pandoc = "@pandoc_%s//:pandoc" % platform,
        visibility = ["//visibility:public"],
    )

    native.toolchain(
        name = "pandoc_toolchain_%s" % platform,
        exec_compatible_with = exec_compatible_with,
        toolchain = toolchain_info_name,
        toolchain_type = ":pandoc_toolchain_type",
    )
